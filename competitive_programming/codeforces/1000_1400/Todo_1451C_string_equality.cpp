#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

/* wrong answer
void solve() {
    int n, k;
    cin >> n >> k;
    string str1, str2;
    cin >> str1 >> str2;
    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());

    if (str1[n - 1] > str2[n - 1]) {
        cout << "No\n";
        return;
    }

    if (k == 1) {
        cout << "Yes\n";
        return;
    }

    int len = 0;
    char pre1, pre2;
    for (int i = 0; i < n; ++i) {
        if (str1[i] != str2[i]) {
            if (len == 0) {
                pre1 = str1[i];
                pre2 = str2[i];
                len += 1;
            } else if (len < k) {
                if (str1[i] == pre1 && str2[i] == pre2 && str1[i] < str2[i]) {
                    ++len;
                } else {
                    cout << "No\n";
                    return;
                }
            }
            if (len == k) {
                len = 0;
            }
        } else {
            if (len != 0) {
                cout << "No\n";
                return;
            }
        }
    }

    if (len) {
        cout << "No\n";
    } else {
        cout << "Yes\n";
    }
}
*/ 

void solve() {
    
}

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        solve();
    }
}