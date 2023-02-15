'''
피연산자는 바로 출력하고
연산자는 스택에 push하여
수식이 끝나면 스택에 남아있는 연산자를 모두 pop하여 출력하시오
연산자는 사칙연산만 사용

3
2+3*4/5
1*2/3+2
3-2*5+4/2-2

#1 2345/*+
#2 1232+/*
#3 325422-/+*
'''
import sys
sys.stdin = open('practice1.txt')
T = int(input())
for tc in range(1, T+1):
    # 코드로 구현
    infix = input()
    stack = []
    result = ''
    for token in infix:
        # 토큰이 피연산자인 경우
        if token.isdecimal(): # 피연산자인지 확인 후
            print(token, end = '') # 바로 출력
        else:
            stack.append(token) # 연산자이면 스택에 추가
    N = len(stack) # 스택의 길이 저장
    for _ in range(N): # 스택의 길이만큼
        print(stack.pop(), end='') # 스택에서 pop
    print()