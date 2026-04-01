class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem 
        self.left = left        # 왼쪽 자식을 위한 링크
        self.right = right      # 오른쪽 자식을 위한 링크

    def isLeaf(self):
        return self.left is None and self.right is None

def preorder(n) :
    if n is not None :
        print('(', end=' ') # 중첩된 괄호 표현을 위한 출력
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
        print(')', end=' ') # 중첩된 괄호 표현을 위한 출력


def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)


def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


# 수식 트리
#=========================================================
# 4.15: 수식트리 계산 함수
def evaluate(node) :
    if node is None :
       return 0
    elif node.isLeaf() :
       return node.data
    else :
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+' : return op1 + op2
        elif node.data == '-' : return op1 - op2
        elif node.data == '*' : return op1 * op2
        elif node.data == '/' : return op1 / op2


# 4.16: 후위표기 수식을 이용한 수식트리 만들기
def buildETree( expr ):
    if len(expr) == 0 :                 
        return None

    token = expr.pop()                  
    if token in "+-*/" :                
        node = BTNode(token)            
        node.right= buildETree(expr)    
        node.left = buildETree(expr)    
        return node
    else :                              
        return BTNode(float(token))     

# 전위표기 수식을 이용해 수식트리를 만들고 루트를 반환함
def buildETree2( expr ):
    if len(expr) == 0 :                 
        return None

    token = expr.pop(0)                 
    if token in "+-*/" :                
        node = BTNode(token)            
        node.left = buildETree2(expr)   
        node.right= buildETree2(expr)   
        return node
    else :                              
        return BTNode(float(token))     


#=========================================================
# 4.17: 수식트리 테스트 프로그램

str = input("입력(후위표기): ") # 후위표기식 입력
expr = str.split() # 토큰 리스트로 변환
print("토큰분리(expr): ", expr)
root = buildETree(expr) # 후위표기 --> 수식트리
print('\n전위 순회: ', end=''); preorder(root)
print('\n중위 순회: ', end=''); inorder(root)
print('\n후위 순회: ', end=''); postorder(root)
print('\n계산 결과 : ', evaluate(root))	# 수식트리 계산

