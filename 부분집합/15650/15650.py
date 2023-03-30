def c(s, x, arr):
    if x == M:
        # print(arr)
        lst2 = []
        # print(arr)
        for i in range(N):
            if arr[i] == 1:
                lst2.append(lst[i])
        print(*lst2)
                
        return
    
    for k in range(s, N):
        if arr[k] != 1:
            arr[k] = 1
            c(k+1, x+1, arr)
            arr[k] = 0
    return

N, M = map(int, input().split())
# N까지의 자연수에서 M개 뽑기
lst = [i for i in range(1, N+1)]
arr = [0]*N
c(0, 0, arr) # 스타트, 카운트, 배열

