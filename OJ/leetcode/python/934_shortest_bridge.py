from typing import List
from typing import Set
from typing import Tuple
from typing import Deque
from collections import deque

class BFSSolution:
    def __init__(self):
        self.direction = [0, -1, 0, 1, 0]
        self.INT_MAX = 10001

    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)
        island = set()

        foundIsland = False
        for i in range(n):
            if foundIsland:
                break
            for j in range(n):
                if A[i][j] == 1:
                    self.getIsland(i, j, island, A)
                    foundIsland = True
                    break

        minimum = self.INT_MAX
        for i, j in island:
            minimum = min(minimum, self.getDistance(i, j, island, A, minimum))
            if minimum == 1:
                return 1
        
        return minimum
    
    # dummy way
    def getDistance(self, ri: int, rj: int, island: Set[Tuple], A: List[List[int]], minimum: int) -> int:
        n = len(A)
        valid = [[True for _ in range(n)] for _ in range(n)]
        queue = deque()
        queue.append((ri, rj))
        valid[ri][rj] == False
        depth = 0
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                ri, rj = queue.pop()
                for k in range(4):
                    i = ri + self.direction[k]
                    j = rj + self.direction[k + 1]
                    if 0 <= i < n and 0 <= j < n and valid[i][j]:
                        if (i, j) in island or not valid[i][j]:
                            continue
                        if A[i][j] == 1:
                            return depth
                        queue.appendleft((i, j))
                        valid[i][j] = False
                size -= 1
            depth += 1
            if depth >= minimum:
                return self.INT_MAX

        return self.INT_MAX
    
    def getIsland(self, ri: int, rj: int, island: Set[Tuple], A: List[List[int]]) -> None:
        n = len(A)
        valid = [[True for _ in range(n)] for _ in range(n)]
        queue = deque()
        queue.append((ri, rj))
        valid[ri][rj] == False
        island.add((ri, rj))
        while len(queue) > 0:
            ri, rj = queue.pop()
            for k in range(4):
                i = ri + self.direction[k]
                j = rj + self.direction[k + 1]
                if 0 <= i < n and 0 <= j < n and valid[i][j] and A[i][j] == 1:
                    queue.appendleft((i, j))
                    valid[i][j] = False
                    island.add((i, j))

class BFSPlusDFS:
    def __init__(self):
        self.direction = [0, -1, 0, 1, 0]
        self.INT_MAX = 10001

    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)
        found = False
        queue = deque()
        for i in range(n):
            if found:
                break
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(i, j, queue, A)
                    found = True
                    break
        minimum = self.INT_MAX
        return self.bfs(queue, A)

    '''
    expand util reaching the other island
    Tip: put all initialing nodes into first level 
    '''
    def bfs(self, queue: Deque[Tuple], A: List[List[int]]):
        depth, n = 0, len(A)
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                ri, rj = queue.pop()
                for k in range(4):
                    i = ri + self.direction[k]
                    j = rj + self.direction[k + 1]
                    if 0 <= i < n and 0 <= j < n:
                        if A[i][j] == 1:
                            return depth
                        if A[i][j] == 0:
                            queue.appendleft((i, j))
                            A[i][j] = 2
                size -= 1
            depth += 1

    def dfs(self, ri: int, rj: int, queue: Deque[Tuple], A: List[List[int]]) -> None:
        n = len(A)
        if ri < 0 or ri >= n or rj < 0 or rj >= n or A[ri][rj] != 1:
            return 
        A[ri][rj] = 2
        queue.appendleft((ri, rj))
        for i in range(4):
            self.dfs(ri + self.direction[i], rj + self.direction[i + 1], queue, A) 


solution1 = BFSSolution()
solution2 = BFSPlusDFS()

A = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]
print("------")
print(solution1.shortestBridge(A))
print(solution2.shortestBridge(A))

A = [
    [1,1,1,1,1,1],
    [1,0,0,0,0,1],
    [1,0,0,1,0,1],
    [1,0,0,0,0,1],
    [1,1,1,1,1,1]
]
print("------")
print(solution1.shortestBridge(A))
print(solution2.shortestBridge(A))

A = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1],
    [1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]
print("------")
print(solution1.shortestBridge(A))
print(solution2.shortestBridge(A))

A = [
    [1,1,1,0,0],
    [1,1,0,0,0],
    [1,0,0,0,1],
    [0,0,0,1,1],
    [0,0,1,1,1]
]
print("------")
print(solution1.shortestBridge(A))
print(solution2.shortestBridge(A))
