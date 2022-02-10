#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int cases, y, x;
    cin >> cases;
    while (cases--) {
        cin >> y >> x;
        int maximum = max(x, y);
        if (maximum == x) {
            if (x & 1) {
                cout << (1 + (2ll * (x - 1) + 1)) * x / 2 - y + 1 << LF;
            } else {
                cout << (1 + (2ll * (x - 2) + 1)) * (x - 1) / 2 + y << LF;
            }
        } else {
            if (y & 1) {
                cout << (1 + (2ll * (y - 2) + 1)) * (y - 1) / 2 + x << LF;
            } else {
                cout << (1 + (2ll * (y - 1) + 1)) * y / 2 - x + 1 << LF;
            }
        }
    }
}