from django.urls import path
from . import views # 내 위치에서 views를 가져와

app_name = 'calculators'
urlpatterns = [
    path('calculator/<int:first>/<int:second>/', views.cal)
]
