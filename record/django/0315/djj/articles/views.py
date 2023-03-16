from django.shortcuts import render

# Create your views here.

def hello(requests, name):
    print('hello 함수 호출됨')
    print(f'name : {name}')
    context = {
        'name' : name
    }
    

    print('hello 함수 종료')
    return render(requests, 'articles/hello.html', context)
