#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    if (n == 2 || n == 3) {
        cout << "NO SOLUTION" << LF;
        return 0;
    }
    if (n == 4) {
        cout << "3 1 4 2" << LF;
        return 0;
    }
    int i = 1;
    while (i <= n) {
        if (i == 1) {
            cout << i;
        } else {
            cout << ' ' << i;
        }
        i += 2;
    }
    i = 2;
    while (i <= n) {
        cout << ' ' << i;
        i += 2;
    }
    cout << LF;
}
