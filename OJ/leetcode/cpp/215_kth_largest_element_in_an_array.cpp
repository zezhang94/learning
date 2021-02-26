#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <ctime>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return search(0, nums.size() - 1, nums, k - 1);
    }

private:
    int search(int l, int r, vector<int>& nums, const int k) {
        int pivot = divide(l, r, nums);
        if (pivot == k) {
            return nums[pivot];
        } else if (pivot < k) {
            return search(pivot + 1, r, nums, k);
        } else {
            return search(l, pivot - 1, nums, k);
        }
    }

    void inline swap(vector<int>& nums, int i, int j) {
        if (i != j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }

    int divide(int l, int r, vector<int>& nums) {
        srand((unsigned) time(0));
        swap(nums, r, l + rand() % (r - l + 1));
        int cur = l;
        for (int i = l; i < r; ++i) {
            if (nums[i] > nums[r]) {
                swap(nums, i, cur++);
            }
        }
        swap(nums, cur, r);
        return cur;
    }
};

int main() {
    Solution *solution = new Solution();
    vector<int> nums;
    int k;

    nums = {3, 2, 1, 5, 6, 4};
    k = 2;
    cout << solution->findKthLargest(nums, k) << "\n";

    nums = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    k = 4;
    cout << solution->findKthLargest(nums, k) << "\n";


    nums = {1};
    k = 1;
    cout << solution->findKthLargest(nums, k) << "\n";

    nums = {3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1,
            1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6};
    k = 20;
    cout << solution->findKthLargest(nums, k) << "\n";

    nums = {7, 6, 5, 4, 3, 2, 1};
    k = 5;
    cout << solution->findKthLargest(nums, k) << "\n";
    return 0;
} 