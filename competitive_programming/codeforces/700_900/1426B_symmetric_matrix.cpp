#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int n, m;
        cin >> n >> m;
        int tl, tr, bl, br;
        if (m % 2) {
            cout << "NO\n";
            while (n--) {
                cin >> tl >> tr >> bl >> br;
            }
        } else {
            bool flag = false;
            while (n--) {
                cin >> tl >> tr >> bl >> br;
                if (!flag && tr == bl) {
                    cout << "YES\n";
                    flag = true;
                } 
            }
            if (!flag) {
                cout << "NO\n";
            }
        }
        
    }
    
}