'''

두 개의 문자열 str1과 str2가 주어진다.
문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우,
str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.
'''
import sys
sys.stdin = open('str_soo.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = input() # 키값이 될 문자열
    str2 = input() # 조사할 문자열
    dic = {} # 빈 딕셔너리 생성
    for i in str1: # 첫번째 문자열 순회하면서 각 키 value를 0으로 생성
        dic[i] = 0
    for j in str2: # 두번째 문자열 한글자씩 비교
        for k in dic: # 딕셔너리의 키 값과 비교
            if j == k: # 키랑 문자열이랑 같으면
                dic[k] += 1 # 1 추가
    max_d = 0
    for l in dic: # 키 값의 value 중에서 제일 큰 값 찾음
        if max_d < dic[l]:
            max_d = dic[l]
    print(f'#{tc} {max_d}')

