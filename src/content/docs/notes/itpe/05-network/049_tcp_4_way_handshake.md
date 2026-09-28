---
title: "4-way handshake"
author: "Antigravity"
date: "2026-09-24T21:25:00+09:00"
tags:
  - "notes-network"
sidebar:
  label: "049. 4-way handshake"
  badge:
    text: "서브"
    variant: note
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 핵심 개념 → **TCP 4-way handshake**

## 30초 인출

- 본질: **TCP 4-way handshake** : 전이중(Full-Duplex) 가상 회선의 양방향 데이터 송수신을 안전하고 독립적으로 종료하기 위한 4단계 연결 해제 절차
- 메커니즘: 능동 종료측(Active Closer)의 FIN 전송 ──► 수동 종료측의 ACK 및 잔여 데이터 송신 ──► 수동 종료측의 FIN 전송 ──► 능동 종료측의 최종 ACK 회신 및 2MSL TIME_WAIT 대기
- 통찰: 전이중 연결의 독립적 반폐쇄(Half-Close)를 보장하고 지연 세그먼트 혼입을 방지하기 위해 능동 종료측의 2MSL TIME_WAIT 대기와 수동 종료측의 CLOSE_WAIT 소켓 누수 방지 튜닝이 필수적임.

<details>
<summary>핵심 용어</summary>

- **Half-Close (반폐쇄)** : 한쪽 방향의 데이터 송신은 종료되었으나, 반대 방향으로부터의 데이터 수신은 계속 유지되는 TCP 연결 상태
- **TIME_WAIT** : 능동 종료측이 최종 ACK를 보낸 후 네트워크상의 잔존 패킷 혼입 방지 및 상대방 FIN 재전송에 대응하기 위해 2MSL 동안 대기하는 상태
- **CLOSE_WAIT** : 수동 종료측이 상대의 FIN에 대해 ACK를 보낸 후, 자체 애플리케이션의 close() 시스템 콜 호출을 기다리는 대기 상태
- **MSL (Maximum Segment Lifetime)** : IP 패킷(세그먼트)이 네트워크에 살아있을 수 있는 최대 수명 시간 (기본값 약 60초)
- **SO_LINGER** : 소켓 닫기 시 버퍼에 남은 잔여 데이터의 처리 방식 및 대기 시간을 제어하는 소켓 레벨 옵션

</details>

---

## 2~4교시 예상문제 (25점)

> TCP 프로토콜의 정상 연결 종료 절차인 4-way handshake의 동작 과정, 상태 천이(FSM), TIME_WAIT 및 CLOSE_WAIT의 발생 원인과 대규모 트래픽 환경에서의 성능 장애 해결 방안을 설명하시오. (기출·제133회 1교시 변형)

---

## 2~4교시 25점 답안

## Ⅰ. TCP 4-way handshake의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | TCP 가상 회선에 연결된 양단 호스트가 각 방향의 데이터 송신 완료를 FIN과 ACK 제어 세그먼트를 통해 개별 확인하고 연결을 우아하게 종료(Graceful Close)하는 4단계 핸드셰이크 절차 |
| 목적 | 송수신 버퍼에 남아있는 잔여 데이터의 완전한 유실 없는 전달 보장, 전이중 통신의 독립적 연결 해제 및 이전 연결의 지연 패킷에 의한 신규 연결 오염 차단 |

## Ⅱ. TCP 4-way handshake의 특징

| 특징 | 상세 내용 |
|---|---|
| 독립적 양방향 종료 | TCP는 양방향 통신이므로 한쪽이 송신을 종료해도 상대방은 남은 데이터를 모두 보낼 때까지 단방향 수신 유지 |
| Half-Close 메커니즘 | 클라이언트가 FIN 송신 후 FIN_WAIT_2 상태에서 서버가 보내는 최종 응답 데이터를 끝까지 안전하게 수신 가능 |
| 2MSL TIME_WAIT 안전 대기| 능동 종료측은 최종 ACK 손실 시 상대의 FIN 재전송을 처리하고 망 내 미아 패킷 소멸을 위해 2*MSL 동안 소켓 유지 |
| 상태 비대칭성 | 먼저 close()를 호출한 쪽(능동 종료)은 TIME_WAIT을 거치고, 나중에 닫는 쪽(수동 종료)은 LAST_ACK를 거쳐 즉시 종료 |

## Ⅲ. 4-way handshake 절차 및 상태 천이 체계

**양단 호스트 간 4-way handshake 단계별 메시지 교환 및 소켓 FSM 상태도**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ TCP 4-way handshake 연결 종료 절차 ]          │
│                                                                        │
│   [ Client : 능동 종료측 (Active Closer) ]    [ Server : 수동 종료측 (Passive) ]│
│   (ESTABLISHED)                               (ESTABLISHED)            │
│         │                                           │                  │
│         ├──── 1. FIN (Seq=u, Ack=v) ───────────────►│ (수신: close() 감지)│
│   (FIN_WAIT_1)                                      ▼                  │
│         │                                     (CLOSE_WAIT)             │
│         │◄─── 2. ACK (Seq=v, Ack=u+1) ──────────────┤ (Half-Close 상태) │
│         ▼                                           │ (잔여 데이터 전송)│
│   (FIN_WAIT_2)                                      │                  │
│         │                                           ▼ 애플리케이션 close()│
│         │◄─── 3. FIN (Seq=w, Ack=u+1) ──────────────┤                  │
│         ▼                                     (LAST_ACK)               │
│   (TIME_WAIT)                                       │                  │
│         ├─── 4. ACK (Seq=u+1, Ack=w+1) ────────────►│ (ACK 수신 즉시)  │
│         │                                           ▼                  │
│         │ [ 2 * MSL 타이머 대기 (약 120초) ]       (CLOSED)            │
│         ▼                                                              │
│     (CLOSED)                                                           │
└────────────────────────────────────────────────────────────────────────┘
```

| 단계 | 발신측 | 수신측 | 플래그 및 시퀀스 | 핵심 동작 및 상태 전이 |
|---|---|---|---|---|
| **1단계** | 클라이언트 | 서버 | `FIN=1, Seq=u` | 클라이언트가 close() 호출, FIN 전송 후 `FIN_WAIT_1` 상태 진입 |
| **2단계** | 서버 | 클라이언트 | `ACK=1, Ack=u+1` | 서버가 FIN 수신 확인 응답, 서버는 `CLOSE_WAIT`, 클라이언트는 `FIN_WAIT_2` 진입 |
| **3단계** | 서버 | 클라이언트 | `FIN=1, Seq=w` | 서버 앱의 잔여 데이터 송신 완료 후 close() 호출, `LAST_ACK` 상태 진입 |
| **4단계** | 클라이언트 | 서버 | `ACK=1, Ack=w+1` | 클라이언트가 최종 ACK 전송 후 `TIME_WAIT` 진입, 서버는 ACK 수신 즉시 `CLOSED` |

## Ⅳ. TCP 3-way handshake와 4-way handshake 비교

| 비교 항목 | 3-way handshake (연결 수립) | 4-way handshake (연결 종료) |
|---|---|---|
| **수행 목적** | 양단 간 시퀀스 번호(ISN) 동기화 및 가상 회선 개설 | **양방향 송신 채널의 안전한 개별 폐쇄 및 자원 회수** |
| **교환 세그먼트 수**| 3개 (SYN ──► SYN+ACK ──► ACK) | **4개 (FIN ──► ACK ──► FIN ──► ACK)** |
| **합침(Piggyback) 여부**| 서버의 SYN과 ACK가 **단일 세그먼트로 합쳐져 전송**| **서버의 잔여 데이터 송신으로 ACK와 FIN이 분리 전송**|
| **핵심 제어 플래그**| SYN (Synchronize Sequence Number) | **FIN (Finish No more data from sender)** |
| **주요 장애 및 위험**| SYN Flooding 공격으로 인한 백로그 큐 고갈 | **TIME_WAIT 누적으로 인한 포트 고갈, CLOSE_WAIT 누수**|
| **최종 대기 상태** | ESTABLISHED 상태로 즉시 데이터 전송 시작 | **능동 종료측의 2MSL(TIME_WAIT) 안전 대기 후 종료** |

## Ⅴ. TCP 4-way handshake의 한계와 방안

| 한계 | 방안 |
|---|---|
| 단시간 대량의 단기 연결(Short-lived Connection) 생성·종료 시 클라이언트/프록시 측의 TIME_WAIT 소켓 급증으로 인한 임시 포트(Ephemeral Port) 고갈(EADDRNOTAVAIL) | HTTP Keep-Alive 및 커넥션 풀링(Connection Pooling) 필수 적용, 리눅스 커널의 `net.ipv4.tcp_tw_reuse=1` 활성화 및 로컬 포트 범위(`net.ipv4.ip_local_port_range`) 대폭 확장 |
| 수동 종료측(서버) 애플리케이션의 소켓 close() 호출 누락 또는 스레드 블로킹으로 인한 CLOSE_WAIT 소켓 영구 누적 및 파일 디스크립터(FD) 고갈 시스템 다운 | 애플리케이션 소켓 통신부에 명시적 소켓 자원 해제(try-with-resources) 구현, 네트워크 Read/Write 타임아웃 강제 설정 및 CLOSE_WAIT 임계치 초과 시 알람 체계 수립 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
대규모 API 게이트웨이 및 역방향 프록시(Nginx, Envoy) 서버 운영 시, 능동 종료 주체가 백엔드 WAS가 되지 않도록 클라이언트와 프록시 간, 프록시와 WAS 간 모든 통신 구간에 HTTP Keep-Alive 커넥션 풀을 구성하고, 대량 TIME_WAIT 소켓이 발생하는 서버에는 `tcp_max_tw_buckets`를 적정 수준으로 상향 조정하여 비정상 RST 전파를 방지.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ TIME_WAIT 소켓의 2MSL 대기가 필요한 2가지 결정적 이유 ]             │
│                                                                        │
│ 1. [ 최종 ACK 분실 시 수동 종료측의 고착 방지 ]                        │
│    클라이언트의 4단계 최종 ACK가 망에서 분실될 경우,                    │
│    서버는 LAST_ACK 상태에서 타임아웃 후 3단계 FIN을 재전송함           │
│    클라이언트가 TIME_WAIT 상태를 유지해야 재전송된 FIN에 다시 ACK 회신 가능│
│                                                                        │
│ 2. [ 이전 연결의 지연 패킷(Ghost Packet) 혼입 방지 ]                    │
│    망 내부 라우터에 갇혀있던 이전 연결의 지연 데이터 세그먼트가          │
│    동일한 포트로 새로 개설된 차기 TCP 연결에 유입되어 데이터를 왜곡하는  │
│    현상을 방지하기 위해 최대 수명(2MSL) 동안 해당 포트 재사용을 동결   │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 소켓 비정상 상태 | 발생 위치 | 원인 및 현상 | 엔지니어링 조치 방안 |
|---|---|---|---|
| **TIME_WAIT 폭증** | 능동 종료측 (Client/Proxy) | 짧은 연결 반복으로 로컬 포트 고갈 | Keep-Alive 풀링, tcp_tw_reuse 활성화 |
| **CLOSE_WAIT 누적**| 수동 종료측 (Server/WAS) | 앱에서 close() 미호출 (버그/행) | 소켓 타임아웃 설정, 코드 리소스 누수 패치 |
| **FIN_WAIT_2 고착**| 능동 종료측 (Client) | 상대방이 FIN을 보내지 않고 무응답 | tcp_fin_timeout (디폴트 60초) 단축 조정 |

## 출제 이력과 검증 출처

- 정보관리기술사 제133회 1교시 13번: TCP 프로토콜의 3-way handshake와 4-way handshake를 설명하시오.
- IETF RFC 793: Transmission Control Protocol - Functional Specification
- IETF RFC 9293: Transmission Control Protocol (TCP) Specification (2022)

## 연결 토픽

- 상위 토픽: [017 OSI 7 계층](./017_osi_7_layer.md)
- 연관 토픽: [052 TCP 3-way handshake](./052_tcp_3_way_handshake.md), [007 TCP 혼잡 제어](./007_tcp_congestion_control.md)
