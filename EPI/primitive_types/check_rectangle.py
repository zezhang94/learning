import collections
import unittest
# Given four points in the plane, 
# how would you check if they are the vertices of a rectangle?
Point = collections.namedtuple('Point', ('x', 'y'))
def check_rectangle(P1, P2, P3, P4):
  P1, P2, P3, P4 = rotate_points([P1, P2, P3, P4])
  print(P1, P2, P3, P4)
  if check_vertical(P1, P2, P3) and \
    check_vertical(P2, P3, P4) and \
    check_vertical(P3, P4, P1):
    return True
  return False

def rotate_points(p):
  for i in range(0, 4):
    min_index = i
    for j in range(i + 1, 4):
      if p[min_index].x > p[j].x:
        min_index = j
        j += 1
    p[i], p[min_index] = p[min_index], p[i]
    i += 1
  if p[0].x == p[1].x and p[0].y > p[1].y:
    p[0], p[1] = p[1], p[0]
  if p[2].x == p[3].x and p[2].y > p[3].y:
    p[2], p[3] = p[3], p[2]
  p[2], p[3] = p[3], p[2]
  return p

def check_vertical(P1, P2, P3):
  if P1.x == P2.x and P2.x == P3.x or \
    P1.y == P2.y and P2.y == P3.y:
    return False
  if P1.x == P2.x and P2.y == P3.y or \
    P1.y == P2.y and P2.x == P3.x:
    return True
  K12 = (P1.x - P2.x) / (P1.y - P2.y)
  K23 = (P3.x - P2.x) / (P3.y - P2.y)
  if K12 * K23 == -1:
    return True
  return False

class Test(unittest.TestCase):
    def test(self):
        P1 = Point(x = 1, y = 1)
        P2 = Point(x = 0, y = 1)
        P3 = Point(x = 1, y = 0)
        P4 = Point(x = 0, y = 0)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), True)
        P1 = Point(x = 1, y = 1)
        P2 = Point(x = 0, y = 1)
        P3 = Point(x = 0, y = 0)
        P4 = Point(x = 1, y = 2)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), False)
        P1 = Point(x = 1, y = 0)
        P2 = Point(x = 0, y = 1)
        P3 = Point(x = -1, y = 0)
        P4 = Point(x = 0, y = -1)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), True)
        P1 = Point(x = 1, y = 0)
        P2 = Point(x = 0, y = 1)
        P3 = Point(x = -1, y = 0)
        P4 = Point(x = 0, y = -1)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), True)
        P1 = Point(x = 1, y = 0)
        P2 = Point(x = 0, y = 1)
        P3 = Point(x = -1, y = 0)
        P4 = Point(x = 0, y = -1)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), True)
        P1 = Point(x = 1, y = 3)
        P2 = Point(x = 0, y = 1)
        P3 = Point(x = 3, y = 2)
        P4 = Point(x = 2, y = 0)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), True)
        P1 = Point(x = 1, y = 3)
        P2 = Point(x = 1, y = 1)
        P3 = Point(x = 1, y = 2)
        P4 = Point(x = 1, y = 0)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), False)
        P1 = Point(x = 1, y = 3)
        P2 = Point(x = 1, y = 1)
        P3 = Point(x = 1, y = 2)
        P4 = Point(x = 2, y = 1)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), False)
        P1 = Point(x = 1, y = 1)
        P2 = Point(x = 2, y = 1)
        P3 = Point(x = 4, y = 1)
        P4 = Point(x = 2, y = 1)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), False)
        P1 = Point(x = 1, y = 1)
        P2 = Point(x = 2, y = 2)
        P3 = Point(x = 4, y = 1)
        P4 = Point(x = 2, y = 1)
        self.assertEqual(check_rectangle(P1, P2, P3, P4), False)



