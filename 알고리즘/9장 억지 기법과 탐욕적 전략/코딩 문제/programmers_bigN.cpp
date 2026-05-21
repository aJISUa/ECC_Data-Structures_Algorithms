// 큰 수 만들기 - Lv.2
/* 스택 + 그리디 알고리즘
결과를 저장할 스택을 만들기
number의 각 자릿수를 순회하면서, 스택의 top이 현재 숫자보다 작고 아직 제거할 수 있다면(k > 0) 스택에서 pop
현재 숫자를 스택에 push
순회가 끝난 후에도 k가 남아있다면, 뒤에서부터 k개를 제거(이미 내림차순으로 정렬된 상태이므로 뒤쪽이 작음)

- 앞자리 숫자가 클수록 전체 수가 커지므로 앞에 있는 작은 숫자를 뒤의 큰 숫자로 대체할 수 있다면 무조건 대체하는 것이 유리
*/
#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    answer.reserve(number.size());
    
    for (char c : number) {
        // 스택 top이 현재 숫자보다 작으면 pop (k가 남아있는 동안)
        while (!answer.empty() && answer.back() < c && k > 0) {
            answer.pop_back();
            k--;
        }
        answer.push_back(c);
    }
    
    // k가 남았다면 뒤에서부터 제거 (이미 내림차순 형태)
    if (k > 0) {
        answer.erase(answer.end() - k, answer.end());
    }
    
    return answer;
}