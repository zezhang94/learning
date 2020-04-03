import unittest
import random
# Write a program that takes a double x and an integer y and retums x^y. 
# You can ignore overflow and underflow.
def exponet(x, y):
    result = 1
    while y:
        result *= x
        y -= 1
    return result

# x ^ y = x ^ (y0 + y1 + ... + yk), yk is 2's exponent
def exponet_fast(x, y):
    x_power = x
    if y < 0:
        x, y = 1.0 / x, -y
    result = 1.0
    while y > 0:
        if y & 1 == 1:
            result *= x_power
            y &= ~1
        else:
            x_power *= x_power
            y >>= 1
        # elegant
        # if y & 1:
        #     result *= x_power
        # x_power, y = x_power * x_power, y >> 1
    return result

class Test(unittest.TestCase):
    def test_exponet(self):
        for i in range(50):
            x = random.random()
            y = random.randint(0, 10)
            self.assertEqual(exponet_fast(x, y), pow(x, y))