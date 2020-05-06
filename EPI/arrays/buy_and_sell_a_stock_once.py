import unittest

# Write a program that takes an array denoting the daily stock price, 
# and returns the maximum profit that could be made by buying and then selling one share of that stock. 
# There is no need to buy if no profit is possible.
def brute_force(A):
  max = 0
  for i in range(0, len(A) - 1):
    for j in range(i + 1, len(A)):
      if A[j] - A[i] > max:
        max = A[j] - A[i]
  return max

class Test(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(brute_force([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]), 30)
