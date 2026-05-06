# 7.5: 이진탐색트리를 위한 노드 클래스
class BSTNode:
    def __init__ (self, key, value): # 생성자: 키와 값을 받음
        self.key = key		
        self.value = value	
        self.left = None	
        self.right = None	

    def __str__(self) :
        return f"({self.key}:{self.value})" # (3,three)


# 7.6: 이진탐색트리의 탐색 연산(순환 구조)
def search_bst(n, key) :		
    if n == None :
        return None
    elif key == n.key: # n의 키 값과 동일->탐색성공
        return n
    elif key < n.key: # key<n의 키
        return search_bst(n.left, key) # 왼쪽 서브트리 탐색
    else: # key>n의 키
        return search_bst(n.right, key) # 오른쪽 서브트리 탐색

# 7.7: 이진탐색트리의 값을 이용한 탐색(전위 순회)
def search_value_bst(n, value) :
    if n == None : return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value) # 왼쪽서브트리에서 탐색
    if res is not None : 
       return res
    else : # 왼쪽에서 탐색 실패이면
       return search_value_bst(n.right, value) # 오른쪽 탐색 결과반환

#=========================================================
# 7.8: 이진탐색트리의 삽입 연산
def insert_bst(root, node):
	if root == None : # 공백 노드에 도달하면, 이 위치에 삽입
		return node

	if node.key == root.key : # 동일한 키는 허용하지 않음. root를 바로 반환
		return root

	# 왼쪽 서브트리에 넣어야 하는 경우. 순환호출하고 left를 갱신
	if node.key < root.key :
		root.left = insert_bst(root.left, node)

	# 오른쪽 서브트리에 넣어야 하는 경우. 순환호출하고 right를 갱신
	else :
		root.right= insert_bst(root.right, node)

	return root	# 루트 노드를 반환함


# 7.9: 이진탐색트리의 삭제 연산

def delete_bst (root, key) :
    if root == None : # 공백 트리
        return root

    # key가 루트보다 작으면 왼쪽 서브트리에서 삭제하고, left를 갱신
    if key < root.key :
        root.left = delete_bst(root.left, key)

    # key가 루트보다 크면 오른쪽 서브트리에서 삭제하고, right를 갱신
    elif key > root.key :
        root.right= delete_bst(root.right, key)

    # key가 루트와 같으면 root를 삭제
    else : 
        if root.left== None : # 단말 노드이거나 오른쪽 자식만 가진 노드 삭제
            return root.right # root 대신에 right로 대체

        if root.right== None : # 왼쪽 자식만 가진 노드 삭제
            return root.left # root 대신에 left로 대체


        # 2개의 자식을 모두 가진 경우
        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key # 후계자의 데이터를 root에 복사
        root.value = succ.value                 
        root.right = delete_bst(root.right, succ.key)

    return root


# 전위 순회: 트리 구조 출력
def preorder(n) :
    if n is not None :
        print('{', end=' ')
        print(n, end=' ')
        preorder(n.left)
        preorder(n.right)
        print('}', end=' ')


#=========================================================
# 7.10: 이진탐색트리의 테스트 프로그램

def print_node(msg, n) : # 노드 출력 함수
    print(msg, n if n != None else "탐색실패")

def print_tree(msg, r) : # 트리 출력 함수
    print(msg, end='')
    preorder(r)
    print()

data = [(6, "여섯"), (8, "여덟"), (2,"둘"), (4,"넷"),  (7,"일곱"), (5,"다섯"), (1,"하나"), (9,"아홉"), (3,"셋"), (0,"영")]

root = None # 루트 노드 생성 및 초기화
for i in range(0, len(data)): # 노드 순서대로 추가하기 
    root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

print_tree("최초: ", root) # 최초의 트리 출력

n = search_bst(root, 3);        print_node("srch 3: ", n)
n = search_bst(root, 8);        print_node("srch 8: ", n)
n = search_bst(root, 0);        print_node("srch 0: ", n)
n = search_bst(root, 10);       print_node("srch10: ", n)
n = search_value_bst(root,"둘");print_node("srch둘: ", n)
n = search_value_bst(root,"열");print_node("srch열: ", n)

root = delete_bst(root, 7);     print_tree("del  7: ", root)
root = delete_bst(root, 8);     print_tree("del  8: ", root)
root = delete_bst(root, 2);     print_tree("del  2: ", root)
root = delete_bst(root, 6);     print_tree("del  6: ", root)