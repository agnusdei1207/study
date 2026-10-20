---
title: "SOAP(역사적 명칭: Simple Object Access Protocol)"
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

- SOAP(Simple Object Access Protocol), WSDL(Web Services Description Language), UDDI(Universal Description, Discovery and Integration)
- SOAP Envelope, WS-Security, 웹 서비스(Web Services) 3대 표준, WS-I Basic Profile, MTOM, ESB(Enterprise Service Bus), REST(Representational State Transfer)

## Ⅰ. SOAP의 개요

- 핵심 요약 : 이기종 시스템 간 XML 메시지 교환을 위한 W3C 표준의 경량 프로토콜.
- 개념 : 분산 네트워크 환경에서 이기종 시스템 간에 구조화된 정보(XML(Extensible Markup Language) 메시지)를 교환하기 위해 W3C(World Wide Web Consortium)에서 표준화한 XML 기반의 경량 프로토콜(SOAP, Simple Object Access Protocol).
- 배경 및 필요성 : 서로 다른 운영체제, 언어, 미들웨어 환경에서 원격 프로시저 호출(RPC, Remote Procedure Call)을 지원하고, 방화벽을 우회하기 위해 표준 웹 프로토콜인 HTTP(Hypertext Transfer Protocol)를 전송 계층으로 활용.
- 웹 서비스 3대 표준 : SOAP(메시지 전송 프로토콜), WSDL(Web Services Description Language, 서비스 인터페이스 기술 언어), UDDI(Universal Description, Discovery and Integration, 서비스 등록 및 검색 레지스트리).
- 명칭 : Simple Object Access Protocol은 SOAP의 역사적 명칭이며, W3C SOAP 1.2 명세에서는 SOAP을 더 이상 약어로 정의하지 않는 것이 공식 입장. [W3C SOAP 1.2](https://www.w3.org/TR/soap12/)

## Ⅱ. SOAP의 특징

- 핵심 요약 : XML 기반, 전송 프로토콜 독립, WS-* 엔터프라이즈 확장의 프로토콜 체계.

1. XML 기반 구조화 정보 교환의 W3C 표준 프로토콜.
2. HTTP, HTTPS(Hypertext Transfer Protocol Secure), SMTP(Simple Mail Transfer Protocol), JMS(Java Message Service) 등 다중 전송 바인딩의 프로토콜 독립성.
3. 플랫폼·언어 중립의 RPC(Remote Procedure Call) 지원.
4. WS-Security, WS-AtomicTransaction 등 엔터프라이즈 표준(WS-*) 확장.
5. 웹 서비스 3대 표준(SOAP, WSDL, UDDI)과의 긴밀 연계.

## Ⅲ. SOAP의 구조 (흐름)

- 핵심 요약 : UDDI 검색과 WSDL 바인딩을 거쳐 Envelope 형식의 SOAP 메시지를 교환하는 구조.
- 웹 서비스 아키텍처에서의 SOAP 역할.

```text
[ 웹 서비스 아키텍처 ]
[ Service Requester ]
   │ (1) WSDL 검색
   ▼
[ UDDI Registry ]
   │ (2) WSDL 기반 바인딩
   ▼
[ Service Provider ]
   ▲
   │ (3) SOAP Envelope 전송
```

- SOAP 메시지(Envelope)의 내부 구조.

```text
[ SOAP Envelope 구조 ]
<Envelope> : 최상위 루트 엘리먼트 (필수)
   ├─ <Header> : WS-Security, 트랜잭션 등
   │            부가 정보 (선택)
   ├─ <Body>   : 호출 메서드·매개변수 (필수)
   └─ <Fault>  : 오류 상세 예외 정보
```

- SOAP Envelope (봉투) : XML 문서가 SOAP 메시지임을 선언하는 최상위 루트 엘리먼트.
- SOAP Header (헤더) : 인증, 암호화, 라우팅, 트랜잭션 등 비기능적 부가 정보를 담는 선택 영역.
- SOAP Body (본문) : 실제 전송하고자 하는 비즈니스 데이터 및 RPC 호출 페이로드를 담는 필수 영역.
- SOAP Fault (오류) : 요청 처리 실패 시 상세 오류 코드, 원인, 액터를 표준화된 포맷으로 반환.

## Ⅳ. SOAP과 RESTful 웹 서비스의 비교

- 핵심 요약 : 엄격한 프로토콜 규약과 경량 아키텍처 스타일의 목적·환경 차이.

| 비교 항목 | SOAP | REST(Representational State Transfer) |
|---|---|---|
| 프로토콜 성격 | 독립적인 엄격한 통신 프로토콜 규약 | HTTP 표준을 활용하는 아키텍처 스타일 |
| 메시지 포맷 | 오직 XML만 지원 (WSDL 엄격한 스키마) | JSON(JavaScript Object Notation), XML, YAML(YAML Ain't Markup Language), HTML(HyperText Markup Language) 등 다변화 (주로 JSON) |
| 전송 프로토콜 | HTTP, HTTPS, SMTP, JMS 등 다중 바인딩 | 주로 HTTP, HTTPS에 강하게 결합 |
| 보안 및 표준 | WS-Security, WS-AtomicTransaction 등 엔터프라이즈 표준 | HTTPS 전송 암호화, JWT(JSON Web Token), OAuth(Open Authorization) 2.0 |
| 오버헤드 및 성능 | 무거운 XML 파싱과 큰 메시지 크기로 성능 낮음 | 경량 JSON 직렬화로 빠르고 모바일/웹에 최적 |
| 주 활용 분야 | 은행, 증권, 정부 행정전산망 등 고신뢰 금융/공공 연계 | 대규모 B2C(Business-to-Consumer) 포털, 모바일 앱, 마이크로서비스(MSA, Microservice Architecture) |

## Ⅴ. SOAP의 장점과 한계

- 핵심 요약 : 메시지 레벨 보안과 엄격한 계약의 장점, XML 비대함·WS-* 복잡성·모던 환경 부적합의 한계.
- 장점
  1. WS-Security 기반 메시지 레벨 암호화(XML-Encryption)와 전자서명(XML-Signature).
  2. WSDL 엄격한 스키마 계약에 따른 높은 신뢰성.
  3. 다중 전송 프로토콜 바인딩의 유연성.
  4. WS-AtomicTransaction 등 트랜잭션 표준 지원.
- 한계점 1 : XML 페이로드의 비대함으로 인한 네트워크 오버헤드 및 파싱 지연
  - 한계점 : SOAP Envelope, Header, Body 구조와 XML 네임스페이스 선언의 극심한 장황성(Verbosity)으로 인해 직렬화/역직렬화 CPU(Central Processing Unit) 부하가 크고 대역폭 낭비 발생.
  - 해결 방안 : 고빈도·대용량 트랜잭션 구간은 경량 REST/JSON 또는 바이너리 기반 gRPC/Protobuf로 전환하고, 기존 SOAP 서비스 유지 시 MTOM(Message Transmission Optimization Mechanism)을 통한 첨부파일 바이너리 최적화.
- 한계점 2 : 복잡한 WS-* 표준 규격으로 인한 벤더 종속성 및 상호운용성 저하
  - 한계점 : WS-Security, WS-ReliableMessaging 등 방대한 스펙이 라이브러리와 프레임워크 벤더마다 구현 차이를 보여 이기종 시스템 간 연동 시 런타임 파싱 오류 빈발.
  - 해결 방안 : 상호운용성을 보장하는 WS-I(Web Services Interoperability) Basic Profile 규격을 엄격히 준수하고, 엔터프라이즈 서비스 버스(ESB, Enterprise Service Bus)나 API(Application Programming Interface) Gateway를 중간에 두어 프로토콜 변환(Mediation) 및 메시지 정규화 수행.
- 한계점 3 : 모바일 및 모던 웹 브라우저 환경과의 직접 통합 불가
  - 한계점 : 브라우저 JavaScript 환경에서 복잡한 WSDL 파싱과 XML SOAP 클라이언트 스텁 생성이 비효율적이어서 SPA(Single-Page Application)나 모바일 앱과의 직접 연계 난제.
  - 해결 방안 : 프론트엔드와 레거시 SOAP 백엔드 사이에 RESTful API Gateway 또는 BFF(Backend For Frontend) 계층을 배치하여 SOAP 메시지를 JSON으로 변환 중계하는 Facade 패턴 적용.

## Ⅵ. 엔터프라이즈 시스템 연계 시 기술사적 제언

- 핵심 요약 : SOAP-to-REST 어댑터 점진적 현대화, WS-Security 정밀 구성, MTOM 경량화 병행의 3대 제언.
- 레거시 연계(EAI(Enterprise Application Integration)/ESB)와 신규 MSA 간의 어댑터 전략 : 금융권 레거시 코어뱅킹의 핵심 트랜잭션은 여전히 SOAP 기반의 엄격한 트랜잭션 정합성을 요구하므로, 전면 폐기 대신 API Gateway나 ESB 레이어에서 SOAP-to-REST 변환 어댑터를 두는 점진적 현대화 추진.
- WS-Security의 정밀한 구성 : SOAP 환경에서는 메시지 레벨 암호화(XML-Encryption)와 전자서명(XML-Signature)을 지원하는 WS-Security를 종단 간(End-to-End) 구간에 명확히 적용하여 중간자 공격 방어.
- 대용량 첨부파일 구간의 MTOM(Message Transmission Optimization Mechanism) 활성화 : XML 첨부파일의 바이너리 최적화 전송으로 오버헤드 완화 필요.

## Ⅶ. 결론

- 핵심 요약 : SOAP은 고신뢰 엔터프라이즈 연계의 표준으로, 어댑터 기반 점진적 현대화가 현실적 전략.
- 요약 : XML 기반 엄격한 계약과 WS-Security로 금융·공공 연계의 신뢰성을 담보하는 프로토콜.
- 시사점 : 경량 REST/gRPC 전환과 병행한 API Gateway·ESB 기반 어댑터 전략 및 WS-I 규격 준수 필요.
