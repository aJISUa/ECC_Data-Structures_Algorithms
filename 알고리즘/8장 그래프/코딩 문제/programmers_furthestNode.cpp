// 가장 먼 노드 - Lv.3
/* 문제 설명
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

- 제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
*/
#include <string>
#include <vector>
#include <queue>

using namespace std;

// BFS로 사용한 이유: 최단 경로 문제에서 DFS는 모든 경로를 탐색하기 때문에 비효율적. 반면 BFS는 레벨별로 탐색하기 때문에 최단 경로를 보장하며, 가장 먼 노드의 레벨을 쉽게 계산할 수 있다.
int solution(int n, vector<vector<int>> edge) {
    // 인접 리스트 구성(양방향)
    vector<vector<int>> graph(n + 1);
    for (const auto& e : edge) {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }

    // BFS로 1번 노드부터 각 노드까지 최단 거리 계산
    vector<int> dist(n + 1, -1);  // -1: 미방문
    queue<int> q;
    
    dist[1] = 0; // 1번 노드부터 시작
    q.push(1); // BFS 시작

    // BFS 탐색
    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        // 현재 노드의 이웃 노드 탐색
        for (int next : graph[cur]) {
            if (dist[next] == -1) { // 아직 방문하지 않은 노드
                dist[next] = dist[cur] + 1; // 현재 거리 + 1
                q.push(next);
            }
        }
    }

    // dist 배열을 두 번 순회해서, 최대값을 먼저 확정한 뒤 그 값과 같은 노드를 세는 방식으로 구현
    // 최대 거리 찾기
    int maxDist = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] > maxDist) maxDist = dist[i];
    }
    // 최대 거리 확정 후, 최대 거리와 같은 노드 개수 세기
    int answer = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == maxDist) answer++;
    }

    return answer;
}