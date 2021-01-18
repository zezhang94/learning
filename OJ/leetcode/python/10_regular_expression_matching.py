def isMatch(s: str, p: str) -> bool:
  # Tip: make the index based on 1
  s, p = "*" + s, "*" + p
  n = len(s)
  m = len(p)
  
  # p[0, i] matches s[0, j]
  dp = [[False for _ in range(n)] for _ in range(m)]
  dp[0][0] = True

  for i in range(2, m):
    dp[i][0] = dp[i - 2][0] and p[i] == '*'

  def cMatch(c1, c2):
    return c1 == c2 or c2 == '.'

  for i in range(1, m):
    for j in range(1, n):
      if p[i] == '*':
        dp[i][j] = dp[i - 2][j] or dp[i - 1][j] or (cMatch(s[j], p[i - 1]) and dp[i][j - 1]) 
      else:
        dp[i][j] = cMatch(s[j], p[i]) and dp[i - 1][j - 1]

  return dp[m - 1][n - 1]

print(isMatch("aa", "a"))                   # false
print(isMatch("aa", "a*"))                  # true
print(isMatch("ab", ".*"))                  # true
print(isMatch("aab", "c*a*b"))              # true
print(isMatch("mississippi", "mis*is*p*.")) # false

