#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
/*
int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int n;
        cin >> n;
        int result;
        vectoc
    }
}
*/

void solve()
{
    int x;
    cin >> x;
    vector<int> ans;
    int sum = 0, last = 9;
    while (sum < x && last > 0) {
        ans.push_back(min(x - sum, last)); // TODO: prove its correctness
        sum += last;
        last--;
    }
    if (sum < x) {
        cout << -1 << "\n";
    } else {
        reverse(ans.begin(), ans.end());
        for (int i : ans) {
            cout << i;
        }
        cout << "\n";
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}