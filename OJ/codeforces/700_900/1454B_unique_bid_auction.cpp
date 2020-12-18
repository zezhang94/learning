#include <iostream>
#include <vector>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int n;
        cin >> n;
        vector<int> arr(n + 1, 0);
        int i;
        int total = n;
        while (n--) {
            cin >> i;
            if (arr[i] == 0) {
                arr[i] = total - n;
            } else if (arr[i] > 0) {
                arr[i] = -1;
            }
        }

        int result = -1;
        for (int j = 1; j < total + 1; ++j) {
            if (arr[j] > 0) {
                result = arr[j];
                break;
            }
        }
        cout << result << "\n";
    }
}