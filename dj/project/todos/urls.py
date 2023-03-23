from django.urls import path, include
from . import views

app_name = 'todos'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('done/<int:pk>/', views.done, name="done"),
]
