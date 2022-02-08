#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

void dfs(int depth, const vector<int>& A, vector<vector<bool>> table, 
         vector<int>& stack, int used, int *ans) {
    if (depth == A.size()) {
        *ans += 1;
        return;
    }

    for (int i = 0; i < A.size(); ++i) {
        if (i > 0 && A[i] == A[i - 1] && !(used & (1 << (i - 1)))) {
            continue;
        }
        if (!(used & (1 << i)) && (depth == 0 || table[stack[depth - 1]][i])) {
            stack[depth] = i;
            dfs(depth + 1, A, table, stack, used | (1 << i), ans);
        }
    }
}

inline bool isPerfectSquare(int i) {
    int root = (int) sqrt(i);
    return root * root == i;
}

int numSquarefulPerms(vector<int>& A) {
    int n = A.size();
    sort(A.begin(), A.end()); // Attention: order and consistency
    // pre-processing
    vector<vector<bool>> table(n, vector<bool>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            table[i][j] = i < j ? isPerfectSquare(A[i] + A[j]) : table[i][j] = table[j][i];
        }
    }

    int zero = 0;
    int *ans = &zero;
    vector<int> stack(n);
    dfs(0, A, table, stack, 0, ans);
    return *ans;
}

int main() {
    vector<int> A = {1, 1, 8, 1, 8};
    cout << numSquarefulPerms(A) << "\n";
    A = {1, 17, 8};
    cout << numSquarefulPerms(A) << "\n";
    A = {2, 2, 2};
    cout << numSquarefulPerms(A) << "\n";
}
