import copy
import unittest
# A permutation can be specified by an array P, where P[] represents the location of the element 
# at i in the permutation. For example, the aray (2,0,1,3) represents the permutation that maps the
# element at location 0 to location 2, the element at location 1 to location 0, 
# the element at location 2 to location 1, and keep the element at location 3 unchanged. 
# A permutation can be applied to an array to reorder the array. 
# For example, the permutation (2,0,1,3) applied to A = (a,b,c,d) yields the array (b,c,a,d).

def permute(A, P):
  F = [True] * len(A)
  for i in range(len(A)):
    j, value = P[i], A[i]
    while F[j]:
      temp, A[j], F[j] = A[j], value, False
      value, j  = temp, P[j]
  return A

# No additional space.
# Caution: status change
def optimize(A, P):
  for i in range(len(A)):
    j, value = i, A[i]
    while P[j] >= 0 and P[j] != j:
      target = P[j]
      if j != i:
        P[j] = -1
      temp, A[target] = A[target], value
      value, j = temp, target
  return A

# Given an array A of integers representing a permutation, 
# update A to represent the inverse permutation using only constant additional storage.
# 
# An inverse permutation is a permutation in which each number and 
# the number of the place which it occupies are exchanged.
def variant(A):
  for i in range(len(A)):
    A[i] -= 1
  l = len(A)
  for i in range(len(A)):
    value, index = i, A[i]
    while index >= 0:
       temp = A[index]
       A[index] = value - l
       value = index
       index = temp
  for i in range(len(A)):
    A[i] += (l + 1)
  return A

class Test(unittest.TestCase):
    def test(self):
        self.assertListEqual(optimize(["a", "b", "c", "d"], [2, 0, 1, 3]), ["b", "c", "a", "d"])
        self.assertListEqual(permute(["a", "b", "c", "d"], [2, 0, 1, 3]), ["b", "c", "a", "d"])
    def test_variant(self):
        self.assertListEqual(variant([1, 2, 3]), [1, 2, 3])
        self.assertListEqual(variant([3, 8, 5, 10, 9, 4, 6, 1, 7, 2]), [8, 10, 1, 6, 3, 7, 9, 2, 5, 4])
        self.assertListEqual(variant([3 ,2, 1]), [3, 2, 1])
        self.assertListEqual(variant([1 ,4, 3, 2]), [1 ,4, 3, 2])
        self.assertListEqual(variant([2 ,3, 4, 5, 1]), [5, 1, 2, 3, 4])