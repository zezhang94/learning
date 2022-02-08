from typing import List

# TLE
class TLESolution:
    def dfs(self, cur_sum: int, k: int, used: int, target: int, nums: List[int]) -> bool:           
        if k == 0:
            return used == (1 << len(nums)) - 1
        for i in range(len(nums)):
            if used & (1 << i):
                continue
            t = cur_sum + nums[i]
            if t > target:
                '''
                print("{0:b}".format(used))
                print("{0:b}".format(used | 1 << i), cur_sum, "+", nums[i], "=", t)
                '''
                break
            if t == target and self.dfs(0, k - 1, used | 1 << i, target, nums):
                return True
            elif self.dfs(t, k, used | 1 << i, target, nums):
                return True
        return False
             
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        nums.sort()
        return self.dfs(0, k, 0, total / k, nums)

class SearchSolution:

    def __init__(self):
        self.average = 0

    def search(self, groups: List[int], nums: List[int]) -> bool:
        if len(nums) == 0:
            print(groups)
            return True
        v = nums.pop()
        for index, group in enumerate(groups):
            if v + group <= self.average:
                groups[index] += v
                if self.search(groups, nums):
                    return True
                groups[index] -= v
            if group == 0:
                break
        nums.append(v)
        return False
            
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        self.average, mod = divmod(sum(nums), k)
        if mod > 0:
            return False
        nums.sort()
        if nums[-1] > self.average:
            return False
        while len(nums) > 0 and nums[-1] == self.average:
            nums.pop()
            k -= 1
        return self.search([0] * k, nums)
        

solution = SearchSolution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(solution.canPartitionKSubsets(nums, k))
nums = [4, 5, 3, 2, 5, 5, 1, 3, 5, 5, 5, 5, 5, 2, 5]
k = 12
print(solution.canPartitionKSubsets(nums, k))