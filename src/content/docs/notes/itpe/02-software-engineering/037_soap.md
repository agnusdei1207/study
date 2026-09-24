---
title: "SOAP"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
author: "Codex"
date: "2026-09-24T00:00:00+09:00"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어 공학 → 구현·객체지향·API → **SOAP**

## 30초 인출

- 본질: **SOAP(Simple Object Access Protocol)**은 분산 환경에서 구조화된 정보(XML)를 교환하기 위해 W3C에서 표준화한 XML 기반의 엄격한 메시징 프로토콜
- 메커니즘: **Envelope**가 **Header**(선택)와 **Body**(필수)를 감싸는 XML 메시지 구조
- 산출/효과: 전송 프로토콜 독립성(HTTP, SMTP 등) · **WS-Security** 기반 엔터프라이즈 보안 · 엄격한 계약(Contract) 기반 상호운용성

<details>
<summary>핵심 용어</summary>

- **SOAP**: 플랫폼과 프로그래밍 언어에 독립적으로 XML 기반 메시지를 교환하기 위한 W3C 표준 분산 프로토콜
- **WSDL(Web Services Description Language)**: 웹 서비스의 위치, 제공하는 메서드, 매개변수 타입을 XML로 엄격히 기술한 인터페이스 계약서
- **UDDI(Universal Description, Discovery, and Integration)**: 웹 서비스 등록·검색을 위한 디렉터리 표준
- **SOAP Fault**: SOAP 메시지 처리 중 오류가 발생했을 때 상세 에러 정보를 표준 규격으로 반환하는 Body 하위 엘리먼트
- **WS-Security**: 메시지 수준에서 서명·암호화·보안 토큰을 다루는 웹 서비스 보안 표준

</details>

---

## 1교시 예상문제 (10점)

> SOAP의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. SOAP의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **SOAP(Simple Object Access Protocol)** 은 분산 환경에서 XML 기반 메시지를 교환하는 표준 메시징 프로토콜 |
| 목적 | 메시지 형식과 확장 규칙의 표준화를 통한 상호운용성 지원 |

### Ⅱ. SOAP 메시지 구조

```text
SOAP Envelope
    ├─ Header: 선택·메타 정보
    └─ Body: 필수·메시지 본문
         ├─ 요청·응답 데이터
         └─ Fault: 오류 정보
```

### Ⅲ. 서비스 계약·보안 연계

- **WSDL**: 서비스 인터페이스·메시지 형식을 기술하는 서비스 설명 표준
- **WS-Security**: 메시지 수준의 서명·암호화·보안 토큰 처리 표준
- 한 줄 제언: 메시지 계약과 보안 확장 요구를 먼저 확인하고 필요한 SOAP 요소만 적용
---

## 2~4교시 예상문제 (25점)

> SOAP의 목적과 메시지 구조를 설명하고, WSDL을 통한 서비스 계약 정의 및 REST와 비교한 적용 고려사항을 제시하시오. (25점, 예상)

---

## 2~4교시 25점 답안

## Ⅰ. SOAP 개요와 메시지 구조

> SOAP은 XML 메시지 형식과 확장 표준을 정의하며, SOAP을 선택할지는 상대 시스템의 계약·보안 요구와 운영 여건에 맞춰 판단한다.

| 구분 | 핵심 |
|---|---|
| 정의 | **SOAP(Simple Object Access Protocol)** 은 분산 환경에서 XML 기반 메시지를 교환하는 표준 메시징 프로토콜 |
| 목적 | 메시지 형식과 확장 규칙의 표준화를 통한 상호운용성 지원 |

> SOAP 메시지는 Envelope를 최상위 요소로 두며, Header는 선택 요소이고 Body는 필수 요소다.

```text
SOAP Envelope
    ├─ Header: 선택·메타 정보
    └─ Body: 필수·메시지 본문
         ├─ 요청·응답 데이터
         └─ Fault: 오류 정보
```

## Ⅱ. 메시징과 서비스 설명·탐색의 연계

> 세 기술은 서비스 출판(Publish), 검색(Find), 바인딩(Bind)의 삼각관계를 형성한다.

```text
제공자: 서비스 계약(WSDL) 게시
    ↓ 선택적 발견
요청자: 계약·엔드포인트 확인
    ↓ SOAP 요청
제공자: SOAP 응답·Fault 반환
```

## Ⅲ. SOAP 적용 한계·대응책

> 경량성과 모바일 확장을 중시하는 웹 환경은 REST로 재편되었으나, 레거시 금융과 보안 연계에서는 여전히 SOAP이 공존한다.

| 비교 항목 | SOAP (Simple Object Access Protocol) | REST (Representational State Transfer) |
|---|---|---|
| **본질적 위상** | **엄격한 프로토콜 (Protocol)** | **유연한 아키텍처 스타일 (Style)** |
| **데이터 포맷** | XML 기반 메시지 | 자원 표현 형식은 구현에 따라 다양 |
| **인터페이스 계약**| WSDL로 서비스 인터페이스를 기술할 수 있음 | 자원·제약 조건에 따라 계약을 기술하고 OpenAPI를 활용할 수 있음 |
| **전송 프로토콜** | 바인딩에 따라 여러 전송을 사용할 수 있음 | 보통 HTTP 제약과 메서드를 활용하지만 REST 자체는 HTTP 전용이 아님 |
| **보안 메커니즘** | **WS-Security (메시지 레벨 암호화/무결성)** | 전송 레벨 HTTPS(TLS) 및 애플리케이션 JWT |
| **성능 및 복잡도** | 파싱 오버헤드 큼, 학습 곡선 높음 | 빠르고 단순함, 브라우저/모바일 친화적 |

| 위험 | 대책 | 효과 |
|---|---|---|
| 대용량 XML 처리 비용 | 메시지 크기 제한 · 스트리밍 파서 · 압축 적용 | 자원 고갈·지연 완화 |
| 계약 변경으로 소비자 장애 | WSDL 버전 관리 · 호환성 테스트 | 연계 시스템 회귀 방지 |
| 메시지 보안 설정 오류 | WS-Security 프로파일 검증 · 키 수명주기 통제 | 종단 간 무결성·기밀성 확보 |

### 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 연계 방식이 과거 선택이나 유행에 따라 고정되어 상대 시스템의 실제 계약 요구를 반영하지 못함 | 새 연계마다 XML 계약·메시지 수준 보안·기존 소비자 호환성 요구를 확인하고, 요구를 만족하는 가장 단순한 방식과 어댑터 범위 선택 |
---

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 2교시: 웹 서비스(SOAP)와 RESTful 아키텍처의 심층 비교
- W3C SOAP Version 1.2 Specification
- [W3C SOAP Version 1.2 Part 1: Messaging Framework](https://www.w3.org/TR/soap12/)
- OASIS Web Services Security (WSS) TC Standard

## 연결 토픽

- 이전 토픽: [McCabe 순환복잡도](./036_mccabe_cyclomatic_complexity.md)
- 연관 토픽: [REST](./015_rest.md), [Open API](./022_open_api.md)
- 다음 토픽: [개발방법론 테일러링](./039_methodology_tailoring.md)
