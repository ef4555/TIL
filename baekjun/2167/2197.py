N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
)print(arr
K = int(input())
for ll in range(K):
    ans = 0
    a, b, c, d = map(int, input().split())

    '''
    for ii in range(a-1, c):
        for jj in range(b-1, d):
            ans += arr[ii][jj]
    '''
    print(ans)
