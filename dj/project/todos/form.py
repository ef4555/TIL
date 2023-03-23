from django import forms # form을 장고에서 불러옴
from .models import Todo # 모델폼 쓸거니까 모델에서 만들어둔 todo 클래스 갖고와야함

'''
Django form Vs. ModelForm
Form : html 랜더링, 유효성 검사 <- 귀찮다. 장고한테 짬처리
ModelForm : 어짜피 form 객체 DB와 같이 쓸건데, 필드도 model 기반으로 만들어줘. 왜? 귀찮으니까
'''


class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo # 이 모델 기반으로 Form을 만들어줘
        fields = ('task',) # 모든 필드를 다 받지 않고 task만 보내는 form을 만들거야
        # exclude와 fields 중 둘 중 하나만 쓰자