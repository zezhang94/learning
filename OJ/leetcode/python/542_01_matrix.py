from typing import List
from collections import deque

class Solution:           
    def updateMatrixBfs(self, matrix: List[List[int]]) -> List[List[int]]:
        inf = 10001
        m, n = len(matrix), len(matrix[0])
        distance = [[inf for _ in range(n)] for _ in range(m)]
        valid = [[True for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                    valid[i][j] = False
                    queue.appendleft((i, j))
        direction = [0, -1, 0, 1, 0]
        depth = 0
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                ri, rj = queue.pop()
                distance[ri][rj] = depth
                for k in range(4): 
                    i, j = ri + direction[k], rj + direction[k + 1]
                    if 0 <= i < m and 0 <= j < n and valid[i][j]:
                        valid[i][j] = False
                        queue.appendleft((i, j))
                size -= 1
            depth += 1
        return distance
    
    def updateMatrixDP(self, matrix: List[List[int]]) -> List[List[int]]:
        inf = 10001
        m, n = len(matrix), len(matrix[0])
        distance = [[inf for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                if i - 1 >= 0:
                    distance[i][j] = min(distance[i - 1][j] + 1, distance[i][j])
                if j - 1 >= 0:
                    distance[i][j] = min(distance[i][j - 1] + 1, distance[i][j])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    distance[i][j] = min(distance[i + 1][j] + 1, distance[i][j])
                if j + 1 < n:
                    distance[i][j] = min(distance[i][j + 1] + 1, distance[i][j])
        return distance

solution = Solution()

matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(solution.updateMatrixBfs(matrix))
print(solution.updateMatrixDP(matrix))


matrix = [
    [0, 1, 0], 
    [0, 1, 0], 
    [0, 1, 0], 
    [0, 1, 0], 
    [0, 1, 0]
]
print(solution.updateMatrixBfs(matrix))
print(solution.updateMatrixDP(matrix))