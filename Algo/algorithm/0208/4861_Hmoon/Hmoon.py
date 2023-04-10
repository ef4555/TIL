'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
 

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.


[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys
sys.stdin = open('Hmoon.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Hmoon = 0 # 회문을 저장할 변수, 회문은 1개만 나온다고 조건에서 주어짐
    lst = [[0] * N for _ in range(N)] # 주어진 정보를 담을 리스트
    for i in range(N):
        lst[i] = list(input()) # 가로줄을 lst에 담아준다.
    for i in range(0, N): # 0부터 N 까지
        for j in range(0, N-M+1): # 만약 N과 M이 같으면 1케이스만 거꾸로 돌려서 확인
            # 만약 M이 N보다 작으면 가로줄을 M개씩 잘라서 거꾸로 돌려서 확인
            if ''.join(lst[i][j:j+M]) == ''.join(lst[i][j:j+M][::-1]):
                Hmoon = ''.join(lst[i][j:j+M]) # 회문인경우 변수에 저장

    sero = [[0] * N for _ in range(N)] # 세로줄을 담을 리스트 생성
    for k in range(N):
        for l in range(N):
            sero[k][l] = lst[l][k] # 가로줄 정보를 바탕으로 슬라이싱하여 세로줄 저장

    for i in range(0, N): # 0부터 N까지
        for j in range(0, N-M+1): # 만약 N과 M이 같으면 1케이스만 거꾸로 돌려서 확인
            # 만약 M이 N보다 작으면 세로줄을 M개씩 잘라서 거꾸로 돌려서 확인
            if ''.join(sero[i][j:j+M]) == ''.join(sero[i][j:j+M][::-1]):
                Hmoon = ''.join(sero[i][j:j+M])
    print(f'#{tc} {Hmoon}')

