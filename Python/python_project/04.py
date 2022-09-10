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
        for i in range(len(results)):
            movie_id=results[0].get("id")
        #movie_id=results[0].get("id")
        return movie_id
            

def recommendation(title):
    pass 
    movie_id=search(title)
    if movie_id == None:
         return None
    base_url= 'https://api.themoviedb.org/3'
    path=f'/movie/{movie_id}/recommendations'
    prams = {
                   'api_key': '{본인의 api 키}',
                    'language': 'ko-KR', }
    res = requests.get(base_url+path, params=prams) 
    if res == None:
         return None
    else:
        data=res.json()
        results=data.get('results')
        movie_list=[]
        for result in results:
                movie=result.get("title")
                movie_list.append(movie)
        return movie_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
