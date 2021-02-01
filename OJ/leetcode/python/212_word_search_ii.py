from typing import List
from typing import Tuple

class Solution:
    def getNeighbors(self, i: int, j: int, valid: List[List[bool]]) -> List[Tuple]:
        neighbors = []
        if i - 1 >= 0 and valid[i - 1][j]:
            neighbors.append((i - 1, j))
        if j - 1 >= 0 and valid[i][j - 1]:
            neighbors.append((i, j - 1))
        if i + 1 < len(valid) and valid[i + 1][j]:
            neighbors.append((i + 1, j))
        if j + 1 < len(valid[0]) and valid[i][j + 1]:
            neighbors.append((i, j + 1))                
        return neighbors
    
    def dfs(self, word: str, row: int, col: int, \
            valid: List[List[bool]], board: List[List[str]]):
        if len(word) == 0:
            return True
        neighbors = self.getNeighbors(row, col, valid)
        for neighbor in neighbors:
            i, j = neighbor
            if board[i][j] == word[0]:
                valid[i][j] = False
                ans = self.dfs(word[1:], i, j, valid, board)
                valid[i][j] = True   
                if ans:
                    return True
        return False

    def findWord(self, valid: List[List[str]], board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    valid[i][j] = False
                    ans = self.dfs(word[1:], i, j, valid, board)
                    valid[i][j] = True
                    if ans:
                        return True
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        valid = [[True for _ in board[0]] for _ in board]
        ans = []
        for word in words:
            if self.findWord(valid, board, word):
                ans.append(word)
        return ans

solution = Solution()

board = [ \
    ["o","a","a","n"], \
    ["e","t","a","e"], \
    ["i","h","k","r"], \
    ["i","f","l","v"]  \
]
words = ["oath","pea","eat","rain"]
print(solution.findWords(board, words))

board = [["a","b"],["c","d"]]
words = ["abcb"]
print(solution.findWords(board, words))