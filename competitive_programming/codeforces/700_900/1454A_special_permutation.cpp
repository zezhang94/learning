#include <iostream>
#include <vector>
using namespace std;

int main() {
    int cases, n, mid;
    bool odd;
    cin >> cases;
    while (cases--) {
        cin >> n;
        odd = n % 2;
        mid = n / 2 + 1;
        for (int i = 0; i < n; ++i) {
            if (odd && n - i == mid) {
                cout << mid + 1 << ' ';
            } else if (odd && n - i - 1 == mid) {
                cout << mid << ' ';
            } else {
                cout << n - i << ' ';
            }
        }
        cout << "\n";
    }
    
}