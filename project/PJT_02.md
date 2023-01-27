>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 01

### 이번 pjt 를 통해 배운 내용

* api 키를 발급받는 방법

* api를 이용하여 정보를 불러오는 방법

* 불러온 정보를 request라이브러리를 이용하여 json형태로 저장하는 방법

* param을 저장하여 param에 맞는 정보를 json형태로 저장하는 방법

* param의 형식을 파악하고 url을 작성하여 원하는 정보를 불러오는 방법

* value를 리스트로 갖는 딕셔너리의 정보를 다루는 방법

* json 뷰어를 통해 json 자료의 구조를 파악하는 방법 

* lambda 함수를 통해 딕셔너리의 value 기준으로 딕셔너리를 정렬하는 방법

* 딕셔너리와 리스트가 혼재되어있는 복잡한 형식의 자료형에서 원하는 정보를 추출하는 방법

## A. 인기 영화 조회

* 요구 사항 : 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.

* 결과 : 
```
20
```
  
  * 문제 접근 방법 및 코드 설명
  
```python
import requests
from pprint import pprint

def popular_count():
    popular_URL = 'https://api.themoviedb.org/3/movie/popular?api_key=03d1fc24e2d5bcba04ac921e799b29c1&language=ko-KR&page=1' # 발급받은 api 키로 page = 1, language=ko-KR인 인기있는 영화 목록 데이터를 요청할 수 있는 url을 변수에 저장합니다.
    popular_response = requests.get(popular_URL).json() # popular_URL에서 인기 영화 정보들을 request 라이브러리를 이용하여 json형태로 popular_response 변수에 저장합니다.
    p_results = popular_response['results'] 
    # 딕셔너리 안에 딕셔너리가 담긴 popular_response 딕셔너리에서 'results'를 key로 가진 value들을 p_result에 저장합니다.
    # 이 때, p_result에 저장된 'results'를 key로 가진 value는 리스트 형태입니다.
    
    p_results_count = len(p_results) # 인기 영화 목록인 p_result 리스트의 길이를 p_results_count에 저장합니다.
    return p_results_count # 인기 영화 목록의 개수를 출력합니다.
```
  
  * 이 문제에서 어려웠던점
    - api를 통해 불러온 자료의 구조를 파악하여 원하는 정보를 가진 부분이 어디인지 파악하는 것 
  * 내가 생각하는 이 문제의 포인트
    - 받아온 json형태의 자료의 구조를 파악하는 것이 핵심입니다. json viewer가 도움이 되었습니다. 

-----
## B. 특정 조건에 맞는 인기 영화 조회 1

* 요구 사항 : 인기 영화 목록을 응답 받아 개수를 출력합니다

* 결과 : 
```
[{'adult': False,
  'backdrop_path': '/faXT8V80JRhnArTAeYXz0Eutpv9.jpg',
  'genre_ids': [16, 28, 12, 35, 10751, 14],
  'id': 315162,
  'original_language': 'en',
  'original_title': 'Puss in Boots: The Last Wish',
  'overview': '아홉 개의 목숨 중 단 하나의 목숨만 남은 장화신은 고양이.  마지막 남은 목숨을 지키기 
위해 히어로의 삶 대신 '
              '반려묘의 삶을 선택한 그에게 찾아온 마지막 기회, 바로 소원을 들어주는 소원별이 있는  
곳을 알려주는 지도!  '
              "잃어버린 목숨을 되찾고 다시 히어로가 되기를 꿈꾸는 장화신은 고양이는 뜻밖에 동료가  
된 앙숙 파트너 '키티 "
              "말랑손', 그저 친구들과 함께라면 모든 게 행복한 강아지 '페로'와 함께 소원별을 찾기 위
해 길을 떠난다.  "
              '그리고 소원별을 노리는 또 다른 빌런들과 마주치게 되는데…',
  'popularity': 5946.788,
  'poster_path': '/rKgvctIuPXyuqOzCQ16VGdnHxKx.jpg',
  'release_date': '2023-01-04',
  'title': '장화신은 고양이: 끝내주는 모험',
  'video': False,
  'vote_average': 8.6,
  'vote_count': 2658},
 {'adult': False,
  'backdrop_path': '/e782pDRAlu4BG0ahd777n8zfPzZ.jpg',
  'genre_ids': [16, 14, 18],
  'id': 555604,
  'original_language': 'en',
  'original_title': "Guillermo del Toro's Pinocchio",
  'overview': '많은 이들의 사랑을 받은 목각 인형 피노키오의 마법 같은 모험. 현실의 한계를 뛰어넘어, 새 생명을 불어넣는 '
              '강력한 사랑의 힘이 펼쳐진다. 이탈리아 고전 동화 "피노키오"가 스톱모션 뮤지컬로 재탄 
생한다. 말썽꾸러기 '
              '피노키오는 과연 인간 소년이 될 수 있을까? 그 여정을 따라가 보자.',
  'popularity': 713.806,
  'poster_path': '/6bdUtxydFXLtgcxHMMvlkNnRZWg.jpg',
  'release_date': '2022-11-23',
  'title': '기예르모 델토로의 피노키오',
  'video': False,
  'vote_average': 8.4,
  'vote_count': 1675}]
```
  
  * 문제 접근 방법 및 코드 설명
  
```python
import requests
from pprint import pprint

def vote_average_movies():
    over8_list = [] # 평점이 8점 이상인 영화 정보를 담을 리스트를 생성합니다.
    popular_URL = 'https://api.themoviedb.org/3/movie/popular' # 인기 영화 정보를 불러오는 url을 popular_URL 변수에 저장합니다. 
    # 주소창 뒤에 묶이는 키 밸류들을 params1에 저장합니다.
    params = {
    'api_key': '03d1fc24e2d5bcba04ac921e799b29c1', # 정보를 불러올 때 사용하는 api키 값
    'language': 'ko-KR', # 언어 한국어
    'region': 'KR' # 지역 한국으로 설정
}
    popular_response = requests.get(popular_URL, params = params).json() # popular_URL에서 param1 조건에 맞는 인기 영화 정보들을 request 라이브러리를 이용하여 json형태로 popular_response 변수에 저장합니다.
    p_results = popular_response['results']
    # 딕셔너리 안에 딕셔너리가 담긴 popular_response 딕셔너리에서 'results'를 key로 가진 value들을 p_result에 저장합니다.
    # 이 때, p_result에 저장된 'results'를 key로 가진 value는 리스트 형태입니다.

    for i in p_results: # p_results 리스트의 원소들을 순회하면서
      if i.get('vote_average') > 8.0: # 'vote_average'이 8점 이상인 영화가 있으면
        over8_list.append(i) # 'vote_average' 8점 이상인 영화 정보들을 over8_list 리스트에 저장합니다. 
    return over8_list # 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다. 
      
```
  
  * 이 문제에서 어려웠던점
    - api에서 정보를 불러올 때 api url의 형식을 파악하는것 
  * 내가 생각하는 이 문제의 포인트
    - 받아온 json형태의 자료의 구조를 파악하여 원하는 정보를 불러오고 그 정보를 조건에 맞추어 가공하는 것이 핵심입니다.

-----
## C. 특정 조건에 맞는 인기 영화 조회 2

* 요구 사항 : 인기 영화 목록을 평점이 높은 순으로 5개 영화 데이터 목록 출력합니다.

* 결과 : 
```
[{'adult': False,
  'backdrop_path': '/faXT8V80JRhnArTAeYXz0Eutpv9.jpg',
  'genre_ids': [16, 28, 12, 35, 10751, 14],
  'id': 315162,
  'original_language': 'en',
  'original_title': 'Puss in Boots: The Last Wish',
  'overview': '아홉 개의 목숨 중 단 하나의 목숨만 남은 장화신은 고양이.  마지막 남은 목숨을 지키기 
위해 히어로의 삶 대신 '
              '반려묘의 삶을 선택한 그에게 찾아온 마지막 기회, 바로 소원을 들어주는 소원별이 있는  
곳을 알려주는 지도!  '
              "잃어버린 목숨을 되찾고 다시 히어로가 되기를 꿈꾸는 장화신은 고양이는 뜻밖에 동료가  
된 앙숙 파트너 '키티 "
              "말랑손', 그저 친구들과 함께라면 모든 게 행복한 강아지 '페로'와 함께 소원별을 찾기 위
해 길을 떠난다.  "
              '그리고 소원별을 노리는 또 다른 빌런들과 마주치게 되는데…',
  'popularity': 5946.788,
  'poster_path': '/rKgvctIuPXyuqOzCQ16VGdnHxKx.jpg',
  'release_date': '2023-01-04',
  'title': '장화신은 고양이: 끝내주는 모험',
  'video': False,
  'vote_average': 8.6,
  'vote_count': 2658},
 {'adult': False,
  'backdrop_path': '/e782pDRAlu4BG0ahd777n8zfPzZ.jpg',
  'genre_ids': [16, 14, 18],
  'id': 555604,
  'original_language': 'en',
  'original_title': "Guillermo del Toro's Pinocchio",
  'overview': '많은 이들의 사랑을 받은 목각 인형 피노키오의 마법 같은 모험. 현실의 한계를 뛰어넘어, 새 생명을 불어넣는 '
              '강력한 사랑의 힘이 펼쳐진다. 이탈리아 고전 동화 "피노키오"가 스톱모션 뮤지컬로 재탄 
생한다. 말썽꾸러기 '
              '피노키오는 과연 인간 소년이 될 수 있을까? 그 여정을 따라가 보자.',
  'popularity': 713.806,
  'poster_path': '/6bdUtxydFXLtgcxHMMvlkNnRZWg.jpg',
  'release_date': '2022-11-23',
  'title': '기예르모 델토로의 피노키오',
  'video': False,
  'vote_average': 8.4,
  'vote_count': 1675},

이하 생략
```
  
  * 문제 접근 방법 및 코드 설명
  
```python
import requests
from pprint import pprint


def ranking():
    popular_URL = 'https://api.themoviedb.org/3/movie/popular' # 인기 영화 정보를 불러오는 url을 popular_URL 변수에 저장합니다. 
    p_sorted_list = [] # 영화 정보를 평점 내림차순으로 정리하여 저장할 리스트 생성
    # 주소창 뒤에 묶이는 키 밸류들을 params1에 저장합니다.
    params = {
    'api_key': '03d1fc24e2d5bcba04ac921e799b29c1', # 정보를 불러올 때 사용하는 api키 값
    'language': 'ko-KR', # 언어 한국어
    'region': 'KR' # 지역 한국으로 설정
}
    popular_response = requests.get(popular_URL, params = params).json() # popular_URL에서 param1 조건에 맞는 인기 영화 정보들을 request 라이브러리를 이용하여 json형태로 popular_response 변수에 저장합니다.
    p_results = popular_response['results'] 
    # 딕셔너리 안에 딕셔너리가 담긴 popular_response 딕셔너리에서 'results'를 key로 가진 value들을 p_result에 저장합니다.
    # 이 때, p_result에 저장된 'results'를 key로 가진 value는 리스트 형태입니다.

    p_sorted = sorted(p_results, key = lambda x : x['vote_average'], reverse =True) # p_sorted 변수에 p_results리스트에 담긴 영화 정보들을 평점 내림차순으로 정리하여 저장합니다
    # 람다 함수를 이용, 정렬의 key를 'vote_average'로 하고, reverse =True로 하여 내림차순으로 정리합니다. 
    for v in range(0, 5):
        p_sorted_list.append(p_sorted[v]) # p_sorted 리스트의 첫번째 부터 5번째 영화 정보를 p_sorted_list 리스트에 저장합니다.
    return p_sorted_list # 인기 영화 정보를 평점이 높은 순으로 5개 담은 리스트를 반환합니다. 



```
  
  * 이 문제에서 어려웠던점
    - 불러온 정보가 딕셔너리 형태로 되어있는데 이 딕셔너리를 value 기준으로 내림차순으로 정렬하여 5개를 추출하는 것
  * 내가 생각하는 이 문제의 포인트
    - 람다식과 sorted함수를 이용하여 정렬의 조건을 평점으로 설정하고 내림차순으로 정럴하는 방법을 아는것이 이 문제의 핵심입니다. 
-----
## D. 특정 추천 영화 조회

* 요구 사항 : 제공된 영화 제목('기생충', '그래비티', '검색할 수 없는 영화') 을 검색하여 추천 영화 목록을 출력합니다

* 결과 : 
```
['그린 북',
 'Awdat Al-Rouh',
 '조커',
 '원스 어폰 어 타임 인… 할리우드',
 '1917',
 '조조 래빗',
 'My Chemical Romance: AOL Sessions',
 'Back Home',
 '결혼 이야기',
 '나이브스 아웃',
 '대부',
 '아이리시맨',
 '센과 치히로의 행방불명',
 'The Wrestling Classic',
 'Shanghai Fever',
 '포드 V 페라리',
 '너의 이름은',
 '쇼생크 탈출',
 'Is Sumiyati Going to Hell?',
 '작은 아씨들',
 '펄프 픽션']
[]
None
```
  
  * 문제 접근 방법 및 코드 설명
  
```python
import requests
from pprint import pprint


def recommendation(title):
    search_URL = 'https://api.themoviedb.org/3/search/movie' # 영화 정보를 불러올 수 있는 url을 search_URL에 저장

    reco_movies_title = [] # 추천 영화 제목을 담을 reco_movies_title 리스트를 생성합니다.
    # 주소창 뒤에 묶이는 키 밸류들을 params1에 저장합니다.
    params1 = { 
    'api_key': '03d1fc24e2d5bcba04ac921e799b29c1',
    'language': 'ko-KR',
    'region': 'KR',
    'query': title # 입력받은 title으로 검색
    }
    search_response = requests.get(search_URL, params = params1).json()  # search_response 변수에 검색한 정보를 저장 
    search_results = search_response['results']
    # search_response에서 'results'를 key로 가진 value들을 p_result에 저장합니다.
    # 이 때, p_result에 저장된 'results'를 key로 가진 value는 리스트 형태입니다.

    if search_results == []: # search_results가 빈 리스트이면 None을 출력합니다.
        return None

    m_first_id = search_results[0]['id'] # m_first_id 변수에 응답받은 결과 중 첫번째 영화의 'id'값을 저장합니다.
    reco_m_URL = f'https://api.themoviedb.org/3/movie/{m_first_id}/recommendations' # reco_m_URL에 m_first_id에 해당한ㄴ 추천 영화를 불러올 수 있는 url을 저장 
    params2 = {
    'api_key': '03d1fc24e2d5bcba04ac921e799b29c1',
    'language': 'ko-KR'
    }

    reco_response = requests.get(reco_m_URL, params = params2).json() # reco_response에 불러온 결과 json형식으로 저장
    reco_results = reco_response['results'] # 추천 영화들의 정보를 reco_results 에 저장

    for i in reco_results: # reco_results를 순회하며
        reco_movies_title.append(i['title']) # reco_movies_title 리스트에 추천 영화 제목을 저장 
    return reco_movies_title # 추천 영화 목록 반환 

```
  
  * 이 문제에서 어려웠던점
    - 불러온 값이 비었을 경우 따로 return 값을 None으로 출력하는것
    - 불러온 id 정보 값을 저장하여 다시 api를 요청하여 그 id값에 해당하는 추천 영화 정보를 불러오는것
  * 내가 생각하는 이 문제의 포인트
    - 받아온 정보를 param으로 이용하여 다시 정보를 불러오는 것이 이 문제의 핵심입니다. 

-----

## E. 출연진, 연출진 데이터 조회 

* 요구 사항 : 제공된 영화 제목('기생충', '검색할 수 없는 영화')을 검색하여 해당 영화의 출연진과 스태프 중 연출진의 이름 출력합니다

* 결과 : 
```
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Jang Hye-jin'],
 'crew': ['Bong Joon-ho',
          'Park Hyun-cheol',
          'Han Jin-won',
          'Kim Seong-sik',
          'Lee Jung-hoon',
          'Yoon Young-woo']}
None
```
  
  * 문제 접근 방법 및 코드 설명
  
```python
import requests
from pprint import pprint


def credits(title): # 제공된 영화 제목을 검색하여 해당 영화의 cast와 crew 이름을 반환하는 함수
    cast_crew_dict = {'cast': [], 'crew': []}  # 해당 영화의 cast와 crew 이름을 저장하는 함수
    search_URL = 'https://api.themoviedb.org/3/search/movie' # 영화 정보를 불러올 수 있는 url을 search_URL에 저장
    # 주소창 뒤에 묶이는 키 밸류들을 params1에 저장합니다.
    params1 = {
    'api_key': '03d1fc24e2d5bcba04ac921e799b29c1',
    'language': 'ko-KR',
    'region': 'KR',
    'query': title  # 입력받은 title으로 검색
    }

    search_response = requests.get(search_URL, params = params1).json() # search_response 변수에 검색한 정보를 저장 
    search_results = search_response['results']
    # search_response에서 'results'를 key로 가진 value들을 p_result에 저장합니다.
    # 이 때, p_result에 저장된 'results'를 key로 가진 value는 리스트 형태입니다.

    if search_results == []: # search_results가 빈 리스트이면 None을 출력합니다.
        return None

    m_first_id = search_results[0]['id']# m_first_id 변수에 응답받은 결과 중 첫번째 영화의 'id'값을 저장합니다.
    credits_URL = f'https://api.themoviedb.org/3/movie/{m_first_id}/credits' # credits_url에 m_first_id에 해당하는 영화의 cast와 crew 정보들을 불러올 수 있는 url을 저장 
    params3 = {
    'api_key': '03d1fc24e2d5bcba04ac921e799b29c1',
    'language': 'ko-KR',
    }
    credit_response = requests.get(credits_URL, params = params3).json() #  credit_response에 param3 조건에 맞는 정보 불러온 결과를 json형식으로 저장
    for cast in credit_response['cast']: # credit_response 딕셔너리의 'cast'값을 key로 가지는 리스트를 순회하며 
        if cast['cast_id'] < 10: # cast_id값이 10 미만이면
            cast_crew_dict['cast'].append(cast['name']) # cast_crew_dict 딕셔너리의 'cast' key에 cast 이름을 저장 
    for crew in credit_response['crew']: # credit_response 딕셔너리의 'crew'값을 key로 가지는 리스트를 순회하며
        if crew['department'] == 'Directing': # crew의 department가 Directing이면 
            cast_crew_dict['crew'].append(crew['name']) # cast_crew_dict 딕셔너리의 'crew' key에 crew 이름을 저장 

    return cast_crew_dict # cast와 crew 이름을 반환

```
  
  * 이 문제에서 어려웠던점
    - value값이 리스트로 되어있는 딕셔너리를 만들어 그 value 리스트에 값들을 추가하는것
    - 불러온 정보의 형태를 파악하는 것 
  * 내가 생각하는 이 문제의 포인트
    - 딕셔너리 형태의 받아온 정보를 조건문으로 원하는 정보만 걸러낸 다음 딕셔너리 값에 추가하는것이 이 문제의 핵심입니다. 

-----

# 후기

* 저번주에는 각 문제간 연관성을 찾지 못하고 헤메었습니다. 이번주에는 앞선 문제를 바탕으로 기능을 더하면서 구현한다는 생각으로 하니 문제를 어렵지 않게 해결할 수 있었습니다.
* api를 이용해 원하는 정보를 이렇게 빠르게 불러올 수 있다는 것이 놀라웠습니다.
* api 키를 받는 과정부터 정보를 받아올 때 url 양식이 낮설었습니다. 어떻게 이렇게 호출하면 정보를 불러올 수 있는지 그 메커니즘이 궁금합니다.
* 실제 쓸모있는 결과가 나오는 코드를 짜니 재미있었습니다.
* 정보들의 이름과 인덱스 위치를 정확히 파악하는것이 헷갈렸습니다.
