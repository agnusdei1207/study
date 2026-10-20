---
title: "Open API(API 일반) (API: Application Programming Interface)"
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

- Open API, API Gateway, Developer Portal, APIM(API Management), API 수익화(Monetization)
- REST API, GraphQL, gRPC, OpenAPI Specification(OAS), OWASP API Security Top 10, Rate Limiting

## Ⅰ. Open API의 개요

- 핵심 요약 : 기업·기관의 데이터와 기능을 표준 인터페이스로 외부 개발자에게 개방하는 공개 프로그래밍 인터페이스.
- 개념 : 기업이나 기관이 보유한 핵심 데이터, 비즈니스 로직, 플랫폼 기능을 표준화된 인터페이스 규격(RESTful, JSON(JavaScript Object Notation) 등)을 통해 외부 서드파티 개발자에게 개방하여 상호 연동할 수 있도록 제공하는 공개 프로그래밍 인터페이스 (**API**, Application Programming Interface).
- 배경 및 필요성 : 플랫폼 비즈니스 생태계 확장, 마이데이터 및 금융 핀테크 혁신, 내부 데이터의 수익화(API Monetization) 및 파트너십 가속화 필요.
- 주요 목적 : 네트워크 효과 창출, 개발 리드타임 단축, 개방형 혁신(Open Innovation) 촉진.

## Ⅱ. Open API의 특징

- 핵심 요약 : 표준 인터페이스 개방을 통한 네트워크 효과와 생태계 기반 수익화가 특징.
1. 표준화된 인터페이스 규격 : RESTful, JSON 등 범용 웹 표준 기반 개방.
2. 네트워크 효과 : 참여 개발자와 서비스 증가에 따른 생태계 가치의 상승.
3. 수익화(Monetization) : 사용량 기반 과금(Billing) 모델을 통한 데이터·기능의 매출화.
4. 개방형 혁신(Open Innovation) : 서드파티 개발자와의 협업을 통한 신규 서비스 창출.
5. 개발 리드타임 단축 : SDK(Software Development Kit), 샌드박스, 명세서 제공을 통한 파트너 개발 가속.

## Ⅲ. Open API의 구조 (흐름)

- 핵심 요약 : Developer Portal- API Gateway-백엔드 서비스의 3계층 생태계 구조.

```text
[ Open API 생태계 아키텍처 ]
[ 외부 앱/파트너 ]
   │ ① API 호출
   ▼
[ API Gateway ]
   OAuth 2.0 인증/인가, Rate Limiting,
   라우팅, SSL 종단, 캐싱, 로깅
   │ ② 백엔드 전달
   ▼
[ 내부 백엔드 서비스 ] (MSA/DB)

[ Developer Portal ] (개발자 창구)
   API 카탈로그/명세서(OAS), API 키 발급,
   SDK 제공, 트래픽 모니터링/과금
```

```text
[ API Gateway 요청 처리 파이프라인 ]
클라이언트 요청
   ↓ 인증/인가 (OAuth 2.0 / JWT 검증)
   ↓ 호출 제한 (Token Bucket / Leaky Bucket)
   ↓ 라우팅 및 SSL(Secure Sockets Layer) 종단
   ↓ 캐싱 / 로깅
백엔드 서비스 → 응답
```

- Developer Portal : 개발자가 API 명세를 확인(Swagger/OAS)하고 테스트 샌드박스를 사용하며 API Key 발급 및 사용량을 확인하는 개발자 창구.
- API Gateway : 모든 외부 요청의 진입점으로서 OAuth(Open Authorization) 2.0 기반 인증/인가, Rate Limiting(호출 제한), 트래픽 라우팅, SSL 종단, 캐싱 및 로깅 일괄 수행.
- API Management(APIM) : 수명주기 관리(기획→발행→버전관리→폐기), 수익화 과금 모델 지원.

## Ⅳ. 주요 API 프로토콜 및 연동 방식의 비교

- 핵심 요약 : REST는 범용 개방, GraphQL은 클라이언트 주도 조회, gRPC는 내부 고성능 통신에 적합.

| 비교 항목 | REST(Representational State Transfer) API | GraphQL | gRPC |
|---|---|---|---|
| 프로토콜 | HTTP(Hypertext Transfer Protocol)/1.1, HTTP/2 | HTTP POST 기반 단일 엔드포인트 | HTTP/2 기반 바이너리 전송 |
| 데이터 포맷 | JSON, XML(Extensible Markup Language) | JSON | Protocol Buffers(Protobuf) |
| 오버/언더페칭 | 다수 엔드포인트 호출 및 불필요 필드 수신 | 단일 쿼리로 클라이언트가 원하는 필드만 정확히 요청 | 고정 스키마 바이너리 직렬화 |
| 성능 및 대역폭 | 텍스트 기반으로 오버헤드 존재 | 네트워크 왕복 감소, 서버 파싱 오버헤드 | 초고속 바이너리 통신, 스트리밍 지원 |
| 주 활용 분야 | 범용 퍼블릭 Open API, 모바일 백엔드 | 모바일 UI(User Interface) 데이터 애그리게이션 | 마이크로서비스 내부 통신, IoT(Internet of Things), 실시간 통신 |

## Ⅴ. Open API의 장점과 한계

- 핵심 요약 : 생태계 확장·수익화의 장점, 트래픽 폭증·호환성 파손·객체 권한 취약점의 한계.
- 장점
  1. 플랫폼 생태계 확장과 네트워크 효과 창출.
  2. 데이터·기능의 수익화 및 파트너십 가속.
  3. 개방형 혁신을 통한 신규 서비스 창출.
- 한계점 1 : 무분별한 트래픽 유입 및 악의적 DoS(Denial of Service) 공격에 의한 백엔드 고갈
  - 한계점 : 공개된 엔드포인트로 비정상적인 대용량 트래픽이 유입되거나 무단 데이터 스크래핑 봇이 동작할 경우 백엔드 리소스 고갈 및 전체 서비스 장애 발생.
  - 해결 방안 : 엔터프라이즈 API Gateway(Kong, Apigee) 전진 배치, 토큰 버킷(Token Bucket) 및 리키 버킷(Leaky Bucket) 알고리즘 기반 계정별 Rate Limiting/Throttling 강제 적용, WAF(Web Application Firewall) 연계 차단.
- 한계점 2 : API 인터페이스 변경 시 서드파티 생태계 하위 호환성 파손
  - 한계점 : 불특정 다수의 외부 개발사 및 애플리케이션이 의존하는 특성상 파라미터 삭제나 응답 구조 변경 시 외부 클라이언트의 런타임 오류 집단 발생.
  - 해결 방안 : URI(Uniform Resource Identifier) 경로(/v1, /v2) 또는 헤더 기반 명시적 버전 관리 정책 수립, 구버전 필드의 즉시 삭제 대신 비권장(Deprecated) 처리 및 충분한 일몰(Sunset) 유예 기간 부여.
- 한계점 3 : API 키 유출 및 객체 레벨 권한 취약점(BOLA/IDOR)
  - 한계점 : 클라이언트 코드에 하드코딩된 API 키 탈취 또는 URL(Uniform Resource Locator) 리소스 ID(Identifier) 변조를 통한 타인 데이터 무단 접근, OWASP(Open Worldwide Application Security Project) API Top 10 1위 취약점(BOLA, Broken Object Level Authorization) 노출.
  - 해결 방안 : OAuth 2.0 / OIDC(OpenID Connect) 기반 단기 유효 JWT(JSON Web Token) 토큰 체계 전환, API Gateway 및 백엔드 계층에서 호출자 식별자와 리소스 소유권을 교차 검증하는 ABAC(Attribute-Based Access Control)/PBAC(Policy-Based Access Control) 인가 로직 강제.

## Ⅵ. Open API 보안 및 거버넌스를 위한 기술사적 제언

- 핵심 요약 : OWASP API Security Top 10 대응 체계와 시맨틱 버저닝 기반 라이프사이클 거버넌스.
- OWASP API Security Top 10 대응 체계 확립 : 특히 BOLA(Broken Object Level Authorization)와 무분별한 자원 소비(Rate Limit 부재) 차단을 위한 세분화된 토큰 스코프 검증 및 WAF/API Gateway 연계 필수.
- 하위 호환성을 보장하는 시맨틱 버저닝(Semantic Versioning) : URI 경로 버전 명시(/v1, /v2) 표준화, 구버전 API 폐기(Deprecation) 시 선제적 공지와 유예 기간 제공의 API 라이프사이클 거버넌스 수립.
- 프로토콜 적재적소 운영 : 퍼블릭 개방 영역의 REST와 내부 고성능 통신의 gRPC를 구분한 이중 전략 채택.

## Ⅶ. 결론

- 핵심 요약 : Open API는 보안·호환성·거버넌스 체계를 갖춘 상태에서 개방할 때 생태계 가치가 극대화.
- 요약 : Developer Portal-API Gateway-백엔드 3계층 구조와 OAS 기반 명세 표준화가 생태계의 기반.
- 시사점 : Rate Limiting, 버전 관리, 객체 레벨 인가 강화를 통한 안전한 개방형 플랫폼 운영 필요.
