---
title: "AJAX(Asynchronous JavaScript and XML)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T11:20:00+09:00"
tags:
  - "notes-software-engineering"
extra:
  model: "Gemini 3.8 Flash"

---

## 답안 골격
```text
[AJAX(Asynchronous JavaScript and XML)] ◀━━ 머리: Ⅶ 내 의견 (XMLHttpRequest에서 Fetch API 및 SPA(Single Page Application)로의 프론트엔드 통신 진화)
 ┃
 ┣━ Ⅰ 개요 ───── 전체 웹페이지의 새로고침 없이 백그라운드 비동기 통신을 통해 화면의 일부만을 동적으로 갱신하는 웹 개발 기술의 결합체
 ┣━ Ⅱ 특징 ───── 비동기 처리(Asynchronous) · 대역폭 절감 및 응답 속도 향상 · 데스크톱 앱 수준의 매끄러운 사용자 경험(UX) 제공
 ┣━ Ⅲ 구조 ───── 5대 핵심 기술 스택: HTML/CSS(표현) + DOM(화면 조작) + XMLHttpRequest/Fetch(비동기 통신) + JSON/XML(데이터) + JavaScript(바인딩)
 ┣━ Ⅳ 흐름 ───── 사용자 이벤트 발생 → XHR/Fetch 객체 생성 → 비동기 HTTP 요청 전송 → 서버 데이터(JSON) 응답 → 콜백 실행 및 DOM 부분 갱신
 ┣━ Ⅴ 비교 ───── 전통적 동기식 웹(Synchronous) vs AJAX 비동기 웹 vs WebSocket 실시간 웹
 ┗━ Ⅵ 실무 ───── 동일 출처 정책(SOP) 위반 및 CORS 에러 대응 / 뒤로가기(History API) 미작동 문제 / 콜백 지옥(Promise, Async/Await로 해결)
```
- 필수 키워드: 비동기(Asynchronous) · XMLHttpRequest(XHR) · Fetch API · DOM 조작 · JSON · 동일 출처 정책(SOP) · CORS · Single Page Application(SPA)
- 기출: 83회 1교시, 95회 1교시 `AJAX의 개념, 동작 원리, 핵심 구성 기술 및 전통적인 웹 페이지 방식과의 비교` → Ⅰ~Ⅵ

## 한 줄 본질
- 서버와 브라우저가 통신할 때마다 하얀 화면으로 깜빡이며 전체 페이지를 다시 그리던 낭비를 없애고, 필요한 JSON 조각만 비동기로 가져와 화면을 부분 조작하는 기술 / 비동기 UX 혁신과 SOP/CORS 극복

## 핵심 그림
```text
[ 전통적 동기식 웹 통신 ]
[ 브라우저 ] ──(요청)──> [ 서버 ]
     │ (화면 멈춤/블로킹)    │
[ 전체 흰 화면 깜빡! ] <──(HTML 전체 재전송)──┘

[ AJAX 비동기식 웹 통신 ]
[ 브라우저 ] ──(XHR/Fetch 비동기 요청)──> [ 서버 ]
     │ (사용자는 화면 계속 조작 가능!)         │
[ DOM 부분 갱신! ] <───(JSON 조각 응답)────────┘
```

## 핵심 용어
- XMLHttpRequest(XHR): 자바스크립트를 이용해 서버와 비동기적으로 HTTP 통신을 수행할 수 있도록 브라우저가 제공하는 핵심 내장 객체
- DOM(Document Object Model): HTML 문서의 계층적 요소를 트리 구조의 객체 모델로 표현하여 자바스크립트가 화면 요소를 동적으로 제어할 수 있게 하는 표준 API
- 동일 출처 정책(SOP, Same-Origin Policy): 프로토콜, 호스트, 포트 번호가 동일한 출처에서만 비동기 요청과 리소스 접근을 허용하는 브라우저의 기본 보안 정책
- CORS(Cross-Origin Resource Sharing): 브라우저의 SOP 제약을 넘어 서버가 허용하는 외부 도메인의 비동기 AJAX 요청을 안전하게 인가해 주는 HTTP 헤더 기반 메커니즘
- Fetch API: 콜백 기반의 복잡한 XMLHttpRequest를 대체하여 Promise 기반으로 깔끔하고 유연하게 HTTP 비동기 통신을 처리하는 최신 브라우저 표준 API

## 핵심 통찰
- 2005년 제시 제임스 가렛(Jesse James Garrett)이 명명한 AJAX는 새로운 언어나 프로토콜이 아니라, 기존에 존재하던 JavaScript, DOM, XHR, CSS를 하나로 결합한 '아키텍처적 재발견'이었음
- AJAX의 출현으로 구글 맵스(Google Maps), 지메일(Gmail)과 같은 혁신적 웹 애플리케이션이 등장할 수 있었으며, 이는 오늘날 Single Page Application(SPA: React, Vue, Angular)의 기술적 모태가 됨
- 데이터 교환 포맷 역시 초기에는 장황한 XML을 주로 사용했으나, 자바스크립트 객체와 1:1로 매핑되는 초경량 JSON(JavaScript Object Notation)으로 완전히 표준이 대체됨

## 이웃 토픽과 구분
| 비교 항목 | 전통적 동기 웹 (Sync Web) | AJAX 비동기 웹 | WebSocket 실시간 웹 |
| :--- | :--- | :--- | :--- |
| **화면 갱신 방식** | 전체 페이지 리로드 (깜빡임 발생) | 요청 부분만 DOM 부분 갱신 | 양방향 푸시를 통한 실시간 부분 갱신 |
| **통신 방식** | 단방향 동기식 HTTP 요청/응답 | 단방향 비동기식 HTTP 요청/응답 | 단일 TCP 연결 기반 양방향 전이중 통신 |
| **사용자 블로킹** | 응답 수신 시까지 화면 조작 불가 | 백그라운드 처리로 상호작용 유지 | 상호작용 완전 유지 |
| **데이터 포맷** | 완전한 HTML/CSS 문서 전체 | 경량 JSON 또는 텍스트 조각 | 바이너리 프레임 또는 텍스트 프레임 |
| **주요 활용처** | 정적 블로그, 관공서 단순 게시판 | 포털 검색 자동완성, 대시보드 | 실시간 채팅, 주식 호가창, 멀티 게임 |

## 문제·원인·대책
| 문제상황 | 원인 | 기술적 대책 |
| :--- | :--- | :--- |
| **CORS 에러로 인한 외부 API 호출 차단** | 브라우저 보안 규정(SOP)으로 인해 다른 도메인으로의 XHR 요청 거부 | 백엔드 응답 헤더에 `Access-Control-Allow-Origin` 명시 또는 프록시(Proxy) 서버 구축 |
| **뒤로가기 클릭 시 이전 폼 상태 유실** | URL 변경 없이 자바스크립트 DOM만 갱신되어 브라우저 히스토리 스택에 미기록 | HTML5 History API(`history.pushState()`) 및 React Router 등 프론트엔드 라우터 도입 |
| **연속된 비동기 호출로 인한 콜백 지옥** | XHR 콜백 함수를 다중 중첩 작성하여 코드 가독성 저하 및 에러 처리 누락 | ES6 Promise 및 ES8 `async / await` 구문으로 직관적인 선형 비동기 코드 리팩토링 |

## 이렇게 출제된다
- **10점형**: AJAX(Asynchronous JavaScript and XML)의 개념, 핵심 구성 기술 및 전통적 동기 웹과의 차이점을 설명하시오.
- **25점형**: 
  - 1) 전통적인 웹 애플리케이션의 화면 갱신 방식과 AJAX 비동기 통신의 차이점을 시퀀스 다이어그램으로 도식화하시오.
  - 2) AJAX 통신 시 발생하는 보안 제약사항인 동일 출처 정책(SOP)의 원리와 이를 극복하기 위한 CORS(Cross-Origin Resource Sharing)의 동작 메커니즘(Preflight Request 등)을 설명하시오.
  - 3) XMLHttpRequest에서 최신 Fetch API 및 Axios 라이브러리로의 진화 과정과 SPA(Single Page Application) 아키텍처 연계 방안을 논하시오.

## 내 의견
- AJAX는 웹을 단순 하이퍼링크 문서 뷰어에서 클라우드 기반 SaaS 데스크톱 플랫폼으로 진화시킨 가장 파괴적인 기술적 변곡점이었음
- 현대 프론트엔드 엔지니어링 실무에서는 단순한 AJAX 호출을 넘어, TanStack Query(React Query)나 SWR과 같은 서버 상태 관리 라이브러리를 결합하여 캐싱, 중복 요청 제거(Deduping), 낙관적 업데이트(Optimistic Update)를 구현하는 것이 표준임
- 또한 검색엔진 최적화(SEO)와 첫 페이지 로딩 속도(FCP) 저하라는 SPA/AJAX의 구조적 단점을 극복하기 위해 Next.js나 Nuxt와 같은 서버 사이드 렌더링(SSR) 및 하이브리드 정적 생성(SSG) 아키텍처를 적절히 조화시켜야 함
