import sys

sys.stdin = open('paint.txt')

T = int(input())
for tc in range(1, T+1): # 테스트 케이스 순회
    N = int(input()) # 받을 좌표의 갯수 받음
    F = [[0]*10 for y in range(10)] # 영역 설정 10*10
    for i in range(N): # 받은 좌표의 갯수만큼 반복 
        p = list(map(int, input().split())) # 좌표 데이터 받음
        for aa in range(p[0], p[2]+1): # x좌표부분 받아서 순회
            for k in range(p[1], p[3]+1): # y좌표부분 받아서 순회
                if F[aa][k] == 0 or F[aa][k] == p[4]: # 좌표부분 영역에 대입해서 자기자신과 같거나 0인 경우
                    F[aa][k] = p[4] # 자기자신 색으로 변경
                else:
                    F[aa][k] = 3 # 다른색인 경우 3으로 변경
    cnt = 0
    for yy in F:
        for ii in yy:
            if ii == 3: # 3인경우
                cnt += 1 # 카운팅
    print(f'#{tc} {cnt}')
