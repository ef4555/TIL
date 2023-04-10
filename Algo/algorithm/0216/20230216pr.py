def f(i, k, s, t): # i 원소, k 집합의 크기, s i-1까지 부분집합의 합, t 찾고자하는 값
    global cnt
    global fcnt
    fcnt += 1
    if s > t: # 이미 세어버린 합이 찾고자 하는 값을 넘으면 탐색 종료
        return
    elif s == t: # 찾고자 하는 값에 도달했으면 cnt에 1 추가하고 탐색 종료
        cnt += 1
        return
    elif i == k: # 모든 원소 고려
        # if s == t:
            # for j in range(k):
                # if bit[j]:
                    # print(A[j], end = ' ')
            # print()
            # cnt += 1
        return 
    else:
        bit[i] = 1 # bit에서 i자리가 1이면
        f(i+1, k, s+A[i], t) # A[i] 포함
        bit[i] = 0 # bit에서 i자리가 0이면
        f(i+1, k, s, t) # A[i] 미포함

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 10
cnt = 0
fcnt = 0
bit = [0]*N
f(0,N,0,key)
print(cnt, fcnt) # 합이 key인 부분집합의 수