'''
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
 



같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
 


입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


[제약 사항]

1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''

import sys

sys.stdin = open('swea_joong_1.txt')
# arr를 한줄씩 리스트로 받아서 처리
# 세로도 똑같이 만들어서 처리 
# 네모는 처음 좌표와 끝 좌표를 잡아서 그 영역 확인
'''
네모 시작점 좌표 잡기
for i in (0, 3, 6):
    for j in (0, 3, 6):
        arr[i][j]
'''
# 리스트를 셋으로 만들어서 중복이 있는지 확인 len(set(lst)) != 9이면 스도쿠 아님

def solve(arr):
    for lst in arr: # 행(가로줄)을 체크
        if len(set(lst)) != 9: # 스도쿠 실패 조건
            return 0
    arr_t = list(zip(*arr)) # 세로줄
    for lst in arr_t: # 열을 체크
        if len(set(lst)) != 9:
            return 0
    
    for i in range(0, 3, 6):
        for j in range(0, 3, 6):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != 9:
                return 0
    return 1


T = int(input()) 
for c in range(1, T+1): 
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = solve(arr)
    print(f'{tc} {ans}')