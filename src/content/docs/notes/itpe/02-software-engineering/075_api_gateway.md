---
title: "API Gateway"
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

## Ⅰ. API Gateway의 개요

- **개념** : 마이크로서비스 아키텍처(MSA) 및 분산 클라우드 환경에서 모든 외부 클라이언트(Web, Mobile, 3rd Party)의 요청을 단일 진입점(Single Point of Entry)으로 수용하여, 적절한 내부 백엔드 마이크로서비스로 라우팅하고 공통 횡단 관심사를 일괄 처리하는 리버스 프록시(Reverse Proxy) 기반 미들웨어.
- **배경 및 필요성** : 수십~수백 개의 마이크로서비스 엔드포인트를 클라이언트가 직접 호출할 때 발생하는 네트워크 오버헤드, 복잡한 인증/보안 처리, 프로토콜 불일치 및 엔드포인트 노출 리스크를 원천 해결.
- **대표 솔루션** : Spring Cloud Gateway, Kong, Apigee, AWS API Gateway, Envoy.

## Ⅱ. API Gateway의 아키텍처 및 핵심 기능 계층

```text
   [ 클라이언트 (Web / Mobile App) ]
                   │
                   ▼
   ┌────────────────────────────────────────────────────────┐
   │                  [ API Gateway ]                       │
   │  - 인증 및 인가 (JWT 검증, OAuth 2.0 Token 교환)       │
   │  - 트래픽 제어 (Rate Limiting, Throttling)             │
   │  - 장애 격리 (Circuit Breaker: Resilience4j)           │
   │  - 라우팅 및 로드밸런싱 (동적 서비스 디스커버리 연동)  │
   │  - 프로토콜 변환 (REST <-> gRPC) 및 응답 캐싱          │
   └──────────┬───────────────────────────────┬─────────────┘
              │ (내부 사설 네트워크 라우팅)    │
              ▼                               ▼
   ┌──────────────────────┐        ┌──────────────────────┐
   │ [ Order Service ]    │        │ [ Payment Service ]  │
   └──────────────────────┘        └──────────────────────┘
```

- **동적 라우팅 및 로드밸런싱** : Eureka, Consul, K8s DNS와 연동하여 백엔드 파드의 인스턴스 IP를 동적으로 감지하고 트래픽 분산.
- **BFF (Backend For Frontend) 패턴 구현** : 웹 전용, 모바일 전용 등 클라이언트 특성에 맞추어 최적화된 API 게이트웨이를 다변화하여 필요한 데이터만 조합(Aggregation) 제공.

## Ⅲ. 주요 오픈소스 API Gateway 솔루션 비교

| 비교 항목 | Spring Cloud Gateway | Kong Gateway | AWS API Gateway |
|---|---|---|---|
| 기반 기술 | Java / Netty (Non-blocking 리액티브) | Nginx / Lua (OpenResty) | AWS 완전 관리형 서버리스 |
| 처리 성능 | 우수 (리액티브 비동기 이벤트 루프) | 최고 (C/Nginx 기반 초저지연) | 클라우드 인프라가 자동 오토스케일링 |
| 확장성 | Java 코딩으로 커스텀 필터 구현 용이 | 다양한 플러그인 생태계 (Lua, Go) | Lambda 연동, 콘솔 기반 구성 |
| 적합 환경 | Spring 생태계 기반 엔터프라이즈 MSA | 대규모 고성능 트래픽, 폴리글랏 환경 | 클라우드 네이티브 서버리스 아키텍처 |

## Ⅳ. 고가용성 API 게이트웨이 구축을 위한 기술사적 제언

- **단일 장애점(SPOF) 방지를 위한 L4/L7 이중화** : API Gateway가 다운되면 전체 비즈니스가 마비되므로, Gateway 인스턴스 전면에 AWS ALB나 로드밸런서를 배치하고 멀티 AZ에 걸쳐 오토스케일링 그룹으로 구성 필수.
- **분산 서킷 브레이커(Circuit Breaker)를 통한 연쇄 장애(Cascading Failure) 차단** : 특정 하위 서비스 장애 시 게이트웨이 스레드가 고갈되어 전체 서비스가 마비되는 것을 막기 위해, 호출 타임아웃을 1~2초 이내로 엄격히 설정하고 즉각적인 폴백(Fallback) 캐시 응답을 반환하는 격리 설계 수립.
