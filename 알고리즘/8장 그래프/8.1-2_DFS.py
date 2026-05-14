# 8.1: 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, adj, s, visited) :
    print(vtx[s], end=' ')          
    visited[s] = True               
    for v in range(len(vtx)) :      
        if adj[s][v] != 0 :         
            if visited[v]==False:   
                DFS(vtx, adj, v, visited)


# 8.2: 깊이 우선 탐색 테스트 프로그램

vtx = ['U','V','W','X','Y']     # 그림 8.9의 정점 리스트
edge= [[0,  1,  1,  0,  0],     # 그림 8.9의 인접 행렬
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('DFS(출발:U) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()

