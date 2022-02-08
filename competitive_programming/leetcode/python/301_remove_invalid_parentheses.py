def dummyDfs(s):
    def dfs(start, l, r, target, stack, ans, s):
        if r > l:
            return
        if target == 0:
            if l == r:
                ans.append(stack)
            return

        for i in range(start, len(s)):
            # pruning, skip duplicate
            if i > start and s[i] == s[i - 1]:
                continue       
            stack += s[i]
            dl, dr = 0, 0
            if s[i] == '(':
                dl = 1
            elif s[i] == ')':
                dr = 1
            dfs(i + 1, l + dl, r + dr, target - 1, stack, ans, s)
            stack = stack[:-1]

    # remove all '(' at the end of string
    end = len(s)
    tail = ""
    while end >= 1 and s[end - 1] != ')':
        if s[end - 1].isalpha():
            tail = s[end - 1] + tail
        end -= 1
    s = s[:end] + tail
    if len(s) == 0:
        return [""]

    # calculate the least number of '(' or ')' has to be removed 
    l, r = 0, 0
    least = 0
    for c in s:
        if c == '(':
            l += 1
        elif c == ')':
            r += 1
        if r > l:
            least += 1
            r -= 1
    least += l - r
            
    ans = []
    start, l, r = 0, 0, 0
    dfs(start, l, r, len(s) - least, "", ans, s)
    return ans

print(dummyDfs("()())()"))
print(dummyDfs("(a)())()"))
print(dummyDfs(")("))
print(dummyDfs("(((("))
print(dummyDfs("))"))
print(dummyDfs(""))
print(dummyDfs("n"))
print(dummyDfs("(()"))