import java.util.Arrays;

public class DecodeWays_91 {
    public int numDecodings(String s) {
        int n = s.length();
        if (s.charAt(0) == '0') {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n];
        dp[0] = 1;
        int head = Integer.parseInt(s.substring(0, 2));
        if (s.charAt(1) != '0') {
            dp[1]++;
        }
        if (10 <= head && head <= 26) {
            dp[1]++;
        }
        for (int i = 2; i < n; ++i) {
            if (s.charAt(i) != '0') {
                dp[i] += dp[i - 1];
            }
            int value = Integer.parseInt(s.substring(i - 1, i + 1));
            if (value >= 10 && value <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        return dp[n - 1];
    }
}
