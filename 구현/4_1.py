n = int(input())
x, y = 1, 1
plans = input().split()

d = ((0,-1), (0,1), (-1,0), (1,0)) # 왼 오 위 아
move = ['L', 'R', 'U', 'D']
for plan in plans:
    for i in range(4):
        if plan == move[i]:
            ni = x + d[i][0]
            nj = y + d[i][1]
            if 1 <= ni <= n and 1 <= nj <= n:
                x, y = ni, nj
print(x, y)
    