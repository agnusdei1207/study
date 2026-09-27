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


## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 소프트웨어 아키텍처·설계 → API Gateway

> **로드맵 경로** : 소프트웨어공학 > 분산 시스템 및 아키텍처 > 마이크로서비스(MSA) > API Gateway

---

## 30초 인출

- 본질: **API Gateway** 는 클라이언트와 백엔드 마이크로서비스 사이의 단일 진입점(Single Point of Entry)을 담당하는 역방향 프록시
- 메커니즘: 사전 필터(JWT·SSL 종료·유량 제어) → 라우팅 필터(서비스 디스커버리·LB·서킷 브레이커) → 사후 필터(TraceId 로깅)의 3단계 파이프라인
- 통찰: 한계: 게이트웨이에 화면별 조합과 내부 서비스 정책까지 몰면 단일 경계가 병목이 됨 → 방안: 외부 공통 통제·BFF·서비스 메시의 책임을 구분

<details>
<summary>핵심 용어</summary>

- **API 게이트웨이(API Gateway)** : 모든 클라이언트 요청의 단일 진입점 역할을 수행하며 라우팅, 인증, 유량 제어를 총괄하는 리버스 프록시
- **BFF(Backend for Frontend)** : 모바일, 웹 등 특정 클라이언트의 UI/UX 화면 요구에 맞춰 API 응답 데이터를 최적 조합(Aggregation)하는 계층
- **유량 제어(Rate Limiting)** : Token Bucket 또는 Leaky Bucket 알고리즘을 활용하여 클라이언트별 초당 요청 수(TPS)를 제한하는 메커니즘
- **North-South 트래픽(North-South Traffic)** : 외부 클라이언트로부터 데이터센터 또는 VPC 내부 서비스로 유입되는 인그레스(Ingress) 트래픽
- **서비스 메시(Service Mesh)** : 마이크로서비스 간의 내부 통신(East-West)을 사이드카(Sidecar) 프록시로 중계하여 mTLS와 추적성을 제공하는 인프라

</details>

---

## 2~4교시 예상문제 (25점)

> 마이크로서비스 환경에서 API Gateway의 역할과 주요 처리 흐름을 설명하고, BFF·서비스 메시와의 역할 구분 및 안정적인 운영 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. API Gateway의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | API Gateway는 클라이언트 요청을 백엔드 서비스로 중계하며 공통 API 처리를 제공하는 진입 계층 |
| 목적 | 서비스 주소와 공통 통신 정책을 클라이언트에서 분리 |

## Ⅱ. API Gateway의 특징과 공통 기능

클라이언트와 서비스 사이의 외부 진입 경계에서 공통 통신 정책을 적용하며, 서비스별 업무 규칙은 백엔드에 유지.

| 기능 영역 | 세부 역할 및 핵심 기술 | 실무 구현 사례 |
|---|---|---|
| **동적 라우팅 및 로드밸런싱** | 요청 경로/헤더에 따라 백엔드 인스턴스로 분기, 서비스 디스커버리(Eureka/K8s) 연계 | Spring Cloud Gateway, Kong, Envoy |
| **인증 및 인가 (Security)** | 클라이언트의 JWT 검증, API Key 유효성 체크, OAuth 2.0 토큰 인트로서펙션 | Keycloak 연동, OAuth 2.0 Resource Server |
| **유량 제어 (Rate Limiting)** | 클라이언트/IP/API별 초당 호출 수(TPS) 제한, 서비스 과부하 차단 | Token Bucket 알고리즘, Redis 분산 카운터 |
| **복원력 (Resilience)** | 백엔드 장애 시 빠른 실패(Fast Fail) 및 대체 응답(Fallback) 반환 | Resilience4j Circuit Breaker 연계 |
| **통합 관측성 (Observability)** | 전사 트랜잭션 추적을 위한 TraceId 발급 및 메트릭 수집 | OpenTelemetry, Prometheus, W3C TraceContext |

## Ⅲ. 요청 처리와 백엔드 라우팅 체계

```text
클라이언트 요청 → Gateway의 인증·유량 제어
                               ↓ 허용 요청
                       경로·헤더별 서비스 선택
                         ├ 주문 서비스
                         ├ 결제 서비스
                         └ 회원 서비스
응답·오류·추적 정보 ← Gateway ← 백엔드 처리 결과
```

## Ⅳ. API Gateway·BFF·서비스 메시 비교

| 비교 항목 | API Gateway | BFF (Backend for Frontend) | Service Mesh |
|---|---|---|---|
| **통신 트래픽 방향** | **North-South (외부 $\rightarrow$ 내부 인그레스)** | North-South (특정 UI $\rightarrow$ 내부 연계) | **East-West (내부 서비스 $\leftrightarrow$ 내부 서비스)** |
| **배치 위치** | 클라이언트와 백엔드 사이의 진입 경계 | 클라이언트별 백엔드 계층 | 서비스 통신 경계; 사이드카 또는 다른 데이터 플레인 구성 |
| **주요 초점** | 전사 보안, 글로벌 라우팅, Rate Limit | **클라이언트(모바일/웹)별 화면 데이터 취합** | 서비스 간 상호 mTLS 보안, 카나리 배포, 추적 |
| **비즈니스 로직** | 공통 경계 기능 중심으로 제한 | 클라이언트별 응답 조합·변환 | 통신 정책 중심으로 제한 |
| **담당 주체** | 플랫폼·API 운영 조직 등 | 제품·클라이언트 담당 조직 등 | 플랫폼·인프라 운영 조직 등 |
---

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 게이트웨이 장애에 따른 요청 경로 중단 | 다중 인스턴스·헬스체크·부하 시험 |
| 특정 백엔드 지연의 게이트웨이 자원 점유 | 서비스별 타임아웃·동시 요청 한도·서킷 브레이커 검토 |
| 화면별 조합·업무 규칙의 게이트웨이 집중 | 화면 조합은 BFF, 업무 규칙은 해당 서비스로 분리 |
| 분산 호출 경로의 추적 정보 유실 | 요청 추적 식별자를 진입 경계에서 생성·전파 |

## Ⅵ. 제언

외부 API에서 공통 인증·유량 제어·라우팅 책임을 먼저 정하고 화면 조합과 업무 규칙의 소유 계층 분리.

## 출제 이력과 검증 출처

- 확인한 제132~140회 공식 문제지에서 해당 문항 미확인
- [Microsoft Learn, API gateways for microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway)

## 연결 토픽

- [마이크로서비스 아키텍처(MSA)](./035_msa.md) : API Gateway를 단일 진입점으로 사용하는 분산 아키텍처
- [스크래핑(Scraping)](./071_scraping.md) : 비공식 화면 스크래핑을 대체하는 API 게이트웨이 기반 표준 연계
- [이벤트 주도 아키텍처(EDA)](./078_event_driven_architecture.md) : 게이트웨이 배후에서 비동기 메시지를 처리하는 백엔드 아키텍처
