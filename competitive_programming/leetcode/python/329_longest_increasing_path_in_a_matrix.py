from typing import List
class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.maximum = 0
        self.direction = [0, -1, 0, 1, 0]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        memo = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.maximum = max(self.maximum, self.dfs(i, j, matrix, memo))
        return self.maximum           

    def dfs(self, ri: int, rj: int, matrix: List[List[int]], memo: List[List[int]]) -> int:
        if memo[ri][rj] > 0:
            return memo[ri][rj]
        memo[ri][rj] += 1
        for k in range(4):
            i = ri + self.direction[k]
            j = rj + self.direction[k + 1]
            if i < 0 or i >= self.m or j < 0 or j >= self.n or matrix[i][j] <= matrix[ri][rj]:
                continue
            memo[ri][rj] = max(memo[ri][rj], self.dfs(i, j, matrix, memo) + 1)
        return memo[ri][rj]

solution = Solution()
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
print(solution.longestIncreasingPath(matrix))
