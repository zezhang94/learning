package easy;

/*
 * 665
 * Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
 * We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
 *
 * Example 1:
 *  Input: [4,2,3]
 *  Output: True
 *  Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
 *
 * Example 2:
 *  Input: [4,2,1]
 *  Output: False
 *  Explanation: You can't get a non-decreasing array by modify at most one element.
 *
 * Note: The n belongs to [1, 10,000].
 */

public class NonDecreasingArray {

    public boolean checkPossibility(int[] nums) {
        int count = 0;

        if (null == nums || nums.length == 0) {
            return false;
        }

        if (nums.length <= 2) {
            return true;
        }

        for (int i = 0, j = i + 1, k = i + 2; i != nums.length - 2; ++i, ++j, ++k) {
            if (nums[i] <= nums[j] && nums[j] <= nums[k]) {
                // continue
            } else if (nums[i] <= nums[j] && nums[j] > nums[k]) {
                if (nums[i] < nums[k]) {
                    nums[j] = nums[i];
                } else {
                    nums[k] = nums[j];
                }
                ++count;
            } else if (nums[i] > nums[j] && nums[j] <= nums[k]) {
                ++count;
            } else {
                return false;
            }
        }

        if (count <= 1) {
             return true;
        } else {
            return false;
        }
    }

}
