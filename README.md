<h1 align="center">
  <img src="https://github.com/ubinjeon/django_project/assets/156033838/26419a91-8ff1-4437-a53b-3dd43ba5d24f" alt="Markdownify" width="800">
</h1>
<p align ="center">
  <a href="#기획의도">기획의도</a> •
  <a href="#구현방향">구현방향</a> •
  <a href="#웹구성">웹구성</a> •
  <a href="#스킬">스킬</a> •
  <a href="credits">Credits</a>
</p>

## 기획의도
- 경험상 직업 탐색 방법 및 기회 부족에 대한 아쉬움
- 교육부, 한국직업능력연구원 (2022)
    - 웹사이트,SNS가 희망 직업을 알게된 주요 경로
        - 초등학생 25.7%
        - 중학생/고등학생 45% 이상
    - 진로교육에 대한 갈증 높음
    - 현존하는 진로교육 웹사이트 한정적
- 어린이들에게 최신 진로교육 정보를 웹으로 제공하면 의미있을 것이라 판단

## 구현방향
- 대상: 어린이(초등학생)
- 참고자료:
    - 진로정보망 커리어넷 OpenAPI
    - World Economic Forum (2023)
    - Foundation for Young Australians (2017)
    - McKinsey Global Institute (2023)
    - 한국고용정보원 (2020)
- 구현특징:
    - 이미지 요소 70여개
    - 다양한 동적 효과들
    - 간단하고 알기 쉬운 설명들

## 웹구성
```mermaid
classDiagram
class `홈 화면`{
  홈화면
  single_pages}
class `어른들이 하는일` {
  직업 종류
  single_pages}
class `나는 누구일까?`{
  직업 적성
  single_pages}
class `나도 해보기`{
  직업 체험
  single_pages}
class `미래직업연구1`{
  글로벌 변화
  single_pages}
class `궁금증 해결하기`{
  게시판
  board}
class `직업 체험`{
  오프라인 체험관
  single_pages}
class `직업 체험영상`{
  온라인 체험영상
  single_pages}
class `미래직업연구2`{
  미래직업 능력
  single_pages}
class `미래직업연구3`{
  미래직업 동영상
  single_pages}
`홈 화면`-->`어른들이 하는일`
`홈 화면`-->`나는 누구일까?`
`홈 화면`-->`나도 해보기`
`홈 화면`-->`미래직업연구1`
`홈 화면`-->`궁금증 해결하기`
`나도 해보기`-->`직업 체험관`
`나도 해보기`-->`직업 체험영상`
`미래직업연구1`-->`미래직업연구2`
`미래직업연구1`-->`미래직업연구3`
```
## 스킬
- django / python
- single_pages app: HTML/CSS/JS/AJAX
- board app: BOOTSTRAP/HTML/CSS
- 웹크롤링: NAVER API, 진로정보망 커리어넷 OpenAPI 활용

## Credits
- 이미지 출처:
  - 클립아트코리아
  - <a href="https://www.flaticon.com/free-icons/swiss" title="swiss icons">Swiss icons created by Rifal Hari Topan - Flaticon</a>
  - <a href="https://www.flaticon.com/free-icons/australia" title="australia icons">Australia icons created by amoghdesign - Flaticon</a>
  - <a href="https://www.flaticon.com/free-icons/south-korea" title="south korea icons">South korea icons created by Hight Quality Icons - Flaticon</a>
  - <a href="https://www.flaticon.com/free-icons/bank-of-america" title="bank of america icons">Bank of america icons created by Icon.doit - Flaticon</a>
