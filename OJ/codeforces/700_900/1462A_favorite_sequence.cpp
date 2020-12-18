#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases > 0) {
        int n;
        cin >> n;
        int i = 0;
        int j = n - 1;
        vector<string> str;
        while (n-- > 0) {
            string s;
            cin >> s;
            str.push_back(s);
        }
        
        while (i <= j) {
            if (i < j) {
                cout << str[i++] << " " << str[j--] << " ";
            } else {
                cout << str[i++] << " ";
                --j;
            }
        }
        
        cout << "\n";
        --cases;
    }
    
}
