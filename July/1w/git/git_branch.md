
1. 브랜치 기초

가지치기를 하기 전에 나무의 뿌리(루트 커밋)를 만들어 주는 과정이 필요하다.

따라서 아래 명령어를 순차적으로 입력해준다.
git init, 

touch README.md, 

git  add .

git commit -m 'Init'

*master: 기준이 되는 뿌리 브랜치



git branch : 현재 '브랜치 조회'

git branch example : example 이라는 이름의 '브랜치 생성'

git checkout example : '브랜치 변경'

작업이 다 끝나면 git status 로 확인

git add . 

git commit -m '변경 내용'

git log --oneline

이 상태에서 git checkout master 명령어로 브랜치 이동

git log --oneline 으로 재확인하면

example 브랜치에서 작성했던 커밋이 사라져있는 것을 확인

*HEAD: 현재 위치하게 된 브랜치를 알려줌



병합하기

git checkout master :기준이 되는 브랜치로 이동

git merge example

git log --oneline 으로 HEAD의 흐름이 어떻게 생겼는지 확인



브랜치 지우기

git branch -d example 

*브랜치를 지워도 지운 브랜치에서 작업했던 커밋이 지워지는 것은 아니다(master에 붙였기 때문)

*실제로 개발할 때 merge 가 완료된 브랜치는 지워버린다



2. 깃헙

*브랜치 이름은 개발을 담당한 사람보단, 기능 이름을 주로 적는다

깃헙으로 merge 작업을 수행했다면, 로컬에서는 별도로

merge 작업을 더하지 않아도 된다.

다만 깃헙에서 merge 해버리면 불필요해진 브랜치는 직접 지워야된다.



컨트롤 l 터미널 정리



과제: 리드미에 수업후기 작성해서 넣어주세요

```bash
$ git push origin example
# 위와 같이 입력했는데 깃헙에 반영이 안된다면,
# 로컬에서 remote: 부분에 뜬 url을 컨트롤+클릭하면 됨!
```



💡특정 파일에 대한 add 만 취소하고 싶다면?

예시) png 파일, exe 파일을 함께 add 해버렸는데

.exe 에 대한 add 를 취소하고 싶을 때

```bash
$ git restore --staged f.exe
```



💡마크다운 보고서를 저장하지 않았는데, 내용이 지워져있을 때

어떻게 복구해야할까?

커밋, 푸시, 풀 아무것도 안한 상황

```bash
$ git status : 파일이 modified 되었는지 먼저 확인
$ git restore 파일명 : modified 이전 상태로 복구해줌
```

