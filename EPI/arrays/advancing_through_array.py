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

def advancing_on(A):
  f = 0
  for i in range(0, len(A)):
    f = max(f, A[i] + i)
    if f <= i and i < len(A) - 1:
      return False
  return True

# Write a program to compute the minimum number of steps needed to 
# advance to the last location.
def variant(A):

  f, count, last, step = 0, 1, len(A) - 1, []
  for i in range(0, len(A)):
    if f < A[i] + i:
      f = A[i] + i
      step.append((i, f))
    if f <= i and i < last:
      return -1
    if f >= last:
      s, j = step[0], 1      
      while j < len(step):
        if s[1] - step[j][0] < 0:  # farthest step from previous step 
          count += 1
          s = step[j - 1]
        else:
          j += 1
      return count + 1
          
           

if __name__ == "__main__":
    A = [3, 3, 1, 0, 2, 0, 1]
    print(A, advancing_on(A), variant(A))
    A = [3, 2, 0, 0, 2, 0, 1]
    print(A, advancing_on(A), variant(A))
    A = [1, 1, 1, 1, 1, 1, 1]
    print(A, advancing_on(A), variant(A))
    A = [1, 12, 1, 1, 1, 1, 1]
    print(A, advancing_on(A), variant(A))
    A = [2, 2, 0, 0, 0, 1, 1]
    print(A, advancing_on(A), variant(A))
    A = [2, 3, 3, 1, 1, 1, 1]
    print(A, advancing_on(A), variant(A))
    A = [2, 3, 3, 1, 0, 0, 1]
    print(A, advancing_on(A), variant(A))
    A = [1, 2, 2, 5, 0, 0, 0, 0, 0]
    print(A, advancing_on(A), variant(A))
    A = [1, 2, 2, 5, 0, 0, 0, 0, 0, 0]
    print(A, advancing_on(A), variant(A))
    