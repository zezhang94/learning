#include <iostream>
#include <string>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int n, q;
        string s;
        cin >> n >> q >> s;
        while (q--) {
            int i, j;
            bool flag = false;
            cin >> i >> j;
            --i;
            --j;
            for (int k = 0; k < i; ++k) {
                if (s[k] == s[i]) {
                    cout << "YES\n";
                    flag = true;
                    break;
                }
            }
            if (flag) {
                continue;
            }

            for (int k = j + 1; k < n; ++k) {
                if (s[k] == s[j]) {
                    cout << "YES\n";
                    flag = true;
                    break;
                }
            }
            if (flag) {
                continue;
            }

            cout << "NO\n";
        }
    }
    return 0;
    
}