// 징검다리 - Lv.4
/*문제
출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

제거한 바위의 위치	각 바위 사이의 거리	거리의 최솟값
[21, 17]	[2, 9, 3, 11]	2
[2, 21]	[11, 3, 3, 8]	3
[2, 11]	[14, 3, 4, 4]	3
[11, 21]	[2, 12, 3, 8]	2
[2, 14]	[11, 6, 4, 4]	4
위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

- 제한사항
도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
바위는 1개 이상 50,000개 이하가 있습니다.
n 은 1 이상 바위의 개수 이하입니다.
*/
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    // 바위 위치 정렬 (입력이 정렬되어 있지 않음)
    sort(rocks.begin(), rocks.end());
    
    int left = 1;
    int right = distance;
    int answer = 0;
    
    // 이분 탐색: 최소 간격을 mid 이상으로 만들 수 있는지
    while (left <= right) {
        int mid = (left + right) / 2;
        
        int removed = 0; // 제거해야 할 바위 개수
        int prev = 0; // 이전에 남긴 지점 위치 (출발점부터 시작)
        
        // Greedy 검증
        for (int rock : rocks) {
            if (rock - prev < mid) {
                // 간격이 mid 미만이면 이 바위 제거
                removed++;
            } else {
                // 충분히 멀면 이 바위를 남기고, 기준점 갱신
                prev = rock;
            }
        }
        
        // 마지막으로 남긴 바위 ~ 도착점 구간 검사
        // 이 구간이 mid 미만이면 추가로 한 번 더 제거가 필요한 상황
        if (distance - prev < mid) {
            removed++;
        }
        
        if (removed > n) {
            // 너무 많이 제거해야 함 → mid가 너무 큼
            right = mid - 1;
        } else {
            // n개 이하 제거로 가능 → 더 큰 값 시도
            answer = mid;
            left = mid + 1;
        }
    }
    
    return answer;
}