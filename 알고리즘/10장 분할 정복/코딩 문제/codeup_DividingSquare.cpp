// 2550 - 사각형 분할하기
/*
크기가 10^9 × 10^9인 정사각형에 선들을 그어 정사각형을 몇 개의 조각으로 나누려고 한다.

모든 선들은 정사각형의 네 변 중 두 변에 평행하며, 정사각형의 네 변 중 한 변에만 접해 있고 나머지 세 변과는 만나지 않는다.

선들을 그었을 때 이 정사각형이 몇 개의 조각으로 나누어지는지 구하시오.

- 입력
첫째 줄에는 선의 개수 n이 입력된다.
(1<=n<=9,600) 둘째 줄부터 (n+1)번째 줄까지는 선의 방향 d, 선의 위치 k, 양 끝점의 좌표 a, b가 빈칸을 사이에 두고 입력된다.
(d∈{0,1}, 0<k<10^9, 0<=a<b<=10^9)

d=0이면 그 선은 가로선이고 (a,k)와 (b,k)를 잇는다.
d=1이면 그 선은 세로선이고 (k,a)와 (k,b)를 잇는다.

주어지는 입력은 임의의 두 선 m1과 m2에 대하여 d1≠d2 또는 k1≠k2이며 모든 선에 대하여 a=0과 b=10^9 중 하나를 만족한다. (둘 다 만족하지는 않는다.)

- 출력
주어진 선을 모두 그은 후 나누어진 조각의 수를 출력한다. 출력되는 값은 2^31을 넘지 않는다.
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> bit;
int bitSize;

void update(int i, int v) {
    for (; i <= bitSize; i += i & -i) bit[i] += v;
}

int query(int i) {
    int s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

int query(int l, int r) {
    if (l > r) return 0;
    return query(r) - query(l - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n;
    
    // 가로선: (k, a, b), 세로선: (k, a, b)
    vector<tuple<int,int,int>> H, V; // 각각 (k, a, b)
    
    for (int i = 0; i < n; i++) {
        int d, k, a, b;
        cin >> d >> k >> a >> b;
        if (d == 0) H.push_back({k, a, b});
        else V.push_back({k, a, b});
    }
    
    // 좌표 압축
    vector<int> ys; // 가로선의 k값 (y좌표)
    for (auto& h : H) ys.push_back(get<0>(h));
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    
    auto getY = [&](int y) {
        return lower_bound(ys.begin(), ys.end(), y) - ys.begin() + 1;
    };
    
    bitSize = ys.size();
    bit.assign(bitSize + 2, 0);
    
    // 스위프라인: x좌표 기준
    // 가로선 (k_y, a, b): x=a에서 시작, x=b에서 끝 (y=k_y에 위치)
    // 세로선 (k_x, a, b): x=k_x에서 y구간 [a,b]를 차지
    //
    // 이벤트:
    // - 가로선 시작 (x=a, type=0): y=k_y를 BIT에 추가
    // - 가로선 끝 (x=b, type=2): y=k_y를 BIT에서 제거
    // - 세로선 (x=k_x, type=1): y구간 [a,b]의 활성 가로선 수 카운트
    //
    // 같은 x에서: 시작(0) -> 쿼리(1) -> 종료(2) 순서로 처리해야
    // 교차점에서의 경계 처리가 일관됨
    
    vector<tuple<int,int,int,int,int>> events; 
    // (x, type, k, a, b)
    
    for (auto& h : H) {
        int k, a, b;
        tie(k, a, b) = h;
        events.push_back({a, 0, k, 0, 0}); // 시작
        events.push_back({b, 2, k, 0, 0}); // 끝
    }
    for (auto& v : V) {
        int k, a, b;
        tie(k, a, b) = v;
        events.push_back({k, 1, 0, a, b}); // 쿼리
    }
    
    sort(events.begin(), events.end());
    
    long long crossings = 0;
    
    for (auto& e : events) {
        int x, type, k, a, b;
        tie(x, type, k, a, b) = e;
        
        if (type == 0) {
            update(getY(k), 1);
        } else if (type == 2) {
            update(getY(k), -1);
        } else {
            // 세로선 쿼리: y가 (a, b) 범위 내인 가로선 개수
            // 경계에서 만나는 건 한 점만 공유하므로 분할에 기여 X
            // 엄밀히는 a < y < b인 활성 가로선
            int lo = lower_bound(ys.begin(), ys.end(), a + 1) - ys.begin() + 1;
            int hi = upper_bound(ys.begin(), ys.end(), b - 1) - ys.begin();
            crossings += query(lo, hi);
        }
    }
    
    // 조각 수 = 1 + (선분 수) + (교차점 수)
    // 오일러 공식 변형: 각 선분은 1개 조각 추가, 각 교차점은 추가로 1개씩 조각 더 추가
    long long answer = 1 + (long long)n + crossings;
    
    cout << answer << endl;
    return 0;
}