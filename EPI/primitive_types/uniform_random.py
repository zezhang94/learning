import unittest
import time
import math
import random

def binary_random():
    return random.randint(0, 1)

def random_generator(a, b):
  diff = b - a + 1
  n = math.floor(math.log2(diff)) + 1
  result = 2 ** n
  while result >= diff:
    result = 0
    time = n
    while time:
      result = result << 1 | binary_random()
      time -= 1
  return result + a

# test 
def main():
    a, b = 1, 5
    arr = [0] * (b - a + 1)
    count = 10000000
    while count > 0:
        r = random_generator(a, b)
        #print(r)
        arr[r - 1] += 1
        count -= 1
    print(arr)

if __name__ == '__main__':
    main()
