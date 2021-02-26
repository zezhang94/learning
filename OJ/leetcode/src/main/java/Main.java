/**
 * Main test.
 */
public class Main {

    public static void main(String[] args) {
        LongestIncreasingPathInAMatrix_329 solution = new LongestIncreasingPathInAMatrix_329();

        int[][] matrix = {
                {9, 9, 4},
                {6, 6, 8},
                {2, 1, 1}
        };
        System.out.println(solution.longestIncreasingPath(matrix));


    }
}