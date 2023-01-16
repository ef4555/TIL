'''
a = []
b = []
c = a #c에게 a의 주솟값을 준 것.(참조)
'''
'''
print(id(a))
print(id(b))
print(id(c))

result = (a is b)
print(result)
result = (a is c)
print(result) #c는 a와 같은 메모리를 참조하고 있어서 True
result = (b is c)
print(result)
'''

'''if not b : 
    print(('b는 비어있습니다.'))

# 빈 리스트는 False
# 0도 False
'''
'''
list_a = []
list_b = [1,2,3] # 1차원
list_c = list()
            
list_d = [[1,2,3], 'python', ['서울', '대전', '부울경', '구미']] # 리스트 안에 리스트, 2차원 리스트
#2차원 리스트는 리스트 안에 또 인덱스 값이 따로 있다
result = list_d[2][2]
print(result)
'''
'''
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]
print(len(boxes))
print(boxes[2])
print(boxes[2][-1])
print(boxes[-1][1][0]) # str도 인덱스를 가진다.

print(len(boxes[-1][1])) #banana의 문자 길이 
'''
'''
# parameter = 함수에게 전달해주는 값 (input)
print(list(range(1, 10, 2))) 

# 역순
print(list(range(6, 1, -1))) #[6,5,4,3,2]

# 슬라이싱
print([1,2,3,4][0:4:2]) # [1, 3]
print((1,2,3,4,5)[0:4:2]) # (1, 3)
print('abcdefg'[1:4:2])

# 시작 또는 끝나는 부분 생략 가능
a = ['a','b','c','d','e','f']
# a[시작:] => 특정 인덱스부터 끝까지 가져오기
# a[:끝] => 시작부터 특정 위치까지 가져오기

dict_a = {'a' : 'apple'}
# print(dict_a['c']) 에러 발생
result = dict_a.get('c') #매칭되는 키값이 없기 때문에 none을 반환한다.

if not result:
    print("값 없음")
'''
'''
s = '이것은 문자입니다'
print(id(s))
s = '이것은 문자열?'
print(id(s)) # 변수를 바꾸게 되면 참조하는 메모리 주소가 바뀐다

num = 10
print(id(num))
num = 9
print(id(num)) # 숫자도 바뀌게 되면 참조하는 메모리 주소가 바뀐다.
'''
'''
score = {
    'python': 80,
    'django': 89,
    'web': 83
}
score['algorithm'] = 90
score['python'] = 85

average = sum(score.values()) / len(score)
print(average)
'''
print("c:\\python_project\\test")
