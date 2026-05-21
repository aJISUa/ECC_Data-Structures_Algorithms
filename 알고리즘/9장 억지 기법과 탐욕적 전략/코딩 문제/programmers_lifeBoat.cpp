// 구명보트 - Lv.2
/* 투 포인터 + 그리디 알고리즘
사람들의 몸무게를 오름차순으로 정렬
가장 가벼운 사람(left)과 가장 무거운 사람(right)을 가리키는 두 포인터를 사용
두 사람의 무게 합이 limit 이하면 함께 태우고(left++, right--), 초과하면 무거운 사람만 혼자 태웁니다(right--).
어느 경우든 보트는 1대 사용됨.

- 가장 무거운 사람은 반드시 보트를 타야 하는데, 누군가와 같이 탈 수 있다면 가장 가벼운 사람과 짝지어야 보트를 가장 적게 사용할 수 있다는 그리디 아이디어
*/
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    
    int left = 0;
    int right = people.size() - 1;
    
    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            // 가장 가벼운 사람과 가장 무거운 사람이 함께 탑승
            left++;
            right--;
        } else {
            // 가장 무거운 사람 혼자 탑승
            right--;
        }
        answer++;
    }
    
    return answer;
}