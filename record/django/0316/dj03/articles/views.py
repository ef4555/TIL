from django.shortcuts import render
from .models import Article

# Create your views here.


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title':message,
        'content':content
    }
    return render(request, 'articles/catch.html', context)


def index(request, name, pk):
    print('articles index 함수 호출됨')
    print(f'name: {name}')

    article_list = Article.object.all()
    article = Article.objects.get(pk=pk)
    context = {
        'name': name,
        'articles': article_list, # DTL에서 for loop <ul><li></li></ul>

    }
    print('article index 함수를 종료')

    return render(request, 'articles/index.html', context)


def creat_article(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    author = request.GET.get('author')

    article = Article(title=title, content=content, author=author)
    article.save()

    return render(request, 'articles/index.html')