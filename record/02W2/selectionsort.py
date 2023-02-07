'''
7
7, 2, 5, 3, 4, 6, 4
'''


N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1): # 작업 구간의 시작 인덱스
    minIdx = i # 맨 앞의 원소가 최소라 가정, 이 값은 인덱스 비교에 쓰임
    # 한바퀴 끝나면 맨 앞값이 최소가 되고 그 다음 자리부터 다시 또 정렬(i가 N-1까지 증가, N-1까지 가면 그 다음은 그대로이거나 한번만 바꾸면 되니까 N-1까지)
    for j in range(i+1, N): # 그 앞자리 부터 N까지 인덱스로 탐색
        if arr[minIdx] > arr[j]: # 보다 작은 수 발견하면 
            minIdx = j # 최솟값의 인덱스 변경
    arr[minIdx], arr[i] = arr[i], arr[minIdx] # 최솟값의 인덱스 찾았으므로 그 인덱스 이용해서 최솟값 위치 바꾼다. 
print(arr)

