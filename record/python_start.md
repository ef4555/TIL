# 파이썬 기초 문법

## 변수와 식별자
### 변수
dust = 60 : 오른쪽에 있는 값을 왼쪽에 할당한다
"=" 할당 연산자
컴퓨터는 어떻게 저장하고 이름을 지을까? 

- 변수란?
    - 데이터를 저장하기 위해 사용
    - 변수를 사용하면 복잡한 값들을 쉽게 사용할 수 있음(추상화)
- 동일 변수에 다른 데이터를 언제든 할당(저장)할 수 있기에 변수라고 불린다.

- 변수는 할당 연산자를 통해 값을 할당
- 같은 값을 동시에 할당 가능
- 다른 값을 동시에 할당할 수 있음


변수 할당 실습

1. 임시 변수 활용
```
x, y = 10, 20

tmp = x #tmp에 x 값 주고
x = y #y한테 y값 받고
y = tmp #tmp에서 값 받고

print(x, y)
```
2. Pythonic
```
x, y = 10, 20
y, x = x, y
print(x, y)
```
### 식별자
변수의 이름을 식별자라고 한다(변수, 함수, 클래스)
문제는 그 변수의 이름을 어떻게 지어야 하는지
읽기 쉽고 이해하기 쉬운 변수명이 최고

- 변수 이름 규칙
    1. 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    2. 첫 글자에 숫자 올 수 없다
    3. 길이 제한이 없고 대소문자를 구별
    4. 예약어로 사용할 수 없는 키워드 존재
    5. 내장 함수나 모듈 등의 이름도 사용하지 않아야 한다. : 동작을 예상할 수 없게 임의로 값을 할당하게 되므로 범용적이지 않은 코드가 된다.

### 주석

- 코드의 실행에 영향을 미치지 않는 나만의 메모
    1. 코드에 대해 쉬운 이해
    2. 유지보구 용이
    3. 협업 용이

기억력을 믿지 말고 주석을 달자

## 연산자

/ : 나눗셈
// : 몫 연산자, 몫 값을 내놓는다.
** : 거듭제곱
% : 나머지를 내놓는다.

연산자 우선순위는 사칙연산하고 동일

## 자료형
자료형이 왜 필요한가?

데이터 10을 컴퓨터가 기억하는 과정
1. 10을 저장할 공간을 메모리에 만들고
2. 저장할 공간에 대한 주소를 할당받는다
3. 할당받은 주소를 기억했다가
4. 10이라는 데이터를 해당 주소로 찾아가서 저장한다
5. 이후에 10이 필요해지만 해당 주소로 가서 읽어온다. 

변수는 주소값에 대한 별명이다.
우리는 변수를 이용해서 데이터를 기억한다
자료형마다 차지하는 메모리의 크기가 다르다.

### 자료형 분류

- 정수 자료형(int)
    - 정수를 표현, 여러 진수 표현 가능

- 실수 자료형(float)
    - 유리수와 무리수를 포함하는 실수를 다루는 자료형
    - 정수를 이진수로 변환하는건 쉽다, 하지만 소수라면? : 실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있다. 컴퓨터는 2진수를 사용하지만 사람은 10진수를 사용한다. 무한대 숫자를 그대로 저장할 수 없어서 근사값으로 표시하게 되기에 이런 현상 생긴다. 따라서 값 비교 과정에서 정수가 아니면 주의해야한다. math 모듈 활용하거나 매우 작은수보다 작은지 확인

- 문자열 자료형
    - 문자열은 작은따옴표나 큰따옴표를 활용하여 표기
    - 문자열을 묶을 때 동일한 문장부호를 활용
    - 중첩 따옴표
        - 따옴표 안에 따옴표를 표현할 경우
            - 작은 따옴표가 들어 있는 경우는 큰 따옴표로 문자열 생성
    - 삼중 따옴표(Triple Quotes)
        - 작은따옴표나 큰따옴표를 삼중으로 사용
            1. 따옴표 안에 따옴표를 넣을때
            2. 여러 줄을 나눠 입력할 때 편리

    - Escape sequence
        - 특정 문자가 어떤 기능을 하게 하는것
            - 역슬래시 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합(제어 시퀸스)
        - \n : 줄바꿈
        - \t : 탭
        - \r : 캐리지 리턴 : 깜빡깜빡 하는 커서를 맨 앞으로 가게 하는것
        - \0 : 널
        - \\ : 문자열 안에 역슬래시를 넣고 싶을때
        - \' : 단일 인용 부호
        - \" : 이중인용부호
    - 문자열 연산
        - 문자열끼리 더하면 파이썬에서 문자열 덧셈은 문자열을 연결
        - 문자열 곱셉도 가능, 문자열이 여러번 나옴
    - 문자열을 변수를 활용하여 만드는법
        ``` 
        name = "kim" 
        score = 4.5 
        print(f'Hello, {name}! 성적은{Score}')
        ```
## 코드 스타일 가이드

## 프로그램 구성 s