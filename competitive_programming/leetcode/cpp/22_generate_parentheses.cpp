#include <iostream>
#include <vector>
#include <string>
using namespace std;

void dfs(int l, int r, string s, vector<string>& ans) {
    if (r < l) {
        return;
    }
    if (l == 0 and r == 0) {
        ans.push_back(s);
        return;
    }

    if (l) {
        dfs(l - 1, r, s + "(", ans);
    }
    if (r) {
        dfs(l, r - 1, s + ")", ans);
    }
}

vector<string> generateParenthesis(int n) {
    int l = n;
    int r = n;
    string s = "";
    vector<string> ans;
    dfs(l, r, s, ans);
    return ans;
}

int main() {
    vector<string> ans;
    ans = generateParenthesis(3);
    for (string s : ans) {
        cout << s << " ";
    }
    cout << "\n";
}