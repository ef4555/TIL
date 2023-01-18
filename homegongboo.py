'''
문제
과수원에 농부 한 명이 썩은 과일이 몇 개 들어있는 과일 봉지를 가지고 있다. 과일 봉지를 입력받아, 썩은 과일 조각들을 모두 신선한 것으로 교체하는 코드를 작성하고 리스트 형식으로 출력하시오.
	예를 들어, apple,rottenBanana,apple,RoTTenorange,Orange이라는 문자열이 주어진 경우, 대체된 리스트는 ['apple', 'banana', 'apple', 'orange', 'orange'] 이어야 한다.

유의 사항
n 만약 리스트가 비어 있는 경우 빈 리스트를 반환한다.
n 반환된 리스트의 요소는 모두 소문자여야 한다.
'''

fruits = 'apple,rottenBanana,apple,RoTTenorange,Orange'

fruits_list = fruits.split(',')
small_fruits = []
for i in fruits_list:
    small_fruits.append(i.lower())
print(small_fruits)
for t in small_fruits:
    count = 0
    if t.find('rotten') == -1:
        small_fruits[count] = t
        count += 1
        print(count)
    else:
        p = t[6:]
        print(p)
        small_fruits[count] = p
        count += 1
        print(count)
print(small_fruits)
 