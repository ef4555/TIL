
'''
순열 구하기
순열은 중복된 원소 없이 섞는것
1. 처음 원소를 결정한다 (갈림길 생김)
2. 두번째 원소를 결정한다 (갈림길 생김)
# 자리에 그 다음 원소를 넣어보고(자리 바뀜), 그 다음다음 원소로 넣어보고, 그 다음다음다음 원소로 넣어보고....
# 그 각각에 대해 또 갈림길이 생긴다.
3. i == K가 되면 더이상 자리 바꿔볼 원소가 없는 것이므로 종료

'''

def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k): # 갈림길이 여러개인 경우, 부분집합은 01 두 가지 갈래길밖에 없었지만 순열은 여러개의 갈림길
            p[i], p[j] = p[j], p[i] # p[i] 결정
            # p[i]결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i] # p[i] 복구

p = [1, 2, 3]
N = len(p) # 순열의 길이
f(0, N)

