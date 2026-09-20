---
title: "REST"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기출 · 96%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "122회, 133회, 134회"
  priority: 96
  priority_note: "[출제:133,134] · [출제(KPC):122]"
---

## 답안 골격
```text
[REST] ◀━━ 머리: Ⅶ 내 의견 (성숙도 모델 Level 2 안주 탈피 및 HATEOAS를 통한 결합도 완화)
 ┃
 ┣━ Ⅰ 개요 ───── 복잡한 SOAP/WSDL 프로토콜 오버헤드 → 웹 표준 HTTP 자원 기반 아키텍처 스타일
 ┣━ Ⅱ 특징 ───── 자원(URI) · 행위(HTTP Method) · 표현(Representation, JSON/XML)의 분리
 ┣━ Ⅲ 구조 ───── 6대 제약조건(클라이언트-서버, 무상태, 캐시, 계층화, 코드온디맨드, 균일한 인터페이스)
 ┣━ Ⅳ 흐름 ───── 클라이언트 요청(Method + URI) → 서버 자원 식별 → JSON 표현 생성 및 캐시 헤더 반환
 ┣━ Ⅴ 비교 ───── REST vs SOAP vs GraphQL
 ┗━ Ⅵ 실무 ───── 무늬만 REST(HTTP RPC) 남발 / 리차드슨 성숙도 모델(RMM) Level 3 적용
```
- 필수 키워드: 로이 필딩 · 자원(URI) · HTTP Method · Stateless · Self-descriptive · HATEOAS · RMM
- 배점 전략: 10점 = Ⅱ 3대 요소 → Ⅲ 6대 제약조건 → Ⅴ SOAP/GraphQL 비교 / 25점 = Ⅰ~Ⅶ 전개, 리차드슨 성숙도 모델 4단계 및 진정한 REST 구현 조건
- 기출: 133회 1교시 `REST API에 대하여 설명하시오.` → Ⅰ·Ⅱ·Ⅲ / 134회 4교시 `개방형 API(Open API)` → Ⅳ·Ⅵ

## 한 줄 본질
- 원격 프로시저 호출(RPC) 및 SOAP의 무거운 XML 파싱과 강한 결합도 병목 → 웹의 기존 인프라(HTTP, URI, MIME)를 그대로 활용하여 자원을 명시하고 무상태(Stateless)로 상호작용 → 분산 하이퍼미디어 시스템의 독립적 진화와 캐싱 극대화 / 대용량 스트리밍 및 오버페칭 비효율 대가

## 핵심 그림
```text
[ Client ]  --- GET /users/102 (HTTP Header: Accept: application/json) --->  [ Server ]
            <-- 200 OK (Cache-Control: max-age=3600, ETag: "x1") -----------
                { "id": 102, "name": "Kim",
                  "_links": { "self": { "href": "/users/102" },
                              "orders": { "href": "/users/102/orders" } } }
```

## 핵심 용어
- 무상태성(Stateless): 클라이언트의 이전 상태를 서버 메모리에 저장하지 않고, 각 요청에 처리에 필요한 모든 정보(인증 토큰 등)를 포함하여 전달하는 성질
- HATEOAS(Hypermedia As The Engine Of Application State): 응답 본문에 다음 상태로 전이할 수 있는 하이퍼링크를 포함시켜 클라이언트가 API의 URI 구조를 하드코딩하지 않게 하는 제약

## 핵심 통찰
- 실무의 대다수 "RESTful API"는 URI에 자원을 명시하고 JSON을 주고받는 수준(RMM Level 2)일 뿐, 자기서술적 메시지(Self-descriptive)와 HATEOAS를 만족하지 못하는 HTTP RPC에 가까움
- Stateless 제약은 서버 확장을 극적으로 쉽게 만들지만, 매 요청마다 인증 토큰(JWT 등)을 검증해야 하므로 토큰 파싱 오버헤드가 발생함
- 자원의 세부 속성 중 일부만 필요한 모바일 환경에서는 REST의 오버페칭(Over-fetching) 문제가 발생하며, 이는 GraphQL을 도입하는 주요 동기가 됨

## 이웃 토픽과 구분
- REST vs GraphQL: REST = 엔드포인트별 고정 데이터 반환, HTTP 캐시 활용 우수 / GraphQL = 단일 엔드포인트에서 클라이언트가 원하는 필드만 정확히 쿼리

## 문제·원인·대책
- 사례: 133회 기출 모바일 대국민 포털 서비스의 REST API 개편 트러블슈팅
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 화면 구성 시 10개 이상의 REST 엔드포인트 연속 호출로 지연 발생 | 엔터티 중심 REST 설계로 인한 N+1 네트워크 언더페칭(Under-fetching) | BFF(Backend For Frontend) 패턴 도입 및 필요 필드 집계 API 제공 | 클라이언트 네트워크 왕복 횟수 80% 감축 |
| API URI 변경 시 모바일 앱이 하드코딩된 경로 오류로 비정상 종료 | HATEOAS 미준수로 클라이언트와 서버 URI 간의 강한 결합 발생 | 응답 페이로드 내 HAL/JSON-LD 링크 표준화 및 동적 링크 탐색 클라이언트 구현 | 클라이언트 배포 없이 서버 API 경로 자율적 진화 |

## 이렇게 출제된다
- 제133회 1교시 1번: "REST API(REpresentational State Transfer Application Programming Interface)에 대하여 설명하시오." → 요구 포인트: Ⅰ 개념 + Ⅱ 3대 요소 + Ⅲ 6대 원칙 + Ⅳ 리차드슨 성숙도 모델
- 제134회 4교시 4번: "개방형 API(Open API)에 대하여 설명하시오." → 요구 포인트: RESTful 아키텍처 기반의 OpenAPI Specification(OAS) 및 거버넌스

## 내 의견
- [HTTP Method만 맞추면 REST라는 착각] GET 요청에 요청 본문을 넣거나 수정 행위를 GET으로 처리하고, 응답 코드는 무조건 200 OK로 퉁치는 가짜 REST API 만연 → 나라면: 리차드슨 성숙도 모델(RMM) Level 2 준수를 기본 품질 게이트로 두고, OpenAPI(Swagger) 명세서를 단일 진실 공급원(SSOT)으로 삼아 클라이언트 SDK와 서버 라우팅 코드를 자동 생성하는 Contract-First 개발 체계 확립
