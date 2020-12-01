def memoized_cut_rod(p, n, r):
  """
  Recursive solution.

  Args:
    p: Price table of rods.
    n: Length of rods to cut to.
    r: Maximum revenue table.
  """
  if n == 0:
    return 0
  r_max = -1
  for i in range(n):
    if r[n - i - 2] >= 0: # subproblem has been solved
      r_max = max(r_max, p[i] + r[n - i - 2])
    else:
      optimal = memoized_cut_rod(p, n - i - 1, r) # solve subproblem
      r[n - i - 2] = optimal
      r_max = max(r_max, p[i] + optimal)
  return r_max

def bottom_up_cut_rod(p, n):
  r = [-1] * n
  for i in range(n):
    r_max = -1
    # Attention: boundary
    for j in range(i):
        r_max = max(r_max, p[j] + r[i - j - 1])
    r[i] = max(r_max, p[i])
  print(r)
  return r[n - 1]

def cut_rod_with_cost(p, n, cost):
  r = [-1] * n
  c = 0
  for i in range(n):
    r_max = float('-inf')
    # Attention: boundary
    for j in range(i):
        r_max = max(r_max, p[j] + r[i - j - 1] - cost)
    r[i] = max(r_max, p[i])
  return r[n - 1]

if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 8
    r = [-1] * n
    print(memoized_cut_rod(p, n, r))
    print(bottom_up_cut_rod(p, n))
    print(cut_rod_with_cost(p, 5, 1))

# r1 = 1 from solution 1 = 1 (no cuts)
# r2 = 5 from solution 2 = 2 (no cuts)
# r3 = 8 from solution 3 = 3 (no cuts)
# r4 = 10 from solution 4 = 2 + 2
# r5 = 13 from solution 5 = 2 + 3
# r6 = 17 from solution 6 = 6 (no cuts)
# r7 = 18 from solution 7 = 1 + 6 or 7 = 2 + 2 + 3
# r8 = 22 from solution 8 = 2 + 6
# r9 = 25 from solution 9 = 3 + 6
# r10 = 30 from solution 10 = 10 (no cuts)