#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll n;
    cin >> n;
    ll ans = 0;
    while (n) {
        n /= 5;
        ans = (ans + n % 1000000007) % 1000000007 ;
    }
    cout << ans << LF;
}
