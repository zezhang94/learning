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

print(bfs([2, 3, 6, 7], 7))
print(bfs([2, 3, 5], 8))
print(bfs([2], 1))
print(bfs([1], 1))
print(bfs([1], 2))
      