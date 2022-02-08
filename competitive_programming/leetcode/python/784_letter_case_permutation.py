def slowSolution(S):
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

print(slowSolution("a1b2"))

def optimizing(S: str):
  def dfs(s, i, ans):
    if i == len(s):
      ans.append("".join(s))
      return 
    dfs(s, i + 1, ans)
    if s[i].isalpha():
      # Tip: ^ (1 << 5), toggle between lowercase and uppercase
      s[i] = chr(ord(s[i]) ^ (1 << 5)) 
      dfs(s, i + 1, ans)
      s[i] = chr(ord(s[i]) ^ (1 << 5))    

  # Tip: avoid creating new space
  s = [c for c in S]
  ans = []
  dfs(s, 0, ans)
  return ans
    
print(optimizing("a1b2"))

