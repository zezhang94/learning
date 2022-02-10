#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    if ((1ll + n) * n >> 1 & 1) {
        cout << "NO\n";
        return 0;
    }
    int s, e;
    int cnt = 0;
    cout << "YES\n";
    if (n & 1) {
        cout << n / 2 + 1 << LF;
        cout << "1 2";
        s = 4, e = n;
        while (s < e && cnt++ < (n - 3) >> 2) {
            cout << ' ' << s++ << ' ' << e--;
        }
        cout << LF << n / 2 << LF;
        cout << "3";
        while (s < e) {
            cout << ' ' << s++ << ' ' << e--;
        }
    } else {
        cout << n / 2 << LF;
        s = 1, e = n;
        while (s < e && cnt++ < n >> 2) {
            cout << s++ << ' ' << e-- << ' ';
        }
        cout << LF << n / 2 << LF;
        while (s < e) {
            cout << s++ << ' ' << e-- << ' ';
        }
        cout << LF;
    }
}