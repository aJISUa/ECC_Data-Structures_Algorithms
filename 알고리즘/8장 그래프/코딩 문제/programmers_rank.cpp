// 순위 - Lv.3
/* 문제 설명
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

- 제한사항
선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.
*/
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector<int>> graph(n + 1, vector<int>(n + 1, 0));

    // 그래프 초기화
    for (const auto& result : results) {
        graph[result[0]][result[1]] = 1; // result[0]이 result[1]을 이겼음
    }

    // 플로이드-워셜 알고리즘으로 모든 선수 간의 승패 관계 계산
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (graph[i][k] == 1 && graph[k][j] == 1) {
                    graph[i][j] = 1; // i가 k를 이겼고 k가 j를 이겼다면 i는 j를 이긴다
                }
            }
        }
    }

    // 각 선수의 승패 관계를 확인하여 정확한 순위를 매길 수 있는 선수 수 계산
    for (int i = 1; i <= n; i++) {
        int win_count = 0;
        int lose_count = 0;
        for (int j = 1; j <= n; j++) {
            if (graph[i][j] == 1) win_count++; // i가 j를 이겼음
            if (graph[j][i] == 1) lose_count++; // j가 i를 이겼음
        }
        if (win_count + lose_count == n - 1) {
            answer++; // i 선수는 나머지 n-1명과 승패 관계가 확실하므로 순위를 매길 수 있다
        }
    }






    return answer;
}