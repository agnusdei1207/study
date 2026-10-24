---
title: "Open API(API 일반) (API: Application Programming Interface)"
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

- Open API, API Gateway, Developer Portal, APIM(API Management), API 수익화(Monetization)
- REST API, GraphQL, gRPC, OpenAPI Specification(OAS), OWASP API Security Top 10, Rate Limiting

## Ⅰ. Open API의 개요

- 핵심 요약 : 기업이나 기관의 데이터와 기능을 표준 인터페이스로 외부 개발자에게 개방하는 공개 프로그래밍 인터페이스.
- 개념 : 기업이나 기관이 보유한 데이터, 비즈니스 로직, 플랫폼 기능을 표준 규격(REST(Representational State Transfer), JSON(JavaScript Object Notation) 등)으로 외부 서드파티 개발자에게 개방하는 공개 프로그래밍 인터페이스 (**API**, Application Programming Interface).
- 배경 및 필요성 : 플랫폼 생태계 확장, 마이데이터와 핀테크 같은 개방형 서비스 확산, 내부 데이터의 수익화와 파트너십 확대 요구가 커짐.
- 주요 목적 : 네트워크 효과 창출, 파트너 개발 리드타임 단축, 개방형 혁신(Open Innovation) 촉진.

## Ⅱ. Open API의 특징 및 장점

- 핵심 요약 : 표준 인터페이스의 개방이 네트워크 효과와 생태계 기반 수익화로 이어지는 구조.

1. 표준화된 인터페이스 : REST, JSON 등 범용 웹 표준으로 개방 → 개발자가 익숙한 방식으로 바로 연동.
2. 네트워크 효과 : 참여 개발자와 연동 서비스가 늘수록 플랫폼 가치가 상승 → 생태계가 스스로 커짐.
3. 수익화 (Monetization) : 사용량 기반 과금 모델로 데이터와 기능을 매출로 전환 → 신규 수익원 확보.
4. 개방형 혁신 : 서드파티 개발자와 협업해 신규 서비스를 만듦 → 자체 개발 범위를 넘는 기능 확장.
5. 개발 리드타임 단축 : SDK, 샌드박스, 명세서를 제공 → 파트너의 연동 기간 단축.

## Ⅲ. Open API의 구조 (흐름)

- 핵심 요약 : 개발자 창구, API 게이트웨이, 내부 백엔드로 나뉘는 3계층 생태계 구조.

```text
[ Open API 3계층 구조 ]

외부 앱 / 파트너
          ↓ ① API 호출
API Gateway (인증, 호출 제한, 라우팅)
          ↓ ② 백엔드 전달
내부 백엔드 서비스

Developer Portal (개발자 창구)
  명세 공개, API 키 발급, SDK 제공
```

```text
[ API Gateway 요청 처리 순서 ]

클라이언트 요청
          ↓ 인증·인가 (OAuth 2.0, 토큰 검증)
          ↓ 호출 제한 (Rate Limiting)
          ↓ 라우팅과 종단 암호화
          ↓ 캐싱과 로깅
백엔드 서비스 → 응답
```

- Developer Portal : 명세(OpenAPI Specification, OAS)를 확인하고 샌드박스에서 테스트하며 API 키를 발급받고 사용량을 보는 개발자 창구.
- **API Gateway** : 모든 외부 요청의 진입점으로서 인증·인가, 호출 제한, 라우팅, 로깅을 일괄 수행.
- **API Management** (APIM) : 기획, 발행, 버전 관리, 폐기까지의 수명주기와 과금 모델을 관리.

## Ⅳ. 주요 API 프로토콜의 비교

- 핵심 요약 : REST는 범용 개방, GraphQL은 클라이언트 주도 조회, gRPC는 내부 고성능 통신에 적합.

| 비교 항목 | REST API | GraphQL | gRPC |
| --- | --- | --- | --- |
| 프로토콜 | HTTP/1.1, HTTP/2 | HTTP 기반 단일 엔드포인트 | HTTP/2 기반 바이너리 전송 |
| 데이터 포맷 | JSON, XML | JSON | Protocol Buffers |
| 데이터 요청 방식 | 엔드포인트별 고정 응답, 불필요 필드 수신 가능 | 클라이언트가 필요한 필드만 쿼리로 요청 | 고정 스키마의 바이너리 직렬화 |
| 주 활용 분야 | 범용 퍼블릭 Open API, 모바일 백엔드 | 모바일 화면의 데이터 조합 | 마이크로서비스 내부 통신, 스트리밍 |

## Ⅴ. Open API의 한계와 방안

- 핵심 요약 : 트래픽 남용, 하위 호환성 파손, 인가 취약점이 개방형 API의 대표 한계이며, 게이트웨이 통제와 버전 정책, 객체 단위 인가로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 트래픽 남용과 DoS | 비정상 대용량 호출, 무단 스크래핑으로 백엔드 고갈 | API Gateway 전진 배치, 계정별 Rate Limiting 적용, WAF(Web Application Firewall) 연계 | 호출 제한 발동 건수, 응답 지연 |
| 하위 호환성 파손 | 파라미터 삭제나 응답 구조 변경으로 외부 클라이언트 오류 집단 발생 | 경로 또는 헤더 기반 버전 관리, 구버전의 비권장(Deprecated) 처리와 유예 기간 부여 | 구버전 호출 비율 |
| 객체 수준 인가 취약점 | API 키 유출과 리소스 ID 변조로 타인 데이터 접근 (BOLA, IDOR) | OAuth 2.0 기반 단기 토큰 사용, 호출자와 리소스 소유권을 교차 검증 | 인가 실패 로그, 키 노출 탐지 건수 |

## Ⅵ. Open API 보안과 거버넌스에 대한 기술사적 제언

- 핵심 요약 : 개방 범위에 맞춘 보안 통제와, 명세 중심의 생애주기 관리를 조직 차원에서 수립.

1. 보안 기준의 체계화 : OWASP(Open Worldwide Application Security Project) API Security Top 10을 점검 기준으로 삼아, 객체 수준 인가 검증을 게이트웨이와 백엔드에 함께 두고 보안 점검을 배포 절차에 넣는다.
2. 버전 정책의 공지 체계 : 주 버전 번호로 호환성 단위를 나누고, 폐기 일정을 개발자 포털에 미리 공지해 파트너가 전환할 시간을 확보한다.
3. 공개 범위에 따른 프로토콜 선택 : 외부 공개 영역은 REST를, 내부 고성능 통신은 gRPC를 쓰는 식으로 목적별 기준을 문서화한다.

## Ⅶ. 결론

- 핵심 요약 : Open API는 보안, 호환성, 거버넌스를 갖춘 상태에서 개방할 때 생태계 가치가 커지는 기술.
- 시사점 : 게이트웨이의 호출 통제와 버전 정책, 객체 수준 인가를 함께 갖출 때 안전한 개방형 플랫폼 운영이 가능.
