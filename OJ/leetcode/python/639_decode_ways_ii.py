def numDecodings(s: str):
  if s[0] == '0':
    return False
  
  m = 1000000007

  s = "0" + s
  n = len(s)
  # decoding ways of i-size string
  dp = [0 for _ in range(n)]
  dp[0] = 1
  dp[1] = 9 if s[1] == '*' else 1
  
  for i in range(2, n):
    if s[i] == '*':
      if s[i - 1] == '0':
        dp[i] += dp[i - 1] * 9 % m 
      elif s[i - 1] == '1':
        dp[i] += (dp[i - 1] * 9 + dp[i - 2] * 9) % m
      elif s[i - 1] == '2':
        dp[i] += (dp[i - 1] * 9 + dp[i - 2] * 6) % m
      elif s[i - 1] == '*':
        dp[i] += dp[i - 1] * 9 % m
        dp[i] += dp[i - 2] * 15 % m
      else:
        dp[i] += dp[i - 1] * 9 % m 
    else:

  return dp[n - 1]

print(numDecodings("*"))
print(numDecodings("1*"))
print(numDecodings("11*")) # 9 + (9 + 10) - 1 = 27 
print(numDecodings("2*"))
print(numDecodings("10"))
print(numDecodings("10*"))
print(numDecodings("**")) # 9 * 9 + 17 = 98
print(numDecodings("***")) # 9 * 9 * 9 + (17 * 9 * 2) = 1035
