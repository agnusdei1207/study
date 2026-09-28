---
title: "서비스 워커(Service Worker)"
category: "02-software-engineering"
tags:
  - "ServiceWorker"
  - "PWA"
  - "CacheStorage"
  - "웹캐시"
  - "오프라인웹"
  - "백그라운드동기화"
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

소프트웨어 공학 → 소프트웨어 아키텍처·설계 → 서비스 워커(Service Worker)

## 지식 위치

소프트웨어공학 > 웹 아키텍처·클라이언트 엔지니어링 > 서비스 워커(Service Worker)

## 30초 인출

- 본질: 웹 브라우저 백그라운드에서 메인 UI 스레드와 독립적으로 실행되며 네트워크 요청 가로채기, 캐싱, 푸시 알림, 백그라운드 동기화를 제어하는 프로그래밍 가능한 클라이언트 프록시 스크립트
- 메커니즘: 서비스 워커 등록(Registration) → 사전 리소스 캐싱 및 설치(Install) → 구버전 캐시 정리 및 활성화(Activate) → 런타임 Fetch 이벤트 가로채기 및 Cache-First/Network-First 등 전략적 응답 반환
- 통찰: 배포 후 신규 버전이 반영되지 않고 구버전 캐시가 유지되는 문제를 방지하기 위해 정적 자산 해시 기반 버전 관리, SkipWaiting() 제어 및 세밀한 캐시 만료(Cache Busting) 정책 수립 필요

<details>
<summary>핵심 용어</summary>

- **서비스 워커 (Service Worker)** : 브라우저가 백그라운드에서 실행하는 이벤트 기반 워커로 DOM에 직접 접근하지 않고 네트워크 프록시 역할을 수행
- **Cache Storage API** : Service Worker 환경에서 HTTP Request/Response 쌍을 프로그래밍 방식으로 저장, 조회, 삭제할 수 있는 비동기 저장소
- **App Shell 모델** : UI를 구성하는 핵심 골격(HTML/CSS/JS)을 미리 로컬에 캐싱하고 동적 콘텐츠만 API로 수신하여 네이티브 앱 수준의 속도를 구현하는 구조
- **PWA (Progressive Web App)** : 오프라인 지원, 푸시 알림, 홈 화면 설치 등 모바일 네이티브 앱과 동일한 사용자 경험을 제공하는 웹 기술
- **Workbox** : 구글에서 개발한 표준 서비스 워커 라이브러리로 사전 캐싱 및 런타임 캐싱 전략을 선언적으로 구축 가능
</details>

---

## 2~4교시 예상문제 (25점)

> PWA(Progressive Web App)의 핵심 기술인 서비스 워커(Service Worker)의 개념과 생명주기(Lifecycle)를 설명하고, 주요 캐싱 전략(Cache First, Network First 등)의 비교 및 운영 시 캐시 갱신(Cache Invalidation) 대응 방안을 제시하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 웹 브라우저의 메인 스레드와 분리되어 백그라운드에서 실행되며, 웹 페이지와 네트워크 사이의 모든 HTTP 트래픽을 가로채어 제어하는 이벤트 기반 자바스크립트 워커 |
| 목적 | 네트워크 단절 환경에서의 오프라인 동작 보장, 정적 리소스 로컬 캐싱을 통한 로딩 성능 극대화, 웹 푸시 알림 및 백그라운드 데이터 동기화 구현 |

## Ⅱ. 핵심 특징

| 특징 | 세부 내용 |
|---|---|
| 클라이언트 사이드 프록시 | 브라우저와 서버 사이의 모든 네트워크 Fetch 요청을 중간 가로채어 캐시 응답 또는 가공 처리 수행 |
| 메인 스레드 분리 | 별도 백그라운드 스레드에서 구동되어 대용량 캐싱 연산 중에도 UI 렌더링 블로킹 원천 배제 (DOM 직접 조작 불가) |
| 이벤트 드리븐 수명주기 | 필요할 때만 메모리에 로드되어 이벤트를 처리하고 유휴 상태가 되면 자동 종료되는 자원 절약형 구조 |
| HTTPS 보안 필수 | 중간자 공격(MITM) 방지를 위해 localhost를 제외한 운영 환경에서는 반드시 HTTPS 프로토콜에서만 구동 |

네이티브 앱의 고유 영역이었던 오프라인 실행과 백그라운드 푸시 기능을 웹 표준 기술로 완벽히 흡수한 핵심 메커니즘.

## Ⅲ. 체계·프로세스

```text
[1. 등록 단계 (Register)]
  메인 스크립트: navigator.serviceWorker.register('/sw.js') 호출
       │
       ▼
[2. 설치 단계 (Install Event)]
  - 서비스 워커 파일 다운로드 및 파싱
  - install 이벤트 핸들러 실행: App Shell 등 핵심 정적 자산 사전 캐싱 (Pre-caching)
  - 실패 시 설치 취소 및 폐기
       │
       ▼
[3. 대기 및 활성화 단계 (Activate Event)]
  - 기존 실행 중인 이전 버전 워커가 종료될 때까지 대기 (skipWaiting()으로 즉시 승격 가능)
  - activate 이벤트 실행: 이전 버전 구형 캐시 저장소 일괄 삭제 및 정리
  - 클라이언트 페이지 제어 권한 획득 (clients.claim())
       │
       ▼
[4. 런타임 제어 단계 (Functional Events)]
  ┌────────────────────────────────────────────────────────┐
  │ - fetch 이벤트      : 네트워크 요청 가로채기 및 캐시 반환│
  │ - push 이벤트       : 서버 웹 푸시 수신 및 알림 생성   │
  │ - sync 이벤트       : 온라인 복귀 시 백그라운드 동기화 │
  └────────────────────────────────────────────────────────┘
```

등록, 설치, 활성화 단계를 거쳐 네트워크 가로채기 및 백그라운드 작업을 제어하는 생명주기 프로세스.

## Ⅳ. 종류·비교

| 캐싱 전략 | 동작 흐름 | 최적 적용 대상 | 장단점 |
|---|---|---|---|
| **Cache First (Cache Falling Back to Network)** | 캐시 먼저 확인 ──► 적중 시 반환, 미적중 시 네트워크 요청 후 캐시 저장 | 폰트, 이미지, 번들링된 정적 JS/CSS | 로딩 속도 극대화 / 최신 콘텐츠 반영 지연 가능 |
| **Network First (Network Falling Back to Cache)** | 네트워크 먼저 요청 ──► 성공 시 최신 반환 및 캐시 갱신, 실패(오프라인) 시 캐시 반환 | 실시간 피드, 게시판 목록, 환율/주가 데이터 | 데이터 최신성 보장 / 네트워크 지연 시 응답 속도 저하 |
| **Stale-While-Revalidate** | 캐시된 데이터 즉시 반환 ──► 백그라운드에서 네트워크 요청 후 캐시 조용히 갱신 | 아바타 이미지, 뉴스 기사, 카테고리 정보 | 빠른 로딩과 데이터 최신화의 최적 균형 / 1회 지연 반영 |
| **Network Only** | 오직 네트워크로만 통신 (캐시 사용 배제) | 결제 API, 로그인 인증, 실시간 보안 토큰 | 오프라인 지원 불가 / 실시간 트랜잭션 무결성 보장 |
| **Cache Only** | 오직 로컬 캐시에서만 데이터 조회 | App Shell 정적 HTML, 고정 오프라인 폴백 페이지 | 네트워크 트래픽 0 / 사전 캐싱 미완료 시 에러 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 신규 서비스 워커가 배포되어도 기존 페이지를 닫기 전까지 구버전 워커와 캐시가 계속 유지됨 | self.skipWaiting()을 호출하여 새 워커를 즉시 활성화하고 self.clients.claim()으로 즉각적인 페이지 제어권 인수 |
| App Shell이나 정적 파일의 수정 사항이 브라우저 캐시에 영구 갇히는 캐시 고착화 문제 | 파일명에 콘텐츠 해시(app.a8f9c.js)를 부여하고 Workbox 기반의 자동 캐시 무효화(Cache Invalidation) 매니페스트 적용 |
| 네트워크 요청 가로채기로 인한 CORS 및 타사(Third-Party) 리소스 캐싱 실패(Opaque Response) | no-cors 모드 응답에 대한 예외 처리 정책을 마련하고 자사 CDN 기반의 도메인 프록싱 구조 구축 |

## Ⅵ. 제언

클라우드 프론트엔드 배포 파이프라인에서 Workbox 도구를 빌드 체인(Vite/Webpack)에 내장하고, 버전별 캐시 정리 및 오프라인 대체 UI를 체계화한 PWA 아키텍처 확립 필요.

```text
[PWA 서비스 워커 배포 아키텍처]
  소스 빌드 (Vite/Workbox) → 해시 매니페스트 생성 → sw.js 배포 → 클라이언트 설치/skipWaiting → 구 캐시 정리
```

| 검증 단계 | 사전 빌드/배포 단계 | 런타임 클라이언트 단계 |
|---|---|---|
| 핵심 통제 | sw.js 파일에 대한 HTTP 응답 헤더 `Cache-Control: no-cache` 설정 | Activate 이벤트 시 구버전 `caches.delete(cacheName)` 강제 |
| 성능 목표 | Lighthouse PWA 점수 100점 달성 | 초기 페인팅(FCP) 1초 이내 단축 및 완전 오프라인 서빙 |

---

## 출제 이력과 검증 출처

- 정보관리기술사 116회 1교시: Progressive Web App(PWA)의 개념과 Service Worker의 역할

## 연결 토픽

- [웹 성능 최적화 기법](./164_web_performance_optimization.md)
- [메시지 큐(Message Queue)](./140_message_queue.md)
- [CSS 스프라이트(Sprite) 기법](./158_sprite.md)
- [반응형 웹(Responsive Web)](./110_responsive_web.md)
