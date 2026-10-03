---
title: "AJAX(Asynchronous JavaScript and XML)"
author: "Antigravity"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. AJAX의 개요

- 개념 : 제시 제임스 개릿(Jesse James Garrett)이 2005년에 명명한 웹 프론트엔드 비동기 통신 기술로, 웹 브라우저에서 전체 웹 페이지를 새로고침(Reload)하지 않고 자바스크립트를 활용하여 백그라운드에서 웹 서버와 비동기적으로 소량의 데이터를 교환한 후 웹 페이지의 일부분만을 동적으로 갱신(DOM Manipulation)하는 인터랙티브 웹 개발 기법.
- 배경 및 필요성 : 과거 웹의 동기식 요청-응답 모델에서 버튼 클릭 시마다 흰 화면이 깜빡거리며 전체 페이지가 다시 로딩되던 사용자 경험(UX) 단절을 해결하고 데스크톱 앱과 같은 매끄러운 반응성 제공.
- 핵심 기술 스택 : XMLHttpRequest / Fetch API, 자바스크립트 DOM 조작, JSON / XML 데이터 직렬화, CSS 비동기 UI 제어.

## Ⅱ. 전통적 웹 통신과 AJAX 비동기 통신의 흐름 비교

```text
   [ 전통적 웹 통신: 동기식 (Synchronous) ]
   [ 브라우저 ] ── HTTP POST 요청 ──> [ 웹 서버 ] ──> [ DB 처리 ]
        │ (화면 멈춤, 흰 화면 깜빡임)                          │
   [ 전체 페이지 재렌더링 ] <── 완전한 HTML 전체 페이지 반환 ──┘

   [ AJAX 웹 통신: 비동기식 (Asynchronous) ]
   [ 브라우저 UI ] ── 사용자 조작 계속 진행 (Non-blocking)
        │
        ▼ (백그라운드 통신)
   [ Fetch / XHR ] ── 비동기 백그라운드 요청 ──> [ 백엔드 API ] ──> [ DB 처리 ]
        ▲                                                               │
        │ (순수 데이터만 수신: JSON)                                    │
        └─────────────────────── { "status": "ok" } ──────────────────┘
        │
        ▼
   [ 자바스크립트 DOM 조작 ] ── 변경된 UI 일부 영역만 즉각 동적 갱신
```

## Ⅲ. XMLHttpRequest와 모던 Fetch API 비교

| 비교 항목 | 레거시 XMLHttpRequest (XHR) | 모던 Fetch API |
|---|---|---|
| 프로그래밍 모델 | 복잡한 이벤트 리스너 기반 (`onreadystatechange`) | 모던 프로미스(Promise) 및 `async` / `await` 기반 |
| 콜백 지옥 (Callback Hell) | 중첩된 콜백으로 가독성 및 에러 처리 취약 | 체이닝(`.then()`) 및 간결한 비동기 제어 |
| 스트리밍 지원 | 응답 완료 후 전체 텍스트 수신 | ReadableStream을 통한 점진적 데이터 스트리밍 지원 |
| 기본 쿠키 전송 | 동일 출처 요청 시 쿠키 자동 전송 | 기본적으로 쿠키 미포함 (`credentials: 'include'` 명시 필요) |
| HTTP 에러 처리 | HTTP 404, 500 에러도 정상 resolve 처리됨 | 동일하게 resolve 처리 (`response.ok` 확인 필요) |

## Ⅳ. AJAX(비동기 자바스크립트와 XML)의 주요 한계점 및 해결 방안

- 브라우저 히스토리(뒤로가기/앞으로가기) 및 북마크 파손 :
  - 한계점 : 페이지 전체 리로드 없이 화면 일부분만 비동기 갱신되므로, 브라우저 URL이 변경되지 않아 뒤로가기 버튼 클릭 시 이전 웹사이트로 이탈.
  - 해결 방안 : HTML5 History API(`pushState`, `popState`)를 활용한 클라이언트 라우팅 구현, 가상 URL 맵핑을 통한 딥링킹(Deep Linking) 보장.
- 검색 엔진 크롤러 인덱싱(SEO) 한계 :
  - 한계점 : 초기 HTML에 콘텐츠가 없고 AJAX 비동기 호출을 통해 렌더링되므로, 자바스크립트를 완벽히 해석하지 못하는 검색 엔진 봇에 빈 페이지 노출.
  - 해결 방안 : 서버 사이드 렌더링(SSR) 병행, 사전 렌더링(Prerendering) 도구 활용 및 정적 HTML 스냅샷을 봇에게 서빙하는 동적 렌더링(Dynamic Rendering) 구성.
- 잦은 비동기 API 요청으로 인한 서버 연결 풀(Pool) 고갈 :
  - 한계점 : 실시간 검색어 자동완성 등 사용자 타이핑마다 비동기 요청을 무차별 전송하여 백엔드 API 게이트웨이 및 DB 커넥션 풀 마비.
  - 해결 방안 : 클라이언트 단 디바운싱(Debouncing) 및 쓰로틀링(Throttling) 패턴 적용, 중복 요청 취소(AbortController) 및 HTTP 응답 캐싱(ETag) 적극 도입.

## Ⅴ. 싱글 페이지 애플리케이션(SPA) 및 모던 웹을 위한 기술사적 제언

- **CORS** (교차 출처 리소스 공유) 보안 정책의 선제적 통제 : 브라우저의 동일 출처 정책(SOP)에 따라 다른 도메인의 API를 AJAX로 호출할 때 발생하는 CORS 차단을 방지하기 위해, 백엔드 API Gateway에서 `Access-Control-Allow-Origin`, 프리플라이트(Preflight OPTIONS) 캐싱을 엄격하고 안전하게 설정해야 함.
- RESTful JSON 기반의 페이로드 최적화 : 과거 무거운 XML 파싱 오버헤드를 탈피하고 직관적인 경량 JSON 포맷을 표준으로 채택하되, 모바일 네트워크 대역폭 절감을 위해 Gzip/Brotli 압축 및 클라이언트 측 상태 관리(TanStack Query/SWR)를 결합한 자동 캐싱 및 중복 요청 제거 아키텍처 구축 권장.
