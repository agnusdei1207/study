---
title: "API Gateway"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "Gemini 3.8 Flash"

---

## 딸려 나오는 하위 토픽
| 서브토픽 | 핵심 키워드 | 답안 차별화 포인트 |
|---|---|---|
| BFF (Backend for Frontend) | 클라이언트 맞춤형 API, 응답 데이터 조합(Aggregation), 프론트엔드 자율 배포 | 게이트웨이의 비즈니스 로직 오염(ESB 회귀)을 방지하는 아키텍처 패턴 제시 |
| 유량 제어 (Rate Limiting) | Token Bucket, Leaky Bucket, Redis 분산 카운터, DDoS 방어 | 트래픽 폭증 시 백엔드 보호 및 API 과금/SLA 보장을 위한 알고리즘 메커니즘 명시 |
| API Gateway vs Service Mesh | North-South(외부-내부) vs East-West(내부-내부), mTLS, Envoy, Istio | 마이크로서비스 환경에서 인그레스 게이트웨이와 메시 간의 명확한 경계 및 연계 구조화 |

---

## 1. API Gateway의 개요 및 필요성

### (1) API Gateway의 정의
- 클라이언트(웹, 모바일, 서드파티)와 백엔드 마이크로서비스 사이에 위치하여, **모든 외부 API 요청의 단일 진입점(Single Point of Entry) 역할을 수행하며 라우팅, 인증/인가, 유량 제어, 로깅, 프로토콜 변환을 일괄 대행하는 역방향 프록시(Reverse Proxy) 기반 인프라 컴포넌트**.

### (2) 핵심 필요성 (123회 기출)
- **클라이언트와 내부 서비스 간 결합도 해소**: 클라이언트가 수십 개 마이크로서비스의 내부 IP, 포트, 분할 구조를 알 필요 없이 단일 도메인으로 호출 가능.
- **공통 관심사(횡단 관심사) 중앙 집중화**: 각 마이크로서비스마다 중복 구현되던 JWT 인증, SSL 종료(Termination), CORS 처리, Rate Limiting을 게이트웨이에서 일괄 통제.
- **백엔드 보안 및 프로토콜 캡슐화**: 외부 인터넷에 내부 사설망(Private VPC) 서비스를 직접 노출하지 않고, 레거시 SOAP이나 gRPC를 RESTful JSON으로 변환 제공.

---

## 2. API Gateway의 핵심 아키텍처 및 주요 기능

### (1) API Gateway 동작 구조도
```text
+-------------------------------------------------------------------------+
|                  API Gateway의 단일 진입점 및 필터 파이프라인           |
+-------------------------------------------------------------------------+
| [ 외부 클라이언트 ] (모바일 앱, 웹 브라우저, 파트너사 API)              |
|        │                                                                |
|        v (HTTPS / REST 요청 : North-South 트래픽)                       |
| +─────────────────────────────────────────────────────────────────────+ |
| │                       API Gateway (역방향 프록시)                   │ |
| │  [사전 필터 (Pre)]     ──▶ [라우팅 필터 (Routing)] ──▶ [사후 필터 (Post)] │ |
| │  - JWT 토큰 인증/인가      - 서비스 디스커버리 연동     - 응답 헤더 가공  │ |
| │  - Rate Limiting (유량)    - 부하 분산 (Round-Robin)   - 통합 감사 로그  │ |
| │  - WAF / 악성 IP 차단      - 서킷 브레이커 (Bulkhead)   - 분산 Trace 기록 │ |
| +─────────────────────────────────────────────────────────────────────+ |
|        │                        │                        │              |
|        v (내부 mTLS)            v (내부 gRPC)            v (내부 HTTP)  |
|   [ 주문 서비스 ]          [ 회원 서비스 ]          [ 결제 서비스 ]    |
+-------------------------------------------------------------------------+
```

### (2) API Gateway의 5대 주요 기능
| 기능 영역 | 세부 역할 및 핵심 기술 | 실무 구현 사례 |
|---|---|---|
| **동적 라우팅 및 로드밸런싱** | 요청 URL 경로/헤더에 따라 백엔드 인스턴스로 분기, 서비스 디스커버리 연계 | Spring Cloud Gateway, Kong, Envoy, Netflix Zuul |
| **인증 및 인가 (Security)** | 클라이언트의 JWT 검증, API Key 유효성 체크, OAuth 2.0 토큰 인트로서펙션 | Keycloak 연동, OAuth 2.0 Resource Server |
| **유량 제어 (Rate Limiting)** | 클라이언트/IP/API별 초당 호출 수(TPS) 제한, 서비스 과부하 차단 | Token Bucket 알고리즘, Redis 분산 레이트 리미터 |
| **복원력 (Resilience)** | 백엔드 장애 시 빠른 실패(Fast Fail) 및 대체 응답(Fallback) 반환 | Resilience4j Circuit Breaker 연계 |
| **통합 관측성 (Observability)** | 전사 트랜잭션 추적을 위한 Correlation ID(TraceId) 발급 및 메트릭 수집 | W3C TraceContext, OpenTelemetry, Prometheus |

---

## 3. API Gateway vs BFF vs Service Mesh 비교

| 비교 항목 | API Gateway | BFF (Backend for Frontend) | Service Mesh |
|---|---|---|---|
| **통신 트래픽 방향**| **North-South (외부 $\rightarrow$ 내부)** | North-South (특정 클라이언트 $\rightarrow$ 내부) | **East-West (내부 서비스 $\leftrightarrow$ 내부 서비스)** |
| **배치 위치** | 시스템 최외곽 DMZ 망 | API Gateway와 마이크로서비스 사이 | 각 마이크로서비스 파드(Pod) 내 사이드카 |
| **주요 초점** | 보안, 전사 라우팅, Rate Limit | **클라이언트별 맞춤형 화면 데이터 취합** | 서비스 간 상호 mTLS 보안, 카나리 배포, 추적 |
| **비즈니스 로직** | **절대 배제 (Stateless dumb pipe)** | 일부 허용 (DTO 변환, 비동기 조인) | 절대 배제 (인프라 네트워크 레벨) |

---

## 4. 실무 실패 시나리오 및 해결 방안

| 실패 시나리오 | 근본 원인 | 공학적 해결 방안 | 정량적 기대효과 |
|---|---|---|---|
| **단일 장애점(SPOF)으로 전사 서비스 셧다운**<br>(게이트웨이 1대 다운 시 모든 앱 마비) | 게이트웨이 인스턴스의 다중화 부재 및 블로킹 I/O(Tomcat) 스레드 고갈 | L4 로드밸런서 하단 무상태(Stateless) 게이트웨이 다중화 및 Netty 비동기 엔진 적용 | 가용성 99.999% 달성, 초당 5만 TPS 탄력 처리 |
| **특정 서비스 장애가 전사 게이트웨이 마비 유발**<br>(계단식 장애 Cascading Failure) | 결제 서비스 지연 시 게이트웨이 커넥션이 회수되지 않고 점유 유지 | 서비스별 벌크헤드(Bulkhead) 격리 및 3초 타임아웃 서킷 브레이커 설정 | 특정 서비스 장애 시에도 타 서비스 정상 응답 100% 보장 |
| **게이트웨이 비대화로 인한 'ESB 회귀' 현상**<br>(게이트웨이에 비즈니스 로직 코딩) | 화면 요구사항 변경 시마다 게이트웨이 코드를 수정하여 배포 병목 발생 | 게이트웨이는 인프라 라우팅만 담당하고, 응답 데이터 조합은 BFF로 완전 분리 | 게이트웨이 무중단 유지 및 프론트엔드 변경 배포 속도 4배 향상 |

---

## 5. 기술사 답안 차별화 포인트 (기술사의 시각)

```text
[과거: 만능 엔터프라이즈 버스 (ESB의 악몽)]     [현대: 스마트 엔드포인트 & 멍청한 파이프]
- 게이트웨이 내부에 복잡한 변환 로직 누적 ──▶   - API Gateway는 Stateless 라우팅/보안에 집중
- 모놀리스 게이트웨이가 배포 병목 유발     ──▶   - 클라이언트별 BFF 분리로 화면 요구 분산 수용
- 외부/내부 트래픽을 단일 장비로 처리     ──▶   - API Gateway(North-South) + Service Mesh(East-West)
```

- **ESB(Enterprise Service Bus) 회귀 안티패턴의 철저한 경계**: 마이크로서비스의 핵심 철학은 "멍청한 파이프와 똑똑한 엔드포인트(Dumb Pipes and Smart Endpoints)"임. API Gateway 내부에 DB를 연결하거나 비즈니스 판단 로직을 집어넣는 순간 시스템은 과거 실패했던 무거운 ESB로 전락함.
- **하이브리드 트래픽 거버넌스 제시**: 최외곽의 보안, 인증, 전사 유량 제어는 **API Gateway(Spring Cloud Gateway, Kong)**가 담당하고, 내부 마이크로서비스 간의 세밀한 mTLS 암호화, 동적 라우팅, 결함 주입은 **서비스 메시(Istio/Envoy)**가 전담하도록 North-South와 East-West를 명확히 분리하는 2계층 트래픽 아키텍처를 제시하는 것이 기술사의 통찰임.
