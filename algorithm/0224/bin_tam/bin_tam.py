def in_order(node):
    global val
    # 이진 탐색 트리는 완전 이진 트리를 유지 하여야 하므로
    # 노드의 개수 N보다 큰 노드 번호는 있을 수 없음
    # 완전 이진 트리의 최대 노드 번호는 2**(h+1)-1
    # 이 문제에선 그냥 N까지라고 편하게 조건 주었음
    # 중위 순회를 하여 1부터 놓기
    if node <= N:
        # 중위 순회
        in_order(node * 2)
        tree[node] = val
        val += 1
        in_order(node * 2 + 1)

import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    val = 1
    # L, R 이 없는 tree 표현
    tree = [0] * (N + 1) # 인덱스가 노드 번호를 의미
    in_order(1)
    print(tree)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')