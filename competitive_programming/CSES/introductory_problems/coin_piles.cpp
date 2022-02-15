#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    int a, b;
    while (t--) {
        cin >> a >> b;
        int diff = abs(a - b);
        if (a > b) {
            a -= 2 * diff;
        } else if (a < b) {
            a -= diff;
        }
        if (a < 0) {
            cout << "NO\n";
        } else if (a == 0) {
            cout << "YES\n";
        } else if (a == 1 || a == 2) {
            cout << "NO\n";
        } else if (a % 3 == 0) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}
