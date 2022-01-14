#include <iostream>
#include <string>
using namespace std;

int main() {
    int s, e;
    cin >> s >> e;
    s--;
    e--;
    string str;
    cin >> str;
    char tmp;
    while (s <= e) {
        tmp = str[s];
        str[s++] = str[e];
        str[e--] = tmp;
    }
    cout << str << endl;
}