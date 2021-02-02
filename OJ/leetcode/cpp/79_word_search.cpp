#include <iostream>
#include <vector>
#include <utility>
#include <string>
using namespace std;

vector<pair<int, int>> getNeighbors(int i, int j, const vector<vector<char>>& board) {
    int m = board.size();
    int n = board[0].size();
    vector<pair<int, int>> neighbors;
    if (i - 1 >= 0) {
        neighbors.push_back(make_pair(i - 1, j));
    }
    if (i + 1 < m) {
        neighbors.push_back(make_pair(i + 1, j));
    }
    if (j - 1 >= 0) {
        neighbors.push_back(make_pair(i, j - 1));
    }
    if (j + 1 < n) {
        neighbors.push_back(make_pair(i, j + 1));
    }
    return neighbors;
}

bool dfs(int row, int col, int wi, vector<vector<bool>>& valid, 
         const vector<vector<char>>& board, string& word) {
    if (wi == word.size()) {
        return true;
    }
    vector<pair<int, int>> neighbors = getNeighbors(row, col, board);
    for (pair<int, int> neighbor: neighbors) {
        int i = neighbor.first;
        int j = neighbor.second;
        if (valid[i][j] and word[wi] == board[i][j]) {
            valid[i][j] = false;
            bool ans = dfs(i, j, wi + 1, valid, board, word);
            valid[i][j] = true;
            if (ans) {
                return true;
            }
        }
    }
    return false;
}

bool exist(vector<vector<char>>& board, string word) {
    int m = board.size();
    int n = board[0].size();
    vector<vector<bool>> valid(m, vector<bool>(n, true));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (board[i][j] == word[0]) {
                valid[i][j] = false;
                bool ans = dfs(i, j, 1, valid, board, word);
                valid[i][j] = true;
                if (ans) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    vector<vector<char>> board = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word = "ABCCED";
    cout << exist(board, word) << "\n";
}