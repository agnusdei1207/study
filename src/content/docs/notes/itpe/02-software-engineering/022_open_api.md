---
title: "Open API(API 일반)"
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

## Ⅰ. Open API의 개요

- 개념 : 기업이나 기관이 보유한 핵심 데이터, 비즈니스 로직, 플랫폼 기능을 **표준화된 인터페이스 규격** (RESTful, JSON 등)을 통해 외부 서드파티 개발자에게 개방하여 상호 연동할 수 있도록 제공하는 공개 프로그래밍 인터페이스.
- 배경 및 필요성 : 플랫폼 비즈니스 생태계 확장, 마이데이터 및 금융 핀테크 혁신, 내부 데이터의 **수익화** (API Monetization) 및 파트너십 가속화.
- 핵심 가치 : **네트워크 효과** 창출, 개발 리드타임 단축, **개방형 혁신** (Open Innovation) 촉진.

## Ⅱ. Open API 생태계 아키텍처 및 연동 흐름

```text
   [ 외부 앱 / 파트너 ] ──> [ API Gateway ] ──────────> [ 내부 백엔드 서비스 ]
          │                   │ (보안/인증/라우팅)            │ (MSA/DB)
          │                   ▼                              │
          └───────────> [ Developer Portal ] <───────────────┘
                        - API 카탈로그 / 명세서(OAS)
                        - API 키 발급 및 SDK 제공
                        - 트래픽 모니터링 / 과금
```

- **Developer Portal** : 개발자가 API 명세를 확인(Swagger/OAS)하고, 테스트 샌드박스를 사용하며 API Key 발급 및 사용량을 확인하는 개발자 창구.
- **API Gateway** : 모든 외부 요청의 진입점으로서 **OAuth 2.0** 기반 인증/인가, **Rate Limiting** (호출 제한), 트래픽 라우팅, SSL 종단, 캐싱 및 로깅 일괄 수행.
- **API Management (APIM)** : 수명주기 관리(기획->발행->버전관리->폐기), 수익화 과금(Billing) 모델 지원.

## Ⅲ. 주요 API 프로토콜 및 연동 방식 비교

| 비교 항목 | REST API | GraphQL | gRPC |
|---|---|---|---|
| 프로토콜 | HTTP/1.1, HTTP/2 | HTTP POST 기반 **단일 엔드포인트** | **HTTP/2** 기반 **바이너리 전송** |
| 데이터 포맷 | JSON, XML | JSON | **Protocol Buffers** (Protobuf) |
| 오버/언더페칭 | 다수 엔드포인트 호출 및 불필요 필드 수신 | 단일 쿼리로 클라이언트가 원하는 필드만 정확히 요청 | 고정 스키마 바이너리 직렬화 |
| 성능 및 대역폭 | 텍스트 기반으로 오버헤드 존재 | 네트워크 왕복 감소, 서버 파싱 오버헤드 | 초고속 바이너리 통신, 스트리밍 지원 |
| 주 활용 분야 | 범용 퍼블릭 Open API, 모바일 백엔드 | 모바일 UI 데이터 애그리게이션 | 마이크로서비스 내부 통신, IoT, 실시간 통신 |

## Ⅳ. Open API의 주요 한계점 및 해결 방안

- 무분별한 트래픽 유입 및 악의적 DoS 공격에 의한 백엔드 고갈 :
  - 한계점 : 공개된 Open API 엔드포인트로 비정상적인 대용량 트래픽이 유입되거나 무단 데이터 스크래핑 봇이 동작할 경우 백엔드 리소스가 고갈되어 전체 서비스 장애 발생.
  - 해결 방안 : 엔터프라이즈 API Gateway(Kong, Apigee)를 전진 배치하여 토큰 버킷(Token Bucket) 및 리키 버킷(Leaky Bucket) 알고리즘 기반 계정별 Rate Limiting/Throttling을 강제 적용하고 WAF 연계 차단.
- API 인터페이스 변경 시 서드파티 생태계 하위 호환성 파손 :
  - 한계점 : 불특정 다수의 외부 개발사 및 애플리케이션이 의존하는 특성상, 파라미터 삭제나 응답 구조 변경 시 외부 클라이언트에서 런타임 오류가 집단 발생.
  - 해결 방안 : URI 경로(`/v1`, `/v2`) 또는 헤더 기반 명시적 API 버전 관리 정책을 수립하고, 구버전 필드는 즉시 삭제 대신 비권장(Deprecated) 처리 후 충분한 일몰(Sunset) 유예 기간 부여.
- API 키 유출 및 객체 레벨 권한 취약점(BOLA/IDOR) :
  - 한계점 : 클라이언트 코드에 하드코딩된 API 키 탈취 또는 URL 리소스 ID 변조를 통해 타인의 데이터에 무단 접근하는 OWASP API Top 10 1위 취약점(BOLA) 노출.
  - 해결 방안 : OAuth 2.0 / OIDC 기반의 단기 유효 JWT 토큰 체계로 전환하고, API Gateway 및 백엔드 서비스 계층에서 호출자의 사용자 식별자와 리소스 소유권을 교차 검증하는 인가 로직(ABAC/PBAC) 강제.

## Ⅴ. Open API 보안 및 거버넌스를 위한 기술사적 제언

- OWASP API Security Top 10 대응 체계 확립 : 특히 BOLA(Broken Object Level Authorization), 무분별한 자원 소비(Rate Limit 부재)를 차단하기 위해 세분화된 토큰 스코프 검증과 WAF/API 게이트웨이 연계 필수.
- 하위 호환성을 보장하는 시맨틱 버저닝(Semantic Versioning) : URI 경로에 버전 명시(/v1, /v2)를 표준화하고, 구버전 API 폐기(Deprecation) 시 선제적 공지와 유예 기간을 제공하는 API 라이프사이클 거버넌스 수립.
