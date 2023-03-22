from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
        
    else:
        form = ArticleForm()
    context = {'form' : form}
    return render(request, 'articles/create.html', context)