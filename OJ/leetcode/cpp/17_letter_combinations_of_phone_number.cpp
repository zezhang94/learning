#include <iostream>
#include <string>
#include <vector>
using namespace std;

void dfs(int depth, int start, string s, const string digits, vector<string>& ans, 
         const string t[]) {
  if (depth == digits.size()) {
    ans.push_back(s);
    return;
  }

  for (int i = start; i < digits.size(); ++i) {
    int j = digits[i] - '0';
    for (char c : t[j]) {
      dfs(depth + 1, i + 1, s + c, digits, ans, t);
    }
  } 
}
 
vector<string> letterCombinations(string digits) {
  string t[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
  vector<string> ans;
  if (!digits.size()) {
      return ans;
  }
  dfs(0, 0, "", digits, ans, t);
  return ans;
}

int main() {
    vector<string> ans;
    ans = letterCombinations("2");
    for (string s : ans) {
        cout << s << " ";
    }
    cout << "\n";
}

