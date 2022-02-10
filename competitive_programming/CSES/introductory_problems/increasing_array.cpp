#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    int pre, cur;
    cin >> pre;
    n--;
    ll ans = 0;
    while (n--) {
        cin >> cur;
        if (cur < pre) {
            ans += pre - cur;
        } else {
            pre = cur;
        }
    }
    cout << ans << LF;
}
