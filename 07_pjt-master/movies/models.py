from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

# Create your models here.
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