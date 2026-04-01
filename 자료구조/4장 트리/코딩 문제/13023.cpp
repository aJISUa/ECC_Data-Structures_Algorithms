// ABCDE - 골드5
/* 문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다.
사람들은 0번부터 N-1번으로 번호가 매겨져 있고,
일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.

위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.
 => 이 관계 유무 판별

- 입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과
친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며,
a와 b가 친구라는 뜻이다.(0 ≤ a, b ≤ N-1, a ≠ b)
같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

- 출력
문제의 조건에 맞는 A, B, C, D, E가
존재하면 1을 없으면 0을 출력한다.
*/
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> friends;
bool visited[2001]; // 방문 여부 체크
bool found = false; // 친구 관계 만족 여부

void dfs(int node, int depth) {
    if (depth == 5) {
        found = true;
        return;
    }

    for (int next : friends[node]) {
        if (!visited[next]) { // 아직 방문하지 않은 친구라면
            visited[next] = true;
            dfs(next, depth + 1);
            visited[next] = false; // 다른 경로 탐색을 위해 방문 해제

            if (found) return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    friends.resize(n);

    for (int i = 0; i < m; i++) { 
        int a, b;
        cin >> a >> b;
        // 서로 친구
        friends[a].push_back(b);
        friends[b].push_back(a);
    }

    // 각 사람을 시작점으로 DFS 탐색
    for (int i = 0; i < n; i++) {
        fill(visited, visited + n, false); // 방문 배열 초기화
        visited[i] = true; // 시작 노드
        dfs(i, 1);

        if (found) {
            cout << 1;
            return 0;
        }
    }

    cout << 0;
}