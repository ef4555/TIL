
import sys
sys.stdin = open('googan.txt')
T = int(input()) # 첫 줄에 주어진 테스트 케이스 저장
count = 0 # 테스트 케이스의 순번을 나타낼 변수
for i in range(0, T): # 테스트 케이스 순회하면서
    N, M = map(int, input().split()) # N에 정수의 개수, M 구간의 개수
    a = list(map(int, input().split())) # 정수 N개 한 리스트에 저장
    max_value = [] # 구간합들을 저장할 리스트
    for idx in range(0, N-M+1): # 정수 - 구간+1의 인덱스만큼 순회하면서
        hap = 0 # 합을 저장할 변수
        for num in a[idx:idx+M]: # 테스트케이스 리스트를 순회하면서 M구간 잘라서 리스트 만들고 그 리스트에서
            hap += int(num) # 구간의 원소들을 더해서 hap에 저장
        max_value.append(hap) # 구간합을 max_value 에 저장
    max1 = max_value[0] # max_value 에 최댓값을 담을 변수, 초기값은 첫번째 원소
    min1 = max_value[0] # max_value 에 최솟값을 담을 변수, 변수 초기값은 첫번째 원소
    for num1 in max_value: # max_value 순회하면서
        if max1 < num1: # 최댓값 갱신
            max1 = num1
    for num2 in max_value: # 최솟값 갱신
        if min1 > num2:
            min1 = num2
    count += 1 # 반복 횟수 1 추가
    print(f'#{count} {max1 - min1}')

