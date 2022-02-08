import java.util.ArrayList;
import java.util.List;

public class RestoreIPAddresses_93 {

    public List<String> restoreIpAddresses(String s) {
        List<String> ans = new ArrayList<>(32);
        if (s.length() > 12) {
            return ans;
        }
        dfs(1, "", s, ans);
        return ans;
    }

    private void dfs(int group, String ip, String s, List<String> ans) {
        if (group > 4 && s.length() == 0) {
            ans.add(ip.substring(0, ip.length() - 1));
            return;
        }
        if (!lengthValid(group, s)) {
            return;
        }
        for (int i = 1; i <= 4; ++i) {
            String prefix = s.substring(0, i);
            int value = Integer.parseInt(prefix);
            if (prefix.charAt(0) == '0' && i == 1 || prefix.charAt(0) != '0' && value > 0 && value < 256) {
                dfs(group + 1, ip + prefix + '.', s.substring(i), ans);
            }
            if (i >= s.length()) {
                return;
            }
        }
    }

    private boolean lengthValid(int group, String s) {
        return group == 1 && s.length() >= 4 && s.length() <= 12 ||
                group == 2 && s.length() >= 3 && s.length() <= 9 ||
                group == 3 && s.length() >= 2 && s.length() <= 6 ||
                group == 4 && s.length() >= 1 && s.length() <= 3;
    }

}
