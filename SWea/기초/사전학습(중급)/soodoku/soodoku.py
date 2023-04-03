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


T = int(input()) #input에 테스트 케이스 갯수 입력 
count = 0 # 스도쿠 횟수 저장하는 변수
for c in range(1, T+1): # 1부터 테스트 케이스 갯수-1까지 
    soo = []
    do = []
    for i in range(9*(c-1), 9*c):
        a = list(input().split()) 
        soo.extend(a)
    # print(soo)
    garo = True
    sero = True
    nemo = True
    correct = True
    # 가로줄 판별 
    for v in range(0,9):
        if len(set(soo[9*v:9*v+9])) != len(soo[9*v:9*v+9]):
            garo = False
    
        for k in range(0,9):
            do.append(soo[9*k+v])
    # 세로줄 판별
    for q in range(0,9):
        if len(set(do[9*q:9*q+9])) != len(do[9*q:9*q+9]):
            sero = False


    for p in range(0,3):
        for u in range(0,3):
            ku = []
            mm = 27*u+p*3
            ku.extend(soo[mm:mm+3])
            ku.extend(soo[mm+9:mm+9+3])
            ku.extend(soo[mm+18:mm+18+3])
            if len(set(ku)) != len(ku):
                nemo = False
    count += 1

    if garo == False:
        correct = False
    if sero == False:
        correct = False
    if nemo == False:
        correct = False

    print(f'#{count} {int(correct)}')






