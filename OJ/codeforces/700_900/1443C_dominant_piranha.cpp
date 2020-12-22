#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int n;
        cin >> n;
        vector<int> a(n, 0);
        int count = 0;
        unsigned long long sum = 0;
        int maximum = 0;
        while (count < n) {
            cin >> a[count];
            maximum = max(maximum, a[count]);
            sum += a[count++];
        }
        if (sum == n * (unsigned long long) maximum) {
            cout << -1 << "\n";
            continue;
        }
        for (int i = 0; i + 1 < n; ++i) {
            if (a[i] == maximum && a[i] != a[i + 1]) {
                cout << i + 1 << "\n";
                break;
            } else if (a[i + 1] == maximum && a[i] != a[i + 1]) {
                cout << i + 2 << "\n";
                break;
            }
            
        }
    }
    
}