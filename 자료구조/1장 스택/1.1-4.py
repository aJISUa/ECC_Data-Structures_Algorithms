# 1.1a 스택을 위한 데이터
capacity = 10 # 스택 용량
array = [None] * capacity # 요소 배열: [None, None, ..., None] (길이가 capacity)
top = -1 # 상단의 인덱스: 공백 상태(-1)로 초기화함

# 1.1b 스택의 공백 상태와 포화 상태 검사
def isEmpty():
    if top == -1: return True # 공백이면 True 반환
    else: return False # 아니면 False 반환

def isFull(): return top == capacity - 1 # 비교 연산 결과를 바로 반환

# 1.1c 스택의 삽입 연산
def push(e):
    #global top
    if not isFull(): # 포화 상태가 아닌 경우
        top += 1 # top 증가(global top 선언 필요)
        array[top] = e # top 위치에 e 복사
    else: # 포화 상태: overflow
        print("stack overflow") 
        exit()

# 1.1d 스택의 삭제 연산
def pop():
    #global top
    if not isEmpty(): # 공백 상태가 아닌 경우
        top -= 1 # top 감소(global top 선언 필요)
        return array[top + 1] # 이전(top + 1) 위치의 요소 반환
    else: # 공백 상태: underflow
        print("stack underflow")
        exit()

# 1.1e 스택의 peek() 연산
def peek():
    if not isEmpty(): # 공백 상태가 아닌 경우
        return array[top]
    else: pass # underflow 예외는 처리하지 않았음

# 1.1f 스택의 size() 연산
def size(): return top + 1 # 현재 요소의 수는 top + 1

#=================================================================
# 1.2a 스택 클래스의 정의와 생성자 함수
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity # 스택 용량
        self.array = [None] * self.capacity # 요소 배열
        self.top = -1 # 상단의 인덱스

    # 1.2b: 스택 클래스의 연산들
    def isEmpty(self) : return self.top == -1
    def isFull(self) : return self.top == self.capacity-1

    def push(self, item):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass # overflow 예외는 처리하지 않았음

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass # underflow 예외는 처리하지 않았음

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass # underflow 예외는 처리하지 않았음

    def size(self) : return self.top + 1


#=================================================================
# 1.3 문자열 역순 출력 프로그램
s = ArrayStack(100) # 스택 객체를 생성

msg = input("문자열 입력: ")
for c in msg : # 문자열의 각 문자 c에 대해
    s.push(c) # c를 스택에 삽입

print("문자열 출력: ", end='')
while not s.isEmpty(): # 스택이 공백상태가 아니라면
    print(s.pop(), end='') # 하나의 요소를 꺼내서 출력
print()


#=================================================================
# 1.4: 괄호 검사 프로그램

def checkBrackets(statement):
    stack = ArrayStack(100) # 공백상태의 스택을 준비
    for ch in statement: # 문자열의 각 문자에 대해
        if ch in ('{', '[', '('): # ch가 {,[,( 중 하나이면
            stack.push(ch) # 스택에 삽입
        elif ch in ('}', ']', ')'): # ch가 닫히는 괄호이면
            if stack.isEmpty() : # 스택이 공백이면
                return False # 조건 2 위반
            else :
                left = stack.pop() # 문자를 pop해서 비교
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False # 조건 3 위반

    return stack.isEmpty() # True이면 괄호 검사 성공

