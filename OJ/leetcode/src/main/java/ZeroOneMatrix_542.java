public class ZeroOneMatrix_542 {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] ans = new int[m][n];

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    continue;
                }
                ans[i][j] = 10000;
                if (i > 0) {
                    ans[i][j] = Math.min(ans[i][j], ans[i - 1][j] + 1);
                }
                if (j > 0) {
                    ans[i][j] = Math.min(ans[i][j], ans[i][j - 1] + 1);
                }
            }
        }

        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (matrix[i][j] == 0) {
                    continue;
                }
                if (i < m - 1) {
                    ans[i][j] = Math.min(ans[i][j], ans[i + 1][j] + 1);
                }
                if (j < n - 1) {
                    ans[i][j] = Math.min(ans[i][j], ans[i][j + 1] + 1);
                }
            }
        }

        return ans;
    }
}
