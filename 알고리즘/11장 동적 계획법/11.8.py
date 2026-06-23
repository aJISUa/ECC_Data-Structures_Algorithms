#=========================================================
# 0-1 배낭 채우기(동적 계획법)

# 분할정복
def knapSack_bf(W, wt, val, n): 
    if n == 0 or W == 0 :       # 기반 상태. 물건이 없거나 용량이 0이면
        return 0                # 전체 가치 합은 0이 됨
  
    if (wt[n-1] > W):                           # 넣을 수 없음
        return knapSack_bf(W, wt, val, n-1)     # 나머지 항목들로 다시 처리
  
    else: 
        valWith = val[n-1] + knapSack_bf(W-wt[n-1], wt, val, n-1)
        valWithout = knapSack_bf(W, wt, val, n-1)
        return max(valWith, valWithout)


# 11.8: 0-1 배낭 채우기(동적 계획법)
def knapSack_dp(W, wt, val, n): 
    # 테이블 생성 및 0으로 초기화(W=0, n=0인 경우 모두 0)
    A = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    for i in range(1, n + 1): 
        for w in range(1, W + 1): 
            if wt[i-1] > w:         # case1: i번째 물건이 배낭 용량을 초과함
                A[i][w] = A[i-1][w] # i번째 물건을 무시하고 나머지로 계산(계산되어 있음)
            else :                  # case2: i번째 물건이 배낭 용량 이하임
                valWith = val[i-1] + A[i-1][w-wt[i-1]]  # case2.1: 넣는 경우
                valWithout = A[i-1][w]                  # case2.2: 빼는 경우
                A[i][w] = max(valWith, valWithout)      # 더 큰 값 선택
  
    return A[n][W]                  # 최종 결과가 저장됨
  

########################################################################
val = [60, 100, 190, 120, 200, 150] 
wt = [2, 5, 8, 4, 7, 6] 
W = 18
n = len(val) 
print("0-1배낭문제(분할 정복): ", knapSack_bf(W, wt, val, n)) 
print("0-1배낭문제(동적 계획): ", knapSack_dp(W, wt, val, n)) 
