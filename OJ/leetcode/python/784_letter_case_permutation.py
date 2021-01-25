def dfsSolution(S):
  def dfs(S, start, stack, ans):
    if len(S) == len(stack):
      ans.append(stack)
      return
    
    for i in range(start, len(S)):
      stack += S[i]
      dfs(S, i + 1, stack, ans)
      stack = stack[:-1]
      if S[i].islower():
        stack += S[i].upper()
        dfs(S, i + 1, stack, ans)
        stack = stack[:-1]
      elif S[i].isupper():
        stack += S[i].lower()
        dfs(S, i + 1, stack, ans)
        stack = stack[:-1]
  
  ans = []
  dfs(S, 0, "", ans)
  return ans

print(dfsSolution("a1b2"))

def letterCasePermutation(S: str):
  ans = [S]
  for i in range(len(S)):
    copy = ans
    if S[i].islower():
      for s in copy:
        s[i] = S[i].upper()
      ans += copy
    elif S[i].isupper():
      for s in copy:
        s[i] = S[i].lower()
      ans += copy
  return ans
    
print(letterCasePermutation("a1b2"))

