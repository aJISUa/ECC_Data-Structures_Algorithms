
#=================================================================
# 1.5: 문자열 역순 출력(파이썬 리스트 이용)

s = list() # 리스트를 객체를 생성해 스택으로 사용

msg = input("문자열 입력: ")
for c in msg :
    s.append(c) # c를 스택에 삽입

print("문자열 출력: ", end='')
while len(s) > 0: # 스택이 공백상태가 아니라면
    print(s.pop(), end='') # 하나의 요소를 꺼내서 출력
print()


#=================================================================
# 1.6: 문자열 역순 출력(LifoQueue 이용)

import queue # 파이썬의 큐 모듈 포함

s = queue.LifoQueue(maxsize=100) # 스택 객체 생성(용량=100)

msg = input("문자열 입력: ")
for c in msg :
    s.put(c) # c를 스택에 삽입

print("문자열 출력: ", end='')
while not s.empty(): # 스택이 공백상태가 아니라면
    print(s.get(), end='') # 하나의 요소를 꺼내서 출력
print()


#=================================================================
# 1.7: 반복 구조의 팩토리얼 함수

def factorial_iter(n) :
    result = 1
    for k in range(2, n+1) : # k: 2, ..., n
        result = result * k	# result에 반복적으로 곱함
    return result


#=========================================================
# 1.8: 순환 구조의 팩토리얼 함수

def factorial(n) : # 순환적으로 구현한 factorial 함수
    if n == 1 : return 1 # 종료 조건: 순환을 멈추는 부분
    else :
        return n * factorial(n - 1)	# 자신을 순환적으로 호출


#=========================================================
# 1.9: 하노이의 탑

def hanoi_tower(n, fr, tmp, to) :
    if (n == 1) : # 종료 조건
        print("원판 1: %s --> %s" % (fr, to)) # 하나의 원판 이동
    else :
        hanoi_tower(n - 1, fr, to, tmp) # 단계 1
        print("원판 %d: %s --> %s" % (n,fr,to))	# 단계 2
        hanoi_tower(n - 1, tmp, fr, to) # 단계 3

