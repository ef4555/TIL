# 비트연산으로 부분집합 구하기
## 준비물

```python
arr = ['Fish', 'And', 'Chips']
N = len(arr)
# arr에 대한 모든 경우의 수 
for i in range(1 << N):
    # j 는 arr의 인덱스
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()
```

- 1 << 2의 의미
```python
N = 3
print(1 << N) # 8
# << : 피연산자를 비트열에서 왼쪽으로 이동시킨다. 
```

- for i in range(1 << N)
    - for i in range(8):
    - 3개의 원소를 가지고 우리가 만들 수 있는 모든 경우의 수는 8 (2^3)


- arr = ['Fish', 'And', 'Chips']의 각 요소들을 비트로 나타내보자
    - 1번째, 2번째, 3번째 4번째 요소에 해당한다
    - arr의 index를 경우의 수에 따라 부분집합에 포함시킬것이냐 시키지 않을 것이냐 

|Fish|And|Chips|
|------|---|---|
|001|010|100|

- if i & (1 이해하기
    - 이 구문을 통과하기 위해서는 i값의 오른쪽부터 n번째 비트값이 1이어야한다. 
    - 비트 연산자 & : 비교 대상의 비트 값의 각 자리수를 비교한다
    - 양쪽의 자리수가 모두 True일때 True를 반환한다. 
        - 숫자 3(N)을 받고 i(3)번째 경우의 수 

- 즉 배열 arr = ['Fish', 'And', 'Chips']의 부분집합의 경우의 수 중.
- 3번째 경우는 Fish와 And 두 요소를 조합한 것과 같다. 