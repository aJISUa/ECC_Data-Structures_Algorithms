// 조이스틱 - Lv.2
/* 두 가지 비용을 더한 것
알파벳 변경 비용 (▲▼): 각 위치마다 독립적으로 계산
    A에서 해당 알파벳까지 위로 가는 횟수와 아래로 가는 횟수 중 작은 값
    min(c - 'A', 26 - (c - 'A'))

커서 이동 비용 (◀▶): 모든 'A'가 아닌 위치를 방문해야 하며, 좌/우로 자유롭게 이동 가능
    그리디로 매 위치에서 다음으로 이동할 최적 경로를 선택
    커서 이동의 함정단순히 "오른쪽으로만 가기" vs "왼쪽으로만 가기"를 비교하는 것으로는 부족함.
    
        예를 들어 "BBBAAAAAAAB"처럼 중간에 A가 길게 있고 끝에 B가 있는 경우, 오른쪽으로 가다가 되돌아와서 왼쪽으로 가는 것이 더 빠를 수 있으므로 각 위치 i에서 다음 비-A 위치까지 갈 때, "오른쪽으로 직진" vs "왼쪽으로 돌아가기" 중 짧은 쪽을 선택
*/
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string name) {
    int answer = 0;
    int n = name.size();
    
    // 1) 알파벳 변경 비용 누적
    for (char c : name) {
        answer += min(c - 'A', 'Z' - c + 1);
    }
    
    // 2) 커서 이동 비용 (그리디)
    int move = n - 1; // 기본: 오른쪽으로 끝까지 직진
    
    for (int i = 0; i < n; i++) {
        // i 다음에 연속된 A 구간의 끝(next)을 찾기
        int next = i + 1;
        while (next < n && name[next] == 'A') {
            next++;
        }
        
        // 경로 1: 0 → i 까지 오른쪽 → 다시 왼쪽으로 돌아가서 끝(n-1)에서 next까지
        //         비용 = i*2 + (n - next)
        //         (0에서 시작해 i까지 i칸, 다시 0으로 i칸, 그리고 왼쪽으로 가서 n-1 → next 이동)
        // 경로 2: 0 → next 위치까지 한 번에 가되, i에서 왼쪽으로 갔다가 오른쪽으로 가기
        //         비용 = (n - next)*2 + i
        move = min(move, min(i * 2 + (n - next), (n - next) * 2 + i));
    }
    
    answer += move;
    return answer;
}