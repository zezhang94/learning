import unittest
# Write a program which takes an integer and returns the integer 
# corresponding to the digits of the input written in reverse order.

def reverse(x):
    result, temp_x, digits = 0, x, 0
    while temp_x:
        temp_x //= 10
        digits += 1
    for i in range(1, digits + 1):
        result += x % pow(10, i) * pow(10, digits + 1 - i) + \
            x / pow(10, digits + 1 - i) * pow(10, i) 
    return result

def reverse_after_hints(x):
    result, temp_x = 0, abs(x)
    while x:
        result *= 10 
        result += x % 10
        x //= 10
    if x > 0:
        return result
    else:
        return -result         


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse(101), 101)
        self.assertEqual(reverse(-341), -143)
        self.assertEqual(reverse(1011111), 1111101)
    
    def test_hints(self):
        self.assertEqual(reverse_after_hints(101), 101)
        self.assertEqual(reverse_after_hints(-341), -143)
        self.assertEqual(reverse_after_hints(-123456789), -987654321)
        self.assertEqual(reverse_after_hints(1011111), 1111101)