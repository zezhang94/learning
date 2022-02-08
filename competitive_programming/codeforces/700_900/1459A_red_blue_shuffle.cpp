#include <iostream>
#include <string>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    int n, rc, bc;
    char rl, bl;
    // Why use string? Because there are zeros.
    string r, b; 
    while (cases-- > 0) {
        cin >> n >> r >> b;
        rc = bc = 0;
        while (n-- > 0) {
            rl = r[n];
            bl = b[n];
            if (rl > bl) {
                ++rc;
            } else if (rl < bl) {
                ++bc;
            }
        }
        
        if (rc == bc) {
            cout << "EQUAL\n";
        } else if (rc > bc) {
            cout << "RED\n";
        } else {
            cout << "BLUE\n";
        }
    }
        
    return 0;
}