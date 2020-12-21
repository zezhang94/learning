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
        int start = n * k - (n % 2 ? mid * k : (mid + 1) * k) + 1;
        //cout << "start: " << start  << "\n";
        long sum = 0;
        int count = 1;
        int i;
        while (count < start) {
            cin >> i;
            ++count;
        }
        
        //cout << "start count: " << count  << "\n";

        int step = 0;
        int factor = n <= 2 ? n : n - 1;
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