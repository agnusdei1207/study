---
title: "4-way handshake"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. TCP 4-Way Handshake의 개요

- 개념 : TCP/IP 네트워크에서 데이터 전송을 완료한 두 종단(Client와 Server) 간에 설정된 연결 세션을 안전하고 정상적으로 종료(Graceful Teardown)하기 위해 수행하는 4단계 제어 패킷 교환 절차.
- 배경 및 필요성 : TCP는 전이중(Full-Duplex) 양방향 독립 연결을 지원하므로, 일방이 전송을 끝냈다고 즉시 세션을 강제 파기하면 반대 방향의 잔여 전송 데이터가 유실될 위험이 존재하여 독립적 반분(Half-Close) 종료 필요.
- 핵심 목적 : 송수신 양방향 버퍼에 남아있는 데이터의 완전한 전달 보장, 지연 패킷(Ghost Packet) 혼입 차단 및 운영체제 소켓 자원의 질서 정연한 반환.

## Ⅱ. TCP 4-Way Handshake의 핵심 아키텍처 및 동작 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ TCP 4-Way Handshake 세션 종료 절차 ]                │
│                                                                        │
│        Active Close (Client)                    Passive Close (Server) │
│       [ ESTABLISHED ]                              [ ESTABLISHED ]     │
│              │                                            │            │
│              │  1. FIN (seq=u)                           │            │
│              ├───────────────────────────────────────────►│            │
│       [ FIN_WAIT_1 ]                                      │            │
│              │                                            │            │
│              │                               [ CLOSE_WAIT ]            │
│              │  2. ACK (seq=v, ack=u+1)                   │ (잔여 전송)│
│              │◄───────────────────────────────────────────┤            │
│       [ FIN_WAIT_2 ]                                      │            │
│              │                                            ▼            │
│              │  3. FIN (seq=w, ack=u+1)                   │ (종료 완료)│
│              │◄───────────────────────────────────────────┤            │
│       [ TIME_WAIT ]                                  [ LAST_ACK ]      │
│              │                                            │            │
│              │  4. ACK (seq=u+1, ack=w+1)                 │            │
│              ├───────────────────────────────────────────►│            │
│              │                                      [ CLOSED ]         │
│         2MSL 대기                                                      │
│              ▼                                                         │
│          [ CLOSED ]                                                    │
└────────────────────────────────────────────────────────────────────────┘
```

- **Step 1 (FIN 송신)** : 연결 종료를 먼저 시작하는 주체(Active Closer)가 `close()` 또는 `shutdown()` 시스템 콜을 호출하여 FIN 플래그를 전송하고 FIN_WAIT_1 상태로 전이.
- **Step 2 (ACK 수신 및 Half-Close)** : 수신측(Passive Closer)은 FIN을 확인하고 ACK를 회신하며 CLOSE_WAIT 상태로 진입. 이 상태에서 상대방으로의 단방향 데이터 송신은 계속 가능.
- **Step 3 (서버 FIN 송신)** : Passive Closer 역시 송신할 모든 잔여 데이터를 전송 완료한 후 소켓을 닫으며 FIN을 전송하고 LAST_ACK 상태로 전이.
- **Step 4 (최종 ACK 및 TIME_WAIT)** : Active Closer는 서버의 FIN에 대한 최종 ACK를 전송하고 TIME_WAIT 상태로 대기하며, 서버는 ACK를 받고 즉시 CLOSED 상태로 종료.

## Ⅲ. 세부 상태 머신 및 핵심 요소 분석

| 상태 (State) | 주체 | 핵심 동작 및 의미 | 비정상 장기 잔류 시 위험 |
|---|---|---|---|
| **FIN_WAIT_1** | Active | 자신의 FIN을 보내고 상대방의 ACK를 기다리는 상태 | 네트워크 단절 시 소켓 자원 누수 |
| **CLOSE_WAIT** | Passive | 상대의 종료를 인지했으나 애플리케이션이 소켓을 미닫은 상태 | 애플리케이션 로직 버그로 소켓 고갈 |
| **FIN_WAIT_2** | Active | 자신의 종료 요청에 대한 ACK를 받고 상대방의 FIN을 대기 | 서버 미응답 시 좀비 소켓 잔류 |
| **LAST_ACK** | Passive | 자신의 FIN을 송신하고 최종 ACK를 대기하는 상태 | 네트워크 유실 시 반복 재전송 유발 |
| **TIME_WAIT** | Active | 최종 ACK를 전송한 후 지연 패킷 소멸을 위해 2MSL 동안 대기 | 고부하 서버의 로컬 포트 고갈 |

- TIME_WAIT의 2대 존재 목적 :
  1. 수신측이 최종 ACK를 유실했을 경우, 재전송된 상대방의 FIN을 수신하여 올바른 재 ACK를 보내주기 위함.
  2. 네트워크 내에 잔류하던 이전 연결의 지연 패킷(Stray Packet)이 향후 동일 5-Tuple로 새로 맺어진 연결에 혼입되는 데이터 오염 원천 차단.
- **2MSL (Maximum Segment Lifetime)** : RFC 793 기준 패킷이 네트워크 상에 생존할 수 있는 최대 시간의 2배를 대기.

## Ⅳ. 주요 장애 한계점 및 커널 엔지니어링 해결 방안

- CLOSE_WAIT 소켓 누수(Leak)로 인한 프로세스 파일 디스크립터 고갈 :
  - 한계점 : 백엔드 애플리케이션에서 네트워크 예외 발생 시 `socket.close()`를 누락하여 CLOSE_WAIT 상태가 지속 누적되어 서비스 거부 발생.
  - 해결 방안 : 애플리케이션 예외 블록 내 확실한 소켓 종료 보장, 커널 레벨 TCP Keepalive 설정 및 타임아웃 강제 회수 로직 구축.
- 고빈도 단기 연결 환경에서의 TIME_WAIT 포트 고갈(Port Exhaustion) :
  - 한계점 : 마이크로서비스 간 HTTP/1.1 단발 호출 급증 시 단말/프록시 측에 수만 개의 TIME_WAIT 소켓이 누적되어 신규 아웃바운드 포트 바인딩 실패.
  - 해결 방안 : `tcp_tw_reuse = 1` 활성화(안전한 타임스탬프 기반 재사용), 커널 로컬 포트 대역(`ip_local_port_range`) 확대, HTTP Keep-Alive 및 커넥션 풀링(Connection Pooling) 필수화.

## Ⅴ. TCP 4-Way Handshake 적용 및 발전을 위한 기술사적 제언

- 모던 네트워크의 전송 프로토콜 전환 검토 : 핸드셰이크 왕복 지연과 TIME_WAIT 오버헤드가 구조적으로 발생하는 TCP 대신, UDP 기반으로 세션 식별자를 활용해 연결 수립/종료 오버헤드를 극소화한 HTTP/3(QUIC) 도입.
- Zero-Downtime 배포 시의 커넥션 드레이닝(Draining) : 무중단 배포 시 구 인스턴스에 즉각적 RST(강제 종료)를 날리지 않고, 정상 4-Way Handshake를 거치도록 로드밸런서의 Deregistration Delay를 적정 시간(30~60초) 유지.
- OS 커널 TCP 스택 튜닝의 거버넌스화 : 대규모 API 게이트웨이 및 리버스 프록시 서버에 대해 TIME_WAIT 재사용, 소켓 재활용 버퍼 크기, FIN 타임아웃(`tcp_fin_timeout = 15~30`) 표준 템플릿 운영.
