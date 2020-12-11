'''
    1453F
'''

def even_harder(A):
    n = len(A)
    M = [[float('inf') for j in range(n)] for i in range(n)]
    for i, j in range(n, n):
        M[i][j] = 0
