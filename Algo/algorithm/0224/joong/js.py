def inorder(k): # 중위순회
    if k <= N : # 존재하는 정점이면
        inorder(k*2)
        print(item[k], end='')
        inorder(k*2+1)
    return

# 일렬로 인덱스별로 저장해서 순회
import sys
sys.stdin = open('input.txt')
T  = 10
for tc in range(1, T+1):
    N = int(input())
    item = [0] * (N + 1) # 일렬로 저장할 장소
    for i in range(N):
        a = list(input().split())
        item[i + 1] = a[1] # 받은 정보의 1번째 인덱스가 노드 번호
    print(f'#{tc}', end=' ')
    inorder(1)
    print()
