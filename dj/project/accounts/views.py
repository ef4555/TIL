from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def login(request):
    if request.method == "POST": # 로그인 요청
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # 로그인 세션 생성
            # return redirect('todos:index')
            return redirect(request.GET.get('next') or 'todos:index')
    else:  # GET
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('todos:index')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # UX적으로 편하게, 회원가입 -> 자동로그인
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/signup.html', context)