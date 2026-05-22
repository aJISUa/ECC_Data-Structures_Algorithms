# 10.1: x의 n 거듭제곱 구하기(억지기법)
def slow_power(x, n) : 		    # 반복으로 을 구하는 함수 
    result = 1.0
    for i in range(n):			# 루브: n번 반복
        result = result * x
    return result

# 10.2: x의 n 거듭제곱 구하기(축소정복)
def power(x, n) :
    if n == 0 :						# 종료 조건
        return 1					# 모든 수의 0승은 1
    elif (n % 2) == 0 :				# n이 짝수 
        return power(x*x, n//2)		# 정수의 나눗셈
    else :							# n이 홀수 
        return x * power(x*x, (n-1)//2)	



# 10.3: x의 n 거듭제곱 테스트 프로그램
import time		# time 모듈 포함
print("    억지기법(2**500) =", power(2.0, 500))
print("축소정복기법(2**500) =", slow_power(2.0, 500))

t1 = time.time()
for i in range(100000) : power(2.0, 500)			# 축소정복 10만회 
t2 = time.time()
for i in range(100000) : slow_power(2.0, 500)	# 억지기법 10만회
t3 = time.time()

print("    억지기법 시간... ", t3-t2)
print("축소정복기법 시간... ", t2-t1)

# =========================================================
# 10.4: 정방형 행렬 M의 n 거듭제곱 구하기
def powerMat(x, n) :
	if n == 1 :												# 종료조건 
		return x
	elif (n % 2) == 0 :                     				# n이 짝수 
		return powerMat(multMat(x,x), n // 2)
	else :													# n이 홀수
		return multMat(x, powerMat(multMat(x,x), (n - 1) // 2)) 

def multMat(A, B) :
    rows = len(A)
    cols = len(B[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows): 
        for j in range(cols): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 

    return result


# 2x2 행렬의 4 거듭제곱 테스트
if __name__ == "__main__":
    fibo = [ [1, 1], [1, 0] ]
    result = powerMat(fibo, 4)
    for r in result: 
        print(r) 
