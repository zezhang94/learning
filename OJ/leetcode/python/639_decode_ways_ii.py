 # Reference: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-639-decode-ways-ii/
def numDecodings(s: str):
  if s[0] == '0':
    return 0
  m = 1000000007

  def one(c):
    if c == '0':
      return 0
    if c == '*':
      return 9
    return 1

  def two(c1, c2):
    if c1 == '*' and c2 == '*':
      return 6 + 9
    elif c1 == '*' and c2 != '*':
      return 2 if 0 <= int(c2) <= 6 else 1
    elif c1 != '*' and c2 == '*':
      if c1 == '1':
        return 9
      elif c1 == '2':
        return 6
      else:
        return 0 
    else:
      return 1 if 10 <= (10 * int(c1) + int(c2)) <= 26 else 0 

  s = "0" + s
  n = len(s)
  # decoding ways of i-size string
  next_pre = 1
  pre = one(s[1])
  
  for i in range(2, n):
    ans = (one(s[i]) * pre + two(s[i - 1], s[i]) * next_pre) % m
    next_pre = pre
    pre = ans

  return pre 

print(numDecodings("*"))
print(numDecodings("1*"))
print(numDecodings("*1")) # 11
print(numDecodings("**1**")) # 18720
print(numDecodings("11*")) # 9 + (9 + 10) - 1 = 27 
print(numDecodings("2*")) # 15
print(numDecodings("*1*1*0")) # 404
print(numDecodings("10"))
print(numDecodings("10*"))
print(numDecodings("**")) # 9 * 9 + 15 = 96
print(numDecodings("***")) # 9 * 9 * 9 + (15 * 9 * 2) = 
