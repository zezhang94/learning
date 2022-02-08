#include <iostream>
using namespace std;

const int N = 100000;
int n;
int p[N];

int main() {
    cin >> n;
    int i = 0;
    while (i != n) {
        cin >> p[i++];
    }
    int ans = p[0];
    for (i = 1; i < n; ++i) {
        if (p[i] <= ans) {
            cout << ans << endl;
            return 0;  
        } 
        ans = p[i];
    } 
    cout << ans << endl;
}