from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles': articles}
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
        
    else:
        form = ArticleForm()
    context = {'form' : form}
    return render(request, 'posts/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('posts:index')