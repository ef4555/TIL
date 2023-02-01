import sys
sys.stdin = open('fall.txt')

T = int(input())  # 테스트 케이스 수 저장
n = 0 # 테스트 케이스 순번
for i in range(0, T):
    t = int(input()) # 상자의 크기
    a = list(map(int, input().split())) # 상자의 높이를 원소로 리스트에 저장
    fall = [] # 각 줄에 떨어진 상자의 최대 낙차를 저장할 리스트
    for idx in range(0, t-1): # 첫번째 줄 상자부터 마지막 줄-1번째 상자까지
        count = 1
        for k in range(idx + 1, t-1): # 해당 상자 줄 바로 오른쪽 상자마지막 줄-1번째 상자까지
            if a[idx] == 0: # 해당 줄에 쌓인 상자의 갯수가 0이면
                count = 0 # count를 0으로 지정
            elif a[k] < a[idx]: # 해당 상자보다 높이가 낮은 상자들이 있으면
                count += 1 # count에 1씩 더한다.
        fall.append(count) # fall 함수에 count 변수를 추가한다.
    n += 1
    max1 = fall[0] # fall 리스트의 최댓값 저장
    for num1 in fall:
        if max1 < num1:
            max1 = num1
    print(f'#{n} {max1}')

