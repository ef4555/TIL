from django.shortcuts import render

# Create your views here.

def pr(request, name, cnt):
    print('pr 함수 호출됨')
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if name in product_price:
        p = product_price[name]
        context = f'{name} {cnt}개의 가격은 {p*cnt}원 입니다.'
    else:
        context = name + '은/는 없어용'
    

    print('pr 함수 종료')
    return render(request, 'price/cal.html', {'context' : context})