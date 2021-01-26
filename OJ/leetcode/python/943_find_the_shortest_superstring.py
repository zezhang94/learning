'''
Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
'''
# TLE
def shortestSuperstring(A) -> str:
  def link(stack):
    s = stack[0]
    for i in range(1, len(stack)):
      l = min(len(stack[i - 1]), len(stack[i]))
      while l > 0:
        if stack[i - 1][(len(stack[i - 1]) - l):] == stack[i][:l]:
          s += stack[i][l:]
          break
        l -= 1
      if l == 0:
        s += stack[i]
      
    return s

  def dfs(depth, A, stack, used, ans):
    if depth == len(A):
      s = link(stack)
      if len(s) < len(ans[0]):
        ans[0] = s
      return

    for i in range(0, len(A)):
      if not used[i]:
        used[i] = True
        stack.append(A[i])
        dfs(depth + 1, A, stack, used, ans)
        stack.pop()
        used[i] = False

  used = [False] * len(A)
  ans = ["".join(A)]
  dfs(0, A, [], used, ans)
  return ans[0]

#print(shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))

def dfsWithPruningAndPreProcessing(A) -> str:
  def dfs(depth, A, stack, used, table, ans, cur_l, min_l):
    # pruning
    if cur_l > min_l[0]:
      return

    if depth == len(A):
      if cur_l <= min_l[0]:
        ans[0] = stack[:]
        min_l[0] = cur_l
      return

    for i in range(0, len(A)):
      if not used[i]:
        diff = len(A[i]) if depth == 0 else len(A[i]) - table[stack[-1]][i]
        cur_l += diff
        used[i] = True
        stack.append(i)  
        dfs(depth + 1, A, stack, used, table, ans, cur_l, min_l)
        stack.pop()
        used[i] = False
        cur_l -= diff

  # pre-processing
  table = [[0 for _ in range(len(A))] for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(A)):
      if i != j:
        l = min(len(A[i]), len(A[j]))
        while l > 0:
          if A[i][(len(A[i]) - l):] == A[j][:l]:
            table[i][j] = l
            break
          l -= 1

  used = [False] * len(A)
  ans = [[]]
  min_l = [sum([len(s) for s in A])]
  dfs(0, A, [], used, table, ans, 0, min_l)

  ans = ans[0]
  result = A[ans[0]]
  for i in range(1, len(ans)):
    result += A[ans[i]][table[ans[i - 1]][ans[i]]:]
  return result

print(dfsWithPruningAndPreProcessing(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
print(dfsWithPruningAndPreProcessing(["alex", "loves", "leetcode"]))
print("gctaagttcatgcatc")