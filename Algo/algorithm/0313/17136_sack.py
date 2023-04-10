import sys
sys.stdin = open("sack.txt")
arr = [list(map(int, input().split())) for _ in range(10)]
print(arr)
sack = [0, 5, 5, 5, 5, 5] # 색종이 개수

for k in range(10-5):
    for kk in range(10-5):
        cnt = 0
        lst = []
        for i in range(0, 10-5):
            for j in range(0, 10-5):
                print(i+k, j+kk)
        print(lst)
        print(len(lst))
print(sack)

