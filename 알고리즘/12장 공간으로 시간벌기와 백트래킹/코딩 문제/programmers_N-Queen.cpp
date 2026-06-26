// N-Queen
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int N, cnt;
int col[16];

bool ok(int row, int c) {
    for (int r = 0; r < row; r++) {
        if (col[r] == c) return false;
        if (abs(col[r] - c) == row - r) return false;
    }
    return true;
}
void dfs(int row) {
    if (row == N) { cnt++; return; }
    for (int c = 0; c < N; c++)
        if (ok(row, c)) { col[row] = c; dfs(row + 1); }
}
int solution(int n) {
    N = n; cnt = 0;
    dfs(0);
    return cnt;
}