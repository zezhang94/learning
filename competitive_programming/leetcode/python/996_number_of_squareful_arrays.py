import math
def numSquarefulPerms(A):
    def dfs(stack, used, ans, t, A):
        if len(stack) == len(A):
            ans[0] += 1
            return

        for i in range(len(A)):
            if i > 0 and A[i] == A[i - 1] and not used & 1 << i - 1:
                continue
            if not used & 1 << i:
                if len(stack) == 0 or t[stack[-1]][i]:
                    stack.append(i)
                    dfs(stack, used | 1 << i, ans, t, A)
                    stack.pop()

    A.sort()
    n = len(A)
    t = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t[i][j] = (math.sqrt(A[i] + A[j]) // 1) ** 2 == A[i] + A[j] if i < j else t[j][i]

    ans = [0]
    dfs([], 0, ans, t, A)
    return ans[0]

print(numSquarefulPerms([1, 17, 8]))
print(numSquarefulPerms([2, 2, 2]))