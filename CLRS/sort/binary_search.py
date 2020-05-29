def binary_search_recursive(A, p, q, t):  
  if p <= q:
    mid = (p + q) // 2
    if A[mid] == t:
      return mid
    elif A[mid] > t:
      return binary_search_recursive(A, p, mid - 1, t)
    else:
      return binary_search_recursive(A, mid + 1, q, t)
  else:
    return -1

def binary_search_iterative(A, p, q, t):
  while p <= q:
    mid = (p + q) // 2
    if A[mid] == t:
      return mid
    elif t < A[mid]:
      q = mid - 1
    else:
      p = mid + 1
  return -1

if __name__ == "__main__":
    A, t = [x for x in range(19)], 18
    print(binary_search_recursive(A, 0, 18, t))
    print(binary_search_iterative(A, 0, 18, t))