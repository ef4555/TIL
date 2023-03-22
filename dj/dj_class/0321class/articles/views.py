from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # 유효성 검사 후 boolean으로 반환
            article = form.save()
            return redirect('articles:detail', article.pk)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm() # 데이터가 없는 form을 만듦(빈칸), new의 역할

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk) # 데이터베이스에서 불러와서 article에 저장

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # 수정한 instance를 받아와서 저장
        if form.is_vaild():
            form.save()
            return redirect('articles:detail', pk=article.pk)
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article) # instance를 받아옴


    context = {'form': form, 'article':article}
    return render(request, 'articles/update.html', context)
