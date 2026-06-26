// 단어 변환
#include <string>
#include <vector>
#include <queue>

using namespace std;

bool diffOne(const string& a, const string& b) {
    int d = 0;
    for (int i = 0; i < (int)a.size(); i++)
        if (a[i] != b[i]) d++;
    return d == 1;
}
int solution(string begin, string target, vector<string> words) {
    int n = words.size();
    vector<bool> visited(n, false);
    queue<pair<string,int>> q;
    q.push({begin, 0});
    while (!q.empty()) {
        auto [cur, step] = q.front(); q.pop();
        if (cur == target) return step;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && diffOne(cur, words[i])) {
                visited[i] = true;
                q.push({words[i], step + 1});
            }
        }
    }
    return 0;
}