from django import forms 
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

# 모델폼
# forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
# 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
# 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '글 내용을 입력하세요',
                'row': 5,
                'col': 50,
            }
        ),
    )
    class Meta: # ModelForm의 정보를 작성하는 곳
        model = Article # Article 모델을 기반으로 form을 작성
        fields = '__all__'
        
