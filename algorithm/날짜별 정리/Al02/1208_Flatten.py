import sys

sys.stdin = open('flatten.txt')

T = 10
for uu in range(1, T+1):
    dump_count = int(input())
    a_list = list(map(int, input().split()))

