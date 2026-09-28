---
title: "웹 성능 최적화(Web Performance Optimization)"
category: "02-software-engineering"
tags:
  - "웹성능"
  - "CoreWebVitals"
  - "LCP"
  - "INP"
  - "CLS"
  - "CRP"
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

소프트웨어 공학 → 웹 아키텍처·클라이언트 엔지니어링 → 웹 성능 최적화(Web Performance Optimization)

## 지식 위치

소프트웨어공학 > 품질·성능 > 웹 성능 최적화

## 30초 인출

- 본질: 사용자가 웹 페이지를 요청한 순간부터 화면 렌더링, 상호작용 및 레이아웃 안정성에 이르는 전 과정을 Core Web Vitals 지표를 중심으로 분석하고 개선하는 프론트엔드/백엔드 최적화 활동
- 메커니즘: 실사용자 모니터링(RUM) 데이터 수집 → 주요 지표(LCP, INP, CLS) 측정 → 중요 렌더링 경로(CRP) 병목 분석(서버 응답, 렌더링 블로킹 JS/CSS, 메인 스레드 롱 태스크) → 리소스 최적화 및 비동기 처리 적용
- 통찰: 등급 점수 개선만을 목적으로 인위적 지연 로딩을 남발할 경우 뷰포트 내 핵심 콘텐츠 표시가 지연되므로 우선순위 힌트(fetchpriority) 및 성능 예산(Performance Budget) 기반 체계적 통제 필요

<details>
<summary>핵심 용어</summary>

- **Core Web Vitals** : 구글이 정의한 웹 사용자 경험의 3대 핵심 품질 척도로 로딩 속도(LCP), 상호작용 반응성(INP), 시각적 안정성(CLS)을 의미
- **LCP (Largest Contentful Paint)** : 사용자가 페이지 URL을 요청한 후 뷰포트 내에서 가장 큰 텍스트 블록이나 이미지/비디오가 화면에 렌더링되기까지 걸리는 시간 (2.5초 이하 권장)
- **INP (Interaction to Next Paint)** : 클릭, 탭, 키보드 입력 등 사용자 상호작용 발생 시 다음 프레임이 화면에 그려질 때까지 걸리는 지연 시간 (200ms 이하 권장, FID 대체)
- **CLS (Cumulative Layout Shift)** : 페이지 로드 중 예기치 않은 레이아웃 변경으로 인한 시각적 불안정성을 누적 수치화한 점수 (0.1 이하 권장)
- **CRP (Critical Rendering Path)** : 브라우저가 HTML, CSS, JavaScript를 수신하여 파싱 후 화면에 픽셀로 변환하는 일련의 렌더링 단계
- **성능 예산 (Performance Budget)** : JS 번들 크기, 이미지 용량, LCP 임계치 등을 설정하여 CI/CD 단계에서 성능 저하를 방지하는 거버넌스 척도
</details>

---

## 2~4교시 예상문제 (25점)

> 구글 Core Web Vitals의 3대 핵심 지표(LCP, INP, CLS)의 개념과 측정 원리를 설명하고, 브라우저의 중요 렌더링 경로(CRP) 최적화 및 엔터프라이즈 웹 성능 향상 방안을 기술하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 사용자가 웹 사이트에 접속하여 탐색하는 전 과정에서 로딩 지연, 상호작용 반응 지연, 화면 깜빡임/밀림 현상을 최소화하기 위해 네트워크, 리소스, 브라우저 렌더링 엔진을 종합 튜닝하는 기술 체계 |
| 목적 | 사용자 이탈률(Bounce Rate) 감소, 전환율(Conversion Rate) 증대, 검색엔진 최적화(SEO) 순위 향상 및 서버/네트워크 인프라 비용 절감 |

## Ⅱ. 핵심 특징

| 특징 | 세부 내용 |
|---|---|
| 사용자 중심의 체감 지표 | 단순 기술적 로드 완료(Window Load)가 아닌 실질적 사용자 경험을 대변하는 Core Web Vitals 중심 평가 |
| 계층적 병목 구조 | 백엔드 TTFB(Time to First Byte), 네트워크 전송(CDN/HTTP), 프론트엔드 CRP 파이프라인의 입체적 연계 |
| 실험실과 현장 데이터 상호보완 | 통제된 환경의 Lighthouse(Lab Data)와 실제 사용자 환경의 Chrome UX Report(CrUX/Field Data) 병행 분석 |
| 지속적 모니터링 필수 | 코드 배포 및 마케팅 스크립트 추가 시 쉽게 회귀하므로 성능 예산(Performance Budget) 기반 자동화 통제 필요 |

웹 비즈니스의 매출과 직결되는 핵심 엔지니어링 역량이자 디지털 경쟁력의 핵심 표준.

## Ⅲ. 체계·프로세스

```text
[1. 중요 렌더링 경로 (Critical Rendering Path) 단계]
  HTML 수신 ──► DOM 트리 구축 ──┐
                                ├─► 렌더 트리(Render Tree) 생성 ──► 레이아웃(Reflow) ──► 페인트(Repaint)
  CSS 수신  ──► CSSOM 트리 구축 ┘
       │
       ▼ (동기식 JS 실행 시 파싱 블로킹 발생)
[2. 주요 성능 지표 측정 구간]
  - TTFB (백엔드 처리 및 첫 바이트 수신)
  - FCP (첫 번째 텍스트/이미지 렌더링)
  - LCP (가장 큰 메인 히어로 이미지/배너 렌더링 완료) ──► 2.5초 이내 목표
  - INP (버튼 클릭 후 메인 스레드 태스크 처리 및 페인트) ──► 200ms 이내 목표
  - CLS (비동기 광고 로드로 인한 본문 밀림 점수) ────────► 0.1 이하 목표
       │
       ▼
[3. 최적화 전술 적용]
  - 네트워크: HTTP/3, CDN 엣지 캐싱, 폰트/DNS 사전 연결(preconnect)
  - 렌더링 차단 해소: Critical CSS 인라인, JS defer/async, 코드 스플리팅
  - 리소스 압축: WebP/AVIF 이미지 포맷, Brotli 텍스트 압축, 리소스 힌트
```

브라우저 CRP 처리 흐름에 따라 TTFB, LCP, INP, CLS의 병목 구간을 식별하고 리소스 최적화 및 비동기 파이프라인을 전개하는 프로세스.

## Ⅳ. 종류·비교

| 지표명 | 측정 대상 및 의미 | 정상 기준 | 주요 발생 원인 | 대표 최적화 기법 |
|---|---|---|---|---|
| **LCP (Largest Contentful Paint)** | 로딩 속도: 뷰포트 내 가장 큰 콘텐츠(히어로 이미지, 타이틀)가 완전히 그려진 시점 | 2.5초 이내 | 느린 서버 응답(TTFB), 렌더링 차단 리소스, 이미지 다운로드 지연 | CDN 적용, LCP 이미지 `fetchpriority="high"`, 중요 CSS 인라인 |
| **INP (Interaction to Next Paint)** | 반응성: 클릭, 탭 등 사용자 인터랙션 후 브라우저가 화면을 갱신하는 데 걸리는 최악 지연 | 200ms 이내 | 긴 메인 스레드 자바스크립트 실행(Long Task), 비대한 이벤트 핸들러 | Web Worker 분산, `scheduler.yield()`, 무거운 DOM 갱신 분할 |
| **CLS (Cumulative Layout Shift)** | 시각적 안정성: 페이지 로딩 중 예상치 못한 레이아웃의 급격한 이동 비율 합산 | 0.1 이하 | 이미지/광고의 width/height 미지정, 웹 폰트 로딩 시 FOIT/FOUT 현상 | 이미지 종횡비(`aspect-ratio`) 예약, `font-display: swap`, 동적 UI 공간 사전 확보 |

### 자바스크립트 로딩 방식 비교

| 로딩 방식 | HTML 파싱 동작 | 스크립트 실행 시점 | 적합한 스크립트 |
|---|---|---|---|
| **기본 (`<script>`)** | 스크립트 다운로드 및 실행 시점 동안 파싱 완전 중단 | 다운로드 즉시 메인 스레드 블로킹 실행 | 화면 렌더링에 절대적으로 필수적인 극소수 스크립트 |
| **비동기 (`async`)** | 백그라운드 병렬 다운로드, 다운로드 완료 즉시 파싱 중단 및 실행 | 다운로드 완료 즉시 (실행 순서 보장 불가) | Google Analytics 등 타 리소스와 의존성 없는 독립 스크립트 |
| **지연 (`defer`)** | 백그라운드 병렬 다운로드, HTML 파싱 완료 후 순차 실행 | DOMContentLoaded 이벤트 직전 (선언 순서대로 실행) | DOM 요소를 참조하는 일반적인 프론트엔드 비즈니스 애플리케이션 번들 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 개발자의 로컬 PC(고성능) 환경 측정 결과와 실제 모바일 저가 기기 사용자의 체감 성능 괴리 | Web-Vitals 라이브러리를 연동하여 실제 사용자 현장 데이터(RUM)를 수집하고 하위 75% 백분위수를 기준으로 튜닝 |
| LCP 최적화를 위해 첫 화면의 히어로 이미지에 무분별한 지연 로딩(`loading="lazy"`)을 적용하여 LCP 급격히 악화 | 뷰포트 첫 화면 메인 LCP 이미지는 지연 로딩을 반드시 제거하고 `fetchpriority="high"` 속성 명시 |
| 무거운 단일 페이지 애플리케이션(SPA)의 초기 번들 비대화로 인한 메인 스레드 점유 | 라우트 기반 코드 스플리팅(React.lazy / 동적 import)을 적용하고 SSR/SSG(Next.js 등) 하이브리드 아키텍처 도입 |

## Ⅵ. 제언

프론트엔드 빌드 파이프라인(CI/CD)에 Lighthouse CI 및 성능 예산(Performance Budget)을 통합하여 임계치 초과 시 자동 빌드 실패 처리하고, 실시간 RUM 메트릭을 APM과 연동하는 지속적 성능 거버넌스 확립 필요.

```text
[지속적 웹 성능 엔지니어링 파이프라인]
  Git PR → Lighthouse CI 성능 예산(Budget) 검증 → CDN 배포 → Datadog RUM 실시간 CrUX 메트릭 관측
```

| 관리 영역 | 전통적 최적화 | 현대적 Core Web Vitals 거버넌스 |
|---|---|---|
| 측정 대상 | 단순 Page Load Time, DOMContentLoaded | LCP (2.5s), INP (200ms), CLS (0.1) 실측치 |
| 통제 방식 | 오픈 직전 1회성 이미지 압축 | CI/CD 파이프라인 상의 번들 사이즈 및 RUM 자동 경보 |

---

## 출제 이력과 검증 출처

- 정보관리기술사 121회 1교시: 웹 브라우저의 렌더링 과정(CRP)과 최적화 기법

## 연결 토픽

- [서비스 워커(Service Worker)](./147_service_worker.md)
- [CSS 스프라이트(Sprite) 기법](./158_sprite.md)
- [성능 요구사항](./149_performance_requirement.md)
- [반응형 웹(Responsive Web)](./110_responsive_web.md)
