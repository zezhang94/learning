import random

def partition(A, p, r):
    x = A[r]
    i, j = p - 1, p
    while j <= r - 1:
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

if __name__ == "__main__":
    A = [i for i in range(0, 10)]
    random.shuffle(A)
    print(A)
    quicksort(A, 0, len(A) - 1)
    print(A)