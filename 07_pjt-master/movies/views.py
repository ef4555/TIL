from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http.response import JsonResponse, HttpResponse

from .models import Actor, Movie, Review

from django.core import serializers
from .serializers import ActorSerializer, MovieListSerializer, ReviewSerializer, ActorListSerializer, MovieSerializer, ReviewListSerializer

# api_view없으면 오류
# Create your views here.
@api_view(['GET',])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Actor) # 리스트를 반환하거나 없으면 404 반환
        serializer = ActorListSerializer(actors, many=True) # many=True: M:N 관계 serializer사용시 필요
        return Response(serializer.data) 

@api_view(['GET',])
def actor_detail(request, actor_pk):
     actor = get_object_or_404(Actor, pk=actor_pk)
     if request.method == 'GET':
         serializer = ActorSerializer(actor)
         return Response(serializer.data)
     
@api_view(['GET',])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True) # many=True: M:N 관계 serializer사용시 필요
        return Response(serializer.data)
    
    
@api_view(['GET',])
def movie_detail(request, movie_pk):
     movie = get_object_or_404(Movie, pk=movie_pk)
     if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
@api_view(['GET',])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET','DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        ment = f'review {review_pk} is deleted'
        context = {
            'delete': ment
        }
        return Response(context)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data)

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): 
        serializer.save(movie=movie) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)