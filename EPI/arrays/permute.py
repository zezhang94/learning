import copy
import unittest
import math
import random
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

# Write a program that takes as input a permutation, 
# and returns the next permutation under dictionary ordering. 
# If the permutation is the last permutation, return the empty array.
#
# Hint: observe extreme
def next(A):
  start = -1
  # Find the longest decreasing suffix.
  for i in range(len(A) - 1, 0, -1):
    if A[i] > A[i - 1]:
      start = i - 1
      break
  if start == -1:
    return []
  # Observe that e must be less than some entries in the suffix 
  # (since the entry immediately after e is greater than e). 
  # Intuitively, we should swap e with the smallest entry s in the suffix which is larger 
  # than e so as to minimize the change to the prefix 
  # (which is defined to be the part of the sequence that appears before the suffix).
  for i in range(len(A) - 1, start, -1):
    if A[i] > A[start]:
      A[i], A[start] = A[start], A[i]
      break
  # Reverse suffix.
  return A[:(start + 1)] + A[:start:-1]

# Compute the k-th permutation under dictionary ordering, 
# starting from the identity permutation 
# (which is the first permutation in dictionary ordering).
def k_th_permutation(n, k):
  i, k = 1, k - 1 
  R, F, fac = [], [x for x in range(1, n + 1)], math.factorial(n - i)
  while k // fac or k % fac:
    v = k // fac
    R.append(F[v])
    k = k % fac
    F = F[:v] + F[v + 1:]
    i += 1
    fac = math.factorial(n - i)
  return R + F 

# Given a permutation p, return the permutation corresponding to the 
# previous permutation of p under dictionary ordering.
def previous(A):
  start = -1
  for i in range(len(A) - 1, 0, -1):
    if A[i] < A[i - 1]:
      start = i - 1
      break
  if start == -1:
    return []
  for i in range(len(A) - 1, start, -1):
    if A[i] < A[start]:
      A[i], A[start] = A[start], A[i]
      break
  return A[:start + 1] + A[:start:-1]



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
    def test_next(self):
        self.assertListEqual(next([1, 0, 3, 2]), [1, 2, 0, 3])
        self.assertListEqual(next([4, 5, 3, 2, 1, 0]), [5, 0, 1, 2, 3, 4])
        self.assertListEqual(next([5, 4, 3, 2, 1, 0]), [])
        for i in range(0, 100):
            current = random.randint(1, math.factorial(6) + 1)
            A = k_th_permutation(6, current)
            if current == math.factorial(6):
                self.assertListEqual(next(A), [])
            else:
                self.assertListEqual(next(A), k_th_permutation(6, current + 1))      
    def test_previous(self):
        for i in range(0, 100):
            current = random.randint(1, math.factorial(6) + 1)
            A = k_th_permutation(6, current)
            if current == 1:
                self.assertListEqual(previous(A), [])
            else:
                self.assertListEqual(previous(A), k_th_permutation(6, current - 1))
        self.assertListEqual(previous([0, 1, 2, 3]), [])
        self.assertListEqual(previous([0, 1]), [])

if __name__ == "__main__":
    for i in range(1, math.factorial(6) + 1):
      A = k_th_permutation(6, i)
      print(A)
    