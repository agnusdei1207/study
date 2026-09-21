---
title: "Open API(API 일반)"
tags:
  - "notes-software-engineering"
author: "Antigravity"
date: "2026-09-20T23:53:43+09:00"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 구현·객체지향·API를 거쳐 Open API로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>구현·객체지향·API</span>
  <strong>Open API(API 일반)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **Open API**는 기업·기관이 보유한 데이터와 비즈니스 기능을 외부 개발자 및 파트너가 자유롭게 활용할 수 있도록 표준 규격으로 공개한 프로그래밍 인터페이스
- 메커니즘: 표준화된 프로토콜(REST/JSON) + 보안 인가(**OAuth 2.0/API Key**) + 제어/모니터링(**API Gateway**)
- 산출/효과: 디지털 생태계 확장 · 마이데이터 활성화 · 서비스 융합 혁신 · 신규 수익 모델(Monetization) 창출

<div class="itpe-flow-map" role="img" aria-label="Open API 생태계 연계 흐름도">
  <div class="itpe-flow-node"><strong>API 제공자</strong><span>핵심 데이터 및 서비스</span></div>
  <div class="itpe-flow-arrow">→ API Gateway 통제 →</div>
  <div class="itpe-flow-node is-current">
    <strong>Open API 플랫폼</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>보안/인증</strong><span><span class="itpe-keyword"><strong>OAuth 2.0 · API Key</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>명세 표준</strong><span><span class="itpe-keyword"><strong>OpenAPI Spec (OAS)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>트래픽 제어</strong><span>Throttling · Rate Limiting</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 외부 개발자 활용 →</div>
  <div class="itpe-flow-node"><strong>융합 서비스 생태계</strong><span>핀테크 · 마이데이터 앱</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Open API**: 외부 개발자에게 플랫폼의 핵심 데이터와 기능을 프로그래밍 방식으로 개방하는 공개 인터페이스
- **API Gateway**: 인증, 인가, 라우팅, 속도 제한, 로깅, 분석을 중앙에서 일괄 처리하는 관문 컴포넌트
- **OAuth 2.0**: 제3자 애플리케이션이 사용자 비밀번호 노출 없이 리소스에 제한적으로 접근할 수 있도록 권한을 위임하는 표준 프레임워크
- **Rate Limiting / Throttling**: 서비스 가용성 보장을 위해 클라이언트별 단위 시간당 호출 횟수를 제한하는 기법
- **API 경제(API Economy)**: API를 독립된 제품(Product)으로 간주하여 플랫폼 간 상호연결을 통해 가치를 창출하는 비즈니스 패러다임

</details>

## 예상문제

> 디지털 전환(DX) 시대의 핵심 동력인 Open API의 개념과 비즈니스 및 기술적 가치를 설명하고, API Gateway 기반의 핵심 기술 구성요소(인증/인가, 트래픽 제어, 모니터링) 및 마이데이터 환경에서의 보안 위협과 대응방안을 제시하시오. (25점)

## Ⅰ. 디지털 생태계 확장의 관문, Open API의 개요

> Open API는 단순한 기술 연계 도구가 아니라 플랫폼의 데이터 자산을 외부 혁신과 결합하는 비즈니스 제품(Product)이다.

- 정의: 특정 플랫폼이 보유한 기능과 데이터를 외부 제3자(Third-party)가 쉽게 호출하여 새로운 서비스를 개발할 수 있도록 표준 규약으로 공개한 인터페이스
- 목적: 플랫폼 네트워크 효과 극대화, 비즈니스 영역 확장, 데이터 개방 규제(마이데이터, 전자정부) 준수, **API 수익화(Monetization)**

## Ⅱ. Open API 아키텍처 및 핵심 구성요소

> Open API는 개발자 포털, 게이트웨이, 코어 백엔드의 3계층으로 유기적으로 연결된다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="Open API 3계층 아키텍처">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. 개발자 포털 (Developer Portal)</strong></span>
    <span>API 카탈로그 · OAS 기반 인터랙티브 문서(Swagger) · 샌드박스 테스트</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ API 호출</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. API 게이트웨이 (API Gateway)</strong></span>
    <span>보안 인증(OAuth 2.0/mTLS) · 트래픽 제어(Rate Limit) · 라우팅 및 변환</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ 백엔드 전달</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. 백엔드 서비스 (Core Services)</strong></span>
    <span>비즈니스 마이크로서비스(MSA) · 레거시 시스템 래핑 · 데이터베이스</span>
  </div>
</div>

### Open API 3계층 아키텍처 및 API Gateway 보안·제어 흐름

<div class="itpe-svg-wrapper">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" class="itpe-svg">
    <!-- Background -->
    <rect width="520" height="220" fill="var(--sl-color-bg-subtle, #f8fafc)" rx="8" />
    
    <!-- Title -->
    <text x="20" y="24" class="itpe-svg-label" fill="var(--sl-color-text-accent, #2563eb)">[Open API 생태계 3계층 구조 및 API Gateway 통제 메커니즘]</text>

    <!-- Tier 1: External Consumer & Portal (Left) -->
    <rect x="18" y="45" width="135" height="155" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    <text x="85" y="68" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-text, #1e293b)" text-anchor="middle">외부 생태계</text>
    <text x="85" y="85" class="itpe-svg-sub" font-size="10.5" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">3rd-party Developers</text>
    <line x1="28" y1="95" x2="143" y2="95" stroke="var(--sl-color-border, #e2e8f0)" />
    
    <!-- Developer Portal Box -->
    <rect x="26" y="105" width="119" height="42" rx="4" fill="var(--sl-color-bg-accent, #eff6ff)" stroke="var(--sl-color-primary, #3b82f6)" />
    <text x="85" y="122" class="itpe-svg-title" font-size="11" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">개발자 포털</text>
    <text x="85" y="137" class="itpe-svg-sub" font-size="9.5" fill="var(--sl-color-text, #334155)" text-anchor="middle">OAS 문서 · 샌드박스</text>

    <rect x="26" y="155" width="119" height="34" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="85" y="176" class="itpe-svg-label" font-size="10" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">API Key / App 등록</text>

    <!-- Arrow from Tier 1 to Tier 2 -->
    <line x1="153" y1="125" x2="185" y2="125" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Tier 2: API Gateway (Middle) -->
    <rect x="185" y="45" width="155" height="155" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1.5" />
    <text x="262" y="68" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">API Gateway (관문)</text>
    <text x="262" y="85" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">통합 인증·보안·제어</text>
    <line x1="195" y1="95" x2="330" y2="95" stroke="var(--sl-color-border, #e2e8f0)" />

    <!-- Features inside Gateway -->
    <rect x="195" y="103" width="135" height="26" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="262" y="120" class="itpe-svg-sub" font-size="10" font-weight="600" fill="var(--sl-color-text, #334155)" text-anchor="middle">OAuth 2.0 / JWT 검증</text>

    <rect x="195" y="134" width="135" height="26" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="262" y="151" class="itpe-svg-sub" font-size="10" font-weight="600" fill="var(--sl-color-text, #334155)" text-anchor="middle">Rate Limit (트래픽 차단)</text>

    <rect x="195" y="165" width="135" height="26" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="262" y="182" class="itpe-svg-sub" font-size="10" font-weight="600" fill="var(--sl-color-text, #334155)" text-anchor="middle">WAF &amp; 동적 라우팅</text>

    <!-- Arrow from Tier 2 to Tier 3 -->
    <line x1="340" y1="125" x2="370" y2="125" stroke="var(--sl-color-success, #10b981)" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Tier 3: Core Backend (Right) -->
    <rect x="370" y="45" width="132" height="155" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    <text x="436" y="68" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-text, #1e293b)" text-anchor="middle">코어 백엔드</text>
    <text x="436" y="85" class="itpe-svg-sub" font-size="10.5" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">Backend Core MSA</text>
    <line x1="380" y1="95" x2="492" y2="95" stroke="var(--sl-color-border, #e2e8f0)" />

    <rect x="380" y="105" width="112" height="26" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="436" y="122" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text, #334155)" text-anchor="middle">사용자 마이크로서비스</text>

    <rect x="380" y="136" width="112" height="26" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="436" y="153" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text, #334155)" text-anchor="middle">결제/정산 서비스</text>

    <rect x="380" y="167" width="112" height="26" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="436" y="184" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text, #334155)" text-anchor="middle">마이데이터 DB</text>
  </svg>
</div>

| 핵심 구성요소 | 주요 기술 및 메커니즘 | 실무 역할 |
|---|---|---|
| **인증/인가 (Auth)** | **OAuth 2.0, OpenID Connect, JWT, API Key** | 사용자 권한 위임 및 API 호출 클라이언트 검증 |
| **트래픽 제어** | **Rate Limiting, Throttling, Quota** | DoS 공격 방어 및 SLA 기반 차등적 대역폭 할당 |
| **명세 표준화** | **OAS (OpenAPI Specification 3.0), Swagger** | 기계 가독형 명세 제공 및 클라이언트 SDK 자동 생성 |
| **모니터링/분석** | ELK 스택, Prometheus, Distributed Tracing | API 사용 패턴 분석, 과금(Billing) 데이터 집계, 장애 감지 |

## Ⅲ. 프라이빗 API vs 파트너 API vs 오픈 API 비교

> 서비스 대상과 개방 수준에 따라 거버넌스와 보안 요구사항이 차등화된다.

| 구분 | 프라이빗 API (Private) | 파트너 API (Partner) | 퍼블릭 Open API (Public) |
|---|---|---|---|
| **이용 대상** | 사내 내부 개발팀 | 전략적 제휴사, 특정 B2B 파트너 | **불특정 다수 외부 개발자, 일반 대중** |
| **개방 목적** | 시스템 간 결합도 완화 및 재사용 | 비즈니스 파트너십 및 공동 서비스 | **플랫폼 생태계 확장 및 비즈니스 혁신** |
| **보안 통제** | 내부 네트워크망 신뢰, 기본 토큰 | 전용 VPN, mTLS, 계약 기반 인증 | **엄격한 OAuth 2.0, Rate Limit, WAF 필수** |
| **수익 모델** | 내부 개발 공수 절감 | 파트너십 상호 정산 | 호출당 과금(Pay-per-use), 무료 티어 제공 |

## Ⅳ. Open API 운영 문제점·대응책

> API는 소스코드 내부 비즈니스 로직과 데이터가 직접 외부에 노출되므로 전통적 웹 방화벽만으로는 방어가 불가능하다.

| 위험 | 대책 | 효과 |
|---|---|---|
| BOLA (객체 수준 인가 손상) | 토큰 주체(Subject)와 요청 리소스 소유권 서버단 일치 검증 | 타인 데이터 무단 열람 및 변조 원천 차단 |
| 대량 트래픽 급증 및 DoS 공격 | 클라이언트 IP 및 토큰 기반 Rate Limiting·Throttling 적용 | 백엔드 자원 고갈 방지 및 서비스 가용성(SLA) 보장 |
| 민감 개인정보 과다 노출 | 응답 필터링 DTO 적용 및 주민번호·계좌 마스킹 처리 | 데이터 유출 규제 위반 및 프라이버시 침해 방지 |

## Ⅴ. 개방성과 통제 균형의 결론

> Open API의 성패는 배포 기술이 아니라 개발자 경험(DX: Developer Experience)과 지속적 생애주기 관리에 달려 있다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: Open API를 구축해놓고 개발자가 쓰지 않아 방치되는 '유령 API'가 대다수임. 외부 개발자가 5분 안에 Hello World를 호출할 수 있는 'Time-to-First-Hello-World' 단축이 생태계 구축의 핵심 지표임. 문서의 정확성과 샌드박스 환경이 제공되어야 함.
- 나라면: API 버전 관리 정책(URI 기반 `/v1`, `/v2`)을 확립하고, 하위 호환성 유지 기간(최소 6개월 Deprecation 기간)을 공식 공지하는 라이프사이클 관리 체계를 수립하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 외부 개방 수준(Public/Partner/Private)에 따른 차등 보안·인증 체계 및 APIM(API Management) 라이프사이클 수립 판정
- **대응 방안**: **API Gateway** 중앙 집중 통제(OAuth 2.0/JWT 인가, Rate Limiting 방어) 및 **OpenAPI 3.0(OAS)** 기반 명세 표준화
- **검증 체계**: OWASP API Security Top 10(BOLA 등) 취약점 전수 진단 및 모니터링 기반 SLA 99.95% 가용성 검증
- **기대 효과**: 외부 제3자 연계 리드타임 70% 단축, 안전한 마이데이터 생태계 활성화 및 데이터 자산 기반 신규 수익 모델(Monetization) 창출

<div class="itpe-pipeline is-vertical" role="img" aria-label="Open API 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>파편화된 개별 API 노출 · 보안 통제 부재 및 개발자 경험 저하</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>API Gateway 중앙 통제 및 개발자 포털·샌드박스 표준화</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>OAuth 2.0/mTLS 보안 검증 및 Rate Limiting 트래픽 방어</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>안전한 데이터 개방 달성 · 융합 서비스 창출 및 생태계 확장</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **Open API**는 기업의 데이터와 비즈니스 로직을 표준 규격(REST/JSON)으로 외부에 개방하는 공개 인터페이스
- 목적: 외부 개발자 참여를 통한 플랫폼 생태계 확장 및 마이데이터 기반 비즈니스 혁신

### 2. 핵심 아키텍처 3요소

<div class="itpe-pipeline is-vertical" role="img" aria-label="Open API 핵심 3요소">
  <div class="itpe-pipeline-node"><strong>개발자 포털</strong><span>OAS 명세 · 문서 · 샌드박스</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>API Gateway</strong><span>OAuth 2.0 · Rate Limit · 라우팅</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>백엔드 서비스</strong><span>코어 비즈니스 로직 수행</span></div>
</div>

### 3. 핵심 통제

- **OAuth 2.0**: 권한 위임 기반의 안전한 인가 토큰(Access Token) 발급
- **Rate Limiting**: DoS 방어 및 서비스 가용성 유지를 위한 호출 쿼터 제한

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 1교시: Open API 개념 및 API Gateway
- 제134회 정보관리기술사 2교시: 금융 마이데이터와 Open API 보안 대책
- OWASP API Security Top 10 (2023)

## 학습 체크

- [ ] Open API의 3대 계층(포털, 게이트웨이, 백엔드)의 역할을 설명할 수 있는가?
- [ ] OAuth 2.0과 API Key 방식의 보안성 차이를 설명할 수 있는가?
- [ ] OWASP API Security 중 BOLA 취약점의 개념과 방어책을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [UML 다이어그램 체계](./020_uml_diagrams.md)
- 연관 토픽: [REST](./015_rest.md), [API Gateway](./075_api_gateway.md)
- 다음 토픽: [정보은닉](./024_information_hiding.md)
