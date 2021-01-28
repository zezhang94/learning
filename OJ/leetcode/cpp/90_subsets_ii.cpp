#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(int start, vector<int>& stack, vector<vector<int>>& ans, vector<int>& nums) {
    ans.push_back(stack);
    for (int i = start; i < nums.size(); ++i) {
        if (i == start || nums[i] != nums[i - 1]) {
            stack.push_back(nums[i]);
            dfs(i + 1, stack, ans, nums);
            stack.pop_back();
        }
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> ans;
    vector<int> stack;
    dfs(0, stack, ans, nums);
    return ans;
}

int main() {
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> ans = subsetsWithDup(nums);
    for (vector<int> vec : ans) {
        for (int i : vec) {
            cout << i << " ";
        }
        cout << "\n";
    }
}