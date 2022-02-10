#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    ll n;
    cin >> n;
    while (n > 1) {
        cout << n << ' ';
        if (n & 1) {
            n = n * 3 + 1;
        } else {
            n = n >> 1;
        }
    }
    cout << 1 << LF;
}
