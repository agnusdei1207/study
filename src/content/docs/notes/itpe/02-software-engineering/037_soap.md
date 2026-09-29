---
title: "SOAP"
author: "Claude Code"
date: "2026-09-29T15:12:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 인터페이스·API → **SOAP**

## 30초 인출

- 본질: SOAP는 XML 메시지로 분산 환경의 서비스 호출 정보를 주고받는 웹 서비스 프로토콜
- 메커니즘: 서비스 제공자가 WSDL로 인터페이스를 기술하고 클라이언트가 Envelope·Header·Body 구조의 XML 메시지를 HTTP 등으로 전송하며 오류는 Fault로 응답
- 통찰: SOAP는 표준 계약(WSDL)과 메시지 보안(WS-Security)을 주지만 XML 처리 비용이 크므로 엄격한 계약·보안이 필요한 기업 간 연계에 적용하고 그 외는 REST 선택

<details>
<summary>핵심 용어</summary>

- **SOAP(Simple Object Access Protocol)** : XML 메시지로 서비스를 호출하고 응답을 받는 프로토콜
- **WSDL(Web Services Description Language)** : 서비스의 위치·오퍼레이션·메시지 형식을 기술하는 XML 문서
- **UDDI(Universal Description, Discovery and Integration)** : 웹 서비스를 등록·검색하는 레지스트리 규격
- **SOAP Envelope** : 메시지의 최상위 요소로 Header와 Body를 감싸는 구조
- **SOAP Fault** : 처리 중 발생한 오류를 표준 형식으로 알리는 요소
- **WS-Security** : 메시지 자체에 서명·암호화를 적용하는 SOAP 보안 규격

</details>

---

## 2~4교시 예상문제 (25점)

> SOAP(Simple Object Access Protocol)에 대하여 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. SOAP의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **SOAP** 는 XML 메시지로 분산 환경의 서비스 호출 정보를 주고받는 웹 서비스 프로토콜 |
| 목적 | 플랫폼·언어에 독립적인 서비스 연계 |

## Ⅱ. SOAP의 특징

| 특징 | 의미 |
|---|---|
| XML 기반 | 메시지를 XML로 표현 |
| 계약 중심 | WSDL로 서비스 인터페이스 사전 정의 |
| 전송 독립 | HTTP·SMTP 등 여러 전송 사용 |
| 확장 표준 | WS-Security 등 부가 규격 |

## Ⅲ. SOAP 메시지 구조와 호출 흐름

### SOAP 메시지 구조

```text
Envelope
    ├─ Header ── 보안·트랜잭션 등 부가 정보
    └─ Body ── 호출 내용 또는 응답 (오류 시 Fault)
```

### 확대: 웹 서비스 호출 흐름

```text
서비스 제공자: WSDL 공개 (UDDI 등록)
    ↓
클라이언트: WSDL로 호출 형식 확인
    ↓
SOAP 요청 (XML) → 서비스 처리 → SOAP 응답 (또는 Fault)
```

## Ⅳ. SOAP와 REST의 구성요소 비교

| 구분 | SOAP | REST |
|---|---|---|
| 성격 | 프로토콜 | 아키텍처 스타일 |
| 메시지 | XML(Envelope·Header·Body) | JSON·XML 등 자유 |
| 서비스 정의 | WSDL | URI·HTTP 메서드 |
| 보안 | WS-Security(메시지 수준) | 전송 계층(TLS)과 토큰 |
| 처리 비용 | 높음 | 낮음 |
| 적합 환경 | 엄격한 계약·트랜잭션·보안이 필요한 기업 연계 | 웹·모바일의 가벼운 연동 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| XML 파싱·메시지 크기로 처리 비용 증가 | 대량·저지연 연동은 REST 등으로 대체 |
| XML 외부 엔티티 등 XML 파서 취약점 | 외부 엔티티 처리 비활성화와 입력 스키마 검증 |
| WSDL 변경 시 클라이언트 재생성 | WSDL 버전 관리와 하위 호환 유지 |

## Ⅵ. 제언

엄격한 계약과 메시지 수준 보안이 필요한 기업 간 연계는 SOAP를 유지하고, 그 밖의 연동은 REST로 구성

### 방식 선택 기준

```text
연동 요구
    ├─ 엄격한 계약·메시지 수준 보안·트랜잭션 → SOAP
    └─ 단순·경량·모바일 → REST
```

### 선택 근거: 일률 적용과의 비교

| 구분 | 모두 SOAP | 제언: 요구별 선택 |
|---|---|---|
| 처리 비용 | 높음 | 요구에 맞춤 |
| 계약·보안 | 일관 | 필요한 곳에만 |
| 개발 부담 | 큼 | 균형 |

## 출제 이력과 검증 출처

- 제134회 4교시 4번: 개방형 API의 정의 및 특징, SOAP 및 REST 구성요소, 취약점 및 대응 방안. SOAP·REST 구성요소 범위로 기본 답안과 구별
- W3C, SOAP Version 1.2

## 연결 토픽

- 이전 토픽: [McCabe 순환복잡도](./036_mccabe_cyclomatic_complexity.md)
- 연관 토픽: [REST](./015_rest.md), [Open API](./022_open_api.md)
- 다음 토픽: [개발방법론 테일러링](./039_methodology_tailoring.md)
