#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string dpSolution(string s) {
        int n = s.size();
        int start = 0, end = 0;
        vector<vector<bool>> dp(n, vector<bool>(n));
        // initialize
        for (int i = 0; i < n; ++i) {
            dp[i][i] = true;
            if (i < n - 1) {
                dp[i][i + 1] = s[i] == s[i + 1];
                if (dp[i][i + 1]) {
                    start = i;
                    end = i + 1;
                }
            }
        }
        for (int step = 2; step < n; ++step) {
            for (int i = 0; i + step < n; ++i) {
                int j = i + step;
                if (dp[i + 1][j - 1] && s[i] == s[j]) {
                    dp[i][j] = true;
                    start = i;
                    end = j;
                } else {
                    dp[i][j] = false;
                }
            }
        }
        return s.substr(start, end - start + 1);
    }

    string diffusionSolution(string s) {
        n = s.size();
        int start = 0, ans_len = 1;
        for (int i = 0; i < n; ++i) {
            int len = max(extendFromCenter(i, i, s), extendFromCenter(i, i + 1, s));
            if (len > ans_len) {
                start = i - (len - 1) / 2;
                ans_len = len;
            }
        }
        return s.substr(start, ans_len);
    }

private:
    int n;

    int extendFromCenter(int l, int r, string s) {
        while (l >= 0 && r < n && s[l] == s[r]) {
            --l;
            ++r;
        }
        return r - l - 1;
    }
};

int main() {
    Solution *solution = new Solution();
    string s;
    
    s = "babad";
    cout << solution->dpSolution(s) << "\n";
    cout << solution->diffusionSolution(s) << "\n";

    s = "cbbd";
    cout << solution->dpSolution(s) << "\n";
    cout << solution->diffusionSolution(s) << "\n";

    s = "a";
    cout << solution->dpSolution(s) << "\n";
    cout << solution->diffusionSolution(s) << "\n";

    s = "ac";
    cout << solution->dpSolution(s) << "\n";\
    cout << solution->diffusionSolution(s) << "\n";

    s = "ccc";
    cout << solution->dpSolution(s) << "\n";
    cout << solution->diffusionSolution(s) << "\n";
}