from django.shortcuts import render

# Create your views here.
def cal(request, first, second):
    minus = first - second
    mul = first * second
    if second == 0:
        div = '계산할 수 없습니다.'
    else:
        div = first / second


    return render(request, 'calculators/calculator.html', {'first':first, 'second':second, 'div':div, 'minus':minus, 'mul':mul})