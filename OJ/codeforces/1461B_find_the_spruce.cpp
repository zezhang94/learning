#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n, r, c;
    cin >> n >> r >> c;
    vector<string> matrix;
    vector<vector<int>> dp(r, vector<int>(c));
    string str;
    for (int count = 0; count != n; ++count) {
        for (int i = 0; i != r; ++i) {
            cin >> str;
            matrix.push_back(str);
        }
        int total = 0;
        for (int i = 0; i != r; ++i) {
            for (int j = 0; j != c; ++j) {
                if (matrix[i][j] == '*') {
                    int k = 1;
                    while (i - k >= 0 && j - k >= 0 && j + k <= c) {
                        
                    }
                    
                }
            }
        }   
    }


}
