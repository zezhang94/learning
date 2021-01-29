#include <iostream>
#include <vector>
#include <utility>
using namespace std;

bool dfs(int index, vector<vector<char>>& board, const vector<pair<int, int>>& target,
         vector<vector<bool>>& row, vector<vector<bool>>& col, vector<vector<bool>>& box) {
    if (index == target.size()) {
        return true;
    }

    for (int v = 1; v < 10; ++v) {
        int i = target[index].first;
        int j = target[index].second;
        if (row[i][v] && col[j][v] && box[i / 3 * 3 + j / 3][v]) {
            board[i][j] = v + '0';
            row[i][v] = false;
            col[j][v] = false;
            box[i / 3 * 3 + j / 3][v] = false;
            if (dfs(index + 1, board, target, row, col, box)) {
                return true;
            }
            box[i / 3 * 3 + j / 3][v] = true;
            col[j][v] = true;
            row[i][v] = true;
            board[i][j] = '.';
        }
    }

    return false;
}

void solveSudoku(vector<vector<char>>& board) {
    vector<vector<bool>> row(9, vector<bool>(10, true));
    vector<vector<bool>> col(9, vector<bool>(10, true));
    vector<vector<bool>> box(9, vector<bool>(10, true));
    vector<pair<int, int>> target;

    for (int i = 0; i < board.size(); ++i) {
        for (int j = 0; j < board.size(); ++j) {
            if (board[i][j] != '.') {
                int k = board[i][j] - '0';
                row[i][k] = false;
                col[j][k] = false;
                box[i / 3 * 3 + j / 3][k] = false;
            } else {
                target.push_back(make_pair(i, j));
            }
        }
    }

    dfs(0, board, target, row, col, box);
}

int main() {
    vector<vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    solveSudoku(board);

    for (vector<char> line : board) {
        for (char c : line) {
            cout << c << " ";
        }
        cout << "\n";
    }

}