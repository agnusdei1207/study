---
title: "API Gateway"
description: "마이크로서비스 아키텍처(MSA) 환경에서 클라이언트 단일 진입점 역할을 수행하는 API Gateway의 아키텍처, 핵심 기능, BFF 및 서비스 메시와의 비교, 운영 안정화 전략"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
    variant: "note"
extra:
  series: "itpe"
  topic: "02-software-engineering"
  sub_topic: "msa"
  order: 75
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어공학 → 분산 시스템 및 아키텍처 → 마이크로서비스(MSA) → **API Gateway**

---

## 30초 인출

- 본질: **API Gateway** 는 클라이언트와 백엔드 마이크로서비스 간의 단일 접점(Single Point of Contact)을 형성하여 동적 라우팅, 인증/인가, 유량 제어, 로드밸런싱 등 공통 인프라 기능을 전담하는 리버스 프록시(Reverse Proxy) 기반 진입 계층
- 메커니즘: 사전 필터(인증·Rate Limiting·SSL 종단) → 라우팅 필터(서비스 디스커버리 연계·부하분산·서킷 브레이커) → 사후 필터(응답 변환·로깅·TraceId 헤더 주입)의 3단계 파이프라인 처리
- 통찰: 게이트웨이에 과도한 비즈니스 로직과 화면 데이터 조합을 집중시킬 경우 단일 장애점(SPOF) 및 성능 병목으로 변질되므로 경계 공통 통제는 API 게이트웨이가 맡고 화면별 조합은 BFF(Backend for Frontend), 내부 통신은 서비스 메시(Service Mesh)로 책임을 분리하는 아키텍처가 필수적임

<details>
<summary>핵심 용어</summary>

- **리버스 프록시(Reverse Proxy)** : 내부 서버들의 앞단에 위치하여 외부 클라이언트의 요청을 받아 적절한 백엔드 서버로 중계하는 중계 서버
- **BFF(Backend for Frontend)** : 모바일, 웹 등 특정 클라이언트의 UI/UX 화면 요구사항에 맞춤형 데이터 취합(Aggregation) 및 변환을 제공하는 전담 백엔드
- **서비스 메시(Service Mesh)** : 서비스 간 내부(East-West) 통신을 전담하는 사이드카 프록시 네트워크 인프라
- **유량 제어(Rate Limiting)** : 토큰 버킷(Token Bucket) 또는 누출 버킷(Leaky Bucket) 알고리즘을 통해 클라이언트별 초당 허용 요청량(TPS)을 제한하는 기법
- **서킷 브레이커(Circuit Breaker)** : 특정 마이크로서비스의 장애 지속 시 호출을 즉시 차단(Open)하여 연쇄 장애(Cascading Failure)를 차단하는 복원 메커니즘

</details>

---

## 2~4교시 예상문제 (25점)

> 마이크로서비스 아키텍처(MSA)에서 API Gateway의 도입 배경과 핵심 기능을 설명하고, API Gateway, BFF(Backend for Frontend), Service Mesh의 아키텍처 계층별 역할 분담 체계 및 단일 장애점(SPOF) 극복을 위한 고가용성 설계 전략을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 다수의 백엔드 마이크로서비스 앞단에 위치하여 모든 클라이언트의 요청을 일괄 수신하고 공통 횡단 관심사(보안, 라우팅, 유량 제어)를 통합 처리하는 단일 진입점 계층 |
| 목적 | 내부 서비스 IP 은닉을 통한 보안 강화, 클라이언트와 서비스 간 결합도 완화, 공통 비기능 요구사항 중앙 집중 관리 |

## Ⅱ. 핵심 특징

API Gateway는 외부 트래픽(North-South)의 진입 관문으로서 시스템의 복원력과 보안성을 극대화.

| 핵심 영역 | 세부 기능 및 역할 | 구현 기술 |
|---|---|---|
| **동적 라우팅 및 부하분산** | URI 경로, 헤더, HTTP 메서드 기반 서비스 라우팅 및 다중 인스턴스 분산 | Spring Cloud Gateway, Kong, Envoy |
| **인증 및 인가 (Security)** | JWT 유효성 검증, API Key 검사, OAuth 2.0 연계, SSL/TLS Termination | Keycloak, Spring Security, OpenID Connect |
| **트래픽 제어 (Rate Limiting)** | 사용자/IP/API 엔드포인트별 호출 빈도 통제 및 DoS 공격 방어 | Redis Token Bucket, Leaky Bucket |
| **장애 격리 (Resilience)** | 백엔드 서비스 지연/장애 감지 시 빠른 실패(Fail-Fast) 및 Fallback 응답 | Resilience4j, Netflix Hystrix |
| **통합 관측성 (Observability)** | 분산 추적 식별자(TraceId, SpanId) 생성/전파 및 글로벌 메트릭 계측 | OpenTelemetry, W3C TraceContext, Prometheus |

## Ⅲ. 체계·프로세스

API Gateway의 요청 파이프라인 처리 흐름 및 마이크로서비스 라우팅 아키텍처.

```text
+---------------------------------------------------------------------------------------------------------+
|                                    API Gateway 요청 처리 및 라우팅 체계                                  |
+---------------------------------------------------------------------------------------------------------+
                                                                                                           
  [웹 브라우저]   [모바일 앱]   [외부 파트너]                                                              
        │             │             │                                                                      
        └─────────────┼─────────────┘                                                                      
                      │ HTTPS 요청 (North-South Traffic)                                                   
                      ▼                                                                                    
  +───────────────────────────────────────────────────────────────────────────+                            
  |                         API Gateway (Reverse Proxy)                       |                            
  |                                                                           |                            
  |   [Pre-Filter]       - TLS Termination & WAF 필터링                       |                            
  |                      - 인증/인가 검증 (JWT Parsing / OAuth Token)          |                            
  |                      - 유량 제어 (Rate Limiting via Redis)                |                            
  |                             │                                             |                            
  |                             ▼                                             |                            
  |   [Routing Filter]   - Service Discovery 조회 (Consul / K8s DNS)          |                            
  |                      - 로드밸런싱 (Round Robin / Least Conn)              |                            
  |                      - 서킷 브레이커 감시 (Circuit Breaker Check)         |                            
  |                             │                                             |                            
  +─────────────────────────────┼─────────────────────────────────────────────+                            
                                │                                                                          
            ┌───────────────────┼───────────────────┐                                                      
            │ 내부 mTLS 통신    │                   │                                                      
            ▼                   ▼                   ▼                                                      
    +───────────────+   +───────────────+   +───────────────+                                              
    |   주문 서비스  |   |   결제 서비스  |   |   회원 서비스  |                                              
    +───────────────+   +───────────────+   +───────────────+                                              
            │                   │                   │                                                      
            └───────────────────┼───────────────────┘                                                      
                                │ 처리 결과 응답                                                           
                                ▼                                                                          
  +───────────────────────────────────────────────────────────────────────────+                            
  |   [Post-Filter]      - 응답 헤더 가공 및 CORS 헤더 부착                   |                            
  |                      - 응답 시간 측정 및 전사 TraceId 로깅                |                            
  +───────────────────────────────────────────────────────────────────────────+                            
                                │                                                                          
                                ▼                                                                          
                          클라이언트 응답                                                                  
```

- **API Gateway 처리 파이프라인 4단계 프로세스**:
  1. **인입 및 보안 검증(Pre-Filter)** : SSL 종료 후 클라이언트 요청 헤더의 JWT 무결성을 검증하고, Redis 카운터 기반으로 요청 쿼터를 확인하여 초과 시 429 Too Many Requests 반환.
  2. **목적지 탐색 및 라우팅(Routing Filter)** : 서비스 레지스트리(Service Registry)를 통해 타깃 마이크로서비스 인스턴스 IP 목록을 조회하고 최적의 인스턴스로 전달.
  3. **장애 차단(Resilience)** : 타깃 인스턴스 호출 실패율이 임계치를 초과할 경우 서킷을 오픈하여 즉각 Fallback 응답을 반환하고 백엔드 보호.
  4. **응답 가공 및 감사(Post-Filter)** : 공통 보안 헤더 주입, CORS 설정 처리, 분산 추적 로그(TraceId) 기록 후 클라이언트로 최종 응답 전송.

## Ⅳ. 종류·비교

#### API Gateway vs BFF vs Service Mesh 아키텍처 비교

| 비교 항목 | API Gateway | BFF (Backend for Frontend) | Service Mesh |
|---|---|---|---|
| **트래픽 방향** | North-South (외부 $\rightarrow$ 내부 인그레스) | North-South (특정 채널 $\rightarrow$ 내부) | East-West (내부 서비스 $\leftrightarrow$ 내부 서비스) |
| **배치 위치** | 전체 시스템의 최전방 경계 계층 | 클라이언트 유형별 중간 계층 | 각 마이크로서비스 파드(Pod) 내부 사이드카 |
| **핵심 역할** | 전사 공통 보안, 글로벌 라우팅, Rate Limit | 채널별 화면 데이터 취합(Aggregation), 변환 | 마이크로서비스 간 mTLS 암호화, 카나리 라우팅 |
| **비즈니스 로직** | 절대 배제 (인프라/경계 정책 전담) | 화면 맞춤형 표현 로직 포함 가능 | 절대 배제 (네트워크 L4/L7 프록시 전담) |
| **관리 주체** | 전사 플랫폼/인프라 운영 조직 | 채널별 프론트엔드/백엔드 개발팀 | 플랫폼/클라우드 엔지니어링 조직 |

#### 주요 API Gateway 오픈소스 설루션 비교

| 솔루션 | 기반 기술 | 특징 | 적합한 환경 |
|---|---|---|---|
| **Spring Cloud Gateway** | Java, Spring WebFlux (Netty) | 스프링 생태계 완벽 통합, 논블로킹 비동기 리액티브 구조 | Java/Spring 기반의 MSA 엔터프라이즈 환경 |
| **Kong Gateway** | Nginx, OpenResty, Lua | 초고성능 C/Nginx 기반, 풍부한 플러그인 생태계 지원 | 대규모 글로벌 트래픽 및 이기종 멀티 언어 환경 |
| **Envoy Proxy** | C++ | 클라우드 네이티브 표준, 고성능 저지연 메모리 점유, gRPC 완벽 지원 | Kubernetes Ingress 및 Service Mesh 통합 환경 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| API Gateway 장애 발생 시 시스템 전체 통신이 마비되는 단일 장애점(SPOF) 위험 | L4/L7 로드밸런서(ALB) 뒷단에 다중 Gateway 인스턴스를 무상태(Stateless) 클러스터로 구성하고 Auto-scaling 연계 |
| 게이트웨이 계층에 화면 조합(Aggregation) 및 비즈니스 로직이 침투하여 팻 게이트웨이(Fat Gateway)로 변질 | UI 맞춤형 데이터 가공은 BFF 계층으로 완전히 이관하고, 게이트웨이는 순수 인프라 라우팅 및 공통 보안만 수행 |
| 모든 요청이 게이트웨이를 경유함에 따라 직렬화/역직렬화 및 필터 체인 오버헤드로 인한 레이턴시 증가 | 논블로킹 I/O(Netty/Envoy) 적용, 정적 자원 CDN 분산, 고부하 내부 통신은 gRPC 및 사이드카 직접 통신 전환 |

## Ⅵ. 제언

API Gateway 구축 시 인프라 라우팅 책임을 게이트웨이에 국한하고, 화면 종속적 로직은 BFF로, 내부 서비스 간 보안/통신은 서비스 메시로 위임하는 3계층 관심사 분리 아키텍처 확립이 필요.

```text
[클라이언트 계층] ──> [API Gateway (North-South)] ──> [BFF 계층] ──> [Service Mesh (East-West)]
 (Web / Mobile)           (공통 보안 & 전사 라우팅)      (화면 조합)       (mTLS & 내부 추적성)
```

| 아키텍처 계층 | 권장 구축 기술 | 핵심 설계 원칙 |
|---|---|---|
| **인그레스 경계** | Envoy Gateway / Spring Cloud Gateway | 완전 무상태화, Rate Limit 기반 시스템 보호, SSL 종단 |
| **채널 연계** | Node.js BFF / GraphQL Gateway | 채널 맞춤형 Over-fetching 방지, API 오케스트레이션 |
| **내부 통신** | Istio / Linkerd (Sidecar Proxy) | 제로 트러스트(Zero Trust) 상호 mTLS, 서비스 간 지연 최소화 |

---

## 출제 이력

- 제131회 정보관리기술사 2교시: 마이크로서비스 아키텍처에서 API Gateway의 기능과 BFF(Backend for Frontend) 패턴 비교
- 제128회 컴퓨터시스템응용기술사 1교시: API 게이트웨이(API Gateway)의 개념 및 주요 기능
- 제122회 정보관리기술사 3교시: MSA 환경에서의 인증/인가 아키텍처와 API Gateway의 역할

## 참고 자료

- Chris Richardson, "Microservices Patterns: With examples in Java"
- Martin Fowler, "Microservice Architecture"
- Microsoft Azure Architecture Center: API Gateway pattern

## 연결 토픽

- [마이크로서비스 아키텍처(MSA)](./035_msa.md)
- [스크래핑(Scraping)](./071_scraping.md)
- [이벤트 주도 아키텍처(EDA)](./078_event_driven_architecture.md)
- [서비스 메시(Service Mesh)](./088_service_mesh.md)
