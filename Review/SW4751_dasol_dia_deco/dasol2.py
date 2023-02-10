import sys
sys.stdin = open('dia.txt')
# 이현도 풀이
T = int(input())
for test_case in range(T):
    words = input()
    N = len(words)
    lining0 = lambda n: '..' + (lambda n:('...').join('#'*n) )(n) +'..'
    lining1 = lambda n: '.' + (lambda n:('.').join('##'*n) )(n) +'.'
    wordline = '#.' + '.#.'.join(words) + '.#'
    print(f'{lining0(N)}\n{lining1(N)}\n{(wordline)}\n{lining1(N)}\n{lining0(N)}')
