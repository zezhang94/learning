'''
    Definition:
        a1, a2, a3, ..., an = 0 or 1
        p: first land index
        k: span
        x: time to add
        y: time to remove (only remove from beginning)
    Description:
        step1: p
        step2: p + k
        step3: p + 2k
        ...
        stepm: p + mk
    Target:
        jump across an
        minimum cost of add and remove
    Examples:
        n p k
        A
        x y
        result

        10 3 2
        0101010101
        2 2
        2

        5 4 1
        00000
        2 10
        4

        11 2 3
        10110011000
        4 3
        10
    Comment:
        Dp as an auxiliary.
'''

import sys

def bouncing_ball(A, p, k, x, y):
    n = len(A)
    C = [0] * n
    # dynamic programming
    for i in range(n - 1, -1, -1):
        if i + k > n - 1:
            C[i] = 1 - A[i]
        else:
            C[i] = C[i + k] + 1 - A[i]

    # brute force
    minimum = float('inf')
    upper, p = n - p + 1, p - 1
    for d in range(upper):
        q = p + d
        cost = d * y + C[q] * x
        if cost < minimum:
            minimum = cost
    
    return minimum

if __name__ == "__main__":
    input = sys.stdin.readline
    cases = int(input())
    results = [None] * cases
    for case in range(cases):
        line = input()
        n, p, k = [int(x) for x in line.split()]
        line = input()
        line = line.strip()
        A = [int(x) for x in line]
        line = input()
        x, y = [int(x) for x in line.split()]
        results[case] = bouncing_ball(A, p, k, x, y)

    for result in results:
        print(str(result))

