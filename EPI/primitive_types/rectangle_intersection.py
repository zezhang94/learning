import collections
import unittest
# Write a program which tests if two rectangles have a nonempty intersection. 
# If the intersection is nonempty, return the rectangle formed by their intersection.

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))
def rectangle_intersection(R1, R2):
  if max(R1.x + R1.width, R2.x + R2.width) - min(R1.x, R2.x) > R1.width + R2.width or \
      max(R1.y + R1.height, R2.y + R2.height) - min(R1.y, R2.y) > R1.height + R2.height:
    return None
  xmin = max(R1.x, R2.x)
  xmax = min(R1.x + R1.width, R2.x + R2.width)
  ymin = max(R1.y, R2.y)
  ymax = min(R1.y + R1.height, R2.y + R2.height)
  if xmax == xmin or ymax == ymin:
    return None
  return Rectangle(x=xmin, y=ymin, width=xmax-xmin, height=ymax-ymin)

class Test(unittest.TestCase):
    def test(self):
        R1 = Rectangle(x=0, y=0, width=4, height=3)
        R2 = Rectangle(x=0, y=0, width=4, height=3)
        R3 = Rectangle(x=0, y=0, width=4, height=3)
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=0, y=0, width=3, height=2)
        R3 = Rectangle(x=0, y=0, width=3, height=2)
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=0, y=0, width=7, height=8)
        R3 = Rectangle(x=0, y=0, width=4, height=3)
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=4, y=3, width=7, height=8)
        R3 = None
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=4, y=0, width=3, height=1)
        R3 = None
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=0, y=3, width=3, height=1)
        R3 = None
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=1, y=1, width=2, height=1)
        R3 = Rectangle(x=1, y=1, width=2, height=1)
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=1, y=1, width=2, height=10)
        R3 = Rectangle(x=1, y=1, width=2, height=2)
        self.assertEqual(rectangle_intersection(R1, R2), R3)
        R2 = Rectangle(x=3, y=2, width=10, height=10)
        R3 = Rectangle(x=3, y=2, width=1, height=1)
        self.assertEqual(rectangle_intersection(R1, R2), R3)