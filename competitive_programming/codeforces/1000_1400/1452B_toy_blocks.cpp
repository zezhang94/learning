#include <iostream>
#include <algorithm>
using namespace std;

using ull = unsigned long long;

void solve() {
    int n, a, i = 1, k, maximum = -1;
    ull sum = 0;
    cin >> n;
    while (i++ <= n) {
        cin >> a;
        maximum = max(maximum, a);
        sum += a;
    }

    if (sum % (n - 1)) {
        k = sum / (n - 1) + 1;
    } else {
        k = sum / (n - 1);
    }
    
    // Tip: observe status change after operation 
    if (maximum > k) {
        k = maximum;
    }

    cout << ((ull) k) * (n - 1) - sum << '\n';
}

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        solve();
    }
}