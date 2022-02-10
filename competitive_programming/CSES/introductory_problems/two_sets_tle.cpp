#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

vector<bool> vec;
ll sum;
int cnt = 0;

void dfs(size_t start) {
    if (sum == 0) {
        return;
    }
    for (size_t i = start; i < vec.size(); ++i) {
        if (sum - i < 0) {
            break;
        }
        sum -= i;
        vec[i] = true;
        ++cnt;
        dfs(i + 1);
        if (sum == 0) {
            return;
        }
        --cnt;
        vec[i] = false;
        sum += i;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    ll total = (1ll + n) * n / 2;
    if (total & 1) {
        cout << "NO\n";
        return 0;
    }
    sum = total >> 1;
    vec.resize(n + 1, false);
    dfs(1);
    cout << "YES\n";
    cout << cnt << LF;
    for (size_t i = 1; i < vec.size(); ++i) {
        if (vec[i]) {
            cout << i << ' ';
        }
    }
    cout << LF << n - cnt << LF;
    for (size_t i = 1; i < vec.size(); ++i) {
        if (!vec[i]) {
            cout << i << ' ';
        }
    }
    cout << LF;
}
