#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int cases, x, y;
    cin >> cases;
    while (cases--) {
        cin >> x >> y;
        int count = min(x, y) * 2;
        int diff = abs(x - y);
        diff = diff > 0 ? diff * 2 - 1 : 0;
        cout << count + diff << "\n";
    }
}