urls.py# Django CRUD

## 1. 가상환경 및 Django 설치

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13  #Django만 설치
$ pip freeze > requirements.txt # requirements.txt에 설치된 패키지들을 기록 
$ pip install -r requirements.txt # 이전에 기록한 패키지 모두 설치
```

### 3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt .
```

## 2. articles app

### 1. app 생성

```bash
python manage.py startapp practice(애플리케이션 이름) # 앱 생성
```

### 2. app 등록

settings.py

* 생성한 앱 등록(필수), 그 외에 언어 설정도 가능

```python
# Application definition

INSTALLED_APPS = [
    'practice', # 앱을 등록한다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr' # 언어 설정도 가능

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

### 3. urls.py 설정

### 1. urls 설정

articles(appname)/urls.py

* 다른 url들의 설정을 가져오려면 include를 import해서 사용한다.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

pjt/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index')
]
```

### 2. view 함수 생성

views.py

```python
from django.shortcuts import render

# 요청 정보를 받아서
def index(request):
        # 페이지를 render
    return render(request, 'articles/index.html')
```

<br>

### 3. template 생성

index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
    <h1>게시판</h1>
    <a href="{% url 'articles:new' %}">글쓰기</a>
</body>

</html>
```

### 4. base.html로 templates 설정

- 프로젝트 폴더의 하위에 `templates` 폴더 생성후 `base.html` 파일 생성
- 부트스트랩과 글꼴도 함께 적용

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.0/font/bootstrap-icons.css">
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js"
    integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT"
    crossorigin="anonymous"></script>
  <style>
    * {
      font-family: "Noto Sans KR", sans-serif;
    }
  </style>
  <title>Document</title>
</head>

<body>
  {% block content %} {% endblock %}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
    integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js"
    integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz"
    crossorigin="anonymous"></script>
</body>

</html>
```

- 프로젝트 단위의 settings.py에 템플릿 적용

```python
# pjt/settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / "templates"],
        ...
    }
]
```

<br>

## 3. Model 정의 (DB 설계)

### 1. 클래스 정의

```python
from django.db import models

# 1. 모델 설계(DB 스키마 설계)
class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  careated_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

### 2. 마이그레이션 파일 생성

```terminal
python mange.py makemigrations # 마이그레이션 파일 생성
```

### 3. DB 반영(`migrate`)

```terminal
python manage.py migrate # DB에 반영
```

## 4. CRUD 기능 구현

### 1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

#### 1. HTML Form 제공

> http://127.0.0.1:8000/articles/new/

#### 2. 입력받은 데이터 처리

> http://127.0.0.1:8000/articles/create/

> 게시글 DB에 생성하고 index 페이지로 redirect

### 2. 게시글 목록

> DB에서 게시글을 가져와서, template에 전달

### 3. 상세보기

> 특정한 글을 본다.

> http://127.0.0.1:8000/articles/<int:pk>/

### 4. 삭제하기

> 특정한 글을 삭제한다.

> http://127.0.0.1:8000/articles/<int:pk>/delete/

### 5. 수정하기

> 특정한 글을 수정한다. => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

> http://127.0.0.1:8000/articles/<int:pk>/update/

urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('new', views.new, name='new'),
  path('create', views.create, name='create')
]
```

views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
        # 페이지를 render
    return render(request, 'articles/index.html')

def new(request):

  return render(request, 'articles/new.html')

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')
```

new.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
    <h1>글쓰기</h1>
  <form action="{% url 'articles:create' %}">
    <label for="title">제목 : </label>
    <input type="text" name="title" id='title'>
    <label for="title">내용 : </label>
    <textarea name="content" id='content' cols='30' rows=10></textarea>
    <input type="submit" value='글쓰기'>
  </form>
</body>

</html>
```

- `{% csrf_token %}` : CSRF 공격을 방어하기 위해 POST 요청에 대해서만 csrf token을 발급하고 체크 

```html
<!-- articles/templates/articles/index.html -->
{% extends 'base.html' %}
{% block content %}
<h1>게시판 목록</h1>
<a href="{% url 'articles:create' %}">글쓰기</a>
{% endblock %}
```

```html
<!-- articles/templates/articles/create.html -->
{% extends 'base.html' %}

{% block content %}
<h1>글쓰기</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ article_form.as_p }}
  <input type="submit" value="글쓰기">
</form>
{% endblock %}
```

- HTML Form 태그 활용시 핵심
  - 어떤 필드를 구성할 것인지(`name`, `value`)
  - 어디로 보낼 것인지(`action`, `method`)

```python
# articles/views.py
def create(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context)
```

#### 2. 읽기(Read)

* 게시글을 가져와서 템플릿에 전달

views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
      # 게시글을 가져와서
      articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
        # 페이지를 render
    return render(request, 'articles/index.html')

def new(request):

  return render(request, 'articles/new.html')

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')
```

<br>

index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
    <h1>게시판</h1>
    <a href="{% url 'articles:new' %}">글쓰기</a>
  {% for article in articles %}
  <h3>{{ article.title}}</h3>
  <p>{{ article.created_at}} | {{ article.updated_at}}</p>
  <hr>
  {% endfor %}
</body>

</html>
```

```python
# articles/views.py
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

```html
<!-- articles/templates/articles/detail.html -->
{% extends 'base.html' %}

{% block content %}
<h1>게시판 목록</h1>
{% for article in articles %}
<p>{{ article.title }}</p>
{% endfor %}
{% endblock %}
```

## Django ModelForm

* DB기반의 애플리케이션을 개발하다보면,  HTML Form(UI)은 Django 모델(DB)과 매우 밀접한 관계를 가지게 됨
  * 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  * 즉, 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정됨
* 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며 이는 서버 사이드에서 반드시 처리해야함.

forms.py 생성

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

  class Meta:
    model = Article
    fields = '__all__'
    # fields = ['title', 'content'] 필요한것만 가져올 수 있음
```

<br>

views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
      # 게시글을 가져와서
      articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
        # 페이지를 render
    return render(request, 'articles/index.html')

#def new(request):
#  article_form = ArticleForm()
#  context = {
#    'article_form' : article_form
#  }
#  return render(request, 'articles/new.html', context=context)

# new를 제거하고 create에서 전부 처리 가능
def create(request): # 유효성 검사도 가능
  if request.method == 'POST':
      article_form = ArticleForm(request.POST)
      if article_form.is_valid():
        article_form.save()
        return redirect('articles:index')
  else:
    # 유효하지 않을때
    article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

<br>

new.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
    <h1>글쓰기</h1>
  <!-- method를 POST로 변경 -->
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <!-- 기존의 form을 대체할 수 있다 -->
    {{ article_form.as_p }}
</body>

</html>
```

<br>

#### 3. read - 상세보기

url.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  # path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
]
```

views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
      # 게시글을 가져와서
      articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
        # 페이지를 render
    return render(request, 'articles/index.html')

#def new(request):
#  article_form = ArticleForm()
#  context = {
#    'article_form' : article_form
#  }
#  return render(request, 'articles/new.html', context=context)

# new를 제거하고 create에서 전부 처리 가능
def create(request): # 유효성 검사도 가능
  if request.method == 'POST':
      article_form = ArticleForm(request.POST)
      if article_form.is_valid():
        article_form.save()
        return redirect('articles:index')
  else:
    # 유효하지 않을때
    article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)

def detail(request):
  article = Article.onjects.get(pk=pk)
  context = {
    'article' : article
  }
  return render(request, 'articles/detail.html', context)
```

detail.html

```python
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
    <h1>{{ article.pk }}번 게시글</h1>
  <p>{{ article.created_at }} | {{ article.updated_at}}</p>
  <p>{{ article.content }}</p>
  <a href="{% url 'article:update' article.pk %}">수정하기</a>
</body>

</html>
```

<br>

#### 수정하기(Update)

urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  # path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/update/', views.update, name='update'),
]
```

<br>

views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
      # 게시글을 가져와서
      articles = Article.objects.order_by('-pk')
    # template에 전달한다
    context = {
      'articles' : articles
    }
        # 페이지를 render
    return render(request, 'articles/index.html')

#def new(request):
#  article_form = ArticleForm()
#  context = {
#    'article_form' : article_form
#  }
#  return render(request, 'articles/new.html', context=context)

# new를 제거하고 create에서 전부 처리 가능
def create(request): # 유효성 검사도 가능
  if request.method == 'POST':
      article_form = ArticleForm(request.POST)
      if article_form.is_valid():
        article_form.save()
        return redirect('articles:index')
  else:
    # 유효하지 않을때
    article_form = ArticleForm()
  context = {
      'article_form': article_form
  }
     return render(request, 'articles/new.html', context=context)

def detail(request):
  article = Article.onjects.get(pk=pk)
  context = {
    'article' : article
  }
  return render(request, 'articles/detail.html', context)

def update(request, pk)
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    # POST : input 값 가져와서 검증하고 DB에 저장
    article_form = ArticleForm(request.POST, instance=article) # 특정한 글을 수정하는 것이기 때문에 인스턴스를 반드시 넘겨주어야 함
    if article_form.is_valid():
      # 유효성 검사 통과하면 저장하고 상세보기 페이지로 
      article_form.save()
      return redirect('articles:detail', article.pk)

  else:
      article_form = ArticleForm(instance=article)
  context = {
    'article_form' : article_form
  }
  return render(request, 'artitle/update.html', context)
```

<br>

update.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
    <h1>글 수정하기</h1>
  <form action="{% url 'articles:update' %}" method="POST"></form>
  {{ article_form.as_p }}
  <input type="submit" value="수정하기">
  </form>
</body>

</html>
```
