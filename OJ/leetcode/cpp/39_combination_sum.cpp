#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

void dfs(int start, vector<int>& stack, vector<int>& candidates, int target, vector<vector<int>>& ans) {
    if (target <= 0) {
        if (target == 0) {
            ans.push_back(stack);
        }
        return;
    }
    for (int i = start; i < candidates.size(); ++i) {
        stack.push_back(candidates[i]);
        dfs(i, stack, candidates,  target - candidates[i], ans);
        stack.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> ans;
    vector<int> stack;
    dfs(0, stack, candidates, target, ans);
    return ans;
}

int main() {
    vector<int> candidates = {2, 3, 6, 7};
    vector<vector<int>> ans;
    ans = combinationSum(candidates, 7);
    for (vector<int> vec : ans) {
        for (int v : vec) {
            cout << v << " ";
        }
        cout << "\n";
    }
}