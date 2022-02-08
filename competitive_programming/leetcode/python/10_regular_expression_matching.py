def isMatch(s: str, p: str) -> bool:
  n = len(s)
  m = len(p)
  # s[0, i) matchs p[0, j) or not
  dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
  dp[0][0] = True
  for j in range(1, m + 1):
    dp[0][j] = dp[0][j - 2] and p[j - 1] == '*' 
    
  def cMatch(sc, pc):
    return sc == pc or pc == '.'

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if p[j - 1] == '*':
        # dp[i][j - 2], dp[i][j - 1]:  '*' swallows pre charater
        # dp[i - 1][j]:  '*' repeats pre charater
        dp[i][j] = cMatch(s[i - 1], p[j - 2]) and dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
      else:
        dp[i][j] = dp[i - 1][j - 1] and cMatch(s[i - 1], p[j - 1])

  return dp[n][m]

print(isMatch("aa", "a"))                   # false
print(isMatch("aa", "a*"))                  # true
print(isMatch("ab", ".*"))                  # true
print(isMatch("aab", "c*a*b"))              # true
print(isMatch("mississippi", "mis*is*p*.")) # false
print(isMatch("aaa", "ab*ac*a"))            # true

