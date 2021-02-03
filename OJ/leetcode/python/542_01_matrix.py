from typing import List
from collections import deque

class Solution:
    def minOfAdjacency(self, i: int, j: int, inf: int, \
                       distance: List[List[int]], matrix: List[List[int]]) -> int:
        if distance[i][j] != inf:
            return distance[i][j]

        m, n = len(matrix), len(matrix[0])
        minimum = inf

        if i - 1 >= 0:
            minimum = min(distance[i - 1][j] + 1, minimum)
        if j - 1 >= 0:
            minimum = min(distance[i][j - 1] + 1, minimum)
        if i + 1 < m:
            minimum = min(bfs(i + 1, j, inf, distance, matrix), minimum)
        if j + 1 < n:
            minimum = min(bfs(i, j + 1, inf, distance, matrix), minimum)
        return minimum

    def bfs(self, i: int, j: int, inf: int, distance: List[List[int]], matrix: List[List[int]]) -> int:

        return 0


        
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        inf = 10001
        m, n = len(matrix), len(matrix[0])
        distance = [[inf for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                else:

