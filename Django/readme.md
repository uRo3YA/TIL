## Django

#### Framework = Frame(뼈대) + work(일하다)

* 서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것

<br>

#### IP와 도메인

- 네트워크에 연결돼있는 각각의 장치를 호스트(Host)라고 함
- 데이터를 요청받았을 때 그것에 응답하는 호스트가 `서버`이고, 데이터를 요청하는 호스트가 `클라이언트`

#####  IP

- 호스트가 다른 호스트와 데이터를 주고 받기 위해, 자신들을 구분하는 특수한 번호가 `IP주소`

    > Internet Protocol Address의 약자

- IP주소는 4개의 숫자와 점으로 이루어짐(IPv4)
- 각각의 숫자는 0 ~ 255 사이의 정수를 가짐 (각 숫자는 8비트로 표현해서 2^8 = 256을 의미)
- IPv4가 고갈되어 감에 따라 IPv6(2^128)로 전환 추세



- 흔히 웹 프로젝트 개발할때 내 컴퓨터를 서버로 설정해서 localhost로 접속하는데

  여기서 로컬 호스트는 `호스트 자기 자신을 가리키는 고유한 별칭`
     ```bash
    localhost:8000
    ```


##### 도메인

- 네이버 검색 포털을 이용한다고 했을 때 우리는 `https://www.naver.com`으로 접속함
- 여기서 `naver.com`부분을 도메인(Domain)이라고 함
- 우리가 문자열로 표현된 인터넷 주소로 웹사이트에 접속할 수 있는 것은, 웹 브라우저가 도메인과 연결되어 있는 IP 주소를 찾아서 이동

    > 이것을 도메인 네임 시스템(DNS)라고 하고, 도메인과 IP의 연결 정보가 있는 서버를 네임 서버(Name Server)
    >
    > 숫자들의 나열인 IP주소 보다는 의미가 있는 문자열을 사용하는 것이 편리하기 때문에 도메인의 개념이 생김


#### 클라이언트와 서버

* 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작
* 클라이언트에서 요청을 하면 서버에서 요청을 받고 응답을 하는 구조로 상호작용함
* 이 중에서 Django는 서버를 구현하는 웹 프레임워크 

<br>

#### 클라이언트

* 웹 사용자의 인터넷에 연결된 장치
* Chrome 또는 Firefox 와 같은 웹 브라우저
* 서비스를 요청하는 주체


<br>

#### 서버

* 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
* 클라이언트가 웹 페이지에 접근하려고 할 때 클라이언트 서버로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 포시됨
* 요청에 대해 서비스를 응답하는 주체
    - 서버가 서비스를 제공하기 위해서는 `서버 프로그램`이 있어야하고, 클라이언트가 서비스를 제공받으려면 서버 프로그램과 연결할 수 있는 `클라이언트 프로그램`이 존재해야함

- 연결 방식

  - 서버기반 모델(server-based model) : 전용 서버를 두는 것

    > 안정적인 서비스 제공이 가능
    >
    > 공유 데이터의 관리와 보안이 용이
    >
    > 서버구축비용과 관리비용이 든다는 단점 존재

  - P2P 모델(peer-to-peer model) : 별도의 전용 서버 없이 각 클라이언트가 서버역할을 동시에 수행하는 것

    > 서버 구축 및 운용 비용을 아낄 수 있음
    >
    > 자원의 활용을 극대화
    >
    > 자원 관리가 어려움
    >
    > 보안에 취약
<br>

## Web browser와 Web page

### 웹 브라우저란?

- 웹에서 페이지를 찾아서 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
- 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는 프로그램 : `렌더링(rendering)`

<br>

###  정적 웹 페이지

- Static Web page
- 있는 그대로를 제공하는 것(served as-is)
- HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것

<br>



#### 동적 웹 페이지

* Dynamic Web page
* 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
* 웹 페이지의 내용을 바꿔주는 주체 == 서버
  * 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
  * 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크가 Django


#### 정적 웹 사이트와 동적 웹 사이트의 차이점

- 정적 웹 페이지는 미리 저장된 파일(HTML 파일, 이미지, JS 파일 등)이 그대로 전달되는 웹 페이지
- 동적 웹 페이지는 데이터들을 스크립트에 의해 가공처리한 후 생성되어 전달되는 웹 페이지
- 정적 웹 페이지는 빠르고 비용이 적게 들지만(웹 서버만 구축하면 됨) 서비스가 한정적이고 관리가 어려움
- 동적 웹 페이지는 다양하고 관리가 쉽지만 상대적으로 속도가 느리고 추가적인 비용이 듦(웹 서버외에 추가적으로 처리를 위한 어플리케이션 서버가 필요)
- 요즘 대부분의 웹 사이트는 동적 웹 페이지를 사용하고 동적인 부분이 필요 없는 경우에는 정적으로 구현

    > DJango는 이런 동적 웹 페이지의 기능들을 빠르게 개발이 가능함

<br>

#### HTTP

- HTTP : HyperText Transfer Protocol
- HTML과 같은 문서를 전송하기 위한 프로토콜(규칙)
- HTTP 메시지에는 요청과 응답 유형이 존재
![HTTP_messages](https://i0.wp.com/hanamon.kr/wp-content/uploads/2021/06/HTTP_messages.png?resize=821%2C244&ssl=1)
    > <기본 구조>
    >
    > 1. Start line : 요청이나 응답의 상태를 나타냄, 항상 첫번째 줄에 위치
    > 2. HTTP headers : 요청을 지정하거나, 메시지에 포함된 본문을 설명하는 헤더의 집합
    > 3. empty line : 헤더와 본문을 구분하는 빈 줄
    > 4. body : 요청 / 응답과 관련된 데이터나 문서를 포함
    >


## Django 초기 설정 가이드  

<br>

### 서버용 폴더 생성
``` bash
mkdir server
cd server
```
### 가상환경 생성
``` bash
python -m venv [가상환경 이름]
```
### 가상환경 실행
```bash
source ./Scripts/activate
 ```
1. 가상환경 실행 확인
    ```bash
    (server-test) 
    ```

 2. 가상환경 종료는 어떻게 하는가?
    ```bash
    deactivate
    ```  



### Djanogo 설치
```bash
pip install requirements.txt # 일반적으로 업무시 필수요소들 모두 설치
pip install django==3.2.13 # Django만 설치
```
### 프로젝트 생성
```bash
django-admin startproject {mysite} .
```
### 앱 생성
``` bash
python manage.py startapp {app name}
```
### 앱 설정
- 생성한 프로젝트 내에서 setteing.py에서 INSTALLED_APPS에 생성한 {app name} 입력

### url 설정
- 프로젝트에서 url.py에서 설정
  ```python
    from random_game import views

    path('',views.index)
  ```
### view-> 템플릿 파일지정
1. app name 폴더 view.py
  ```python
  def index(request):

      return render(request, 'index.html')
  ```
2. app name  templates 폴더 생성
    - index.html 생성
### 모델 마이그레이션
```bash
python manage.py makemigrations

python manage.py migrate
```

### 서버 실행
``` bash
python manage.py runserver
```