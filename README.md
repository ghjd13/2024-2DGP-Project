# 2024-2DGP-Project
게임의 간단한 소개 (카피의 경우 원작에 대한 언급)

    ○게임 컨셉, 핵심 메카닉 제시
    ○스크린샷 혹은 그림판으로 끄적인 이미지 포함

# 프로젝트 명: 무법 레이서
    
    게임 컨셉: 닌텐도의 f1같은 고전 레이싱 게임
    
    배경: 80년대 배경으로 경찰과 차들을 피해 도시를 향해 도망치는 차량을 주인공으로 하는 게임
    
    문제점: 도로 리소스를 구하기 힘들어 스프라이트를 자체제작해야함
    
 # 컨셉아트
    F1레이스NES버전에서 기본 아이디어를 얻었음
![idea1](https://i.ytimg.com/vi/9Wk9DwxO6po/maxresdefault.jpg)
![idea2](https://media.discordapp.net/attachments/1289396317956866108/1295291831185047552/121_20241014164707.png?ex=671f4185&is=671df005&hm=645c0cbef1b2ca03f7393e989d0954c2494206c989f1c0e8b8254e67af0ba72f&)


    

예상 게임 실행 흐름

    ○간단히 스케치한 그림 사용
    ○게임이 어떤 식으로 진행되는지 직관적으로 알 수 있도록 구성

개발 내용

# scene 의 종류 및 구성, 전환 규칙
## 기본 Scene(거의 반드시 구현해야 하는 부분)
### 로딩 화면
![loading scene](https://media.discordapp.net/attachments/1289396317956866108/1300373598539616276/121_20241028172003.png?ex=67209ac9&is=671f4949&hm=207b5c59405e0ecdc38e64012f5d03f29ac210d1336de06ede59dc4cb67da4fa&)
### 타이틀 화면
### 게임 화면
![gameplay scene](https://media.discordapp.net/attachments/1289396317956866108/1295291831185047552/121_20241014164707.png?ex=67209305&is=671f4185&hm=95574bfbc1b0043836a21b1d4dd4446162d4ed22ad5491924dbd9e5a0f42f18c&)
            
## 서브 scene(반드시 구현하는 것이 아닌 부가적인 부분)
### 캐릭터 선택창
![gameplay scene](https://media.discordapp.net/attachments/1289396317956866108/1300304676901883955/121_20241028124623.jpg?ex=67205a99&is=671f0919&hm=165ca7917112a0af4c053f9d3f318f983aa4f542199c5ca2498385702249c47e&)

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
        -함수 단위의 설명 (1차발표때는 아직 알 수 없을 것이므로, 2차발표때 추가)
    ○사용한/사용할 개발 기법들에 대한 간단한 소개
        스프라이트들을 이용해 자동차와 도로를 구현할 것이다.
        배경을 여러장 사용해 입체적인 효과를 낼 것이다.
    
    ○각 개발 요소들을 정량적으로 제시할 것

게임 프레임워크

    ○프레임워크에서 지원되는 기능들 중 어떤 것을 사용할 것인지
    ○아직 배우지 않았거나 다루지 않을 항목이 있는지
## 1차 발표 관련
    ○1차 발표 영상 YouTube link
    ○1차 발표 전까지의 활동 정리
        