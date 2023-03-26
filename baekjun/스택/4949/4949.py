
while True:
    m = input()
    if m == '.':
        break
    stack = []
    temp = True
    for i in m:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[': # 스택이 비어있거나 (가 아니라 [이면
                temp = False # 짝  안맞음
                break
            elif stack[-1] == '(': # 짝이 맞으므로 스택에서 pop
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(': 
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack: # 스택이 비어있고 짝이 안맞는 경우 없는 경우
        print('yes')
    else:
        print('no')