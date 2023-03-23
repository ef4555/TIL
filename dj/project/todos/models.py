from django.db import models

# Create your models here.
class Todo(models.Model):
    '''
    task = charfield 채택
    isCompleted = False 채택
    created_at = datafield 생성 시간
    completed_at = datafield 완료 시간
    inProgress = True
    -> 

    not : 부정연산자
    '''

    task         = models.CharField(max_length=300)
    isCompleted  = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True) # auto_now_add=False 인지 구분 중요
    completed_at = models.DateTimeField(auto_now=True)

    # 최초 모델을 생성하고 migrate 해주어야 한다.
    # 데이터베이스 테이블 이름은 : 앱이름_모델이름(todos_todo)