from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), # 새로운 글 DB에 등록
    # path('new/', views.new, name='new'), # 새로운 글 작성
    path('<int:pk>/', views.detail, name="detail"), # pk 기준 글의 디테일 보여줌
    path('<int:pk>/delete/', views.delete, name="delete"), # 글 삭제
    path('<int:pk>/edit/', views.edit, name="edit"), # 글 수정하는 페이지 이동
    path('<int:pk>/update/', views.update, name="update"), # 글 수정
]