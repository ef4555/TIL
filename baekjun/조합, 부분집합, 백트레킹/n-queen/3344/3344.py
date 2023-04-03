N = int(input())
row = [0]*N
ans = 0

def is_promising(x):
    for i in range(x): # 인덱스가 행, row[n]값이 열, 그 전의 열들과 비교(range(x))
        # row[x] == row[i] : 같은 열 체크
        # abs(row[x] - row[i]) == abs(x - i) : 대각선 체크
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # x좌표 뺀 값과 y좌표 뺀 값이 같으면 대각선
            # 위쪽 행의 요소만 비교해주면 된다(아래쪽은 아직 안놓았으므로)
            return False
        
    return True


def queen(x):
    global ans
    if x == N:
        ans += 1
        print(row)
        return 
    else:
        for i in range(N):
            row[x] = i  #[x, i]에 퀸을 놓는다.
            if is_promising(x): # x가 0일때는 다 통과
                queen(x+1) # 다음 행으로 이동
            


queen(0)
print(ans)
