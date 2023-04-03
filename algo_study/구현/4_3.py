d = ((2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)) # 나이트가 움직일 수 있는 8방향
p = input()
cnt = 0
row = int(p[1])
column = int(ord(p[0]))-int(ord('a')) + 1
for i in range(8):
    ni = row + d[i][1]
    nj = column + d[i][0]
    if 1 <= ni <= 8 and 1 <= nj <= 8:
        cnt += 1
print(cnt)