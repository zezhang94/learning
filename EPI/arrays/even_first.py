import unittest

# Your input is an array of integers, 
# and you have to reorder its entries so that the even entries appear first. 
# You are required to solve it without allocating additional storage.

def reorder(A):
  i, even, odd = 0, 0, len(A) - 1
  while even < odd:
    if A[i] % 2:
      A[i], A[odd] = A[odd], A[i]
      odd -= 1
    else:
      A[i], A[even] = A[even], A[i]
      i += 1
      even += 1
  return A

# elegant
def reorder_elegant(A):
    even, odd = 0, len(A) - 1
    while even < odd:
        if A[even] % 2:
            A[even], A[odd] = A[odd], A[even]
            odd -= 1
        else:
            even += 1
    return A

A = [1, 2, 3]
B = A.copy()
print(A, reorder(B))
A = [1, 2, 3, 4, 5, 6, 6, 6, 7, 1]
B = A.copy()
print(A, reorder(B))
A = [1, 2, 3, 4, 5, 6, 6, 6, 7, 1, 2, 1, 8, 0, 9]
B = A.copy()
print(A, reorder(B))
print("------------------------------------------")
A = [1, 2, 3]
B = A.copy()
print(A, reorder_elegant(B))
A = [1, 2, 3, 4, 5, 6, 6, 6, 7, 1]
B = A.copy()
print(A, reorder_elegant(B))
A = [1, 2, 3, 4, 5, 6, 6, 6, 7, 1, 2, 1, 8, 0, 9]
B = A.copy()
print(A, reorder_elegant(B))
        


