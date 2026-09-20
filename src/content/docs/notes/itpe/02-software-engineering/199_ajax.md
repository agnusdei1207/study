---
title: "AJAX(Asynchronous JavaScript and XML)"
category: "02-software-engineering"
tags:
  - "AJAX"
  - "비동기통신"
  - "XHR"
  - "FetchAPI"
  - "CORS"
  - "SOP"
  - "DOM조작"
  - "SPA"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 웹 아키텍처와 클라이언트 엔지니어링을 거쳐 AJAX로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>웹 아키텍처·클라이언트 엔지니어링</span>
  <strong>AJAX(Asynchronous JavaScript and XML)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 전체 웹페이지를 새로고침하여 화면이 하얗게 깜빡이는 블로킹 현상 없이, 브라우저 백그라운드에서 XMLHttpRequest 또는 Fetch API를 통해 서버와 비동기적으로 경량 데이터(JSON/XML)를 교환하고 DOM을 부분 갱신하여 데스크톱 앱 수준의 매끄러운 사용자 경험을 제공하는 웹 기술의 결합체
- 메커니즘: 사용자 이벤트 발생 $\rightarrow$ XHR/Fetch 비동기 HTTP 요청 $\rightarrow$ 백엔드 JSON 데이터 반환 $\rightarrow$ Promise 비동기 수신 $\rightarrow$ DOM 동적 부분 조작 및 렌더링
- 산출물: 비동기 데이터 통신 모듈 · REST API 엔드포인트 정의서 · CORS 보안 설정 명세서

<div class="itpe-flow-map" role="img" aria-label="AJAX 비동기 통신 및 DOM 부분 갱신 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 사용자 이벤트 및 비동기 요청 생성</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>요청</strong><span>사용자 조작을 가로채어 Fetch/XHR 객체로 백그라운드 HTTP 요청 전송</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 무중단 백그라운드 통신</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>비동기</strong><span>브라우저 UI 스레드는 멈추지 않고 사용자와 상호작용 계속 유지</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 경량 데이터 응답 및 파싱</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>파싱</strong><span>서버로부터 전체 HTML 대신 필요한 JSON 데이터 조각만 수신</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 보안 정책 및 렌더링 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>동일 출처 정책(SOP)을 준수하거나 적법한 CORS 응답을 수신하여 렌더링에 성공했는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (DOM 부분 갱신 완료)</strong>
      <span>깜빡임 없는 화면 갱신 완결 $\rightarrow$ History API 연동 및 SPA 상태 유지</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (CORS 차단 / 5xx 오류)</strong>
      <span>통신 거부 $\rightarrow$ 백엔드 CORS 인가 헤더 추가 및 프록시 게이트웨이 경유</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **XMLHttpRequest(XHR)**: 자바스크립트를 이용해 웹 브라우저와 서버 간에 데이터를 비동기적으로 송수신할 수 있도록 지원하는 브라우저 내장 객체
- **Fetch API**: 콜백 기반의 복잡한 XHR을 대체하여 현대적 Promise 기반으로 네트워크 요청을 처리하는 경량 웹 표준 API
- **동일 출처 정책(SOP, Same-Origin Policy)**: 브라우저가 보안을 위해 프로토콜, 도메인, 포트 번호가 동일한 출처에서만 비동기 데이터 접근을 허용하는 핵심 보안 모델
- **CORS(Cross-Origin Resource Sharing)**: 타 도메인 간의 리소스 요청 시 서버가 허용 출처를 HTTP 헤더(`Access-Control-Allow-Origin`)로 명시하여 브라우저의 SOP 제약을 합법적으로 해제하는 메커니즘
</details>

## 1. 개요 및 필요성

### 전통적 동기식 웹의 한계와 비동기 패러다임

과거 웹 환경에서는 사용자가 버튼 하나를 클릭할 때마다 브라우저가 화면을 멈추고 서버로부터 전체 HTML 문서를 새로 받아와 페이지 전체를 다시 렌더링했다. 이로 인해 화면이 하얗게 깜빡이고 서버 대역폭이 낭비되며 사용자 경험이 크게 저해되었다.

2005년 제시 제임스 가렛(Jesse James Garrett)이 정립한 AJAX는 기존의 표준 기술들(JS, DOM, XHR, CSS)을 재조합하여, **전체 화면 새로고침 없이 백그라운드에서 필요한 데이터만 비동기로 가져와 화면을 부분 조작**하는 혁신적인 사용자 경험을 탄생시켰다.

### 전통 동기 웹 vs AJAX 비동기 웹 vs WebSocket 비교

| 구분 | 전통적 동기 웹 (Sync Web) | AJAX 비동기 웹 | WebSocket 실시간 웹 |
|---|---|---|---|
| **화면 갱신** | **전체 페이지 리로드 (깜빡임 발생)** | **필요한 영역만 DOM 부분 갱신** | 푸시 데이터를 통한 실시간 부분 갱신 |
| **통신 방식** | 단방향 동기식 HTTP 요청/응답 | **단방향 비동기식 HTTP 요청/응답** | **단일 TCP 상의 양방향 전이중 통신** |
| **사용자 블로킹**| 응답 수신 전까지 화면 조작 일시 중단 | **백그라운드 통신으로 상호작용 유지** | 상호작용 완전 유지 |
| **데이터 크기** | 완전한 HTML/CSS 문서 전체 (무거움) | **경량 JSON 데이터 조각 (가벼움)** | 헤더가 거의 없는 바이너리/텍스트 프레임 |
| **대표 사례** | 정적 웹페이지, 관공서 단순 게시판 | **포털 검색창 자동완성, 무한 스크롤 피드** | 실시간 주식 호가창, 멀티플레이 웹 게임 |

## 2. 아키텍처 및 핵심 메커니즘

### AJAX 비동기 통신 처리 구조

```text
+-------------------------------------------------------------------------+
|                  AJAX 비동기 통신 및 DOM 부분 갱신 메커니즘             |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 웹 브라우저 클라이언트 ]                              [ 웹/API 서버 ] |
|                                                                         |
|  1. 이벤트 발생 (버튼 클릭 / 스크롤)                                    |
|          │                                                              |
|          v                                                              |
|  2. Fetch / XHR 비동기 호출 ────── HTTP GET/POST ──────> 3. 요청 처리   |
|          │ (UI 스레드 논블로킹!)                                 │      |
|          │                                                       v      |
|  5. DOM 부분 갱신           <───── JSON 데이터 반환 ───── 4. JSON 직렬화 |
|     (document.getElementById.innerHTML)                                 |
+-------------------------------------------------------------------------+
```

### AJAX 핵심 5대 결합 기술

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① HTML/CSS</strong></span>
      <span class="itpe-badge">표현 계층</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>사용자 화면의 시각적 인터페이스와 스타일을 표준적으로 표현</li>
        <li>DOM 조작의 대상이 되는 기본 골격 구조 제공</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② DOM (Document Object Model)</strong></span>
      <span class="itpe-badge">동적 화면 조작</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>HTML 문서를 트리 구조의 메모리 객체로 추상화하여 제공</li>
        <li>자바스크립트가 특정 노드만 골라 실시간으로 내용 수정 및 추가</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ XMLHttpRequest / Fetch</strong></span>
      <span class="itpe-badge">비동기 통신</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>브라우저 백그라운드에서 원격 서버와 HTTP 통신을 수행하는 엔진</li>
        <li>Promise 기반의 Fetch API를 통해 간결한 비동기 코드 작성</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ JSON</strong></span>
      <span class="itpe-badge">경량 데이터 포맷</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>과거 무거운 XML을 완벽히 대체한 키-값 구조의 초경량 텍스트 규격</li>
        <li>자바스크립트 객체와 1:1로 즉각 역직렬화(Parsing) 가능</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 브라우저 동일 출처 정책(SOP) 제약으로 인해 외부 결제/날씨 API 호출 시 CORS 에러 발생 | 백엔드 API 서버에 `Access-Control-Allow-Origin` 응답 헤더 추가 또는 API Gateway 리버스 프록시 구성 | 크로스 도메인 API 연동 100% 정상화 |
| AJAX 부분 갱신 시 브라우저 주소창 URL이 변하지 않아 '뒤로가기' 클릭 시 이전 입력 상태 유실 | HTML5 History API(`history.pushState()`) 및 React Router 등 프론트엔드 라우터 도입 | 브라우저 히스토리 탐색 연속성 보장 |
| 연속된 비동기 요청 간 콜백 중첩으로 인한 콜백 지옥(Callback Hell) 및 레이스 컨디션 발생 | ES8 `async / await` 구문으로 선형 비동기 코드 작성 및 AbortController 요청 취소 적용 | 비동기 코드 가독성 개선 및 버그 차단 |

## 4. 기술사 답안 차별화 포인트

### 현대 프론트엔드 상태 관리(TanStack Query)와 낙관적 업데이트

현대 프론트엔드 엔지니어링 실무에서는 바닐라 AJAX 호출을 직접 다루지 않는다. **TanStack Query(React Query)나 SWR**을 활용하여 서버 상태를 선언적으로 관리한다. 특히 사용자가 '좋아요'나 '댓글'을 누르는 즉시 서버 응답을 기다리지 않고 화면을 먼저 갱신한 뒤 백그라운드 통신을 완료하는 **"낙관적 업데이트(Optimistic Update)"**와 자동 캐싱 및 중복 요청 제거(Deduping) 패턴을 실무적 차별화로 제시한다.

### SPA의 한계 극복: SSR 및 하이브리드 아키텍처 연계

AJAX 기반 단일 페이지 애플리케이션(SPA)은 검색 엔진 로봇이 비어있는 초기 HTML을 크롤링하여 색인에 실패하는 **SEO(검색 노출) 취약점**과 초기 자바스크립트 번들 다운로드로 인한 **첫 화면 표시(FCP) 지연** 문제를 안고 있다. 이를 극복하기 위해 첫 화면은 서버에서 렌더링(SSR)하고 이후 인터랙션은 AJAX로 처리하는 **Next.js 기반 하이브리드 아키텍처**를 결론으로 제언한다.

## 5. 참고 및 연계 학습

- [REST(Representational State Transfer)](./015_rest.md)
- [Web 2.0](./183_web_2_0.md)
- [HTML5](./186_html5.md)
- [웹 성능 최적화](./164_web_performance_optimization.md)
