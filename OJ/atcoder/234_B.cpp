#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> points;
    int i = n;
    while (i-- > 0) {
        int x, y;
        cin >> x >> y;
        points.push_back(make_pair(x, y));
    }
    double ans = 0;
    for (i = 0; i < n; ++i) {
        pair<int, int> pa = points[i];
        for (int j = 0; j < n; ++j) {
            pair<int, int> pb = points[j];
            ans = max(
                sqrt(
                    (pa.first - pb.first) * (pa.first - pb.first) + 
                    (pa.second - pb.second) * (pa.second - pb.second)
                ), ans);
        }
    }
    cout.precision(17);
    cout << ans << endl;
}