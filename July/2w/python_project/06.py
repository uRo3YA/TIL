# - 영화 데이터 `movies.json` 와 `genres.json` 을  활용하여 필요한 정보로만 구성된 리스트를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.
#     - 개별 영화 정보는 id, title, vote_average, overview, genre_names로 결과를 만듭니다.
#         - genre_names는 키로, 각 장르 정보를 값으로 가집니다.
#         - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.
import json
from pprint import pprint


def movie_info(movies, genres):
    result = []
    genre_id_name = {}

    for d in genres :
        genre_id_name[d['id']] = d['name']
    
    for i in range(len(movies)) :
        genre_name = []
        for j in movies[i]['genre_ids'] :
            genre_name.append(genre_id_name[j])
        movies[i]['genre_names'] = genre_name

    for d in movies :
         temp = {}
         temp['genre_names'] = d['genre_names']
         temp['id'] = d['id']
         temp['overview'] = d['overview']
         temp['title'] = d['title']
         temp['vote_average'] = d['vote_average']
         result.append(temp)
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('2회차\이태극\data\movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('2회차\이태극\data\genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
    