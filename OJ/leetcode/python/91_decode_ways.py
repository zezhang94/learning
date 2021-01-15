def numDecodings(s) -> int:
  n = len(s)
  # edge cases
  if s[0] == '0':
    return 0
  for i in range(1, n):
    if s[i] == '0' and s[i - 1] != '1' and s[i - 1] != '2':
      return 0

  dp = [0 for _ in range(n)]
  if s[0] != '0': 
    dp[0] = 1
  for i in range(1, n):
    pre = int(s[i - 1]) * 10 + int(s[i])
    if s[i] == '0' or s[i - 1] == '0':
      dp[i] = dp[i - 1]
    else:
      dp[i] = dp[i - 1] + 1 if 0 < pre <= 26 else dp[i - 1]
  return dp[n - 1]

print(numDecodings("12")) # 2
print(numDecodings("226")) # 3
print(numDecodings("0")) # 0
print(numDecodings("1")) # 1
print(numDecodings("10")) # 1
print(numDecodings("2101")) # 1
