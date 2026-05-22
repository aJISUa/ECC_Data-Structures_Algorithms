#=========================================================
# k번째 작은 수 찾기 문제
#=========================================================

# 정렬을 이용한 방법
def kth_smallest_sort(A, k): 
    A.sort() 
    return A[k-1] 

  
# 10.5: 분할정복을 이용한 k번째 작은 수 찾기
def quick_select(A, left, right, k): 
    pos = partition(A, left, right) 	# A에서 피벗의 인덱스
    print(A)

    if (pos+1 == left+k):				# case 1: 찾음. 완료.
        return A[pos] 
    elif (pos+1 > left+k):				# case 2: 답은 왼쪽 부분리스트에. 
        return quick_select(A, left, pos-1, k) 
    else : 							# case 3: 답은 오른쪽 부분리스트에.
        return quick_select(A, pos+1, right, k-(pos+1-left)) 


def partition(A, left, right) :
    low = left + 1                  # 공백 4칸
    high = right                    # 공백 4칸
    pivot = A[left]                 # 공백 4칸
    while (low <= high) :           # 공백 4칸
        while low <= right and A[low] <= pivot : low += 1  # 공백 8칸
        while high>= left  and A[high] > pivot : high-= 1  # 공백 8칸

        if low < high :             # 공백 8칸
            A[low], A[high] = A[high], A[low]  # 공백 12칸

    # while문이 끝났으므로 다시 공백 4칸으로 정렬
    A[left], A[high] = A[high], A[left] 
    return high

# 테스트 프로그램
org = [27, 4, 26, 23, 34, 13, 42, 22, 48]
n = len(org) 
array = list(org)
print("입력 리스트 =", array) 
print("[축소정복] 최솟값: ", quick_select(array, 0, n-1, 1))
print()

array = list(org)
print("[축소정복] 최댓값: ", quick_select(array, 0, n-1, n)) 
print()

array = list(org)
print("[축소정복] 중앙값: ", quick_select(array, 0, n-1, 1+(n-1)//2)) 
print()

array.sort()
print("정렬 리스트 =", array) 

array = [6, 5, 7, 9, 18, 3, 8]
n = 7
print("[축소정복] 중앙값: ", quick_select(array, 0, n-1, 1+(n-1)//2)) 
print()


#=========================================================
# 10.6: 병합 정렬 알고리즘

def merge_sort(A, left, right) :	    # A[left..right]를 오름차순으로 정렬
    if left<right :			            # 항목이 2개 이상인 경우
        mid = (left + right) // 2		# 리스트의 균등 분할
        merge_sort(A, left, mid)		# 부분 리스트 정렬
        merge_sort(A, mid + 1, right)	# 부분 리스트 정렬
        merge(A, left, mid, right)	# 병합
    # else: 항목이 1개 인 경우. 자동으로 정복되었음(하나이므로)


# 10.7: 병합 과정
def merge(A, left, mid, right) :
    k = left			# 병합을 위한 임시 리스트의 인덱스
    i = left			# 왼쪽 리스트의 인덱스
    j = mid + 1			# 오른쪽 리스트의 인덱스
    while i<=mid and j<=right :
        if A[i] <= A[j] :	
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid :			# 한쪽에 남아 있는 레코드의 일괄 복사
        sorted[k:k+right-j+1] = A[j:right+1]	# 슬라이싱 이용
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]		# 슬라이싱 이용

    A[left:right+1] = sorted[left:right+1]		# A로 복사



data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]	# 입력 리스트
sorted = [0] * len(data)			# 길이가 len(data)인 임시 리스트를
print("Original  : ", data)			# 만들고 모든 항목을 0으로 초기화
merge_sort(data, 0, len(data)-1)	# 병합 정렬
print("MergeSort : ", data)



