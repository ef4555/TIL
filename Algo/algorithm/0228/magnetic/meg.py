import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    cnt = 0
    for j in range(100):
        stack = []
        for i in range(100):
            if arr[i][j] == 1:
                stack.append(arr[i][j])
            elif arr[i][j] == 2:
                if len(stack) != 0:
                    while len(stack) != 0:
                        stack.pop()
                    cnt += 1
    print(cnt)

