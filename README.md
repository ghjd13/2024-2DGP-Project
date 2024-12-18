# 2024-2DGP-Project
게임의 간단한 소개 (카피의 경우 원작에 대한 언급)

    ○게임 컨셉, 핵심 메카닉 제시
    ○스크린샷 혹은 그림판으로 끄적인 이미지 포함

# 프로젝트 명: 무법 레이서
    
    게임 컨셉: NES의 f1 Race같은 고전 레이싱 게임
    
    배경: 80년대를 배경으로 경찰과 차들을 피해 도시를 향해 도망치는 차량을 주인공으로 하는 게임
    
 # 아이디어
    F1레이스NES버전에서 기본 아이디어를 얻었음
![idea1](https://i.ytimg.com/vi/9Wk9DwxO6po/maxresdefault.jpg)

    

예상 게임 실행 흐름

    ○간단히 스케치한 그림 사용
    ○게임이 어떤 식으로 진행되는지 직관적으로 알 수 있도록 구성

개발 내용

# scene 의 종류 및 구성, 전환 규칙
## 기본 Scene(거의 반드시 구현해야 하는 부분)
### 로딩 화면
![loading scene](https://media.discordapp.net/attachments/1289396317956866108/1300373598539616276/121_20241028172003.png?ex=672dc9c9&is=672c7849&hm=e6233318b3c1e337483dac80eb0ee2bed6889896ad9300c381fc55032e64150e&=&format=webp&quality=lossless&width=711&height=502)
### 타이틀 화면
![gameplay scene](https://media.discordapp.net/attachments/1289396317956866108/1300380214236282890/121_20241028174631.png?ex=672dcff2&is=672c7e72&hm=57a6a3642172f446c1c307b619672d4fb95e26c65669bdcdaad51ce7605be969&=&format=webp&quality=lossless&width=711&height=502)
### 게임 화면
![gameplay scene](https://media.discordapp.net/attachments/1289396317956866108/1295291831185047552/121_20241014164707.png?ex=672dc205&is=672c7085&hm=88fd328b115fb78c79c1cca24b717bfb5082bbf96d3d1fbe06bdef81df0aaa9d&=&format=webp&quality=lossless&width=711&height=502)
            
## 서브 scene(반드시 구현하는 것이 아닌 부가적인 부분)
### 캐릭터 선택창
![gameplay scene](https://media.discordapp.net/attachments/1289396317956866108/1300304676901883955/121_20241028124623.jpg?ex=672d8999&is=672c3819&hm=0cc37511657677cb91c0a84c9bded90ea602eec82415490b541fa670efa5c5d1&=&format=webp&width=711&height=502)

    ○각 Scene 에 등장하는 GameObject 의 종류 및 구성, 상호작용
        -모든 class 에 대한 언급
            car 클래스: 주인공인 자동차에 대한 클래스
            enemyCar 클래스: 주요 적들인 경찰, 차량들에 대한 클래스 입니다.
        -각 클래스의 역할을 나열
        -생김새를 간단한 문장으로 표현
        -화면에 보이지 않는 Controller 객체들에 대한 언급
            -속도 객체 : 자동차의 속도를 규정합니다. 속도에 따라 화면과 적들의 움직임이 바뀔 것입니다.
            -커브 객체: 자동차의 커브력을 규정하는 객체입니다. 높을수록 급커브에 대응하기 쉽습니다.
            -가속 객체: 높을수록 속도가 빠르게 올라갑니다. 미리 설정된 최대 속도까지 올라갑니다.
            -연료 객체 주행을 하거나 충돌 했을 경우 감소하는 객체로 다 떨어지면 게임이 종료됩니다.
        -함수 단위의 설명 (1차발표때는 아직 알 수 없을 것이므로, 2차발표때 추가)
    ○사용한/사용할 개발 기법들에 대한 간단한 소개
        스프라이트들을 이용해 자동차와 도로를 구현할 것이다.
        배경을 여러장 사용해 입체적인 효과를 낼 것이다.
    
    ○각 개발 요소들을 정량적으로 제시할 것

게임 프레임워크

    ○프레임워크에서 지원되는 기능들 중 어떤 것을 사용할 것인지
    ○아직 배우지 않았거나 다루지 않을 항목이 있는지
    
## 1차 발표 관련
### 1차 발표 영상 YouTube link
https://youtu.be/FwmZ5BERFtg?si=Ae5WCi3fTRH9whiM

ㅇ1차 발표 전까지의 활동 정리
---
10.04일 레이싱 게임으로 개발 방향
10.26 - 10.27일 추가적으로 개발할 신, 객체 구상

ㅇ2차 발표전까지 활동 정리
---
10.29 자동차 좌우이동 구현
https://youtu.be/YZiQRvdvx-I?si=s6JOe6a6U0vrCxUx

10.31 가속, 감속, 좌우 이동 구현, 도로 가장자리로 가면 감속 기믹 추가
https://youtu.be/3nYC5xvbv70?si=3I10tRmKIfCz63eh
10.31 배경화면 이미지 추가
	
11.02 브레이크 추가, 적 생성기 비활성화
https://youtu.be/IFuHxSZZlVY?si=7pBWNKRKxSGN2y2m
	
11.07 read.md 파일 업데이트(구현 예정 사항 목록 추가)
11.13 도로 리소스 수정(적용은 안함)
11.21 적(경찰차) 생성

ㅇ최종 발표전까지 활동 정리
---
12.10 
점수, 연료 추가, 본격적으로 개발 시작

12.11 
배경 이미지 변경 및 도로 상태 변경
도로 변화에 따라 자동차 이동

12.12
막판 스퍼트
https://youtu.be/TkMlBy86PNs
완성
https://youtu.be/_mG7EHMQluk

    
# 개발 계획


# 개발 목표(66%/100%) +40%
##엔딩신(10%/10%) +10%
### 이미지(5%/5%)
 [x]체포엔딩
 [x]도착엔딩
### 코드(5%/5%)
 [x]점수
 [ㅌ]엔딩에 따라 화면 변경

## 로딩신(0%/10%) (포기)
### 이미지(0%/5%)
### 코드(0%/5%)

## 타이틀신(10%/10%) +7%
### 이미지(5%/5%) +2%
- [X] 타이틀 화면
- [X] 게임 시작 버튼
- [X] 게임 설명 버튼
### 코드(5%/5%) +5%
- [X] 타이틀 화면
- [X] 게임 시작 버튼

## 캐릭선택신(0%/10%) (포기)
### 이미지(0%/5%)
- [ ] 배경 화면
### 코드(0%/5%)

## 게임화면신 (46%/50%) +26%
### 이미지(10%/10%) +5%
- [X] 도로
- [X] 적
- [X] 주인공
### 코드(36%/40%) +21%
- [X] 감속, 가속
- [X] 도로 커브
- [X] 점수
- [X] 연료
- [△] 적
    - [x] 적 생성
    - [ ] 적 움직임

# 출처
엔진음
Sound Effect by <a href="https://pixabay.com/ko/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=47745">freesound_community</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=47745">Pixabay</a>
충돌음
Sound Effect by <a href="https://pixabay.com/ko/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=6054">freesound_community</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=6054">Pixabay</a>

## 메인음악
https://suno.com/song/2f7faaa4-30b6-4657-acea-42326669e90a

## 폰트
경기천년제목
PF스타더스트

## 에셋
https://chasersgaming.itch.io/racing-asset-touring-car-nes-psuedo