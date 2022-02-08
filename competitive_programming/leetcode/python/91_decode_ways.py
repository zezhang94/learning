def numDecodings(s) -> int:
  n = len(s)
  if s[0] == '0':
    return 0
  
  # the ways of decoding string whose length is i 
  dp = [0 for _ in range(n + 1)]
  dp[0] = 1 # Tip: use zero index for recursive consistency
  dp[1] = 1
  for i in range(2, n + 1):
    if 1 <= int(s[i - 1 : i]) <= 9:
      dp[i] += dp[i - 1]
    if 10 <= int(s[i - 2 : i]) <= 26:
      dp[i] += dp[i - 2]
    # return from zero immediately
    if dp[i] == 0:
      return 0

  return dp[n]

print(numDecodings("12")) # 2: dp = {1, 1, 2}
print(numDecodings("226")) # 3
print(numDecodings("0")) # 0
print(numDecodings("1")) # 1
print(numDecodings("10")) # 1
print(numDecodings("2101")) # 1
