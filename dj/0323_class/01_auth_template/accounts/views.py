from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods # 특정한 요청만 처리하게 하는 데코레이터

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == "POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['POST']) # 데코레이터를 써서 간단하게 방지 가능
def delete(request):
    # if request.method == "POST": 주소창 입력으로 삭제하는 것 방지
    request.user.delete()
    auth_logout(request) # 탈퇴 후 로그아웃 순서
    # 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어지기 때문에
    return redirect('articles:index')
    # else:
        # return redirect('articles:index')
def update(request):
    if request.method == "POST":
        form=CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('article:index')
        pass
    else:
        form = PasswordChangeForm(request.user)
    context = {'form' : form}
    return render(request, 'accounts/change_password.html', context)