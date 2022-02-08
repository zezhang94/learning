#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    int cases;
    cin >> cases;
    while (cases-- > 0) {
        string str;
        cin >> str;
        vector<char> stack1(str.size(), 0);
        vector<char> stack2(str.size(), 0);
        int top1 = 0;
        int top2 = 0;
        int count = 0;
        for (int i = 0; i != str.size(); ++i) {
            if (str[i] == '(') {
                stack1[top1++] = str[i];
            } else if (str[i] == '[') {
                stack2[top2++] = str[i];
            } else if (top1 > 0 && str[i] == ')' && stack1[top1 - 1] == '(') {
                ++count;
                --top1; 
            } else if (top2 > 0 && str[i] == ']' && stack2[top2 - 1] == '[') {
                ++count;
                --top2;
            }
        }
        cout << count << "\n";
    }
    
}