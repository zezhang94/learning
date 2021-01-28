def solveSudoku(board) -> None:
    def getCandidates(board, x, y):
        candidates = [True for _ in range(10)]
        candidates[0] = False
        for i in range(9):
            if board[i][y] != ".":
                candidates[int(board[i][y])] = False
            if board[x][i] != ".":
                candidates[int(board[x][i])] = False
        x //= 3
        y //= 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if board[i][j] != ".":
                    candidates[int(board[i][j])] = False
        return [str(i) for i in range(10) if candidates[i]]

    def dfs(i_start, j_start, count, board):
        if count == 0:
            for line in board:
                print(line)
            return

        if i_start == j_start == 9:
            for line in board:
                print(line)
        for i in range(i_start, 9):
            for j in range(j_start, 9):
                if board[i][j] == '.':
                    print(i, j)
                    candidates = getCandidates(board, i, j)
                    for v in candidates:
                        board[i][j] = v
                        dfs(i, j + 1, count - 1, board)
                        board[i][j] = "."

    count = 0
    for line in board:
        for s in line:
            if s == ".":
                count += 1
    dfs(0, 0, count, board)
    print(getCandidates(board, 0, 2))


board = [ \
    ["5","3",".",".","7",".",".",".","."], \
    ["6",".",".","1","9","5",".",".","."], \
    [".","9","8",".",".",".",".","6","."], \
    ["8",".",".",".","6",".",".",".","3"], \
    ["4",".",".","8",".","3",".",".","1"], \
    ["7",".",".",".","2",".",".",".","6"], \
    [".","6",".",".",".",".","2","8","."], \
    [".",".",".","4","1","9",".",".","5"], \
    [".",".",".",".","8",".",".","7","9"]  \
]
solveSudoku(board)
    