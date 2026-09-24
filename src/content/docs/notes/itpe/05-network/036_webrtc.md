---
sidebar:
  order: 36
  label: "036. WebRTC"
  badge:
    text: "기초"
    variant: note
title: "WebRTC(Web Real-Time Communication)"
author: "Codex"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 36
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "036"
---

## 지식 로드맵 내 현재 위치

지식 위치: 네트워크 → 실시간 브라우저 통신 → **WebRTC**

## 30초 인출

- 본질: **WebRTC(Web Real-Time Communication)** : 브라우저·응용에서 실시간 오디오·영상·데이터 통신을 지원하는 웹 API와 프로토콜 체계
- 메커니즘: 응용의 signaling으로 SDP 교환 → ICE로 통신 경로 확인 → DTLS-SRTP 미디어·SCTP 데이터 통신

<details>
<summary>핵심 용어</summary>

- **WebRTC(Web Real-Time Communication)** : 실시간 미디어·데이터 연결을 위한 웹 API와 관련 통신 체계
- **Signaling(시그널링)** : 세션 설명과 ICE 후보를 교환하는 응용 경로; WebRTC 표준이 특정 signaling 전송 프로토콜을 정하지 않음
- **SDP(Session Description Protocol)** : 세션·미디어 속성을 표현하는 형식; 자체적으로 미디어를 전달하지 않음
- **ICE(Interactive Connectivity Establishment)** : 후보 주소·포트를 시험해 통신 경로를 찾는 NAT 통과 프레임워크
- **STUN(Session Traversal Utilities for NAT)** : NAT 환경의 주소 정보를 파악하고 연결성 검사를 지원하는 프로토콜
- **TURN(Traversal Using Relays around NAT)** : 직접 연결이 어려울 때 미디어·데이터를 중계하는 릴레이 프로토콜
- **DTLS-SRTP(Datagram Transport Layer Security–Secure Real-time Transport Protocol)** : WebRTC 미디어 전송 보안에 쓰이는 키 교환·보호 구조
- **SCTP(Stream Control Transmission Protocol)** : WebRTC 데이터 채널의 신뢰성 있는 메시지 전달에 사용되는 전송 프로토콜
- **SFU(Selective Forwarding Unit)** : 참가자 미디어를 선택·전달하는 다자 통화 서버 구조

</details>

---

## 1교시 예상문제 (10점)

> WebRTC의 개념과 signaling·ICE 기반 연결 과정을 설명하시오. (예상·10점)

---

## 1교시 10점 답안

### Ⅰ. WebRTC의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **WebRTC** : 실시간 미디어·데이터 통신을 위한 브라우저·응용 API와 프로토콜 체계 |
| 목적 | 웹 응용에서 피어 간 실시간 통신과 미디어·데이터 연결 지원 |

### Ⅱ. 연결 절차와 통신

```text
피어 A·B 간 SDP Offer/Answer·ICE 후보 교환
                 ↓ 응용 signaling 경로
ICE 후보 쌍 연결성 검사 (STUN·TURN 활용 가능)
                 ↓ 경로 선택
DTLS 키 협상
                 ↓
SRTP 미디어 · SCTP 데이터 채널
```

- 제언: signaling·ICE 경로 확인·보안 미디어 전송을 함께 설계.

---

## 2~4교시 예상문제 (25점)

> WebRTC의 세션 협상·ICE 연결·보안 전송 구조를 설명하고, NAT·망 정책·다자 통화의 한계와 대응 방안을 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

### Ⅰ. WebRTC의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **WebRTC** : 실시간 미디어·데이터 통신을 위한 브라우저·응용 API와 프로토콜 체계 |
| 목적 | 웹 응용에서 피어 간 실시간 통신과 미디어·데이터 연결 지원 |

### Ⅱ. 연결 절차와 통신

```text
피어 A·B 간 SDP Offer/Answer·ICE 후보 교환
                 ↓ 응용 signaling 경로
ICE 후보 쌍 연결성 검사 (STUN·TURN 활용 가능)
                 ↓ 경로 선택
DTLS 키 협상
                 ↓
SRTP 미디어 · SCTP 데이터 채널
```

Signaling은 응용이 구현하는 SDP·ICE 후보 교환 경로. ICE는 직접 후보뿐 아니라 TURN 릴레이 후보를 포함해 연결 가능한 경로를 검사.

### Ⅲ. 주요 구성요소

| 구성 | 역할 | 참고 |
|---|---|---|
| SDP | 미디어 종류·코덱·전송 매개변수 교환 | Offer/Answer 등 협상 절차에 사용 |
| ICE | 후보 수집·연결성 검사·경로 선택 | STUN·TURN 사용 가능 |
| DTLS-SRTP | 미디어 키 설정·보호 | 브라우저 간 미디어 보안 |
| SCTP over DTLS | 데이터 채널 메시지 전송 | 순서·신뢰성 모드는 응용에서 설정 |

### Ⅳ. NAT·방화벽 연결 경로

| 경로 후보 | 역할 | 운용상 고려 |
|---|---|---|
| Host candidate | 로컬 인터페이스 주소 후보 | 로컬 네트워크·접근 정책 |
| Server-reflexive candidate | STUN 기반 공인 측 주소 후보 | NAT 매핑·필터 동작 |
| Relay candidate | TURN 서버를 통한 중계 경로 | 서버 비용·대역폭·중계 지연 |

### Ⅴ. 다자 통화 토폴로지

| 구조 | 미디어 처리 | 주요 고려 |
|---|---|---|
| Mesh | 참가자 간 직접 연결 | 참가자 수 증가 시 단말 업로드·연결 수 증가 |
| SFU(Selective Forwarding Unit) | 수신자별 미디어 스트림 선택 전달 | 서버 네트워크·미디어 라우팅 비용 |
| MCU(Multipoint Control Unit) | 서버에서 미디어 합성·처리 | 서버 연산·지연·코덱 처리 부담 |

### Ⅵ. 한계와 대응

| 한계 | 대응 |
|---|---|
| NAT·방화벽 정책으로 직접 후보 연결 실패 | TURN 경로·전송 프로토콜 후보를 포함해 기업망 연결 시험 |
| 네트워크·장치 성능에 따른 지연 편차 | 실제 단말·망 조건에서 종단 지연·손실·지터 측정 |
| 다자 Mesh의 단말 업로드 증가 | 참가자 규모·기기 성능 기준으로 SFU·MCU 검토 |
| signaling 서버 장애로 신규 연결 협상 실패 | signaling 가용성·인증·세션 상태 복구 설계 |

### Ⅶ. 기술사적 제언

| 우선 선택 | 적용·검증 |
|---|---|
| 단말·망 조건과 회의 규모에 맞는 연결·미디어 토폴로지 선택 | P2P·TURN·SFU/MCU를 장애·부하·보안 조건별 시험 후 비용·품질 기준 수립 |

---

## 출제 이력과 검증 출처

- 제123회 2교시: “WebRTC의 개념, 주요 프로토콜 스택, 세션 연결 절차(SDP, ICE, STUN, TURN) 및 1:N/N:M 통화 구성을 위한 아키텍처(Mesh, MCU, SFU)를 설명하시오.”
- [W3C WebRTC: Real-Time Communication in Browsers](https://www.w3.org/TR/webrtc/)
- [RFC 8825: Overview: Real-Time Protocols for Browser-Based Applications](https://www.rfc-editor.org/rfc/rfc8825)
- [RFC 8445: Interactive Connectivity Establishment (ICE)](https://www.rfc-editor.org/rfc/rfc8445)
- [RFC 8827: WebRTC Security Architecture](https://www.rfc-editor.org/rfc/rfc8827)

## 연결 토픽

- 연관 토픽: [SCTP](./034_sctp.md), [NAT](./071_nat.md)
