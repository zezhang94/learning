def removeInvalidParentheses(s):
    def calculate(s):
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')' and l == 0:
                r += 1
            elif c == ')' and l > 0:
                l -= 1
        return (l, r)
                
    def isValid(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def dfs(start, l, r, s, ans):
        if l == 0 and r == 0:
            if isValid(s):
                ans.append(s)
            return
        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            if s[i] == '(' and l > 0:
                ss = s[:i] + s[(i + 1):]
                dfs(i, l - 1, r, ss, ans)
            elif s[i] == ')' and r > 0:
                ss = s[:i] + s[(i + 1):]
                dfs(i, l, r - 1, ss, ans)

    l, r = calculate(s)
    ans = []
    dfs(0, l, r, s, ans)
    return ans

print(removeInvalidParentheses("()())()"))
print(removeInvalidParentheses("(a)())()"))
print(removeInvalidParentheses(")("))
                