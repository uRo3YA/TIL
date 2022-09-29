from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path("", views.index, name="index"),
    # path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("delete/<int:todo_pk>", views.delete, name="delete"),
    path(
        "completed_toggle/<int:todo_pk>",
        views.completed_toggle,
        name="completed_toggle",
    ),
    path("edit/<int:todo_pk>", views.edit, name="edit"),
    ##테스트 출력용
    path("hello", views.hello, name="hello"),
    path("editUpdate/<int:pk>", views.editUpdate, name="editUpdate"),
]
