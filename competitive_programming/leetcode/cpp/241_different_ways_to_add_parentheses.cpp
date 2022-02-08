#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        ops = {'+', '-', '*'};
        return binary(expression);
    }

private:
    map<string, vector<int>> record;
    unordered_set<char> ops;

    vector<int> binary(string exp) {
        if (record.count(exp) > 0) {
            return record[exp];
        }
        vector<int> left, right, tmp;
        for (int i = 0; i < exp.size(); ++i) {
            if (ops.count(exp[i]) > 0) {
                left = binary(exp.substr(0, i));
                right = binary(exp.substr(i + 1));
                for (int l : left) {
                    for (int r : right) {
                        tmp.push_back(calc(exp[i], l, r));
                    }
                }
            }
        }
        if (tmp.empty()) {
            vector<int> single = {stoi(exp)};
            record[exp] = single;
            return single;
        }
        record[exp] = tmp;
        return tmp;
    }

    int calc(char op, int v1, int v2) {
        switch (op) {
            case '+':
                return v1 + v2;
            case '-':
                return v1 - v2;
            default:
                return v1 * v2;
        }
    }
};

void print(vector<int> vec) {
    for (int value : vec) {
        cout << value << " ";
    }
    cout << "\n";
}

int main() {
    Solution* solution = new Solution();
    vector<int> ans;

    ans = solution->diffWaysToCompute("2-1-1");
    print(ans);

    ans = solution->diffWaysToCompute("2*3-4*5");
    print(ans);
}