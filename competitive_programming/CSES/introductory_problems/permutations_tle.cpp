#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int c = 0;
int n;
bool flag = false;
vector<int> ans;

void backtrace(vector<bool>& b) {
    if (ans.size() == n) {
        for (int v : ans) {
            cout << v << ' ';
        }
        cout << LF;
        flag = true;
        return;
    }
    for (int i = 1; i <= n; ++i) {
        if (b[i] || ans.size() > 0 && abs(i - *ans.crbegin()) <= 1) {
            continue;
        }
        b[i] = true;
        ans.push_back(i);
        backtrace(b);
        if (flag) {
            break;
        }
        ans.pop_back();
        b[i] = false;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    vector<bool> b(n + 1);
    backtrace(b);
    if (!flag) {
        cout << "NO SOLUTION" << LF;
    }
}
