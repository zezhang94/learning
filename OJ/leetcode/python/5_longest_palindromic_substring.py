from typing import List
class Solution:
    def __init__(self):
        self.n = 0

    def longestPalindrome(self, s: str) -> str:
        self.n = len(s)
        arr = [ch for ch in s]
        maxLength = 0
        start = 0
        for i in range(self.n):
            length = max(self.getLenFromCenter(i, i, arr), 
                self.getLenFromCenter(i, i + 1, arr))
            if length > maxLength:
                maxLength = length
                start = i - (maxLength - 1) // 2
        return "".join([arr[i] for i in range(start, start + maxLength)])

    def getLenFromCenter(self, center1: int, center2: int, arr: List[str]) -> int:
        l, r = center1, center2
        while l >= 0 and r < self.n and arr[l] == arr[r]:
            l -= 1
            r += 1
        return r - l - 1

solution = Solution()
print(solution.longestPalindrome("aaaaa"))
print(solution.longestPalindrome("ababa"))
print(solution.longestPalindrome("abcdef"))
print(solution.longestPalindrome("abacdcc"))
print(solution.longestPalindrome("accb"))