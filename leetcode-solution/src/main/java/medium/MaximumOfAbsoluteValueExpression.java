package medium;

/**
 * # 1131
 * Given two arrays of integers with equal lengths, return the maximum value of:
 *  |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
 * where the maximum is taken over all 0 <= i, j < arr1.length.
 * 
 * Example 1:
 *  Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
 *  Output: 13
 * 
 * Example 2:
 *  Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
 *  Output: 20
 * 
 * Constraints:
 *  2 <= arr1.length == arr2.length <= 40000
 *  -10^6 <= arr1[i], arr2[i] <= 10^6
 * 
 * Hints:
 *   Manhattan distance 
 *   Chebyshev distance
 */
public class MaximumOfAbsoluteValueExpression {

    public int stupidWay(int[] arr1, int[] arr2) {

        int max = 0;
        int temp;
        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr1.length; j++) {
                temp = 0;
                temp += i - j >= 0 ? i - j : j -i;
                temp += arr1[i] - arr1[j] >= 0 ? arr1[i] - arr1[j] : arr1[j] - arr1[i];
                temp += arr2[i] - arr2[j] >= 0 ? arr2[i] - arr2[j] : arr2[j] - arr2[i];
                if (temp > max) {
                    max = temp;
                }
            }
        }
        return max;
        
    }

    // TODO: Simpler solution.
    
}