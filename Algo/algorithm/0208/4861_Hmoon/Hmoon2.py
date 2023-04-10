from pprint import pprint
import sys
sys.stdin = open('Hmoon.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Hmoon = 0 # 회문을 저장할 변수, 회문은 1개만 나온다고 조건에서 주어짐
    lst = [[0] * N for _ in range(N)] # 주어진 정보를 담을 리스트
    for i in range(N):
        lst[i] = list(input()) # 가로줄을 lst에 담아준다.
    pprint(lst)
    for i in range(0, N): # 0부터 N 까지
        for j in range(0, N-M+1):
            if lst[i][j:j+M][0] == lst[i][j:j+M][-1]: # 기본적으로 회문이 되려면 맨 첫글자와 맨 뒷글자가 같아야 하므로 같은지 확인하여 아니면 탐색하지 않음
            # 만약 N과 M이 같으면 1케이스만 거꾸로 돌려서 확인
            # 만약 M이 N보다 작으면 가로줄을 M개씩 잘라서 거꾸로 돌려서 확인
                if ''.join(lst[i][j:j+M]) == ''.join(lst[i][j:j+M][::-1]):
                    Hmoon = ''.join(lst[i][j:j+M]) # 회문인경우 변수에 저장
            else:
                continue

    sero = [[0] * N for _ in range(N)] # 세로줄을 담을 리스트 생성
    for k in range(N):
        for l in range(N):
            sero[k][l] = lst[l][k] # 가로줄 정보를 바탕으로 슬라이싱하여 세로줄 저장

    for i in range(0, N): # 0부터 N까지
        for j in range(0, N-M+1):
            if sero[i][j:j+M][0] == sero[i][j:j+M][-1]: # 기본적으로 회문이 되려면 맨 첫글자와 맨 뒷글자가 같아야 하므로 같은지 확인하여 아니면 탐색하지 않음
            # 만약 N과 M이 같으면 1케이스만 거꾸로 돌려서 확인
            # 만약 M이 N보다 작으면 세로줄을 M개씩 잘라서 거꾸로 돌려서 확인
                if ''.join(sero[i][j:j+M]) == ''.join(sero[i][j:j+M][::-1]):
                    Hmoon = ''.join(sero[i][j:j+M])
            else:
                continue
    print(f'#{tc} {Hmoon}')
