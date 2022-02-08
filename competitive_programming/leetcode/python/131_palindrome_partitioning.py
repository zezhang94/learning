from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False for _ in s] for _ in s]
        n = len(s)
        for step in range(n):
            for i in range(n):
                j = i + step
                if j >= n:
                    break
                if step == 0:
                    dp[i][j] = True
                elif step == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        ans = []
        self.dfs(0, [], ans, s, dp)
        return ans
    
    def dfs(self, start: int, stack: List[str], ans: List[List[str]], s: str, dp: List[List[bool]]) -> None:
        if start == len(s):
            ans.append(stack[:])
        for i in range(start, len(s)):
            if dp[start][i]:
                stack.append(s[start : (i + 1)])
                self.dfs(i + 1, stack, ans, s, dp)
                stack.pop()

def printAns(ans: List[List[str]]):
    print("--------------------------------")
    for line in ans:
        print(line)

solution = Solution()
ans = solution.partition("aab")
printAns(ans)


solution = Solution()
ans = solution.partition("aaaaaaaaaaaaaaaa")
print(len(ans))
