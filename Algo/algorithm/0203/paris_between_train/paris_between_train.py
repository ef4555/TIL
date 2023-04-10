import sys

sys.stdin = open('paris.txt')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # D는 두 기차 사이 거리
    # A는 A 기차의 속력
    # B는 기차 B의 속력
    # F는 파리의 속력
    sigan = (D/(A+B))
    print(f'#{tc}', sigan*F)