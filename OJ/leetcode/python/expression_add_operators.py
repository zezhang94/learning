class Solution:
    def __init__(self):
        self.ops = ["*", "+", "-"]
        self.record = {}

    def addOperators(self, num: str, target: int, depth: int) -> List[str]:
        return []
                
    def calculate(self, op: str, v1: int, v2: int):
        if op == "*":
            return v1 * v2
        elif op == "+":
            return v1 + v2
        else:
            return v1 - v2

