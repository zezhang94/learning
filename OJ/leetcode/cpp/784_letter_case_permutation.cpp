#include <iostream>
#include <string>
#include <vector>
#include <cctype>
using namespace std;
void dfs(int depth, int start, string& S, vector<string>& ans) {
  if (depth == S.size()) {
    ans.push_back(S);
    return;
  }
  dfs(depth + 1, start + 1, S, ans);
  if (isalpha(S[start])) {
    S[start] ^= 32;
    dfs(depth + 1, start + 1, S, ans);
    S[start] ^= 32;
  }
}

vector<string> letterCasePermutation(string S) {
  vector<string> ans;
  dfs(0, 0, S, ans);
  return ans;
}

void print(const vector<string>& vec) {
    for (string s : vec) {
        cout << s << " ";
    }
    cout << "\n";
}

int main() {
    vector<string> ans;
    ans = letterCasePermutation("a1b2CC");
    print(ans);
}


