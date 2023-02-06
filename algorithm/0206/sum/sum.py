'''
[제약 사항]

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
# '''





T = 10
for tt in range(1, T+1):
    count = int(input())
    num_lst = [] # 합들을 저장할 리스트
    big_lst = [[] for i in range(100)] # 배열을 저장할 빈 리스트
    for dd in range(0, 100): 
        lst = list(map(int, input().split())) # 입력되는 값들을 리스트에 저장
        big_lst[dd].extend(lst) # 가로 한줄씩 리스트로 저장된 리스트 (리스트로 된 원소 100개)
    sero = [[] for pp in range(100)] # 세로 원소를 한줄씩 저장할 100개의 원소 자리가 있는 빈 리스트 
    # 가로 합
    for nn in range(0, 100): 
        num_lst.append(sum(big_lst[nn])) # 원소 하나(가로 한 줄)의 합들을 합 리스트에 저장

        for tt in range(0, 100):
            sero[nn].append(big_lst[tt][nn]) # 세로 원소들을 sero 리스트에 한줄씩 원소로 저장
    # 세로 합
    for kk in range(100):
        num_lst.append(sum(sero[kk])) # sero 리스트에 저장된 세로 한줄들의 합을 저장

    # 대각선 합
    dae1 = [0 for i in range(100)] # 대각선 원소들을 저장할 리스트
    dae2 = [0 for i in range(100)]
    for yy in range(100):
        big_lst[yy][yy] = dae1[yy] # 한 칸씩 내려가면서 dae1 리스트에 원소들 저장
    for ii in range(100):
        big_lst[99-ii][ii-1] = dae1[ii] # 맨 아래서부터 한 칸씩 대각선으로 올라가면서 dae2 리스트에 원소들 저장

    num_lst.append(sum(dae1))
    num_lst.append(sum(dae2))
    print(f'#{count} {max(num_lst)}')