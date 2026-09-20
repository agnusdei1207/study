---
title: "Open API(API 일반)"
author: "Antigravity"
date: "2026-09-20T12:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
    variant: "tip"
extra:
  model: "Antigravity"

---

## 딸려 나오는 하위 토픽

| 번호 | 토픽명 | 핵심 키워드 | 흡수 근거 |
|---|---|---|---|
| 02-132 | API(Application Programming Interface) | 계약(Contract), 인터페이스 추상화, REST/gRPC/GraphQL, 멱등성, OWASP API Top 10, API-First | API 일반 개념 및 내부/외부 인터페이스 표준 아키텍처의 상위 주제로 통합 |

---

## 답안 골격 (10점 / 25점)

```text
[Open API / API] ◀━━ 머리: Ⅶ 공학적 제언 (API-First 거버넌스와 Zero-Trust 기반 API 보안 통제)
 ┃
 ┣━ Ⅰ 개요 ───── 사일로 극복과 생태계 확장, 인터페이스 추상화 및 명세 기반 표준 계약(Contract)
 ┣━ Ⅱ 생태계 구조 ─ Developer Portal · API Gateway · API Manager/Analytics · Backend Services
 ┣━ Ⅲ API 3대 프로토콜 ─ REST(자원중심, JSON) vs gRPC(HTTP/2, 바이너리) vs GraphQL(단일 쿼리)
 ┣━ Ⅳ 노출 범위별 ─ Open API(퍼블릭 개방) vs Partner API(제휴사) vs Private API(내부 마이크로서비스)
 ┣━ Ⅴ 보안·거버넌스 ─ OAuth 2.0/mTLS, Rate Limiting(토큰 버킷), OpenAPI Spec(OAS), OWASP API Top 10
 ┣━ Ⅵ 실무 문제 ─ 무차별 호출로 인한 리소스 고갈 / 섀도우(Shadow) API로 인한 데이터 유출
 ┗━ Ⅶ 결론 ───── CI/CD 연계 OAS 자동 검증 및 BOLA 방지를 위한 세밀한 인가 체계 구축
```

- **필수 키워드**: API Gateway, OAuth 2.0 / JWT, OpenAPI Specification (OAS), Rate Limiting / Throttling, 토큰 버킷, gRPC / GraphQL, 마이데이터, OWASP API Top 10 (BOLA)
  - **10점형**: API 정의 및 플랫폼 구성도(포털-게이트웨이-백엔드) → REST vs gRPC vs GraphQL 비교표 → 핵심 트래픽 제어 기법.
  - **25점형**: Ⅰ~Ⅶ 전개, Open API 노출 범위(Private/Partner/Public) 분류 + API Gateway 트래픽 제어 알고리즘 + 금융 마이데이터/오픈뱅킹 법제화 표준 및 보안 거버넌스 심층 제시.

---

## 30초 인출용 핵심 다이어그램

```text
+-------------------------------------------------------------------------+
|                  현대적 API 플랫폼 아키텍처 및 트래픽 흐름              |
+-------------------------------------------------------------------------+
|  [외부 개발자/클라이언트]                 [개발자 포털 (Dev Portal)]     |
|   (Web, Mobile, 3rd Party)                - 계정/API Key 발급, 샌드박스 |
|              │ (HTTPS / OAuth 2.0 Bearer) - OAS 명세서 (Swagger)        |
|              ▼                                    ▲                     |
|  +------------------------------------------------┴------------------+  |
|  | [ API Gateway ] (단일 진입점 DMZ 전진 배치)                       |  |
|  | - 인증/인가 (OAuth 2.0, mTLS, JWT 검증)                           |  |
|  | - 트래픽 제어: Throttling / Rate Limiting (Token Bucket)           |  |
|  | - 프로토콜 변환: REST (HTTP/1.1) <-> gRPC (HTTP/2)                |  |
|  +-------------------------------------------------------------------+  |
|              │ 라우팅 (East-West 통신)                                  |
|         ┌────┴───────────────────────────┐                              |
|         ▼ (REST/JSON)                    ▼ (gRPC/Protobuf)              |
|  [ 비즈니스 서비스 A ]            [ 초저지연 트랜잭션 서비스 B ]        |
+-------------------------------------------------------------------------+
```

---

## 본론: 개념 및 핵심 메커니즘

### 1. API(인터페이스)와 Open API의 본질

- **API(Application Programming Interface)**: 구현 내부를 은닉하고, 약속된 표준 규약(Contract)을 통해 애플리케이션 간 기능과 데이터를 안전하게 교환하는 추상화 접점.
- **Open API**: 기업 내부 자원(데이터·기능)을 표준화된 인터페이스(REST, JSON 등)로 외부에 개방하여 제3자 개발자가 혁신적 서비스를 창출하도록 돕는 플랫폼 비즈니스 모델.

### 2. API 접근 범위별 3대 분류

1. **Private API**: 기업 내부 시스템 간 또는 마이크로서비스 간 연계용. 높은 성능과 유연성 중심 (gRPC, 내부 REST).
2. **Partner API**: 비즈니스 협력 관계를 맺은 특정 제휴사에게만 허용. B2B VPN, mTLS 기반 상호 인증.
3. **Public (Open) API**: 불특정 다수 외부 개발자에게 개방. 엄격한 사용자 등록, API Key 발급, 트래픽 쿼터(Quota) 및 과금 체계 필수.

### 3. 현대 API 3대 아키텍처 프로토콜 비교

| 비교 항목 | REST API | gRPC | GraphQL |
|---|---|---|---|
| **기반 프로토콜** | HTTP/1.1 (JSON/XML) | HTTP/2 (Protocol Buffers) | HTTP/1.1, HTTP/2 (JSON) |
| **통신 방식** | 요청-응답 (Request-Response) | 단방향/양방향 스트리밍 지원 | 단방향 쿼리/변이 (Subscription 지원) |
| **성능 및 지연** | 텍스트 기반으로 오버헤드 큼 | 바이너리 직렬화로 **초저지연/고속** | 단일 요청으로 오버페칭 방지 |
| **적용 영역** | 퍼블릭 Open API, 웹 프론트엔드 | 마이크로서비스 내부 통신(IPC) | 복잡한 관계형 UI, 모바일 BFF |
| **표준화 명세** | OpenAPI Specification(Swagger) | `.proto` 파일 명세 | GraphQL Schema (SDL) |

---

## API 게이트웨이 트래픽 제어 및 보안 거버넌스

### 1. 트래픽 제어 메커니즘 (Throttling / Rate Limiting)

- **토큰 버킷(Token Bucket) 알고리즘**:
  - 일정한 주기(초당 $r$개)로 버킷에 토큰을 채우고, 요청마다 토큰을 소비.
  - 버킷이 비어있으면 즉시 HTTP 429(Too Many Requests)를 반환하여 백엔드 보호.
- **Leaky Bucket 알고리즘**:
  - 큐에 요청을 쌓고 일정한 속도로 누출시켜 백엔드로 전달. 버스트 트래픽을 완벽히 평활화(Smoothing).

### 2. API 보안 위협과 방어 (OWASP API Security Top 10)

- **BOLA (Broken Object Level Authorization)**:
  - 공격자가 URI 파라미터의 ID값(`/users/100` -> `/users/101`)을 변조하여 타인 정보를 조회하는 취약점.
  - **대응**: 게이트웨이 및 서비스 레벨에서 토큰의 주체(Subject)와 자원 소유권 매핑을 강제 검증.
- **섀도우 API (Shadow/Zombie API)**:
  - 문서화되지 않거나 구버전이 방치되어 공격 경로로 노출되는 현상.
  - **대응**: CI/CD 파이프라인에서 OpenAPI 명세서(OAS)와 실제 라우팅 경로를 일치시키는 API 거버넌스 자동화.

---

## 실무 장애 시나리오 및 공학적 대안

### 1. 현장 장애 사례

1. **파트너사 무한 루프 호출로 메인 서비스 중단**:
   - 특정 제휴사 배포 오류로 초당 5만 건의 API가 인입되어 전체 DB 커넥션 고갈.
2. **API 스펙 파괴적 변경(Breaking Change)으로 모바일 클라이언트 대규모 먹통**:
   - 하위 호환성 검토 없이 필드명을 수정 배포하여 구버전 모바일 앱 전면 오류 발생.

### 2. 문제 원인 및 공학적 해결책

| 장애 상황 | 근본 원인 | 공학적 대책 (대안 기술) | 개선 효과 |
|---|---|---|---|
| **폭주 트래픽 서비스 다운** | API별 인입 유량 제한 정책 부재 | **API Gateway 분산 토큰 버킷** (Redis 연계) 적용 | 클라이언트별 초당 호출 한도 강제, 서비스 99.99% 가용성 보장 |
| **하위 호환성 파괴** | 버전 관리 정책 부재 및 즉각적 필드 변경 | **URL 경로 버전 관리** (`/api/v1/orders`) + 시맨틱 버저닝 | 최소 6개월 이상 일몰(Deprecation) 유예 및 무중단 전환 |
| **비인가 데이터 유출** | Basic 인증 또는 고정 API Key 탈취 | **OAuth 2.0 PKCE + mTLS** 상호 인증 의무화 | 토큰 위변조 차단 및 금융 마이데이터 법적 보안 요건 충족 |

---

## 결론: 기술사 답안 차별화 포인트

1. **API-First 개발 방법론 제시**: 사후 문서화 관행을 탈피하고, 설계 단계에서 OpenAPI Specification(OAS 3.0)을 단일 진실 공급원(SSOT)으로 삼아 클라이언트-백엔드 목(Mock) 서버 병렬 개발 및 계약 테스트(Pact) 체계를 답안에 강조할 것.
2. **비즈니스적 가치와 공학적 안정성의 균형**: Open API는 개방을 통한 데이터 경제(마이데이터, BaaS) 활성화가 목적이지만, 기술적 무기(API 게이트웨이, Throttling, BOLA 방어)가 전제되지 않으면 시스템 붕괴로 직결된다는 공학적 경각심을 명문화할 것.
