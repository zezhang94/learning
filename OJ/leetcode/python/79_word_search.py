from typing import List
from typing import Tuple

class Solution:
    def findNeighbors(self, i: int, j: int, valid: List[List[bool]]) -> List[Tuple]:
        neighbors = []
        m, n = len(valid), len(valid[0])
        if i - 1 >= 0 and valid[i - 1][j]:
            neighbors.append((i - 1, j))
        if j - 1 >= 0 and valid[i][j - 1]:
            neighbors.append((i, j - 1))
        if i + 1 < m and valid[i + 1][j]:
            neighbors.append((i + 1, j))
        if j + 1 < n and valid[i][j + 1]:
            neighbors.append((i, j + 1))
        return neighbors

    def dfs(self, row: int, col: int, word: str, \
            valid: List[bool], board: List[List[str]]) -> bool:
        if len(word) == 0:
            return True
        neighbors = self.findNeighbors(row, col, valid)
        for neighbor in neighbors:
            i, j = neighbor
            if word[0] == board[i][j]:
                valid[i][j] = False
                if self.dfs(i, j, word[1:], valid, board):
                    return True
                valid[i][j] = True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        valid = [[True for _ in board[0]] for _ in board]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    valid[i][j] = False
                    ans = self.dfs(i, j, word[1:], valid, board)
                    if ans:
                        return True
                    valid[i][j] = True
        return False
                     

solution = Solution()

board = [ \
    ["C","A","A"], \
    ["A","A","A"], \
    ["B","C","D"]  \
]
word = "AAB"
print(solution.exist(board, word))

board = [ \
    ["A","B","C","E"], \
    ["S","F","C","S"], \
    ["A","D","E","E"]  \
]
word = "ABCCED"
print(solution.exist(board, word))

board = [ \
    ["A","B","C","E"], \
    ["S","F","C","S"], \
    ["A","D","E","E"]  \
]
word = "SEE"
print(solution.exist(board, word))

board = [ \
    ["A","B","C","E"], \
    ["S","F","C","S"], \
    ["A","D","E","E"]  \
]
word = "ABCB"
print(solution.exist(board, word))

board = [["a","a"]]
word = "aaa"
print(solution.exist(board, word))