    
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    i = N
    ic = 1
    j = M
    jc = 1
    while j > M-N:
        jc = jc*j
        j -= 1

    while i > 0:
        ic = ic*i
        i-=1
    print(int(jc / ic))