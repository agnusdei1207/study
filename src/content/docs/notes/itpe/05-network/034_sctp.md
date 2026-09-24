---
sidebar:
  order: 34
  label: "034. SCTP"
  badge:
    text: "서브"
    variant: note
title: "SCTP(Stream Control Transmission Protocol)"
author: "Codex"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 34
extra:
  model: "GPT-6"
  keyword_grade: "서브"
  question_no: "034"
---

## 지식 로드맵 내 현재 위치

지식 위치: 네트워크 → 전송 계층 프로토콜 → **SCTP**

## 30초 인출

- 본질: **SCTP(Stream Control Transmission Protocol)** : IP 위에서 신뢰성 있는 메시지 전송과 다중 스트림·멀티호밍을 지원하는 전송 프로토콜
- 메커니즘: 4-way 쿠키 핸드셰이크로 association 구성 → 스트림별 순서·확인 응답으로 데이터 전송 → 복수 경로 상태 관리

<details>
<summary>핵심 용어</summary>

- **SCTP(Stream Control Transmission Protocol)** : 메시지 기반 신뢰 전송·다중 스트림·멀티호밍을 제공하는 전송 프로토콜
- **Association** : SCTP 양단 사이의 논리적 전송 관계
- **청크(Chunk)** : SCTP 패킷을 구성하는 제어·데이터 단위
- **멀티스트리밍(Multistreaming)** : 하나의 association 안에서 여러 순서화 스트림을 독립적으로 전달하는 기능
- **멀티호밍(Multihoming)** : 한쪽 또는 양쪽 endpoint에서 복수 전송 주소를 이용할 수 있는 기능
- **SCTP 쿠키 핸드셰이크(Cookie Handshake)** : INIT·INIT ACK·COOKIE ECHO·COOKIE ACK 순으로 association을 설정하는 절차
- **SACK(Selective Acknowledgement)** : 수신 청크 상태를 알리는 SCTP 확인 응답 청크
- **HoL(Head-of-Line) blocking** : 앞선 데이터의 지연·손실 때문에 뒤 데이터가 대기하는 현상; SCTP 스트림 간 순서 독립으로 일부 완화

</details>

---

## 1교시 예상문제 (10점)

> SCTP의 개념과 association·멀티스트리밍·멀티호밍을 설명하시오. (예상·10점)

---

## 1교시 10점 답안

### Ⅰ. SCTP의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **SCTP** : 메시지 기반 신뢰 전송과 다중 스트림·복수 경로 주소를 지원하는 전송 프로토콜 |
| 목적 | 메시지 경계 유지, 스트림 간 순서 분리, 경로 장애 대응 지원 |

### Ⅱ. 주요 기능

```text
SCTP association
    ├─ 멀티스트리밍 · 스트림별 순서화
    ├─ 멀티호밍 · 복수 전송 주소
    └─ 청크 기반 메시지 전송
```

- 제언: 메시지 경계·스트림 독립성·경로 전환 요구를 기준으로 전송 방식 선정.

---

## 2~4교시 예상문제 (25점)

> SCTP의 association 설정과 청크·멀티스트리밍·멀티호밍 구조를 설명하고, 적용 시 순서·경로 관리의 한계 및 대응을 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

### Ⅰ. SCTP의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **SCTP** : 메시지 기반 신뢰 전송과 다중 스트림·복수 경로 주소를 지원하는 전송 프로토콜 |
| 목적 | 메시지 경계 유지, 스트림 간 순서 분리, 경로 장애 대응 지원 |

```text
SCTP association
    ├─ 멀티스트리밍 · 스트림별 순서화
    ├─ 멀티호밍 · 복수 전송 주소
    └─ 청크 기반 메시지 전송
```

### Ⅱ. Association 설정

```text
Initiator → INIT → Responder
Initiator ← INIT ACK + state cookie ← Responder
Initiator → COOKIE ECHO → Responder
Initiator ← COOKIE ACK ← Responder
```

상태 쿠키를 이용해 INIT 단계에서 응답자가 association 상태를 바로 생성하지 않도록 해 자원 남용 위험을 완화.

### Ⅲ. 패킷·청크 구성

| 항목 | 역할 |
|---|---|
| SCTP 패킷 | 공통 헤더 뒤 하나 이상의 청크 포함 가능 |
| DATA 청크 | 사용자 메시지 일부·순서 정보를 전달 |
| 제어 청크 | INIT·SACK·HEARTBEAT 등 association·전송 상태 처리 |
| Bundling | 복수 청크를 한 SCTP 패킷에 넣는 기능 |

### Ⅳ. 멀티스트리밍과 순서 제어

```text
하나의 association
    ├─ Stream 0 · 메시지 순서 관리
    ├─ Stream 1 · 독립된 순서 관리
    └─ Stream 2 · 독립된 순서 관리
```

한 스트림의 순서화 데이터 지연이 다른 스트림의 애플리케이션 순서 처리까지 막는 현상을 완화. 공통 경로 혼잡·패킷 손실·수신 자원 영향까지 제거하는 것은 아님.

### Ⅴ. 멀티호밍과 경로 장애

| 기능 | 동작 | 적용 시 점검 |
|---|---|---|
| 복수 주소 등록 | 한 endpoint가 복수 전송 주소를 association에서 사용 | 주소 도달성·경로 분리 |
| Primary Path | 기본 전송 경로 지정 | 평상시 송신 경로·경로 품질 |
| HEARTBEAT | 경로 도달성 확인에 사용 | 주기·실패 판정·전환 지연 |
| 대체 경로 | 기본 경로 장애 시 도달 가능한 주소 활용 | 구현·타이머·네트워크 정책에 따른 동작 시험 |

### Ⅵ. 한계와 대응

| 한계 | 대응 |
|---|---|
| 스트림 분리만으로 공통 경로 손실·혼잡이 사라지지 않음 | 손실·혼잡 제어와 응용 메시지 순서 요구를 함께 설계 |
| 복수 주소가 같은 장애 구간을 공유할 수 있음 | 사업자·경로·전원 등 실패 도메인 분리 확인 |
| NAT·방화벽에서 SCTP 프로토콜 지원 차이 | 중간 장비 호환성·필터 정책 시험; 필요한 경우 규격 기반 UDP 캡슐화 검토 |
| 경로 장애 감지·전환 시간이 환경별로 다름 | heartbeat·재전송·경로 failover 타이머를 장애 주입으로 측정 |

### Ⅶ. 기술사적 제언

| 우선 적용 | 검증 기준 |
|---|---|
| 메시지 전송·스트림 격리·경로 복원 요구에 맞춰 SCTP 적용 범위 선정 | 실제 방화벽·NAT·경로 장애 환경에서 순서성·재전송·전환 시간을 시험 |

---

## 출제 이력과 검증 출처

- 제132회 3교시 4번: “SCTP(Stream Control Transmission Protocol)에 대하여 다음을 설명하시오.”
- [RFC 9260: Stream Control Transmission Protocol](https://www.rfc-editor.org/rfc/rfc9260) — 최신 SCTP 기본 규격, 청크·멀티스트리밍·멀티호밍·쿠키 핸드셰이크
- [RFC 6951: UDP Encapsulation of SCTP Packets](https://www.rfc-editor.org/rfc/rfc6951) — NAT 통과를 위한 SCTP UDP 캡슐화 규격

## 연결 토픽

- 연관 토픽: [ARQ](./015_arq.md), [WebRTC](./036_webrtc.md)
