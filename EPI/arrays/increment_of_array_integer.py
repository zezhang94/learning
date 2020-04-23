import unittest
import random

# Write a program which takes as input an array of digits encoding a nonnegative decimal integer D 
# and updates the array to represent the integer D + 1.
def increment(A):
  carry = 0
  for i in range(len(A) - 1, -1, -1):
    carry = (A[i] + 1) // 10
    A[i] = (A[i] + 1) % 10
    if carry == 0:
      break
  if carry == 1:
    A = [1] + A
  return A

# Write a program which takes as input two strings s and t of bits encoding binary numbers Bs, and Bt, respectively, 
# and refurns a new string of bits representing the number Bs + Bt.
def variant1(S, T):
  c = 0
  if len(T) < len(S):
      T, S = S, T
  d = len(T) - len(S)
  for i in range(len(T) - 1, -1, -1):
    if i - d >= 0:
      t = c + T[i] + S[i - d]
      c, T[i] = t // 2, t % 2 
    else:
      t = c + T[i]
      c, T[i] = t // 2, t % 2
      if c == 0:
        break
  if c == 1:
    T = [1] + T
  return T

class Test(unittest.TestCase):
    def test(self):
        test_case = [
            ("123456789", "123456790"), 
            ("99", "100"),
            ("21312356670", "21312356671"),
            ("999999999999999999999999999999999999999", "1000000000000000000000000000000000000000")
        ]
        for i in range(0, len(test_case)):
            self.assertListEqual(increment(list(map(int, test_case[i][0]))), list(map(int, test_case[i][1])))

    def test_variant1(self):
        for i in range(0, 16):
            x, y = random.randint(0, 65536), random.randint(0, 65536)
            self.assertListEqual(
                variant1(list(map(int, bin(x)[2:])), list(map(int, bin(y)[2:]))), 
                list(map(int, bin(x + y)[2:]))
            )


