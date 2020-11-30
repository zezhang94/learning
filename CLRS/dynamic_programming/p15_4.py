"""
Printing neatly
    L = [l1, l2, ..., ln]: words length list
    or W = [w1, w2, ..., wn]: words list
    M: maximum characters one line can contain

cost(i, j) {
    i == j, (M - L[i]) ** 3 
    j == n, min(cost(i, k))
    j < n,  min((M - (j - k - 1) - sum(k + 1, j, L)) ** 3 + cost(i, k)) 
}

last(i, j): last character in line
"""

def calculate_space(M, j, k, L, L_SUM):
    length = 0
    if L_SUM[j][k] != -1:
        length = L_SUM[j][k]
    else:
        for i in range(j, k + 1):
            length += L[i]
        L_SUM[j][k] = length
    return (M - (j - k) - length) ** 3

def printing_neatly(W, M):
    L = [len(w) for w in W]
    n = len(W)
    COST = [[float('inf') for j in range(n)] for i in range(n)]
    LAST = [[-1 for j in range(n)] for i in range(n)]
    L_SUM = [[-1 for j in range(n)] for i in range(n)]
    # initialize
    for i in range(n):
        COST[i][i] = (M - L[i]) ** 3
        LAST[i][i] = i
    COST[n - 1][n - 1] = 0

    for step in range(1, n - 1):
        for i in range(n):
            j = i + step
            if j >= n:
                break
            for k in range(i, j):
                tail_sum = calculate_space(M, j, k, L, L_SUM)
                if tail_sum < 0:
                    continue
                
                if j == n:
                    cost = COST[i][k - 1]
                else:
                    cost = tail_sum + COST[i][k - 1]
                if cost < COST[i][j]:
                    COST[i][j] = cost
                    LAST[i][j] = k
                


