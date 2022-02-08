from typing import List

class Solution:
    def remainValid(self, group: int, s: str) -> bool:
        if group == 1 and 3 <= len(s) <= 9 or \
            group == 2 and 2 <= len(s) <= 6 or \
            group == 3 and 1 <= len(s) <= 3 or \
            group == 4 and len(s) == 0:
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
        if group > 4:
            ans.append(ip[:(len(ip) - 1)])
            return
        for i in range(1, 4):
            prefix = s[:i]
            if i > len(s):
                break
            if not self.remainValid(group, s[i:]):
                continue
            value = int(prefix)
            if value <= 255 and (value == 0 and i == 1 or prefix[0] != "0"):
                self.dfs(group + 1, s[i:], ip + prefix + ".", ans)


solution = Solution()
print(solution.restoreIpAddresses("1111"))
print(solution.restoreIpAddresses("25525511135"))
print(solution.restoreIpAddresses("0000"))
print(solution.restoreIpAddresses("010010"))
print(solution.restoreIpAddresses("101023"))