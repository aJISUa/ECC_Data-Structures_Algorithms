// 도넛과 막대 그래프 - Lv.2
/* 문제 설명
도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프들이 있습니다. 이 그래프들은 1개 이상의 정점과, 정점들을 연결하는 단방향 간선으로 이루어져 있습니다.

* 크기가 n인 도넛 모양 그래프는 n개의 정점과 n개의 간선이 있습니다. 도넛 모양 그래프의 아무 한 정점에서 출발해 이용한 적 없는 간선을 계속 따라가면 나머지 n-1개의 정점들을 한 번씩 방문한 뒤 원래 출발했던 정점으로 돌아오게 됩니다. 도넛 모양 그래프의 형태는 다음과 같습니다.

* 크기가 n인 막대 모양 그래프는 n개의 정점과 n-1개의 간선이 있습니다. 막대 모양 그래프는 임의의 한 정점에서 출발해 간선을 계속 따라가면 나머지 n-1개의 정점을 한 번씩 방문하게 되는 정점이 단 하나 존재합니다. 막대 모양 그래프의 형태는 다음과 같습니다.

* 크기가 n인 8자 모양 그래프는 2n+1개의 정점과 2n+2개의 간선이 있습니다. 8자 모양 그래프는 크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태의 그래프입니다. 8자 모양 그래프의 형태는 다음과 같습니다.


도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프가 여러 개 있습니다. 이 그래프들과 무관한 정점을 하나 생성한 뒤, 각 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 임의의 정점 하나로 향하는 간선들을 연결했습니다.
그 후 각 정점에 서로 다른 번호를 매겼습니다.
이때 당신은 그래프의 간선 정보가 주어지면 생성한 정점의 번호와 정점을 생성하기 전 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 구해야 합니다.

그래프의 간선 정보를 담은 2차원 정수 배열 edges가 매개변수로 주어집니다. 이때, 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 순서대로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

- 제한사항
1 ≤ edges의 길이 ≤ 1,000,000
edges의 원소는 [a,b] 형태이며, a번 정점에서 b번 정점으로 향하는 간선이 있다는 것을 나타냅니다.
1 ≤ a, b ≤ 1,000,000
문제의 조건에 맞는 그래프가 주어집니다.
도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.
*/
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// edges_rows는 2차원 배열 edges의 행 길이, edges_cols는 2차원 배열 edges의 열 길이입니다.
int* solution(int** edges, size_t edges_rows, size_t edges_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(4 * sizeof(int));
    answer[0] = 0; answer[1] = 0; answer[2] = 0; answer[3] = 0;

    // 최대 정점 번호 찾기
    int maxV = 0;
    for (size_t i = 0; i < edges_rows; i++) {
        if (edges[i][0] > maxV) maxV = edges[i][0];
        if (edges[i][1] > maxV) maxV = edges[i][1];
    }

    // in/out degree 계산
    int* outDeg = (int*)calloc(maxV + 1, sizeof(int));
    int* inDeg  = (int*)calloc(maxV + 1, sizeof(int));

    for (size_t i = 0; i < edges_rows; i++) {
        outDeg[edges[i][0]]++;
        inDeg[edges[i][1]]++;
    }

    // 각 유형의 정점 카운트
    int created = 0;     // 생성된 정점 번호
    int bars = 0;        // 막대 그래프 수
    int eights = 0;      // 8자 그래프 수

    for (int v = 1; v <= maxV; v++) {
        // 존재하지 않는 정점 번호일 수 있으므로 degree가 모두 0이면 skip
        if (outDeg[v] == 0 && inDeg[v] == 0) continue;

        if (outDeg[v] >= 2 && inDeg[v] == 0) {
            created = v;                       // 생성된 정점
        } else if (outDeg[v] == 0) {
            bars++;                            // 막대 끝 정점
        } else if (outDeg[v] == 2 && inDeg[v] >= 2) {
            eights++;                          // 8자 중심 정점
        }
    }

    // 도넛 개수 = (생성 정점의 out-degree) - 막대 - 8자
    int donuts = outDeg[created] - bars - eights;

    answer[0] = created;
    answer[1] = donuts;
    answer[2] = bars;
    answer[3] = eights;

    free(outDeg);
    free(inDeg);
    return answer;
}