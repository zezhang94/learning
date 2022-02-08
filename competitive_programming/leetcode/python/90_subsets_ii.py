def subsetsWithDup(nums):
  def dfs(nums, start, stack, ans):
    ans.append(stack[:])

    for i in range(start, len(nums)):
      if i > start and nums[i] == nums[i - 1]:
        continue
      stack.append(nums[i])
      dfs(nums, i + 1, stack, ans)
      stack.pop()

  nums.sort()
  ans = []
  dfs(nums, 0, [], ans)
  return ans

print(subsetsWithDup([1, 2, 2]))
print(subsetsWithDup([0]))