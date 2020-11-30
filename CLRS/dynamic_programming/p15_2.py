import LCS

"""
Longest palindrome subsequence
    A palindrome is a nonempty string over some alphabet that reads the same 
    forward and backward. Examples of palindromes are all strings of length 1, 
    `civic`, `racecar`, and `aibohphobia` (fear of palindromes).
    Give an efficient algorithm to find the longest palindrome 
    that is a subsequence of a given input string. 
    For example, given the input `character`, your algorithm should return `carac`. 
    What is the running time of your algorithm?
    (Note: not a continuous sequence)
"""
def solve(S):
    _S = list(reversed(S))
    row, col = len(S) + 1, len(_S) + 1
    C = [[-1 for j in range(col)] for i in range(row)]
    B = [[None for j in range(col)] for i in range(row)]
    LCS.LCS_length(S, _S, B, C)
    LCS.rebuid_solution(S, _S, B, C, len(S), len(_S))

if __name__ == "__main__":
    str = "aibohphobia1111aibohphobia"
    S = [s for s in str]
    solve(S)
     

