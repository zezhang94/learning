#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        n = s.size();
        vector<vector<string>> ans;
        vector<vector<bool>> dp(n, vector<bool>(n, true));
        constructDP(dp, s);
        vector<string> stack;
        dfs(0, s, stack, ans, dp);
        return ans;
    }

private:
    int n;

    void constructDP(vector<vector<bool>>& dp, const string& s) {
        for (int step = 1; step < n; ++step) {
            for (int i = 0; i < n; ++i) {
                int j = i + step;
                if (j >= n) {
                    break;
                }
                if (step == 1) {
                    dp[i][j] = s[i] == s[j];
                } else {
                    dp[i][j] = dp[i + 1][j - 1] && s[i] == s[j];
                }
            }
        }
    }

    void dfs(int start, string& s, vector<string>& stack, vector<vector<string>>& ans, const vector<vector<bool>>& dp) {
        if (start == n) {
            ans.push_back(stack);
            return;
        }
        for (int i = start; i < n; ++i) {
            if (dp[start][i]) {
                stack.push_back(s.substr(start, i - start + 1));
                dfs(i + 1, s, stack, ans, dp);
                stack.pop_back();
            }
        }
    }
};

void print(vector<vector<string>> vec) {
    cout << "--------------------------------\n";
    for (vector<string> line : vec) {
        for (string s : line) {
            cout << s << " ";
        }
        cout << "\n";
    }
}

int main() {
    Solution* solution = new Solution();
    vector<vector<string>> ans;

    ans = solution->partition("aab");
    print(ans);

    ans = solution->partition("a");
    print(ans);

    ans = solution->partition("aaaaaaaaaaaaaaaa");
    print(ans);
}
