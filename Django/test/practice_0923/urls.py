"""practice_0923 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

#
from random_game import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path 등록
    # 1. 주소를 지정
    # 2. 어떤 view를 실행할건지 지정
    path("", views.index),
    path("todaybeer/", views.todaybeer),
    path("lotto/", views.lotto),
    path("is-even-odd/<int:_number>", views.is_even_odd),
    path("calc/<int:a>/<int:b>", views.calc),
    path("pastlife/", views.pastlife),
    path("krlipsum/", views.krlipsum),
    path("krlipsum_output/", views.krlipsum_output),
    ## url 분리
    # 방명록 목록
    path("geustbook/", views.geustbook),
    path("create/", views.create),
]
