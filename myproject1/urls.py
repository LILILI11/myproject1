"""myproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/',include('polls.urls')), #include를 이용해 polls.url 참조 하도록 함
    path("admin/", admin.site.urls),
]

#1) 127.0.0.1/polls/ url이 들어왔으면 이 url을 파싱해서 (url 파일에서 요청한 주소를 잘게 나누어 주는게 파싱)
#polls라는 해당 path를 잡아내고 polls앱 url로 연결 시켜주고

#다음 -->polls/urls.py/