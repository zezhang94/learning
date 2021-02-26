/**
 * Main test.
 */
public class Main {

    public static void main(String[] args) {
        PartitionToKEqualSumSubsets_698 solution = new PartitionToKEqualSumSubsets_698();

        int[] nums = new int[]{4, 3, 2, 3, 5, 2, 1};
        int k = 4;
        System.out.println(solution.canPartitionKSubsets(nums, k));

        nums = new int[]{4, 5, 3, 2, 5, 5, 1, 3, 5, 5, 5, 5, 5, 2, 5};
        k = 12;
        System.out.println(solution.canPartitionKSubsets(nums, k));

        nums = new int[]{2, 2, 2, 2, 3, 4, 5};
        k = 4;
        System.out.println(solution.canPartitionKSubsets(nums, k));
    }
}