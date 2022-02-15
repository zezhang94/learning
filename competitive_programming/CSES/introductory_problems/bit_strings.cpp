#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    ll ans = 2;
    for (int i = 2; i <= n; i++) {
        ans = ans * 2 % 1000000007;
    }
    cout << ans << LF;
}
