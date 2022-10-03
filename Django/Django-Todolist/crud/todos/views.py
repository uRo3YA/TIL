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


def completed_toggle(request, todo_pk):
    obj = Todo.objects.get(id=todo_pk)
    obj.completed = not obj.completed
    obj.save()
    return redirect("todos:index")


def edit(request, todo_pk):

    return redirect("todos:index")


def editUpdate(request, pk):
    todos = Todo.objects.get(id=pk)
    todos.content = request.GET.get("content_")
    todos.priority = request.GET.get("priority_")
    todos.deadline = request.GET.get("deadline_")
    todos.save()

    return redirect("todos:index")


def hello(request):
    # 대강의 필터 구현
    data = []
    for obj in Todo.objects.filter(priority=5):
        data.append(obj)
    context = {"todos": data}
    return render(request, "todos/hello.html", context)

    # return render(request, "todos/hello.html")


# def priority_filter(request):
#     todos = []
#     for obj in Todo.objects.filter(priority=5):
#         todos.append(obj)
#     context = {"todos": todos}
#     return render(request, "todos:index")
