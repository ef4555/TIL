'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

[제약 사항]

1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)

2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.

테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.

퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
import sys
sys.stdin = open('where_word.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    # 가로 K개 연속인지 확인
    puzzle_garo = [[0]*N for _ in range(N)]
    tri2 = 0
    tri1 = 0
    for g in range(N):
        puzzle_garo[g] = list(map(int, input().split()))
    for ga in puzzle_garo:
        cnt1 = 0
        for garo in range(N-1):
            if ga[garo] == 1 and ga[garo+1] == 1:
                cnt1 += 1
            elif ga[garo] != ga[garo+1]:
                if cnt1 == K-1:
                    tri1 += 1


    puzzle_sero = [[0]*N for _ in range(N)]
    for l in range(N):
        for o in range(N):
            puzzle_sero[l][o] = puzzle_garo[o][l]
    print(puzzle_garo)
    print(puzzle_sero)
    for se in puzzle_sero:
        cnt2 = 0
        for sero in range(N-1):
            if se[sero] == 1 and se[sero+1] == 1:
                cnt2 += 1
            elif se[sero] != se[sero+1]:
                if cnt2 == K-1:
                    tri2 += 1
            
    print(tri1)
    print(tri2)
    print(f'#{tc} {tri1+tri2}')



