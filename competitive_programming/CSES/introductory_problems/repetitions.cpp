#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string seq;
    cin >> seq;
    int ans = 0;
    int sum = 1;
    for (int i = 1; i < seq.size(); ++i) {
        if (seq[i] == seq[i - 1]) {
            sum += 1;
        } else {
            ans = max(ans, sum);
            sum = 1;
        }
    }
    cout << max(ans, sum) << LF;
}
