def combinationSum3(k, n):
  def dfs(depth, k, target, start, stack, ans):
    if depth == k:
      if target == 0:
        ans.append(stack[:])
      return
  
    for i in range(start, 10):
      if i > target:
        return
      stack.append(i)
      dfs(depth + 1, k, target - i, i + 1, stack, ans)
      stack.pop()

  ans = []
  dfs(0, k, n, 1, [], ans)
  return ans

print(combinationSum3(3, 7))
print(combinationSum3(3, 9))
print(combinationSum3(4, 1))
print(combinationSum3(3, 2))
print(combinationSum3(9, 45))
print(combinationSum3(2, 18))