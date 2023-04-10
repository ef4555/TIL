import sys

sys.stdin = open('newbus.txt')

T = int(input())
for test_case in range(1, T + 1):
    stops = [0]*1001 # 버스 정류장 번호만큼의 빈 리스트 생성, 인덱스 번호는 정류장 번호를 의미
    N = int(input()) # 입력받는 버스 노선의 개수
    for i in range(N): # 버스 노선만큼 반복하면서
        tp, st, arr = map(int, input().split()) # 버스타입과 출발점, 도착점 입력받음
        if tp == 1: # 일반버스라면
            for ill in range(st, arr+1): # 출발점과 도착점 사이 모든 버스에 +1씩
                stops[ill] += 1
        elif tp == 2: # 급행버스라면
            for ex in range(st, arr+1, 2): # 2개씩 건너서 시작점이 짝수면 짝수만 홀수면 홀수만 카운팅
                stops[ex] += 1
        elif tp == 3: # 광역버스라면
            stops[st] += 1
            stops[arr] += 1
            if st % 2 == 0: # 출발점이 짝수면
                f = 1 # f는 1부터 시작하여
                while 4*f <= 1000: # 1000 이하의 4의 배수중에 반복하여
                    if st < 4*f < arr: # 출발점과 도착점 사이에 있으면
                        stops[4*f] += 1 # 버스 정류장 + 1
                    f += 1
            elif st % 2 != 0: # 출발점이 홀수면
                tr = 1 # tr는 1부터 시작하여
                while 3*tr <= 1000: # 1000 이하의 3의 배수중에 반복하여
                    if st < 3*tr < arr and 3*tr % 10 != 0: # 출발점과 도착점 사이에 있고, 10의 배수가 아니면
                        stops[3*tr] += 1 # 카운팅
                    tr += 1
    max_no = 0
    for nosun in stops: # 정류장에 지나간 버스 빈도 중 가장 큰 값을 max_no에 저장
        if max_no < nosun:
            max_no = nosun
    print(f'#{test_case}', max_no)



