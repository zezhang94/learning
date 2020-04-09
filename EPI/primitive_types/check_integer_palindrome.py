import unittest
import math

# Write a Program that takes an integer and determines 
# if that integer's representation as a decimal string is a palindrome.
def check_interger_palandrome(x):
  if x < 0:
    return False
  temp_x, most = x, 0
  while temp_x:
    temp_x //= 10
    most += 1
  while x > 10:
    most_d, least_d = x // pow(10, most - 1), x % 10
    if most_d != least_d:
      return False
    x, most = (x - most_d * pow(10, most - 1)) // 10, most - 2
  return True

def check_interger_palandrome_elegant(x):
  if x < 0:
    return False
  n = math.floor(math.log10(x)) + 1
  most = 10 ** (n - 1)
  while x > 10:
    if x % 10 != x // most:
      return False
    x = x // 10 % (most * x // most)
    most //= 100
  return True



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_interger_palandrome(2147447412), True)
        self.assertEqual(check_interger_palandrome(333), True)
        self.assertEqual(check_interger_palandrome(121), True)
        self.assertEqual(check_interger_palandrome(2147483647), False)
    def test_elegant(self):
        self.assertEqual(check_interger_palandrome(2147447412), True)
        self.assertEqual(check_interger_palandrome(333), True)
        self.assertEqual(check_interger_palandrome(121), True)
        self.assertEqual(check_interger_palandrome(2147483647), False)

    