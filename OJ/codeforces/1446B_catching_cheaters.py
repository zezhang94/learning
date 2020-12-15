'''
Definition:
    S(C, D) = 4 * LCS(C, D) - |C| - |D|
    |X| = len(X)
    substring: consequent characters in string
    C is a substring of A
    D is a substring of B
Target:
    maximal S(C, D) for all pairs (C, D)
Solution:
    dp[i][j]: optimal solution for C ends with A[i], D end withs B[j]
    dp[i][j] = {
        # 4 - 1 - 1 = 2
        dp[i - 1][j - 1] + 2   if A[i] = A[j]
        max(dp[i - 1][j], dp[i][j - 1]) - 1   if A[i] != A[j]
    }
'''

input()
A = input().strip()
B = input().strip()
na, nb = len(A), len(B)
DP = [[0 for j in range(nb + 1)] for i in range(na + 1)]
maximum = float('-inf')
for i in range(1, na + 1):
    for j in range(1, nb + 1):
        if A[i - 1] == B[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 2
        else:
            DP[i][j] = max(DP[i][j], DP[i - 1][j] - 1, DP[i][j - 1] - 1)
        maximum = max(maximum, DP[i][j])
print(maximum)