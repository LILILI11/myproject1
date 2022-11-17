from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
]

#2) 여기서는 전달 받으면 /polls/ 이외에 아무것도 없음
#그러면 path내에서 views.index라는 view 내부로 연결을 시켜줌
#다음 --> views.py