#include <iostream>
#include <vector>
using namespace std;

void dfs(int depth, int start, vector<int>& stack, int k, int n, vector<vector<int>>& ans) {
    if (depth >= k) {
        if (depth == k) {
            ans.push_back(stack);
        }
        return;
    }
    
    for (int i = start; i <= n; ++i) {
        stack.push_back(i);
        dfs(depth + 1, i + 1, stack, k, n, ans);
        stack.pop_back();
    }
}

vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> ans;
    vector<int> stack;
    dfs(0, 1, stack, k, n, ans);
    return ans;
}

int main() {
    vector<vector<int>> ans = combine(4, 2);
    for (vector<int> vec : ans) {
        for (int i : vec) {
            cout << i << " ";
        }
        cout << "\n";
    }
}