#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k) {
            return false;
        }
        int target = sum / k;
        sort(nums.begin(), nums.end());
        if (nums[nums.size() - 1] > target) {
            return false;
        }
        for (int i = nums.size() - 1; i >= 0 && nums[i] == target; --i) { 
            nums.pop_back();
            k--;
        }
        vector<int> groups(k, 0);
        bool ans = search(groups, nums, target);
        return ans;
    }

private:
    bool search(vector<int>& groups, vector<int>& nums, const int target) {
        if (nums.size() == 0) {
            return true;
        }
        for (int i = 0; i < groups.size(); ++i) {
            int last = nums[nums.size() - 1];
            nums.pop_back();
            if (last + groups[i] <= target) {
                groups[i] += last;
                if (search(groups, nums, target)) {
                    return true;
                }
                groups[i] -= last;
            }
            nums.push_back(last);
            if (groups[i] == 0) {
                break;
            }
        }
        return false;
    }
};


int main() {
    Solution* solution = new Solution();
    vector<int> nums;
    int k;

    nums = {4, 3, 2, 3, 5, 2, 1};
    k = 4;
    cout << solution->canPartitionKSubsets(nums, k) << "\n";
}