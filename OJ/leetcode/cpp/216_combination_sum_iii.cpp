#include <iostream>
#include <vector>
using namespace std;

void dfs(int target, int start, vector<int>& stack, vector<vector<int>>& ans, int k, int n) {
    if (target <= 0) {
        if (stack.size() == k && target == 0) {
            ans.push_back(stack);
        }
        return;
    }
    for (int i = start; i <= n; ++i) {
        stack.push_back(i);
        dfs(target - i, i + 1, stack, ans, k, n);
        stack.pop_back();
    }
}

vector<vector<int>> combinationSum3(int k, int n) {
    vector<vector<int>> ans;
    vector<int> stack;
    dfs(n, 1, stack, ans, k , n <= 9 ? n : 9);
    return ans;
}

void printAns(vector<vector<int>> ans) {
    cout << "================\n";
    for (vector<int> combination : ans) {
        for (int i : combination) {
            cout << i << " ";
        }
        cout << "\n";
    }
}

int main() {
    vector<vector<int>> ans;
    ans = combinationSum3(3, 7);
    printAns(ans);
    ans = combinationSum3(3, 9);
    printAns(ans);
    ans = combinationSum3(4, 1);
    printAns(ans);
    ans = combinationSum3(3, 2);
    printAns(ans);
    ans = combinationSum3(9, 45);
    printAns(ans);
}
