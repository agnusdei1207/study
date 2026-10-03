---
title: "REST"
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

## Ⅰ. REST(Representational State Transfer)의 개요

- 개념 : 웹의 창시자 중 한 명인 로이 필딩(Roy Fielding)이 2000년 박사 학위 논문에서 제시한 아키텍처 스타일로, HTTP 고유의 특성을 최대한 활용하여 네트워크 상의 자원(Resource)을 명확히 식별하고 상태를 주고받는 분산 하이퍼미디어 시스템 아키텍처.
- 배경 및 필요성 : 과거 복잡한 RPC(Remote Procedure Call)나 무거운 SOAP/XML 기반 통신의 복잡성을 극복하고, 플랫폼 독립적이며 단순하고 확장성 높은 웹 기반 API 연동 표준으로 자리매김.
- 핵심 구성요소 3요소 : 자원(URI), 행위(HTTP Method: GET/POST/PUT/PATCH/DELETE), 표현(Representation: JSON/XML).

## Ⅱ. REST 아키텍처의 6대 제약조건

```text
   [ Client-Server ] ──── 사용자 인터페이스와 데이터 저장소의 관심사 분리
          │
   [ Stateless ] ──────── 서버가 클라이언트의 세션 상태를 보관하지 않음
          │
   [ Cacheable ] ──────── HTTP 캐싱 헤더(Cache-Control)를 통한 응답 캐싱
          │
   [ Layered System ] ─── 게이트웨이, 로드밸런서, 프록시 등 계층적 구조
          │
   [ Code-on-Demand ] ─── 자바스크립트 등 실행 코드를 동적으로 전송 (선택)
          │
   [ Uniform Interface ] ─ 자원 식별, 표현을 통한 조작, 자기서술적 메시지, HATEOAS
```

- Uniform Interface 4대 원칙 :
  - **자원의 식별 (Identification of Resources)** : URI를 통한 고유 자원 식별 (예: /orders/123).
  - **표현을 통한 자원 조작 (Manipulation through Representations)** : 메시지 본문의 JSON 표현을 통한 생성 및 변경.
  - **자기 서술적 메시지 (Self-descriptive Messages)** : Content-Type 헤더 등 메시지 자체만으로 온전히 해석 가능한 구조.
  - **HATEOAS (Hypermedia As The Engine Of Application State)** : 응답 본문에 다음 상태로 전이할 수 있는 하이퍼링크를 포함.

## Ⅲ. Richardson 성숙도 모델(RMM) 4단계 분석

| 레벨 | 핵심 메커니즘 | HTTP 활용 수준 | 예시 |
|---|---|---|---|
| **Level 0** | 단일 URI와 단일 메서드(POST) 활용 | 단순 전송 터널로 활용 (RPC 스타일) | POST /endpoint (payload에 method 기재) |
| **Level 1** | 개별 자원마다 고유한 URI 부여 | 자원 개념 도입 | POST /users, POST /users/1/orders |
| **Level 2** | 자원에 맞는 HTTP 메서드(GET/POST/PUT 등)와 상태코드 적용 | HTTP 동사 및 규약의 올바른 활용 | GET /users/1, 200 OK / 201 Created |
| **Level 3** | HATEOAS 도입 (하이퍼미디어 링크 제공) | 진정한 의미의 완전한 RESTful API 달성 | 응답 내 "_links": { "self": "...", "cancel": "..." } |

## Ⅳ. REST의 주요 한계점 및 해결 방안

- 고정 엔드포인트 응답으로 인한 오버페칭(Over-fetching) 및 언더페칭(Under-fetching) :
  - 한계점 : 리소스 엔드포인트의 반환 스키마가 고정되어 있어 클라이언트에 불필요한 데이터까지 전송(Over-fetching)되거나, 연관 데이터를 조회하기 위해 N+1번의 다중 API 왕복 호출(Under-fetching) 발생.
  - 해결 방안 : 필드 필터링(Sparse Fieldsets) 쿼리 파라미터를 지원하거나, 클라이언트 플랫폼별 전용 BFF(Backend For Frontend) 계층을 구축하고, 복잡한 클라이언트 주도형 쿼리 영역에는 GraphQL 혼용 검토.
- HATEOAS 및 자기서술적 메시지 구현의 현실적 난제 :
  - 한계점 : REST 성숙도 모델(Richardson 성숙도 3단계)의 완전한 준수를 위한 HATEOAS(하이퍼미디어 링크 제공) 구현은 백엔드 개발 공수를 과도하게 증가시키나 클라이언트 소비 효용은 미미.
  - 해결 방안 : 실용적 REST(Pragmatic REST) 가이드라인을 채택하여 HATEOAS 대신 OpenAPI 3.0 스펙을 기반으로 API 계약을 표준화하고, OpenAPI Generator를 통한 클라이언트 SDK 코드 자동 생성 파이프라인 구축.
- HTTP 표준 메서드의 한계와 복합 비즈니스 행위 표현 제약 :
  - 한계점 : CRUD 중심의 4대 HTTP 동사(GET, POST, PUT, DELETE)만으로 '결제 승인', '주문 취소', '일괄 상태 전이' 등 상태 기계(State Machine) 기반 복합 도메인 행위를 직관적으로 URI에 표현하기 곤란.
  - 해결 방안 : 컨트롤러 리소스 패턴(Sub-resource `/orders/{id}/cancel` 등)을 명문화하거나, 도메인 주도 설계(DDD) 기반의 명령-조회 분리(CQRS) 패턴 및 이벤트 주도 비동기 API 연계.

## Ⅴ. 대규모 마이크로서비스 환경에서의 기술사적 제언

- 실용적 REST(Pragmatic REST)와 gRPC 간의 적재적소 선택 : 외부 퍼블릭 클라이언트 연동에는 가독성과 범용성이 뛰어난 REST/JSON(Level 2 중심)을 표준으로 삼되, 마이크로서비스 간 내부 통신(East-West)에는 바이너리 프로토콜 기반의 고성능 gRPC(HTTP/2)를 혼용하는 하이브리드 아키텍처 권장.
- OpenAPI Specification(OAS) 기반 API 거버넌스 수립 : Swagger/OAS 문서를 자동 생성하고 API Gateway에서 인증, 트래픽 셰이핑, 계약 테스트(Pact)를 연계하여 API 파손 방지.
