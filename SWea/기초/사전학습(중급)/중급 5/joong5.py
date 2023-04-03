import sys

sys.stdin = open('input.txt')
T = int(input())
count = 0
for i in range(1, T+1):
    t = int(input())
    lst = list(map(int, input().split()))
    c = [0]*101 # 101개의 0을 가진 리스트 생성
    for k in lst: # 받은 입력값을 순회하면서
        c[k] += 1 # 해당 인덱스에 빈도 수를 기록

    d = 0# 최대 빈도에 해당하는 인덱스 값 기록할 리스트 
    for yy in range(len(c)-1, -1, -1): # 만약 최대 빈도가 여러개 나타나면 큰 수를 출력해야 하므로 거꾸로 순회
        if c[yy] == max(c): # 최대 빈도수를 가진 인덱스를 d에 저장
            d = yy
            break
    print(f'#{i} {d}')


