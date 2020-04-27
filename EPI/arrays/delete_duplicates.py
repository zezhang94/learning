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




