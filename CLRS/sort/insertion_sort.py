def insertion_sort(A):
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    # insert into sorted sequence
    while i > -1 and A[i] > key:
      A[i + 1] = A[i]
      i -= 1
    A[i + 1] = key

def insertion_sort_reverse(A):
  for j in range(len(A) - 2, -1, -1):
    key = A[j]
    i = j + 1
    while i < len(A) and key < A[i]:
      A[i - 1] = A[i]
      i += 1
    A[i - 1] = key

if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    insertion_sort(A)
    print(A)
    A = [5, 2, 4, 6, 1, 3]
    insertion_sort_reverse(A)
    print(A)

