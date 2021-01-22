def combine(n, k):
  def dfs(depth, k, n, start, stack, ans):
    if depth == k:
      ans.append(stack[:])
      return

    for i in range(start, n + 1):
      stack.append(i)
      dfs(depth + 1, k, n, i + 1, stack, ans)
      stack.pop()

  ans = []
  dfs(0, k, n, 1, [], ans)
  return ans

print(combine(4, 2))
print(combine(1, 1))