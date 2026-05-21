// 체육복 - Lv.1

#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve){ // n: 전체 학생 수, lost: 체육복을 도난당한 학생 번호, reserve: 여벌 체육복을 가져온 학생 번호
    int answer = 0;
    vector<int> clothes_cnt(n+1, 1); // 학생들의 체육복 상태를 나타내는 벡터, 1: 체육복 있음, 0: 체육복 없음 - 처음에는 모두 옷을 갖고 있었으므로 1로 초기화

    // 잃어버린 학생들의 인덱스 [감소 --]
    for(int i = 0; i < lost.size(); i++) {
        clothes_cnt[lost[i]]--; // 잃어버린 학생의 체육복 감소
    }
    // 여벌 인덱스 [증가 ++]
    for(int i = 0; i < reserve.size(); i++) {
        clothes_cnt[reserve[i]]++; // 여벌을 가진 학생의 체육복 증가
    }

    // 처음부터 탐색하면서 체육복이 없는 학생이 있으면 앞뒤 학생에게 빌릴 수 있는지 확인
    for(int i = 1; i <= n; i++) {
        if(clothes_cnt[i]){
            continue; // 체육복이 있는 학생은 넘어감
        }
        // 앞번호의 학생
        if(i > 1 && clothes_cnt[i-1] == 2) { // 앞 학생이 여벌을 가지고 있는 경우
            clothes_cnt[i-1]--; // 앞 학생의 체육복 감소
            clothes_cnt[i]++; // 현재 학생의 체육복 증가
        }
        // 뒷번호의 학생
        else if(i < n && clothes_cnt[i+1] == 2) { // 뒤 학생이 여벌을 가지고 있는 경우
            clothes_cnt[i+1]--; // 뒤 학생의 체육복 감소
            clothes_cnt[i]++; // 현재 학생의 체육복 증가
        }
        // if - else 구조인 이유: 동시에 체육복 받는 것 방지
    }

    for(int i = 1; i <= n; i++) {
        if(clothes_cnt[i]) {
            answer++; // 체육복이 있는 학생 수 증가
        }
    }
     
    return answer;
}