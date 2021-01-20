'''
        abc   def
  ghi   jkl   mno
  pqrs  tuv   wxyz
'''

def bfs(digits):
  n = len(digits)
  if n == 0:
    return []
  arr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
  ans = [""]
  for digit in digits:
    tmp = []
    for s in ans:
      for c in arr[int(digit)]:
        tmp.append(s + c)
    ans = tmp
  return ans

print(bfs("23"))
print(bfs("2"))
print(bfs(""))
