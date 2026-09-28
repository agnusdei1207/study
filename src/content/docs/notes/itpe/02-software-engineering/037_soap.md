---
title: "SOAP"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 구현·객체지향·API → **SOAP**

## 30초 인출

- 본질: 분산 이기종 환경에서 구조화된 정보(XML)를 안전하고 신뢰성 있게 교환하기 위해 W3C가 표준화한 엄격한 메시지 기반 통신 규약
- 메커니즘: Envelope(루트) + Header(선택적 메타데이터/보안) + Body(필수 요청·응답 데이터) + Fault(표준 에러) 구조 및 WSDL 기반 인터페이스 사전 계약
- 통찰: 무거운 XML 페이로드와 복잡한 WS-* 표준으로 인해 성능 저하가 발생하므로 경량 웹 서비스는 REST/gRPC로 전환하되 고신뢰 금융·공공 트랜잭션 영역에 선별 적용 필요

<details>
<summary>핵심 용어</summary>

- **SOAP(Simple Object Access Protocol)** : 분산 환경에서 XML 기반으로 정보를 교환하기 위한 W3C 표준 프로토콜 규격
- **WSDL(Web Services Description Language)** : 웹 서비스의 위치(Endpoint), 제공 오퍼레이션, 파라미터 타입을 XML로 정밀 기술한 기계 판독형 계약 문서
- **UDDI(Universal Description, Discovery, and Integration)** : 전 세계 비즈니스 웹 서비스를 등록하고 동적으로 검색할 수 있는 디렉터리 표준
- **SOAP Envelope** : XML 문서의 루트 엘리먼트로서 메시지의 시작과 끝, 네임스페이스를 선언하는 필수 컨테이너
- **SOAP Fault** : 서비스 처리 중 발생한 예외 상황(코드, 액터, 상세 사유)을 표준화된 규격으로 클라이언트에 전달하는 에러 엘리먼트
- **WS-Security** : 메시지 전송 구간뿐만 아니라 메시지 페이로드 자체에 대한 전자서명, 암호화, SAML 토큰 인증을 제공하는 보안 표준

</details>

---

## 2~4교시 예상문제 (25점)

> SOAP의 목적과 메시지 구조를 설명하고, WSDL을 통한 서비스 계약 정의 및 REST와 비교한 적용 고려사항을 제시하시오. (25점, 예상)

---

## 2~4교시 25점 답안

## Ⅰ. SOAP의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 분산 네트워크 환경에서 이기종 시스템 간에 구조화된 XML 데이터를 안전하게 교환하기 위해 W3C에서 제정한 엄격한 표준 메시징 프로토콜 |
| 목적 | 플랫폼 및 프로그래밍 언어의 독립성 보장, WSDL 기반의 강력한 타입 계약 준수 및 엔터프라이즈급 신뢰성·트랜잭션(WS-*) 지원 |

## Ⅱ. SOAP의 핵심 특징

| 특징 | 의미 |
|---|---|
| 엄격한 계약 기반 | WSDL(XML 스키마)을 통해 서비스 인터페이스를 사전 정의하여 클라이언트와 서버 간 컴파일 타임 타입 검증 보장 |
| 프로토콜 독립성 | 기본 HTTP 외에도 SMTP, TCP, JMS 등 다양한 하위 전송 계층 프로토콜 바인딩 지원 |
| 메시지 수준 보안 | WS-Security 표준을 통해 중간 프록시를 거치더라도 종단간(E2E) 페이로드 암호화 및 서명 유지 |
| 표준화된 예외 처리 | SOAP Fault 규격을 내재화하여 클라이언트에 일관된 에러 코드(Code, Reason, Detail) 반환 |

## Ⅲ. SOAP 웹 서비스 체계 및 메시지 구조

### 웹 서비스 3대 축(SOAP/WSDL/UDDI) 및 Envelope 메시지 아키텍처

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [UDDI 서비스 레지스트리]                         │
│                     - 웹 서비스 등록(Publish) 및 탐색(Find)            │
└───────────────────────▲────────────────────────▲───────────────────────┘
     1. WSDL 등록       │                        │ 2. 서비스 검색
     (Publish)          │                        │ (Find)
┌───────────────────────┴────────┐      ┌────────┴───────────────────────┐
│     [서비스 제공자 (Server)]    │      │     [서비스 요청자 (Client)]    │
│  - 비즈니스 오퍼레이션 실행    │      │  - WSDL 기반 스텁(Stub) 생성   │
└────────────────────────────────┘      └────────────────────────────────┘
                 ▲                                       │
                 │ 3. SOAP 요청 (Envelope/Body)          │
                 │ 4. SOAP 응답 (Envelope/Body or Fault) │
                 └───────────────────────────────────────┘
                                     │
                                     ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   [SOAP 1.2 표준 메시지 내부 구조]                     │
│                                                                        │
│  <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">  │
│    │                                                                   │
│    ├─ <soap:Header> (선택적) ──────────────────────────────────────┐  │
│    │    ├─ wsse:Security (인증 토큰, 전자서명, 암호화 블록)         │  │
│    │    └─ wsa:Action / wsa:MessageID (라우팅 및 메시지 상관 ID)    │  │
│    │                                                               │  │
│    └─ <soap:Body> (필수 요소) ─────────────────────────────────────┤  │
│         ├─ [정상 응답: 비즈니스 페이로드]                          │  │
│         │    └─ <m:GetAccountBalanceResponse> ... </m:...>         │  │
│         │                                                          │  │
│         └─ [오류 발생 시: <soap:Fault>]                            │  │
│              ├─ <soap:Code> : Sender / Receiver 등 표준 오류 코드  │  │
│              ├─ <soap:Reason> : 사람이 읽을 수 있는 오류 설명      │  │
│              └─ <soap:Detail> : 애플리케이션 특화 상세 디버그 정보 │  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### SOAP 메시지 핵심 구성요소

| 엘리먼트 | 필수 여부 | 주요 역할 및 상세 기능 |
|---|---|---|
| **Envelope** | **필수 (Mandatory)** | XML 문서의 루트 요소로 해당 XML이 SOAP 메시지임을 선언하고 네임스페이스 정의 |
| **Header** | 선택 (Optional) | 인증 자격 증명(WS-Security), 트랜잭션 ID(WS-Coordination), 라우팅 정보 등 횡단 관심사 전달 |
| **Body** | **필수 (Mandatory)** | 실제 주고받는 핵심 비즈니스 데이터(XML 엘리먼트) 또는 처리 실패 시 Fault 요소 포함 |
| **Fault** | 조건부 (오류 시) | Body 내부에 위치하며 오류 발생 시 원인, 코드, 발생 주체(Role/Node), 세부 정보를 표준화하여 반환 |

## Ⅳ. SOAP vs REST 비교 및 적용 고려사항

### SOAP 프로토콜과 REST 아키텍처 스타일 비교

| 비교 항목 | SOAP (Simple Object Access Protocol) | REST (Representational State Transfer) |
|---|---|---|
| **아키텍처 본질** | **엄격한 표준 통신 규약 (Protocol)** | **웹 표준 기반의 유연한 아키텍처 스타일 (Style)** |
| **데이터 포맷** | 오직 **XML 포맷** 만 지원 (구조적 엄격성) | **JSON**, XML, YAML, 텍스트 등 다양한 포맷 지원 |
| **인터페이스 계약** | **WSDL** 기반의 명확하고 정적인 기계 판독형 계약 | **OpenAPI(Swagger)** 명세 또는 자원 URI 중심 설계 |
| **전송 프로토콜** | HTTP, HTTPS, SMTP, TCP, JMS 등 다양 | 주로 **HTTP / HTTPS** 표준 프로토콜 활용 |
| **보안 메커니즘** | **WS-Security** (메시지 수준 암호화 및 무결성) | **HTTPS/TLS** (전송 계층 암호화), OAuth 2.0 |
| **네트워크 오버헤드** | XML 태그 및 봉투 구조로 인해 페이로드가 무거움 | 경량 JSON 지원으로 데이터 크기가 작고 파싱 빠름 |
| **주 활용 분야** | 금융 결제망, 은행 간 연계, 공공 행정망, 레거시 ERP | 모바일 앱 백엔드, MSA 서비스 연계, 오픈 퍼블릭 API |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| XML 페이로드의 크기 비대화 및 직렬화/역직렬화 연산으로 인한 CPU 오버헤드 | 대용량 바이너리 전송 시 MTOM(Message Transmission Optimization Mechanism) 압축 바인딩 적용 |
| WSDL의 복잡성 및 클라이언트 코드 생성 도구 종속성으로 개발 민첩성 저하 | 신규 외부 연동 시스템은 REST/OpenAPI로 표준화하고 내부 코어 영역에만 SOAP 국소 유지 |
| 복잡한 WS-* 보안 표준 설정 오류로 인한 인증 실패 및 상호운용성 장애 | 상용 API Gateway의 SOAP ↔ REST 변환 엔진을 도입하여 보안 검증 및 프로토콜 변환 일원화 |

## Ⅵ. 제언

레거시 SOAP 서비스의 현대화를 위한 API Gateway 기반 SOAP-to-REST 트랜스포메이션 파이프라인

### API Gateway 기반 SOAP 현대화 아키텍처

```text
[현대적 모바일 / 웹 클라이언트]
       │
       ▼ (경량 HTTPS / JSON REST 요청)
┌────────────────────────────────────────────────────────────────────────┐
│ API Gateway 계층 (Kong / Apigee / AWS API Gateway)                     │
│                                                                        │
│  [1. 클라이언트 JSON 요청 수신]                                       │
│        ↓                                                               │
│  [2. XSLT / 템플릿 변환 엔진]                                         │
│        ├─ JSON 페이로드를 SOAP XML Body로 변환                         │
│        ├─ WS-Security 전자서명 및 인증 헤더 자동 주입                 │
│        └─ SOAP 1.2 Envelope 패키징                                     │
│        ↓                                                               │
│  [3. 백엔드 레거시 SOAP 서버로 전송 (HTTP POST)]                      │
│                                                                        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼ (SOAP XML 요청)
┌────────────────────────────────────────────────────────────────────────┐
│ [레거시 코어뱅킹 / ERP 시스템] (WSDL 기반 SOAP 서비스 무수정 유지)     │
└────────────────────────────────────────────────────────────────────────┘
```

### 웹 서비스 프로토콜 선정 의사결정 체계

```text
시스템 연계 요구사항 분석
       ↓
[엔터프라이즈급 메시지 수준 암호화(WS-Security)나 복합 트랜잭션이 필수인가?]
       ├─ 예 ──→ SOAP 채택 (WSDL 계약 기반 안전성 확보)
       └─ 아니오 ─→ [대용량 스트리밍 및 초저지연 내부 마이크로서비스인가?]
                         ├─ 예 ──→ gRPC / HTTP/2 채택
                         └─ 아니오 ─→ REST / JSON 채택 (개발 생산성 및 웹 표준화)
```

### 선택 근거: 직접 연동과 API Gateway 변환 연계 비교

| 구분 | 레거시 SOAP 직접 클라이언트 연동 | 제언: API Gateway 기반 REST 변환 |
|---|---|---|
| 클라이언트 부담 | 모바일 기기에서 무거운 XML 파서 라이브러리 탑재 | 경량 JSON 기본 내장 파서 활용으로 모바일 부하 제거 |
| 레거시 수정 여부 | 레거시 시스템을 REST로 전면 재개발 필요 (막대한 비용) | 레거시 코드는 일체 수정 없이 Gateway 설정만으로 즉시 개방 |
| 보안 통제 | 서비스별 개별 WS-Security 설정으로 관리 복잡도 가중 | API Gateway에서 OAuth 2.0과 WSS 상호 변환 중앙 통제 |

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 4교시: 개방형 API 문항 중 SOAP 및 REST 구성요소
- W3C SOAP Version 1.2 Part 1: Messaging Framework (W3C Recommendation)
- W3C Web Services Description Language (WSDL) 1.1 / 2.0
- OASIS Web Services Security: SOAP Message Security 1.1

## 연결 토픽

- 이전 토픽: [McCabe 순환복잡도](./036_mccabe_cyclomatic_complexity.md)
- 연관 토픽: [REST](./015_rest.md), [Open API](./022_open_api.md)
- 다음 토픽: [개발방법론 테일러링](./039_methodology_tailoring.md)
