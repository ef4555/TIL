

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import TodoForms # DB로 만든 form을 불러온다.
from .models import Todo # 저장되어있는 데이터베이스 불러온다.


# Create your views here.
def index(request):
    print('index 함수 도착')
    form = TodoForms()
    todo_list = Todo.objects.all() # 모든 Todo 데이터 조회
    context = {
        'form' : form,
        'todo_list' : todo_list
    }
    return render(request, 'todos/index.html', context)

@ login_required
def create(request):
    print('#'*30)
    print('create 함수 도착')
    print(f'request: {request}')
    print(request.method) # POST
    print(type(request.method)) # str
    print(request.POST)
    print('#'*30)

    if request.method == "POST":
        # task = request.POST.get('task')를 모델폼이 대신 해줌
        form = TodoForms(request.POST) 
        if form.is_valid(): # 유효성 검사 -> cleaned_data(dict) => clean_field
            form.save()

    return redirect('todos:index')


@ login_required
def update(request, pk):
    print('update')
    print(pk)
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForms(request.POST, instance=todo)
        if form.is_valid:
            form.save()
        return redirect('todos:index')

    else:
        form = TodoForms(instance=todo)

    context = {
        'form':form,
        'todo': todo # pk값을 todo에서 뽑아오므로 todo를 넘겨주어야 한다.
    }
    return render(request, 'todos/update.html', context)


def delete(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(pk=pk)
        todo.delete()
    else:
        pass
    return redirect('todos:index')

def done(request, pk):
    # Auth가 있으면?
    todo = Todo.objects.get(pk=pk)
    todo.isCompleted = True
    todo.save()
    return redirect('todos:index')