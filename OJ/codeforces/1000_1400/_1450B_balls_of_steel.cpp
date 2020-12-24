#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
using namespace std;
using ull = unsigned long long;

void solve() {
    int n, k;
    cin >> n >> k;
    int i = 0;
    vector<pair<int, int>> nodes;
    while (i++ < n) {
        int x, y;
        cin >> x >> y;
        nodes.push_back(make_pair(x, y));
    }

    for (i = 0; i < n; ++i) {
        pair<int, int> n1 = nodes[i];
        int count = 0;
        for (int j = 0; j < n; ++j) {
            pair<int, int> n2 = nodes[j];
            if (abs(n1.first - n2.first) + abs(n1.second - n2.second) <= k) {
                count++;
            }
        }
        if (count == n) {
            cout << "1\n";
            return;
        }
    }
    cout << "-1\n";    
}

int main() {
    int cases;
    cin >> cases;
    while(cases--) {
        solve();
    }
}