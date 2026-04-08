// 국영수 - 실버4

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Student
{
    string name;
    int kor, eng, math;
};

// false일 때만 순서 변경[true 현상 유지]
bool comp(const Student &s1, const Student &s2)
{
    if (s1.kor != s2.kor)
    {
        return s1.kor > s2.kor; // 국어 내림차순
    }
    if (s1.eng != s2.eng)
    {
        return s1.eng < s2.eng; // 영어 오름차순
    }
    if (s1.math != s2.math)
    {
        return s1.math > s2.math; // 수학 내림차순
    }
    return s1.name < s2.name; // 이름 오름차순
}

int main()
{
    int n;
    cin >> n;

    vector<Student> students(n);

    for (int i = 0; i < n; i++)
    {
        cin >> students[i].name >> students[i].kor >> students[i].eng >> students[i].math;
    }

    sort(students.begin(), students.end(), comp);

    for (int i = 0; i < n; i++)
    {
        cout << students[i].name << '\n'; // endl보다 줄바꿈 문자가 빠름
    }

    return 0;
}