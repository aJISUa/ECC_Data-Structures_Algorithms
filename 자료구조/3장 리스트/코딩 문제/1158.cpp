// 요세푸스 문제 - 실버4
/* 문제

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.

예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
: 1 2 3 4 5 6 7
     3 제거
 4 5 6 7 1 2 
     6 제거
    ...


N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성

- 입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

- 출력
예제와 같이 요세푸스 순열을 출력
*/
#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;
    cin >> n >> k;

    deque<int> dq;
    for (int i = 1; i <= n; i++)
    {
        dq.push_back(i);
    }
    
    vector<int> result;
    
    while (!dq.empty()) {
        for (int i = 0; i < k-1; i++){ // k번째 사람이므로 k-1번 회전
            dq.push_back(dq.front()); // 맨 앞을 뒤로 이동 시킴
            dq.pop_front(); // 맨 앞 원소 제거
        }

        result.push_back(dq.front());
        dq.pop_front();
    }

    cout << "<";
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i];
        if (i != result.size() - 1)
            cout << ", ";
    }
    cout << ">\n";

    return 0;
}