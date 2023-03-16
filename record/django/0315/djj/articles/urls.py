from django.urls import path
from . import views # 내 위치에서 views를 가져와

app_name = 'articles'

urlpatterns = [
    path('hello/<name>/', views.hello, name='hello')
]

