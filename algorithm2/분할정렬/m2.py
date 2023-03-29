def merge_sort(arr):
    def sort(low, high): # 원소를 나눠주는 함수
        if 1+ low == high:
            return
        mid = (high+low) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
        
    def merge(low, mid, high):
        global cnt
        tmp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l] <= arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1
        
        if l >= mid:
            while h < high:
                tmp.append(arr[h])
                h += 1
        else:  
            cnt += 1   
            while l < mid:
                tmp.append(arr[l])
                l += 1

            
        for i in range(low, high):
            arr[i] = tmp[i-low]

    return sort(0, len(arr))                  


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    a = merge_sort(lst)
    print(f'#{tc} {lst} {cnt}')