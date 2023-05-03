from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment 
from .serializers import ArticleListSerializer, CommentSerializer, ArticleDetailSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article) # get_list_or_404 : 전체 조회시 사용
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk) # get_object_or_404 : 하나만 조회시
    
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
# @api_view(['GET', 'POST'])        
# def comment_list(request):
#     if request.method == 'GET':
#         comment = Comment.objects.all()
#         serializer = CommentSerializer(comment, many=True)
#         return Response(serializer.data)


@api_view(['GET', 'POST'])      
def comment_detail(request, comment_pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

@api_view(['GET', 'POST'])      
def comment_list(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
        