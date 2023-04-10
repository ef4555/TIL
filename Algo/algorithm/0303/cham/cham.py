import sys
sys.stdin = open('cham.txt')
# 큰 사각형 넓이를 구하고
# 인접하지 않은 사각형의 넓이를 구하여 빼 주면 답을 구할 수 있다
# 가장 긴 변 양 옆 값 제외하면 작은 사각형의 변들이 나온다.
N = int(input())
# 4 북 3 남 1 동 2 서
g = []
s = []
for _ in range(6):
    A, B = map(int, input().split())
    if A == 1 or A == 2:
        g.append(B)
    elif A == 3 or A == 4:
        s.append(B)
# print(g, s)
b_g_i = g.index(max(g))
b_s_i = s.index(max(s))
s_m = abs(g[b_s_i] - g[b_s_i - 1]) * abs(s[b_g_i] - s[b_g_i + 1])
print((max(g)*max(s) - s_m)*N)

