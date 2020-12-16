/*
    Description & definition:
        S = [s1, s2, ..., sn], int sequence
        J = [j1, j2, ..., jm], indices array of S's subsequence
    Condition:   
        ji+1 % ji = 0
        sji < sji+1
    Target:
        Longest J
    Comment:
        You can solve dp by starting from subproblem.
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases > 0) {
        int n;
        cin >> n;
        vector<int> s(n + 1, 0);
        vector<int> dp(n + 1, 1);
        dp[1] = 1;
        for (int i = 1; i != n + 1; ++i) {
            cin >> s[i];
        }

        int maximum = dp[1];
        for (int i = 1; i != n + 1; ++i) {
            int j = i * 2;
            while (j <= n) {
                if (s[j] > s[i]) {
                    dp[j] = dp[i] + 1 > dp[j] ? dp[i] + 1 : dp[j];
                }
                maximum = dp[j] > maximum ? dp[j] : maximum;
                j += i;
            }
        }
        cout << maximum << "\n";

        --cases;
    }
    
}