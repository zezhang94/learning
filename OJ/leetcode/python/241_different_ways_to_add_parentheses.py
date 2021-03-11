from typing import List

class Solution:
    def __init__(self):
        self.opSet = {"*", "+", "-"}
        self.record = {}

    def diffWaysToCompute(self, input: str) -> List[int]:
        ans = self.divide(input)
        return ans

    def divide(self, input: str) -> List[int]:
        if input in self.record:
            return self.record[input]
        
        temp_ans = []
        for i in range(len(input)):
            if input[i] in self.opSet:
                left = self.divide(input[:i])
                right = self.divide(input[(i + 1):])
                for left_v in left:
                    for right_v in right:
                        temp_ans.append(self.calculate(input[i], left_v, right_v))
        
        if len(temp_ans) == 0:
            return [int(input)]
        
        self.record[input] = temp_ans
        return temp_ans
     
    def calculate(self, op: str, v1: int, v2: int) -> int:
        if op == "*":
            return v1 * v2
        elif op == "+":
            return v1 + v2
        else:
            return v1 - v2 

solution = Solution()
print(solution.diffWaysToCompute("2-1-1"))  
print(solution.diffWaysToCompute("2*3-4*5"))