// 등굣길
#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    const int MOD = 1000000007;
    static long long dp[101][101];
    static bool wet[101][101];

    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++) {
            dp[i][j] = 0;
            wet[i][j] = false;
        }

    for (auto& p : puddles)
        wet[p[1]][p[0]] = true;

    dp[1][1] = 1;
    for (int y = 1; y <= n; y++)
        for (int x = 1; x <= m; x++) {
            if (y == 1 && x == 1) continue;
            dp[y][x] = wet[y][x] ? 0 : (dp[y-1][x] + dp[y][x-1]) % MOD;
        }

    return (int)dp[n][m];
}