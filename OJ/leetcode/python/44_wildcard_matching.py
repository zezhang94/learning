def isMatch(s, p):
    # remove * from p
    p = p.replace('*', '')
    if p == "":
        return True
    

print(isMatch("aaaa", "*"))