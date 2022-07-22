import requests
from pprint import pprint

def search(title):
    movie_id=None
    base_url='https://api.themoviedb.org/3'
    path='/search/movie'
    prams = {
                   'api_key': '{본인의 api 키}',
                    'language': 'ko-KR', 
                    'query': f'{title}'}
    res=requests.get(base_url+path, params=prams) 
    if res == None:
         return None
    else:
        data = res.json()
        results=data.get('results')
        for _ in range(len(results)):
            movie_id=results[0].get("id")
        return movie_id

def credits(title):
    pass 
    movie_id=search(title)
    if movie_id == None:
         return None
    base_url='https://api.themoviedb.org/3'
    path=f'/movie/{movie_id}/credits'
    prams = {
                   'api_key': '{본인의 api 키}',
                    'language': 'ko-KR', 
                    }
    
    res=requests.get(base_url+path, params=prams)
    if res == None:
         return None
    data = res.json()
    cast=data.get("cast")
    crew=data.get("crew")
    return_data={"cast":[],"crew":[]}
    for baewoo in cast:
        if baewoo.get('cast_id')<10:
            return_data["cast"].append((baewoo.get('name')))
    for staff in crew:
        if staff.get('department')== "Directing":
            return_data["crew"].append(staff.get('name'))
    return(return_data)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
