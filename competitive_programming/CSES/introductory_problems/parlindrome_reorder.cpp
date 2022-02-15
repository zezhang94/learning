#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define LF '\n'

int arr[26];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string str;
    cin >> str;

    for (char c: str) {
        arr[c - 'A']++;
    }
    int cnt = 0;
    int even_index = -1;
    for (int i = 0; i < 26; ++i) {
        if (arr[i] % 2) {
            even_index = i;
            ++cnt;
        }
    }
    if (cnt > 1) {
        cout << "NO SOLUTION" << LF;
        return 0;
    }
    for (int i = 0; i < 26; ++i) {
        if (i == even_index) {
            continue;
        }
        string ans(arr[i] / 2, i + 'A');
        cout << ans;
    }
    if (even_index >= 0) {
        string ans(arr[even_index], even_index + 'A');
        cout << ans;
    }
    for (int i = 25; i >= 0; --i) {
        if (i == even_index) {
            continue;
        }
        string ans(arr[i] / 2, i + 'A');
        cout << ans;
    }
    cout << LF;
}
