def kConcatenationMaxSum(arr, k) -> int:
  n = len(arr)
  m = 1000000007
  def kadane(arr):
    current, maximum = 0, 0
    for v in arr:
      current = max(0, current + v)
      maximum = max(maximum, current)
    return maximum
  return ((k - 2) * max(sum(arr), 0) + kadane(arr * 2)) % m if k > 1 else kadane(arr) % m 
     
print(kConcatenationMaxSum([1, 2], 3))
print(kConcatenationMaxSum([1, -2 ,1], 5))
print(kConcatenationMaxSum([-1, -2], 7))
print(kConcatenationMaxSum([9, -1, 100, 1, -2], 3))
print(kConcatenationMaxSum([1, -1], 1))
print(kConcatenationMaxSum([-5, -2, 0, 0, 3, 9, -2, -5, 4], 5)) # 20