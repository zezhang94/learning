import unittest
import random
import copy

# Write a program that takes an array A of n numbers, 
# and rearranges A's elements to get a new array B having the property that
# B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ....
def altenation(A):
  d = 1
  for i in range(0, len(A) - 1):
    if (A[i + 1] - A[i]) * d < 0:
      A[i], A[i + 1] = A[i + 1], A[i]
    d *= -1
  return A

def rearrange(A):
  for i in range(len(A)):
    A[i : i + 2] = sorted(A[i  :i + 2], reverse = i % 2)
  return A

class Test(unittest.TestCase):
    def test(self):
        for i in range(50):
            A = random.sample(range(1, 100), random.randint(1, 30)) + random.sample(range(1, 100), random.randint(1, 30))
            B = copy.copy(A)
            self.assertListEqual(rearrange(A), altenation(A))
