"""
Printing neatly
    L = [l1, l2, ..., ln]: words length list
    or W = [w1, w2, ..., wn]: words list
    M: maximum characters one line can contain

cost(i) {
    i = 0, 0
    i > 0, min(C[k − 1] + S[k, i]) (0 <= k <= i)
}

first(i): first character in line

reference: https://alumni.media.mit.edu/~dlanman/courses/cs157/HW5.pdf

"""


def calculate_l_sum(L, L_SUM):
    n = len(L)
    for step in range(n):
        for i in range(n):
            j = i + step
            if j >= n:
                break
            elif i == j:
                L_SUM[i][j] = L[i]
            else:
                L_SUM[i][j] = L_SUM[i][j - 1] + L[j]
    
def printing_neatly(W, M, FIRST):
    L = [len(w) for w in W]
    n = len(W)
    COST = [float('inf') for i in range(n)]
    COST[0] = 0
    L_SUM = [[-1 for j in range(n)] for i in range(n)]
    calculate_l_sum(L, L_SUM)

    for i in range(1, n):

        for k in range(i, -1, -1):                
            tail_sum = (M - (i - k) - L_SUM[k][i]) ** 3
            if tail_sum < 0:
                break
            
            pre_cost = 0
            if k - 1 < 0:
                pre_cost = 0
            else:
                pre_cost = COST[k - 1]
            
            if i != n - 1:
                cost = tail_sum + pre_cost
            else:
                cost = pre_cost
            
            cost = tail_sum + pre_cost

            if cost < COST[i]:
                COST[i] = cost
                FIRST[i] = k
 
    '''
    for i in range(n):
        print(L_SUM[i])
    print()
    for i in range(n):
        print(COST[i])
    print()
    for i in range(n):
        print(i, FIRST[i])
    '''

    return list(FIRST)

def print_paragraph(W, FIRST, M):
    start = 1
    for k in range(start, 0, -1):
        print("-" * M)
        LINES = []
        i = len(W) - k
        j = len(W) - (k - 1)
        while i > 0:
            LINES.insert(0, W[FIRST[i]:j])
            j = FIRST[i]
            i = j - 1
        for i in range(len(LINES)):
            print(" ".join(LINES[i]))

if __name__ == "__main__":
    M = 64
    file = open("paragraph.txt", "r")
    content = file.read()
    #content = "aa aaaa aa aaAA aaaaa a aaa"
    content.index
    W = content.split()
    n = len(W)
    FIRST = [-1 for i in range(n)]
    FIRST[0] = 0
    printing_neatly(W, M, FIRST)
    print_paragraph(W, FIRST, M)
    





