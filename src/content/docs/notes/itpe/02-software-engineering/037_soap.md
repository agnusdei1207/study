---
title: "SOAP"
author: "Antigravity"
date: "2026-09-20T13:20:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
    variant: "tip"
extra:
  model: "Antigravity"

---

## 답안 골격 (10점 / 25점)

```text
[SOAP] ◀━━ 머리: Ⅶ 공학적 제언 (레거시 금융 결제망 어댑터 격리와 대외 서비스의 REST/JSON 전환 아키텍처)
 ┃
 ┣━ Ⅰ 개요 ───── 이기종 분산 환경 원격 프로시저 호출(RPC), W3C 표준 XML 기반 정형화된 메시징 프로토콜
 ┣━ Ⅱ 웹서비스 3대 축 ─ SOAP(메시지 전송 규약) · WSDL(서비스 인터페이스 기술) · UDDI(서비스 등록/탐색)
 ┣━ Ⅲ 메시지 구조 ─ SOAP Envelope(루트 컨테이너) · Header(WS-* 메타데이터) · Body(실제 페이로드) · Fault(오류 정보)
 ┣━ Ⅳ 엔터프라이즈 WS-* ─ WS-Security(전자서명/암호화) · WS-ReliableMessaging(신뢰 전송) · WS-AtomicTransaction
 ┣━ Ⅴ 비교 ───── SOAP(엄격한 프로토콜, XML) vs REST(경량 스타일, JSON) vs gRPC(HTTP/2, 바이너리)
 ┣━ Ⅵ 실무 문제 ─ 무거운 XML 파싱 CPU 부하 / 모바일·웹 프론트엔드 연동 비효율
 ┗━ Ⅶ 결론 ───── BFF(Backend For Frontend) 및 API Gateway 기반 SOAP $\leftrightarrow$ REST 변환 계층화
```

- **필수 키워드**: W3C 표준, SOAP Envelope / Header / Body / Fault, WSDL, UDDI, WS-Security, WS-ReliableMessaging, 메시지 레벨 보안, XML 파싱 오버헤드, REST 비교, BFF
  - **10점형**: SOAP 정의 및 봉투(Envelope) 구조도 → 웹 서비스 3대 표준(SOAP/WSDL/UDDI) → REST 비교표.
  - **25점형**: Ⅰ~Ⅶ 전체 구조 전개 + WS-* 엔터프라이즈 확장 표준(보안, 트랜잭션, 신뢰성) 심층 분석 + 모바일/클라우드 환경에서 REST/gRPC로의 진화 배경 및 레거시 연계 BFF 아키텍처 제시.

---

## 30초 인출용 핵심 다이어그램

```text
+-------------------------------------------------------------+
|                  SOAP 메시지 봉투(Envelope) 구조            |
+-------------------------------------------------------------+
|  <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/...">|
|                                                             |
|    <soap:Header>  <!-- 선택: 트랜잭션/보안/라우팅 정보 -->  |
|      <wsse:Security> (XML Signature, Encryption, Token)    |
|    </soap:Header>                                           |
|                                                             |
|    <soap:Body>    <!-- 필수: 실제 RPC 메서드 호출 데이터 -->|
|      <m:TransferMoney>                                      |
|        <m:Amount>1000000</m:Amount>                         |
|      </m:TransferMoney>                                     |
|                                                             |
|      <soap:Fault> <!-- 오류 발생 시 생성되는 예외 블록 -->  |
|        <faultcode>, <faultstring>, <detail>                 |
|      </soap:Fault>                                          |
|    </soap:Body>                                             |
|                                                             |
|  </soap:Envelope>                                           |
+-------------------------------------------------------------+
```

---

## 본론: 개념 및 핵심 메커니즘

### 1. SOAP의 공학적 본질과 웹 서비스 3대 축

- **개념**: Simple Object Access Protocol의 약자로, 이기종 분산 시스템 간에 정보(RPC 호출 및 데이터)를 교환하기 위해 W3C에서 제정한 **XML 기반의 표준 메시징 프로토콜**.
- **웹 서비스(Web Services) 3대 구성요소**:
  1. **SOAP**: 서비스 간 메시지를 포장하고 전송하는 **메시지 전송 프로토콜**.
  2. **WSDL (Web Services Description Language)**: 서비스 엔드포인트, 사용 가능한 메서드, 입출력 데이터 스키마를 명시하는 **인터페이스 기술 언어(XML)**.
  3. **UDDI (Universal Description, Discovery, and Integration)**: 웹 서비스를 검색하고 등록할 수 있는 **전역 비즈니스 레지스트리 저장소**.

### 2. SOAP 메시지 4대 구성요소

1. **SOAP Envelope (봉투)**: XML 문서를 SOAP 메시지로 식별하는 최상위 루트 요소로, 네임스페이스와 인코딩 규칙 선언.
2. **SOAP Header (헤더)**: 선택적 블록으로, 인증 토큰, WS-Security 전자서명, 세션 관리, 메시지 라우팅 등 부가 정보 전달.
3. **SOAP Body (본문)**: 필수 블록으로, 실제 호출 대상 메서드 이름과 전달 매개변수(Payload)를 XML로 인코딩하여 포함.
4. **SOAP Fault (오류)**: Body 내부 요소로, 요청 처리 중 오류가 발생했을 때 에러 코드(`faultcode`), 설명(`faultstring`), 상세 내역(`detail`)을 표준화하여 반환.

### 3. 엔터프라이즈 WS-* 확장 표준군

- **WS-Security**: 전송 계층(HTTPS)에만 의존하지 않고, 중간 프록시를 거치더라도 페이로드 자체를 종단 간(End-to-End) 암호화(XML Encryption)하고 전자서명(XML Signature)하여 위변조 방지.
- **WS-ReliableMessaging**: 네트워크 단절 시에도 메시지의 정확한 1회 전달(Exactly-once), 순서 보장(In-order) 전달을 메시지 레벨에서 보장.
- **WS-AtomicTransaction**: 분산 이기종 시스템 간에 2PC(Two-Phase Commit) 기반 ACID 트랜잭션 전파.

---

## SOAP vs REST vs gRPC 3자 비교

| 비교 항목 | SOAP | REST | gRPC |
|---|---|---|---|
| **프로토콜 성격** | 엄격한 규약의 공식 프로토콜 | 유연한 웹 아키텍처 스타일 | 초고속 RPC 프레임워크 |
| **데이터 포맷** | XML 전용 (장황함) | JSON, XML, YAML (텍스트) | Protocol Buffers (바이너리) |
| **전송 계층** | 전송 프로토콜 독립 (HTTP, SMTP, TCP) | HTTP/1.1, HTTP/2 종속 | HTTP/2 전용 (멀티플렉싱) |
| **계약(명세)** | 엄격한 WSDL 명세 필수 | OpenAPI Specification (선택) | `.proto` 파일 컴파일 필수 |
| **보안 체계** | WS-Security (메시지 자체 암호화) | TLS/HTTPS (전송 계층 암호화) | TLS/HTTPS (전송 계층 암호화) |
| **성능 및 오버헤드**| 매우 큼 (무거운 DOM XML 파싱) | 중간 (가벼운 JSON 파싱) | **극도로 빠름 (바이너리 직렬화)** |
| **현대 주 활용처** | 금융 결제망, 정부 레거시 행정망 | 퍼블릭 Open API, 웹/모바일 UI | 마이크로서비스 내부 고속 IPC |

---

## 실무 장애 시나리오 및 공학적 대안

### 1. 현장 장애 사례

1. **대규모 트래픽 시 SOAP XML 파싱에 의한 WAS 서버 다운**:
   - 금융 대외계 거래 폭증 시 거대한 XML 텍스트 파싱과 WS-Security 복호화 연산으로 CPU 사용률 100% 도달 및 서비스 중단.
2. **모바일 앱의 SOAP 연동 불가**:
   - 최신 Flutter/React Native 모바일 클라이언트에서 무거운 WSDL 기반 SOAP 클라이언트 라이브러리를 지원하지 않아 연동 개발 지연.

### 2. 문제 원인 및 공학적 해결책

| 장애 상황 | 근본 원인 | 공학적 대책 (대안 기술) | 개선 효과 |
|---|---|---|---|
| **XML 파싱 병목** | 텍스트 XML의 장황한 오버헤드 및 CPU 부하 | **Fast Infoset(바이너리 XML)** 적용 또는 게이트웨이 캐싱 | 페이로드 크기 60% 절감, 파싱 처리량 2.5배 향상 |
| **모바일 연동 난제** | 클라이언트-레거시 간 프로토콜 불일치 | **BFF(Backend for Frontend) 패턴** 적용 (SOAP $\rightarrow$ REST 변환) | 모바일 클라이언트 표준 JSON 연동 100% 지원 |
| **대외계 보안 위협** | 전송 계층만 암호화 시 중간 노드 탈취 위험 | 금융 결제 구간에 **WS-Security 종단 간(E2E) 암호화** 강제 | 중간 프록시 경유 시에도 데이터 무결성 보장 |

---

## 결론: 기술사 답안 차별화 포인트

1. **SOAP의 현대적 위상 재정립**: SOAP을 "버려야 할 옛 기술"로만 치부하지 않고, 엔터프라이즈 환경에서 **메시지 레벨 종단 간 보안(WS-Security)과 신뢰성 있는 전송(WS-RM)이 절대적으로 요구되는 금융 대외계 및 기간계 통신**에서는 여전히 핵심 인프라로 동작하고 있음을 균형 있게 기술할 것.
2. **2계층 인터페이스 아키텍처(BFF) 제시**: 대외 모바일/클라우드 영역은 가볍고 개방적인 REST/JSON으로 노출하고, 내부 백엔드 기간계 영역은 SOAP 어댑터를 통해 안전하게 연계하는 하이브리드 통합 아키텍처를 결론으로 제시할 것.
