/*
    Time: 01:16
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

using ull = unsigned long long;

void solve() {
    ull n;
    vector<ull> seq;
    vector<ull> max_seq;
    cin >> n;
    ull source = n;
    if (n % 2 == 0) {
        while (n / 2 % 2 == 0) {
            max_seq.push_back(2);
            n /= 2;
        }
        if (n > 1) {
            max_seq.push_back(n);
        }
    }

    for (ull i = 3; i <= sqrt(n); i += 2) {
        n = source;
        seq.clear();
        if (n % i == 0) {
            while (n / i % i == 0) {
                seq.push_back(i);
                n /= i;
            }
            if (n > 1 && n % i == 0) {
                seq.push_back(n);
            }
        }  
        if (max_seq.size() < seq.size()) {
            max_seq = seq;
        } 
    }

    if (max_seq.size()) {
        cout << max_seq.size() << '\n';
        for (ull i : max_seq) {
            cout << i << ' ';
        }
    } else {
        cout << "1\n" << source << '\n';
    }

}

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        solve();
    }
}