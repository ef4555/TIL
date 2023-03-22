from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('create/', views.creat_article, name='create')
]
