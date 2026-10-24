---
title: "REST(Representational State Transfer)"
author: "agnusdei1207"
date: "2026-10-24T23:54:03+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- REST(Representational State Transfer), RESTful, Roy Fielding, 아키텍처 스타일
- Uniform Interface, HATEOAS, Stateless, Richardson 성숙도 모델(RMM), OpenAPI(OAS), gRPC, BFF

## Ⅰ. REST의 개요

- 핵심 요약 : HTTP의 고유 특성을 살려 자원을 식별하고 그 표현을 주고받는 분산 하이퍼미디어 아키텍처 스타일.
- 개념 : HTTP 명세 작성에 참여한 로이 필딩(Roy Fielding)이 2000년 박사 논문에서 제시한 아키텍처 스타일로, 네트워크상의 자원을 URI로 식별하고 그 표현을 주고받는 방식 (**REST**, Representational State Transfer).
- 배경 및 필요성 : 복잡한 RPC(Remote Procedure Call)나 무거운 SOAP(Simple Object Access Protocol) 기반 연동은 구현과 연동 비용이 커서, 플랫폼에 독립적이고 단순한 웹 API 연동 방식이 필요해짐.
- 주요 목적 : 자원, 행위, 표현의 3대 구성요소로 일관된 자원 지향 연동 체계를 구축.

## Ⅱ. REST의 특징 및 장점

- 핵심 요약 : 6대 제약조건이 확장성과 독립성을 만들고, 그중 Uniform Interface가 REST를 다른 방식과 구분하는 핵심 원칙.

1. Client-Server : 사용자 인터페이스와 데이터 저장소를 분리 → 양쪽이 독립적으로 진화.
2. Stateless (무상태) : 요청마다 필요한 정보를 모두 담고 세션 상태는 서버가 보관하지 않음 → 수평 확장과 장애 격리가 쉬움.
3. Cacheable (캐시 가능) : 응답에 캐시 가능 여부를 표시 → 반복 요청의 지연과 서버 부하 감소.
4. Layered System (계층화) : 게이트웨이, 프록시, 로드밸런서를 중간에 두는 것을 허용 → 보안과 트래픽 제어 계층 추가가 자유로움.
5. Code-on-Demand (주문형 코드) : 실행 코드를 필요할 때 내려받는 선택적 제약 → 클라이언트 기능 확장.
6. **Uniform Interface** (일관된 인터페이스) : 아래 4원칙으로 구성된 통일된 인터페이스 → 구현이 달라도 같은 방식으로 상호작용.
   - 자원 식별 : URI로 고유 자원을 식별.
   - 표현을 통한 자원 조작 : JSON 등 표현을 주고받아 생성·변경.
   - 자기서술적 메시지 : Content-Type 등 헤더만으로 메시지를 해석.
   - **HATEOAS** (Hypermedia As The Engine Of Application State) : 응답에 다음 상태로 가는 링크를 포함.

## Ⅲ. REST의 구조 (흐름)

- 핵심 요약 : 자원-행위-표현의 3대 구성요소 위에서 계층화와 무상태 원칙을 따르는 요청-응답 흐름.

```text
[ REST 3대 구성요소 ]

자원 (Resource) : URI로 식별 (/orders/123)
          ↓
행위 (Verb) : HTTP 메서드 (GET, POST 등)
          ↓
표현 (Representation) : JSON, XML 본문
```

```text
[ 요청-응답 흐름 ]

클라이언트
          ↓ HTTP 요청
프록시 / 게이트웨이 (계층화)
          ↓
서버 (세션 상태 미보관, 무상태)
          ↓
응답 : 자원 표현 + 상태 전이 링크
```

- 실무 관행 : 업계에서는 HATEOAS를 생략한 Level 2 수준의 실용적 REST(Pragmatic REST)를 주로 적용.

## Ⅳ. Richardson 성숙도 모델 4단계 비교

- 핵심 요약 : Richardson 성숙도 모델(RMM)로 보면 단일 엔드포인트의 RPC형 호출에서 하이퍼미디어 기반 REST까지 단계적으로 성숙함.

| 레벨 | 핵심 메커니즘 | 예시 |
| --- | --- | --- |
| Level 0 | 단일 URI와 단일 메서드로 전송 (RPC형) | POST /endpoint (본문에 호출 정보) |
| Level 1 | 개별 자원마다 고유 URI 부여 | POST /users, POST /users/1/orders |
| Level 2 | 자원에 맞는 HTTP 메서드와 상태 코드 사용 | GET /users/1 → 200 OK, 201 Created |
| Level 3 | HATEOAS로 하이퍼미디어 링크 제공 | 응답에 "_links" 항목으로 다음 행위 제시 |

- 업계 관행 : 대다수 API가 Level 2에 머물며 Level 3 완전 준수 사례는 제한적.

## Ⅴ. REST의 장점과 한계

- 핵심 요약 : 범용성과 확장성이라는 장점과 달리, 응답 과부하, 링크 구현 부담, 복합 행위 표현의 어려움이 한계.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 오버페칭·언더페칭 | 고정 응답 스키마 → 불필요한 데이터 전송 또는 연쇄 호출 증가 | 필드 선택 쿼리 지원, 클라이언트별 BFF(Backend For Frontend) 계층 구축 | 응답 크기, 요청당 호출 수 |
| HATEOAS 구현 난제 | 링크 구현 공수 대비 클라이언트 활용 효과가 작음 | 실용적 REST 채택, OpenAPI 명세 기반 계약 관리 | 명세 준수율, 계약 위반 건수 |
| 복합 행위 표현 제약 | 4대 HTTP 메서드만으로 결제 승인·주문 취소 같은 상태 전이를 표현하기 어려움 | 하위 자원 행위 URI(/orders/{id}/cancel) 명문화, 명령과 조회 분리(CQRS) 검토 | 행위 URI 일관성, 상태 전이 오류율 |

## Ⅵ. 마이크로서비스 환경에서의 기술사적 제언

- 핵심 요약 : 외부는 REST, 내부는 gRPC로 나누어 쓰고 OpenAPI 명세로 API 거버넌스를 세우는 방향.

1. 외부와 내부 통신의 분리 : 외부 공개 API는 가독성과 범용성이 높은 REST/JSON을 기준으로 하고, 서비스 간 내부 통신에는 HTTP/2 기반 gRPC를 적용한다.
2. 명세 중심의 API 거버넌스 : 조직 차원에서 OpenAPI 명세를 설계 산출물로 삼고, 게이트웨이의 인증과 트래픽 제어, 계약 테스트를 함께 운영한다.
3. 리소스 설계 표준 : URI 명명 규칙, 상태 코드 사용법, 버전 관리 방식을 조직 가이드로 정해 API 간 일관성을 확보한다.

## Ⅶ. 결론

- 핵심 요약 : REST는 HTTP 위에서 단순하고 확장 가능한 자원 지향 연동을 제공하는 표준 아키텍처 스타일.
- 시사점 : 실용적 수준의 REST와 BFF, CQRS 같은 보완 기법을 함께 쓸 때 오버페칭과 복합 행위 표현의 한계를 넘을 수 있음.
