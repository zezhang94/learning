/*
    Time: 29:20
*/

#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int n, v, pre, first;
    cin >> n;
    vector<int> a(n + 1, 0);
    for (int i = 1; i <= n; ++i) {        
        cin >> v;
        if (i == 1) {
            first = v;
        } else if (i > 1 && v != pre) {
            ++a[v];
        }
        pre = v;
    }
    
    int mimimum = 300000;
    for (int i = 1; i <= n; ++i) {
        int cur = a[i];
        if (i == first || cur != 0) { // edge condition
            if (i != v) {
                cur += 1;
            }   
            mimimum = cur < mimimum ? cur : mimimum;
        }

    }
    
    cout << (mimimum != 300000 ? mimimum : 0) << '\n';
}

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        solve();
    }
}