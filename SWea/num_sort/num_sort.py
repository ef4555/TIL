import sys
sys.stdin = open('num_sort.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    mid = len(lst)//2
    print(mid)
    


