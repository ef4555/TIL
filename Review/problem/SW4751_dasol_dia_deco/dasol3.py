import sys
sys.stdin = open('dia.txt')

# 김동욱 풀이
t = int(input())

for tc in range(1, t + 1):
    a = input()
    for i in range(5):
        if i == 0 or i == 4:
            print('.', end='')
        elif i == 1 or i == 3:
            print('.', end='')
        else:
            print('#', end='')
        for j in range(len(a)):
            if i == 0 or i == 4:
                print('.#..', end='')
            elif i == 1 or i == 3:
                print('#.#.', end='')
            else:
                print(f'.{a[j]}.#', end='')
        print()