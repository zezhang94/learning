#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <iostream>
using namespace std;

// last test case TLE
void dfs(int depth, const vector<string>& A, const vector<vector<int>>& table,
         stack<int>& s, vector<bool>& used, stack<int>& index_ans, int cur_l, int *min_l) {
    if (cur_l > *min_l) {
        return;
    }

    if (depth == A.size()) {
        if (cur_l <= *min_l) {
            *min_l = cur_l;
            index_ans = s;
        }
        return;
    }

    for (int i = 0; i < A.size(); ++i) {
        if (!used[i]) {
            int diff;
            if (depth == 0) {
                diff = A[i].size();
            } else {
                diff = A[i].size() - table[s.top()][i];
            }
            cur_l += diff;
            used[i] = true;
            s.push(i);
            dfs(depth + 1, A, table, s, used, index_ans, cur_l, min_l);
            s.pop();
            used[i] = false;
            cur_l -= diff;
        }
    }
}

string shortestSuperstring(vector<string>& A) {
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

    vector<bool> used(n, false);
    stack<int> index_ans;
    stack<int> s;
    int zero = 0;
    int *min_l = &zero;
    for (int i = 0; i < n; ++i) {
        *min_l += A[i].size();
    }
    dfs(0, A, table, s, used, index_ans, 0, min_l);
    
    int pre = index_ans.top();
    string ans = A[pre];
    index_ans.pop();
    int cur;
    while (!index_ans.empty()) {
        cur = index_ans.top();
        ans = A[cur].substr(0, A[cur].size() - table[cur][pre]) + ans;
        pre = cur;
        index_ans.pop();
    }
    return ans;
}



int main() {
    vector<string> A {"catg","ctaagt","gcta","ttca","atgcatc"};
    cout << shortestSuperstring(A) << '\n';
    cout << "gctaagttcatgcatc\n"; 
    return 0;
}