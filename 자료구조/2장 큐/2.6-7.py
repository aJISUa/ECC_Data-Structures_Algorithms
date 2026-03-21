# 코드 2.6: queue 모듈의 Queue 테스트 프로그램

import queue # 파이썬의 큐 모듈 포함
import random # 난수 발생을 위해 random 모듈 포함 

q = queue.Queue(8) # 큐 객체를 생성(capacity=8)

print("삽입 순서: ", end='')
while not q.full() : # 큐에 빈 칸인 남았으면
    v = random.randint(0,100) # 0~99사이의 정수 발생
    q.put(v) # 삽입
    print(v, end=' ')
print()

print("삭제 순서: ", end='') 
while not q.empty() : # 큐에 요소가 남아 있으면
    print(q.get(), end=' ') # 꺼내서 화면에 출력
print()

#=========================================================
# 2.7: collections 모듈의 deque 클래스 테스트 프로그램

import collections # 덱을 사용하기 위해 collections 모듈 포함
dq = collections.deque() # 덱 객체를 생성

print("덱은 공백상태 아님" if dq else "덱은 공백상태")
for i in range(9):
    if i%2==0 : dq.append(i)
    else : dq.appendleft(i)
print("홀수는 전단 짝수는 후단 삽입", dq)

for i in range(2): dq.popleft()
for i in range(3): dq.pop()
print("전단 삭제 2번, 후단 삭제 3번", dq)

for i in range(9,14): dq.appendleft(i)
print("전단에 9 ~ 13 삽입          ", dq)

print("덱은 공백상태 아님" if dq else "덱은 공백상태")
