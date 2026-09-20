---
title: "웹 성능 최적화(Web Performance Optimization)"
category: "02-software-engineering"
tags:
  - "웹성능최적화"
  - "CoreWebVitals"
  - "LCP"
  - "INP"
  - "CLS"
  - "CRP"
  - "렌더링최적화"
  - "트리셰이킹"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 웹 아키텍처와 성능 엔지니어링을 거쳐 웹 성능 최적화로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>웹 아키텍처·성능 엔지니어링</span>
  <strong>웹 성능 최적화(Web Performance Optimization)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 브라우저의 중요 렌더링 경로(Critical Rendering Path)와 네트워크 자원 전송 파이프라인 전반을 분석하여, 사용자가 첫 화면을 인지하고 인터랙션하기까지의 시간(LCP, INP)을 최소화하고 화면의 시각적 흔들림(CLS)을 제거하는 전주기 웹 엔지니어링 최적화 체계
- 메커니즘: Lighthouse 기반 성능 계측 $\rightarrow$ 전송 계층 최적화(HTTP/2·3, CDN, Brotli) $\rightarrow$ 리소스 최적화(트리 셰이킹, WebP/AVIF) $\rightarrow$ 브라우저 렌더링 최적화(CSSOM 블로킹 제거, GPU 합성) $\rightarrow$ Core Web Vitals 통과 판정
- 산출물: 성능 진단 보고서(Lighthouse Audit) · 번들 시각화 분석서(Bundle Analyzer) · 성능 예산 규칙서(Performance Budget)

<div class="itpe-flow-map" role="img" aria-label="웹 성능 최적화 및 Core Web Vitals 검증 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 성능 측정 및 병목 프로파일링</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>계측</strong><span>Lighthouse 및 Chrome DevTools를 통해 LCP, INP, CLS 실측치 추출</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 네트워크 및 리소스 전송 가속</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>가속</strong><span>CDN 엣지 캐싱, Brotli 압축, `<link rel="preload">` 핵심 자원 선제 다운로드</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 브라우저 중요 렌더링 경로(CRP) 최적화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>최적화</strong><span>자바스크립트 비동기화(`defer`/`async`), CSS 블로킹 제거, GPU 레이어 합성</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: Core Web Vitals 적합성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>LCP(≤2.5초), INP(≤200ms), CLS(≤0.1) 3대 핵심 품질 기준을 만족하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (성능 Baseline 충족)</strong>
      <span>배포 승인 $\rightarrow$ 검색 엔진 최적화(SEO) 상위 랭크 및 고객 이탈률 최소화</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (임계치 초과)</strong>
      <span>배포 차단 $\rightarrow$ 이미지 WebP 차세대 변환 및 번들 트리 셰이킹(Tree-Shaking) 재수행</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Core Web Vitals**: 구글이 웹 페이지의 사용자 경험을 정량적으로 계측하기 위해 표준화한 3대 지표(LCP: 로딩 성능, INP: 인터랙션 반응성, CLS: 시각적 안정성)
- **중요 렌더링 경로(CRP)**: 브라우저가 HTML, CSS, JavaScript 바이트를 수신하여 화면의 픽셀로 변환하기까지 거치는 5단계 과정(DOM $\rightarrow$ CSSOM $\rightarrow$ Render Tree $\rightarrow$ Layout $\rightarrow$ Paint)
- **트리 셰이킹(Tree-Shaking)**: ES 모듈 시스템(`import`/`export`)의 정적 구조를 분석하여 실제 호출되지 않는 무용 코드(Dead Code)를 빌드 번들에서 자동 제거하는 기법
- **Reflow vs Repaint**: 레이아웃 위치/크기가 바뀌어 전체 기하학적 구조를 재계산하는 연산(Reflow)과, 색상 등 시각적 변화만 다시 그리는 연산(Repaint)
</details>

## 1. 개요 및 필요성

### 모던 웹의 비대화(Bloatware)와 비즈니스 파급 효과

단일 페이지 애플리케이션(SPA)의 확산과 수많은 서드파티 마케팅 라이브러리 추가로 인해 웹 애플리케이션의 번들 크기가 수 메가바이트로 폭증했다. 아마존의 연구에 따르면 페이지 로딩 시간이 0.1초 지연될 때마다 전자상거래 매출이 1% 감소하며, 모바일 사용자의 53%는 로딩이 3초 이상 걸리면 사이트를 즉각 이탈한다.

구글은 사용자 체감 품질을 검색 순위 평가에 직접 반영하는 **Core Web Vitals**를 도입하였으며, 웹 성능 최적화는 단순한 코드 정리를 넘어 **SEO(검색 노출)와 비즈니스 생존을 좌우하는 필수 엔지니어링 과제**가 되었다.

### 구글 Core Web Vitals 3대 지표 규격

| 지표 | 정식 명칭 | 측정 대상 | 권장 기준 (Good) | 개선 필요 (Poor) |
|---|---|---|---|---|
| **LCP** | Largest Contentful Paint | **로딩 성능 (가장 큰 콘텐츠 렌더링 시간)** | **2.5초 이하** | 4.0초 초과 |
| **INP** | Interaction to Next Paint | **응답 반응성 (클릭/키보드 입력 반응 지연)** | **200ms 이하** | 500ms 초과 |
| **CLS** | Cumulative Layout Shift | **시각적 안정성 (콘텐츠의 예기치 않은 밀림)** | **0.1 이하** | 0.25 초과 |

## 2. 아키텍처 및 핵심 메커니즘

### 브라우저 중요 렌더링 경로(CRP)와 최적화 접점

```text
+-------------------------------------------------------------------------+
|                  브라우저 중요 렌더링 경로(CRP) 및 최적화 포인트         |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ HTML 바이트 ] ──> [ DOM 트리 생성 ] ────────┐                         |
|                             │                  │                         |
|  [ CSS 바이트  ] ──> [ CSSOM 트리 생성 ] ──────┴─> [ 렌더 트리 (Render Tree) ]
|                             │                                  │         |
|  * 최적화:                  * 최적화:                          v         |
|    - HTML 조기 스트리밍       - Non-critical CSS 비동기화      [ 레이아웃 ] |
|    - script defer/async      - Critical CSS 인라인             (Reflow)  |
|                                                                │         |
|                                                                v         |
|                                                            [ 페인트 ]    |
|                                                            (Repaint)     |
|                                                                │         |
|                                                                v         |
|                                                            [ 합성 ]      |
|                                                            (Composite)   |
|                                                                          |
|  * Composite 최적화: transform, opacity 속성 사용 ──> GPU 하드웨어 가속  |
+-------------------------------------------------------------------------+
```

### 4대 계층별 웹 성능 최적화 전략

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 네트워크 계층</strong></span>
      <span class="itpe-badge">전송 지연 단축</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>CDN 엣지 서버 캐싱 및 정적 자산 분산 배포</li>
        <li>HTTP/2 다중화(Multiplexing) 및 HTTP/3 QUIC 프로토콜 도입</li>
        <li>Brotli/Gzip 알고리즘을 통한 텍스트 리소스 압축 전송</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 리소스 계층</strong></span>
      <span class="itpe-badge">용량 경량화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>Webpack/Vite 기반 정적 모듈 트리 셰이킹(Tree-Shaking)</li>
        <li>이미지 차세대 포맷(WebP, AVIF) 전환 및 지연 로딩(`loading="lazy"`)</li>
        <li>웹 폰트 깜빡임 방지를 위한 `font-display: swap` 적용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 파싱·실행 계층</strong></span>
      <span class="itpe-badge">블로킹 해소</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>자바스크립트 비동기 로딩(`defer`, `async`)으로 파서 차단 방지</li>
        <li>코드 분할(Code Splitting) 및 동적 임포트를 통한 초기 번들 축소</li>
        <li>웹 워커(Web Worker) 도입으로 무거운 연산의 백그라운드 격리</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 렌더링 계층</strong></span>
      <span class="itpe-badge">CPU 부하 최소화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>`top/left` 대신 `transform`, `opacity`로 GPU 레이어 합성 유도</li>
        <li>DOM 조작 일괄 처리(`requestAnimationFrame`)로 강제 동기식 레이아웃 방지</li>
        <li>이미지 및 광고 컨테이너에 명시적 크기 예약으로 CLS 차단</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 대용량 메인 비주얼 이미지 다운로드 지연으로 모바일 LCP가 5초를 초과하여 구글 검색 순위 하락 | WebP 포맷 변환, 반응형 `srcset` 적용 및 `<link rel="preload">`로 우선 순위 상향 | LCP 1.8초로 단축 및 Good 등급 확보 |
| 폰트 및 늦게 로딩된 배너 때문에 텍스트와 버튼이 아래로 덜컥 밀려 오클릭 발생(CLS 불합격) | 이미지 및 iframe 영역에 CSS `aspect-ratio` 사전 할당 및 폰트 사전 로딩(preload) | CLS 수치 0.03으로 안정화 및 오클릭 방지 |
| 수십 개의 외부 마케팅 트래커 스크립트가 메인 스레드를 장시간 점유하여 클릭 반응(INP) 지연 | Google Tag Manager 비동기 지연 실행 및 고부하 연산 작업의 Web Worker 이관 | 인터랙션 지연(INP) 120ms 이내 보장 |

## 4. 기술사 답안 차별화 포인트

### FID에서 INP(Interaction to Next Paint)로의 표준 전환 분석

2024년 3월부터 구글은 최초 1회 클릭 반응만 보던 FID(First Input Delay)를 폐기하고, 사용자가 페이지에 머무는 동안 발생하는 **모든 클릭·탭·키보드 인터랙션의 지연시간을 누적 평가하는 INP**를 Core Web Vitals 정식 지표로 승격시켰다. 자바스크립트 Long Task(50ms 이상 실행 블록)를 `scheduler.yield()`나 `setTimeout`으로 쪼개어 브라우저 메인 스레드에 숨 쉴 틈을 주는 현대적 코드 아키텍처를 제시하여 최신 동향 전문성을 부각한다.

### CI/CD 내 성능 예산(Performance Budget) 거버넌스 자동화

개발자가 기능을 추가할 때마다 번들 크기가 야금야금 늘어나는 현상을 방지하기 위해, **Lighthouse CI**를 도입하여 배포 파이프라인에서 성능 예산을 강제화해야 한다. "초기 JS 번들 300KB 초과 시 빌드 실패", "LCP 2.5초 초과 시 PR 머지 차단"과 같은 **정량적 성능 거버넌스 게이트**를 운영 모델로 제언한다.

## 5. 참고 및 연계 학습

- [서비스 워커(Service Worker)](./147_service_worker.md)
- [스프라이트(Sprite) 최적화](./158_sprite.md)
- [성능 요구사항(Performance Requirement)](./149_performance_requirement.md)
- [성능 테스트(Performance Test)](./191_performance_test.md)
