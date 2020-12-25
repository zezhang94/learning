/*
    Time: 18:15
*/

#include <iostream>
using namespace std;
using ull = unsigned long long;

void solve() {
    int row, col;
    cin >> row >> col;
    int n = row * col;
    int negtive = 0, sum = 0;
    int min_abs = 101;
    while (n--) {
        int a;
        cin >> a;
        if (a < 0) {
            a = -a;
            ++negtive;
        }
        sum += a;
        min_abs = min_abs < a ? min_abs : a;
    }
    if (negtive % 2) {
        sum -= 2 * min_abs;
    }

    cout << sum << '\n';
}

int main() {
    int cases;
    cin >> cases;
    while(cases--) {
        solve();
    }
}