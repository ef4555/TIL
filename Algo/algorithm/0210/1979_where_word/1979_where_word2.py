import sys
sys.stdin = open('where_word.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split()) # N은 가로, 세로 길이, K는 단어의 길이
    # 가로줄 세로줄 리스트 만들기
    puzzle_garo = [[0]*(N) for _ in range(N)]
    for g in range(N):
        puzzle_garo[g] = list(map(int, input().split()))
    puzzle_sero = [[0]*(N) for _ in range(N)]
    for l in range(N):
        for o in range(N):
            puzzle_sero[l][o] = puzzle_garo[o][l]
    print(puzzle_garo)
    print(puzzle_sero)
    tri1 = 0
    tri2 = 0
    for i in range(N):
        j = 0 # 인덱스를 카운팅할 변수
        cnt1 = 0 # 1을 카운팅할 변수
        while j <= N-1: # 한 줄씩 인덱스 전체 순회
            if puzzle_garo[i][j] == 1: # 1을 만나면 카운팅
                cnt1 += 1
                if cnt1 == K:
                    if j == N-1: # 연속된 1이 K개인데 인덱스 마지막이면 
                        tri1 += 1 # tri1 카운트하고 반복 종료됨
                        j += 1

                    elif puzzle_garo[i][j+1] != 1:  # j가 인덱스 마지막이 아닌데 연속된 1이 K개인데 다음 인덱스 숫자가 1이 아니면(반복 끊김)
                        tri1 += 1 # tri1 카운트하고 반복 종료됨
                        cnt1 = 0 # cnt1 리셋
                        j += 1
                else: # 연속된 1이 K개가 아니면 다시 반복으로 돌아감 
                    j += 1
            else: # 1이 아니면 cnt를 0으로 리셋
                cnt1 = 0
                j += 1

    for i in range(N):
        j = 0 # 인덱스를 카운팅할 변수
        cnt2 = 0 # 1을 카운팅할 변수
        while j <= N-1: # 한 줄씩 인덱스 전체 순회
            if puzzle_sero[i][j] == 1: # 1을 만나면 카운팅
                cnt2 += 1
                if cnt2 == K:
                    if j == N-1: # 연속된 1이 K개인데 인덱스 마지막이면 
                        tri2 += 1 # tri1 카운트하고 반복 종료됨
                        j += 1

                    elif puzzle_sero[i][j+1] != 1:  # j가 인덱스 마지막이 아닌데 연속된 1이 K개인데 다음 인덱스 숫자가 1이 아니면(반복 끊김)
                        tri2 += 1 # tri1 카운트하고 반복 종료됨
                        cnt2 = 0 # cnt1 리셋
                        j += 1
                else: # 연속된 1이 K개가 아니면 다시 반복으로 돌아감 
                    j += 1
            else: # 1이 아니면 cnt를 0으로 리셋
                cnt2 = 0
                j += 1


    print(f'#{tc} {tri1+tri2}')