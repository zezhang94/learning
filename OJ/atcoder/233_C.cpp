#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
vector<vector<ll>> a;


ll n, x, ans = 0;

void dfs(int pos, ll val) {
    if (pos == n) {
        if (val == x) ++ans;
        return;
    }

    for (ll ai: a[pos]) {
        if (ai > x / val) {
            continue;
        }
        dfs(pos + 1, ai * val);
    }
}


int main() {
    cin >> n >> x;
    int cases = n;
    while (cases--) {
        int l, v;
        cin >> l;
        vector<ll> vec(l);
        for (int i = 0; i < l; ++i) {
            cin >> v;
            vec[i] = v;
        }
        a.push_back(vec);
    }
    dfs(0, 1);
    cout << ans << endl;
}