# 파이썬 02

날짜: 2022년 7월 22일

# 파이썬 기반 데이터 활용

<aside>
💡 이번 프로젝트는 **개인 프로젝트**입니다.
프로젝트는 별도의 해설이 없으며, 공식 문서와 구글링 등을 자유롭게 활용하며 풀이를 합니다.

</aside>

<aside>
👉 프로젝트 완료 후 README.md에 아래의 내용을 작성합니다.
- 프로젝트에 대한 주요 코드 및 해설
- 배운점, 느낀점 등

커밋을 완료한 이후에 Pull Request를 하고 PR 링크를 Syllaverse에 제출합니다.

</aside>

[GitHub - kdt-hphk/01-PJT-02: [KDT1] 프로젝트 02](https://github.com/kdt-hphk/01-PJT-02)

## 프로젝트 안내

### 목표

- Python 기본 문법(조건문, 반복문) 활용
- Python 외부 라이브러리 활용
- API와 JSON 데이터의 활용

### 본 제공 소스코드

**프로젝트의 [README.md](http://README.md) 파일을 반드시 확인합니다**

```
N회차/
	홍길동/
		README.md
		problem_a.py
		problem_b.py
		...
```

### 개발 도구

- Visual Studio Code
- Python 3.9
- TMDB API [https://developers.themoviedb.org/3/getting-started/introduction](https://developers.themoviedb.org/3/getting-started/introduction)

## 00. API 문서와 requests 활용 (연습)

- 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 가격으로 출력하시오.
- [https://apidocs.bithumb.com/reference/현재가-정보-조회](https://apidocs.bithumb.com/reference/%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C)

### 결과 예시

```
30000000
```

## 01. 인기 영화 조회

- 인기 영화 목록의 개수를 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
- 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.

### 결과 예시

```json
20
```

## 02. 특정 조건에 맞는 인기 영화 조회

- 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
- 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.

### 결과 예시

**요청 시점에 따라 다른 결과가 나올 수가 있습니다.**

```json
[
    {
        "adult": false,
        "backdrop_path": "/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg",
        "genre_ids": [
            28,
            18
        ],
        "id": 361743,
        "original_language": "en",
        "original_title": "Top Gun: Maverick",
        "overview": "최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…",
        "popularity": 8058.252,
        "poster_path": "/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg",
        "release_date": "2022-05-24",
        "title": "탑건: 매버릭",
        "video": false,
        "vote_average": 8.4,
        "vote_count": 1620
    },
    {
        "adult": false,
        "backdrop_path": "/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg",
        "genre_ids": [
            28,
            12,
            878
        ],
        "id": 634649,
        "original_language": "en",
        "original_title": "Spider-Man: No Way Home",
        "overview": "미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 사상 최악의 위기를 맞게 되는데…",
        "popularity": 1513.591,
        "poster_path": "/voddFVdjUoAtfoZZp2RUmuZILDI.jpg",
        "release_date": "2021-12-15",
        "title": "스파이더맨: 노 웨이 홈",
        "video": false,
        "vote_average": 8.1,
        "vote_count": 14255
    }
]
```

## 03. 특정 조건에 맞는 인기 영화 조회

- 인기 영화 목록을 평점이 높은 순으로 5개의 정렬하여 영화 데이터 목록을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
- 응답 받은 데이터 중 평점(`vote_average`)이 높은 영화 5개의 정보를 리스트로 반환하는 함수를 작성합니다.

**TIP.** 정렬시 sorted 함수의 key를 활용합니다.

### 결과 예시

**요청 시점에 따라 다른 결과가 나올 수가 있습니다.**

```json
[
    {
        "adult": false,
        "backdrop_path": "/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg",
        "genre_ids": [
            28,
            18
        ],
        "id": 361743,
        "original_language": "en",
        "original_title": "Top Gun: Maverick",
        "overview": "최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…",
        "popularity": 8058.252,
        "poster_path": "/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg",
        "release_date": "2022-05-24",
        "title": "탑건: 매버릭",
        "video": false,
        "vote_average": 8.4,
        "vote_count": 1620
    },
	   // ... 생략
    {
        "adult": false,
        "backdrop_path": "/wNQpfAZkySbinb93qVwWIWaot1x.jpg",
        "genre_ids": [
            10402,
            14,
            35,
            878,
            10751,
            10770
        ],
        "id": 809107,
        "original_language": "en",
        "original_title": "Z-O-M-B-I-E-S 3",
        "overview": "올해는 제드와 애디슨에게 시브룩에서의 마지막 해이고, 시브룩은 몬스터와 인간에게 천국이 되었다. 제드는 좀비 최초로 대학에 입학하고자 풋볼 장학생이 되려고 애쓰고, 애디슨은 전국 응원 대회를 준비 중이다. 은하계 외부인들이 나타나 응원 대회에 출전하게 되자, 시브룩에서는 이들이 대회 출전보다 다른 속셈이 있을지도 모른다는 의심이 커져 간다.",
        "popularity": 1848.58,
        "poster_path": "/egX5gH8UmRl2eLL4EMbJfm5p05d.jpg",
        "release_date": "2022-07-09",
        "title": "좀비스 3",
        "video": false,
        "vote_average": 7.9,
        "vote_count": 86
    }
]
```

## 04. 영화 조회 및 추천 영화 조회

- 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
- 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
- 추천 영화 목록 중 첫번째 영화만 출력하는 함수를 작성합니다.

### 결과 예시

**요청 시점에 따라 다른 결과가 나올 수가 있습니다.**

```json
["조커", "1917", "조조 래빗", "원스 어폰 어 타임 인… 할리우드", "... 생략" ,"펄프픽션"]
```

## 05. 출연진 및 연출진 데이터 조회

- 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
- 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
- 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서가 `Directing` 인 데이터만 추출합니다.
- `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.

### 결과 예시

```json
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Jang Hye-jin'],
 'directing': ['Bong Joon-ho',
               'Park Hyun-cheol',
               'Han Jin-won',
               'Kim Seong-sik',
               'Lee Jung-hoon',
               'Yoon Young-woo']
}
```