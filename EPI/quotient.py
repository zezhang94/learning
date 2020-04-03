import unittest
import random
import sys
# Given two positive integers, compute their quotient, using only the addition, 
# subtraction, and shifting operators.
def quotient(x, y):
    result = 0
    while x >= y:
        x = x - y
        result += 1
    return result

def quotient_by_two_index(x, y):
    temp_y, result = y, 0
    while x >= y:
        k = 1
        while (temp_y << 1) < x:
            temp_y <<= 1
            k <<= 1
        x, result, temp_y = x - temp_y, result + k, y
    return result

def quotient_fast(x, y):
    result, shift = 0, 32
    temp = y << shift
    while x >= y:
        while temp > x:
            temp >>= 1
            shift -= 1
        x -= temp
        result += 1 << shift
    return result

class Test(unittest.TestCase):
    def test_devide(self):
        self.assertEqual(quotient_fast(6, 5), 1)
        self.assertEqual(quotient_fast(100, 2), 50)
        self.assertEqual(quotient_fast(43895345, 321), 43895345 // 321)
        self.assertEqual(quotient_fast(pow(2, 31), 2), pow(2, 31) // 2)
        self.assertEqual(quotient_fast(65535, 65535), 1)
        self.assertEqual(quotient_fast(65535, 255), 65535 / 255)
        for i in range(1000):
            x = random.randint(0, sys.maxsize)
            y = random.randint(1, x)
            self.assertEqual(quotient_fast(x, y), x // y)
