# 8.5: DFS를 이용한 신장트리(인접행렬 방식)

def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력
                ST_DFS(vtx, adj, v, visited)


# DFS를 이용한 신장트리 테스트 프로그램
vtx = ['U','V','W','X','Y']
edge= [[0,  1,  1,  0,  0],
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('ST_DFS_AM: ', end="")
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()




#=========================================================
# Prim의 MST 알고리즘


# 8.7: MST에 포함되지 않은 최소 dist의 정점 찾기
INF = 999
def getMinVertex(dist, selected) :
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if selected[v]==False and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv


# 8.8: 프림의 최소 신장 트리 알고리즘

def MSTPrim(vertex, adj) :
    n = len(vertex)
    dist = [INF] * n		# dist는 MST에서 정점까지의 거리 배열
    dist[0] = 0			    # dist: [0, INF, ... INF]
    selected = [False] * n	# selected: [False, False, ... False]

    for _ in range(n) :		# n개의 정점을 MST에 추가하면 종료됨
        u = getMinVertex(dist, selected)
        selected[u] = True	# u는 이제 MST에 포함됨
        print(vertex[u], end=' ')	# u출력 
        for v in range(n) :
             # 간선 (u,v)가 있고, v ∉ MST 이면
            if adj[u][v] != INF and not selected[v] :
                if adj[u][v]< dist[v] :	# (u,v)가 dist[v]보다 작으면
                    dist[v] = adj[u][v]	# dist[v] 갱신

        print(': ', dist)	# 중간 결과 출력

    print()


# Prim의 MST 테스트 프로그램
vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [0,	   25,		INF,	12,	  INF,     INF,		INF],
           [25,		0,	    10,		INF,	15,	   INF,	    INF],
           [INF,	10,		0,	    INF,	INF,	INF,	16],
           [12,	    INF,    INF,	0,      17,	    37,	    INF],
           [INF,	15,	    INF,    17,	    0,      19,		14  ],
           [INF,	INF,	INF,	37,     19,		0,	    42],
           [INF,    INF,	16,     INF,	14,		42,	    0   ]]    

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)
