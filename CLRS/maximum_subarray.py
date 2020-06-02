def find_max_crossing(l, r, m, A):
  l_sum = r_sum = float('-inf')
  l_index = r_index = m
  sum = 0
  for i in range(m, l - 1, -1):
    sum += A[i]
    if sum > l_sum:
      l_sum = sum
      l_index = i
  sum = 0
  for i in range(m + 1, r + 1):
    sum += A[i]
    if sum > r_sum:
      r_sum = sum
      r_index = i
  return (l_index, r_index, l_sum + r_sum)

def find_max_subarray(l, r, A):
  if l == r:
    return (l, r, A[l])
  else:
    m = (l + r) // 2
    L = find_max_subarray(l, m, A)
    R = find_max_subarray(m + 1, r, A)
    M = find_max_crossing(l, r, m, A)
    max_sum = max(L[2], R[2], M[2])
    #print(m, max_sum)
    if max_sum == L[2]:
      return L
    elif max_sum == R[2]:
      return R
    else:
      return M

if __name__ == "__main__":
    A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    B = (len(A) - 1) * [None]
    for i in range(0, len(A) - 1):
        B[i] = A[i + 1] - A[i]
    print(B)
    print(find_max_subarray(0, len(B) - 1, B))