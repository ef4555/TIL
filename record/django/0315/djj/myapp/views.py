from django.shortcuts import render

# Create your views here.
def index(request):
    apple = ['iphone', 'airpod']

    info = {
        'name' : 'Aiden',
        'age' : 26,
    }

    return render(request, "myapp/index.html", {'apple' : apple})