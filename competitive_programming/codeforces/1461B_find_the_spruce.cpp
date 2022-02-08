/*
    How many tress in matrix?

   .*.
   ***

   ..*.. 
   .***.
   *****
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int calculate(int r, int c, vector<string> matrix) {
    int total = 0;
    vector<vector<int>> dp(r, vector<int>(c));
    for (int i = 0; i != r; ++i) {
        for (int j = 0; j != c; ++j) {
            int left, right, up, horizon;
            if (matrix[i][j] == '*') {
                // up
                if (i - 1 >= 0) {
                    up = dp[i - 1][j];
                } else {
                    up = 0;
                }
                // horizontal
                left = j - 1;
                right = j + 1;
                horizon = 0;
                while (left >= 0 && right < c && matrix[i][left] == '*' && matrix[i][right] == '*') {
                    ++horizon;
                    left -= 1;
                    right += 1;
                }
                dp[i][j] = up < horizon ? up + 1 : horizon + 1;
            } else {
                dp[i][j] = 0;
            }
            total += dp[i][j];
        }
    }  
    return total; 
}

int main() {
    int n, r, c;
    cin >> n;
    vector<string> matrix;
    vector<int> result;
    string str;
    for (int count = 0; count != n; ++count) {
        cin >> r >> c;
        for (int i = 0; i != r; ++i) {
            cin >> str;
            matrix.push_back(str);
        }
        int total = calculate(r, c, matrix);
        cout << total << "\n";
        matrix.clear();
    }
}
