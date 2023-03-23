from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): # 모델 AbstractUser폼을 상속받아서 씀
    pass