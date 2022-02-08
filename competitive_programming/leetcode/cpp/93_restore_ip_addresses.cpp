#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        if (s.size() > 12 || s.size() < 4) {
            return ans;
        }
        dfs(1, "", s, ans);
        return ans;
    }

private:
    bool remainLengthValid(int octet, int remain) {
        return octet == 1 && remain >= 3 && remain <= 9 || 
            octet == 2 && remain >= 2 && remain <= 6 ||
            octet == 3 && remain >= 1 && remain <= 3 ||
            octet == 4 && remain == 0;
    }

    void dfs(int octet, string stack, string s, vector<string>& ans) {
        if (octet > 4) {
            if (s.empty()) {
                ans.push_back(stack.substr(0, stack.size() - 1));
            }
            return;
        }

        for (int l = 1; l <= 3; ++l) {
            if (!remainLengthValid(octet, s.size() - l)) {
                continue;
            }
            string prefix = s.substr(0, l);
            if (prefix[0] == '0' and l > 1) {
                return;
            }
            int value = stoi(prefix);
            if (value == 0) {
                dfs(octet + 1, stack + prefix + ".", s.substr(l), ans);
                return;
            }
            if (value > 0 && value < 256) {
                dfs(octet + 1, stack + prefix + ".", s.substr(l), ans);
            }
        }
    }
};

void print(vector<string> vec) {
    for (string s : vec) {
        cout << s << "  ";
    }
    cout << "\n";
}

int main() {
    Solution* solution = new Solution();
    vector<string> ans;

    print(solution->restoreIpAddresses("25525511135"));
    print(solution->restoreIpAddresses("0000"));
    print(solution->restoreIpAddresses("1111"));
    print(solution->restoreIpAddresses("010010"));
    print(solution->restoreIpAddresses("101023"));

}

