def isMatch(s, p):
    def cMatch(c1, c2):
        return c1 == c2 or c2 == '?'

    n = len(s)
    m = len(p)
    
    '''
      dp[i][j] = True if s[0...i) matches p[0...j)
      dp[i][j] = {
          True                                              if i == 0 and j == 0
            ([0, 0) means empty set, empty matches empty)
          i and dp[i - 1][j] or dp[i][j - 1]                if p[j - 1] == '*'
            (s[i - 1] matches p[j - 2] or s[i - 2] matches p[j - 1])
          i and s[i - 1] == p[j - 1] and dp[i - 1][j - 1]   if p[j - 1] != '*'
      }
    '''
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n + 1):
        for j in range(1, m + 1): # from none empty pattern
            if p[j - 1] == '*':
                dp[i][j] = (i and dp[i - 1][j]) or dp[i][j - 1]
            else:
                dp[i][j] = (i and cMatch(s[i - 1], p[j - 1])) and dp[i - 1][j - 1] 
    return dp[n][m]
    
print(isMatch("aa", "a"))           # false
print(isMatch("aa", "*"))           # true
print(isMatch("cb", "?a"))          # false
print(isMatch("adceb", "*a*b"))     # true
print(isMatch("acdcb", "a*c?b"))    # false