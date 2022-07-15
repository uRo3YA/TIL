import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    moive_info_dict={}
    genre_id_name={}
    get_id=0
    for d in genres :
        genre_id_name[d['id']] = d['name']
    genre_name = []
    for id in movie['genre_ids'] :
        genre_name.append(genre_id_name[id])
    moive_info_dict['genre_names'] = genre_name
    # for i in range(len(genres)):
    #     if genres[i].get('id') == 80:
    #         g_list.append(genres[i].get('name'))
    #     if genres[i].get('id') == 18:
    #         g_list.append(genres[i].get('name'))
    #moive_info_dict['genre_names']=g_list
    moive_info_dict['id'] = movie["id"]     
    moive_info_dict['overview']=movie["overview"]
    moive_info_dict['title']=movie['title']
    moive_info_dict['vote_average']=movie['vote_average']
    # 여기에 코드를 작성합니다.  
    return moive_info_dict    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('2회차\이태극\data\movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('2회차\이태극\data\genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)
 
    pprint(movie_info(movie, genres_list))