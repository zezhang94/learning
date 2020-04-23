# Write a program which takes an array of n integers, 
# where A[i] denotes the maximum you can advance from index i, 
# and returns whether it is possible to advance to the last index starting 
# from the beginning of the array.

def advancing(A):
  T, R = [len(A) - 1], []
  while len(T) > 0:
    for i in range(0, len(T)):
      for j in reversed(range(T[i])):
        if A[j] >= T[i] - j:
          if j == 0:
            return True
          R.append(j)
    T, R = R, []
  return False

if __name__ == "__main__":
    A = [3, 3, 1, 0, 2, 0, 1]
    print(advancing(A))
    A = [3, 2, 0, 0, 2, 0, 1]
    print(advancing(A))
    A = [1, 1, 1, 1, 1, 1, 1]
    print(advancing(A))
    A = [0, 12, 1, 1, 1, 1, 1]
    print(advancing(A))
