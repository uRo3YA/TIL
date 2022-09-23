
import random
from django.shortcuts import render

# Create your views here.
# view-> 템플릿 파일지정
def index(request):

    return render(request, 'index.html')

def todaybeer(request):
    beer_list=[
        {"name":"테라","src":"" },
        {"name":"카스","src":"" },
        {"name":"하이트","src":"" },
    ]
    context={
        "beer":random.choice(beer_list)
    }
    return render(request, 'todaybeer.html',context)

def lotto(request):
    lotto_list=[]
    for i in range(5):
        lotto=sorted(random.sample(range(1,46),6))
        lotto_list.append(lotto)
    
    context={
        'lotto_list':lotto_list
    }
    return render(request, 'lotto.html',context)
