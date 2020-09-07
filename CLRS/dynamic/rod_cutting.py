def memoized_cut_rod(p, n, r):
  if n == 0:
    return 0
  r_max = -1
  for i in range(n):
    if r[n - i - 2] >= 0:
      r_max = max(r_max, p[i] + r[n - i - 2])
    else:
      optimal = memoized_cut_rod(p, n - i - 1, r)
      r[n - i - 2] = optimal
      r_max = max(r_max, p[i] + optimal)
  return r_max

if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    r = [-1] * len(p)
    print(memoized_cut_rod(p, 4, r))