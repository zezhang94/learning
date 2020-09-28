import unittest
import random

def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

def dynamic_On_fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  f = [-1] * (n + 1)
  f[0] = 0
  f[1] = 1
  for i in range(2, n + 1):
    f[i] = f[i - 1] + f[i - 2]
  return f[n]

class test(unittest.TestCase):
    def test(self):
        for i in range(0, 100):
            n = random.randint(0, 30)
            self.assertEqual(fibonacci(n), dynamic_On_fibonacci(n))