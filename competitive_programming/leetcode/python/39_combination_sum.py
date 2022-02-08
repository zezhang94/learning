def bfs(candidates, target):
  n = len(candidates)
  ans = []
  tree = [[i] for i in range(n)]
  count = target // min(candidates) + 1
  
  while count > 0:
    tmp = []
    for arr in tree:
      sum_ = sum([candidates[i] for i in arr])
      if sum_ >= target:
        if sum_ == target:
          ans.append([candidates[i] for i in arr])
        continue
      for i in range(arr[-1], n):
        tmp.append(arr + [i])
    tree = tmp
    count -= 1

  return ans

def dfsSolution(candidates, target):
  def dfs(candidates, target, start, stack, ans):
    if target == 0:
      ans.append(stack[:])
      return
    
    for i in range(start, len(candidates)):
      if candidates[i] > target:
          return 
      stack.append(candidates[i])
      dfs(candidates, target - candidates[i], i, stack, ans)
      stack.pop()

  candidates.sort()
  ans = []
  dfs(candidates, target, 0, [], ans)
  return ans

print(dfsSolution([2, 3, 6, 7], 7))
print(dfsSolution([2, 3, 5], 8))
print(dfsSolution([2], 1))
print(dfsSolution([1], 1))
print(dfsSolution([1], 2))
print(dfsSolution([10, 1, 2, 7, 6, 1, 5], 8))
print(dfsSolution(
    [1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1], 27
    )
)