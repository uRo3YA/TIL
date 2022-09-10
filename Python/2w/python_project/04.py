# - 영화 데이터 `movie.json` 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - `id`, `title`, `vote_average`, `overview, genre_ids`으로 구성된 결과를 만듭니다.

import json
from pprint import pprint


def movie_info(movie):
    #pass 
    # 여기에 코드를 작성합니다.
    movie_dict={}
    movie_dict['genre_ids']=movie["genre_ids"]
    movie_dict['id'] = movie["id"]     
    movie_dict['overview']=movie["overview"]
    movie_dict['poster_path']=movie['poster_path']
    movie_dict['title']=movie['title']
    movie_dict['vote_average']=movie['title']
    #print(id)
    return movie_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('July/2w/python_project/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
   
    pprint(movie_info(movie))