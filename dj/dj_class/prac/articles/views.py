from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1] # 전체 아티클 조회 최근 글이 앞으로
    # 동일 : articles = Article.objects.all().order_by('-pk') 
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# READ
def detail(request, pk): # pk에 맞는 글을 DB에서 불러와서 context에 저장
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

'''
# CREATE
def new(request):
    print('new 함수에 도달')
    return render(request, 'articles/new.html')
'''

# POST 요청 받아서 DB에 게시글 저장 함수
# title, content 받아서 새로운 article형성
def create(request):
    print('create 함수에 도달')
    print(request)
    # 1. 유효성 검사(장고가 이미 해주고 있다.)

    # 분기처리 new함수와 create함수를 합침
    if request.method == 'POST': # 게시글 작성 요청
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:index')
    
    else: # 게시글 작성 페이지 요청
        print('new 함수에 도달')
        return render(request, 'articles/new.html')

    # 2. Article 객체 생성
    # article = Article(title=title, content=content)
    # 3. 저장
    # article.save()
    # return render(request, 'articles/index.html') index함수 작동 안함
    # urls -> view -> html
    # 게시글이 갱신되었으므로 다시 urls로부터 시작해야 하니까 redirect를 쓴다.(데이터베이스의 변동이 있을때)
    # return redirect('articles:index')

# DELETE
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

'''
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)
'''



def update(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)

    else: # 게시글 작성 페이지 요청
        article = Article.objects.get(pk=pk)
        context = {
            'article': article,
        }
        return render(request, 'articles/edit.html', context)