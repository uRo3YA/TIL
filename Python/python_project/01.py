import requests


def popular_count():
    pass 
    base_url= 'https://api.themoviedb.org/3'
    path='/movie/popular'
    prams = {
       'api_key': '{본인의 api 키}',
        'language': 'ko-KR',
        #'page':'20'
    }
    res=requests.get(base_url+path,params=prams)
    data = res.json()
    result = len(data['results'])
      

    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
