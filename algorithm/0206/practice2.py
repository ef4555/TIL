'''
10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성
'''
import sys
sys.stdin = open('practice2.txt')
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    # lst에 원래 집합의 원소들 저장
    n = len(lst)
    count = False
    for i in range(1<<n):
        hap = []
        for j in range(n):
            if i & (1 << j):  # j번 비트가 1이면(그 원소가 들어있으면), if문에서 0이면 거짓 1이면 참
                hap.append(lst[j]) # j번 원소 출력
        if sum(hap) == 0 and hap != []:
            count = True
    print(f'{tc} {int(count)}')

