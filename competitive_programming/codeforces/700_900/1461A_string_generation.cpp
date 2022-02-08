#include <iostream>
#include <string>
using namespace std;
int main() {
    int cases;
    cin >> cases;
    while (cases-- > 0) {
        int n, k;
        cin >> n >> k;
        int _n = n;
        string result;
        while (n > 0) {
            result.append("abc");
            n -= 3;
        }
        cout << result.substr(0, _n) << "\n";
    }
    

}