// 3761 - 평면 분할하기
/*
무한한 평면 위에 n개의 무한한 직선들을 긋는다.
단, 모든 직선들은 평행하지 않고, 세 직선이 한 점에서 만나지 않는다.

그 후 생긴 평면들의 총 갯수를 구하여라.

수가 커질 수 있으니 137로 나눈 나머지를 출력하여라.

- 입력
n이 입력된다. (0<=n<=10,000,000)
- 출력
평면들의 총 개수를 137로 나눈 나머지를 출력한다.
*/
#include <iostream>
using namespace std;

int main() {
    long long n;
    cin >> n;
    
    // f(n) = 1 + n*(n+1)/2 (mod 137)
    // 주기 274 활용
    long long m = n % 274;
    long long ans = (1 + m * (m + 1) / 2) % 137;
    
    cout << ans << endl;
    return 0;
}