#include <cstdio>
#include <algorithm>
using namespace std;
int n, m;
char s[5005], t[5005];
int f[5005][5005];
int main()
{
    scanf("%d%d", &n, &m);
    scanf("%s%s", s, t);
    int ans = 0;
    for (int i = n - 1; i >= 0; i--)
        for (int j = m - 1; j >= 0; j--)
        {
            f[i][j] = max(max(f[i + 1][j], f[i][j + 1]) - 1, 0);
            if (s[i] == t[j])
                f[i][j] = max(f[i][j], 2 + f[i + 1][j + 1]);
            ans = max(ans, f[i][j]);
        }
    printf("%d", ans);
}