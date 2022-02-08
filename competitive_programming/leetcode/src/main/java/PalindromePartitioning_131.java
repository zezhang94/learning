import java.util.ArrayList;
import java.util.List;

public class PalindromePartitioning_131 {

    public List<List<String>> partition(String s) {
        int n = s.length();
        List<List<String>> ans = new ArrayList<>();
        boolean[][] dp = new boolean[n][n];
        solveDP(dp, s);
        dfs(0, new ArrayList<>(), ans, dp, n, s);
        return ans;
    }

    private void dfs(int start, List<String> stack, List<List<String>> ans, boolean[][] dp, int n, String s) {
        if (start == n) {
            ans.add(new ArrayList<>(stack));
            return;
        }

        for (int i = start; i < n; ++i) {
            if (dp[start][i]) {
                stack.add(s.substring(start, i + 1));
                dfs(i + 1, stack, ans, dp, n, s);
                stack.remove(stack.size() - 1);
            }
        }
    }

    private void solveDP(boolean[][] dp, String s) {
        int n = s.length();
        for (int step = 0; step < n; ++step) {
            for (int i = 0; i < n; ++i) {
                int j = i + step;
                if (j >= n) {
                    break;
                }
                if (step == 0) {
                    dp[i][j] = true;
                } else if (step == 1) {
                    dp[i][j] = s.charAt(i) == s.charAt(j);
                } else {
                    dp[i][j] = dp[i + 1][j - 1] && s.charAt(i) == s.charAt(j);
                }
            }
        }
    }
}
