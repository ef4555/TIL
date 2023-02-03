

'''

A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 


[예시]



다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

 

[입력]
 

첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 

[출력]


#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

'''

import sys

sys.stdin = open('elec_bus.txt')

T = int(input())
for ii in range(1, T+1):
    K, N, M = map(int,input().split()) # K는 이동거리 N은 목적지 M은 충전소의 갯수
    lst = list(map(int,input().split())) # 충전소 위치가 담긴 리스트
    st = 0 # 출발지점을 0으로
    choong = 0 # 충전 횟수 0으로 

    while True:
        if st+K >= N: # 출발지점에서 K만큼 갔을때 목적지보다 크면 반복 탈출
            break
        a = [] # K만큼 이동했을때 이동한것보다 앞에 있는 충전소의 리스트
        b = [] # K만큼 이동했을때 이동한것보다 앞에 있는 충전소의 리스트
        st += K # 출발지점에서K만큼 이동
        for i in lst: # 리스트 i를 순회하면서 
            if i <= st: # 만약 출발지점에서K만큼 이동했을때 그보다 앞에 있던  충전소들을 
                a.append(i) # a 리스트에 저장
            else:
                b.append(i) # 나머지 그보다 뒤에있는 충전소를 b에 저장
        if a == []: # K만큼 갔는데도 앞에 충전소 없는 경우(목적지에도 도달 못함)
            choong = 0 # 0을 반환하고 break
            break
        if b == []: # 뒤에 충전소가 없는 경우
            if st + K >= N: # 그 상태에서 K만큼 더 가면 도착일시
                choong += 1 # 변수 1 올리고 반복 탈출
                break
        elif a[-1] + K < b[0]: # 바로 직전 충전소에 돌아갔을때 그보다 K만큼 더 가도 다음 충전소에 도달하지 못할 경우
            choong = 0 # 0으로 리셋
            break
        st = a[-1] # 반복 마지막에 시작 지점을 a[-1]로 설정
        choong += 1

    print(f'#{ii} {choong}')


