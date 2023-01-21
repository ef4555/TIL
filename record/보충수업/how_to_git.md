# git 시작하기

1. 환경 설정
   1. 누가 커밋(파일 수정 또는 생성, 삭제 등등..)을 했는지 알아볼수 있도록 초기에 설정

```
git config --global user.name ""
git config --global user.email ""
```

올바르게 설정되었는지 확인

```
git config --global -list
```

1. Working Directory : 사용자의 일반적인 작업이 일어나는곳
2. Staging Area : 커밋을 위한 파일 및 폴더가 추가되는곳
3. Repository : staging area 에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는곳
4. 1 => 2 => 3 의 과정으로 버전관리를 수행한다.

```
git init
```

현재 작업하고 있는 경로(디렉토리)를 버전관리로(git 으로 관리) 하겠다. 라는 의미

주의사항

1. 이미 git 저장소인 폴더 내에 또 다른 git 저장소를 만들면 안된다.(중첩 금지)
   1. 터미널에 master 표시가 있다면 git init 명령어를 입력하면 안된다.
2. 홈 디렉토리에서 git init 을 하지 않는다. 터미널의 경로가 ~ 인지 확인합니다.

```
git status
```
현재 저장소의 상태를 파악하는 명령어


```
git add .
git add "파일이름"
```

현재 작업 경로(working directory)에 있는 내용(파일)들을 staging area로 올리는 명령어

git이 해당 파일을 추적(관리)할 수 있도록 만들어준다.


```
git commit -m "커밋 메시지"
```

staging area에 올라온 파일의 변경사항을 하나의 버전(커밋)으로 저장하는 명령어

```
git log
```

커밋 내역을 조회할수 있는 명령어


아래 명령어를 실행하기 전에 github나 gitlab을 이용해서 원격 저장소를 만들어야 한다.

```
git remote add origin "레포지토리 주소"
```

컴퓨터의 로컬저장소(working directory)와 원격 저장소를 연동하는 명령어


```
git push origin master
```

컴퓨터의 커밋내역을 원격 저장소(레포지토리)에 업로드하는 명령어


```
git clone "레포지토리 주소"
```

다른 컴퓨터에서 원격 저장소의 내용을 복사하고 싶을때

이 명령어를 실행하면 실행 당시 있었던 커밋내역을 해당 디렉토리에 복사


```
git pull origin master
```
원격 저장소에 새로 올라온 변경 내역을들을 현재 로컬저장소에 업데이트


## 만약 내가 해당 경로에 버전관리하고 싶지 않은 폴더가 있다면??

.gitignore

파일 이름이 없고 확장자가 .gitignore

쉽게 만드는 방법

gitignore.io