from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    print(articles)
    return render(request, 'articles/index.html', context)



def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')


    # DB에 새로운 Article 저장
    '''
    Article.objects.create(
        title=title,
        content=content
    )
    '''

    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')