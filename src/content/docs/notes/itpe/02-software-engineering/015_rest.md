---
title: "REST"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 구현·객체지향·API → **REST**

## 30초 인출

- 본질: REST(Representational State Transfer)는 웹의 기존 HTTP 인프라와 표준 프로토콜을 활용하여 자원 중심의 상태 전송을 정의하는 분산 하이퍼미디어 아키텍처 스타일
- 메커니즘: 자원(URI) 식별 + 행위(HTTP Method) 표현 + 표현(JSON/XML) 전송 + 무상태(Stateless) 상호작용
- 통찰: 분산 네트워크 환경에서 POST 재전송 시 중복 결제 및 데이터 중복 생성 오류가 발생하므로 멱등성 보장을 위한 멱등키(Idempotency Key) 메커니즘 필수 적용

<details>
<summary>핵심 용어</summary>

- **REST(Representational State Transfer)** : Roy Fielding이 제안한 웹 아키텍처 스타일로, 자원의 식별과 무상태 상태 전이를 핵심 원칙으로 규정한 아키텍처
- **Stateless(무상태성)** : 각 클라이언트 요청은 서버 세션 문맥에 의존하지 않고 요청 자체에 처리에 필요한 모든 정보를 담아야 하는 제약조건
- **Uniform Interface** : 자원 식별(URI), 표현 조작, 자기기술적 메시지, HATEOAS의 4대 인터페이스 제약조건
- **HATEOAS(Hypermedia As The Engine Of Application State)** : 응답 본문에 다음 가능한 상태 전이를 위한 링크를 동적으로 포함하는 성숙도 최상위 원칙
- **Idempotency(멱등성)** : 동일한 연산을 단 한 번 수행하거나 여러 번 연속 수행해도 서버의 최종 자원 상태가 동일하게 유지되는 성질
- **RMM(Richardson Maturity Model)** : Level 0(단일 URI)부터 Level 3(HATEOAS)까지 RESTful API의 성숙도를 4단계로 평가하는 모델

</details>

---

## 2~4교시 예상문제 (25점)

> REST(Representational State Transfer)의 개념과 6대 아키텍처 제약조건을 설명하고, HTTP 메서드의 멱등성과 Richardson 성숙도 모델(RMM) 및 실무 API 설계 원칙을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. REST의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **REST(Representational State Transfer)** 는 웹의 표준 HTTP 프로토콜을 기반으로 자원을 명시하고 상태를 교환하는 분산 소프트웨어 아키텍처 스타일 |
| 목적 | 시스템 구성요소의 독립적 진화, 이종 플랫폼 간 상호운용성 확보 및 웹 인프라(캐시·프록시)의 확장성 극대화 |

## Ⅱ. REST의 핵심 특징

| 특징 | 의미 |
|---|---|
| 자원 지향성 | 모든 관리 대상을 고유한 URI(Uniform Resource Identifier)로 명사형 식별 |
| 무상태 통신 | 서버가 클라이언트의 세션 상태를 유지하지 않아 수평적 서버 확장(Scale-out) 용이 |
| 자기서술적 메시지 | 메시지 헤더와 Content-Type만으로 본문의 해석 및 처리 방식을 온전히 파악 가능 |

## Ⅲ. REST 아키텍처 6대 기본 제약조건

### REST 아키텍처 분산 상호작용 체계

```text
[Client] ──(HTTP Request: 자원 식별 URI + Method)──→ [Layered System]
   ▲                                                       │
   │                                           (Gateway, WAF, Cache)
   │                                                       ▼
   └──────(HTTP Response: 자원 표현 + HATEOAS 링크)────── [Server]
```

### 무상태(Stateless) 요청 및 자원 처리 메커니즘

```text
클라이언트 요청 (토큰·파라미터 포함 무상태 요청)
    ↓
인증/인가 게이트웨이: 요청 헤더의 JWT 검증
    ↓
자원 서버: URI 및 HTTP 메서드 매핑
    ├─ GET /orders/123 → 주문 자원 표현 조회 (캐시 확인)
    ├─ POST /orders → 신규 주문 자원 생성 (201 Created + Location 헤더)
    └─ DELETE /orders/123 → 주문 자원 삭제 (204 No Content)
    ↓
표현 생성: JSON 응답 본문 및 다음 상태 전이 하이퍼링크(HATEOAS) 반환
```

| 6대 제약조건 | 핵심 요구 원칙 | 아키텍처 기대 효과 |
|---|---|---|
| Client-Server | 사용자 인터페이스 관심사와 데이터 저장 관심사의 완전한 분리 | 플랫폼 독립적 진화 지원 |
| Stateless (무상태) | 서버에 클라이언트 컨텍스트 저장 금지, 요청 내 완전한 정보 포함 | 서버 확장성 및 복구성 향상 |
| Cacheable (캐시 가능) | 모든 응답에 캐시 제어 헤더(Cache-Control) 명시 필수 | 네트워크 대역폭 절감 및 응답속도 향상 |
| Uniform Interface | 자원 식별, 표현을 통한 조작, 자기서술 메시지, HATEOAS 준수 | 전체 아키텍처의 단순화 및 가시성 제공 |
| Layered System | 프록시, 캐시, 로드밸런서 등 중간 계층의 투명한 배치 허용 | 보안 강화 및 부하 분산 캡슐화 |
| Code on Demand (선택) | 서버가 클라이언트에 실행 코드(JS 등)를 전송하여 기능 확장 | 클라이언트 기능 확장성 부여 |

## Ⅳ. HTTP 메서드 특성과 Richardson 성숙도 모델

### HTTP 주요 메서드의 안전성(Safe) 및 멱등성(Idempotent)

| HTTP Method | 자원 조작 행위 | 안전성 (Safety) | 멱등성 (Idempotency) | 캐시 가능성 |
|---|---|---|---|---|
| GET | 자원 상태 조회 | **보장 (Safe)** | **보장 (Idempotent)** | 가능 (기본) |
| POST | 신규 자원 생성 또는 처리 | 미보장 (상태 변경) | **미보장 (호출마다 신규 생성)** | 조건부 가능 |
| PUT | 자원의 전체 교체 (덮어쓰기) | 미보장 (상태 변경) | **보장 (여러 번 수행해도 동일 상태)** | 불가 |
| PATCH | 자원의 부분 수정 | 미보장 (상태 변경) | **미보장 (연산 방식에 따라 상이)** | 조건부 가능 |
| DELETE | 자원 삭제 | 미보장 (상태 변경) | **보장 (삭제 후 부재 상태 불변)** | 불가 |

### Richardson 성숙도 모델 (RMM: Richardson Maturity Model)

```text
Level 3: HATEOAS (응답 본문에 다음 상태 전이 URI 링크 제공)
   ▲
Level 2: HTTP 메서드 및 상태 코드 준수 (GET, POST, PUT, DELETE, 200, 201, 404)
   ▲
Level 1: 개별 자원 식별 (/orders, /users 등 고유 URI 도입)
   ▲
Level 0: 단일 엔드포인트 전송 (단일 URI /api 로 모든 요청을 POST 전송)
```

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 분산 네트워크 재시도 시 POST 요청 중복 실행으로 인한 중복 결제 및 레코드 생성 | 헤더에 클라이언트 생성 UUID 기반 **멱등키(Idempotency Key)** 전달 및 처리 이력 검증 |
| 지나치게 엄격한 HATEOAS 구현 시 페이로드 오버헤드 급증 및 클라이언트 파싱 복잡 | 모바일 및 대용량 트래픽 환경에서는 실용적 Level 2 중심으로 테일러링 수행 |
| 일관성 없는 비표준 에러 응답으로 인한 API 소비자 예외 처리 파편화 | RFC 9457(Problem Details for HTTP APIs) 표준 규격의 일관된 JSON 에러 포맷 적용 |

## Ⅵ. 제언

OpenAPI Specification 기반의 API 계약 우선(Contract-First) 개발과 멱등성 보장 인프라 표준화

### 멱등키(Idempotency Key) 기반 중복 방지 처리 파이프라인

```text
클라이언트: POST 요청 + 헤더 `Idempotency-Key: <UUID>` 전송
    ↓
API Gateway / 서버: 멱등키 캐시(Redis) 확인
    ├─ 동일 멱등키 처리 중 → 409 Conflict 또는 대기 응답
    ├─ 동일 멱등키 기완료 → 저장된 이전 응답 결과 즉시 반환 (비즈니스 로직 스킵)
    └─ 신규 멱등키 → 비즈니스 로직 정상 실행 후 결과 캐싱
```

### 계약 우선(Contract-First) API 개발 및 검증 파이프라인

```text
OpenAPI(Swagger) 3.1 명세서 공동 설계
    ↓
API Mock 서버 자동 생성 (프론트/백엔드 병렬 개발)
    ↓
코드 생성기 연계: DTO 및 컨트롤러 인터페이스 자동 생성
    ↓
소비자 주도 계약 테스트(Pact) 자동화를 통한 하위 호환성 상시 검증
```

### 선택 근거: 전통적 코드 우선과 계약 우선(Contract-First) 비교

| 구분 | 코드 우선 개발 (Code-First) | 제언: 계약 우선 개발 (Contract-First) |
|---|---|---|
| 설계 일관성 | 개발자 성향에 따라 URI 및 응답 불일치 | 전사 REST 표준 가이드라인 강제 준수 |
| 협업 효율성 | 백엔드 구현 완료 시까지 프론트엔드 대기 | Mock 서버를 활용한 즉각적인 병렬 개발 |
| 변경 가시성 | 인터페이스 변경 시 사전 감지 난해 | 명세 버전 관리로 Breaking Change 선제 예방 |

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 1교시: REST API
- 제134회 정보관리기술사 4교시: SOAP 및 REST의 구성요소
- Roy Thomas Fielding, Architectural Styles and the Design of Network-based Software Architectures (Doctoral dissertation)
- RFC 9110 — HTTP Semantics
- RFC 9457 — Problem Details for HTTP APIs

## 연결 토픽

- 이전 토픽: [ATAM](./014_atam.md)
- 연관 토픽: [SOAP](./037_soap.md), [Open API](./022_open_api.md)
- 다음 토픽: [기술 부채](./016_technical_debt.md)
