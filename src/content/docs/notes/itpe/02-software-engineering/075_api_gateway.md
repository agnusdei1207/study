---
title: "API Gateway"
author: "Antigravity"
date: "2026-09-22T07:24:00+09:00"
tags:
  - "소프트웨어공학"
  - "APIGateway"
  - "MSA"
  - "마이크로서비스"
  - "BFF"
  - "서비스메시"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "GLM-5.3-Flash"
  keyword_grade: "B"
---

> **로드맵 경로**: 소프트웨어공학 > 분산 시스템 및 아키텍처 > 마이크로서비스(MSA) > API Gateway

---

## 30초 인출

- 본질: **API Gateway**는 클라이언트와 백엔드 마이크로서비스 사이의 단일 진입점(Single Point of Entry)을 담당하는 역방향 프록시
- 메커니즘: 사전 필터(JWT·SSL 종료·유량 제어) → 라우팅 필터(서비스 디스커버리·LB·서킷 브레이커) → 사후 필터(TraceId 로깅)의 3단계 파이프라인
- 판정 기준: North-South 외부 경계는 게이트웨이, 화면 데이터 취합은 BFF, East-West 내부 통신은 Service Mesh로 분격하는 2계층 거버넌스

<details>
<summary>핵심 용어</summary>

- **API 게이트웨이(API Gateway)**: 모든 클라이언트 요청의 단일 진입점 역할을 수행하며 라우팅, 인증, 유량 제어를 총괄하는 리버스 프록시
- **BFF(Backend for Frontend)**: 모바일, 웹 등 특정 클라이언트의 UI/UX 화면 요구에 맞춰 API 응답 데이터를 최적 조합(Aggregation)하는 계층
- **유량 제어(Rate Limiting)**: Token Bucket 또는 Leaky Bucket 알고리즘을 활용하여 클라이언트별 초당 요청 수(TPS)를 제한하는 메커니즘
- **North-South 트래픽(North-South Traffic)**: 외부 클라이언트로부터 데이터센터 또는 VPC 내부 서비스로 유입되는 인그레스(Ingress) 트래픽
- **서비스 메시(Service Mesh)**: 마이크로서비스 간의 내부 통신(East-West)을 사이드카(Sidecar) 프록시로 중계하여 mTLS와 추적성을 제공하는 인프라

</details>

---

## 25점형 답안 프레임워크

### [예상 문제]
> "마이크로서비스 아키텍처(MSA) 환경에서 API Gateway의 개념과 필요성을 설명하고, 핵심 기능 및 API Gateway, BFF, Service Mesh 간의 역할 비교와 대용량 트래픽 처리를 위한 2계층 트래픽 거버넌스 구축 전략을 제시하시오."

---

### Ⅰ. 분산 마이크로서비스의 단일 관문, API Gateway의 개요

#### 1. API Gateway의 정의
- 클라이언트(웹, 모바일, 서드파티)와 백엔드 마이크로서비스 사이에 위치하여, **모든 외부 API 요청의 단일 진입점(Single Point of Entry) 역할을 수행하며 라우팅, 인증/인가, 유량 제어, 로깅, 프로토콜 변환을 일괄 대행하는 역방향 프록시(Reverse Proxy) 기반 인프라 컴포넌트**.

#### 2. 핵심 도입 필요성
- **클라이언트-서비스 간 결합도 해소**: 클라이언트가 수십 개 마이크로서비스의 내부 IP, 포트, 분할 구조를 알 필요 없이 단일 도메인으로 호출.
- **공통 횡단 관심사 중앙 집중화**: JWT 검증, SSL 종료(Termination), CORS, Rate Limiting을 게이트웨이에서 일괄 통제.
- **내부 보안 및 캡슐화**: 사설망(Private VPC) 내부 서비스를 외부에 직접 노출하지 않고 안전하게 보호.

---

### Ⅱ. API Gateway의 핵심 아키텍처 및 5대 주요 기능

#### 1. API Gateway 3단계 필터 파이프라인 구조도

```mermaid
flowchart LR
    C["클라이언트 · 단일 도메인"] --> GW
    subgraph GW["API Gateway 단일 진입점"]
        direction TB
        F1["사전 필터 JWT · SSL · 유량 제어"] --> F2["라우팅 필터 LB · 서킷 브레이커"] --> F3["사후 필터 TraceId 로깅"]
    end
    GW -->|"동적 라우팅"| MS
    subgraph MS["백엔드 마이크로서비스"]
        direction TB
        M1["주문 서비스"] ~~~ M2["결제 서비스"] ~~~ M3["회원 서비스"]
    end
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

### Ⅲ. API Gateway vs BFF vs Service Mesh 비교

| 비교 항목 | API Gateway | BFF (Backend for Frontend) | Service Mesh |
|---|---|---|---|
| **통신 트래픽 방향** | **North-South (외부 $\rightarrow$ 내부 인그레스)** | North-South (특정 UI $\rightarrow$ 내부 연계) | **East-West (내부 서비스 $\leftrightarrow$ 내부 서비스)** |
| **배치 위치** | 시스템 최외곽 DMZ 망 (클라우드 관문) | API Gateway와 마이크로서비스 사이 계층 | 각 마이크로서비스 파드(Pod) 내 사이드카 |
| **주요 초점** | 전사 보안, 글로벌 라우팅, Rate Limit | **클라이언트(모바일/웹)별 화면 데이터 취합** | 서비스 간 상호 mTLS 보안, 카나리 배포, 추적 |
| **비즈니스 로직** | **절대 배제 (Stateless dumb pipe)** | 일부 허용 (DTO 변환, 비동기 응답 조인) | 절대 배제 (인프라 네트워크 계층) |
| **담당 주체** | 플랫폼 인프라 / DevOps 팀 | 각 프론트엔드 전담 개발팀 | 인프라 / SRE 팀 |

---

### Ⅳ. API Gateway 운용 시 발생 위험 및 대응 전략

| 위험 | 대책 | 효과 |
|---|---|---|
| **단일 장애점(SPOF) 발생으로 게이트웨이 다운 시 전사 서비스 마비** | L4 로드밸런서 하단 무상태(Stateless) 게이트웨이 오토스케일링 및 Netty 비동기 논블로킹 엔진 적용 | 시스템 가용성 확보 및 트래픽 급증 탄력 처리 |
| **특정 마이크로서비스 지연이 게이트웨이 스레드 고갈 및 연쇄 마비 유발** | 서비스별 벌크헤드(Bulkhead) 격리 및 타임아웃 기반 서킷 브레이커 설정 | 연쇄 장애 차단 및 타 서비스 정상 응답 보장 |
| **게이트웨이에 비즈니스 로직이 누적되어 과거 '무거운 ESB'로 퇴보** | 게이트웨이는 순수 인프라 라우팅만 담당하고 화면 데이터 조합은 BFF 계층으로 분리 | 게이트웨이 무중단 유지 및 프론트엔드 배포 독립성 확보 |
| **대규모 분산 환경에서 요청 경로 유실로 인한 장애 추적 불가** | W3C 표준 TraceId/SpanId 헤더를 인그레스 단계에서 자동 채번하여 전파 | 전사 분산 트랜잭션 추적성 확보 |

---

### Ⅴ. 기술사적 제언: North-South와 East-West의 2계층 트래픽 거버넌스

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: API Gateway는 마이크로서비스의 '정문(Front Door)'이다. 게이트웨이가 없으면 클라이언트는 수십 개 서비스의 IP와 인증 방식을 모두 알아야 하며 강하게 결합되지만, 게이트웨이에 DB 연동이나 비즈니스 판단 로직을 넣는 순간 과거 SOA 시절의 거대하고 실패했던 '무거운 ESB'로 퇴보한다. 게이트웨이는 '멍청한 파이프(Dumb Pipe)'로서 무상태 라우팅과 보안에 집중하고, 화면별 데이터 조합은 BFF, 내부 서비스 간 통신은 Service Mesh로 분격하는 2계층 거버넌스가 핵심이다.
- `나라면`: 1단락 또는 2단락에서 사전·라우팅·사후 필터의 3단계 파이프라인을 도해하고, API Gateway(North-South) vs BFF(화면 취합) vs Service Mesh(East-West)의 3자 매트릭스를 제시한 후, 2계층 트래픽 거버넌스 아키텍처를 결론으로 제언하겠다.

### 실전 답안용 기술사적 제언
- **판정 기준**: 트래픽의 방향(외부 인그레스 North-South vs 내부 서비스 간 East-West), 화면별 데이터 집계 요구 여부, 서비스별 호출량 급증에 따른 임계치(TPS)를 기준으로 라우팅 및 거버넌스 경로를 자동 판정함.
- **대응 방안**: 시스템 최외곽에는 Spring Cloud Gateway/Kong 기반 무상태(Stateless) API Gateway를 배치하여 전사 인증(JWT) 및 Rate Limiting을 수행하고, 화면 종속 데이터 가공은 BFF(Backend for Frontend)에 위임하며, 내부 서비스 간 통신은 Istio/Envoy 서비스 메시로 격리함.
- **검증 체계**: W3C TraceContext 표준 헤더(TraceId, SpanId)를 인그레스 단계에서 필수 주입하여 전사 분산 추적성을 검증하고, Resilience4j 기반 서킷 브레이커로 하위 서비스 지연 전파를 차단함.
- **기대 효과**: 게이트웨이 SPOF 위험을 제거하여 가용성을 확보하고, 무거운 ESB 안티패턴으로의 퇴보를 방지하며 서비스 간 통신의 상호 mTLS 제로 트러스트 보안을 완성함.

---

## 1교시 10점형 답안 발췌 (핵심 서술형)

- **API Gateway**는 클라이언트와 백엔드 마이크로서비스 사이에 위치하여 단일 진입점(Single Point of Entry) 역할을 수행하는 역방향 프록시(Reverse Proxy)이다.
- 동적 라우팅, 인증/인가(JWT/OAuth 2.0), 유량 제어(Rate Limiting), 서킷 브레이커, 분산 로깅의 공통 횡단 관심사를 일괄 처리한다. 외부에서 내부로 들어오는 North-South 트래픽을 관장하며, 클라이언트 맞춤형 데이터 취합을 담당하는 **BFF** 및 내부 서비스 간 East-West 통신을 제어하는 **Service Mesh**와 상호보완적으로 연계된다.

---

## 출제 이력 및 기출 분석

- **정보관리기술사**: 110회, 117회, 123회, 133회 (API Gateway의 필요성과 주요 기능, MSA 패턴, Service Mesh와의 비교)
- **컴퓨터시스템응용기술사**: 115회, 125회 (리버스 프록시 아키텍처, Rate Limiting 알고리즘, 클라우드 인그레스 거버넌스)
- **출제 경향성**: 단순 기능 나열을 넘어 단일 장애점(SPOF) 극복을 위한 비동기 논블로킹 엔진(Netty) 채택, 과거 무거운 ESB로의 퇴보 방지(BFF 분리), 그리고 Service Mesh와의 North-South vs East-West 트래픽 역할 분담을 명확히 제시해야 고득점 달성.

---

## 실전 작성 팁 & 감점 방지

- **필터 파이프라인 도해**: Pre-filter(인증/유량제어), Routing-filter(로드밸런싱), Post-filter(로깅/헤더가공)의 3단계 처리 흐름을 도식으로 명시할 것.
- **ESB와의 차이점 강조**: ESB는 무거운 비즈니스 변환을 내장했으나, API Gateway는 경량 무상태(Stateless) 라우팅에 집중한다는 점을 대비할 것.
- **BFF 및 Service Mesh와의 3자 매트릭스**: 3단락에서 트래픽 방향, 위치, 목적, 비즈니스 로직 허용 여부를 표로 명확히 정리할 것.

---

## 연결 토픽

- [마이크로서비스 아키텍처(MSA)](./035_msa.md) : API Gateway를 단일 진입점으로 사용하는 분산 아키텍처
- [스크래핑(Scraping)](./071_scraping.md) : 비공식 화면 스크래핑을 대체하는 API 게이트웨이 기반 표준 연계
- [이벤트 주도 아키텍처(EDA)](./078_event_driven_architecture.md) : 게이트웨이 배후에서 비동기 메시지를 처리하는 백엔드 아키텍처

