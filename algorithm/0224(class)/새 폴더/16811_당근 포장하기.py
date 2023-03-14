T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    # 오름차순 정렬 후
    lst.sort()

    minV = 1001

    for i in range(N-2):
        for j in range(i+1, N-1):
            if lst[i] != lst[i+1] and lst[j] != lst[j+1]: # 같은 크기가 다른 박스에 들어가는 경우 제외
                A = i + 1
                B = j - ( i + 1 ) + 1
                C = N - ( j + 1 )
                if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2: # 빈 박스 없고 절반 초과하는 박스도 없으면
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)
    
    if minV == 1001: # 포장 할 수 없는 경우
        minV = -1

    print(minV)
