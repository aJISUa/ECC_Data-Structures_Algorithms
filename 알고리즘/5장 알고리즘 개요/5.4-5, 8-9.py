# 5.4: 세 개의 숫자에서 최댓값을 찾는 알고리즘

def find_max( a, b, c ) :
    
    max = a
    if b > max :
        max = b
    if c > max :
        max = c
    return max

print("find_max(1, 2, 3) = ", find_max(1, 2, 3))
print("find_max(3, 2, 1) = ", find_max(3, 2, 1))
print("find_max(2, 1, 3) = ", find_max(2, 1, 3))


#=========================================================
# 5.5: time 모듈을 이용한 실행시간 측정 예
import time # time 모듈 불러오기

start = time.time() # 현재 시각을 start에 저장(시작 시각)
#testAlgorithm(input) # 실행시간을 측정하려는 알고리즘 호출
for _ in range (1000000): 
	find_max(2, 1, 3)
end = time.time() # 현재 시각을 end에 저장(종료 시각)
print("실행시간 = ", end-start)	# 실제 실행시간(종료-시작)을 출력



#=========================================================
# 5.8: 리스트에서 최댓값을 찾는 알고리즘

def find_max( A ):
    n = len(A) # 입력의 크기
    max = A[0] # max 초기화
    for i in range(n) : # 반복 제어부
        if A[i] > max : # 반복문 내부 -> n번 반복(가장 많이 처리)
            max = A[i]
    return max # 결과 반환


#=========================================================
# 5.9: 리스트에서 어떤 값을 찾는 알고리즘

def find_key( A, key ):
    n = len(A) # 입력의 크기
    for i in range(n) : # 반복 제어부
        if A[i] == key : # 탐색 성공 --> 인덱스 반환
            return i
    return -1 # 탐색 실패 --> -1 반환



data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("find_max: ", find_max(data))
print("find_key: ", find_key(data, 5))
print("find_key: ", find_key(data, 10))