#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <climits>
using namespace std;

int min_l;
void dfs(int depth, const vector<string>& A, const vector<vector<int>>& table,
         vector<int>& s, int used, vector<int>& index_ans, int cur_l) {
    if (cur_l >= min_l) {
        return;
    }

    if (depth == A.size()) {
        min_l = cur_l;
        index_ans = s;
        return;
    }

    for (int i = 0; i < A.size(); ++i) {
        if (!(used & (1 << i))) {
            int diff = depth ? A[i].size() - table[s[depth - 1]][i] : A[i].size();
            s[depth] = i;
            dfs(depth + 1, A, table, s, used | (1 << i), index_ans, cur_l + diff);
        }
    }
}

// on the edge of TLE (:-
string dfsSolution(vector<string>& A) {
    vector<vector<int>> table(A.size(), vector<int>(A.size()));
    int n = A.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i != j) {
                int l = min(A[i].size(), A[j].size());
                while (l) {
                    if (A[i].substr(A[i].size() - l) == A[j].substr(0, l)) {
                        table[i][j] = l;
                        break;
                    }
                    l -= 1;
                }
            }
        }
    }

    vector<int> s(n);
    vector<int> index_ans;
    min_l = INT_MAX;
    dfs(0, A, table, s, 0, index_ans, 0);
    string ans = A[index_ans[0]];
    for (int i = 1; i < n; ++i) {
        ans += A[index_ans[i]].substr(table[index_ans[i - 1]][index_ans[i]]);
    }
    return ans;
}

int main() {
    vector<string> A {"catg","ctaagt","gcta","ttca","atgcatc"};
    cout << dfsSolution(A) << '\n';
    cout << "gctaagttcatgcatc\n";
    vector<string> B {"we", "love", "pho"};
    cout << dfsSolution(B) << '\n';
    cout << "welovepho\n";
    return 0;
}