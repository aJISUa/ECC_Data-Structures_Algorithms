# 2.1a: 원형 큐: 클래스 정의와 생성자
class ArrayQueue :
    def __init__( self, capacity = 10 ) : # 생성자 정의
        self.capacity = capacity # 용량(고정)
        self.array = [None] * capacity # 요소들을 저장할 배열
        self.front = 0 # 전단 인덱스
        self.rear = 0 # 후단 인덱스

    # 2.1b: 원형 큐: 공백상태와 포화상태 검사
    def isEmpty( self ) : # 공백 상태
        return self.front == self.rear

    def isFull( self ) : # 포화 상태
        return self.front == (self.rear+1)%self.capacity

    # 2.1c: 원형 큐: 삽입 연산
    def enqueue( self, item ): # 삽입 연산
        if not self.isFull(): # 포화 상태가 아닌 경우
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass # 오버플로 오류: 처리 않음

    # 2.1d: 원형 큐: 삭제 연산
    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass # 언더플로 오류: 처리 않음

    # 2.1e: 원형 큐: 상단 들여다보기 연산
    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else : pass # 언더플로 오류: 처리 않음

    # 2.1f: 원형 큐: 전체 요소의 수
    def size( self ) :
        return (self.rear - self.front + self.capacity) % self.capacity

    # 2.1g: 원형 큐: 전체 요소를 화면으로 출력
    def display(self, msg='Queue:' ):
        print(msg, end='= [')
        count = self.size()
        for i in range(count):
            print(self.array[(self.front+1+i)%self.capacity], end=' ')
        print("]")


#=========================================================
# 2.2: 원형 큐: 테스트 프로그램

import random
if __name__ == "__main__":
    q = ArrayQueue(8) # 큐 객체를 생성(capacity=8)

    q.display("초기 상태")
    while not q.isFull() : # 큐에 빈 칸인 남았으면
        q.enqueue(random.randint(0,100)) # 0~99사이의 정수 발생->삽입
    q.display("포화 상태")

    print("삭제 순서: ", end='') 
    while not q.isEmpty() : # 큐에 요소가 남아 있으면
        print(q.dequeue(), end=' ') # 꺼내서 화면에 출력
    print()


#=========================================================
# 2.3: 링버퍼를 위한 원형큐 삽입 수정 및 테스트 프로그램 

class ArrayQueue :
    def __init__( self, capacity = 10 ) : # 생성자 정의
        self.capacity = capacity # 용량(고정)
        self.array = [None] * capacity # 요소들을 저장할 배열
        self.front = 0 # 전단 인덱스
        self.rear = 0 # 후단 인덱스

    def isEmpty( self ) : # 공백 상태
       return self.front == self.rear

    def isFull( self ) : # 포화 상태
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ): # 삽입 연산
        if not self.isFull(): # 포화 상태가 아닌 경우
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass # 오버플로 오류: 처리 않음

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass # 언더플로 오류: 처리 않음

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else : pass # 언더플로 오류: 처리 않음

    def size( self ) : # 퀴즈
       return (self.rear - self.front + self.capacity) % self.capacity

    def display(self, msg='Queue:' ):
        print(msg, end='= [')
        count = self.size()
        for i in range(count):
            print(self.array[(self.front+1+i)%self.capacity], end=' ')
        print("]")

    # 2.3a: 원형 큐: 링 버퍼를 위한 삽입 연산
    def enqueue2( self, item ): # 링 버퍼 삽입 연산
        self.rear = (self.rear + 1) % self.capacity # 무조건 삽입
        self.array[self.rear] = item
        if self.isEmpty(): # front == rear
            self.front = (self.front + 1) % self.capacity

# 2.3b: 링 버퍼의 테스트 프로그램

import random
if __name__ == "__main__":
    q = ArrayQueue(8) # 큐 객체를 생성(capacity=8)

    q.display("초기 상태")
    for i in range(6) : # enqueue2(): 0, 1, 2, 3, 4, 5
        q.enqueue2(i)
    q.display("삽입 0-5")

    q.enqueue2(6); q.enqueue2(7) # enqueue2(): 6, 7
    q.display("삽입 6,7")

    q.enqueue2(8); q.enqueue2(9) # enqueue2(): 8, 9
    q.display("삽입 8,9")

    q.dequeue(); q.dequeue() # dequeue() 2회
    q.display("삭제  x2")


# ==========================================================
# 2.4a: 원형 덱: 큐를 상속한 클래스 정의
class CircularDeque(ArrayQueue) :
    def __init__( self, capacity=10 ) :
        super().__init__(capacity)

    # 2.4b: 원형 덱: 동작이 동일한 연산들
    def addRear( self, item ): self.enqueue(item )
    def deleteFront( self ): return self.dequeue()
    def getFront( self ): return self.peek()

    # 2.4c: 원형 덱: 추가된 연산들
    def addFront( self, item ):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else: pass

    def deleteRear( self ):
        if not self.isEmpty():
            item = self.array[self.rear];
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else: pass

    def getRear( self ): 
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass


#=========================================================
# 2.5: 원형 덱: 테스트 프로그램

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i%2==0 : dq.addRear(i)
        else : dq.addFront(i)
    dq.display("홀수는 전단 짝수는 후단 삽입")

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    dq.display("전단 삭제 2번, 후단 삭제 3번")

    for i in range(9,14): dq.addFront(i)
    dq.display("전단에 9 ~ 13 삽입")
