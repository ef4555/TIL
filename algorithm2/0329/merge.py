def merge(left, right):
    pass

def msort(m):
    if len(m) == 1:
        return m
    middle = len(m //2)
    left = m[0:middle]
    right = m[middle:]
    # for x in range(m[0:middle+1]):
    #     left.append(m[x])
    # for x in range(m[middle:]):
    #     right.append(m[x])
    left = msort(left)
    right = msort(right)
    return merge(left, right)
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    msort(m)