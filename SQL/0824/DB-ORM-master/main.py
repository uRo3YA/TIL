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


### 8월 25일 실습
# 3번
directors = [
    ("봉준호","1993-01-01","KOR"),
    ("김한민","1999-01-01","KOR"),
    ("최동훈","2004-01-01","KOR"),
    ("이정재","2022-01-01","KOR"),
    ("이경규","1992-01-01","KOR"),
    ("한재림","2005-01-01","KOR"),
    ("Joseph Kosinski","1999-01-01","KOR"),
    ("김철수","2022-01-01","KOR"),
]

for director in directors:
    name_ = director[0]
    debut_ = director[1]
    country_ = director[2]
    Director.objects.create(name=name_, debut=debut_, country=country_)

genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

## 4번
dic = Director.objects.filter(name='봉준호').values()[0]
for k in dic:
    print(f'{k}: {dic[k]}')
## 5번 
gen = Genre.objects.get(title='드라마')
print("id:",gen.id)
print("title:",gen.title)

## 6번
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')
movie = Movie()
data= ("봉준호",  "드라마" , "기생충" , "2019-05-30" , 132  ,False )
movie_title=data[2]
movie_opening_data=data[3]
movie_running_time=data[4]
movie_screening_=data[5]
movie.director=director_
movie.genre=genre_
movie.title=movie_title
movie.opening_date=movie_opening_data
movie.running_time=movie_running_time
movie.screening=movie_screening_
movie.save()


## 7번
movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for data in movies:
    movie = Movie()
    director_ = Director.objects.get(name=data[0])
    genre_ = Genre.objects.get(title=data[1])
    movie_title=data[2]
    movie_opening_data=data[3]
    movie_running_time=data[4]
    movie_screening_=data[5]
    movie.director=director_
    movie.genre=genre_
    movie.title=movie_title
    movie.opening_date=movie_opening_data
    movie.running_time=movie_running_time
    movie.screening=movie_screening_
    movie.save()

## 8번
for obj in Movie.objects.all():
    print(obj.director,
    obj.genre, 
    obj.title,
    obj.opening_date, 
    obj. running_time,
    obj.screening )
## 9번
for obj in Movie.objects.all():
    print(obj.director.name,
    obj.genre, 
    obj.title,
    obj.opening_date, 
    obj. running_time,
    obj.screening )

## 10번
for obj in Movie.objects.all():
    print(obj.director.name,
    obj.genre.title, 
    obj.title,
    obj.opening_date, 
    obj. running_time,
    obj.screening )
## 11번 
for obj in Movie.objects.all().order_by('-opening_date'):
    print(obj.director.name,
        obj.genre.title, 
        obj.title,
        obj.opening_date, 
        obj. running_time,
        obj.screening )
## 12번
obj=Movie.objects.all().order_by('opening_date')[0]
print(obj.director.name,
    obj.genre.title, 
    obj.title,
    obj.opening_date, 
    obj. running_time,
    obj.screening )
## 13번
for obj in Movie.objects.all().order_by('opening_date'):
    if obj.screening == True:
        print(obj.director.name,
            obj.genre.title, 
            obj.title,
            obj.opening_date, 
            obj. running_time,
            obj.screening )
## 14번
for obj in Movie.objects.all().order_by('opening_date'):
    if obj.director.name== "봉준호":
        print(obj.director.name,
            obj.genre.title, 
            obj.title,
            obj.opening_date, 
            obj. running_time,
            obj.screening )
## 15번
b_id=Director.objects.get(name="봉준호").id
obj=Movie.objects.filter(director=b_id).order_by('opening_date')[1]
print(obj.director.name,
        obj.genre.title, 
        obj.title,
        obj.opening_date, 
        obj. running_time,
        obj.screening )

## 16번
for obj in Movie.objects.all().order_by('running_time'):
    if obj.running_time>119:
        print(obj.director.name,
            obj.genre.title, 
            obj.title,
            obj.opening_date, 
            obj. running_time,
            obj.screening )
## 17번
for obj in Movie.objects.all().order_by('running_time'):
#for obj in Movie.objects.filter(running_time__gte=119).order_by('running_time')
    if obj.running_time>=119:
        print(obj.director.name,
            obj.genre.title, 
            obj.title,
            obj.opening_date, 
            obj. running_time,
            obj.screening )
## 18번
for obj in Movie.objects.filter(opening_date__gte="2022-01-01").order_by('opening_date'):
        print(obj.director.name,
            obj.genre.title, 
            obj.title,
            obj.opening_date, 
            obj. running_time,
            obj.screening )
## 19번
b_id=Director.objects.get(name="봉준호").id
drama_id=Genre.objects.get(title="드라마").id
for obj in Movie.objects.filter(director=b_id,genre=drama_id).order_by('opening_date'):
            print(obj.director.name,
            obj.genre.title, 
            obj.title,
            obj.opening_date, 
            obj. running_time,
            obj.screening )

## 20번
b_id=Director.objects.get(name="봉준호").id
for obj in Movie.objects.exclude(director=b_id).order_by('opening_date'):
            print(obj.director.name,
            obj.genre.title, 
            obj.title,
            obj.opening_date, 
            obj. running_time,
            obj.screening )