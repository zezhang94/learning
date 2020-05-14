import unittest
import random

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

def buy_and_sell(A):
  min, p = A[0], 0
  for i in range(1, len(A)):
    if A[i] < min:
      min = A[i]
    if p < A[i] - min:
      p = A[i] - min
  return p

# Write a program that takes an array of integers and 
# finds the length of a longest subarray all of whose entries are equal.
def variant(A):
  pre, c, l = A[0], 0, 0
  for i in range(0, len(A)):
    if pre == A[i]:
      c += 1
    else:
      l = max(c, l)
      c = 1
    pre = A[i]
  return max(c, l)

# Write a program that computes the maximum profit that can be made by buying and selling a share at most twice. 
# The second buy must be made on another date after the first sale.
def twice(A):
  profit = 0
  for i in range(1, len(A)):
    profit = max(profit, buy_and_sell(A[:i]) + buy_and_sell(A[i:]))
  return profit

# hint: 
# The inefficiency in the above approaches comes from not taking advantage of previous computations. 
# Suppose we record the best solution for A[0, j], j between 1, and n - 1, inclusive. 
# Now we can do a reverse iteration, computing the best solution for a single buy-and-sell for A[j, n - 1], 
# j between i and n - 1, inclusive. For each day, we combine this result with the result from the forward iteration for the previous day-
# this yields the maximum profit if we buy and sell once before the current day and once at or after the current day.
def twice_better(A):
  current, SELL = A[0], [0]
  for x in A:
    SELL.append(max(x - current, SELL[len(SELL) - 1]))
    current = min(current, x)
  current, BUY = A[len(A) - 1], [0]
  SELL = SELL[1:]
  for x in reversed(A):
    BUY = [(max(current - x, BUY[0]))] + BUY
    current = max(current, x)
  BUY = BUY[:(len(BUY) - 1)]
  profit = 0
  for i in range(1, len(A) - 1):
    profit = max(profit, SELL[i] + BUY[i + 1])
  return profit

# TODO O(n) time and O(1) space

class Test(unittest.TestCase):
    def test(self):
        A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        self.assertEqual(brute_force(A), buy_and_sell(A))
        A = [0, 5, 0, 20, 0, 10, 30, 0, 25, 20]
        self.assertEqual(brute_force(A), buy_and_sell(A))
        for i in range(0, 100):
            A = random.sample(range(10, 100), 10)
            self.assertEqual(brute_force(A), buy_and_sell(A))
    def test_variant(self):
        self.assertEqual(variant([1, 2, 3, 1, 1, 3, 3, 3, 1]), 3)
        self.assertEqual(variant([1, 1, 1, 1, 1, 1, 1, 1, 1]), 9)
        self.assertEqual(variant([1, 1, 2, 2]), 2)
        self.assertEqual(variant([1, 2, 2, 1]), 2)
        self.assertEqual(variant([1, 2, 3, 4]), 1)
    def test_twice(self):
        A = [12, 11, 13, 9, 12, 8, 14, 13, 15]
        self.assertEqual(twice_better(A), twice(A))
        A = [1, 2, 1, 2]
        self.assertEqual(twice_better(A), twice(A))
        for i in range(0, 100):
            A = random.sample(range(10, 100), 10)
            self.assertEqual(twice_better(A), twice(A))
