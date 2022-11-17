from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. you're at the polls index.")


#3) view 내부의 index 함수에서는 hello world 라는 응답을 클라이언트 한테 전달 
#