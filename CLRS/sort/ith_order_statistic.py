import random
import unittest
import copy

def ith_order_statistic(A, p, r, i):
  """Find i-th element in array.

  Args:
    A: array to find
    p: start index
    r: end index plus 1
    i: i-th (form 1)
  """

  if p == r:
    return A[p]
  q = randomized_partition(A, p, r)
  if i - 1 < q:
    return ith_order_statistic(A, p, q - 1, i)
  if i - 1 > q:
    return ith_order_statistic(A, q + 1, r, i)
  return A[i - 1]

def ith_order_statistic_iterative(A, p, r, i):
    if p == r:
      return A[p]
    pivot = randomized_partition(A, p, r)
    while pivot != i - 1:
      if i - 1 < pivot:
        p, r = p, pivot - 1
      elif i - 1 > pivot:
        p, r = pivot + 1, r 
      pivot = randomized_partition(A, p, r)
    return A[i - 1]

def partition(A, p, r):
  i, j, pivot_value = p, p - 1, A[r]
  while i <= r - 1:
    if A[i] < pivot_value:
      j += 1
      A[i], A[j] = A[j], A[i]
    i += 1
  pivot = j + 1
  A[pivot], A[r] = A[r], A[pivot]
  return pivot

def randomized_partition(A, p, r):
  i = random.randint(p, r)
  A[i], A[r] = A[r], A[i]
  return partition(A, p, r)

class Test(unittest.TestCase):
    def test(self):
        for i in range(0, 10000):
            A = random.sample(range(0, 100), 15)
            B = sorted(A)
            j = random.randint(1, len(A))
            self.assertEqual(ith_order_statistic(A, 0, len(A) - 1, j), B[j - 1])
        for i in range(0, 10000):
            A = random.sample(range(0, 100), 15)
            B = sorted(A)
            j = random.randint(1, len(A))
            self.assertEqual(ith_order_statistic_iterative(A, 0, len(A) - 1, j), B[j - 1])