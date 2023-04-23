from rest_framework import serializers
from .models import Movie, Actor, Review

# 영화 제목만 직렬화
class MovieTitle(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

# 배우를 직렬화, 역참조로 movie 추가
class ActorSerializer(serializers.ModelSerializer):
    movie = MovieTitle(many=True, read_only=True, source='movie_set')
    class Meta:
        model = Actor
        fields = '__all__' 
         
# 배우 이름만 직렬화
class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)

# 배우 전체 직렬화
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 영화 목록 직렬화, 제목하고 오버뷰만 
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')
 

# 리뷰 직렬화, MovieTitle이용 정참조 
class ReviewSerializer(serializers.ModelSerializer):   
    movie = MovieTitle(many=False, read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

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
        