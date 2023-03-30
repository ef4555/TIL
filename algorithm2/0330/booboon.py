def f(i, k, s, key, rs):
    global cnt 
    global c
    c += 1 # 들어갈때부터 +1
    
    if s == key: # 합이 key값에 도달하면
        print(bit)
        cnt += 1
        return
    elif i == k or s>key or s+rs < key: # 리스트 끝에 도달했거나 or 합이 key보다 크거나 or 합에서 나머지를 다 더해도 키값에 도달하지 못할 때
        return 
    else:
        bit[i] = 0
        f(i+1, k, s, key, rs-A[i]) # A[i] 미포함
        bit[i] = 1
        f(i+1, k, s+A[i], key, rs-A[i]) # A[i] 포함
        
       
A = [i for i in range(1, 11)] # 인덱스에 해당하는 숫자

N = 10
bit = [0]*N # 선택한 숫자들 인덱스 위치 저장
key = 55
cnt = 0
c = 0
f(0, N, 0, key, sum(A))
print(cnt, c)