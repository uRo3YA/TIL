# 예제 03 [오류 해결] 입력 받기
# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Input
# 10 20
# Output

### 오류 코드
# TypeError 
# 입력이 문자 형태의 리스트로 받아 sum 함수 작동하지 않음
#numbers = input().split()
numbers = map(int,input().split())
print(sum((numbers)))

# 예제 04. [오류 해결] 입력 받기 - 2
# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Input
# I'm Tuotur 6
# Output
# ["I'm", 'Tutor', '6']


### 오류 코드
# ValueError
# map(int)는 정수 형태로 매핑하기 때문에
#문자열 입력을 받을수 없다
#words = list(map(int, input().split()))
words = list(input().split())
print(words)

# 예제 05. [오류 해결] 숫자의 길이 구하기
# 아래 코드는 수의 자릿수를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# Output
# 8
### 오류 코드
# TypeError: object of type 'int' has no len()
# len 함수는 문자열만 인식하기 때문에 입력받은 정수를 문자열로 치환하거나
# 10으로 나누는 반복문을 통해서 자릿수를 계산하여 반환한다. 

def what_length(n):
    ans = 0
    while n:
        n //= 10
        ans += 1
    return ans
number = 22020718
print(what_length(number))
#print(len(number))

# 예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기
# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요. 
#  Output
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 오류 코드
# AttributeError: 'tuple' object has no attribute 'append'
# 문제에서 answer는 튜플형태이다.
# 튜플은 생성 후 요소의 값이나 튜플의 크기를 변경할 수 없기 때문에 answer를 리스트형태로 바꿔준다.

N = 10
answer = []
#answer = ()
for number in range(N + 1):
    answer.append(number * 2)
print(answer)

# 예제 07. [오류 해결] 평균 구하기
# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Ouput
# 5
# 오류코드 
# count가 반복문 밖에 있었기 때문에 
# 한번만 실행되었다.
# 따라서 count를 반복문 안쪽으로 들여쓰기를 한다.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
count = 0
for number in number_list:
    total += number
#count += 1
    count += 1
print(total // count)
 

# 예제 08. [오류 해결] 과일 개수 구하기
# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output
# 3
### 오류 코드
# char == "a" or "e" or "i" or "o" or "u"는 a를 제외한 나머지값은 판별이 생략되어 
# 오류가 발생한다.
word = "HappyHacking"
count = 0
for char in word:
    if char == "a" or char == "A":
        count += 1
    elif char == "e" or char == "E":
        count += 1
    elif char == "i"or char == "I":
        count += 1
    elif char == "o"or char == "O":
        count += 1
    elif char == "u"or char == "U":
        count += 1
print(count)

# 예제 09. [오류 해결] 과일 개수 구하기
# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
### Output
# {'Apricot': 1,
#  'Blackcurrant': 1,
#  'Cantaloupe': 1,
#  'Feijoa': 1,
#  'Grapefruit': 1,
#  'Juniper berry': 1,
#  'Salal berry': 1,
#  'Soursop': 1}
### 오류 코드
# fruit_count = {fruit: 1}는 전체 딕셔너리를 선언하기때문에
# 반복문이 실행되고 가장 마지막 요소인 {'Salal berry': 1}가 입력 된다.
from pprint import pprint
fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]
fruit_count = {}
for fruit in fruits:
    if fruit not in fruit_count:
        #fruit_count = {fruit: 1}
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 예제 10. [오류 해결] 더 큰 최댓값 찾기
# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요. 
### Output
#두 번째 리스트의 최댓값이 더 큽니다.
### 오류 코드
#max = max(number_list)에서 max는 내장 함수이기때문에 따로 선언을 하게 된다면
#이후 선언하는 max는 사용 할 수 없다. 

number_list = [1, 23, 9, 6, 91, 59, 29]
#max = max(number_list)
max1 = max(number_list)
number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)
if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")
elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")
else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")



# 예제 11. [오류 해결] 영화 정보 찾기

# 아래 코드는 영화의 장르id를 장르 이름으로 바꿔서 영화 정보를 출력하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
### 오류 코드
# def movie_info의 함수를 선언하였지만
# return 값을 선언 하지 않았기 때문에 실행시 기본값인 None를 반환하였기 때문이다.

from pprint import pprint

def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }
    return new_movie_info

if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))



# 문제 19. 숫자의 길이 구하기
# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수 number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지
# Input
# 123
# Output
# 3
def what_length(x):
    x=int(x)
    ans=0
    while x:
        x//=10
        ans+=1
    return ans
n=123
print(what_length(n))