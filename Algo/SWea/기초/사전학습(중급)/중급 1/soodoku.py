import sys

sys.stdin = open('swea_joong_1.txt')


T = int(input()) #input에 테스트 케이스 갯수 입력 
count = 0 # 스도쿠 횟수 저장하는 변수
for c in range(1, T+1): # 1부터 테스트 케이스 갯수-1까지 
    soo = []
    do = []
    for i in range(9*(c-1), 9*c):
        a = list(sys.stdin.readline().split()) 
        soo.extend(a)
    print(soo)
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

    if garo*sero*nemo:
        correct = False
    if sero == False:
        correct = False
    if nemo == False:
        correct = False

    print(f'#{count} {int(correct)}')






