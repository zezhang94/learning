def solveSudoku(board) -> None:
    def dfs(depth, pairs, row, col, box, board):
        if depth == len(pairs):
            return True

        i = pairs[depth][0]
        j = pairs[depth][1]
        for v in range(1, 10):
            if row[i][v] and col[j][v] and box[i // 3 * 3 + j // 3][v]:
                board[i][j] = str(v)
                row[i][v] = 0
                col[j][v] = 0
                box[i // 3 * 3 + j // 3][v] = 0
                # Tip: cast result, not recover
                if dfs(depth + 1, pairs, row, col, box, board):
                    return True
                board[i][j] = "."
                row[i][v] = 1
                col[j][v] = 1
                box[i // 3 * 3 + j // 3][v] = 1
        return False

    row = [[1 for _ in range(10)] for _ in range(9)]
    col = [[1 for _ in range(10)] for _ in range(9)]
    box = [[1 for _ in range(10)] for _ in range(9)]
    pairs = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                pairs.append((i, j))
            else:
                index = int(board[i][j])
                row[i][index] = 0
                col[j][index] = 0
                # Tip: flat to one-dimestion 
                box[i // 3 * 3 + j // 3][index] = 0 
    dfs(0, pairs, row, col, box, board)


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
for line in board:
    print(line)
    