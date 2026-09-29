---
title: "REST"
author: "Claude Code"
date: "2026-09-29T13:53:00+09:00"
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

소프트웨어 공학 → 인터페이스·API → **REST**

## 30초 인출

- 본질: REST는 자원을 URI로 식별하고 HTTP 메서드로 조작하는 웹 아키텍처 스타일
- 메커니즘: 클라이언트가 자원 URI에 GET·POST·PUT·DELETE 요청을 보내면 서버가 상태를 저장하지 않고 자원의 표현(JSON 등)을 응답
- 통찰: 네트워크 재시도로 POST 요청이 중복 처리될 수 있으므로 멱등 키로 중복 생성을 방지

<details>
<summary>핵심 용어</summary>

- **REST(Representational State Transfer)** : Roy Fielding이 제안한 자원 중심의 웹 아키텍처 스타일
- **REST API** : REST 제약을 따라 HTTP로 자원을 조작하도록 만든 API
- **무상태성(Stateless)** : 각 요청이 필요한 정보를 모두 담고 서버가 클라이언트 상태를 저장하지 않는 성질
- **균일한 인터페이스(Uniform Interface)** : 자원 식별·표현을 통한 조작·자기 서술 메시지·HATEOAS로 이루어진 통일된 인터페이스
- **멱등성(Idempotency)** : 같은 요청을 여러 번 보내도 결과가 한 번 보낸 것과 같은 성질
- **SOAP** : XML 메시지와 WSDL로 서비스를 정의하는 프로토콜 기반의 웹 서비스 방식

</details>

---

## 2~4교시 예상문제 (25점)

> REST API에 대하여 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. REST의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **REST** 는 자원을 URI로 식별하고 HTTP 메서드로 조작하는 웹 아키텍처 스타일 |
| 목적 | 단순한 표준 인터페이스에 의한 확장성과 서비스 간 연동성 확보 |

## Ⅱ. REST의 특징

| 특징 | 의미 |
|---|---|
| 자원 중심 | 기능이 아닌 자원을 URI로 식별 |
| 무상태성 | 요청마다 필요한 정보를 포함해 서버 확장 용이 |
| 표준 메서드 | HTTP 메서드로 자원 조작 |
| 다양한 표현 | JSON·XML 등으로 자원 상태 전달 |

## Ⅲ. REST 제약 조건과 요청 처리 흐름

### REST의 아키텍처 제약

```text
REST 제약
    ├─ 클라이언트-서버 ── 관심사 분리
    ├─ 무상태 ── 요청 자체에 필요한 정보 포함
    ├─ 캐시 가능 ── 응답의 캐시 여부 명시
    ├─ 균일한 인터페이스 ── URI·표현·자기 서술·HATEOAS
    ├─ 계층형 시스템 ── 중간 서버 투명 사용
    └─ 코드 온 디맨드 ── 선택 사항
```

### 확대: 요청 처리 흐름

```text
클라이언트: GET /orders/10
    ↓
서버: 자원 조회 (세션 상태 미사용)
    ↓
응답: 200 OK + 자원 표현(JSON)
```

## Ⅳ. HTTP 메서드와 SOAP와의 비교

### HTTP 메서드

| 메서드 | 동작 | 안전 | 멱등 |
|---|---|---|---|
| GET | 조회 | 예 | 예 |
| POST | 생성 | 아니오 | 아니오 |
| PUT | 전체 교체 | 아니오 | 예 |
| PATCH | 부분 수정 | 아니오 | 일반적으로 아니오 |
| DELETE | 삭제 | 아니오 | 예 |

### REST와 SOAP의 구성요소 비교

| 구분 | REST | SOAP |
|---|---|---|
| 성격 | 아키텍처 스타일 | 프로토콜 |
| 메시지 | JSON·XML 등 자유 | XML 필수 |
| 서비스 정의 | URI와 메서드 | WSDL |
| 전송 | 주로 HTTP | HTTP 외 다른 전송도 가능 |
| 상태 | 무상태 | 상태 유지 가능 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 네트워크 재시도로 POST 중복 처리 | 클라이언트가 보낸 멱등 키로 중복 요청 식별 |
| 자원 이름·URI 설계 규칙 불일치로 API 혼란 | 명사 복수형·계층 구조 등 URI 설계 규칙 표준화 |
| 응답 필드 과다 또는 부족 | 필드 선택·페이지네이션 파라미터 제공 |

## Ⅵ. 제언

상태를 바꾸는 POST 요청에는 멱등 키를 요구해 재시도 시 중복 생성을 방지

### 멱등 키 처리 흐름

```text
클라이언트: POST + 멱등 키
    ↓
서버: 키 조회
    ├─ 처음 → 처리 후 결과 저장
    └─ 이미 처리됨 → 저장된 결과 반환
```

### 확대: 재시도 상황

```text
응답 유실 → 클라이언트 재시도(동일 키)
    ↓
서버가 이미 처리한 결과 반환 → 중복 생성 없음
```

### 선택 근거: 멱등 키 없는 POST와의 비교

| 구분 | 멱등 키 없음 | 제언: 멱등 키 사용 |
|---|---|---|
| 재시도 시 결과 | 중복 생성 위험 | 동일 결과 |
| 클라이언트 부담 | 없음 | 키 생성 필요 |
| 서버 부담 | 없음 | 키 저장·조회 |

## 출제 이력과 검증 출처

- 제133회 1교시 1번: REST API(REpresentational State Transfer Application Programming Interface)
- 제134회 4교시 4번: 개방형 API의 정의·특징, SOAP 및 REST 구성요소, 취약점 및 대응 방안. Open API 범위로 기본 답안과 구별
- Fielding(2000), Architectural Styles and the Design of Network-based Software Architectures

## 연결 토픽

- 이전 토픽: [ATAM](./014_atam.md)
- 연관 토픽: [SOAP](./037_soap.md), [Open API](./022_open_api.md)
- 다음 토픽: [기술 부채](./016_technical_debt.md)
