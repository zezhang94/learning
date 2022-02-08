#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isValid(int x, int y, 
             const vector<bool>& col,
             const vector<bool>& down,
             const vector<bool>& up) {
    return col[y] and up[x + y] and down[col.size() - x - 1 + y];
}

int dfs(int x, vector<bool>& col, vector<bool>& down, vector<bool>& up,
        const int n) {
    if (x == n) {
        return 1;
    }
    int count = 0;
    for (int y = 0; y < col.size(); ++y) {
        if (isValid(x, y, col, down, up)) {
            col[y] = false;
            down[n - x - 1 + y] = false;
            up[x + y] = false;
            count += dfs(x + 1, col, down, up, n);
            up[x + y] = true;
            down[n - x - 1 + y] = true;
            col[y] = true;
        }
    }
    return count;
}

int totalNQueens(int n) {
    vector<bool> col(n, true);
    vector<bool> down(2 * n - 1, true);
    vector<bool> up(2 * n - 1, true);
    return dfs(0, col, down, up, n);
}

int main() {
    for (int n = 1; n < 10; ++n) {
        cout << totalNQueens(n) << "\n";
    }
    return 0;
}