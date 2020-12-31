#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ull = unsigned long long;

int divide(vector<int> &a, vector<int> &b, int i, int j) {
    int pivot = a[j], k = i, start = i, temp;  
    while (k < j) {
        if (a[k] <= pivot) {

            temp = a[start];
            a[start] = a[k];
            a[k] = temp;

            temp = b[start];
            b[start] = b[k];
            b[k] = temp;

            ++start;
        }
        ++k;
    }

    a[j] = a[start]; 
    a[start] = pivot;

    temp = b[start]; 
    b[start] = b[j];
    b[j] = temp;

    return start;
}

void quicksort(vector<int> &a, vector<int> &b, int i, int j) {
    if (i < j) {
        int p = divide(a, b, i, j);
        quicksort(a, b, i, p - 1);
        quicksort(a, b, p + 1, j);
    } 
}

void tle_solve() {
    int n;
    cin >> n;
    vector<int> a(n, 0), b(n, 0);
    int i = 0;
    while (i < n) {
        cin >> a[i++];
    }
    i = 0;
    while (i < n) {
        cin >> b[i++];
    }

    quicksort(a, b, 0, a.size() - 1);

    i = a.size() - 1;
    ull minimum = a[i], sum = 0, bigger; 
    while (i > 0) {
        sum += b[i];
        bigger = sum > a[i - 1] ? sum : a[i - 1];
        minimum = minimum < bigger ? minimum : bigger;
        i--;
    }

    if (i == 0) {
        sum += b[0];
        minimum = minimum < sum ? minimum : sum;
    }

    cout << minimum << '\n';
}

struct ab {
    int a, b;
} s[200000];
 
bool cmp(ab x, ab y) {
    return x.a < y.a;
}

void solve() {
    int n, i = 0;
    cin >> n;
    while (i < n) {
        cin >> s[i].a;
        i++;
    }
    i = 0;
    while (i < n) {
        cin >> s[i].b;
        i++;
    }

    /*
        Tip: Using std::sort when sorting is needed. It has high performance.
    */
    sort(s, s + n, cmp);

    i = n - 1;
    ull minimum = s[i].a, sum = 0, bigger; 
    while (i > 0) {
        sum += s[i].b;
        bigger = sum > s[i - 1].a ? sum : s[i - 1].a;
        minimum = minimum < bigger ? minimum : bigger;
        i--;
    }

    sum += s[0].b;
    minimum = minimum < sum ? minimum : sum;

    cout << minimum << '\n';
}

int main() {
    int cases;
    cin >> cases;
    while(cases--) {
        solve();
    }
}