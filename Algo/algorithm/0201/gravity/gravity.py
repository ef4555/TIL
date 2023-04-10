'''
상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 
낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하여라
중력은 회전이 완료된 후 적용된다
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다. 
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53


#1 7
#2 6
#3 13

'''


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

