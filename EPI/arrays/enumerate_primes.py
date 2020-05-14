import unittest
import random

# Write a program that takes an integer argument and returns all the primes 
# between 1 and that integer.

# Solution from book.
def primes(n):
  A, F = [], [False, False] + [True] * (n - 1)
  for i in range(2, n + 1):
    if F[i]:
      A.append(i)
      for j in range(i, n + 1, i):
        F[j] = False
  return A

# Sieving p's multiples from p^2 instead of p, since all numbers of the form kp, 
# where k < p have already been sieved out.
# TODO why?
def optimize(n):
  if n < 2:
    return []
  size = (n - 3) // 2 + 1
  A, F = [2], [True] * size
  for i in range(size):
    if F[i]:
      p = i * 2 + 3
      A.append(p)
      # Sieving from p^2, where p^2 = (4i^2 + 12i + 9). 
      # The index in F is (2i^2 + 6i + 3) because F[i] represents 2i + 3.
      for j in range(2 * (i ** 2) + 6 * i + 3, size, p):
        F[j] = False
  return A

class Test(unittest.TestCase):
    def test(self):
        for i in range(0, 50):
            n = random.randint(0, 2 ** 16)
            self.assertListEqual(primes(n), optimize(n))

