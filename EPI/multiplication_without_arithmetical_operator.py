import unittest

# Write a program that multiplies two nonnegative integers. 
# The only operators you are allowed to use are 
#   assignment,
#   the bitwise operators >>, <<, |, &, ~, ^ and
#   equality checks and Boolean combinations thereof.

# Attention: Be clear of variables meaning。
#            Move bit flexibly
def add(x, y):
    mask, value, carry, result = 1, 0, 0, 0
    cx, cy = x, y
    while cx or cy:
        x0, y0 = x & mask, y & mask
        value = x0 ^ y0 ^ carry
        # two or more 1 will carry
        carry = (x0 & carry) | (x0 & y0) | (y0 & carry)
        mask, cx, cy, carry, result = mask << 1, cx >> 1, cy >> 1, carry << 1, result | value
    return result | carry
        
def multiple(x, y):
    result = 0
    while y:
        y0 = y & 1
        if y0 == 1:
            result = add(result, x)
        x, y = x << 1, y >> 1
    return result
        

class Test(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(multiple(5, 6), 30)
        self.assertEqual(multiple(8, 8), 64)
        self.assertEqual(multiple(15, 15), 225)
        self.assertEqual(multiple(32768, 65535), 2147450880)
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(8, 4), 12)
        self.assertEqual(add(7, 15), 22)

