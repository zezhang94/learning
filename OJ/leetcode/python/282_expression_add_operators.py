from typing import List
 
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        nums = [ch for ch in num]
        exp = ["\0" for _ in range(2 * len(num))]
        ans = []
        self.dfs(nums, target, exp, 0, 0, 0, 0, ans)
        return ans

    def dfs(self, nums: List[str], target: int,
            exp: List[str], tail: int, start: int, pre: int, cur: int,
            ans: List[str]):
            if start == len(nums):
                if cur == target:
                    ans.append("".join(exp[:tail]))
                return

            value = 0
            op_index = tail
            if start > 0:
                tail = tail + 1
            end = start
            for i in range(start, len(nums)):
                value = 10 * value + int(nums[i])
                if value > (1 << 31) - 1:
                    break
                exp[tail] = nums[end]
                tail += 1
                end += 1
                if nums[start] == "0" and end - start > 1:
                    return
                if start == 0:
                    self.dfs(nums, target, exp, tail, i + 1, value, value, ans)
                    continue
                exp[op_index] = "+"
                self.dfs(nums, target, exp, tail, i + 1, value, cur + value, ans)
                exp[op_index] = "-"
                self.dfs(nums, target, exp, tail, i + 1, -value, cur - value, ans)
                exp[op_index] = "*"
                self.dfs(nums, target, exp, tail, i + 1, pre * value, cur - pre + pre * value, ans)

solution = Solution()
print(solution.addOperators("123", 6))
print(solution.addOperators("232", 8))
print(solution.addOperators("1234", 10))
print(solution.addOperators("105", 5))
print(solution.addOperators("00", 0))
print(solution.addOperators("3456237490", 9191))
