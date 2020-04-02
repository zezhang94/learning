import unittest

# Write a program that multiplies two nonnegative integers. 
# The only operators you are allowed to use are 
#   assignment,
#   the bitwise operators >>, <<, |, &, ~, ^ and
#   equality checks and Boolean combinations thereof.
def multiple(x, y):
    return x * y

def add(x, y):
    return x + y
        

class Test(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(multiple(5, 6), 30)
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(8, 4), 12)
        self.assertEqual(add(7, 15), 22)

