# TLE
def combinationSum(candidates, target):
  index_ans = []
  candidates.sort()
  count = target // candidates[0]
  n = len(candidates)
  tree, ans = [[]], []

  while count > 0:
    tmp = []
    for arr in tree:
      start = 0 if len(arr) == 0 else arr[-1] + 1
      for i in range(start, n):
        sum_ = sum([candidates[j] for j in arr]) + candidates[i]
        if sum_ < target:
          tmp.append(arr + [i])
        elif sum_ == target:
          index_ans.append(arr + [i])
    tree = tmp 
    count -= 1

  hash_table = set()
  for arr in index_ans:
    s = "".join([str(candidates[i]) for i in arr])
    if s not in hash_table:
      ans.append([candidates[i] for i in arr])
      hash_table.add(s)

  return ans

def dfsSolution(candidates, target):
  def dfs(candidates, target, start, stack, ans):
    if target == 0:
      ans.append(stack[:])
      return
    
    for i in range(start, len(candidates)):
      if candidates[i] > target:
        return
      # prune - omit equivalant elements in same depth
      if i > start and candidates[i] == candidates[i - 1]: 
        continue
      stack.append(candidates[i])
      dfs(candidates, target - candidates[i], i + 1, stack, ans)
      stack.pop()

  candidates.sort()
  ans = []
  dfs(candidates, target, 0, [], ans)
  return ans

print(dfsSolution([10, 1, 2, 7, 6, 1, 5], 8))
print(dfsSolution([2, 5, 2, 1, 2], 5))
print(dfsSolution([1, 1], 2))
print(dfsSolution(
    [1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1], 27
    )
)