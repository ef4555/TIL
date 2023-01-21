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

* 데이터 파일을 불러와서 파이썬으로 처리하여 출력하는 방법을 배웠습니다. 

* 여러 데이터 파일을 불러와서 필요한 정보를 비교하는 방법을 배웠습니다.

* 딕셔너리에 새로운 키와 밸류를 추가하는 법을 배웠습니다. 

* get함수를 이용해서 원하는 키 값의 value값을 불러내는 방법을 배웠습니다

* 리스트 안에 딕셔너리가 들었을때 정보를 탐색하여 조건문에 적용하는 방법을 배웠습니다

* 새롭게 딕셔너리를 만들어서 리스트 안에 넣고 그 리스트에서 원하는 키 값의 value값을 불러내는 방법을 배웠습니다.

* 리스트 안에 든 딕셔너리의 정보를 변경하는 방법을 배웠습니다. 

* 딕셔너리 안에 든 키를 제거하는 del 명령어를 배웠습니다. 

* sorted와 sort를 이용해서 리스트의 값을 정렬하는 법을 배웠습니다.

* for문을 중첩해서 사용하는 법을 배웠습니다. 

## A. 제공되는 영화 데이터의 주요내용 수집

* 요구 사항 : 영화 데이터에서 필요한 정보만 추출하여 반환하는 함수를 만든다

* 결과 :
```
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는
 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지 
옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못
한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일
하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불
려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
 ```
  * 문제 접근 방법 및 코드 설명
  
  ```python
  def movie_info(movie):  
    result ={
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'), # 해당 key가 있으면 해당 value를 반환, 없으면 none을 반환
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    } 
  ```
  
  * 이 문제에서 어려웠던점
    - 데이터를 다른 파일에서 불러오는 부분이 생소했고, get함수를 처음 써 보아서 어떻게 적용하는지 알아보는 것이 어려웠습니다. 
  * 내가 생각하는 이 문제의 포인트
    - 파일을 불러와서 원하는 데이터만 추출하는 것이 바로 포인트인 것 같습니다.

-----
## B. 제공되는 영화 데이터의 주요내용 수정

* 요구 사항 : 이전 단계에서 만들었던 데이터 중 genre_ids를 장르 번호가 아닌 장르 이름 리스트
genre_names로 바꿔 반환하는 함수를 완성합니다.

* 결과 : 
```
{'genre_names': ['Crime', 'Drama'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는
 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지 
옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못
한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일
하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불
려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
 ```
  
  * 문제 접근 방법 및 코드 설명
  
  ```python
  def movie_info(movie, genres):
    result ={
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'), # 해당 key가 있으면 해당 value를 반환, 없으면 none을 반환
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids'),
        'genre_names' : [] # 빈 'genre_names' 키 생성
    }
    for i in range(len(genres)): # 장르 리스트의 길이만큼 반복
        for gl in result['genre_ids']:
            if gl == list(genres[i].values())[0]: # 장르 리스트 안의 딕셔너리 순회하며, 만약 장르 리스트 안의 딕셔너리 중 id 값이 result 딕셔너리의 'genre_ids' 리스트의 첫번째 값 일치하는게 있으면
                result['genre_names'].append(list(genres[i].values())[1]) # 그 일치하는 id값이 들어있는 딕셔너리의 장르를 result 리스트에 있는 'genre_ids'키의 리스트에 추가
    del result['genre_ids'] # result 딕셔너리에서 'genre_ids' 키 제거
    return result   
  ```
  
  * 이 문제에서 어려웠던점
    - 장르 리스트를 불러와서 장르 리스트 안에 딕셔너리를 순회하면서 비교하는 것이 어려웠습니다. 처음에는 genre_idx값이 모든 영화가 다 2개인줄 알았는데 영화마다 갯수가 달라서 이중으로 for문을 쓰면서 반복을 하도록 코드를 짰습니다. 처음으로 for문을 이중으로 짜는 것이 머릿속으로 잘 구상이 가지 않아서 종이에 적어가면서 짰습니다. 
    - 리스트 안에 든 딕셔너리 값에서 필요한 정보를 추출하는 것이 헷갈렸습니다.
  * 내가 생각하는 이 문제의 포인트
    - 리스트 안에 든 딕셔너리에서 값을 추출하는것
    - 이중으로 반복문을 구성하는것
    - 길이가 정해지지 않은 리스트를 순회하는것

## C. 다중 데이터 분석 및 수정

* 요구 사항 : movies.json에는 평점이 높은 20개의 영화 데이터가 주어집니다.
이 중 서비스 구성에 필요한 정보만 추출해 반환하는 함수를 완성합니다.
완성된 함수는 향후 커뮤니티 서비스에서 제공되는 영화 목록을 제공하기 위한 기능
으로 사용됩니다.

* 결과 :
```
[{'genre_names': ['Crime', 'Drama'],
  'id': 278,
  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다 
는 누명을 쓴다. 주변의 증언과 살해 현장의 '
              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지
옥같은 교도소 쇼생크로 향한다. 인간 말종 '
              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다  
못한 취급을 당한다. 그러던 어느 날, 간수의 '
              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로  
일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여  
불려주면서 그의 돈을 관리하는데...',
  'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
  'title': '쇼생크 탈출',
  'vote_average': 8.7},
 {'genre_names': ['Crime', 'Drama'],
  'id': 238,
  'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 
돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '
              '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오 
네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '
              '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로  
하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '
              '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 
동원해 다른 패밀리들과 피를 부르는 전쟁을 '
              '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지
내왔던 막내 아들 마이클은 아버지가 총격을 '
              '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.',   
  'poster_path': '/cOwVs8eYA4G9ZQs7hIRSoiZr46Q.jpg',
  'title': '대부',
  'vote_average': 8.7},

  이하 생략...
  ```
  
  * 문제 접근 방법 및 코드 설명
  
  ```python
  def movie_info(movies, genres):
    m_list = [] # 영화의 정보들을 담은 딕셔너리를 요소로 저장하는 리스트 m_list를 만듦
    for m in movies:
        result ={
        'id' : m.get('id'),
        'title' : m.get('title'),
        'poster_path' : m.get('poster_path'), # 해당 key가 있으면 해당 value를 반환, 없으면 none을 반환
        'vote_average' : m.get('vote_average'),
        'overview' : m.get('overview'),
        'genre_ids' : m.get('genre_ids'),
        'genre_names' : [] # 빈 'genre_names' 키 생성
    }
        for i in range(len(genres)): # 장르 idx값을 장르 종류로 바꿔주기 위해 우선 장르 리스트의 길이만큼 반복
            for gl in result['genre_ids']: 
                if gl == list(genres[i].values())[0]: # 장르 리스트 안의 딕셔너리 순회하며, 만약 장르 리스트 안의 딕셔너리 중 id 값이 gl 딕셔너리의 'genre_ids' 리스트의 첫번째 값 일치하는게 있으면
                    result['genre_names'].append(list(genres[i].values())[1]) # 그 일치하는 id값이 들어있는 딕셔너리의 장르를 gl 딕셔너리에 있는 'genre_ids'키의 리스트에 추가
        m_list.append(result) # m_list 에 result 값 추가
        del result['genre_ids'] # result 딕셔너리에서 'genre_ids' 키 제거
    return m_list   
  ```
  
  * 이 문제에서 어려웠던점
    - 영화가 여러개가 든 파일에서 정보를 반복적으로 읽어와서 그 값을 반복적으로 바꿔주는 것이 어려웠습니다.
    - B번을 반복해야하는 것은 파악을 빨리 했지만 그 방법을 어떻게 할지 고민을 많이 했습니다
    - 반복문이 어디서 시작해서 어디서 끝나는지 헷갈렸습니다.  
  * 내가 생각하는 이 문제의 포인트
    - 파일을 반복적으로 불러와서 원하는 정보를 읽고 그 정보를 바꾼다음에 저장하는 방법을 배우는 것 
    - 리스트 안에 딕셔너리를 저장하는 것

## D. 알고리즘을 사용한 데이터 출력

* 요구 사항 : 영화 세부 정보 중 수입 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을
낸 영화를 출력하는 알고리즘을 작성합니다. 해당 과정은 향후 커뮤니티 서비스에서
수익순으로 영화를 정렬하여 출력하는 정보로 사용됩니다

* 결과 :
```
반지의 제왕: 왕의 귀환
```
  
  * 문제 접근 방법 및 코드 설명
  
  ```python
  def max_revenue(movies):
    m_list = [] # 영화의 정보들을 담은 딕셔너리를 요소로 저장하는 리스트 m_list를 만듦
    for m in movies:
        result ={
        'id' : m.get('id'),
        'title' : m.get('title'),
        'poster_path' : m.get('poster_path'), # 해당 key가 있으면 해당 value를 반환, 없으면 none을 반환
        'vote_average' : m.get('vote_average'),
        'overview' : m.get('overview'),
        'genre_ids' : m.get('genre_ids'),
    }
        m_list.append(result) # m_list 에 result 값 추가
    re_list = [] # 영화에 수익을 key값으로 가지고 타이틀을 value값으로 가지는 딕셔너리들을 저장하는 리스트 re_list
    revenue = [] # 영화의 수익들(key)값을 저장하는 revenue 리스트 
    for movie_dict in m_list: # m_list에서 각 영화 정보 담긴 딕셔너리 추출
        re_dict = {}
        movie_dict_id = movie_dict.get('id') # Movie_dict_id에 각 영화 정보 딕셔너리에 담긴 id value를 저장 
        movies_file = open(f'data/movies/{movie_dict_id}.json', encoding='utf-8')  # movie_dict_id에 해당하는 영화 상세정보 파일 불러오기
        movies_list_file = json.load(movies_file) # movies_list_file에 저장
        re_dict[movies_list_file['revenue']] = movies_list_file['title'] # 영화에 수익을 key값으로 가지고 타이틀을 value값으로 가지는 딕셔너리를 만듦
        re_list.append(re_dict) # 영화에 수익을 key값으로 가지고 타이틀을 value값으로 가지는 딕셔너리들을 re_list에 저장
        revenue.append(int(movies_list_file['revenue'])) #값을 비교할 수 있도록 영화의 수익들(key)값을 저장하는 revenue 리스트 에 정수로 저장
    top_movie = 0 # 최고로 수익이 높은 영화의 이름을 저장할 변수 
    for retitle in re_list: # re_list 리스트에서 원소인 딕셔너리들을 순회하면서
        if retitle.get(sorted(revenue)[-1]): # 수익을 정렬한 리스트에서 가장 수익이 높은 영화의 수익을 키 값으로 가지는 딕셔너리가 retitle에 있으면 
            top_movie = retitle.get(sorted(revenue)[-1]) # 그 영화의 이름을 top_movie 변수에 저장
    return top_movie # 수익이 가장 높은 영화의 이름 반환  
  ```
  
  * 이 문제에서 어려웠던점
    - 수익에 관한 정보를 불러와서 수익 : 영화이름 인 딕셔너리를 만들고 그것을 정렬한 다음 가장 높은 수익을 찾고 그것을 다시 영화이름과 매치하는 과정에서 리스트에 딕셔너리들을 추가하고 get함수로 조건문을 만들어서 판별하는 방법이 어려웠습니다.
  * 내가 생각하는 이 문제의 포인트
    - 수익과 영화이름 정보를 묶어서 불러와서 get을 통해 조건문 생성하는것 

## E. 알고리즘을 사용한 데이터 출력

* 요구 사항 : 영화 세부 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다. 해당 과정은 향후 커뮤니티 서비스에서 추천 기능의 일부로 사용됩니다

* 결과 : 
```
['그린 마일', '인생은 아름다워', '반지의 제왕: 왕의 귀환', '스파이더맨: 뉴 유니버스']
```
  
  * 문제 접근 방법 및 코드 설명
  
  ```python
  def dec_movies(movies):
    m_list = [] # 영화의 정보들을 담은 딕셔너리를 요소로 저장하는 리스트 m_list를 만듦
    for m in movies:
        result ={
        'id' : m.get('id'),
        'title' : m.get('title'),
        'poster_path' : m.get('poster_path'), # 해당 key가 있으면 해당 value를 반환, 없으면 none을 반환
        'vote_average' : m.get('vote_average'),
        'overview' : m.get('overview'),
        'genre_ids' : m.get('genre_ids'),
    }
        m_list.append(result) # m_list 에 result 값 추가
    dec_title_list = [] # 개봉일이 12월인 영화 제목들을 저장하는 리스트 
    for movie_dict in m_list: # m_list에서 각 영화 정보 담긴 딕셔너리 추출
        movie_dict_id = movie_dict.get('id') # Movie_dict_id에 각 영화 정보 딕셔너리에 담긴 id value를 movie_dict_id에 저장 
        movies_file = open(f'data/movies/{movie_dict_id}.json', encoding='utf-8')  # movie_dict_id에 해당하는 영화 상세정보 파일 불러오기
        movies_list_file = json.load(movies_file) # movies_list_file 변수에 저장.  
        if movies_list_file["release_date"][5:7] == '12': # movies_list_file 변수에서 조건문을 걸어서 개봉일이 12월이면 
            dec_title_list.append(movies_list_file["title"]) # 그 영화의 이름을 dec_title_list 리스트에 추가 
    return dec_title_list    
  ```
  
  * 이 문제에서 어려웠던점
    - 아이디값으로 영화의 데이터를 불러온 다음 개봉일자에 해당하는 정보를 탐색하고 슬라이싱하는것이 어려웠습니다. 
  * 내가 생각하는 이 문제의 포인트 
    - 정보를 불러온 다음 슬라이싱하여 조건을 형성하고, 12월에 개봉한 영화 이름을 담을 리스트에 추가하는것


# 후기

* 오늘 프로젝트 첫 프로젝트인 만큼 어떻게 무엇을 해야하는지 알지 못해서 두려웠습니다. 문법과 간단한 문제만 풀었던 저에게 갑자기 어떤 기능을 만들어보라고 하니 갑갑하였습니다. 솔직히 저는 과제를 처음 보고는 어떻게 하는지 전혀 감을 잡지 못하였습니다. 하지만 작은 소단위의 기능을 하나하나 구현해보고 그것을 발전시키자 더 다양한 기능을 구현할 수 있었고 나도 이런 기능을 만들어 낼 수 있다는 것이 신기하였습니다. 
* 저 자신에 대해 약간의 자신감이 하락하였습니다. 저는 그나마 주어진 시간 내에 완성을 하였으나 주변에서는 저보다 훨씬 빠른 시간에 완성하는 학우들이 있었습니다. 어떻게 바로 어떤식으로 구현할지 생각하여 코드를 짜는것인지 신기하고 저도 그런 능력을 갖고싶었습니다. 
* 기능을 구현하는데 삽질을 많이 하였습니다. 결정적인 포인트 하나를 실수하여 뺑 돌아가게 되는 경우도 나오고 한정된 특이 상황만 정상적으로 동작하는 꼼수 코드도 있었습니다. 다양한 시행착오를 겪으며 개발은 어렵다는 것을 느꼈습니다. 
* 코드를 짜면서 어떻게든 기능을 구현을 해 내었지만 가독성이 많이 떨어지고 복잡한 방식으로 구현하는 것 같다는 느낌이 들었습니다. 코드를 더 간결하고 직관적으로 짜고 싶습니다.
* 리스트 안에 딕셔너리가 있는 복합적인 자료형을 다루는 것이 헷갈리고 어렵게 느껴졌습니다. 자료 탐색이란 이렇게 어려운 것인줄 몰랐습니다. 자료가 직관적으로 나타나지 않고 내가 지금 다루는 자료가 어떤 형식인지 일일히 확인해야 한다는 것을 알았습니다.  
* 개발을 할 때는 일일히 print 함수를 찍어보면서 자료 구조를 파악하고 현재 내가 어떤 자료를 다루고 있는지 확인하는 것이 중요하다는것을 배웠습니다. 
* 이전까진 데이터를 입력하거나 있는 데이터로 코드를 작동시키는 법만을 실습했는데 밖에 있는 데이터를 읽어서 사용하는 방법을 익힐 수 있어서 좋았습니다. 
* 코드를 옆 사람에게 논리적으로 설명해보는 것의 중요성을 깨달았습니다. 막힌 부분이 있을때 지금 내 코드가 어떤 식으로 작동하고 어디서 오류가 났는지 설명하다 보면 코드의 문제점을 파악하기 쉬워집니다. 그리고 남의 코드 설명을 들으면서 저랑 다른 방식으로 구현한 것을 참고하여 사고를 확장시킬 수 있었습니다. 
* 만든 코드를 되돌아보면 쉽게 느껴지는데 실제 아무것도 없는 환경에서 구현하는것은 매우 어렵게 느껴집니다. 스스로 만들어보는것의 중요성을 알았습니다. 
* 이중으로 for문을 쓰면서 범위가 많이 헷갈리고 실제로 어떤 문자가 무엇을 반복하는지 헷갈렸습니다
* 변수가 엄청 많이 쓰이는데 변수 명을 생각하는 것이 어렵다는걸 이번에 직접 느꼈습니다. 
* 금요일 과제는 배운것을 몽땅 다 활용하고 구글링까지 해야 풀 수 있다는 것을 알고나니 다음주 금요일이 무서워졌습니다...
* for문에는 대부분 결과값을 저장할 변수와 리스트를 만들어내는것이 편하다는 것을 알았습니다. 
* 이렇게 해도 작동할까? 이게 작동하네? 하면서 이렇게 코드를 짜서 문제상황을 해결하는 것이 재미있었습니다. 창의성을 발휘할 수 있어서 좋았습니다.
* 기능을 추가하기만 하면 되는데 코드를 덧붙이거나 그대로 반복문에 넣어서 다음 문제를 해결하는 것이 처음이라 어렵게 느껴졌습니다.  
* 결국 개발자는 남과 협업해야 하기 때문에 자신의 코드를 설명하고 남의 코드를 이해하는 것이 중요하다고 생각하였습니다.