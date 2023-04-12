from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    hashtag = Hashtag.objects.all()
    context = {'articles': articles, 'hashtag':hashtag}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    # Select * from comment where parent is NULL;
    comments = article.comment_set.filter(parent__isnull=True) # 댓글
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user            
            article.save()
            
            # hash tag 저장
            for word in article.content.split(): # 공백을 기준으로 리스트
                if word[0] == '#':
                    # word랑 같은 해시태그가 존재하면 기존 객체 반환, 없으면 새로운 객체 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # 1. 현재 등록된 모든 해시태그 보기
                    # 2. 클릭 시 hashtag 기준으로 filter 해주기
                    # 3. 게시물 수정 시, 새로 등록된 해시태그 검사 해주기                      
                    article.hashtags.add(hashtag)
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm()
        hash = Hashtag.objects.all()

    context = {'form': form, 'hash': hash}
    return render(request, 'articles/create.html', context)



def hashtag_filter(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)

    articles = hashtag.article_set.order_by('-pk')
    print(articles)
    hashtag_list = Hashtag.objects.all()
    context = {
        'hashtag_list': hashtag_list,
        'hashtag' : hashtag,
        'articles' : articles,
    }
    return render(request, 'articles/hashtag.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                s = article.hashtags.all()
                for i in s:
                    article.hashtags.remove(i)
                    
                for word in article.content.split():
                    if word[0] == '#':
                        # word랑 같은 해시태그가 존재하면 기존 객체 반환, 없으면 새로운 객체 생성
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        # 1. 현재 등록된 모든 해시태그 보기
                        # 2. 클릭 시 hashtag 기준으로 filter 해주기
                        # 3. 게시물 수정 시, 새로 등록된 해시태그 검사 해주기                      
                        article.hashtags.add(hashtag)
                        
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article.pk)
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)


def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        parent_pk = request.POST.get('parent_pk')
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # comment_form는 article과 user행 정보는 안받은 상태(exclude 되어있음)
            comment.article = article # 비어있는 칼럼에 정보 추가
            comment.user = request.user
            if parent_pk:
                parent = Comment.objects.get(pk=parent_pk)
                comment.parent = parent
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


def comments_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', pk)


def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
