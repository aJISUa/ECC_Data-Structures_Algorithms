# 3.1a: 단순연결구조를 위한 Node 클래스
class Node: # 단순 연결 구조를 위한 노드 클래스
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next

    # 3.1b: Node 클래스: append(node) 연산
    def append (self, node): # 현재 노드(self) 다음에 node를 넣는 연산
        if node is not None : # node가 None이 아니면
            node.link = self.link # node의 link에 self 다음 노드를 연결
        self.link = node # 이제 다음 노드는 node가 됨

    # 3.1c: Node 클래스: popNext() 연산
    def popNext (self): # 현재 노드(self)의 다음 노드를 삭제하는 연산
        next = self.link # 현재 노드(self)의 다음 노드
        if next is not None : # next가 None이 아니면
            self.link = next.link # self의 다음 노드는 next.link
        return next # 다음 노드를 반환


#=========================================================
# 3.2: 단순연결구조의 리스트 클래스

class LinkedList: # 단순연결리스트 클래스
    def __init__( self ): # 생성자
        self.head = None  # head 선언 및 None으로 초기화

    # 3.2b: LinkedList 연산: 포화, 공백 상태 검사
    def isEmpty( self ): # 공백상태 검사
        return self.head == None # head가 None이면 공백

    def isFull( self ): # 포화상태 검사
        return False # 연결된 구조에서는 포화상태 없음

    def clear( self ) : self.head = None

    # 3.2c: LinkedList 연산: getNode(pos)
    def getNode(self, pos) :
        if pos < 0 : return None # 잘못된 위치 -> None 반환
        ptr = self.head # 시작 위치 -> head
        for i in range(pos): # pos-1번 링크를 따라 이동
            if ptr == None : # pos가 리스트 크기보다 큰 경우
               return None # None 반환
            ptr = ptr.link # ptr을 진행시킴
        return ptr # 최종 노드를 반환

    # 3.2d: LinkedList 연산: getEntry(pos)
    def getEntry(self, pos) :
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None : return None # 해당 노드가 없는 경우
        else : return node.data # 있는 경우 데이터 필드 반환

    def replace(self, pos, elem) :
        node = self.getNode(pos)
        if node != None : node.data = elem

    def find(self, val) :
        node = self.head;
        while node is not None:
            if node.data == val : return node
            node = node.link
        return node

    # 3.2e: LinkedList 연산: 삽입 연산 insert(pos, e)
    def insert(self, pos, elem) :
        node = Node(elem, None) # 삽입할 새로운 노드를 만듦
        before = self.getNode(pos-1) # 삽입할 위치 이전 노드 탐색
        if before == None : # 머리 노드로 삽입하는 경우
            node.link = self.head # node의 링크가 머리노드를 가리킴
            self.head = node # 이제 node가 머리노드가 됨
        else : before.append(node) # 아닌 경우: before 다음에 추가

    # 3.2f: LinkedList 연산: 삭제 연산 delete(pos)
    def delete(self, pos) :
        before = self.getNode(pos-1) # 삭제할 위치 이전 노드 탐색
        if before == None : # 머리노드 삭제 경우
            if self.head is not None : # 공백 상태가 아니면
                self.head = self.head.link # 머리노드를 갱신
        else: before.popNext() # before의 다음노드 삭제

    # 3.2g: LinkedList 연산: 전체 요소의 수 size()
    def size( self ) :
        ptr = self.head # ptr은 머리노드에서 시작함
        count = 0; # 맨 처음에 count는 0
        while ptr is not None : # ptr이 None이 아닌 동안
            ptr = ptr.link # 링크를 따라 ptr 이동
            count += 1 # 이동할 때 마다 count 증가
        return count # count 반환

    # 3.2h: LinkedList 연산: 화면 출력 display( )
    def display(self, msg='LinkedList:' ):
        print(msg, end='')
        ptr = self.head
        while ptr is not None :
            print(ptr.data, end='->')
            ptr = ptr.link
        print('None')


#=========================================================
# 3.3: LinkedList와 파이썬 리스트 비교

# 단순연결리스트(LinkedList) 사용
s = LinkedList()
s.display('연결리스트( 초기 ): ')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("연결리스트(삽입x5): ")
s.replace(2, 90)
s.display("연결리스트(교체x1): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("연결리스트(삭제x3): ")


# 파이썬의 리스트 사용
l = []
print('파이썬list( 초기 ):', l)
l.insert(0, 10)
l.insert(0, 20)
l.insert(1, 30)
l.insert(len(l), 40)
l.insert(2, 50)
print('파이썬list(삽입x5):', l)
l[2] = 90
print('파이썬list(교체x1):', l)
l.pop(2)
l.pop(3)
l.pop(0)
print('파이썬list(삭제x3):', l)

