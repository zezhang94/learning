def selection_sort(A):
  for i in range(0, len(A) - 1):
    min_index = i
    for j in range(i + 1, len(A)):
      if A[j] < A[min_index]:
        min_index = j
    A[i], A[min_index] = A[min_index], A[i]

if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    selection_sort(A)
    print(A)