'''
후위 표기법

3
2+3*4/5
(6+5*(2-8)/2)
3-2*5+4/2-2


#1 234*5/+
#2 6528-*2/+
#3 325*-42/+2-
'''

import sys
sys.stdin = open('practice1.txt')
T = int(input())
for tc in range(1, T+1):
    # 코드로 구현
    infix = input()
    stack = []
    result = ''
    # 변환할 식을 순회
    for token in infix:
        # 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token

        # 토큰이 연산자인 경우
        else:
            # stack이 비어있는 경우, stack에 push
            if not stack:  # if len(stack) == 0
                stack.append(token)


            # 스택이 비어있지 않은 경우
            else:
                # (는 incoming 우선순위가 가장 높음.
                if token == '(':
                    stack.append(token)
                # )는 (가 나올때까지 stack에서 pop, result에 append
                elif token == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
                # incoming 우선순위가 2인 경우
                elif token == '*' or token == '/':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    while stack and stack[-1] in '*/':
                        result += stack.pop()
                    stack.append(token)

                # incoming 우선순위가 1인 경우
                elif token == '+' or token == '-':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    # (가 아닌 경우 모두 동치
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()




    print(f'#{tc} {result}')

