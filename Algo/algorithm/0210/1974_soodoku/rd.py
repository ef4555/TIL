import sys

sys.stdin = open('swea_joong_1.txt')


T = int(input()) #input에 테스트 케이스 갯수 입력 
count = 0 # 스도쿠 횟수 저장하는 변수
for c in range(1, T+1): # 1부터 테스트 케이스 갯수-1까지 
    garo = True
    sero = True
    nemo = True
    correct = True
    sero_num = []
    nemo_num = []
    b = []


    for i in range(9*(c-1), 9*c):
# 세로줄 판별
        a = list(map(int, sys.stdin.readline().split())) # 스도쿠 가로줄부터 한줄 씩 리스트로 만듦
        print(a) # a에는 가로줄 한줄이 들어있음
        sero_num.append(a[0])
        if len(sero_num) == 9:
            sero_num_set = set(sero_num)
            if len(sero_num_set) != len(sero_num):
                sero = False

# 가로줄 판별
        a_set = set(a)
        if len(a) != len(a_set):
            garo = False

# 사각형 판별
        b.extend(a)
        if len(b) == 81:
            # print(b[0:81])
            for v in range(0,3):
                nemo_list = []
                for i in range(3*v,3*v+3):
                    nemo_list.extend(b[9*i:9*i+3])
                # print(nemo)
                if len(nemo_list) != len(set(nemo_list)):
                    # print('네모틀림')
                    nemo = False

                nemo_list = []
                for i in range(3*v,3*v+3):
                    nemo_list.extend(b[9*i+3:9*i+3+3])
                # print(nemo)
                if len(nemo_list) != len(set(nemo_list)):
                    # print('네모틀림')
                    nemo = False

                nemo_list = []  
                for i in range(3*v,3*v+3):
                    nemo_list.extend(b[9*i+6:9*i+3+6])
                # print(nemo)
                if len(nemo_list) != len(set(nemo_list)):
                    # print('네모틀림')
                    nemo = False       
    print(len(b)) 

    if garo == False:
        correct = False
    elif sero == False:
        correct = False
    elif nemo == False:
        correct = False
    else:
        correct = True
    count += 1
    print(f'#{count} {int(correct)}')





