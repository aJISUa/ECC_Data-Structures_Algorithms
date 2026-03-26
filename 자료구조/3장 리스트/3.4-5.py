# 3.4a: 이중 연결 구조를 위한 DNode 클래스 정의
class DNode: # 이중 연결 노드 클래스
    def __init__ (self, elem, prev=None, next=None):
        self.data = elem # 노드의 데이터 필드(요소)
        self.next = next # 다음노드를 위한 링크
        self.prev = prev # 이전노드를 위한 링크(추가됨)

    # 3.4b: DNode의 append(node) 연산
    def append (self, node): # self 다음에 node를 넣는 연산
        if node is not None : # node가 None이 아니면
            node.next = self.next # 1)
            node.prev = self # 2)
            if node.next is not None: # 3) self의 다음노드가 있으면
                node.next.prev = node #    그 노드의 이전노드는 node
        self.next = node # 4)

    # 3.4 c: DNode의 popNext( ) 연산
    def popNext (self): # self 다음노드 삭제 연산
        node = self.next # 삭제할 노드
        if node is not None : # next가 None이 아니면
            self.next = node.next # 1)
            if self.next is not None: # 2) 다음 노드가 있으면
                self.next.prev = self # 그 노드의 이전노드는 self
        return node # 다음 노드를 반환


#======================================================================
# 3.5a: 이중 연결 리스트 클래스 정의와 생성자
class DblLinkedList: # 이중연결리스트 클래스
    def __init__( self ): # 생성자
        self.head = None # head 선언 및 None으로 초기화

    def isEmpty( self ): # 공백상태 검사
       return self.head == None # head가 None이면 공백

    def isFull( self ): # 포화상태 검사
       return False # 연결된 구조에서는 포화상태 없음

    def clear( self ) : self.head = None
    def size( self ) :
        ptr = self.head # ptr은 머리노드에서 시작함
        count = 0; # 맨 처음에 count는 0
        while ptr is not None : # ptr이 None이 아닌 동안
            ptr = ptr.next # 링크를 따라 ptr 이동
            count += 1 # 이동할 때 마다 count 증가
        return count # count 반환

    # 3.5b: DblLinkedList 연산: 화면 출력 display( )
    def display(self, msg='DblLinkedList:' ): # 기본 msg 내용을 수정
        print(msg, end='')
        ptr = self.head
        while ptr is not None :
            print(ptr.data, end='<=>') # 이중연결은 <=>로 표시
            ptr = ptr.next # 다음노드로 이동. next
        print('None')


    def getNode(self, pos) :
        if pos < 0 : return None # 잘못된 위치 -> None 반환
        ptr = self.head # 시작 위치 -> head
        for i in range(pos): # pos-1번 링크를 따라 이동
            if ptr == None : # pos가 리스트 크기보다 큰 경우
               return None # None 반환
            ptr = ptr.next # ptr을 진행시킴
        return ptr # 최종 노드를 반환

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
            node = node.next
        return node

    # 3.5c: DblLinkedList 연산: 삽입 연산
    def insert(self, pos, elem) :
        node = DNode(elem) # DNode를 만들어야 함
        before = self.getNode(pos-1) # 삽입할 위치 이전 노드 탐색
        if before == None : # 머리 노드로 삽입하는 경우
            node.next = self.head # node의 링크가 머리노드를 가리킴
            if node.next is not None: # node 다음 노드가 있으면
                node.next.prev = node # 그 노드의 이전노드는 node
            self.head = node # 이제 node가 머리노드가 됨
        else : before.append(node) # 아닌 경우: before 다음에 추가


    # 3.5d: DblLinkedList 연산: 삭제 연산
    def delete(self, pos) :
        before = self.getNode(pos-1) # 삭제할 위치 이전 노드 탐색
        if before == None : # 머리노드 삭제 경우
            if self.head is not None : # 공백 상태가 아니면
                self.head = self.head.next # 머리노드를 갱신
                self.head.prev = None # 머리노드는 이전노드 없음
        else: before.popNext() # before의 다음노드 삭제


#======================================================================
s = DblLinkedList()
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

