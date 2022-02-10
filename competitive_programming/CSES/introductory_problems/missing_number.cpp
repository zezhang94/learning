#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

const int N = 200001;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, a;
    cin >> n;
    ll ans = (1ll + n) * n / 2;
    while (n-- > 1) {
        cin >> a;
        ans -= a;
    }
    cout << ans << LF;
}
