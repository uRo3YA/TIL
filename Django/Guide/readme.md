# 빠른 시작을 위한 Django 프로젝트 기본 가이드
## 프로젝트 시작
```python
# 가상환경 생성
python -m venv venv
```

```python
# 가상환경 실행
. venv/scripts/active
```

```python
# 미리 준비된 패키지 일괄 설치
pip instrall -r requirements.txt
```

```python
django-admin startproject pjt . #pjt는 프로젝트명
```

```python
python manage.py startapp {app name} # 프로젝트 내부 각 앱마다 생성
```

프로젝트 기본 템플릿 폴더

```bash
#pjt/templates
base.html # 각 페이지의 기본 바탕이 되는 기초 페이지
root.html # 루트 페이지 http://127.0.0.1:8000/
```

프로젝트 기본 설정

```python
#pjt/setting.py
# 보안을 위한 SECRET_KEY 분리
import os, json
from django.core.exceptions import ImproperlyConfigured

...


secret_file = os.path.join(BASE_DIR, "secrets.json")  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

# 상위 폴더의 secrets.json에 생성된 SECRET_KEY를 딕셔너리 형태로 저장
# secrets.json은 gitignore로 설정해서 업로드 안되게 하자
```

앱 설정

```python
#pjt/setting.py
INSTALLED_APPS = [
    "articles", # 생성한 앱1
    "accounts", # 생성한 앱2
    "django_bootstrap5", # 부트스트랩을 적용시켜주자
    ...
```

부트스트랩 확장을 위한 설정

```
#pjt/setting.py
TEMPLATES = [
            ...
             "DIRS": [BASE_DIR / "pjt" / "templates"],
            ...
```

시간대 설정

```python
#pjt/setting.py
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

커스텀 유저 Auth 설정

```python
#pjt/setting.py
AUTH_USER_MODEL = "accounts.User"
```

프로젝트 URL 설정

```python
#pjt/urls.py
from . import views
...
from django.urls import path, include

...
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.root), # 루트 페이지 호출
    # 프로젝트 내부의 각 앱들 마다 설정
    path("articles/", include("articles.urls")),
    path("accounts/", include("accounts.urls")),
]
```

## accounts 앱

user 생성, 그 리스트, user의 상세 정보를 출력
``` bash
accounts
├── templates/accounts
│   			├── index.html  # 생성된 user 리스트 출력
│   			├── signup.html # user 생성
│   			└── detail.html # user의 상세 정보 출력
```
admin 설정
```python
#accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(get_user_model(), UserAdmin)
```
user 생성을 위한 입력 form 설정 
```python
#accounts/forms.py
# from .models import User
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
        )

```
DB에 저장 하기 위한 데이터 형식 설정
```python
#accounts/models.py
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

```

accounts 앱을 표시 위한 URL 설정
```python
#accounts/urls.py
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("<int:pk>/", views.detail, name="detail"),
]

```
accounts 앱을 구동을 위한 view 설정
```python
#accounts/views.py
from django.shortcuts import render, redirect


# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import User

# from .models import User
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    users = User.objects.all()
    # Template에 전달한다.
    context = {"users": users}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)

```


