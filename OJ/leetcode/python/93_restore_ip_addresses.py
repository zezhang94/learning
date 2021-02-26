from typing import List
class Solution:
    
    def remainValid(self, group: int, s: str) -> bool:
        if group == 1 and 4 <= len(s) <= 12 or \
            group == 2 and 3 <= len(s) <= 9 or \
            group == 3 and 2 <= len(s) <= 6 or \
            group == 4 and 1 <= len(s) <= 3:
            return True
        else:
            return False

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) < 4 or len(s) > 12:
            return ans
        self.dfs(1, s, "", ans)
        return ans

    def dfs(self, group: int, s: str, ip: str, ans: List[str]) -> None:
        print(s, ip)
        if group > 4:
            ans.append(ip)
            return
        for i in range(1, 4):
            prefix = s[:i]
            if not self.remainValid(group - 1, s[i:]):
                print("")
                return
            value = int(prefix)
            if i > 1 and (value == 0 or value // (i - 1) * 10 == 0) or value > 255:
                return 
            self.dfs(group + 1, s[i:], ip + prefix + ".", ans)

solution = Solution()
print(solution.restoreIpAddresses("25525511135"))