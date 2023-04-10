def inorder(i): # 중위순회
    if i != 0: # 존재하는 정점이면
        inorder(c1[i])
        ans.append(i)
        inorder(c2[i])
    return

import sys
sys.stdin = open('sample_input.txt')
# 노드 N을 루트로 하는 서브트리에 속한 노드의 개수 알안는 프로그램
T  = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # 간선개수 E, 주어진 노드 N
    lst = list(map(int, input().split()))
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)
    i = 0
    while i < E:
        if c1[lst[2*i]] == 0: # 자식이 하나면
            c1[lst[2*i]] = lst[2*i+1]
        else: # 자식이 두개면
            c2[lst[2 * i]] = lst[2 * i + 1]
        i += 1
    ans = []
    inorder(N)
    print(f'#{tc} {len(ans)}')