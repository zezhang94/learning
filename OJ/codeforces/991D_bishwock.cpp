/*
Description:
    Bishwock:
    X0 0X XX XX
    XX XX 0X X0
Target:
    maximum number of Bishwock can put into input sequence
Examples:
    00
    00
    1

    00X00X0XXX0
    0XXX0X00X00
    4

    0X0X0
    0X0X0
    0

    0XXX0
    00000
    2
    
    000X0
    00000
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    int n =  s1.size();
    vector<int> dp(n ,0);
}