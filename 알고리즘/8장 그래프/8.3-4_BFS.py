# 8.3: 너비 우선 탐색(인접 리스트 방식)

from queue import Queue                 
def BFS_AL(vtx, aList, s):
    n = len(vtx)                        
    visited = [False]*n                 
    Q = Queue()                         
    Q.put(s)                            
    visited[s] = True                   
    while not Q.empty() :
        s = Q.get()                     
        print(vtx[s], end=' ')          
        for v in aList[s] :             
            if visited[v]==False :      
                Q.put(v)                
                visited[v] = True       



# 8.4: 너비 우선 탐색 테스트 프로그램

vtx = ['U','V','W','X','Y']     # 그림 8.11(c)의 정점 리스트
aList=[[1, 2],                  # 그림 8.11(c)의 인접 리스트
       [0, 2, 3],   
       [0, 1, 4],
       [1],
       [2]]

print('BFS_AL(출발:U): ', end="")
BFS_AL(vtx, aList, 0)
print()
