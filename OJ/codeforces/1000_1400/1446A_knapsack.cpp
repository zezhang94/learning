/*
    Time: 59:08 + 10:00
    Tip: data type range
    Tip: continue reading input after getting result
    Tip: pay attention to status change when inputting and solving are at the same time
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ull = unsigned long long;

void solve() {
    int n;
    ull W;
    cin >> n >> W;
    ull half = W % 2 ? W / 2 + 1 : W / 2;
    vector<int> ans;
    int i = 1;
    ull sum = 0, w;
    bool flag = false;
    while (i <= n) {
        cin >> w;
        if (!flag && w >= half && w <= W) {
            cout << "1\n" << i << "\n";
            flag = true;
        } else if (w > W) {
            // skip
        } else if (sum < half) {
            sum += w;
            ans.push_back(i);
        } 
        ++i;
    }

    if (flag) {
        return;
    }

    if (sum >= half && sum <= W) {
        cout << ans.size() << '\n';
        for (int j : ans) {
            cout << j << ' ';
        }
        cout << '\n';
    } else {
        cout << "-1\n";
    }

}

int main() {
    int cases;
    cin >> cases;
    while(cases--) {
        solve();
    }
}