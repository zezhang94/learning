/*
Description:
    Bishwock:
    X0 0X XX XX
    XX XX 0X X0
Target:
    maximum number of Bishwock can put into input sequence
Examples:
    00
    00
    1

    00X00X0XXX0
    0XXX0X00X00
    4

    0X0X0
    0X0X0
    0

    0XXX0
    00000
    2
    
    000X0
    00000
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    int n =  s1.size();
    vector<int> dp(n ,0);
    // how many consequent 2-line 0 from index i (0 <= i < n) 
    vector<int> zeros(n, -1);
    for (int i = 1; i != n; ++i) {
        if (s1[i - 1] == 'X' && s2[i - 1] == '0') {
            if (s1[i] == '0' && s2[i] == '0') {
                dp[i] = dp[i - 1] + 1;
                s2[i - 1] = s1[i] = s2[i] = 'X';
            } else {
                dp[i] = dp[i - 1];
            }
        } else if (s1[i - 1] == '0' && s2[i - 1] == 'X') {
            if (s1[i] == '0' && s2[i] == '0') {
                dp[i] = dp[i - 1] + 1;
                s1[i - 1] = s1[i] = s2[i] = 'X';
            } else {
                dp[i] = dp[i - 1];
            }
        } else if (s1[i - 1] == 'X' && s2[i - 1] == 'X') {
            dp[i] = dp[i - 1];
        } else {
            
        }
    }
}