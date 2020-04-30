import unittest

# Write a program which takes as input a sorted array and updates it so that 
# all duplicates have been removed and the remaining elements have been shifted left to 
# fill the emptied indices. Return the number of valid elements.
def delete_duplicates(A):
  ci, value, i = 0, A[0], 0
  while i < len(A):
    if A[i] != value:
      value = A[i]
      ci += 1
      A[ci] = value
    if A[i] == value and i != ci:
      A[i] = 0
    i += 1 
  return (ci + 1, A)

# Implement a function which takes as input an array and a key, 
# and updates the array so that all occurrences of the input key have been removed 
# and the remaining elements have been shifted left to fill the emptied indices. 
# Return the number of remaining elements. 
# There are no requirements as to the values stored beyond the last valid element.
def variant1(k, A):
  i, c = 0, 0
  for i in range(0, len(A)):
    if A[c] != k:
      c += 1
    elif A[c] == k and A[i] != k:
      A[c] = A[i]
      A[i] = k
      c += 1
  print(A)
  return c

# Write a program which takes as input a sorted atay A of integers 
# and a positive integer m, and updates A so that 
# if x appears m times in A it appears exactly min(2,m) times in A. 
# The update to A should be performed in one pass, 
# and no additional storage may be allocated.


class Test(unittest.TestCase):
    def test(self):
      A = [1, 1, 2, 2]
      B = delete_duplicates(A)
      self.assertEqual(B[0], 2)
      self.assertListEqual(B[1], [1, 2, 0, 0])
      A = [2, 3, 5, 5, 7, 11, 11, 11, 13]
      B = delete_duplicates(A)
      self.assertEqual(B[0], 6)
      self.assertListEqual(B[1], [2, 3, 5, 7, 11, 13, 0, 0, 0])
      A = [1, 1, 2, 2]
      B = delete_duplicates(A)
      self.assertEqual(B[0], 2)
      self.assertListEqual(B[1], [1, 2, 0, 0])
      A = [2, 3, 5, 7, 11, 13]
      B = delete_duplicates(A)
      self.assertEqual(B[0], 6)
      self.assertListEqual(B[1], [2, 3, 5, 7, 11, 13])
      A = [1, 1, 1, 1, 1, 1]
      B = delete_duplicates(A)
      self.assertEqual(B[0], 1)
      self.assertListEqual(B[1], [1, 0, 0, 0, 0, 0])
      
    def test_variant1(self):
      self.assertEqual(5, variant1(1, [1, 2, 3, 4, 5, 6]))
      self.assertEqual(5, variant1(4, [1, 2, 3, 4, 5, 6]))
      self.assertEqual(6, variant1(-1, [1, 1, 1, 2, 2, 2]))
      self.assertEqual(3, variant1(1, [1, 1, 1, 2, 2, 2]))
      self.assertEqual(6, variant1(2, [1, 1, 1, 2, 2, 2, 3, 3, 3]))
      self.assertEqual(5, variant1(2, [2, 1, 2, 2, 3, 2, 3, 1, 3]))





