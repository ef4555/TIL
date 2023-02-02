'''

3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

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


