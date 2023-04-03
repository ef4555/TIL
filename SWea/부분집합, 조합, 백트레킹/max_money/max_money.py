import sys
sys.stdin = open('input.txt')


def search(s, e, c, lst2):
    global result
    if c == 0:
        # print(lst2)
        r = ''
        for k in range(len(lst2)):
            r += lst2[k]
        result.append(r)
        
    else:
        for i in range(s, e):
            lst2[s], lst2[i] = lst2[i], lst2[s]
            search(s+1, e, c-1, lst2)
            # print(lst2)
            lst2[s], lst2[i] = lst2[i], lst2[s]
            


N = int(input())
for tc in range(1, N+1):
    lst = list(map(str, input().split()))
    # print(lst) # 0번째 원소 숫자판 1번째 원소 횟수
    l = list(lst[0])
    c = int(lst[1])
    result = []
    search(0, len(l), c, l)
    # print(result)
    # print(result)
    ans = 0
    for kk in range(len(result)):
        if int(result[kk]) >= ans:
            ans = int(result[kk])
    print(f'#{tc} {ans}')