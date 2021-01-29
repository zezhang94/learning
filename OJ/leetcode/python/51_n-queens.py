def solveNQueens(n):
    def isValid(i, j, col, diagonal_down, diagonal_up):
        return col[j] and diagonal_up[i + j] \
            and diagonal_down[len(col) - i - 1 + j]

    def dfs(i, diagonal_down, diagonal_up, col, board, ans, n):
        if i == n:
            ans.append(["".join(line) for line in board])
            return
        
        for j in range(n):
            if isValid(i, j, col, diagonal_down, diagonal_up):
                col[j] = 0
                diagonal_up[i + j] = 0
                diagonal_down[n - i - 1 + j] = 0
                board[i][j] = "Q"
                dfs(i + 1, diagonal_down, diagonal_up, col, board, ans, n)
                board[i][j] = "."
                diagonal_down[n - i - 1 + j] = 1
                diagonal_up[i + j] = 1
                col[j] = 1

    col = [1 for _ in range(n)]
    # diagonal from left-top to right-down 
    diagonal_down = [1 for _ in range(2 * n - 1)]
    # diagonal from left-down to right-up 
    diagonal_up = [1 for _ in range(2 * n - 1)]
    board = [["." for _ in range(n)] for _ in range(n)]
    ans = []
    dfs(0, diagonal_down, diagonal_up, col, board, ans, n)
    return ans

n = 5
ans = solveNQueens(n)
for line in ans:
    print("=" * n)
    for row in line:
        print(row)