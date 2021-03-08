#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m =  matrix.size();
        n =  matrix[0].size();
        int maximum = 0;
        vector<vector<int>> memo(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                maximum = max(maximum, dfs(i, j, memo, matrix)); 
            }
        }
        return maximum;
    }

private:
    int m, n;
    int direction [5] = {0, -1, 0, 1, 0}; 

    int dfs(int ri, int rj, vector<vector<int>>& memo, const vector<vector<int>>& matrix) {
        if (memo[ri][rj] > 0) {
            return memo[ri][rj];
        }
        memo[ri][rj] = 1;
        for (int k = 0; k < 4; ++k) {
            int i = ri + direction[k];
            int j = rj + direction[k + 1];
            if (i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] <= matrix[ri][rj]) {
                continue;
            }
            memo[ri][rj] = max(memo[ri][rj], dfs(i, j, memo, matrix) + 1);
        }
        return memo[ri][rj]; 
    }
};

int main() {
    Solution *solution = new Solution();
    vector<vector<int>> matrix;

    matrix = {
        {9, 9, 4},
        {6, 6, 8},
        {2, 1, 1}
    };
    cout << solution->longestIncreasingPath(matrix) << "\n";

    matrix = {
        {3, 4, 5},
        {3, 2, 6},
        {2, 2, 1}
    };
    cout << solution->longestIncreasingPath(matrix) << "\n";

    matrix = {{1}};
    cout << solution->longestIncreasingPath(matrix) << "\n";
}