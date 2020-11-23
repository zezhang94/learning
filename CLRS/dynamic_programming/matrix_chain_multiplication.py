def matrix_multiply(A, B):
    """
        m*n x n*p = m*p
    """
    if len(A[0]) != len[B]:
        return None
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    ROW = [0] * p
    C = [ROW] * m
    for r in range(m):
        for c in range(p):
            for i in range(n):
                C[r][c] += A[r][i] + B[i][c] # Compute m*n*p times.
    return C

def matrix_chain_order(P, m, s):
    n = len(P)
    # bottom-up: smaller problem first
    for step in range(n - 1):
        for i in range(1, n - step): 
            j = i + step 
            if step == 0:
                m[i][j] = 0
                continue
            minimun = -1
            for k in range(i, j):
                times = m[i][k] + m[k + 1][j] + P[i - 1] * P[k] * P[j]
                if times < m[i][j]:
                    m[i][j] = times
                    s[i][j] = k

def print_optimal_parens(s, start, end):
    if start == end:
        print("A" + str(start), end='')
    else:
        print("(", end='')
        str(print_optimal_parens(s, start, s[start][end]))
        str(print_optimal_parens(s, s[start][end] + 1, end))
        print(")", end='')


if __name__ == "__main__":
    P = [30, 35, 15, 5, 10, 20, 25]
    n = len(P)
    m = [[float('inf') for x in range(n)] for y in range(n)] 
    s = [[-1 for x in range(n)] for y in range(n)]

    matrix_chain_order(P, m, s)

    print("------ times ------")
    for i in range(len(m)):
        print(m[i])
    print("------ order ------")
    for i in range(len(s)):
        print(s[i])

    print_optimal_parens(s, 1, n - 1)