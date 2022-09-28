from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {"todos": _todos}

    return render(request, "todos/index.html", context)


def create(request):

    # 1. parameter로 날라온 데이터를 받아서
    content = request.GET.get("content_")
    priority = request.GET.get("priority_")
    deadline = request.GET.get("deadline_")

    # 2. DB에 저장
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    context = {"content": content, "priority": priority, "deadline": deadline}

    return redirect("todos:index")


def delete(request, todo_pk):
    # pk에 해당하는 글 삭제
    Todo.objects.get(id=todo_pk).delete()

    return redirect("todos:index")


def update(request, todo_pk):
    obj = Todo.objects.get(id=todo_pk)
    if obj.completed == True:
        obj.completed = False
    else:
        obj.completed = True
    obj.save()
    return redirect("todos:index")


def hello(request):

    return render(request, "todos/hello.html")
