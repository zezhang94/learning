#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(int start, vector<int>& stack, vector<vector<int>>& ans, 
         const vector<int>& candidates, int target) {
    if (target <= 0) {
        if (target == 0) {
            ans.push_back(stack);
        }
        return;
    }

    for (int i = start; i < candidates.size(); ++i) {
        if (i != start && candidates[i] == candidates[i - 1]) {
            continue;
        }
        stack.push_back(candidates[i]);
        dfs(i + 1, stack, ans, candidates, target - candidates[i]);
        stack.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> ans;
    vector<int> stack;
    dfs(0, stack, ans, candidates, target);
    return ans;
}

int main() {
    vector<int> candidates = {2, 5, 2, 1, 2};
    vector<vector<int>> ans = combinationSum2(candidates, 5);
    for (vector<int> vec : ans) {
        for (int i : vec) {
            cout << i << " ";
        }
        cout << "\n";
    }
}