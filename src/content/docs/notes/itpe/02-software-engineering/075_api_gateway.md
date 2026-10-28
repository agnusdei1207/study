---
title: "API Gateway (Application Programming Interface)"
description: "단일 진입점·리버스 프록시, 인증·Rate Limiting·서킷 브레이커, 솔루션 비교, SPOF·Fat Gateway 한계와 방안"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  question_no: "075"
---

## 연관 키워드
- API Gateway, MSA, 단일 진입점, 리버스 프록시, 동적 라우팅, BFF, Rate Limiting, 서킷 브레이커, SPOF, JWT

### Ⅰ. API Gateway의 개요

- 핵심 요약 : 모든 외부 요청을 단일 진입점으로 받아 라우팅과 공통 기능을 일괄 처리하는 리버스 프록시 기반 미들웨어.
- 개념 : 마이크로서비스 아키텍처(MSA, Microservice Architecture)에서 외부 클라이언트의 API(Application Programming Interface) 요청을 단일 진입점(Single Point of Entry)으로 받아 적절한 백엔드 서비스로 전달하고 공통 기능을 처리하는 API 게이트웨이(API Gateway)는 리버스 프록시(Reverse Proxy) 기반 미들웨어임.
- 배경 및 필요성 : 수십에서 수백 개의 마이크로서비스를 클라이언트가 각각 직접 호출하면 호출 경로가 늘고, 인증 처리가 중복되며, 프로토콜이 어긋나고, 내부 엔드포인트가 외부에 노출되는 문제가 생김.
- 대표 솔루션 : Spring Cloud Gateway, Kong, Apigee, AWS(Amazon Web Services) API Gateway, Envoy.
- 주요 목적 : 단일 진입점에서 라우팅과 공통 기능을 일원화하는 것.

### Ⅱ. API Gateway의 특징 및 장점

- 핵심 요약 : 인증, 트래픽 제어, 장애 격리, 동적 라우팅, 프로토콜 변환을 게이트웨이 한 곳에 일원화하는 구조.

1. 인증 및 인가 : JWT(JSON Web Token) 검증과 OAuth 2.0 토큰 처리를 게이트웨이에서 수행 → 백엔드마다 보안 로직을 중복 구현하지 않음.
2. Rate Limiting(단위 시간당 요청 수를 제한하는 트래픽 제어) : 요청 폭주를 입구에서 걸러 백엔드 과부하 방지 → 가용성 보호.
3. 서킷 브레이커(Circuit Breaker) : 실패가 누적된 하위 서비스로의 호출을 차단 → 연쇄 장애(Cascading Failure) 확산 방지.
4. 동적 라우팅 : 서비스 디스커버리와 연동해 인스턴스 주소를 실시간 반영 → 인스턴스가 늘거나 줄어도 경로 설정을 바꿀 필요가 없음.
5. 프로토콜 변환과 캐싱 : REST(Representational State Transfer)와 gRPC 간 변환, 응답 캐싱 → 클라이언트 형식 차이를 흡수하고 응답 지연을 줄임.
6. BFF 패턴(Backend For Frontend) : 웹과 모바일 등 클라이언트별 게이트웨이를 두어 필요한 데이터만 조합해 제공 → 클라이언트별 응답 최적화.

### Ⅲ. API Gateway의 구조 (흐름)

- 핵심 요약 : 클라이언트 요청이 게이트웨이의 공통 기능 계층을 통과한 뒤 사설 네트워크의 백엔드 서비스로 분기되는 흐름.

```text
[ 클라이언트 (Web / Mobile) ]
   ↓
[ API Gateway : 단일 진입점 ]
 1. 인증·인가 (토큰 검증)
 2. 트래픽 제어 (요청 수 제한)
 3. 장애 격리 (서킷 브레이커)
 4. 동적 라우팅 (서비스 디스커버리)
 5. 프로토콜 변환과 응답 캐싱
   ↓
[ 사설 네트워크 내부 서비스 ]
 - 주문 서비스 (Order Service)
 - 결제 서비스 (Payment Service)
```

### Ⅳ. 주요 API Gateway 솔루션의 비교

- 핵심 요약 : 기반 기술과 확장 방식, 적합 환경이 달라 조직의 기술 스택과 운영 주체에 따라 선택이 갈림.

| 비교 항목 | Spring Cloud Gateway | Kong Gateway | AWS API Gateway |
|---|---|---|---|
| 기반 기술 | Java 기반 Netty 리액티브 처리 | Nginx(OpenResty)와 Lua 기반 | AWS가 운영하는 관리형 서비스 |
| 처리 방식 | 리액티브 비동기 처리 | Nginx 기반 고성능 처리 | 클라우드 제공자가 확장을 관리 |
| 확장 방식 | Java 코드로 커스텀 필터 구현 | 플러그인 생태계 활용 | Lambda 연동, 콘솔 기반 구성 |
| 적합 환경 | Spring 생태계의 엔터프라이즈 MSA | 대규모 고성능 트래픽과 다중 언어 환경 | 클라우드 네이티브 서버리스 구조 |

### Ⅴ. API Gateway의 한계와 방안

- 핵심 요약 : 엔드포인트 은닉과 공통 정책 일원화의 이점, 단일 장애점과 Fat Gateway 변질의 한계.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 단일 장애점(SPOF, Single Point of Failure) | 모든 인바운드 트래픽이 한 계층에 집중 → 장애 시 전사 서비스 중단, 추가 홉으로 지연 증가 | 여러 가용 영역에 걸친 액티브-액티브 구성, DNS 기반 GSLB(Global Server Load Balancing) 적용 | 가용성 수준, 응답 지연 |
| Fat Gateway 변질 | 인증과 라우팅을 넘어 비즈니스 데이터 결합 로직이 쌓임 → 유지보수성과 배포 속도 저하 | 인프라 횡단 관심사만 게이트웨이에 두고, 화면 조합은 BFF 계층으로 분리 | 게이트웨이 변경 빈도, 배포 소요 시간 |
| 토큰 검증 병목 | 모든 요청을 중앙 인증 서버가 동기 검증 → 인증 서버 부하 집중 | 공개키 기반 JWT를 게이트웨이에서 로컬 검증하고, 폐기 목록은 Redis 같은 캐시에서 조회 | 인증 지연 시간, 인증 서버 부하율 |

### Ⅵ. 고가용성 API 게이트웨이 구축에 대한 기술사적 제언

- 핵심 요약 : 이중화된 진입 계층과 역할 경계를 함께 관리하여 고가용성 게이트웨이를 상시 운영하는 방향.

1. 게이트웨이는 단일 인스턴스가 아니라 여러 가용 영역에 걸친 이중화 집단으로 운영하고, 앞단에 L4/L7(Layer 4/Layer 7) 로드밸런서를 두는 구성을 기본 설계로 삼음.
2. 게이트웨이 설정과 라우팅 규칙을 코드로 관리하고 변경을 승인 절차로 통제해야 Fat Gateway 변질을 막을 수 있음. 화면 조합 로직은 서비스 팀이 소유하는 BFF 계층에 두어 게이트웨이의 역할 경계를 유지하는 것이 좋음.

### Ⅶ. 결론

- 핵심 요약 : API 게이트웨이는 MSA의 진입점이자 공통 인프라 정책을 집행하는 지점이다.
- 시사점 : 이중화로 가용성을 확보하고 역할 경계로 비대화를 막으며 토큰 검증 구조를 최적화하는 것이 안정적 운영의 기본 조건.
