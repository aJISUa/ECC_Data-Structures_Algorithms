class CircularQueue :
    def __init__( self, maxSize=20 ) :
        self.front = 0
        self.rear = 0
        self.MaxSize = maxSize
        self.items = []
        for i in range( self.MaxSize ) :
            self.items.append(0)
        
    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.MaxSize

    def __len__( self ) :
       return (self.rear - self.front + self.MaxSize) % self.MaxSize

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.MaxSize
            self.items[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.MaxSize
            return self.items[self.front]

    def peek( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.MaxSize]

    def print( self ):
        list = []
        if self.front < self.rear :
            list = self.items[self.front+1:self.rear+1]
        else:
            list1 = self.items[self.front+1:self.MaxSize]
            list2 = self.items[0:self.rear+1]
            list = list1 + list2
        print(list)


#=========================================================
# 모스코드 결정트리
#=========================================================

# 4.9: 영어 대문자에 대한 모스코드 표
table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

# 4.10: 모스코드 인코딩 함수
def encode(ch):
    idx = ord(ch.upper())-ord('A')
    return table[idx][1]


# 4.11: 단순한 방법의 모스코드 디코딩 함수
def decode_simple(morse):
    for tp in table : # 모스 코드 표의 모든 문자에 대해
        if morse == tp[1] : # 찾는 코드와 같으면
            return tp[0] # 그 코드의 문자를 반환


# 4.12: 모스코드 디코딩을 위한 결정트리 만들기
def make_morse_tree():
    root = TNode( None, None, None )
    for tp in table :
        code = tp[1] # 모스 코드
        node = root
        for c in code : # 맨 마지막 문자 이전까지 --> 이동
            if c == '.' : # 왼쪽으로 이동
                if node.left == None : # 비었으면 빈 노드 만들기
                    node.left = TNode (None, None, None)
                node = node.left # 그쪽으로 이동
            elif c == '-' : # 오른쪽으로 이동
                if node.right == None : # 비었으면 빈 노드 만들기
                    node.right = TNode (None, None, None)
                node = node.right # 그쪽으로 이동

        node.data = tp[0] # 코드의 알파벳
    return root

# 4.13: 결정트리를 이용한 디코딩 함수
def decode(root, code):
    node = root
    for c in code : # 맨 마지막 문자 이전까지 --> 이동
        if c == '.' : # 왼쪽으로 이동
            node = node.left
        elif c=='-' :
           node = node.right
    return node.data



# 4.14: 인코딩과 디코딩 테스트 프로그램
morseCodeTree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code: ", mlist)
print("Decoding  : ", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()
