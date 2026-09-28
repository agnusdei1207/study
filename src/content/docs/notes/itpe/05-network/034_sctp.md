---
sidebar:
  order: 34
  label: "034. SCTP"
  badge:
    text: "기초"
    variant: note
title: "SCTP(Stream Control Transmission Protocol)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 34
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
  question_no: "034"
---

## 지식 로드맵 내 현재 위치

지식 위치: 네트워크 → 전송 계층 프로토콜 → **SCTP**

## 30초 인출

- 본질: **SCTP(Stream Control Transmission Protocol)** : IP 위에서 신뢰성 있는 메시지 전송과 다중 스트림·멀티호밍을 지원하는 전송 프로토콜
- 메커니즘: 4-way 쿠키 핸드셰이크로 association 구성 → 스트림별 순서·확인 응답으로 데이터 전송 → 복수 경로 상태 관리
- 통찰: TCP의 바이트 스트림 기반 순서 의존성 및 단일 IP 연결 취약점을 극복하기 위해 다중 스트림(Multi-streaming)으로 HOL 블로킹을 해소하고 멀티호밍(Multi-homing)으로 무중단 네트워크 고가용성을 제공하는 전송 계층 프로토콜임.

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

## 2~4교시 예상문제 (25점)

> 차세대 전송 계층 프로토콜인 SCTP(Stream Control Transmission Protocol)의 개념, TCP/UDP와의 비교, 4-Way 핸드셰이크(SYN Flood 방어), 멀티호밍(Multi-homing) 및 멀티스트리밍(Multi-streaming) 구조를 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. SCTP(Stream Control Transmission Protocol)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | TCP의 신뢰성 있는 연결 지향 전송 특성과 UDP의 메시지 경계 보존 특성을 결합하고, 멀티호밍(복수 IP) 및 멀티스트리밍(복수 독립 채널)을 지원하는 IP 전송 계층 표준 프로토콜(RFC 4960) |
| 목적 | 통신사 PSTN 시그널링(SS7)의 IP망 수용(SIGTRAN), WebRTC 데이터 채널 지원 및 단일 인터페이스 장애 시 무중단 서비스 페일오버 보장 |

## Ⅱ. SCTP(Stream Control Transmission Protocol)의 특징

| 특징 | 상세 내용 |
|---|---|
| 멀티호밍 (Multi-homing)| 단일 SCTP 결합(Association)에 양단 호스트의 복수 IP 주소를 바인딩하여 장애 시 자동 경로 절체 |
| 멀티스트리밍 | 하나의 연결 내에서 독립적인 여러 개의 스트림을 병렬 전송하여 특정 패킷 손실 시 타 스트림 차단 방지 |
| 메시지 경계 보존 | TCP처럼 바이트 스트림으로 뭉개지지 않고 응용 프로그램이 보낸 메시지(청크, Chunk) 단위 경계 유지 |
| 쿠키 기반 4-Way 연결 | INIT-ACK 단계에서 State Cookie를 발행하여 TCP 고질병인 SYN 플러딩(SYN Flood) 공격 원천 방어 |

## Ⅲ. SCTP(Stream Control Transmission Protocol)의 체계·프로세스

**SCTP 패킷 청크 구조 및 멀티호밍 페일오버 아키텍처**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ SCTP 패킷 및 멀티호밍 아키텍처 ]              │
│                                                                        │
│   [ SCTP 패킷 구조 ]                                                   │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 공통 헤더 (12B: 발신/착신 포트, 검증 태그 Verification Tag, CRC)│   │
│   ├────────────────────────────────┬───────────────────────────────┤   │
│   │ 청크 1 (Control Chunk: INIT)   │ 청크 2 (Data Chunk: Stream 0) │   │
│   └────────────────────────────────┴───────────────────────────────┘   │
│                                                                        │
│   [ SCTP 멀티호밍 (Multi-homing) 무중단 경로 절체 ]                    │
│   [ Host A ]                                            [ Host B ]     │
│   IP A-1 (기본) ═══════ Primary Path (정상 전송) ═══════► IP B-1 (기본) │
│                                 X (선로 단절 발생)                     │
│   IP A-2 (보조) ─────── Alternate Path (자동 절체) ────► IP B-2 (보조) │
│   (기존 세션 재수립 없이 즉각 보조 IP 경로로 데이터 흐름 자동 전환 완료)│
└────────────────────────────────────────────────────────────────────────┘
```

| 핵심 기능 | 세부 동작 메커니즘 | 기술적 기대 효과 |
|---|---|---|
| **멀티호밍** | Heartbeat 청크로 주기적 보조 경로 생존 검사, Primary 단절 시 Secondary로 즉시 Failover | 통신사 99.999% 무중단 네트워크 고가용성 달성 |
| **멀티스트리밍** | 스트림별 독립 시퀀스 번호(SSN) 부여, 1번 스트림 패킷 손실 시에도 2번 스트림 정상 소비 | TCP의 고질적 헤드오브라인(HOL) 블로킹 완벽 해소 |
| **State Cookie** | 서버가 연결 상태 TCB를 메모리에 생성하지 않고 클라이언트에 암호화 쿠키로 서명 전달 | SYN Flooding DoS 공격 원천 무력화 |
| **선택적 ACK (SACK)**| 수신된 데이터 블록을 정밀하게 보고하는 SACK 청크를 기본 프로토콜 스펙으로 내장 | 불필요한 패킷 재전송 방지 및 처리율 향상 |

## Ⅳ. SCTP(Stream Control Transmission Protocol)의 종류·비교

| 비교 항목 | TCP (Transmission Control) | UDP (User Datagram) | SCTP (Stream Control) |
|---|---|---|---|
| **연결 지향성** | 연결 지향 (Connection) | 비연결형 (Connectionless) | **연합 지향 (Association)** |
| **전송 단위** | 연속된 바이트 스트림 | 독립적 데이터그램 | **메시지 청크 (Chunk 단위)** |
| **신뢰성 보장** | 완전 신뢰성 (ACK/재전송) | 비신뢰성 (손실 무시) | **완전 신뢰성 / 부분 신뢰성(PR-SCTP)**|
| **다중 스트림** | 미지원 (단일 스트림) | 미지원 | **지원 (HOL 블로킹 방지)** |
| **멀티호밍 지원** | 불가 (단일 IP 쌍 바인딩) | 불가 | **완벽 지원 (복수 IP 자동 절체)** |
| **연결 수립 방식** | 3-Way Handshake (SYN Flood 취약)| 없음 | **4-Way Handshake (Cookie 방어)** |

## Ⅴ. SCTP(Stream Control Transmission Protocol)의 한계와 방안

| 한계 | 방안 |
|---|---|
| TCP/UDP에만 최적화된 기존 상용 NAT 라우터 및 레거시 방화벽에서 SCTP 프로토콜(IP 프로토콜 번호 132) 패킷을 미인식하여 임의 폐기 | 레거시 NAT 구간 통과를 위해 UDP 캡슐화(RFC 6951, SCTP-over-UDP) 적용 또는 에지 프록시 게이트웨이 배치 |
| 멀티호밍(Multi-homing) 환경에서 기본 경로(Primary Path) 장애 감지 및 보조 경로(Secondary Path) 절체 시 하트비트 타임아웃 지연(수 초)으로 인한 순간 단절 | 하트비트 주기(HB.Interval) 및 재전송 임계값(Path.Max.Retrans) 튜닝과 BFD(Bidirectional Forwarding Detection) 연동 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
WebRTC 기반 대화형 멀티미디어 시스템 구축 시, 음성/영상 미디어는 UDP 기반 SRTP로 전송하고 채팅·파일 공유·게임 입력 제어 등 신뢰성 데이터는 브라우저 내장 SCTP 데이터 채널(Data Channel)을 활용하되, `maxRetransmits=0` 옵션(PR-SCTP)을 통해 실시간성 우선 데이터의 불필요한 재전송을 선별 차단.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ SCTP 4-Way Handshake를 통한 SYN Flooding 공격 원천 방어 ]            │
│                                                                        │
│   [ 클라이언트 ]                                       [ 서버 ]        │
│        │                                                  │            │
│        ├─── 1. INIT (클라이언트 난수, IP 목록 전송) ────►│            │
│        │                                                  ├─► TCB 생성 │
│        │                                                  │   하지 않음│
│        │                                                  │  (메모리 0)│
│        │◄── 2. INIT-ACK (암호화 State Cookie 동봉 회신) ──┤            │
│        │                                                               │
│        ├─── 3. COOKIE-ECHO (수신받은 State Cookie 반환) ─►│            │
│        │                                                  ├─► 쿠키 서명│
│        │                                                  │   검증 통과│
│        │                                                  │   비로소   │
│        │◄── 4. COOKIE-ACK (연결 확정 및 데이터 전송 시작) ┤   TCB 할당 │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 청크 유형 | 기능 분류 | 핵심 파라미터 |
|---|---|---|
| **INIT / INIT-ACK** | 연결 수립 제어 | Initiator IP 목록, Outbound/Inbound 스트림 수, Cookie |
| **DATA 청크** | 사용자 페이로드 전송 | TSN(Transmission Sequence No), Stream ID, SSN |
| **SACK 청크** | 수신 누적/선택 확인 | Cumulative TSN Ack, Gap Ack Blocks |
| **HEARTBEAT** | 보조 경로 생존 확인 | Heartbeat Information, 송수신 타임스탬프 |

## 출제 이력과 검증 출처

- IETF RFC 4960: Stream Control Transmission Protocol
- IETF RFC 6951: UDP Encapsulation of Stream Control Transmission Protocol (SCTP)
- IETF RFC 8831: WebRTC Data Channels

## 연결 토픽

- 상위 토픽: [017 OSI 7 계층](./017_osi_7_layer.md)
- 연관 토픽: [007 TCP 혼잡 제어](./007_tcp_congestion_control.md), [036 WebRTC](./036_webrtc.md)
