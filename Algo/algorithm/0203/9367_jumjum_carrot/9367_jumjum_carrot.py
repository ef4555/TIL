import sys

sys.stdin = open('jumjum.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    c_lst = list(map(int, input().split())) # 당근의 크기 리스트를 받음
    cnt = 1 # 당근이 연속해서 커지는 것을 카운팅할 변수
    max = 1 # 당근이 연속해서 커지는 최대 횟수 기록할 변수
    for i in range(N-1):
        if c_lst[i] < c_lst[i+1]: # i 번째 당근보다 i+1번째 당근이 크면
            cnt += 1 # 카운트 증가
            if max < cnt: # 최대 변수가 카운트 변수보다 작으면
                max = cnt # 갱신
        else:
            cnt = 1 # 아니면 초기화

    print(f'#{test_case}', max)