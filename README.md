#git 연습
git으로 SSAFY 컴과 집 컴 동기화 하기

## 1. 대원칙
진실은 github에 존재
언제나 github에 있는 코드를 중심으로 생각
github를 중심으로 싱크를 맞춘다.

## 2. branch
브랜치 만들기

`$ git branch` :모든 브랜치를 보여준다.

* master

`$ git branch [새로운 브랜치 이름] :` 새 브랜치 생성                                                                                                              

`  heko                                                                                                                                

- master                                                                                                                              `

`$ git checkout` 브랜치간 이동, 커밋간 이동

git checkout [브랜치 이름] : 해당 브랜치로 이동

student@M70213 MINGW64 ~/git_practice (master)                                                                                        
$ git checkout heko                                                                                                                   
Switched to branch 'heko'                                                                                                             
A       README.md                                                                                                                     
student@M70213 MINGW64 ~/git_practice (heko)                                                                                          
$           