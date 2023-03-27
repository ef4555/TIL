def perm(i, k): # i값을 결정할 자리, k는 결정할 개수
    if  i == l:
        print(*p)
    else:
        for j in range(i, k): # 자신부터 오른쪽 원소들과 교환
            p[i], p[j] = p[j], p[i] # 계속 옆에꺼 옆옆에꺼 ... 자리 바꿈
            perm(i+1, k) # 다음 자리 탐색
            p[i], p[j] = p[i], p[j]


p = [1, 2, 3]
perm(0,3)
