import random
from django.shortcuts import render
from .models import Article

# Create your views here.
# view-> 템플릿 파일지정
def index(request):

    return render(request, "index.html")


def todaybeer(request):
    beer_list = [
        {"name": "테라", "src": ""},
        {"name": "카스", "src": ""},
        {"name": "하이트", "src": ""},
    ]
    context = {"beer": random.choice(beer_list)}
    return render(request, "todaybeer.html", context)


def lotto(request):
    lotto_list = []
    for i in range(5):
        lotto = sorted(random.sample(range(1, 46), 6))
        lotto_list.append(lotto)

    context = {"lotto_list": lotto_list}
    return render(request, "lotto.html", context)


def is_even_odd(request, _number):
    number = _number
    if _number % 2 == 0:
        p = "짝수"
    else:
        p = "홀수"
    context = {"number": number, "num": p}
    return render(request, "is-even-odd.html", context)


def calc(request, a, b):
    num1 = a
    num2 = b
    context = {
        "num1": num1,
        "num2": num2,
        "calc1": num1 + num2,
        "calc2": num1 - num2,
        "calc3": num1 * num2,
        "calc4": num1 // num2,
    }
    return render(request, "calc.html", context)


def pastlife(request):
    adj = [
        "좋은",
        "주제넘은",
        "줄기찬",
        "즐거운",
        "지나친",
        "지혜로운",
    ]
    ani = [
        "사슴",
        "늑대",
        "재규어",
        "알파카",
        "양",
        "다람쥐",
        "담비",
    ]
    context = {
        "name": request.GET.get("name"),
        "adj": random.choice(adj),
        "ani": random.choice(ani),
    }
    return render(request, "pastlife.html", context)


def krlipsum(request):
    return render(request, "krlipsum.html")


def krlipsum_output(request):
    cnt_para = int(request.GET.get("num1"))
    cnt_words = int(request.GET.get("num2"))

    # lorems = [[] for _ in range(cnt_para)]
    lorems = [[] for _ in range(cnt_para)]
    ran_words = [
        "바나나",
        "짜장면",
        "사과",
        "바나나",
        "딸기",
    ]

    for i in range(len(lorems)):
        while len(lorems[i]) < cnt_words:
            word = random.choice(ran_words)
            lorems[i].append(word)

    context = {"lorems": lorems}
    return render(request, "krlipsum_output.html", context)


# def geustbook(request):
#     geustbook = Article.objects.all()
#     return render(request, "geustbook.html", {"geustbook": geustbook})


def geustbook(request):
    geustbook = Article.objects.all()
    return render(request, "geustbook.html", {"geustbook": geustbook})


create_data = []


def create(request):

    content = request.GET.get("content")
    # create_data.append(content)
    # DB에 저장
    Article.objects.create(content=content)

    return render(request, "create.html", {"content": content})
