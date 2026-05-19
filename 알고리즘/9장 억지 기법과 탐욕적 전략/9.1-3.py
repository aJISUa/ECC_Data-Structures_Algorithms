# 9.1: 문자열 매칭(억지기법)

def string_matching( T, P ):		# T는 입력, P는 패턴
    n = len(T)						# n: 입력 문자열의 길이
    m = len(P)						# m: 패턴 문자열의 길이
    for i in range(n-m+1) :			# i: 0, 1, ..., n-m
        j = 0
        while j < m and P[j]==T[i+j] :	# 패턴 문자열을 모두 비교
               j = j + 1
        if j == m :					# 모든 문자가 일치하면, 매칭 성공
            return i				# 현재 위치 반환
    return -1						# 문자열 매칭 실패


# 문자열 매칭(억지 기법) 테스트
text = 'HELLO WORLD'
pattern = 'LO'
print( pattern, 'in', text, '-->', string_matching(text, pattern))
pattern = 'HI'
print( pattern, 'in', text, '-->', string_matching(text, pattern))

#=========================================================
# 0-1 배낭 채우기
#=========================================================

# 9.2: 0-1 배낭 채우기(억지 기법)

# wgt: 물건들의 무게 리스트
# val: 물건들의 가치 리스트
# W: 배낭의 용량
def Knapsack01_BF(wgt, val, W):
    n = len(wgt)
    bestVal = 0
    bestLst = []
    for i in range(2**n) :      # 0 ~ 2^n-1
#        print(".", end='')
        s = [0]*n
        for d in range(n) :
            s[d] = i%2
            i = i//2

        sumVal = 0
        sumWgt = 0
        for d in range(n):
            if s[d] == 1 :
               sumWgt += wgt[d]
               sumVal += val[d]

        if sumWgt <= W :
            if sumVal > bestVal :
                bestVal = sumVal
                bestLst = list(s)

    # print(bestVal, bestLst)
    return bestVal


# 0-1 배낭 채우기(억지 기법) 테스트 프로그램
if __name__ == '__main__':
    weight = [10, 20, 30, 25, 35]	# 물건별 무게
    value  = [60, 100, 120, 70, 85]	# 물건별 가치
    W = 80				            # 배낭의 제한 용량

    print("Knapsack01-BruteForce:", Knapsack01_BF(weight, value, W))


#=========================================================
# 분할 가능한 배낭 채우기
#=========================================================

# 9.3: 분할 가능한 배낭 채우기(탐욕적 기법)
def KnapSackFrac(wgt, val, W):
    bestVal = 0                 # 전체 배낭의 가치
    for i in range(len(wgt)):
        if W <= 0 :             # 용량이 다 찬 경우
           break
        if W >= wgt[i]:         # 물건 전체가 들어갈 수 있는 경우
            W -= wgt[i]
            bestVal += val[i] 
        else:                   # 물건의 일부만 넣을 수 있는 경우
            fraction = W / wgt[i]
            bestVal += val[i] * fraction 
            break

    return bestVal

weight = [12,  10, 8]	# 물건별 무게 (가치/무게 의 내림차순으로 정렬됨)
value  = [120, 80, 60]	# 물건별 가치 (가치/무게 의 내림차순으로 정렬됨)
W = 18				    # 배낭의 제한 용량
print("Fractional Knapsack(18):", KnapSackFrac(weight, value, W)) 
