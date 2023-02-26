


import sys
sys.stdin = open('input.txt')

def inorder(t, idx):
    temp = ''
    if idx*2 < len(t):
        temp += inorder(t, idx*2)
    temp += t[idx]
    if idx*2 + 1 < len(t):
        temp += inorder(t, idx*2+1)

    return temp

for test_case in range(1, 11):
    N = int(input())
    lst = []
    tree = [0] * (N+1)
    for _ in range(N):
        s = list(input().split())
        tree[int(s[0])] = s[1]
    print(tree)
    a = inorder(tree, 1)

    print("#{}".format(test_case), a)



