// 완주하지 못한 선수
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    unordered_map<string, int> count;
    count.reserve(participant.size() * 2);
    
    for (const string& name : participant)
        count[name]++;
    for (const string& name : completion)
        count[name]--;
    
    for (const auto& pair : count)
        if (pair.second != 0)
            return pair.first;
    
    return "";
}