import sys
sys.stdin = open('input.txt')


for test_case in range(1, int(input()) + 1):
    num, k = input().split()
    k, data, sub = int(k), set([num]), set()
    for _ in range(k):
        print(data)
        while data:
            s = data.pop()
            s = list(s)

 
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    s[i], s[j] = s[j], s[i]
                    print(s)
                    sub.add(''.join(s))
                    s[i], s[j] = s[j], s[i]

        data, sub = sub, data
    print(f'#{test_case} {max(map(int, data))}')
