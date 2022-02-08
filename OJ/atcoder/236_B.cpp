#include <bits/stdc++.h>
using namespace std;
#define endl "\n"

const int N = 100001;

int arr[N];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int count = 4 * n - 1;
    int a;
    while (count--) {
        cin >> a;
        arr[a] += 1;
    }
    for (int i = 1; i <= n; ++i) {
        if (arr[i] != 4) {
            cout << i << endl;
        }
    }
}

