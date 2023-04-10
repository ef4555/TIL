import sys
sys.stdin = open('GNS_test_input.txt')
T = int(input())
elien = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    t, N = input().split()
    papago = []
    lst = list(input().split()) # 받은 외계 문자 리스트로 저장
    for i in lst: # 카운팅 정렬 사용하여 작은 수가 앞에 오도록 정렬
        papago.append(elien.index(i))

    papago_c = [0]* (int(N)+1) # 원소별로 카운트 할 리스트
    papago_b = [0]*int(N) # 정렬된 수들을 넣을 리스트
    elien_sort = [0] * int(N)

    for i in range(0, int(N)):
        papago_c[papago[i]] += 1 # 원소별로 카운트

    for i in range(1, len(papago_c)): # 카운트 누적하는 반복문
        papago_c[i] += papago_c[i-1]

    for i in range(int(N)-1, -1, -1):
        papago_c[papago[i]] -= 1 # 누적한 카운트 리스트에서 에서 하나하나 빼면서
        papago_b[papago_c[papago[i]]] = papago[i] # 정렬할 수들을 저장하는 리스트에 뒤에서부터 넣어줌
    for y in range(int(N)):
        elien_sort[y] = elien[papago_b[y]]

    print(f'#{tc}')
    print(*elien_sort)


'''
# 버블 정렬로 정렬
    for i in range(int(N) - 1, 0, -1):
        for j in range(0, i):  # 처음부터 i까지
            if papago[j] > papago[j + 1]:  # 옆에게 크면 자리 바꿈
                papago[j], papago[j + 1] = papago[j + 1], papago[j]
'''
