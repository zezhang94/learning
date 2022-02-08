def totalNQueens(n):
    def isValid(board, col, diagonal_down, diagonal_up, i, j):
        return col[j] and diagonal_up[i + j] and \
            diagonal_down[len(col) - i - 1 + j]

    def dfs(filling, i, board, col, diagonal_down, diagonal_up):
        if i == len(col):
            if filling == 0:
                return 1
            else:
                return 0
        
        count = 0
        for j in range(len(col)):
            if isValid(board, col, diagonal_down, diagonal_up, i, j):
                board[i][j] = 'Q'
                col[j] = 0
                diagonal_up[i + j] = 0
                diagonal_down[len(col) - i - 1 + j] = 0
                count += dfs(filling - 1, i + 1, board, col, diagonal_down, diagonal_up)
                diagonal_down[len(col) - i - 1 + j] = 1
                diagonal_up[i + j] = 1
                col[j] = 1
        return count

    board = [['.' for _ in range(n)] for _ in range(n)]
    col = [1 for _ in range(n)]
    diagonal_down = [1 for _ in range(2 * n - 1)]
    diagonal_up = [1 for _ in range(2 * n - 1)]
    return dfs(n, 0, board, col, diagonal_down, diagonal_up)


print(totalNQueens(1))
print(totalNQueens(2))
print(totalNQueens(3))
print(totalNQueens(4))
print(totalNQueens(5))
print(totalNQueens(6))
print(totalNQueens(7))
print(totalNQueens(8))
print(totalNQueens(9))