---
title: "AJAX(Asynchronous JavaScript and XML)"
author: "agnusdei1207"
date: "2026-10-25T00:07:34+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- AJAX(Asynchronous JavaScript and XML), 비동기 통신(Asynchronous Communication), XMLHttpRequest
- Fetch API(Application Programming Interface), DOM(Document Object Model), JSON(JavaScript Object Notation)
- 부분 갱신(Partial Update), SPA(Single Page Application), SSR(Server-Side Rendering), CORS(Cross-Origin Resource Sharing)

## Ⅰ. AJAX의 개요

- 핵심 요약 : 전체 페이지를 새로고침하지 않고 백그라운드에서 데이터를 주고받아 화면 일부만 갱신하는 웹 개발 기법.
- 개념 : **AJAX** (Asynchronous JavaScript and XML)는 2005년 제시 제임스 개릿(Jesse James Garrett)이 명명한 기법으로, 브라우저가 전체 페이지를 다시 읽지 않고 자바스크립트로 서버와 비동기 통신하여 받은 데이터로 **DOM** (Document Object Model) 일부를 동적으로 갱신하는 인터랙티브 웹 개발 방식.
- 배경 및 필요성 : 기존 웹은 요청마다 전체 페이지가 다시 로딩되어 화면이 깜빡이고 사용자 흐름이 끊겨, 데스크톱 앱 같은 반응성이 필요해짐.
- 핵심 기술 조합 : **XMLHttpRequest** (XHR)와 **Fetch API** (Application Programming Interface) 같은 비동기 호출 수단, 자바스크립트 DOM 조작, **JSON** (JavaScript Object Notation)이나 XML 기반 데이터 교환.

## Ⅱ. AJAX의 특징 및 장점

- 핵심 요약 : 논블로킹 통신, 부분 갱신, 경량 데이터 교환이 결합되어 반응성과 대역폭 효율을 함께 얻는 구조.

1. 비동기(Non-blocking) 통신 : 응답을 기다리는 동안에도 사용자 조작이 계속됨 → 화면 멈춤이 없어 체감 반응성 향상.
2. 부분 갱신 : 필요한 영역만 DOM을 바꿈 → 화면 깜빡임이 사라지고 작업 흐름이 유지됨.
3. 경량 데이터 교환 : 완전한 HTML(HyperText Markup Language) 대신 JSON 같은 순수 데이터만 송수신 → 전송량과 서버 렌더링 부담 감소.
4. 기술 융합 : 비동기 호출, 자바스크립트, DOM, 데이터 포맷이 결합 → 웹 앱의 상호작용 수준을 끌어올림.
5. 발전의 기반 : 화면 전환을 클라이언트가 맡는 **SPA** (Single Page Application) 등장의 기술적 토대가 됨.

## Ⅲ. AJAX의 구조 (흐름)

- 핵심 요약 : 요청마다 전체 페이지를 받아 다시 그리는 동기식 흐름과, 데이터만 받아 일부를 고치는 비동기식 흐름의 대비.

```text
[ 전통적 웹 : 동기식 (Synchronous) ]
[ 브라우저 ] 요청 (HTTP POST)
          ↓
[ 웹 서버 + DB 처리 ]
          ↓ 완전한 HTML 전체 반환
[ 전체 페이지 재렌더링 ]
 화면 멈춤, 깜빡임 발생
```

```text
[ AJAX : 비동기식 (Asynchronous) ]
[ 브라우저 UI ] 사용자 조작 계속 진행
          ↓ 백그라운드 요청 (XHR / Fetch)
[ 백엔드 API + DB 처리 ]
          ↓ 순수 데이터만 수신 (JSON)
[ 자바스크립트 DOM 조작 ]
 UI 일부 영역만 즉시 갱신
```

## Ⅳ. XMLHttpRequest와 모던 Fetch API의 비교

- 핵심 요약 : 이벤트 리스너 기반의 레거시 XHR과 프로미스 기반의 Fetch API는 같은 비동기 통신을 다른 프로그래밍 모델로 제공.

| 비교 항목 | 레거시 XMLHttpRequest (XHR) | 모던 Fetch API |
| --- | --- | --- |
| 프로그래밍 모델 | 이벤트 리스너 기반 (`onreadystatechange`) | 프로미스(Promise)와 `async` / `await` 기반 |
| 중첩 콜백 | 콜백이 깊어지면 가독성과 오류 처리가 취약 | 체이닝과 `async` / `await`로 흐름이 단순함 |
| 스트리밍 | 응답 완료 후 전체 데이터를 받는 방식이 기본 | ReadableStream으로 점진적 수신 가능 |
| 쿠키 전송 | 같은 출처 요청에 쿠키 자동 포함 | 같은 출처에는 자동 포함, 교차 출처는 `credentials` 옵션 명시 필요 |
| HTTP 오류 처리 | 404, 500도 요청 완료로 처리되어 상태 코드 직접 확인 | 404, 500도 resolve되므로 `response.ok` 확인 필요 |

- 선택 기준 : 신규 코드는 Fetch API로 작성하고, 레거시 시스템 유지보수 구간에서만 XHR을 다룸.

## Ⅴ. AJAX의 한계와 방안

- 핵심 요약 : 히스토리 파손, 검색 엔진 인덱싱 한계, 과도한 요청에 따른 서버 부하가 주요 한계이며 클라이언트 라우팅, 서버 렌더링, 요청 제어로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 브라우저 히스토리·북마크 파손 | URL이 바뀌지 않아 뒤로 가기 시 이전 사이트로 이탈 | HTML5 History API(`pushState`, `popstate`) 기반 클라이언트 라우팅과 URL별 딥링크 보장 | 뒤로 가기 이탈률, 북마크 복원 성공률 |
| 검색 엔진 인덱싱 한계 | 초기 HTML에 콘텐츠가 없어 자바스크립트를 완전히 해석하지 못하는 크롤러에 빈 페이지 노출 | 서버 사이드 렌더링(SSR, Server-Side Rendering) 병행, 사전 렌더링(Prerendering) 활용 | 색인 페이지 수, 크롤링 오류율 |
| 잦은 요청에 따른 서버 자원 고갈 | 입력마다 요청을 보내 API 게이트웨이와 DB(Database) 커넥션 풀에 부담 집중 | 디바운싱과 쓰로틀링 적용, `AbortController`로 중복 요청 취소, ETag 기반 응답 캐싱 | 초당 요청 수, 커넥션 풀 사용률 |

- 장점 : 화면 깜빡임 없는 사용자 경험, 소량 데이터 송수신에 따른 대역폭과 서버 자원 절감, 통신과 조작의 병행으로 반응성 향상.

## Ⅵ. SPA 및 모던 웹을 위한 기술사적 제언

- 핵심 요약 : 다른 출처의 API 호출을 위한 CORS(Cross-Origin Resource Sharing) 정책을 설계 단계에서 통제하고, JSON 기반 전송을 캐싱과 압축으로 최적화하는 방향.
- CORS 정책의 선제 설계 : 브라우저의 **동일 출처 정책** (SOP, Same-Origin Policy)에 따라 다른 도메인 API를 호출할 때 차단되지 않도록, API 게이트웨이에서 허용 출처와 프리플라이트 응답 캐싱을 엄격하게 설정하는 것이 바람직하다.
- 데이터 전송 최적화 : 개발 조직은 JSON 포맷을 표준으로 쓰고 Gzip이나 Brotli 압축을 적용하며, 클라이언트 측 데이터 캐시 라이브러리로 중복 요청을 줄이는 구조를 갖추는 것이 좋다.

## Ⅶ. 결론

- 핵심 요약 : AJAX는 비동기 부분 갱신으로 인터랙티브 웹을 구현한 기반 기술.
- 시사점 : 히스토리 관리, 서버 렌더링 병행, 요청 제어, CORS 정책이 함께 설계되어야 현대 웹의 품질이 확보됨.
