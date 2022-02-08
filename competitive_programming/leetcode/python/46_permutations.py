def permute(self, nums: List[int]):
  def dfs(depth, nums, stack, used, ans):
    if depth == len(nums):
      ans.append(stack[:])
      return

    for i in range(len(nums)):
      if used[i]:
        continue
      used[i] = True
      stack.append(nums[i])
      dfs(depth + 1, nums, stack, used, ans)
      stack.pop()
      used[i] = False 

  ans = []
  dfs(0, nums, stack, [False] * len(nums), ans)
  return ans
