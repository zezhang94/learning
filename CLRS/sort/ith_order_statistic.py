import random
import unittest
import copy

def ith_order_statistic(A, p, r, i):
  if p == r:
    return A[p]
  q = randomized_partition(A, p, r)
  k = q - p + 1
  if i == k:
    return A[i]
  if i < k:
    return ith_order_statistic(A, p, q - 1, i)
  else:
    return ith_order_statistic(A, q + 1, r, i - k)    

def partition(A, p, r):
  i, j, pivot_value = p, p - 1, A[r]
  while i <= r - 1:
    if A[i] < pivot_value:
      j += 1
      A[i], A[j] = A[j], A[i]
    i += 1
  pivot = j + 1
  A[pivot], A[r] = pivot_value, A[pivot]
  return pivot

def randomized_partition(A, p, r):
  i = random.randint(p, r)
  A[i], A[r] = A[r], A[i]
  return partition(A, p, r)

class Test(unittest.TestCase):
    def test(self):
        for i in range(0, 1000):
            A = random.sample(range(0, 100), 15)
            B = sorted(A)
            j = random.randint(1, len(A))
            print(j, A, B)
            self.assertEqual(ith_order_statistic(A, 0, len(A) - 1, j), B[j - 1])