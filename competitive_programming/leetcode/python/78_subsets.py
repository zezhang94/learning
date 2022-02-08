def iterativeBfsSolution(nums):
  n = len(nums)
  tree = [[i] for i in range(0, n)]
  index_ans = []
  count = n
  while count > 0:
    tmp = []
    for arr in tree:
      for i in range(arr[-1] + 1, n):
        tmp.append(arr + [i])
      index_ans.append(arr)
    tree = tmp
    count -= 1
  ans = [[]]
  for arr in index_ans:
    ans.append([nums[i] for i in arr])
  return ans


def dfsSolution(nums):
  def dfs(depth, nums, start, stack, ans):
    ans.append(stack[:])
    if depth == len(nums):
      return

    for i in range(start, len(nums)):
      stack.append(nums[i])
      dfs(depth + 1, nums, i + 1, stack, ans)
      stack.pop()

  ans = []
  dfs(0, nums, 0, [], ans)
  return ans  
  
print(dfsSolution([1, 2, 3]))
  


