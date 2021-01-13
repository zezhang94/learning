# TLE
def checkSubarraySum(nums, k):
  n = len(nums)
  dp = [[-1 for j in range(n)] for i in range(n)]
  for i in range(n):
    dp[i][i] = nums[i]
  for step in range(1, n):
    for i in range(n):
      j = i + step
      if j >= n:
        break
      value = dp[i][j - 1] + nums[j]
      if k == 0 and value == 0:
        return True  
      elif k != 0 and value % k == 0:
        return True
      dp[i][j] = value
  return False

# (a + n * k) % k = a % k
def on(nums, k):
  n = len(nums)
  if k == 0:
    for i in range(n - 1):
      if nums[i] == nums[i + 1] == 0:
        return True
    return False
  mod_k = 0
  record = {0: -1} # first two element construct the answer 
  for i in range(0, n):
    mod_k = (mod_k + nums[i]) % k
    if mod_k not in record:
      record[mod_k] = i
    elif i - record[mod_k] > 1:
      return True
  return False

print(on([23, 2, 4, 6, 7], 6))
print(on([23, 2, 6, 4, 7], 6))
print(on([0, 1, 0], 0))
print(on([1, 0, 0], 2))
   