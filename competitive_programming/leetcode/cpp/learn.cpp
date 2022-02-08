#include <iostream>
#include <vector>
#include <string>
using namespace std;

class SimpleSolution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> ans;
        dfs(num, target, 0, "", 0, 0, &ans);
        return ans;
    }
private:
    void dfs(const string& num, const int target,               // input
             int pos, const string& exp, long prev, long curr,  // state
             vector<string>* ans) {                             // output
        if (pos == num.length()) { // have dealt all characters
            if (curr == target) {
                ans->push_back(exp);
            }
            return;
        }
        for (int l = 1; l <= num.size() - pos; ++l) {
            string t = num.substr(pos, l);
            if (t[0] == '0' && t.length() > 1) break;  // string starts with 0
            long n = stol(t);
            if (n > INT_MAX) break;
            if (pos == 0) {
                dfs(num, target, l, t, n, n, ans);
                continue;
            }
            dfs(num, target, pos + l, exp + '+' + t, n, curr + n, ans);
            dfs(num, target, pos + l, exp + '-' + t, -n, curr - n, ans);
            dfs(num, target, pos + l, exp + '*' + t, prev * n, curr - prev + prev * n, ans); // the associativity of multiply 
        }
    }
};


class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> ans;
        string exp(num.length() * 2, '\0');    
        dfs(num, target, 0, exp, 0, 0, 0, &ans);
        return ans;
    }
private:
    void dfs(const string& num, const int target,
             int pos, string& exp, int len, long prev, long curr,
             vector<string>* ans) {    
        if (pos == num.length()) {      
            if (curr == target) ans->push_back(exp.substr(0, len));
            return;
        }
        long n = 0;
        int s = pos;
        int l = len;
        if (s != 0) {
            ++len;
        }    
        while (pos < num.size()) {      
            n = n * 10 + (num[pos] - '0');
            if (num[s] == '0' && pos - s > 0) break; // 0X... invalid number
            if (n > INT_MAX) break; // too long
            exp[len++] = num[pos++];
            if (s == 0) {
                dfs(num, target, pos, exp, len, n, n, ans);
                continue;
            }
            exp[l] = '+'; dfs(num, target, pos, exp, len, n, curr + n, ans);
            exp[l] = '-'; dfs(num, target, pos, exp, len, -n, curr - n, ans);
            exp[l] = '*'; dfs(num, target, pos, exp, len, prev * n, curr - prev + prev * n, ans);
        }   
    }
};