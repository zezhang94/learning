# Kadane's algorithm
def kadane(arr):
    current = 0
    maximum = 0 # float('-inf') if disallowing empty subarray
    for v in arr:
        current = max(0, current + v) # max(x, current + v) if disallowing empty subarray
        maximum = max(maximum, current)
    return maximum