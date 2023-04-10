def hoare(A, l, r):
    pivot = A[l] # 맨 왼쪽원소 기준
    i = l        # 피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = r        # 피복보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j : # 교차하지 않은 경우
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]
    return j

def qsort(A, l, r):
    global cnt
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)
        
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    qsort(arr, 0, N-1)
    print(*arr, cnt)