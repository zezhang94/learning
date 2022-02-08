#include <iostream>
#include <string>
using namespace std;
int main() {
    int cases, n;
    string str;
    bool flag;
    cin >> cases;
    while (cases > 0) {
        cin >> n;
        cin >> str;
        flag = false;
        if (n >= 4 && (
            str[n - 4] == '2' && str[n - 3] == '0' && str[n - 2] == '2' && str[n - 1] == '0' ||
            str[0] == '2' && str[n - 3] == '0' && str[n - 2] == '2' && str[n - 1] == '0' ||
            str[0] == '2' && str[1] == '0' && str[n - 2] == '2' && str[n - 1] == '0' ||
            str[0] == '2' && str[1] == '0' && str[2] == '2' && str[n - 1] == '0' ||
            str[0] == '2' && str[1] == '0' && str[2] == '2' && str[3] == '0'
        )) {
            cout << "yes\n";
        } else {
            cout << "no\n";
        }
        --cases;
    }

    return 0;
}