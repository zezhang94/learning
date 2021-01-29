#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isValid(string s) {
    int count = 0;
    for (char c : s) {
        if (c == '(') {
            ++count;
        } else if (c == ')') {
            --count;
        }
        if (count < 0) {
            return false;
        }
    }
    return count == 0;
}

void dfs(int start, int l, int r, string s, vector<string>& ans) {
    if (l == 0 and r == 0) {
        if (isValid(s)) {
            ans.push_back(s);
        }
        return;
    }

    for (int i = start; i < s.size(); ++i) {
        if (i > start and s[i] == s[i - 1]) {
            continue;
        }
        if (s[i] == '(' || s[i] == ')') {
            string copy = s;
            copy.erase(i, 1);
            if (s[i] == '(' && l > 0) {
                dfs(i, l - 1, r, copy, ans);
            } else if (s[i] == ')' && r > 0) {
                dfs(i, l, r - 1, copy, ans);
            }
        }
    }
}

vector<string> removeInvalidParentheses(string s) {
    vector<string> ans;
    // number of parentheses to remove 
    int l = 0;
    int r = 0;
    for (char c : s) {
        l += c == '(';
        if (l == 0) {
            r += c == ')';
        } else {
            l -= c == ')';
        }
    }
    dfs(0, l, r, s, ans);
    return ans;
}

void print(vector<string> ans) {
    for (string s : ans) {
        cout << s << " ";
    }
    cout << "\n";
}

int main() {
    vector<string> ans = removeInvalidParentheses("()())()");
    print(ans);
    ans = removeInvalidParentheses("(a)())()");
    print(ans);
    ans = removeInvalidParentheses(")(");
    print(ans);
}