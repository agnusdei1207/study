---
title: "REST(Representational State Transfer)"
author: "agnusdei1207"
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

## 연관 키워드

- REST(Representational State Transfer), RESTful, Roy Fielding, 아키텍처 스타일
- Uniform Interface, HATEOAS, Stateless, Richardson 성숙도 모델(RMM), OpenAPI(OAS), gRPC, BFF

## Ⅰ. REST의 개요

- 핵심 요약 : HTTP 고유 특성을 활용해 자원을 식별하고 상태를 주고받는 분산 하이퍼미디어 시스템 아키텍처 스타일.
- 개념 : 웹의 창시자 중 한 명인 로이 필딩(Roy Fielding)이 2000년 박사 학위 논문에서 제시한 아키텍처 스타일로, HTTP(Hypertext Transfer Protocol) 고유의 특성을 최대한 활용하여 네트워크 상의 자원(Resource)을 명확히 식별하고 상태를 주고받는 분산 하이퍼미디어 시스템 아키텍처 (**REST**, Representational State Transfer).
- 배경 및 필요성 : 과거 복잡한 RPC(Remote Procedure Call)나 무거운 SOAP(Simple Object Access Protocol)/XML(Extensible Markup Language) 기반 통신의 복잡성을 극복하고, 플랫폼 독립적이며 단순하고 확장성 높은 웹 기반 API(Application Programming Interface) 연동 표준의 확립 필요.
- 주요 목적 : 자원, 행위, 표현의 3대 구성요소를 통한 일관된 자원 지향 연동 체계 구축.

## Ⅱ. REST의 특징 (6대 제약조건)

- 핵심 요약 : 6대 제약조건, 특히 Uniform Interface의 4대 원칙이 REST의 차별점.
1. Client-Server(클라이언트-서버) : 사용자 인터페이스와 데이터 저장소의 분리 및 독립적 진화.
2. Stateless(무상태) : 클라이언트 세션 상태의 서버 측 미보관.
3. Cacheable(캐시 가능) : HTTP 캐싱 헤더(Cache-Control) 기반 응답 캐싱.
4. Layered System(계층 시스템) : 게이트웨이, 로드밸런서, 프록시의 계층 구조 허용.
5. Code-on-Demand(주문형 코드) : 실행 코드의 동적 전송(선택 사항).
6. Uniform Interface(일관된 인터페이스) :
   - 자원의 식별(Identification of Resources) : URI(Uniform Resource Identifier) 기반 고유 자원 식별.
   - 표현을 통한 자원 조작(Manipulation through Representations) : 메시지 본문의 JSON(JavaScript Object Notation) 표현을 통한 생성 및 변경.
   - 자기서술적 메시지(Self-descriptive Messages) : Content-Type 헤더 등 메시지 자체만으로 온전히 해석 가능한 구조.
   - HATEOAS(Hypermedia As The Engine Of Application State) : 응답 본문에 다음 상태로 전이 가능한 하이퍼링크 포함.

## Ⅲ. REST의 구조 (흐름)

- 핵심 요약 : 자원-행위-표현의 3대 구성요소와 계층화·무상태 기반 요청-응답 흐름.

```text
[ REST 3대 구성요소 ]
자원(Resource) : URI 고유 식별 (예: /orders/123)
        ↓
행위(Verb) : HTTP Method (GET/POST/PUT/PATCH/DELETE)
        ↓
표현(Representation) : JSON/XML 메시지 본문
```

```text
[ REST 상호작용 흐름 ]
클라이언트 --HTTP 요청--> 프록시/게이트웨이/로드밸런서
        (Layered System : 계층 구조)
                  ↓
        서버 : 세션 상태 미보관(Stateless)
                  ↓
        Cache-Control 기반 캐시 응답(Cacheable)
                  ↓
        응답 : 자원 표현(JSON) + 상태 전이 링크(HATEOAS)
```

- 실용적 관행 : 업계에서는 HATEOAS를 제외한 Level 2 수준의 실용적 REST(Pragmatic REST)가 일반적인 준수 수준.

## Ⅳ. REST 성숙도(Richardson Maturity Model)의 4단계 비교

- 핵심 요약 : 단일 엔드포인트 RPC 스타일에서 하이퍼미디어 기반 완전한 RESTful까지의 단계적 성숙도.

| 레벨 | 핵심 메커니즘 | HTTP 활용 수준 | 예시 |
|---|---|---|---|
| Level 0 | 단일 URI와 단일 메서드(POST) 활용 | 단순 전송 터널로 활용 (RPC 스타일) | POST /endpoint (payload에 method 기재) |
| Level 1 | 개별 자원마다 고유한 URI 부여 | 자원 개념 도입 | POST /users, POST /users/1/orders |
| Level 2 | 자원에 맞는 HTTP 메서드(GET/POST/PUT 등)와 상태코드 적용 | HTTP 동사 및 규약의 올바른 활용 | GET /users/1, 200 OK / 201 Created |
| Level 3 | HATEOAS 도입 (하이퍼미디어 링크 제공) | 진정한 의미의 완전한 RESTful API 달성 | 응답 내 "_links": { "self": "...", "cancel": "..." } |

- 업계 표준 관행은 Level 2 중심이며, Level 3 완전 준수 사례는 제한적.

## Ⅴ. REST의 장점과 한계

- 핵심 요약 : 범용성·확장성의 장점, 오버페칭·HATEOAS 난제·복합 행위 표현 제약의 한계.
- 장점
  1. HTTP 표준 인프라 활용에 따른 플랫폼 독립성과 범용성.
  2. Stateless 구조의 수평 확장 및 장애 격리 용이.
  3. 캐싱과 계층화를 통한 성능 및 가용성 확보.
- 한계점 1 : 고정 엔드포인트 응답에 따른 오버페칭(Over-fetching) 및 언더페칭(Under-fetching)
  - 한계점 : 리소스 엔드포인트의 반환 스키마가 고정되어 있어 클라이언트에 불필요한 데이터까지 전송되거나, 연관 데이터 조회를 위한 N+1번의 다중 API 왕복 호출 발생.
  - 해결 방안 : 필드 필터링(Sparse Fieldsets) 쿼리 파라미터 지원, 클라이언트 플랫폼별 전용 BFF(Backend For Frontend) 계층 구축, 복잡한 클라이언트 주도형 쿼리 영역의 GraphQL 혼용 검토.
- 한계점 2 : HATEOAS 및 자기서술적 메시지 구현의 현실적 난제
  - 한계점 : 성숙도 모델 완전 준수를 위한 하이퍼미디어 링크 구현은 백엔드 개발 공수를 과도하게 증가시키나 클라이언트 소비 효용은 미미.
  - 해결 방안 : 실용적 REST(Pragmatic REST) 가이드라인 채택, OpenAPI 3.0 스펙 기반 API 계약 표준화, OpenAPI Generator를 통한 클라이언트 SDK(Software Development Kit) 코드 자동 생성 파이프라인 구축.
- 한계점 3 : HTTP 표준 메서드의 한계와 복합 비즈니스 행위 표현 제약
  - 한계점 : CRUD(Create, Read, Update, Delete) 중심의 4대 HTTP 동사(GET, POST, PUT, DELETE)만으로 결제 승인, 주문 취소, 일괄 상태 전이 등 상태 기계(State Machine) 기반 복합 도메인 행위의 직관적 URI 표현 곤란.
  - 해결 방안 : 컨트롤러 리소스 패턴(하위 자원 /orders/{id}/cancel 등)의 명문화, 도메인 주도 설계(DDD, Domain-Driven Design) 기반 명령-조회 분리(CQRS, Command Query Responsibility Segregation) 패턴 및 이벤트 주도 비동기 API 연계.

## Ⅵ. 대규모 마이크로서비스 환경에서의 기술사적 제언

- 핵심 요약 : REST와 gRPC의 적재적소 혼용, OAS 기반 API 거버넌스 수립.
- 실용적 REST와 gRPC 간의 적재적소 선택 : 외부 퍼블릭 클라이언트 연동에는 가독성과 범용성이 뛰어난 REST/JSON(Level 2 중심)을 표준으로 삼되, 마이크로서비스 간 내부 통신(East-West)에는 바이너리 프로토콜 기반의 고성능 gRPC(HTTP/2)를 혼용하는 하이브리드 아키텍처 권장.
- OpenAPI Specification(OAS) 기반 API 거버넌스 수립 : Swagger/OAS 문서의 자동 생성, API Gateway에서의 인증·트래픽 셰이핑·계약 테스트(Pact) 연계를 통한 API 파손 방지.
- 리소스 설계 표준화 : URI 명명 규칙, 상태코드, 버전 관리(/v1, /v2)의 조직 표준 가이드라인 정립.

## Ⅶ. 결론

- 핵심 요약 : REST는 HTTP 표준 위에서의 단순하고 확장 가능한 자원 지향 연동 표준.
- 요약 : 6대 제약조건과 Uniform Interface 4원칙이 REST의 본질, Level 2 수준의 실용적 준수가 업계 관행.
- 시사점 : 오버페칭·복합 행위 표현 한계는 BFF·GraphQL·CQRS 등 보완 기법의 적재적소 활용을 통한 극복 필요.
