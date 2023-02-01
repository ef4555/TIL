'''
5
55 7 78 12 42
for i : N-1 -> 1 #각 구간의 끝
    for j : 0 -> i-1 # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1]
'''

lst = [55, 7, 78, 12, 42]
for i in range(len(lst) - 1, 0, -1): # 각 구간의 끝
    for j in range(0, i):  # 비교할 왼쪽 원소
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j] # 큰 원소 오른쪽으로로print(lst)

print(lst)