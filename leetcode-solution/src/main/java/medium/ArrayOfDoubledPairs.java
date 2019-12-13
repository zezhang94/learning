package medium;

/**
 * # 954
 * Given an array of integers A with even length, 
 * return true if and only if it is possible to reorder it such that 
 * A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.
 * 
 * Example 1:
 *  Input: [3,1,3,6]
 *  Output: false
 * 
 * Example 2:
 *  Input: [2,1,2,6]
 *  Output: false
 *
 * Example 3:
 *  Input: [4,-2,2,-4]
 *  Output: true
 *  Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
 * 
 * Example 4:
 *  Input: [1,2,4,16,8,4]
 *  Output: false
 * 
 * Note:
 *  0 <= A.length <= 30000
 *  A.length is even
 *  -100000 <= A[i] <= 100000
 */
public class ArrayOfDoubledPairs {

    public boolean canReorderDoubled(int[] A) {
        quickSort(A, 0, A.length);
        for (int i = 0; i != A.length; ++i) {
            if (A[i] <= 100000) {
                int target = binarySearch(A, i + 1, A.length - 1, A[i] >= 0 ? 2 * A[i] : A[i] / 2);
                if (target == -1) {
                    return false;
                }
                A[i] = 100001;
                A[target] = 100001;
            }
        }
        return true;
    }

    private int orderSearch(int[] A, int start, int end, int target) {
        for (int index = start; index <= end; ++index) {
            if (A[index] == target) {
                return index;
            }
        }
        return -1;
    }

    private int binarySearch(int[] A, int start, int end, int target) {
        int diff;
        int index;
        while (start <= end) {
            int middle = (start + end) / 2;

            if (A[middle] == 100001 && middle - 1 >=0 && middle + 1 <= end) {
                if (A[middle - 1] <= target) {
                    middle = middle + 1;
                } else if (A[middle + 1] >= target) {
                    middle = middle - 1;
                }
            }

            if (A[middle] == target) {
                index = middle;
                diff = 1;
                while (index - diff >= 0) {
                    if (A[index - diff] == 100001) {
                        diff++;
                        continue;
                    }

                    if (A[index] == A[index - diff]) {
                        middle = index - diff;
                    } else {
                        break;
                    }
                }
                return middle;
            }

            if (A[middle] < target) {
                start = middle + 1;
            } else {
                end = middle - 1;
            }
        }
        return -1;
    }

    private void quickSort(int[] A, int start, int end) {
        if (start < end) {
            int pivot = A[end - 1];
            int pivotLocation = start - 1;
            for (int index = start; index < end; ++index) {
                if (pivot > A[index]) {
                    int temp = A[++pivotLocation];
                    A[pivotLocation] = A[index];
                    A[index] = temp;
                }
            }
            int pivotIndex = pivotLocation + 1;

            A[end - 1] = A[pivotIndex];
            A[pivotIndex] = pivot;

            quickSort(A, start, pivotIndex);
            quickSort(A, pivotIndex + 1, end);
        }
    }
}