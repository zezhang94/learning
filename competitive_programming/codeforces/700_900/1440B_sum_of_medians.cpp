/*
 * Tip: data type range
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        //cout << "------------";
        int n, k, mid;
        cin >> n >> k;
        mid = n % 2 ? n / 2 + 1 : n / 2;
        //cout << "mid: " << mid  << "\n";
        long start = n * k - (n % 2 ? mid * k : (mid + 1) * k) + 1;
        //cout << "start: " << start  << "\n";
        unsigned long long sum = 0;
        unsigned long long count = 1;
        long i;
        while (count < start) {
            cin >> i;
            ++count;
        }
        
        //cout << "start count: " << count  << "\n";

        long step = 0;
        long factor = (n - mid) + 1;
        while (count <= n * k) {
            cin >> i;
            if (step % factor == 0) {
                sum += i;
                //cout << "i: " << i << "\n";
            }
            ++step;
            ++count;
        }

        cout << sum << "\n";
    }
}