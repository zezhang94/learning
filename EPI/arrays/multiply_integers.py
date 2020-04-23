import unittest
import random

# Write a program that takes two arrays representing integers, 
# and returns an integer representing their product.
def multiply(X, Y):
  if len(X) == 1 and X[0] == 0 or len(Y) == 1 and X[0] == 0:
    return [0]
  R = [0] * (len(X) + len(Y))
  s = X[0] * Y[0] // abs(X[0] * Y[0])
  X[0], Y[0] = abs(X[0]), abs(Y[0])
  # Caution: Order and boundary
  for i in range(len(X) - 1, -1, -1):
    c = 0
    for j in range(len(Y) - 1, -1, -1):
      t = R[i + j + 1] + X[i] * Y[j] + c
      c, R[i + j + 1] = t // 10, t % 10
    R[i] = c
  if R[0] == 0:
      R.remove(R[0])
  R[0] *= s
  return R      

class test(unittest.TestCase):
    def test(self):
        for i in range(0, 65536):
            x, y = random.randint(-65536, 65535), random.randint(-65536, 65535)
            m = x * y
            X, Y, M = [], [], []
            # op1
            if x < 0:
                X = list(map(int, str(abs(x))))
                X[0] *= -1
            else:
                X = list(map(int, str((x))))
            # op2
            if y < 0:
                Y = list(map(int, str(abs(y))))
                Y[0] *= -1
            else:
                Y = list(map(int, str(y)))
            # product
            if m < 0:
                M = list(map(int, str(abs(m))))
                M[0] *= -1
            else:
                M = list(map(int, str(m)))
            self.assertListEqual(multiply(X, Y), M)
            
