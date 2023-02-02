import sys
sys.stdin = open('jomang.txt')
T = 10 # 테스트 케이스 10개
count = 0 # 테스트 케이스 순번 저장할 변수
for i in range(1,T+1): # 테스트 케이스만큼 순회하면서
    gun_num = int(input()) # 건물의 갯수 저장
    gun_mool = list(map(int, input().split())) # 건물의 높이들 리스트에 원소로 저장
    jomang_num = 0 # 조망권이 확보된 세대를 저장
    for idx in range(2,gun_num-2): # 왼쪽 건물 2개 맨오른쪽 건물2개는 0이므로 인덱스 2부터 마지막보다 2적은 인덱스까지 순회하면서
        side = [gun_mool[idx-2], gun_mool[idx-1], gun_mool[idx+1],gun_mool[idx+2]] # 해당 건물 양쪽 두개 씩 건물의 높이 리스트에 저장
        max1 = side[0] # 4개의 건물 중 제일 높은 건물의 층수를 저장할 변수
        for num1 in side: # 해당 건물 양쪽 두개 씩 건물들 높이 저장한 리스트를 순회하면서
            if max1 < num1: # 4개 건물 중 최대 높이 건물 층수 저장
                max1 = num1
        if max1 < gun_mool[idx]: # 해당 건물이 양 옆 두개 건물 중 최대 높이 건물보다 크면
            jomang_num += gun_mool[idx]-max1 # 해당 건물 높이에서 양 옆 두개 건물 중 최대 높이 빼주면 조망권 확보된 세대수가 나오고 이를 조망권 확보된 세대수를 저장하는 jomang_num에 더해준다.
    count += 1 # 테스트 케이스 순번 갱신
    print(f'#{count} {jomang_num}')


'''
for t in range(1, 11): # test case 10개
    buildings_num = int(input())
    buildings = list(map(int, input().split()))
    result = 0
 
    i = 2
    while i < buildings_num-2:
        if max(buildings[i-2:i+3]) == buildings[i]:
            # 좌2우2 중 최대 높이이면
            second_high = max(buildings[i-2:i] + buildings[i+1:i+3])
            # 조망권 확보 세대는 2번째 높은 층 위 세대들
            result += buildings[i] - second_high
            i += 3
        else:
            i += 1
 
    print(f'#{t} {result}')
'''
