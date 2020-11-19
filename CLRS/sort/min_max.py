import random
import unittest

def min_max(A):
  if len(A) == 0:
    return (None, None)
  if len(A) == 1:
    return (A[0], A[0])

  result, i = (0, 0), -1
  if len(A) % 2 == 0: # have even elements 
    result = (min(A[0], A[1]), max(A[0], A[1]))
    i = 2
  else: # have odd elements
    result = (A[0], A[0])
    i = 1
  s, l = None, None
  while i < len(A):  
    if A[i] < A[i + 1]: # Compare once
      s, l = A[i], A[i + 1]
    else:
      s, l = A[i + 1], A[i]
    result = (min(s, result[0]), max(l, result[1])) # Compare twice
    i += 2
  return result

class Test(unittest.TestCase):
    def test(self):
        for i in range(1000):
            A = random.sample(range(0, 100), 15)
            self.assertEqual(min_max(A), (min(A), max(A)))
