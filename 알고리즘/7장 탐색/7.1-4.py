# 7.1: 순차 탐색 알고리즘

def sequential_search(A, key, low, high) : # 순차탐색
    for i in range(low, high+1) : # i : low, low+1, ... high
        if A[i] == key : # 탐색 성공하면
            return i # 인덱스 반환 
    return -1 # 탐색에 실패하면 -1 반환 


#=========================================================
# 7.2: 교환하기 전략이 추가된 순차 탐색 알고리즘

def sequential_search_transpose(A, key, low, high) :
	for i in range(low, high+1) :
		if A[i] == key :
			if i > low : # 맨 처음 요소가 아니면 이전 요소와 교환
				A[i], A[i-1] = A[i-1], A[i] 
				i = i - 1
			return i # 탐색에 성공하면 키 값의 인덱스 반환 
	return -1 # 탐색에 실패하면 -1 반환 


#=========================================================
# 7.3: 이진 탐색 알고리즘(순환 구조)

def binary_search(A, key, low, high) :
    if (low <= high) : # 항목들이 남아 있으면(종료 조건)
        middle = (low + high)//2
        if key == A[middle] :	
            return middle		
        elif (key<A[middle]) :	
            return binary_search(A, key, low, middle - 1)
        else :			
            return binary_search(A, key, middle + 1, high)
    return -1        		



#=========================================================
# 7.4: 이진 탐색 알고리즘(반복 구조)

def binary_search_iter(A, key, low, high) :
    while (low <= high) : # 항목들이 남아 있으면(종료 조건)
        middle = (low + high)//2
        if key == A[middle]:	
            return middle
        elif (key > A[middle]):	
            low = middle + 1	
        else:			
            high = middle - 1	
    return -1        		


# 보간탐색 중앙요소 위치
# middle = low + (high-low) * (key-A[low].key) / (A[high].key-A[low].key)

array = [ 3, 9, 15, 22, 31, 55, 67, 88, 91 ]
n = len(array)

print("입력배열 = ", array)
number = int(input("탐색할 숫자를 입력하시요: "))

print("순차 탐색: ", sequential_search(array, number, 0, n-1) )
print("이진 탐색: ", binary_search(array, number, 0, n-1) )
print("이진 반복: ", binary_search_iter(array, number, 0, n-1) )
