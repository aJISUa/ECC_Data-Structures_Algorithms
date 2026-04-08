// 잃어버린 괄호 - 실버2
/* 문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
=> -가 등장한다면 이후 식을 모두 더해 큰 값을 빼는 것이 최소

- 입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.

그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.

입력으로 주어지는 식의 길이는 50보다 작거나 같다.

- 출력
첫째 줄에 정답을 출력한다.
*/
#include <iostream>
#include <string>

using namespace std;

int main() {
    string expression;
    cin >> expression;

    int result = 0;
    int currentNum = 0;
    bool isMinus = false; // '-' 연산자가 나왔는지 여부

    for (char ch : expression) {
        if (isdigit(ch)) { // 숫자인 경우
            currentNum = currentNum * 10 + (ch - '0'); // 숫자로 변환하여 현재 숫자에 추가
        } else {
            if (isMinus) { 
                result -= currentNum;
            } else {
                result += currentNum;
            }
            currentNum = 0;

            if (ch == '-') {
                isMinus = true;
            }
        }
    }

    // 연산자와 만나지 않고 끝난 숫자 처리
    // 마지막 숫자 처리
    if (isMinus) {
        result -= currentNum;
    } else {
        result += currentNum;
    }

    cout << result << endl;

    return 0;
}