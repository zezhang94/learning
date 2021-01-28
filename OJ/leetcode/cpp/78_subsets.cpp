#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(int start, vector<int>& stack, vector<vector<int>>& ans, vector<int>& nums) {
    ans.push_back(stack);
    for (int i = start; i < nums.size(); ++i) {
        stack.push_back(nums[i]);
        dfs(i + 1, stack, ans, nums);
        stack.pop_back();
    }
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> ans;
    vector<int> stack;
    dfs(0, stack, ans, nums);
    return ans;
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> ans = subsets(nums);
    for (vector<int> vec : ans) {
        for (int i : vec) {
            cout << i << " ";
        }
        cout << "\n";
    }
}