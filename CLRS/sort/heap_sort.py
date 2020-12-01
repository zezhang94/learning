class Heap:
    def __init__(self, A):
        self.A = A
        self.heap_size = len(A) 

    def parent(self, i):
        return (i - 1) // 2
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2

    def max_heapify_recursive(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and A[l] > A[i]:
            largest = l
        if r < self.heap_size and A[r] > A[largest]:
            largest = r
        if i != largest:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify_recursive(A, largest)

    def max_heapify_iterative(self, index):
        largestIndex = index
        while True:
            l = self.left(largestIndex)
            r = self.right(largestIndex)
            if l < self.heap_size and A[l] > A[largestIndex]:
                largestIndex = l
            if r < self.heap_size and A[r] > A[largestIndex]:
                largestIndex = r
            if largestIndex != index:
                A[index], A[largestIndex] = A[largestIndex], A[index]
                index = largestIndex
            else:
                return

    def build_max_heap(self):
        for i in range((self.heap_size - 1) // 2, -1, -1):
            self.max_heapify_iterative(i)
            #max_heapify_recursive(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.heap_size - 1, 0, -1):
            A[i], A[0] = A[0], A[i]
            self.heap_size -= 1
            self.max_heapify_iterative(0)
        
if __name__ == "__main__":
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap(A)
    heap.heap_sort()
    print(heap.A)