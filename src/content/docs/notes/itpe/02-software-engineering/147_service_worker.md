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
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
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

### 서비스 워커 프록시 및 생명주기 아키텍처

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="sw-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Background Frame -->
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">서비스 워커 네트워크 프록시 및 4단계 생명주기</text>

    <!-- Main Page Thread -->
    <rect x="15" y="45" width="110" height="150" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="15" y="45" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="70" y="60" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">웹 페이지 (UI)</text>
    <text x="70" y="85" text-anchor="middle" font-size="7.5" fill="var(--color-text, #1e293b)">메인 UI 스레드</text>
    <text x="70" y="102" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">DOM 조작 / 렌더링</text>
    <text x="70" y="125" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">fetch() 요청</text>
    <text x="70" y="170" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">오프라인 화면 출력 차단</text>

    <!-- Arrow from UI to SW -->
    <line x1="125" y1="120" x2="155" y2="120" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#sw-arrow)"/>

    <!-- Service Worker Thread (Center) -->
    <rect x="160" y="45" width="180" height="150" rx="6" fill="var(--color-bg-subtle, #eff6ff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <rect x="160" y="45" width="180" height="22" rx="6" fill="var(--color-primary, #2563eb)"/>
    <text x="250" y="60" text-anchor="middle" font-size="8" font-weight="bold" fill="#ffffff">서비스 워커 (백그라운드 프록시)</text>
    
    <rect x="170" y="75" width="160" height="24" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="250" y="90" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">① Register ──> ② Install</text>

    <rect x="170" y="105" width="160" height="24" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="250" y="120" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">③ Activate (구캐시 삭제)</text>

    <rect x="170" y="135" width="160" height="50" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.2"/>
    <text x="250" y="152" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">④ Fetch 이벤트 가로채기</text>
    <text x="250" y="168" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">Cache Hit 여부 실시간 판정</text>

    <!-- Branch Arrows from SW -->
    <line x1="340" y1="100" x2="368" y2="75" stroke="#16a34a" stroke-width="1.4" marker-end="url(#sw-arrow)"/>
    <line x1="340" y1="150" x2="368" y2="165" stroke="var(--color-primary, #2563eb)" stroke-width="1.4" marker-end="url(#sw-arrow)"/>

    <!-- Storage (Right Top) -->
    <rect x="375" y="45" width="130" height="65" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#16a34a" stroke-width="1.2"/>
    <text x="440" y="65" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#16a34a">Cache Storage</text>
    <text x="440" y="80" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">로컬 저장소 (0ms)</text>
    <text x="440" y="95" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">오프라인 즉각 응답</text>

    <!-- Origin Server (Right Bottom) -->
    <rect x="375" y="130" width="130" height="65" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="440" y="150" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">원격 서버 (Cloud)</text>
    <text x="440" y="165" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">Network Fetch</text>
    <text x="440" y="180" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">최신 데이터 갱신</text>
  </svg>
</div>

### 4대 런타임 캐싱 전략 구조 비교

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <!-- Frame -->
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">서비스 워커 4대 런타임 캐싱 전략 (Workbox 표준)</text>

    <!-- Strategy 1 -->
    <rect x="15" y="42" width="115" height="135" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="15" y="42" width="115" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="72" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Cache First</text>
    <text x="72" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">캐시 우선 조회</text>
    <text x="72" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">부재 시 네트워크</text>
    <text x="72" y="125" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">적용: 이미지, 폰트</text>
    <text x="72" y="145" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">불변 정적 에셋</text>
    <text x="72" y="165" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#16a34a">[속도 최우선]</text>

    <!-- Strategy 2 -->
    <rect x="140" y="42" width="115" height="135" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="140" y="42" width="115" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="197" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Network First</text>
    <text x="197" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">네트워크 우선</text>
    <text x="197" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">실패 시 캐시 폴백</text>
    <text x="197" y="125" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">적용: 계좌/주문</text>
    <text x="197" y="145" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">최신성 필수 데이터</text>
    <text x="197" y="165" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-accent, #0284c7)">[정확도 우선]</text>

    <!-- Strategy 3 -->
    <rect x="265" y="42" width="115" height="135" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.4"/>
    <rect x="265" y="42" width="115" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="322" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Stale-While-Reval</text>
    <text x="322" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">구캐시 즉시 출력</text>
    <text x="322" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">+ 백그라운드 갱신</text>
    <text x="322" y="125" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">적용: 피드/뉴스</text>
    <text x="322" y="145" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">0초 화면 렌더링</text>
    <text x="322" y="165" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#ca8a04">[UX 극대화]</text>

    <!-- Strategy 4 -->
    <rect x="390" y="42" width="115" height="135" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="390" y="42" width="115" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="447" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Network Only</text>
    <text x="447" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">캐시 완전 배제</text>
    <text x="447" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">오직 원격 통신</text>
    <text x="447" y="125" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">적용: 결제/인증</text>
    <text x="447" y="145" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">보안 트랜잭션</text>
    <text x="447" y="165" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#ef4444">[보안 필수]</text>
  </svg>
</div>

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

## 5. 결론 및 종합 제언

### 학습자 통찰 메모 — 답안 밖

[핵심 통찰]
서비스 워커는 웹 브라우저를 '단순한 문서 뷰어'에서 **'오프라인에서도 동작하는 완전한 분산 런타임 플랫폼'**으로 변모시킨 웹 생태계 최대의 혁신이다. 네트워크 요청의 프록시 제어권이 브라우저 스크립트에 부여됨으로써, 웹은 네트워크 단절이라는 태생적 한계를 극복하고 네이티브 앱과 동등한 수준의 복원력과 속도를 획득했다.

나라면:
본 시험에서 서비스 워커가 출제되면, Register $\rightarrow$ Install $\rightarrow$ Activate의 3단계 생명주기와 4대 캐싱 전략을 표로 정리한 뒤 **(1) 지하철 음영 구간 트랜잭션을 보증하는 Background Sync API와 IndexedDB 결합, (2) 구버전 캐시 고착을 방어하는 `skipWaiting()`과 Workbox 자동화, (3) 웹의 경계를 허무는 Project Fugu 디바이스 API 융합**을 3단락에 명쾌하게 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 모바일 웹 서비스의 로딩 지연 시간(LCP) 2.5초 초과 및 오프라인 네트워크 단절 시 서비스 중단 발생 시 도입
- **대응 방안**: Google Workbox를 기반으로 App Shell(Cache First)과 동적 피드(Stale-While-Revalidate) 복합 전략 구축
- **검증 체계**: 배포 파이프라인에 `self.skipWaiting()` 자동 주입 및 Lighthouse PWA 검사 항목 100점 달성 여부 검증
- **기대 효과**: 재방문자 로딩 시간 80% 단축(0ms 캐시 응답) 및 오프라인 환경에서도 핵심 비즈니스 연속성 완벽 보장

<div class="itpe-pipeline-container" role="region" aria-label="서비스 워커 기반 PWA 오프라인 캐싱 및 동기화 파이프라인">
  <div class="itpe-pipeline-header">
    <span class="itpe-pipeline-title">서비스 워커 기반 PWA 오프라인 캐싱 및 동기화 파이프라인</span>
    <span class="itpe-pipeline-badge">PWA 엔지니어링</span>
  </div>
  <div class="itpe-pipeline-grid">
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">1단계: 선제 적재</div>
      <div class="itpe-card-title">App Shell 캐싱</div>
      <div class="itpe-card-body">Install 단계에서 핵심 UI 골격(HTML/CSS/JS)을 Cache Storage에 사전 적재</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">2단계: 즉시 활성화</div>
      <div class="itpe-card-title">skipWaiting 처리</div>
      <div class="itpe-card-body">Activate 단계에서 구버전 캐시 정리 및 클라이언트 제어권 즉각 획득</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">3단계: 프록시 라우팅</div>
      <div class="itpe-card-title">Fetch 분기 제어</div>
      <div class="itpe-card-body">Workbox 기반 Cache First, Stale-While-Revalidate 선언적 분기 응답</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">4단계: 오프라인 보증</div>
      <div class="itpe-card-title">백그라운드 동기화</div>
      <div class="itpe-card-body">네트워크 단절 시 IndexedDB 적재 후 통신 복구 시 자동 백그라운드 전송</div>
    </div>
  </div>
</div>

## 6. 참고 및 연계 학습

- [웹 성능 최적화 기법](./164_web_performance_optimization.md)
- [메시지 큐(Message Queue)](./140_message_queue.md)
- [CSS 스프라이트(Sprite) 기법](./158_sprite.md)
- [반응형 웹(Responsive Web)](./110_responsive_web.md)
