import sys

sys.stdin = open('flat.txt')

def maxx_idx(lst):
    max_v = lst[0]  # 기본은 맨 앞
    idx = 0  # 인덱스 값 저장할거
    count = 0  # 인덱스 값 표시할거
    for i in lst:  # 리스트 역으로 순회하면서
        if max_v < i:  # 큰값 만나면 값을 바꿈
            max_v = i
            idx = count
        count += 1
    return max_v, idx  # 값, 위치 반환

def minn_idx(lst):
    max_v = lst[0]  # 기본은 맨 앞
    idx = 0  # 인덱스 값 저장할거
    count = 0  # 인덱스 값 표시할거
    for i in lst:  # 리스트 역으로 순회하면서
        if max_v > i:  # 큰값 만나면 값을 바꿈
            max_v = i
            idx = count
        count += 1
    return max_v, idx  # 값, 위치 반환

for tc in range(1,11):

    dumping_numb = int(input())
    area_lst = list(map(int, input().split()))

    for dump in range(dumping_numb):  # 덤핑 횟수만큼
        area_lst[maxx_idx(area_lst)[1]] -= 1  # 큰거 줄임
        area_lst[minn_idx(area_lst)[1]] += 1  # 작은거 올림


    print(f'#{tc} {maxx_idx(area_lst)[0] - minn_idx(area_lst)[0]}')  # 높은거 낮은거 뺌





