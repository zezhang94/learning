from enum import Enum

class Direction(Enum):
    LEFT_UP = 1
    UP = 2
    LEFT = 3

# theta(mn)
def LCS_length(X, Y, B, C):
    nx, ny = len(X), len(Y)
    row, col = nx + 1, ny + 1
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                C[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = Direction['LEFT_UP']
            elif X[i - 1] != Y[j - 1]:
                if C[i - 1][j] >= C[i][j - 1]:
                    C[i][j] = C[i - 1][j]
                    B[i][j] = Direction['UP']
                else:
                    C[i][j] = C[i][j - 1]
                    B[i][j] = Direction['LEFT']                   

def rebuid_solution(X, Y, B, C, m, n):
    print("LCS length:", C[m][n])
    result = [''] * C[m][n]
    count = C[m][n]
    while count > 0:
        if B[m][n] is Direction.LEFT_UP:
            result[count - 1] = X[m - 1]
            m, n, count = m - 1, n - 1, count - 1
        elif B[m][n] is Direction.LEFT:
            n -= 1
        else:
            m -= 1
    print("LCS:", "".join(result))
    ''' longest monotonically increasing subsequence (square complexity)
    print("LCS:", result)
    '''

if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    ''' longest monotonically increasing subsequence (square complexity)
    X = [8, 7, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0,]
    Y = sorted(X)
    '''
    row, col = len(X) + 1, len(Y) + 1
    C = [[-1 for j in range(col)] for i in range(row)]
    B = [[None for j in range(col)] for i in range(row)]
    LCS_length(X, Y, B, C)
    rebuid_solution(X, Y, B, C, len(X), len(Y))           