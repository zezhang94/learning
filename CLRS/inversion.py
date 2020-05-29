import unittest
import random
import copy

def insertion_sort(A):
  count = 0
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i > -1 and A[i] > key:
      A[i + 1] = A[i]
      count += 1
      i -= 1
    A[i + 1] = key
  return count

def merge(A, p, q, r):
  c = 0
  B = [None] * (r - p + 1)
  i, j, count = p, q + 1, 0
  while i <= q and j <= r:
    if A[i] <= A[j]:
      B[count] = A[i]
      i += 1
    else:
      B[count] = A[j]
      c += j - count - p
      j += 1
    count += 1
  while i <= q:
    B[count] = A[i]
    i += 1
    count += 1
  while j <= r:
    B[count] = A[j]
    j += 1
    count += 1
  A[p:(r + 1)] = B
  return c
  

def merge_sort(A, p, r):
  if p < r:
    q = (p + r) // 2
    left = merge_sort(A, p, q)
    right = merge_sort(A, q + 1, r)
    return merge(A, p, q, r) + left + right
  return 0

class Test(unittest.TestCase):
    def test(self):
        for i in range(100):
            len = random.randint(0, 100)
            A = [random.randint(0, 50) for x in range(len)]
            self.assertEqual(insertion_sort(copy.copy(A)), merge_sort(A, 0, len - 1))
    
    
    