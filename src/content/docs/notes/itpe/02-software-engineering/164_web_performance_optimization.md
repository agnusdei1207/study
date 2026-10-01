---
title: "웹 성능 최적화(Web Performance Optimization)"
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

## Ⅰ. 웹 성능 최적화의 개요

- **개념** : 웹 브라우저가 사용자의 요청에 따라 웹 페이지의 HTML, CSS, JavaScript, 이미지 등 리소스를 네트워크를 통해 다운로드하고, 파싱 및 렌더링 과정을 거쳐 사용자 화면에 완전히 표시될 때까지의 전 구간 지연시간을 최소화하는 프론트엔드 및 네트워크 엔지니어링 기법.
- **배경 및 필요성** : 페이지 로딩이 1초 지연될 때마다 사용자 전환율 $7\%$ 감소, 이탈률 급증 등 비즈니스 매출과 직결되며, 구글 검색엔진 최적화(SEO)의 필수 랭킹 요소로 작용.
- **핵심 표준** : 구글 Core Web Vitals (LCP, INP, CLS).

## Ⅱ. 중요 렌더링 경로(Critical Rendering Path) 및 Core Web Vitals

```text
   [ 1. HTML 파싱 ] ──> [ DOM 트리 생성 ]
                               │
                               ▼
   [ 2. CSS 파싱 ]  ──> [ CSSOM 트리 생성 ] ──> [ 3. 렌더 트리 결합 (Render Tree) ]
                                                            │
                                                            ▼
                                                [ 4. 레이아웃 (Layout / Reflow) ]
                                                - 요소의 정확한 크기와 위치 계산
                                                            │
                                                            ▼
                                                [ 5. 페인트 및 합성 (Paint / Composite) ]
                                                - 픽셀 래스터화 및 GPU 레이어 합성
```

- **구글 Core Web Vitals 3대 지표** :
  - **LCP (Largest Contentful Paint)** : 뷰포트 내 가장 큰 콘텐츠(이미지, 텍스트 블록)가 렌더링되는 시간 (목표: $2.5초 이하$).
  - **INP (Interaction to Next Paint)** : 사용자의 클릭, 키보드 조작 후 다음 화면 프레임이 브라우저에 표시될 때까지의 반응성 (목표: $200ms 이하$).
  - **CLS (Cumulative Layout Shift)** : 리소스 비동기 로딩 등으로 인해 페이지 레이아웃이 예기치 않게 덜컹거리는 시각적 불안정성 (목표: $0.1 이하$).

## Ⅲ. 웹 성능 최적화 4대 계층별 기법

| 최적화 계층 | 핵심 적용 기술 및 기법 | 구체적 효과 |
|---|---|---|
| 네트워크 계층 | CDN 엣지 캐싱, HTTP/2 및 HTTP/3(QUIC) 채택, DNS 사전 조회(`dns-prefetch`) | RTT 지연 단축, TCP 핸드셰이크 최소화 |
| 자원 크기 계층 | Brotli/Gzip 텍스트 압축, WebP/AVIF 차세대 이미지 포맷, 트리쉐이킹(Tree Shaking) | 전송 페이로드 용량 60~80% 절감 |
| 브라우저 파싱 계층 | JS 비동기 로딩(`defer` / `async`), CSS 상단 배치, 중요 CSS 인라인화(Critical CSS) | 렌더링 차단 리소스(Render-Blocking) 제거 |
| 렌더링 실행 계층 | CSS `content-visibility: auto`, 레이아웃 스레싱 방지, GPU 가속(`transform`, `opacity`) | 리플로우(Reflow) 억제, 60fps 렌더링 유지 |

## Ⅳ. 지속 가능한 프론트엔드 성능 관리를 위한 기술사적 제언

- **Lighthouse CI 기반의 성능 예산(Performance Budget) 자동화** : 코드가 추가됨에 따라 성능이 야금야금 퇴보하는 현상을 방지하기 위해, 번들 크기 한도(예: 초기 JS 150KB 이하)와 Lighthouse 성능 점수 90점 이상을 CI 파이프라인의 빌드 게이트웨이로 강제.
- **이미지 및 동영상 레이아웃 이동(CLS)의 원천 차단** : 이미지 태그에 `width`, `height` 및 CSS `aspect-ratio`를 반드시 명시하여 이미지가 로드되기 전부터 브라우저가 화면 영역을 사전에 확보하도록 코딩 표준 준수 필수.
