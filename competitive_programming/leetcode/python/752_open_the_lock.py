from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        candidates = [True for _ in range(10000)]
        for end in deadends:
            candidates[int(end)] = False
        if not candidates[0]:
            return -1
        target = int(target)
        if target == 0:
            return 0

        queue = deque()
        queue.appendleft((0, 0))
        candidates[0] = False
        depth = 0
        while len(queue) > 0:
            parent, depth = queue.pop()
            thousand = parent // 1000 * 1000
            hundred = parent // 100 * 100
            ten = parent // 10 * 10
            possible = [
                (parent - 1000) % 10000, 
                (parent + 1000) % 10000,
                (parent - thousand - 100) % 1000 + thousand, 
                (parent - thousand + 100) % 1000 + thousand,
                (parent - hundred - 10) % 100 + hundred, 
                (parent - hundred + 10) % 100 + hundred,
                (parent - ten - 1) % 10 + ten, 
                (parent - ten + 1) % 10 + ten
            ]
            for candidate in possible:
                if candidate == target:
                    return depth + 1
                if candidates[candidate]:
                    queue.appendleft((candidate, depth + 1))
                    candidates[candidate] = False
            depth += 1
        return -1



solution = Solution()

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
# ans = 6,  "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"
print(solution.openLock(deadends, target))

deadends = ["8888"]
target = "0009"
print(solution.openLock(deadends, target))

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(solution.openLock(deadends, target))

deadends = ["0000"]
target = "8888"
print(solution.openLock(deadends, target))
