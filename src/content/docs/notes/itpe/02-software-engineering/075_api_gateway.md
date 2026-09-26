---
title: "API Gateway"
author: "Antigravity"
date: "2026-09-27T00:24:59+09:00"
tags:
  - "소프트웨어공학"
  - "APIGateway"
  - "MSA"
  - "마이크로서비스"
  - "BFF"
  - "서비스메시"
sidebar:
  badge:
    text: "서브"
    variant: "note"
extra:
  model: "GPT-6"
  keyword_grade: "서브"
---

> **로드맵 경로**: 소프트웨어공학 > 분산 시스템 및 아키텍처 > 마이크로서비스(MSA) > API Gateway

---

## 30초 인출

- 본질: **API Gateway**는 클라이언트와 백엔드 마이크로서비스 사이의 단일 진입점(Single Point of Entry)을 담당하는 역방향 프록시
- 메커니즘: 사전 필터(JWT·SSL 종료·유량 제어) → 라우팅 필터(서비스 디스커버리·LB·서킷 브레이커) → 사후 필터(TraceId 로깅)의 3단계 파이프라인
- 판정 기준: 외부 요청의 공통 경계에는 게이트웨이, 화면별 데이터 취합에는 BFF, 내부 서비스 통신 정책에는 서비스 메시를 검토

<details>
<summary>핵심 용어</summary>

- **API 게이트웨이(API Gateway)**: 모든 클라이언트 요청의 단일 진입점 역할을 수행하며 라우팅, 인증, 유량 제어를 총괄하는 리버스 프록시
- **BFF(Backend for Frontend)**: 모바일, 웹 등 특정 클라이언트의 UI/UX 화면 요구에 맞춰 API 응답 데이터를 최적 조합(Aggregation)하는 계층
- **유량 제어(Rate Limiting)**: Token Bucket 또는 Leaky Bucket 알고리즘을 활용하여 클라이언트별 초당 요청 수(TPS)를 제한하는 메커니즘
- **North-South 트래픽(North-South Traffic)**: 외부 클라이언트로부터 데이터센터 또는 VPC 내부 서비스로 유입되는 인그레스(Ingress) 트래픽
- **서비스 메시(Service Mesh)**: 마이크로서비스 간의 내부 통신(East-West)을 사이드카(Sidecar) 프록시로 중계하여 mTLS와 추적성을 제공하는 인프라

</details>

---

## 1교시 예상문제 (10점)

> API Gateway의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 클라이언트 요청을 백엔드 서비스로 중계하며 공통 API 처리를 제공하는 역방향 프록시 |
| 목적 | 서비스 주소와 공통 통신 정책을 클라이언트에서 분리 |

### Ⅱ. 요청 처리

| 단계 | 대표 기능 |
|---|---|
| 요청 전 | 인증·인가, 유량 제어 |
| 라우팅 | 경로·대상 서비스 선택 |
| 응답 후 | 로깅·응답 처리 |

제언: 외부 요청 경계와 내부 서비스 통신의 정책을 분리해 운영
---

### 핵심 관계

```text
클라이언트
    ↓ 단일 API 진입점
Gateway: 인증·유량 제어·라우팅
    ├─ 주문 서비스
    ├─ 결제 서비스
    └─ 회원 서비스

응답·오류·추적 정보 → Gateway → 클라이언트
```

---

## 2~4교시 예상문제 (25점)

> 마이크로서비스 환경에서 API Gateway의 역할과 주요 처리 흐름을 설명하고, BFF·서비스 메시와의 역할 구분 및 안정적인 운영 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 클라이언트 요청의 단일 진입점

| 구분 | 핵심 |
|---|---|
| 정의 | 클라이언트 요청을 백엔드 서비스로 중계하며 공통 API 처리를 제공하는 역방향 프록시 |
| 목적 | 서비스 주소와 공통 통신 정책을 클라이언트에서 분리 |

요청 경계에 인증·라우팅·유량 제어 정책을 적용하고, 응답에 필요한 공통 처리를 수행.
---

## Ⅱ. API Gateway의 핵심 아키텍처 및 5대 주요 기능

#### 1. API Gateway 3단계 필터 파이프라인 구조도

```text
클라이언트
    ↓ 단일 API 진입점
Gateway: 인증·유량 제어·라우팅
    ├─ 주문 서비스
    ├─ 결제 서비스
    └─ 회원 서비스

응답·오류·추적 정보 → Gateway → 클라이언트
```

#### 2. API Gateway의 5대 주요 기능

| 기능 영역 | 세부 역할 및 핵심 기술 | 실무 구현 사례 |
|---|---|---|
| **동적 라우팅 및 로드밸런싱** | 요청 경로/헤더에 따라 백엔드 인스턴스로 분기, 서비스 디스커버리(Eureka/K8s) 연계 | Spring Cloud Gateway, Kong, Envoy |
| **인증 및 인가 (Security)** | 클라이언트의 JWT 검증, API Key 유효성 체크, OAuth 2.0 토큰 인트로서펙션 | Keycloak 연동, OAuth 2.0 Resource Server |
| **유량 제어 (Rate Limiting)** | 클라이언트/IP/API별 초당 호출 수(TPS) 제한, 서비스 과부하 차단 | Token Bucket 알고리즘, Redis 분산 카운터 |
| **복원력 (Resilience)** | 백엔드 장애 시 빠른 실패(Fast Fail) 및 대체 응답(Fallback) 반환 | Resilience4j Circuit Breaker 연계 |
| **통합 관측성 (Observability)** | 전사 트랜잭션 추적을 위한 TraceId 발급 및 메트릭 수집 | OpenTelemetry, Prometheus, W3C TraceContext |
---

## Ⅲ. API Gateway vs BFF vs Service Mesh 비교

| 비교 항목 | API Gateway | BFF (Backend for Frontend) | Service Mesh |
|---|---|---|---|
| **통신 트래픽 방향** | **North-South (외부 $\rightarrow$ 내부 인그레스)** | North-South (특정 UI $\rightarrow$ 내부 연계) | **East-West (내부 서비스 $\leftrightarrow$ 내부 서비스)** |
| **배치 위치** | 클라이언트와 백엔드 사이의 진입 경계 | 클라이언트별 백엔드 계층 | 서비스 통신 경계; 사이드카 또는 다른 데이터 플레인 구성 |
| **주요 초점** | 전사 보안, 글로벌 라우팅, Rate Limit | **클라이언트(모바일/웹)별 화면 데이터 취합** | 서비스 간 상호 mTLS 보안, 카나리 배포, 추적 |
| **비즈니스 로직** | **절대 배제 (Stateless dumb pipe)** | 일부 허용 (DTO 변환, 비동기 응답 조인) | 절대 배제 (인프라 네트워크 계층) |
| **담당 주체** | 플랫폼 인프라 / DevOps 팀 | 각 프론트엔드 전담 개발팀 | 인프라 / SRE 팀 |
---

## Ⅳ. API Gateway 운용 시 발생 위험 및 대응 전략

| 위험 | 대책 | 효과 |
|---|---|---|
| **단일 장애점(SPOF) 발생으로 게이트웨이 다운 시 전사 서비스 마비** | L4 로드밸런서 하단 무상태(Stateless) 게이트웨이 오토스케일링 및 Netty 비동기 논블로킹 엔진 적용 | 시스템 가용성 확보 및 트래픽 급증 탄력 처리 |
| **특정 마이크로서비스 지연이 게이트웨이 스레드 고갈 및 연쇄 마비 유발** | 서비스별 벌크헤드(Bulkhead) 격리 및 타임아웃 기반 서킷 브레이커 설정 | 연쇄 장애 차단 및 타 서비스 정상 응답 보장 |
| **게이트웨이에 비즈니스 로직이 누적되어 과거 '무거운 ESB'로 퇴보** | 게이트웨이는 순수 인프라 라우팅만 담당하고 화면 데이터 조합은 BFF 계층으로 분리 | 게이트웨이 무중단 유지 및 프론트엔드 배포 독립성 확보 |
| **대규모 분산 환경에서 요청 경로 유실로 인한 장애 추적 불가** | W3C 표준 TraceId/SpanId 헤더를 인그레스 단계에서 자동 채번하여 전파 | 전사 분산 트랜잭션 추적성 확보 |
---

## Ⅴ. 적용 제언

| 한계 | 해결 방안 |
|---|---|
| 공통 진입점에 업무 로직과 서비스별 정책이 집중될 가능성 | 인증·라우팅 등 공통 경계 기능에 책임을 한정하고 업무 규칙은 해당 서비스에 유지 |

## 출제 이력과 검증 출처

- 확인한 제132~140회 공식 문제지에서 해당 문항 미확인
- [Microsoft Learn, API gateways for microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway)

## 연결 토픽

- [마이크로서비스 아키텍처(MSA)](./035_msa.md) : API Gateway를 단일 진입점으로 사용하는 분산 아키텍처
- [스크래핑(Scraping)](./071_scraping.md) : 비공식 화면 스크래핑을 대체하는 API 게이트웨이 기반 표준 연계
- [이벤트 주도 아키텍처(EDA)](./078_event_driven_architecture.md) : 게이트웨이 배후에서 비동기 메시지를 처리하는 백엔드 아키텍처
