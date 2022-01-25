#include <iostream>
#include <vector>
#include <map>
using namespace std;

int n, q;

int main() {
    std::ios::sync_with_stdio(false);  
    std::cin.tie(NULL);

    cin >> n >> q;
    int i = 1, a;
    map<int, vector<int>> search;
    map<int, vector<int>>::iterator iter;
    while (i <= n) {
        cin >> a;
        iter = search.find(a);
        if (iter != search.end()) {
            (*iter).second.push_back(i);
        } else {
            vector<int> vec = {i};
            search[a] = vec;
        }
        ++i;
    }

    int x, k;
    while (q-- > 0) {
        cin >> x >> k;
        iter = search.find(x);
        if (iter == search.end() || k > (*iter).second.size()) {
            cout << -1 << endl; 
        } else {
            cout << (*iter).second[k - 1] << endl; 
        }   
    }
}