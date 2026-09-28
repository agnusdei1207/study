---
title: "AJAX(Asynchronous JavaScript and XML)"
category: "02-software-engineering"
tags:
  - "AJAX"
  - "비동기통신"
  - "XMLHttpRequest"
  - "FetchAPI"
  - "CORS"
  - "SOP"
date: "2026-09-28T18:35:00+09:00"
author: "Antigravity"
sidebar:
  badge:
    text: "기초"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 웹 아키텍처·인터넷 기술 → AJAX(Asynchronous JavaScript and XML)

## 지식 위치

소프트웨어공학 > 웹 애플리케이션 > 브라우저 비동기 통신 > AJAX

## 30초 인출

- 본질: 웹 브라우저가 전체 웹 페이지를 다시 로드하지 않고 백그라운드에서 서버와 비동기적으로 데이터를 교환(JSON/XML)하여 화면의 일부분만 동적으로 갱신하는 웹 개발 기술
- 메커니즘: 사용자 UI 이벤트 발생 → JavaScript의 XMLHttpRequest 또는 Fetch API 비동기 HTTP 요청 발행 → 서버 데이터 처리 및 응답(JSON) → 브라우저 이벤트 루프 콜백 수신 및 DOM 부분 갱신
- 통찰: 비동기 호출 급증 시 동일 출처 정책(SOP) 제약 및 응답 순서 역전(Race Condition)으로 인한 UI 왜곡이 발생하므로 CORS 헤더 규격 준수와 AbortController 기반 이전 요청 취소 통제 필수

<details>
<summary>핵심 용어</summary>

- **AJAX** : 2005년 제시 제임스 가렛이 명명한 기법으로 JavaScript, DOM, CSS, XMLHttpRequest를 결합한 비동기 웹 통신 모델
- **XMLHttpRequest (XHR)** : 브라우저 내에서 자바스크립트를 이용해 서버로 HTTP/HTTPS 요청을 전송하고 응답을 수신하는 원조 객체
- **Fetch API** : XHR의 복잡한 콜백 구조를 개선하여 Promise 기반으로 네트워크 요청을 깔끔하게 처리하는 모던 웹 표준 API
- **SOP (Same-Origin Policy)** : 프로토콜, 호스트, 포트가 일치하는 출처(Origin)의 리소스에만 접근을 허용하는 브라우저의 기본 보안 정책
- **CORS (Cross-Origin Resource Sharing)** : 서버가 `Access-Control-Allow-Origin` 등 HTTP 응답 헤더를 통해 타 출처 브라우저의 자원 접근을 안전하게 허용하는 메커니즘
- **경쟁 상태 (Race Condition)** : 네트워크 지연 편차로 인해 먼저 보낸 요청의 응답이 나중에 보낸 요청의 응답보다 늦게 도착하여 최신 데이터가 덮어씌워지는 현상
</details>

---

## 2~4교시 예상문제 (25점)

> 비동기 웹 애플리케이션의 핵심 기술인 AJAX의 개념과 통신 아키텍처를 설명하고, 전통적 웹 동기 방식과의 비교 및 브라우저 보안 정책(SOP, CORS) 대응과 상태 관리 방안을 기술하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 웹 브라우저가 화면 전체를 새로고침(Reload)하지 않고, 백그라운드에서 자바스크립트 엔진을 통해 웹 서버와 비동기적으로 HTTP 데이터를 송수신하여 DOM의 특정 영역만 실시간 갱신하는 프론트엔드 통신 기법 |
| 목적 | 사용자 인터랙션의 연속성 보장(화면 깜빡임 제거), 불필요한 전체 페이지 HTML 재다운로드 방지를 통한 네트워크 대역폭 절감 및 데스크톱 네이티브 앱 수준의 반응성 달성 |

## Ⅱ. 핵심 특징

| 특징 | 세부 내용 |
|---|---|
| 비동기 백그라운드 통신 | 서버 응답을 대기하는 동안 브라우저 메인 UI 스레드가 멈추지(Blocking) 않고 사용자의 추가 입력 지속 수용 |
| 화면 부분 갱신 (Partial Update) | 전체 HTML 문서가 아닌 필요한 비즈니스 데이터(JSON)만 수신하여 변경된 DOM 노드만 선택적 재렌더링 |
| 데이터 포맷의 현대화 | 초기 XML 중심에서 경량성과 파싱 효율이 뛰어난 JSON(JavaScript Object Notation) 중심으로 표준화 |
| 브라우저 보안 샌드박스 종속 | 클라이언트에서 직접 외부 API를 호출하므로 Same-Origin Policy(SOP)와 CORS 프로토콜의 엄격한 통제 수반 |

단순한 하이퍼링크 문서 뷰어였던 웹 브라우저를 본격적인 엔터프라이즈 SPA(Single Page Application) 플랫폼으로 견인한 원동력.

## Ⅲ. 체계·프로세스

```text
[전통적 동기식 웹 vs AJAX 비동기식 웹 통신 비교]

[전통적 웹: 동기식 (Synchronous Request)]
  사용자 클릭 ──► [HTTP Request] ──► 서버 처리 ──► [HTML 응답] ──► 전체 렌더링
  (요청 시 화면 멈춤 및 깜빡임 발생)

[AJAX 웹: 비동기식 (Asynchronous Request)]
  사용자 클릭 ──► JS 이벤트 리스너 ──► XMLHttpRequest / Fetch API 백그라운드 호출
                                              │
                                              ▼ (백그라운드 네트워크 전송)
                                         [웹 서버 / API]
                                              │
                                              ▼ (JSON 데이터만 반환)
  JS 비동기 콜백 (Promise) ◄───────────────────┘
       │
       ▼ DOM API (getElementById 등)
  특정 <div> 영역만 부드럽게 갱신 (사용자 입력 방해 없음)
```

동기식 전체 페이지 새로고침과 대비되는 자바스크립트 엔진 매개 백그라운드 요청, JSON 수신 및 부분 DOM 갱신 흐름.

## Ⅳ. 종류·비교

| 비교 항목 | 전통적 웹 통신 모델 (동기식) | AJAX 통신 모델 (비동기식) |
|---|---|---|
| **통신 방식** | 동기식 (Synchronous) | 비동기식 (Asynchronous) |
| **요청 주체** | 브라우저 자체의 폼 제출 및 링크 이동 | JavaScript 엔진 (`fetch()`, `axios`, `XHR`) |
| **응답 데이터** | 화면 전체를 구성하는 완전한 HTML 문서 | 순수 비즈니스 데이터 (JSON, XML, 텍스트) |
| **화면 갱신** | 페이지 전체가 백색으로 번쩍인 후 재렌더링 | 변경된 UI 컴포넌트 영역만 선택적 재렌더링 |
| **네트워크 트래픽** | 헤더, 푸터, 스크립트 등 중복 자원 반복 전송 (과다) | 순수 페이로드 데이터만 전송 (극소화) |
| **사용자 경험** | 응답 대기 시간 동안 모든 조작 불가능 (블로킹) | 요청 중에도 스크롤, 입력 등 자유로운 조작 가능 |

### AJAX 비동기 구현 기술 비교 (XHR vs Fetch vs Axios)

| 비교 항목 | XMLHttpRequest (XHR) | Fetch API | Axios 라이브러리 |
|---|---|---|---|
| **기반 메커니즘** | 이벤트 기반 (onreadystatechange) | **Promise** 기반 (Web 표준 API) | Promise 기반 (서드파티 라이브러리) |
| **문법 가독성** | 중첩 콜백 지옥(Callback Hell) 발생 | async/await와 결합하여 깔끔한 비동기 코드 | 직관적인 요청/응답 문법 제공 |
| **응답 파싱** | `JSON.parse(xhr.responseText)` 수동 | `response.json()` Promise 호출 필수 | JSON 자동 변환 (자동 직렬화) |
| **요청 취소** | `xhr.abort()` 제공 | `AbortController` 인터페이스 활용 | CancelToken / AbortController 지원 |
| **인터셉터 기능** | 지원하지 않음 (수동 래핑) | 지원하지 않음 | 요청/응답 가로채기(Interceptor) 내장 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 서로 다른 도메인(출처)의 API 호출 시 브라우저 SOP 정책에 의해 요청이 차단되는 문제 | 서버 응답 헤더에 `Access-Control-Allow-Origin`을 명시(CORS 설정)하거나 백엔드 리버스 프록시(Nginx) 구성 |
| 검색 엔진 크롤러가 초기 빈 HTML만 수집하여 검색엔진 최적화(SEO) 순위가 급락하는 현상 | 서버 사이드 렌더링(SSR: Next.js/Nuxt)을 결합하거나 빌드 타임 정적 사이트 생성(SSG) 하이브리드 아키텍처 도입 |
| 네트워크 속도 편차로 인해 먼저 요청한 오래된 데이터가 최신 데이터를 덮어쓰는 경쟁 상태(Race Condition) | 신규 요청 발행 시 `AbortController.abort()`를 호출하여 이전 진행 중인 요청을 즉각 폐기하고 요청 고유 ID 매핑 |

## Ⅵ. 제언

프론트엔드 아키텍처에서는 단순 무분별한 Fetch 호출을 지양하고, React Query(TanStack Query)나 SWR과 같은 서버 상태 관리 라이브러리를 도입하여 캐싱, 중복 요청 제거, 백그라운드 재검증을 통합 자동화할 것을 필요.

```text
[현대적 비동기 데이터 페칭 아키텍처]
  컴포넌트 렌더링 → TanStack Query (캐시 조회) ──► 캐시 적중 시 즉각 표출 (Stale-While-Revalidate)
                                              └──► Fetch 통신 (AbortController 관리)
```

| 검증 단계 | 네트워크 통신 단계 | 클라이언트 상태 관리 단계 |
|---|---|---|
| 핵심 통제 | CORS 사전 요청(Preflight) 캐싱(`Max-Age`) 및 보안 헤더 검증 | 401/403 토큰 만료 시 자동 재발급 인터셉터 및 글로벌 에러 바운더리 |
| 달성 목표 | 무의미한 OPTIONS 프리플라이트 왕복 오버헤드 최소화 | 비동기 통신 실패 시에도 안전한 UI 폴백(Fallback) 보장 |

---

## 출제 이력과 검증 출처

- 정보관리기술사 112회 1교시: 동일 출처 정책(SOP)과 교차 출처 리소스 공유(CORS) 메커니즘

## 연결 토픽

- [Web 2.0](./183_web_2_0.md)
- [HTML5](./186_html5.md)
- [RESTful 아키텍처 원칙](./015_rest.md)
- [웹 성능 최적화 기법](./164_web_performance_optimization.md)
