def c(x, arr):
    if sum(arr) == M:
        lst2 = []
        # print(arr)
        for i in range(N):
            if arr[i] == 1:
                lst2.append(lst[i])
        print(*lst2)
                
        return
    
    for k in range(x, N):
        if arr[k] != 1:
            arr[k] = 1
            c(k, arr)
            arr[k] = 0
    return

N, M = map(int, input().split())
# N까지의 자연수에서 M개 뽑기
lst = [i for i in range(1, N+1)]
arr = [0]*N
c(0, arr)

