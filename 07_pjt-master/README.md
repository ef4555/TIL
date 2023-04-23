>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 07

### 이번 pjt 를 통해 배운 내용

* Django REST framework

* REST API의 이해 및 구축

* Django Serializer 사용법

* Serializer로 직렬화하여 JSON형태로 정보 가공

* Nested relationships를 통한 역참조 데이터 조회

## 사전 설정


```python 
# settings.py
INSTALLED_APPS = [
    'movies',
    'rest_framework', # 추가 pip install 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```


```python 
# urls.py
urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
]
```

```python
# 총 3가지 모델 설정
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    actors = models.ManyToManyField(Actor)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

```

## A. 전체 배우 목록 제공

* 결과 : 
  
  ```python
  # views.py
  @api_view(['GET',])
  def actor_list(request):
      if request.method == 'GET':
          actors = get_list_or_404(Actor) # 리스트를 반환하거나 없으면 404 반환
          serializer = ActorListSerializer(actors, many=True) # many=True: M:N 관계 serializer사용시 필요
          return Response(serializer.data)  
  ```

  ```python
  # 배우 전체 직렬화
  # serializers.py
  class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
  ```

  ```python 
  # models.py
  class Actor(models.Model):
    name = models.CharField(max_length=100)

  class Movie(models.Model):
    actors = models.ManyToManyField(Actor)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    
  class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  ```
  
  * 이 문제에서 어려웠던점
    - serializer 사용하여 정보를 json으로 직렬화

  * 내가 생각하는 이 문제의 포인트
    - 모델 설정과 serializer 사용법


## B. 단일 배우 목록 제공

* 결과 : 
  
  ```python
  # views.py
  @api_view(['GET',])
  def actor_detail(request, actor_pk):
      actor = get_object_or_404(Actor, pk=actor_pk)
      if request.method == 'GET':
          serializer = ActorSerializer(actor)
          return Response(serializer.data)
      
  ```

  ```python
  # serializers.py 

  # 영화 제목만 직렬화
  class MovieTitle(serializers.ModelSerializer):
      class Meta:
          model = Movie
          fields = ('title',)

  # 배우를 직렬화, 역참조로 movie 제목 데이터 조회
  class ActorSerializer(serializers.ModelSerializer):
      movie = MovieTitle(many=True, read_only=True, source='movie_set')
      class Meta:
          model = Actor
          fields = '__all__'
  ```
  
  * 이 문제에서 어려웠던점
    - Nested relationships를 통한 역참조 데이터 조회
      - source : 필드를 채우는데 사용할 속성의 이름
      - 그냥 movie_set = MovieTitle(many=True, read_only=True)도 가능


  * 내가 생각하는 이 문제의 포인트
    - Nested relationships를 통한 역참조 데이터 조회
    - 중첩된 관계 설정
    - 필드 설정


## C. 전체 영화 목록 제공

* 결과 : 
  
  ```python
  # views.py
  @api_view(['GET',])
  def movie_list(request):
      if request.method == 'GET':
          movies = get_list_or_404(Movie)
          serializer = MovieListSerializer(movies, many=True) # many=True: M:N 관계 serializer사용시 필요
          return Response(serializer.data)
  ```

  ```python
  # serializers.py 

  # 영화 목록 직렬화, 제목하고 오버뷰만
  class MovieListSerializer(serializers.ModelSerializer):
      class Meta:
          model = Movie
          fields = ('title', 'overview')
  ```
  
  * 이 문제에서 어려웠던점
    - 영화 목록 직렬화하고 필드 설정


  * 내가 생각하는 이 문제의 포인트
    - 영화 목록 직렬화하고 필드 설정

## D. 단일 영화 목록 제공

* 결과 : 
  
  ```python
  # views.py
  @api_view(['GET',])
  def movie_detail(request, movie_pk):
      movie = get_object_or_404(Movie, pk=movie_pk)
      if request.method == 'GET':
          serializer = MovieSerializer(movie)
          return Response(serializer.data)
  ```

  ```python
  # serializers.py 
  # 배우 이름만 직렬화
  class ActorNameSerializer(serializers.ModelSerializer):
      class Meta:
          model = Actor
          fields = ('name',)

  # 리뷰 목록 직렬화
  class ReviewListSerializer(serializers.ModelSerializer):
      class Meta:
          model = Review
          fields = ('title', 'content')
          read_only_fields = ('movie',)

  # 영화 세부정보 직렬화
  class MovieSerializer(serializers.ModelSerializer):
      actors = ActorNameSerializer(many=True, read_only=True) # 배우 이름은 정참조로 직렬화
      review_set = ReviewListSerializer(many=True, read_only=True) # 리뷰는 역참조로 직렬화 
      class Meta:
          model = Movie
          fields = '__all__' # 추가한 필드까지 모두 직렬화
  ```
  
  * 이 문제에서 어려웠던점
    - Nested relationships를 통한 정참조, 역참조 데이터 조회
      - 배우 id 이용 배우 이름을 정참조하여 직렬화
      - 영화에 쓰여진 댓글 불러오기 위해 review 테이블에 있는 정보를 불러와야 하므로 ReviewListSerializer를 이용해 역참조하여 직렬화
      - review_set이라 했으므로 따로 source 써 줄 필요 없다


  * 내가 생각하는 이 문제의 포인트
    - 영화 정보에 정참조 역참조 데이터 조회하여 추가

## E. 전체 리뷰 목록 제공

* 결과 : 
  
  ```python
  @api_view(['GET',])
  def review_list(request):
      if request.method == 'GET':
          reviews = get_list_or_404(Review)
          serializer = ReviewListSerializer(reviews, many=True) # 1대 N 관계, 하나의 영화에 여러 리뷰가 존재, many=True
          return Response(serializer.data)
  ```

  ```python
  # serializers.py 
  # 리뷰 목록 직렬화
  class ReviewListSerializer(serializers.ModelSerializer):
      class Meta:
          model = Review
          fields = ('title', 'content')
          read_only_fields = ('movie',)

  ```
  
  * 이 문제에서 어려웠던점
    - 리뷰 목록 직렬화
    - read_only_fields설정 


  * 내가 생각하는 이 문제의 포인트
    - 1대N 관계 이해하여 serializer 사용


## F. 단일 리뷰 조회, 수정, 삭제

* 결과 : 
  
  ```python
  @api_view(['GET','DELETE', 'PUT'])
  def review_detail(request, review_pk):
      review = get_object_or_404(Review, pk=review_pk)
      if request.method == 'GET': 
          serializer = ReviewSerializer(review) # pk에 맞는 리뷰 데이터 직렬화
          return Response(serializer.data)
      
      # 삭제
      elif request.method == 'DELETE':
          review.delete()
          ment = f'review {review_pk} is deleted' # 삭제 후 메시지
          context = {
              'delete': ment
          }
          return Response(context)

      # 수정
      elif request.method == 'PUT':
          serializer = ReviewSerializer(review, data=request.data) # 수정이므로 데이터는 request의 데이터
          if serializer.is_valid(raise_exception=True): 
              serializer.save() 
              return Response(serializer.data)

  ```

  ```python
  # serializers.py 
  # movie 모델에서 영화 제목만 직렬화하는 Serializer
  class MovieTitle(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

  # 리뷰 직렬화, MovieTitle이용 정참조 
  class ReviewSerializer(serializers.ModelSerializer):   
      movie = MovieTitle(many=False, read_only=True) # 리뷰가 달린 영화 id에 따른 영화 제목 출력, review 테이블에서 정참조 관계
      class Meta:
          model = Review
          fields = '__all__'

  ```
  
  * 이 문제에서 어려웠던점
    - 정참조를 통해 리뷰가 달린 영화 id에 따른 영화 제목 출력
    - request 요청에 따라 수정, 삭제, 조회 구현
      - 'request.method ==' 사용


  * 내가 생각하는 이 문제의 포인트
    - request 요청에 따라 수정, 삭제, 조회 구현
    - 삭제후 메시지 context에 담아서 Response
    - data=request.data로 수정(PUT) 시 원래 데이터 받기

## G. 리뷰 생성

* 결과 : 
  
  ```python
  @api_view(['POST'])
  def review_create(request, movie_pk):
      movie = Movie.objects.get(pk=movie_pk)
      serializer = ReviewSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True): 
          serializer.save(movie=movie) 
          return Response(serializer.data, status=status.HTTP_201_CREATED)

    ```

    ```python
    # 리뷰 직렬화, MovieTitle이용 정참조 
  class ReviewSerializer(serializers.ModelSerializer):   
      movie = MovieTitle(many=False, read_only=True) # 정참조 해서 직렬화, 1개의 글에 1개의 리뷰 생김 1대1관계 many=False
      class Meta:
          model = Review
          fields = '__all__'

  ```
  
  * 이 문제에서 어려웠던점
    - 리뷰와 영화의 관계 파악 (1대1)
      - 1개의 리뷰는 한개의 영화에 달린다.
      - many=False


  * 내가 생각하는 이 문제의 포인트
    - 정참조 해서 직렬화


-----

....

문제 푼 내용을 기반으로 적어주세요.

# 후기

* Nested Serilizer에서 많이 헤메어서 시간이 많이 소요되었다. 
* 수업 내용에 다 나온 내용인데 기억하지 못하였다. README를 쓰면서 다시 한 번 복습하였다. 
* 관계 설정을 명확히 해야 정참조인지 역참조인지 파악하여 직렬화를 할 수 있다.
* 정참조 역참조에 따른 문법 요소들을 정확히 알고 있어야 오류가 나지 않는다.
* API는 기능별로 하나씩 만드는게 헷갈리지 않는 것 같다
