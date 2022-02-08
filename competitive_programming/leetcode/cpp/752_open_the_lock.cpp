#include <iostream>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

class Solution {
private:
    inline int positiveModulo(int i, int m) {
        return (i % m + m) % m; 
    }
    vector<int> getCandidates(int cur) {
        int thousand = cur / 1000 * 1000;
        int hundred = cur / 100 * 100;
        int ten = cur / 10 * 10;
        return {
            positiveModulo(cur + 1000, 10000), 
            positiveModulo(cur - 1000, 10000),
            positiveModulo(cur - thousand + 100, 1000) + thousand,
            positiveModulo(cur - thousand - 100, 1000) + thousand,
            positiveModulo(cur - hundred + 10, 100) + hundred,
            positiveModulo(cur - hundred - 10, 100) + hundred,
            positiveModulo(cur - ten + 1, 10) + ten,
            positiveModulo(cur - ten - 1, 10) + ten
        };
    }
public:
    int openLock(vector<string>& deadends, string target) {
        vector<bool> valid(10000, true);
        for (string deadend : deadends) {
            valid[stoi(deadend)] = false;
        }
        if (!valid[0]) {
            return -1;
        }
        int ti = stoi(target);
        if (ti == 0) {
            return 0;
        }
        queue<pair<int, int>> q;
        q.push(make_pair(0, 0));
        valid[0] = false;
        pair<int, int> p;
        while (!q.empty()) {
            p = q.front();
            q.pop();
            int wheel = p.first;
            int depth = p.second;
            if (wheel == ti) {
                return depth;
            }
            vector<int> candidtes = getCandidates(wheel);
            for (int candidate : candidtes) {
                if (valid[candidate]) {
                    valid[candidate] = false;
                    q.push(make_pair(candidate, depth + 1));
                }
            }
        }
        return -1;
    }
};

int main() {
    Solution* solution = new Solution();
    vector<string> deadends;

    deadends = {"0201", "0101", "0102", "1212", "2002"};
    cout << solution->openLock(deadends, "0202") << "\n";

    deadends = {"8888"};
    cout << solution->openLock(deadends, "0009") << "\n";

    deadends = {"8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"};
    cout << solution->openLock(deadends, "8888") << "\n";

    deadends = {"0000"};
    cout << solution->openLock(deadends, "8888") << "\n";

    return 0;
}