import sys

sys.stdin = open('sam_bus.txt')

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    # N 번 반복하면서 노선 입력, 빈도수 표시
    cnt = [0] * 5001 # 전체 정류장 개수
    for _ in range(N): # N 번 반복하면서
        S, E = map(int, input().split()) # 버스 정류장 어디부터 어디까지 다니는지
        for i in range(S, E+1): # S부터 E까지 정류장에 +1씩 해줌
            cnt[i] += 1
    stop = int(input()) # P개의 정류장의 개수 입력받음
    alst = [] # 각 정류장에 몇 번씩 버스가 지나갔는지
    for _ in range(stop):
        P = int(input()) # 정류장 번호 입력 받아서
        alst.append(cnt[P])

    print(f'#{test_case}', *alst)