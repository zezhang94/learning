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

# Given an affay A of integers representing a permutation, 
# update A to represent the inverse permutation using only constant additional storage.
# 
# An inverse permutation is a permutation in which each number and 
# the number of the place which it occupies are exchanged.


class Test(unittest.TestCase):
    def test(self):
        self.assertListEqual(optimize(["a", "b", "c", "d"]), ["b", "c", "a", "d"])
        self.assertListEqual(permute(["a", "b", "c", "d"]), ["b", "c", "a", "d"])

