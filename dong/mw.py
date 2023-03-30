import sys
sys.stdin = open('input.txt')


def p(x):
    for i in range(x):
        if order[x] == order[i]:
            return False
    return True
def back(x, ans=1):
    global max_ans
    if x == len(pos):
        if ans > max_ans:
            max_ans = ans
            print(order)
        return
    for i in range(0,len(pos)):
        order[x] = i
        if p(x) and ans*pos[x][order[x]]/100 > max_ans:
            back(x+1, ans*pos[x][order[x]]/100)
 
for t in range(int(input())):
    pos = [list(map(int, input().split())) for _ in range(int(input()))]
    order = [len(pos)]*len(pos)
    max_ans = 0
    back(0)
    if len(str(round(max_ans*100, 6)).split('.')[1]) > 6:
        print(f'#{t + 1} {round(max_ans * 100, 6)}')
    else:
        print(f'#{t + 1} {str(round(max_ans * 100, 6))}'+'0'*(6-len(str(round(max_ans*100,6)).split('.')[1])))