from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        while True:
            pivot = self.partition(nums, start, end)
            if pivot == k - 1:
                return nums[pivot]
            if pivot < k - 1:
                start = pivot + 1
            else:
                end = pivot - 1

    def partition(self, nums: List[int], start: int, end: int) -> int:
        rand = random.randint(start, end)
        nums[rand], nums[end] = nums[end], nums[rand]
        pivot = nums[end]
        cur = start
        for i in range(start, end):
            if nums[i] > pivot:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        nums[cur], nums[end] = nums[end], nums[cur]
        return cur


solution = Solution()
arr = [i for i in range(10)]
random.shuffle(arr)
ans = solution.findKthLargest(arr, 3)
print(arr, ans)
