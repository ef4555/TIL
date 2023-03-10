'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

#1 630739
#2 740510
#3 838110

'''
T = int(input())
count = 0 # 테스트 케이스 순번 저장할 변수
for i in range(0, T): # 테스트 케이스만큼 순회
    N = int(input()) # 리스트의 원소의 갯수 N에 저장
    lst = list(map(int,input().split())) # 입력된 원소들 리스트로 만듦
    max1 = lst[0] # 최댓값을 담을 변수, 초기값은 첫번째 원소
    min1 = lst[0] # 최솟값을 담을 변수, 초기값은 첫번째 원소
    for num1 in lst: # 리스트를 순회하면서
        if max1 < num1: # 첫번째 원소보다 크면 max1 갱신
            max1 = num1
    for num2 in lst:
        if min1 > num2: # 첫번째 원소보다 크면 min1 갱신
            min1 = num2
    count += 1 # 테스트 케이스 순번 갱신
    print(f'#{count} {max1 - min1}')


