import java.util.Random;

public class KthLargestElementInAnArray_215 {

    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        quicksort(nums, 0, n - 1);
        for (int v : nums) {
            System.out.print(v + " ");
        }
        System.out.println();
        return nums[k - 1];
        /*
        for (int index = (n - 1) / 2; index >= 0; --index) {
            heapify(nums, index, n);
        }

        int count = 1;
        while (count < k) {
            swap(nums, n - count, 0);
            heapify(nums, 0, n - count);
            ++count;
        }
        return nums[0];
         */
    }

    private void heapify(int[] nums, int root, int heap_size) {
        while (true) {
            int li = left(root);
            int ri = right(root);
            int large = root;
            if (li < heap_size && nums[li] > nums[large]) {
                large = li;
            }
            if (ri < heap_size && nums[ri] > nums[large]) {
                large = ri;
            }
            if (large == root) {
                System.out.println();
                return;
            }
            swap(nums, large, root);
            root = large;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private int left(int i) {
        return 2 * i + 1;
    }

    private int right(int i) {
        return 2 * i + 2;
    }

    private Random random = new Random();
    private void quicksort(int[] nums, int l, int r) {
        if (l < r) {
            int p = partition(nums, l, r);
            quicksort(nums, l, p - 1);
            quicksort(nums, p + 1, r);
        }
    }

    private int partition(int[] nums, int l, int r) {
        swap(nums, random.nextInt(r - l + 1) + l, r);
        int cur = l;
        for (int i = l; i < r; ++i) {
            if (nums[i] > nums[r]) {
                swap(nums, i, cur++);
            }
        }
        swap(nums, r, cur);
        return cur;
    }
}
