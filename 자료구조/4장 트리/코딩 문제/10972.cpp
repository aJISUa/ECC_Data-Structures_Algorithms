// 트리 만들기 - 실버4
/* 문제
n과 m이 주어졌을 때,
n개의 노드로 이루어져 있고,
m개의 리프로 이루어져 있는 트리를 만드는 프로그램을 작성하시오.

항상 정답이 존재하는 경우만 입력으로 주어진다.

트리는 사이클이 없는 연결 그래프이고,
리프는 차수가 1인 노드를 의미한다.

- 입력
첫째 줄에 n과 m이 주어진다.
(3 ≤ n ≤ 50, 2 ≤ m ≤ n-1)

- 출력
첫째 줄부터 n-1개의 줄에 트리의 간선 정보를 출력한다.
트리의 정점은 0번부터 n-1번까지 이다.
*/
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    // 중심 만들기
    cout << 0 << " " << 1 << '\n';

    // 리프 m개 만들기
    for (int i = 2; i <= m; i++)
    {
        cout << 1 << " " << i << '\n';
    }

    // 남은 노드 이어붙이기
    int prev = m;
    for (int i = m + 1; i < n; i++)
    {
        cout << prev << " " << i << '\n';
        prev = i;
    }

    return 0;
}