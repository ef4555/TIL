import sys
sys.stdin = open('dia.txt')
# 조재웅님 풀이
T = int(input())
for test_case in range(1, 1 + T):
    answer = [str()] * 5
    print(answer)
    string = input()
    print(string)
    for c in string:
        answer[0] += '..#.'
        answer[1] += '.#.#'
        answer[2] += f'#.{c}.'
        answer[3] += '.#.#'
        answer[4] += '..#.'

    answer[0] += '.'
    answer[1] += '.'
    answer[2] += '#'
    answer[3] += '.'
    answer[4] += '.'

    for row in answer:
        print(row)