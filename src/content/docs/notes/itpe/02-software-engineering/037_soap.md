---
title: "SOAP(Simple Object Access Protocol)"
description: "W3C 표준 XML 프로토콜, 웹 서비스 3대 표준, REST 비교, WS-* 복잡성 한계와 어댑터 제언"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드

- SOAP(Simple Object Access Protocol), WSDL(Web Services Description Language), UDDI(Universal Description, Discovery and Integration)
- SOAP Envelope, WS-Security, 웹 서비스(Web Services) 3대 표준, WS-I Basic Profile, MTOM, ESB(Enterprise Service Bus), REST(Representational State Transfer)

## Ⅰ. SOAP의 개요

- 핵심 요약 : 이기종 시스템 간 XML 메시지 교환을 위해 W3C(World Wide Web Consortium)가 표준화한 XML 기반 프로토콜.
- 개념 : 분산 환경에서 이기종 시스템끼리 구조화된 정보를 교환하도록 XML(Extensible Markup Language) 메시지 형식을 정의한 프로토콜(**SOAP**, 역사적으로 Simple Object Access Protocol로 불림).
- 배경 및 필요성 : 운영체제, 언어, 미들웨어가 서로 다른 환경에서 **원격 프로시저 호출** (RPC, Remote Procedure Call)을 지원해야 하고, 방화벽 통과를 위해 표준 웹 프로토콜인 HTTP(Hypertext Transfer Protocol)를 전송 수단으로 활용할 필요가 있음.
- 주요 목적 : 플랫폼과 언어에 상관없는 서비스 호출과 엔터프라이즈 수준의 보안·트랜잭션 확장 제공.
- 웹 서비스 3대 표준 :
  1. **WSDL** (Web Services Description Language, 서비스 인터페이스 기술 언어).
  2. **UDDI** (Universal Description, Discovery and Integration, 서비스 등록·검색 레지스트리).
  3. SOAP (메시지 전송 프로토콜).
- 명칭 : Simple Object Access Protocol은 역사적 명칭이며, W3C SOAP 1.2 명세에서는 SOAP을 더 이상 약어로 정의하지 않음([W3C SOAP 1.2](https://www.w3.org/TR/soap12/)).

## Ⅱ. SOAP의 특징 및 장점

- 핵심 요약 : XML 기반, 전송 프로토콜 독립성, WS-* 엔터프라이즈 확장으로 이루어진 프로토콜 체계.

1. XML 기반 구조화 : 메시지 형식을 XML 스키마로 엄격히 정의 → 송수신 측의 해석 차이 최소화.
2. 전송 프로토콜 독립성 : HTTP, HTTPS(Hypertext Transfer Protocol Secure), SMTP(Simple Mail Transfer Protocol), JMS(Java Message Service) 등 다양한 바인딩 지원 → 환경에 맞는 전송 수단 선택 가능.
3. 플랫폼·언어 중립 RPC : 서로 다른 기술 스택 간 메서드 호출을 표준 형식으로 수행 → 이기종 연계 비용 절감.
4. **WS-Security** 등 WS-* 확장 : 메시지 보안, 트랜잭션 등 엔터프라이즈 요구를 표준 규격으로 보완 → 기업 간 신뢰 연계 기반 확보.
5. 웹 서비스 3대 표준과의 연계 : WSDL로 계약을 정의하고 UDDI로 검색하는 전 과정을 한 체계로 운영 → 서비스 자동 연동 기반 마련.

## Ⅲ. SOAP의 구조 (흐름)

- 핵심 요약 : UDDI 검색과 WSDL 바인딩을 거쳐 Envelope 형식의 SOAP 메시지를 교환하는 구조.
- **SOAP Envelope** (봉투) : XML 문서가 SOAP 메시지임을 선언하는 최상위 루트 엘리먼트.
- **SOAP Header** (헤더) : 인증, 암호화, 라우팅, 트랜잭션 등 비기능적 부가 정보를 담는 선택 영역.
- **SOAP Body** (본문) : 실제 비즈니스 데이터와 RPC 호출 정보를 담는 필수 영역.
- **SOAP Fault** (오류) : 요청 처리 실패 시 오류 코드, 원인, 발생 지점을 표준 포맷으로 반환.

```text
[ 웹 서비스 아키텍처 ]

[ 서비스 요청자 (Service Requester) ]
   ↓ (1) WSDL 검색
[ UDDI 레지스트리 ]
   ↓ (2) WSDL 기반 바인딩
[ 서비스 제공자 (Service Provider) ]
   ↕ (3) SOAP 메시지 교환
```

```text
[ SOAP Envelope 구조 ]

Envelope (최상위 루트, 필수)
  - Header : 인증·트랜잭션 등 부가 정보 (선택)
  - Body : 호출 메서드와 매개변수 (필수)
  - Fault : 오류 상세 정보 (오류 발생 시)
```

## Ⅳ. SOAP과 RESTful 웹 서비스의 비교

- 핵심 요약 : 엄격한 프로토콜 규약을 따르는 SOAP과 HTTP 자원을 중심에 둔 경량 아키텍처 스타일 REST의 목적과 환경이 다름.

| 비교 항목 | SOAP | REST(Representational State Transfer) |
| --- | --- | --- |
| 프로토콜 성격 | 독립적인 엄격한 통신 프로토콜 규약 | HTTP 표준을 활용하는 아키텍처 스타일 |
| 메시지 포맷 | XML만 지원 (WSDL로 엄격한 스키마 정의) | JSON, XML 등 다양하며 주로 JSON 사용 |
| 전송 프로토콜 | HTTP, HTTPS, SMTP, JMS 등 다중 바인딩 | 주로 HTTP, HTTPS에 결합 |
| 보안 및 표준 | WS-Security, WS-AtomicTransaction 등 엔터프라이즈 표준 | HTTPS 전송 암호화, JWT(JSON Web Token), OAuth(Open Authorization) 2.0 |
| 오버헤드 및 성능 | XML 파싱과 큰 메시지 크기로 상대적으로 무거움 | JSON 기반으로 가볍고 웹·모바일 환경에 적합 |
| 주 활용 분야 | 은행, 증권, 공공 기관 간 고신뢰 연계 | 대규모 B2C(Business-to-Consumer) 포털, 모바일 앱, 마이크로서비스(MSA, Microservice Architecture) |

## Ⅴ. SOAP의 한계와 방안

- 핵심 요약 : 메시지 수준 보안과 엄격한 계약이라는 장점이 있으나, XML 장황성과 WS-* 복잡성, 최신 클라이언트와의 불일치가 한계.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| XML 메시지의 장황성 | Envelope, Header, Body 구조와 네임스페이스 선언이 길어 직렬화·역직렬화 CPU 부하와 대역폭 낭비 발생 | 고빈도·대용량 구간은 경량 REST/JSON 또는 gRPC(Protobuf)로 전환하고, 유지되는 SOAP 구간은 **MTOM** (Message Transmission Optimization Mechanism)으로 첨부파일을 바이너리 최적화 | 구간별 응답 시간, 메시지 크기 |
| WS-* 규격의 복잡성과 벤더 종속 | 방대한 WS-* 스펙을 벤더마다 다르게 구현해 이기종 연동 시 파싱 오류가 빈발 | WS-I(Web Services Interoperability) Basic Profile을 준수하고, ESB(Enterprise Service Bus)나 API(Application Programming Interface) Gateway에서 프로토콜 변환과 메시지 정규화 수행 | 연동 오류율 |
| 브라우저·모바일 직접 연동 불가 | 브라우저 JavaScript에서 WSDL 파싱과 XML 클라이언트 스텁 생성이 비효율적이라 SPA(Single-Page Application)나 모바일 앱과 직접 연계가 어려움 | 프론트엔드와 SOAP 백엔드 사이에 BFF(Backend For Frontend) 계층을 두고 SOAP 메시지를 JSON으로 변환하는 퍼사드(Facade) 패턴 적용 | 변환 계층 지연 시간 |

## Ⅵ. 엔터프라이즈 시스템 연계 시 기술사적 제언

- 핵심 요약 : 기존 SOAP 자산은 전면 교체 대신 어댑터로 점진 현대화하고, 보안과 서비스 포트폴리오를 체계적으로 관리하는 것이 필요.
- 레거시 연계 어댑터 전략 : 금융권 코어 시스템의 핵심 트랜잭션은 SOAP 기반의 정합성을 유지하는 경우가 많으므로, EAI(Enterprise Application Integration)나 ESB 계층에 SOAP-to-REST 변환 어댑터를 두고 단계적으로 현대화하는 것이 현실적이다.
- WS-Security의 정밀한 구성 : 메시지 수준의 암호화와 전자서명을 종단 간 구간에 명확히 적용해, 중간 노드를 거치는 동안의 위·변조와 도청을 막아야 한다.
- 서비스 포트폴리오 관리 : 신규 서비스는 REST나 gRPC로 설계하고, 기존 SOAP 서비스는 목록과 의존 관계를 관리하여 전환 우선순위를 정하는 체계를 갖춰야 한다.

## Ⅶ. 결론

- 핵심 요약 : SOAP은 고신뢰 엔터프라이즈 연계의 표준 프로토콜이며, 어댑터 기반 점진적 현대화가 현실적인 전략.
- 시사점 : 경량 REST·gRPC 전환과 API Gateway·ESB 기반 어댑터를 병행하는 방식이 기존 자산의 가치를 지키면서 전환 비용을 낮추는 길임.