from typing import List
class Solution:
    def __init__(self):
        self.n
        self.m
        self.maximum
        self.direction = [0, -1, 0, 1, 0]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        memo = [[1 for _ in range(n)] for _ in range(m)]

    def dfs(self, ri: int, rj: int, matrix: List[List[int]], memo: List[List[int]]) -> int:
        ans = 0
        for k in range(4):
            i = ri + direction[k]
            j = rj + direction[k + 1]
            if i < 0 or i >= self.m or j < 0 or j >= n or matrix[i][j] <= matrix[ri][rj]:
                continue
            ans = max()
