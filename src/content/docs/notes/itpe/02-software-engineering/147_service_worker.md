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
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 웹 아키텍처와 클라이언트 엔지니어링을 거쳐 서비스 워커로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>웹 아키텍처·클라이언트 엔지니어링</span>
  <strong>서비스 워커(Service Worker)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 웹 브라우저의 메인 UI 스레드와 완전히 분리되어 백그라운드에서 동작하는 프로그래밍 가능한 네트워크 프록시 스크립트로, 오프라인 캐싱·백그라운드 동기화·푸시 알림을 제공하여 웹 애플리케이션의 신뢰성을 네이티브 앱 수준으로 끌어올리는 PWA(Progressive Web Apps) 핵심 기술
- 메커니즘: 서비스 워커 스크립트 브라우저 등록(Register) $\rightarrow$ 정적 리소스 사전 캐싱 및 설치(Install) $\rightarrow$ 구버전 캐시 정리 및 활성화(Activate) $\rightarrow$ 런타임 네트워크 요청 가로채기(Fetch Intercept) 및 캐시 반환
- 산출물: 서비스 워커 스크립트(`sw.js`) · 웹앱 매니페스트(`manifest.json`) · 캐시 전략 설정서(Workbox Config)

<div class="itpe-flow-map" role="img" aria-label="서비스 워커 생명주기 및 네트워크 프록시 처리 절차">
  <div class="itpe-flow-node">
    <strong>1단계: 서비스 워커 등록 (Register)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>등록</strong><span>메인 스레드에서 브라우저 백그라운드로 스크립트 비동기 다운로드 및 등록</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 설치 및 사전 캐싱 (Install)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설치</strong><span>앱 셸(App Shell: HTML/CSS/JS) 핵심 정적 자산을 Cache Storage에 선제 적재</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 활성화 및 구버전 캐시 정리 (Activate)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>활성화</strong><span>이전 버전 캐시를 삭제하고 클라이언트 제어권 획득 (`clients.claim()`)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 네트워크 요청 처리 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>요청된 리소스가 Cache Storage에 존재하며 유효(Valid)한가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Cache Hit)</strong>
      <span>로컬 Cache Storage에서 즉시 반환 $\rightarrow$ 오프라인 0ms 응답 완료</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (Cache Miss / Stale)</strong>
      <span>원격 서버로 네트워크 fetch 요청 전송 $\rightarrow$ 응답 수신 후 로컬 캐시 갱신</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Service Worker(서비스 워커)**: 브라우저가 백그라운드에서 실행하는 독립 스크립트로, 웹 페이지와 네트워크 사이의 중간자로서 요청을 가로채고 수정할 수 있는 이벤트 기반 워커
- **Cache Storage API**: 서비스 워커 스코프 내에서 네트워크 요청(Request)과 응답(Response) 객체 쌍을 영구적으로 저장하고 검색할 수 있는 비동기 스토리지
- **App Shell 모델**: 웹 애플리케이션의 핵심 UI 골격(HTML, CSS, 기본 자바스크립트)을 로컬에 미리 캐싱해 두고, 동적 데이터만 네트워크를 통해 주입받는 아키텍처 패턴
- **Workbox**: 구글에서 개발한 프로덕션급 서비스 워커 라이브러리로, 캐싱 전략·사전 캐싱·백그라운드 동기화를 선언적으로 구현할 수 있도록 표준화한 도구
</details>

## 1. 개요 및 필요성

### 전통적 웹 브라우저의 오프라인 취약점과 서비스 워커의 등장

전통적인 웹 애플리케이션은 네트워크 연결이 불안정하거나 끊기면 브라우저의 접속 오류 화면(공룡 화면)을 출력하며 즉각 동작을 멈춘다. 브라우저 내장 HTTP 캐시는 만료 기간(TTL) 기반으로만 수동 동작하므로 정밀한 오프라인 제어나 동적 데이터 캐싱이 불가능했다.

서비스 워커는 웹 페이지와 물리적 네트워크 사이에 위치하는 **"프로그래밍 가능한 네트워크 프록시"** 역할을 수행하여, 네트워크 단절 상황에서도 로컬 캐시를 반환해 웹 애플리케이션을 중단 없이 실행할 수 있도록 보장한다.

### 서비스 워커 vs 웹 워커 vs 웹소켓 비교

| 구분 | 서비스 워커 (Service Worker) | 웹 워커 (Web Worker) | 웹소켓 (WebSocket) |
|---|---|---|---|
| **동작 위치** | 브라우저 백그라운드 독립 스레드 | 브라우저 백그라운드 독립 스레드 | 브라우저 메인 스레드 연동 통신 계층 |
| **주요 목적** | **네트워크 프록시, 오프라인 캐시, 푸시 알림** | **고부하 CPU 연산(수학 연산, 암호화, 이미지 처리)** | **실시간 양방향 전이중(Full-Duplex) 데이터 통신** |
| **수명 주기** | 이벤트 기반 실행 후 유휴 시 자동 종료/재기동 | 메인 페이지와 수명을 함께함 (페이지 닫히면 종료) | 연결 수립(Handshake) 후 연결 유지 |
| **DOM 접근** | **불가 (postMessage 통신)** | **불가 (postMessage 통신)** | **불가 (콜백 함수를 통해 메인 스레드로 전달)** |
| **보안 요구** | **HTTPS 필수 (localhost 예외)** | 동일 출처 정책(SOP) 준수 | WSS(WebSocket Secure) 권장 |

## 2. 아키텍처 및 핵심 메커니즘

### 서비스 워커 네트워크 프록시 아키텍처

```text
+-------------------------------------------------------------------------+
|                  서비스 워커(Service Worker) 프록시 아키텍처            |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 웹 브라우저 페이지 (DOM / UI Thread) ]                               |
|        │                                                                |
|        │ 1. fetch(요청: HTML/CSS/API)                                   |
|        v                                                                |
|  +--------------------------------------------------------------------+ |
|  | [ 서비스 워커 (Service Worker Thread) ] (HTTPS 프록시)            | |
|  |   - 이벤트 핸들러: oninstall, onactivate, onfetch, onsync, onpush  | |
|  |   - 캐시 판정 엔진 (Cache Strategy Engine)                         | |
|  +───────┬────────────────────────────────────────────────────┬───────+ |
|          │                                                    │         |
|          │ 2-A. Cache Hit                                     │ 2-B.    |
|          v                                                    v Fetch   |
|  [ Cache Storage / IndexedDB ]                      [ 원격 웹 서버 / API ] |
|  (브라우저 로컬 저장소 - 0ms 응답)                  (Cloud / Origin Server)  |
|                                                                         |
|  * 4대 생명주기: Register ──> Install ──> Activate ──> Fetch (이벤트 대기) |
+-------------------------------------------------------------------------+
```

### 4대 런타임 캐싱 전략 (Caching Strategies)

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① Cache First</strong></span>
      <span class="itpe-badge">정적 자산 최적화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>캐시를 먼저 확인하여 적중 시 즉시 반환하고, 부재 시에만 네트워크 호출</li>
        <li>이미지, 폰트, 빌드된 CSS/JS 등 해시가 부여된 불변 자산에 적용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② Network First</strong></span>
      <span class="itpe-badge">실시간 데이터 최적화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>항상 네트워크 조회를 우선 시도하며, 네트워크 오류 시에만 캐시된 데이터 반환</li>
        <li>최신성이 생명인 금융 계좌 잔액, 실시간 주문 현황 등에 적용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ Stale-While-Revalidate</strong></span>
      <span class="itpe-badge">사용자 경험(UX) 극대화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>캐시된 오래된 데이터(Stale)를 0초 만에 화면에 렌더링하면서 백그라운드 네트워크 동기화</li>
        <li>소셜 미디어 피드, 뉴스 목록, 사용자 프로필 화면에 적용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ Network Only / Cache Only</strong></span>
      <span class="itpe-badge">특수 보안 및 완전 격리</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>Network Only: 결제 승인 요청 등 캐싱이 절대 불가한 트랜잭션에 적용</li>
        <li>Cache Only: 오프라인 전용 안내 페이지 등 고정 에셋에 적용</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 프론트엔드 새 버전을 배포했으나 사용자가 브라우저를 재시작해도 구버전 JS/CSS가 고착 | `self.skipWaiting()`을 호출하여 대기(Waiting) 상태를 건너뛰고 활성화 단계에서 구버전 캐시 키 자동 삭제 | 신규 배포 코드의 클라이언트 즉시 반영 보장 |
| 서비스 워커가 네트워크 트래픽 전체를 가로챌 수 있어 스크립트 탈취 시 대규모 개인정보 유출 발생 | 개발 환경(`localhost`)을 제외한 전 운영 환경에 HTTPS 필수 적용 및 배포 스크립트 SRI(Subresource Integrity) 검증 | 중간자 공격(MitM) 및 악성 프록시 주입 차단 |
| 바닐라 자바스크립트로 캐시 로직을 직접 구현하다가 캐시 오염 및 메모리 누수 발생 | Google Workbox 라이브러리를 도입하여 정적 자산과 동적 라우팅 캐시 전략을 선언적으로 규격화 | 캐시 관리 코드 복잡도 70% 감소 및 안정성 확보 |

## 4. 기술사 답안 차별화 포인트

### 백그라운드 동기화(Background Sync API)를 통한 오프라인 트랜잭션 보장

사용자가 지하철 음영 지역이나 비행기 모드에서 게시글을 작성하거나 폼을 제출할 경우, 서비스 워커는 요청 데이터를 브라우저 **IndexedDB**에 안전하게 보관한다. 이후 브라우저가 다시 인터넷 연결을 감지하면 `sync` 이벤트를 트리거하여 백그라운드에서 자동으로 서버로 전송을 완료한다. 사용자가 앱을 닫더라도 브라우저 백그라운드에서 트랜잭션을 끝까지 완결시키는 메커니즘을 답안에 제시하면 높은 점수를 얻는다.

### 프로젝트 후구(Project Fugu)와 모바일 웹 생태계 혁신

구글이 주도하는 **Project Fugu(Capabilities Project)**와의 연계성을 강조한다. 서비스 워커를 기점으로 파일 시스템 접근(File System Access API), 블루투스 연동(Web Bluetooth), 로컬 알림(Push API) 등 과거 네이티브 앱의 전유물이었던 디바이스 기능들이 웹 표준으로 편입되고 있다. 서비스 워커는 단순한 캐시 계층을 넘어 **"웹이 네이티브 플랫폼을 대체하는 아키텍처 허브"**임을 결론부에서 강조한다.

## 5. 참고 및 연계 학습

- [PWA(Progressive Web Apps)](./149_performance_requirement.md)
- [메시지 큐(Message Queue)](./140_message_queue.md)
- [웹 성능 최적화 및 스프라이트](./158_sprite.md)
- [스프링 부트(Spring Boot) 백엔드 아키텍처](./159_spring_boot.md)
