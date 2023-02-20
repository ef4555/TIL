import sys
sys.stdin = open('ro.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N은 회전할 수열의 길이, M은 이동 횟수
    lst = list(map(int, input().split()))
    # print(lst)
    for i in range(M): # 선형 큐의 크기 할당, M번의 이동이 있으므로 자리 M개 만들어줌
        lst.append(0)
    # print(lst)
    front = 0
    rear = N-1
    for j in range(M): # M번 회전하면서
        lst[rear+1] = lst[front] # front에 해당하는 원소를 rear+1 위치에 보내고
        front += 1 # front + 1
        rear += 1 # rear + 1
    print(f'#{tc} {lst[-N]}') # 맨 첫번째 숫자 출력
