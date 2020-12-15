#include <iostream>
#include <string>
using namespace std;
int main()
{
  string array[3] = {};
  for (int i = 0; i != 3; ++i) {
    cin >> array[i];
  }

  for (int i = 2; i != -1; --i) {
    cout << array[i];
  }

  return 0;
}