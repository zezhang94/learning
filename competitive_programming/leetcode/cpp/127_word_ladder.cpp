#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
#include <utility>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        queue<pair<string, int>> q;
        q.push(make_pair(beginWord, 0));
        wordSet.erase(beginWord);
        while (!q.empty()) {
            pair<string, int> p = q.front();
            q.pop();
            string s = p.first;
            int depth = p.second;
            if (s == endWord) {
                return depth + 1;
            }
            for (int i = 0; i < s.size(); ++i) {
                for (int j = 'a'; j <= 'z'; ++j) {
                    char cur = s[i];
                    s[i] = j;
                    if (wordSet.find(s) != wordSet.end()) {
                        q.push(make_pair(s, depth + 1));
                        wordSet.erase(s);
                    }
                    s[i] = cur;
                }
            }
        }
        return 0;
    }
};

int main() {
    Solution* solution = new Solution();
    vector<string> wordList;

    wordList = {"hot", "dot", "dog", "lot", "log", "cog"};
    cout << solution->ladderLength("hit", "cog", wordList) << "\n";

    wordList = {"hot", "dot", "dog", "lot", "log"};
    cout << solution->ladderLength("hit", "cog", wordList) << "\n";
    return 0;
}