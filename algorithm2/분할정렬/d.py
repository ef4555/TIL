import sys
sys.stdin = open('input.txt')

def msort(s, e):
    global cnt
    if s + 1 == e:
        return
    m = (s+e)//2
    msort(s, m)
    msort(m, e)
    merge(s,m,e)

    # if arr[m] > arr[e]:
    #     cnt += 1

def merge(s, m, e):
    global cnt
    # print(arr)
    k = 0
    l, r = s, m # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l < m and r < e:
        if l < m and r < e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]     # 더 작은 애 복사
                l += 1  # 인덱스 하나 옆으로 이동
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1

    if l >= m:
        while r < e:
            tmp[k] = arr[r]
            r += 1
            k += 1
    else:
        cnt += 1
        while l < m:
            tmp[k] = arr[l]
            l += 1
            k += 1

    i = 0
    while i < k:
        arr[s+i] = tmp[i]
        i += 1
    return






T = int(input())
for test_case in range(1,T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    #print(ar)
    msort(0, N)  # 이 구간에 대해서 정렬해보자
    print(tmp, 'asdasd')
    # print(arr)
    print(f'#{test_case}', arr[N//2], cnt)