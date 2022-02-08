#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(int used, vector<int>& stack, vector<vector<int>>& ans, const vector<int>& nums) {
    if (stack.size() == nums.size()) {
        ans.push_back(stack);
        return;
    }
    for (int i = 0; i < nums.size(); ++i) {
        if (i > 0 && nums[i] == nums[i - 1] && !(used & 1 << (i - 1))) {
            continue;
        }
        if (!(used & 1 << i)) {
            stack.push_back(nums[i]);
            dfs(used | 1 << i, stack, ans, nums);
            stack.pop_back();
        }
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> ans;
    vector<int> stack;
    sort(nums.begin(), nums.end());
    dfs(0, stack, ans, nums);
    return ans;
}

void print(vector<vector<int>> ans) {
    for (vector<int> arr : ans) {
        for (int i : arr) {
            cout << i << " ";
        }
        cout << "\n";
    }
}

int main() {
    vector<int> nums = {1, 1, 3};
    vector<vector<int>> ans = permuteUnique(nums);
    print(ans);
}