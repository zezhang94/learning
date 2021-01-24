def permuteUnique(nums):
  def dfs(nums, stack, used, ans):
    if len(stack) == len(nums):
      ans.append(stack[:])
      return

    for i in range(len(nums)):
      # same value should appear in index order
      if used[i] or i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
        continue
      used[i] = True
      stack.append(nums[i])
      dfs(nums, stack, used, ans)
      stack.pop()
      used[i] = False 

  nums.sort()
  ans = []
  dfs(nums, [], [False] * len(nums), ans)
  return ans


print(permuteUnique([1, 1, 2]))
print(permuteUnique([0]))
print(permuteUnique([1, 1, 1, 1]))
print(permuteUnique([0, 1, 1, 1, 0]))