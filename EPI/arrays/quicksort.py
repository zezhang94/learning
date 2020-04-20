import random
import unittest

def partition(A, s, e):
    i, j, x = s, e - 2, A[e - 1]
    while i < j:
        if A[i] > x:
            A[j], A[i] = A[i], A[j]
            j -= 1
        else:
            i += 1
    if A[j] > x:
        A[j], A[e - 1] = A[e - 1], A[j]
        return j
    else:
        A[j + 1], A[e - 1] = A[e - 1], A[j + 1]
        return j + 1

def partition_elegant(A, s, e):
    j, x = s - 1, A[e - 1]
    for i in range(s, e - 1):
        if A[i] <= x:
            j += 1
            A[i], A[j] = A[j], A[i]
    A[j + 1], A[e - 1] = A[e - 1], A[j + 1]
    return j + 1
    


def quicksort(A, s, e):
    if s < e - 1:
        pivot = partition_elegant(A, s, e)
        quicksort(A, s, pivot)
        quicksort(A, pivot + 1, e)

def main():
    A = [x for x in range(16)]
    random.shuffle(A)
    print(A)
    quicksort(A, 0, len(A))
    print(A)

if __name__ == "__main__":
    main()

class Test(unittest.TestCase):
    def test(self):
        A = [x for x in range(16)]
        for i in range(0, 100):
            random.shuffle(A)
            quicksort(A, 0, len(A))
            self.assertListEqual(A, [x for x in range(16)])