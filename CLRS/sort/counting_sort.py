import random

# Eelements of array are in range 0 to 1.
def counting_sort(A, k):
    R = [-1] * len(A)
    C = [0] * (k + 1)
    # number of elements equal to i
    for i in range(0, len(A)):
        C[A[i]] += 1
    # number of elements less or equal to i
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    # unstable
    # for i in range(0, len(A)):
    # unstable
    for i in range(len(A) - 1, -1, -1):
        R[C[A[i]] - 1]= A[i]
        C[A[i]] -= 1
    return R

if __name__ == "__main__":
    k = 10
    A = [None] * 20
    for i in range(0, 20):
        A[i] = random.randint(0, k)
    print(A)
    print(counting_sort(A, k))

    