# Git 기본기

- **README.md**

프로젝트에 대한 설명 문서

프로젝트에서 가장 먼저 보는 문서

일반적으로 소프트웨어와 함께 배포

작성 형식은 따로 없으나 마크다운으로 작성

- **Repository**

특정 디렉토리를 버전 관리하는 저장소

git init 명령어로 로컬 저장소를 생성

.git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

 
 
git init 하면

.git 폴더는 숨김 폴더로 생성

ls -a 명령어로 확인 가능하나 보이지는 않는다

절대로 루트 디렉토리에는 git init을 하면 안된다

- **초기 설정**

특정 버전을 남긴다 = “커밋(Commit)” 한다

Working Directory(w.d) :  내가 작업하고 있는 실제 디렉토리, 버전을 기록하기 전에 변화를 만드는 곳 (프로젝트를 개발할때 새로운 기능 추가.. 수정..)

Staging Area : 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

Repository : 커밋들이 저장되는곳

커밋은 이 3가지 영역을 바탕으로 동작


git status : 상태 보여준다

git add . : 추적 되지 않은 파일 Staging Area에 올려줌



git commit -m ‘ initial commit’ : ‘ initial commit’ 으로 올려줘~

이것만 하면 너가 누군데! 하고 안올랴줌

github 가입

git config —global user.name 닉네임

git config —global user.email 이메일

해서 닉네임과 이메일 등록

VS code에서 터미널로 git bash 사용 가능 (git init 설정한 폴더로 경로 잡아줘야 한다.)



git add와 git commit 입력한 커밋 완료 화면

루트커밋은 레포지터리가 만들어졌을때 최초의 커밋이다.

루트 커밋이 있어야만 업로드가 된다. 

파일을 갱신하고 저장해서 git add 를 해주어야 한다. 

git log 로 수정내용 확인 가능

우리가 커밋을 하는 것은 기능 단위다.



staging area에서 커밋할 것과 안할 것을 구분한다

미완성된것은 커밋으로 남기지 않는다.

remote repository

내가 소유한 remote를 보통 origin 이라고 함.

git remote ~~~ 원격 저장소 관련 세팅 명령어

gir remote add origin 주소 : 원격 저장소 설정s

git remote -v : 지금 어디가 원격 저장소인지 확인

git log —oneline : 상태 한줄로 알려줌

git push -u origin master : 원격 저장소에 푸시

단어 앞글자만 치고 탭 누르면 자동완성
설정 끝

연결이 되어 있으니까 이제는 git push 만 쳐도 자동으로 알아서 올라간다.



git clone 원격 저장소 주소

깃 저장소에 있는 것 다운로드 받음

* 자격증명
컴퓨터에 자격 증명이 저장되어있음

컴퓨터를 옮길 때 제거 해줘야 함.

- 설정 끝

연결이 되어 있으니까 이제는 git push 만 쳐도 자동으로 알아서 올라간다. 

1. 로컬 생성
2. root commit
3. remote repo 만들기
4. remote add .
5. git push


# 깃을 이용한 협업 체험

- shared repository
    - git remote add origin 주소 에서 origin이 권한
    

git commit 했는데 변화 없을 때 : 오타 아니면 저장 안한 거

vim 파일 : 파일 여는것

wq : 파일에서 빠져나오기