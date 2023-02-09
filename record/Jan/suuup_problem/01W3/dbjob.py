a, b = map(int, input().split())
dd = []
bb = []
for i in range(a):
    dd.append(input())
for m in range(b):
    bb.append(input())
s_dd = set(dd)
s_bb = set(bb)
ssss = s_dd & s_bb
gggg = sorted(list(ssss))
print(len(ssss))
for aaa in gggg:
    print(aaa)