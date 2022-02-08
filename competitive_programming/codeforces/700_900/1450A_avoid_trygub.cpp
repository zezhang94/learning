#include <iostream>
#include <string>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int n;
        cin >> n;
        string str;
        cin >> str;
        int i = 0;
        int j = n - 1;
        while (i < n && j >= 0 && i <= j) {
            while (i < n && str[i] != 't') { // index range
                ++i;
            }
            while (j >= 0 && str[j] == 't') { // index range
                --j;
            }
            if (i < n && j >= 0 && i <= j) {
                str[i] = str[j];
                str[j--] = 't';
            }
        }
        cout << str << "\n";
    }
}