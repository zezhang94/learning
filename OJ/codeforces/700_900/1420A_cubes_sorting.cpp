#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int pre = 1000000001;
        int n, a;
        bool flag = false;
        cin >> n;
        while (n > 0) {
            cin >> a;
            if (!flag && pre - a <= 0) {
                cout << "YES\n";
                flag = true;
            }
            pre = a;
            --n;
        }
        if (!flag) {
            cout << "NO\n";
        }
    }
    
}