#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int a, b, c;
        cin >> a >> b >> c;
        int sum = a + b + c;
        if (sum % 9 != 0) {
            cout << "NO\n";
        } else {
            int x = sum / 9;
            int minimum = min(min(a, b), c);
            if (x > minimum) {
                cout << "NO\n";
            } else {
                cout << "YES\n";
            }
        }
    }
    
}