# 6.1: 선택 정렬 알고리즘(제자리 정렬 방식)

def selection_sort(A) :
    n = len(A)                              # 리스트의 크기
    for i in range(n-1) :                   # i범위: 0~n-2
        least = i                           # 최소 요소의 인덱스
        for j in range(i+1, n) :            # j의 범위: i+1~n-1
            if (A[j]<A[least]) :            # A[j]가 더 작으면
                least = j                   # least 갱신
        A[i], A[least] = A[least], A[i]	  # A[i]와 A[least] 교환 

        print("  Step %2d ="%(i+1) , A)     # 각 단계별 리스트 변화 출력


# 6.2: 선택 정렬 테스트 프로그램
print("\n선택정렬 테스트")
data = [6,3,7,4,9,1,5,2,8]
print("Original  :", data)
selection_sort(data)
print("Selection :", data)


# 6.3: 삽입 정렬 알고리즘

def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :           # i범위: 1~n-1
        key = A[i]                   # A[i]를 key에 저장
        j = i-1                      # 탐색은 i-1부터 앞으로 진행
        while j>=0 and A[j] > key :  # key보다 작은 A[j]가 나올 때 까지 
            A[j + 1] = A[j]          # A[j]를 미리 뒤로 한 칸 옮김
            j -= 1
        A[j + 1] = key               # j+1이 A[i]가 삽입될 위치임

        print("  Step %2d ="%(i+1) , A)     # 각 단계별 리스트 변화 출력



print("\n삽입정렬 테스트")
data = [6,3,7,4,9,1,5,2,8]
print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)

# ==========================================================
# 6.4: 퀵 정렬 알고리즘

def quick_sort(A, left, right) :
    if left<right :		    			# 정렬 범위가 2개 이상인 경우
        q = partition(A, left, right)	# 좌우로 분할 
        quick_sort(A, left, q - 1)		# 왼쪽 부분리스트를 퀵 정렬
        quick_sort(A, q + 1, right)		# 오른쪽 부분리스트를 퀵 정렬


# 6.5: 분할 알고리즘
def partition(A, left, right) :
	low = left + 1			
	high = right			
	pivot = A[left] 		
	while (low < high) :	
		while low <= right and A[low] <= pivot :
			low += 1
		while high >= left and A[high] > pivot :
			high-= 1

		if low < high :
			A[low], A[high] = A[high], A[low]

	A[left], A[high] = A[high], A[left]
	return high


data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]		# 입력 리스트
print("Original  : ", data)				# 만들고 모든 항목을 0으로 초기화
quick_sort(data, 0, len(data)-1)        # 퀵 정렬
print("QuickSort : ", data)

#=========================================================
# 6.6: 기수 정렬 알고리즘

from collections import deque

def radix_sort(A) :
    queues = []                             
    for i in range(BUCKETS) :               
        queues.append(deque())              

    n = len(A)
    factor = 1                              
    for d in range(DIGITS) :                
        for i in range(n) : 	            
            queues[(A[i]//factor) % BUCKETS].append(A[i])

        i = 0
        for b in range(BUCKETS) :		    
            while queues[b] :               
                A[i] = queues[b].popleft()  
                i += 1
        factor *= BUCKETS					
        print("step", d+1, A)



# 6.7: 기수 정렬 테스트 프로그램

import random       
BUCKETS = 10        
DIGITS  = 4         

data = [random.randint(1,9999) for _ in range(10)]
radix_sort(data)
print("Radix:", data)