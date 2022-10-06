from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    # 영화 데이터 목록 조회
    path("", views.index, name="index"),
    # 영화 데이터 정보 조회 detail
    path("<int:pk>/", views.detail, name="detail"),
    # - 영화 데이터 생성 create
    path("create/", views.create, name="create"),
    # - 영화 데이터 수정 update
    path("<int:pk>/update/", views.update, name="update"),
    # - 영화 데이터 삭제 delete
    path("<int:pk>/delete/", views.delete, name="delete"),
]
