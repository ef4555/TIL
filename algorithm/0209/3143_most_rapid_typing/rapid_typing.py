'''
어떤 문자열 A를 타이핑하려고 한다.

그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.

여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서
키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.

이미 타이핑 한 문자를 지우는 것은 불가능하다.

예를 들어 A=”asakusa”, B=”sa”일 때, 다음 그림과 같이
B를 두 번 사용하면 5번 만에 A를 타이핑 할 수 있다.
'''


import sys
sys.stdin = open('rapid_typing.txt')

T = int(input())
for tc in range(1, T + 1):
    moon, word = map(str, input().split())
    cnt = 0
    i = 0
    while i <= len(moon) - 1: # while문으로 문장 전체를 탐색해서
        if moon[i] == word[0]: # 첫 글자가 단어의 첫 글자와 일치하면 탐색 시작
            if moon[i:i + len(word)] == word: # 뒤 문자열과 비교 해서 같으면
                cnt += 1 # 카운팅
                i += len(word) # 인덱스 단어 크기만큼 전진
            else:
                i += 1 # 아니면 인덱스 한칸만큼 전진
        else:
            i += 1 # 첫글자와 일치하지도 않으면 그냥 한칸 전진
    tp = len(moon) - cnt * len(word) + cnt # 문장전체글자수에서 카운팅*단어길이를 빼고 카운트만큼 더한다.

    print(f'#{tc} {tp}')



