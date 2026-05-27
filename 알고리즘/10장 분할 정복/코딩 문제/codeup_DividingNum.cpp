// 2826 - 자연수 분할
/*
자연수 n을 입력받아서 n이하의 자연수 합으로 분할할 수 있는 서로 다른 경우의 수를 구하는 프로그램을 작성하시오.

n이 5인 경우의 서로 다른 분할 방법은 다음과 같다.

5
4 1
3 2
3 1 1
2 2 1
2 1 1 1
1 1 1 1 1

따라서 모두 7가지이다.
*/
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    // dp[i][j] = i를 j 이하의 수들의 합으로 분할하는 경우의 수
    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));
    
    // 0을 분할하는 방법은 1가지 (아무것도 선택하지 않음)
    for (int j = 0; j <= n; j++) dp[0][j] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (j > i) dp[i][j] = dp[i][i];
            else dp[i][j] = dp[i-j][j] + dp[i][j-1];
        }
    }
    
    cout << dp[n][n] << endl;
    return 0;
}