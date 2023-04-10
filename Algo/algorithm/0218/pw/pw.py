import sys
sys.stdin = open('pw.txt')
# 같은 번호로 붙어있는 쌍을 소거하고 남은 번호를 비밀번호로
# 번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 또 같으면 또 소거
# 스택 이용한 문제
for tc in range(1, 4):
    N, M = input().split()
    # N은 문자열의 길이, M은 문자열
    pw = ''
    stack = []
    for i in range(int(N)):
        if len(stack) == 0:
            stack.append(M[i])
        else:
            if M[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(M[i])

    # print(stack)
    pw = ''.join(stack)

    print(f'#{tc} {pw}')