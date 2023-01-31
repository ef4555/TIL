import sys

sys.stdin = open('swea_joong_1.txt')

T = int(input()) #input에 테스트 케이스 갯수 입력 
for c in range(1, T+1):
    sero_num = []
    for i in range(9*(c-1), 9*c):
        a = list(map(int, sys.stdin.readline().split()))
        print(a)

        a = list(map(int, sys.stdin.readline().split())) # 스도쿠 가로줄부터 한줄 씩 리스트로 만듦
        print(a) # a에는 가로줄 한줄이 들어있음
        sero_num.append(a[0])
        if len(sero_num) == 9:
            sero_num_set = set(sero_num)
            if len(sero_num_set) != len(sero_num):
                print('세로줄 틀림')

        a_set = set(a)
        if len(a) != len(a_set):
            print('가로줄 틀림')
    print('스도쿠끝')
