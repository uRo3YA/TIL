import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 1. Artist 생성
import datetime 
artist = Artist() 
artist.name = '아이브'
# 2021년 12월 1일
artist.debut = datetime.date(2021, 12, 1)
artist.save()

artist = Artist() 
artist.name = '아이유'
artist.debut = '2019-12-26'
artist.save()

director=Director()
director.name="봉준호"
director.debut="1993-01-01"
director.country="kor"
director.save()
director=Director()
director.name="김한민"
director.debut="1999-01-01"
director.country="KOR"
director.save()
director=Director()
director.name="최동훈"
director.debut="2004-01-01"
director.country="KOR"
director.save()
director=Director()
director.name="이정재"
director.debut="2022-01-01"
director.country="KOR"
director.save()
director=Director()
director.name="이경규"
director.debut="1992-01-01"
director.country="KOR"
director.save()
director=Director()
director.name="한재림"
director.debut="2005-01-01"
director.country="KOR"
director.save()
director=Director()
director.name="Joseph Kosinski"
director.debut="1999-01-01"
director.country="KOR"
director.save()
director=Director()
director.name="김철수"
director.debut="2022-01-01"
director.country="KOR"
director.save()


genre=Genre()
genre.title="액션"
genre.save()
genre=Genre()
genre.title="드라마"
genre.save()
genre=Genre()
genre.title="사극"
genre.save()
genre=Genre()
genre.title="범죄"
genre.save()
genre=Genre()
genre.title="스릴러"
genre.save()
genre=Genre()
genre.title="SF"
genre.save()
genre=Genre()
genre.title="무협"
genre.save()
genre=Genre()
genre.title="첩보"
genre.save()
genre=Genre()
genre.title="재난"
genre.save()

# 실습 5번
for i in range(len(Director.objects.all())):
    temp = []
    temp.append(Director.objects.all()[i].name)
    temp.append(Director.objects.all()[i].debut)
    temp.append(Director.objects.all()[i].country)
    print(*temp)
# 실습 6번
dir_id1 = Director.objects.get(id=1)
print(dir_id1.name, dir_id1.debut, dir_id1.country)

# 실습 7번
Director.objects.get(country = 'USA')

# 실습 9번
jk = Director.objects.get(name = 'Joseph Kosinski')
jk.country = 'USA'
jk.save()

jk = Director.objects.get(name='Joseph Kosinski')
print(jk.name, jk.debut, jk.country)

# 실습 10번
Director.objects.get(country = 'KOR')

# 실습 12번
c_kr = Director.objects.filter(country = 'KOR')
for i in range(len(c_kr)):
    print(c_kr[i].name, c_kr[i].debut, c_kr[i].country)

# 실습 14번
kcs=Director.objects.get(name="김철수")
kcs.delete()

# 실습 15번
dic = Director.objects.filter(name='봉준호').values()[0]
for k in dic:
    print(f'{k}: {dic[k]}')

# 전체 데이터 출력
for obj in Director.objects.all().values():
    for o in obj:
        print(obj[o])
    print()

####
for obj in Director.objects.all().values():
    l = [*obj]
    for field in l:
        print(obj[field])
    print()