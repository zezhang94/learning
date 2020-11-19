def merge(A, p, q, r):
  """Merger adjacent sorted sequence

  p <= q <= r

  Args:
    A: sequence to sort
    p: start index
    q: divide index
    r: end index
  """
  B = [None] * (r - p + 1)
  i, j, count = p, q + 1, 0
  while i <= q and j <= r:
    if A[i] <= A[j]:
      B[count] = A[i]
      i += 1
    else:
      B[count] = A[j]
      j += 1
    count += 1
  while i <= q:
    B[count] = A[i]
    i += 1
    count += 1
  while j <= r:
    B[count] = A[j]
    j += 1
    count += 1
  A[p:(r + 1)] = B

def merge_sort(A, p, r):
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)