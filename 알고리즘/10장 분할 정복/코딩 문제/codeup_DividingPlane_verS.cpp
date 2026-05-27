// 1960 - (재귀함수) 평면 분할하기 (small)
/*
무한한 평면 위에 n개의 무한한 직선들을 긋는다.

단, 모든 직선들은 평행하지 않고, 세 직선이 한 점에서 만나지 않는다.

그 후 생긴 평면들의 총 갯수를 구하여라.

수가 커질 수 있으니 137로 나눈 나머지를 출력하여라.
*/
#include <iostream>
using namespace std;

int solve(int n) {
    if (n == 0) return 1;
    return (solve(n - 1) + n) % 137;
}

int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}