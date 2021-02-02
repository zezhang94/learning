#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool dfs(int row, int col, int wi, vector<vector<char>>& board, int m, int n, string& word) {
    if (wi == word.size()) {
        return true;
    }
    if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] != word[wi]) {
        return false;
    }
    char cur = board[row][col];
    board[row][col] = 0;
    bool ans = dfs(row - 1, col, wi + 1, board, m, n, word) || 
        dfs(row + 1, col, wi + 1, board, m, n, word) ||
        dfs(row, col - 1, wi + 1, board, m, n, word) ||
        dfs(row, col + 1, wi + 1, board, m, n, word);
    board[row][col] = cur;
    if (ans) {
        return true;
    }
    return false;
}

bool findWord(vector<vector<char>>& board, string& word, int m ,int n) {
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (dfs(i, j, 0, board, m, n, word)) {
                return true;
            }
        }
    }
    return false;
}

vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    vector<string> ans;
    int m = board.size();
    int n = board[0].size();
    for (string word: words) {
        if (findWord(board, word, m, n)) {
            ans.push_back(word);
        }
    }
    return ans;
}

void print(vector<string> vec) {
    cout << "--------\n";
    for (string str : vec) {
        cout << str << "\n";
    }
}

int main() {
    vector<string> ans;

    vector<vector<char>> board = {
        {'o','a','a','n'},
        {'e','t','a','e'},
        {'i','h','k','r'},
        {'i','f','l','v'}
    };
    vector<string> words = {"eat", "oath"};
    ans = findWords(board, words);
    print(ans);

    return 0;
}