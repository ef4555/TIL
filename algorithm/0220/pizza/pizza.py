import sys
sys.stdin = open('pizza.txt')


def pizza(N, M, arr):
    ans = 0
    Narr = list(enumerate(arr)) # (인덱스, 숫자) 리스트 Narr
    print(Narr)
    fire = []

    for n in range(N):
        fire.append(Narr.pop(0)) # 화덕의 크기만큼 남은 피자 대기열에 추가
    print(fire)
    while fire:
        for n in range(N):
            if len(fire) == 1: # 피자가 하나만 남아있으면
                ans = fire[0][0] # 첫번째 위치의 인덱스값 추출
                fire.pop()
                break
            fst = fire.pop(0) # 1번 화덕에 있는 피자꺼내서 인덱스와 치즈 상태 확인
            if fst[1] == 0: # 치즈가 다 녹아있으면
                if Narr: # 피자 대기열에 남아있는 피자가 있으면
                    add = Narr.pop(0) # 남은 피자 대기열 첫번째 것
                    fire.append((add[0], add[1] // 2)) # 새로운 반죽을 빈 위치에 넣고(꺼내고 넣은것) 치즈양 2분의 1
                continue
            fire.append((fst[0], fst[1] // 2)) # 치즈가 다 녹지 않았으면 맨 뒷 자리에 치즈 2분의 1 해서 교체
            print(fire)
    return (ans + 1)


T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{i} {pizza(N, M, arr)}')