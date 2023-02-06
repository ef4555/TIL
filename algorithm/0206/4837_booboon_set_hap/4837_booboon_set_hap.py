'''
3
3 6
5 15
5 10
'''


import sys

sys.stdin = open('booboon_set_hap.txt')
T = int(input()) # 영역 설정
A = [ a for a in range(1, 13)] # 12까지의 수가 들어간 리스트
for tc in range(1, T+1): 
    cnt = 0
    N, K = map(int, input().split()) # 집합의 길이와 합 기준 받음
    for i in range(1<<12): # 2^12가지의 경우 존재, 12칸을 가졌다고 생각
        hap = []
        for j in range(12): # 12까지 순회하면서 
            if i & (1<<j): # 각각 자리에 있는지 파악하고
                hap.append(A[j]) # 있으면 더해줌
        if len(hap) == N and sum(hap) == K: # 길이가 N이고 합이 K이면
            cnt += 1 # 카운트
    print(f'#{tc} {cnt}')




