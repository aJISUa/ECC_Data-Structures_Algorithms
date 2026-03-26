// 풍선 터뜨리기 - 실버3
/* 문제
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고.
i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다.
단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다.

각 풍선 안에는 종이가 하나 들어있고,
종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다.
이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다.
다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다.
양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다.
이동할 때에는 이미 터진 풍선은 빼고 이동한다.

예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자.
이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.

- 입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.
다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다.
종이에 0은 적혀있지 않다.


- 출력
첫째 줄에 터진 풍선의 번호를 차례로 나열한다.
*/
#include <iostream>
// #include <map> - map은 자동 정렬되므로 부적합
#include <deque>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    deque<pair<int,int>> dq;
    vector<int> result;

    cin >> n;

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        dq.push_back({i, x});
    }

    while (!dq.empty()) {
        pair<int,int> cur = dq.front(); // 현재 풍선
        dq.pop_front();

        result.push_back(cur.first); // 번호 저장

        int move = cur.second;

        if (dq.empty()) break;

        if (move > 0) {// 양수: 오른쪽 → 앞에서 빼서 뒤로
            for (int i = 0; i < move - 1; i++) {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        } else {// 음수: 왼쪽 → 뒤에서 빼서 앞으로   
            for (int i = 0; i < -move; i++) {
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }

    }

    for (int x : result)
        cout << x << " ";
    
    
    return 0;
}