/*
Description:
    vv = w (must be consecutive)
    S = [s1, s2, ..., sn], si = 'o' or 'v'
Target:
    How many 'wow' subsequence does S have ?
Examples:
    vvvovvv
    wwoww
    4

    vvovooovovvovoovoovvvvovovvvov
    100

    wooooo  wooooo  wwwoo        ww
       5      5       6
            5       10 + 5    12 + 7 + 6
                  5 + 3 * 15  50 + 2 * 25                  
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
}