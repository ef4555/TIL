'''
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.


[제약 사항]

가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

[입력]

총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.
'''

import sys

sys.stdin = open('flat.txt')
T = 10
for tc in range(1, T+1):
    dum = int(input()) # 덤프 횟수 입력
    a_list = list(map(int, input().split())) # 숫자 입력받음
    for i in range(len(a_list)-1, 0, -1): # 버블정렬을 이용해서 전체 리스트 정렬
        for j in range(0, i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    cnt = 0 # 카운트를 저장할 변수
    while cnt < dum: # 덤프 횟수에 도달할때까지
        a_list[-1] -= 1 # 정렬된 리스트의 가장 뒤 숫자 = 최댓값
        a_list[0] += 1 # 정렬된 리스트의 가장 앞 숫자 = 최솟값
        cnt += 1 # 덤프 횟수 증가
        for i in range(len(a_list) - 1, 0, -1):
            for j in range(0, i):
                if a_list[j] > a_list[j + 1]:
                    a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

        if a_list[-1] == a_list[0]: # 덤프 수행 후에 최댓값과 최솟값이 같으면
            break

    for i in range(len(a_list) - 1, 0, -1): # 덤프가 끝나고 다시 한번 버블정렬
        for j in range(0, i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    print(f'#{tc} {a_list[-1]-a_list[0]}') # 최댓값과 최솟값 차이 출력

