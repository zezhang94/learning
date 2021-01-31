#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isValid(int x, int y, 
             const vector<bool>& col,
             const vector<bool>& down,
             const vector<bool>& up) {
    return col[y] && up[x + y] && down[col.size() - 1 - x + y];
}

void dfs(int x, 
         vector<bool>& col, vector<bool>& down, vector<bool>& up,
         vector<string>& board, vector<vector<string>>& ans) {
    if (x == board.size()) {
        ans.push_back(board);
        return;
    }

    for (int y = 0; y < board.size(); ++y) {
        if (isValid(x, y, col, down, up)) {
            board[x][y] = 'Q';
            col[y] = false;
            down[board.size() - 1 - x + y] = false;
            up[x + y] = false;
            dfs(x + 1, col, down, up, board, ans);
            up[x + y] = true;
            down[board.size() - 1 - x + y] = true;
            col[y] = true;
            board[x][y] = '.';
        }
    }
}

vector<vector<string>> solveNQueens(int n) {
    vector<string> board(n, string(n, '.'));
    vector<bool> col(n, true);
    // from top-left to down-right
    vector<bool> down(2 * n - 1, true);
    // from down-left to top-right
    vector<bool> up(2 * n - 1, true);

    vector<vector<string>> ans;
    dfs(0, col, down, up, board, ans);
    return ans;
}

void print(const vector<vector<string>>& ans) {
    for (vector<string> line : ans) {
        for (string s : line) {
            cout << s << "\n";
        }
    }
    cout << ans.size();
}

int main() {
    vector<vector<string>> ans;
    ans = solveNQueens(8);
    print(ans);
    return 0;
}

