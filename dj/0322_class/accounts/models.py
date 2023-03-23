from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 장고가 가지고 있는 User Model을 상속 받고 세부 요소들을 재정의
# 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User클래스와 완전히 같은 모습을 가지게 됨
class User(AbstractUser):
    pass
