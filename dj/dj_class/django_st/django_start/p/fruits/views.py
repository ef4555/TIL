from django.shortcuts import render

# Create your views here.
def aa(requests):
    return render(requests, "fruit.html")

def bb(requests):
    return render(requests, "dd.html")
