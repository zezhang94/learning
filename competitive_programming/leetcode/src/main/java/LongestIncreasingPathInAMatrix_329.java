import java.util.Arrays;

public class LongestIncreasingPathInAMatrix_329 {

    private static final int[] direction = {0, -1, 0, 1, 0};
    private static int m;
    private static int n;

    private int searchWithMemory(int ri, int rj, int[][] memo, int[][] matrix) {
        if (memo[ri][rj] > 0) {
            return memo[ri][rj];
        }
        memo[ri][rj] = 1;
        for (int k = 0; k < 4; ++k) {
            int i = ri + direction[k];
            int j = rj + direction[k + 1];
            if (i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] <= matrix[ri][rj]) {
                continue;
            }
            memo[ri][rj] = Math.max(searchWithMemory(i, j, memo, matrix) + 1, memo[ri][rj]);
        }
        return memo[ri][rj];
    }

    public int longestIncreasingPath(int[][] matrix) {
        m = matrix.length;
        n = matrix[0].length;
        int[][] memo = new int[m][n];
        int maximum = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                maximum = Math.max(searchWithMemory(i, j, memo, matrix), maximum);
            }
        }
        return maximum;
    }
}
