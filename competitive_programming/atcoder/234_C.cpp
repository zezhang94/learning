#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    long k;
    cin >> k;
    string ans = "";
    while (k > 0) {
        if (k % 2 == 0) ans.push_back('0');
        else ans.push_back('2');
        k /= 2;
    }
    reverse(ans.begin(), ans.end());
    cout << ans << endl;
}