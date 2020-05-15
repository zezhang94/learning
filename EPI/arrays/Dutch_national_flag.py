import unittest
import random
import copy

# Assuming that keys take one of three values, 
# reorder the array so that all objects with the same key appear together. 
# The order of the subarrays is not important.
def variant1(A):
  a, b, c = 0, 0, len(A) - 1
  while b <= c:
    if A[b] == 1:
      A[a], A[b] = A[b], A[a]
      a, b = a + 1, b + 1
    elif A[b] == 2:
      b += 1
    else:
      A[c], A[b] = A[b], A[c]
      c -= 1
  return A

# Given an array A of n objects with keys that takes one of four values, 
# reorder the array so that all objects that have the same key appear together.
def variant2(A):
  a, b, c, d = 0, 0, len(A) - 1, len(A) - 1
  while b <= c:
    if A[b] == 1:
      A[a], A[b] = A[b], A[a]
      a, b = a + 1, b + 1
    elif A[b] == 2:
      b += 1
    elif A[b] == 3:
      A[b], A[c] = A[c], A[b]
      c -= 1
    else:
      A[b], A[c] = A[c], A[b]
      A[c], A[d] = A[d], A[c]
      c, d = c - 1, d - 1 
  return A

# Given em array A of n objects with Boolean-valued keys, 
# reorder the array so that objects that have the key false appear first. 
# The relative ordering of objects with key true should not change.
def variant3(A):
  f, t = len(A) - 1, len(A) - 1
  while f > -1:
    if A[f][0] == True:
      A[t], A[f] = A[f], A[t]
      t, f = t - 1, f - 1
    else:
      f -= 1
  return A

if __name__ == "__main__":
    A = [(x, y) for x in [True, False] for y in range(0, 5)]
    #for i in range(0, 32):
    random.shuffle(A)
    print("source: ", A)
    print("result: ", variant3(A))
    print()
     
class Test(unittest.TestCase):
    def test_variant1(self):
        for i in range(0, 64):
            A = []
            for i in range(0, 32):
                A.append(random.choice([1, 2, 3]))
            B = copy.copy(A)
            B.sort()
            self.assertListEqual(variant1(A), B)
    def test_variant2(self):
        for i in range(0, 64):
            A = []
            for i in range(0, 32):
                A.append(random.choice([1, 2, 3, 4]))
            B = copy.copy(A)
            B.sort()
            self.assertListEqual(variant2(A), B)
        

