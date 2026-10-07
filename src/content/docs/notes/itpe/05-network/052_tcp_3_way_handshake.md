---
title: "3-way handshake"
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

## Ⅰ. TCP 3-Way Handshake의 개요

- 개념 : TCP(Transmission Control Protocol)/IP(Internet Protocol) 통신을 시작하기 전, 신뢰성 있는 가상 양방향 연결 회선을 수립하기 위해 클라이언트와 서버가 3단계에 걸쳐 제어 플래그(SYN(Synchronize), ACK(Acknowledgment))와 시퀀스 번호(ISN)를 상호 교환 및 동기화하는 절차.
- 배경 및 필요성 : 비신뢰적이고 패킷 유실·역전이 상존하는 IP 네트워크 환경에서 패킷의 전송 순서를 복원하고, 중복 수신을 방지하며 전송률을 조절하기 위한 사전 상태 동기화 필수.
- 핵심 목적 : 송수신 양단의 **초기 시퀀스 번호(ISN)** 안전 동기화, **수신 버퍼 윈도우 크기(Window Size)** 및 통신 옵션(MSS, SACK, 타임스탬프) 사전 협상.

## Ⅱ. TCP 3-Way Handshake의 핵심 아키텍처 및 동작 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ TCP 3-Way Handshake 연결 수립 절차 ]               │
│                                                                        │
│        Client                                        Server            │
│       [ CLOSED ]                                    [ LISTEN ]         │
│           │                                              │             │
│           │  1. SYN (seq = x, MSS, WScale, SACK-Perm)    │             │
│           ├─────────────────────────────────────────────►│             │
│    [ SYN_SENT ]                                          │             │
│           │                                       [ SYN_RCVD ]         │
│           │  2. SYN + ACK (seq = y, ack = x + 1)         │             │
│           │◄─────────────────────────────────────────────┤             │
│   [ ESTABLISHED ]                                        │             │
│           │                                              │             │
│           │  3. ACK (seq = x + 1, ack = y + 1)           │             │
│           ├─────────────────────────────────────────────►│             │
│           │     (3단계 ACK에 첫 데이터 피기백 가능)       │             │
│           │                                       [ ESTABLISHED ]      │
│           ▼                                              ▼             │
│   [ 양방향 전이중 데이터 전송 시작 (Data Stream Read/Write) ]           │
└────────────────────────────────────────────────────────────────────────┘
```

- **Step 1 (SYN 송신)** : 클라이언트가 무작위 의사 난수로 생성된 클라이언트 초기 시퀀스 번호(ISN_c = x)를 담은 SYN 세그먼트를 서버로 송신하고 SYN_SENT 상태로 전이.
- **Step 2 (SYN+ACK 응답)** : 서버는 클라이언트의 ISN을 확인하고, 자신의 초기 시퀀스 번호(ISN_s = y)와 함께 클라이언트의 번호를 1 증가시킨 승인 번호(ACK = x + 1)를 회신하며 SYN_RCVD 상태 진입.
- **Step 3 (ACK 최종 승인)** : 클라이언트는 서버의 ISN을 확인하고 1 증가시킨 승인 번호(ACK = y + 1)를 서버로 전송하며 ESTABLISHED 상태로 즉시 전이. 서버는 이 ACK를 수신하는 순간 ESTABLISHED로 전환.

## Ⅲ. 세부 협상 옵션 및 보안 파라미터 분석

| 핵심 파라미터 | RFC(Request for Comments) 표준 | 기능 및 역할 | 성능 및 보안 영향도 |
|---|---|---|---|
| **ISN (초기 일련번호)** | RFC 793, 6528 | 패킷 순서 정렬 및 중복 패킷 제거의 기준선 | 암호학적 의사난수 사용 (시퀀스 예측 공격 방어) |
| **MSS (최대 세그먼트 크기)** | RFC 879 | IP 단편화(Fragmentation)를 막기 위한 L4 페이로드 크기 | MTU - 40바이트 (일반 이더넷 환경 1,460 Byte) |
| **윈도우 스케일 (Window Scale)** | RFC 7323 | 기존 16비트(64KB) 수신 윈도우 한계를 최대 1GB로 확장 | BDP가 큰 고속 장거리 통신망 전송률 극대화 |
| **SACK Permitted** | RFC 2018 | 유실된 특정 세그먼트만을 선택적으로 재전송 허용 | 불필요한 전체 재전송 방지 및 혼잡 완화 |
| **타임스탬프 (Timestamps)** | RFC 7323 | RTT(Round-Trip Time) 정밀 측정 및 PAWS(시퀀스 랩어라운드 방지) | 기가비트급 고속망에서 시퀀스 재사용 오류 방지 |

- **TCP 백로그 큐 (Backlog Queue)** : 커널은 SYN_RCVD 상태의 미완결 연결을 담는 `SYN Queue`와 Handshake가 완료되어 `accept()`를 기다리는 `Accept Queue`를 이원화 관리.

## Ⅳ. TCP 3-Way Handshake의 한계점·문제점 및 해결 방안

- SYN Flooding 분산 서비스 거부(DDoS, Distributed Denial of Service) 공격에 의한 백로그 큐 고갈 :
  - 한계점 : 공격자가 위조된 IP로 수많은 SYN 패킷만 전송하고 최종 ACK를 보내지 않아, 서버의 SYN Queue가 가득 차 신규 정상 접속 차단.
  - 해결 방안 : `TCP SYN Cookie` 활성화(상태 저장 없이 ISN에 암호학적 해시를 인코딩하여 Step 3 수신 시 복원 검증), SYN 캐시 메모리 증설 및 방화벽 SYN Proxy 기능 적용.
- 1 RTT 왕복 지연 시간 발생에 따른 단기 트랜잭션 성능 저하 :
  - 한계점 : TLS(Transport Layer Security) 1.3 핸드셰이크까지 결합 시 최초 데이터 전송 전 수회의 RTT가 소요되어 모바일 웹 로딩 지연.
  - 해결 방안 : `TCP Fast Open (TFO, RFC 7413)` 도입(이전 접속 시 발급받은 쿠키를 이용해 1단계 SYN 패킷에 HTTP(Hypertext Transfer Protocol) 요청 데이터를 직접 포함시켜 0-RTT 전송 달성).

## Ⅴ. TCP 3-Way Handshake 적용 및 발전을 위한 기술사적 제언

- 차세대 QUIC / HTTP/3 프로토콜로의 점진적 전환 : 연결 수립에 최소 1 RTT, TLS 암호화에 추가 RTT가 소모되는 TCP의 본질적 한계를 극복하기 위해, 최초 접속 시에도 1-RTT, 재접속 시 0-RTT로 연결과 암호화를 동시 완결하는 QUIC 도입 가속.
- OS(Operating System) 커널 SYN 파라미터 최적화 가이드라인 : 대규모 트래픽을 수용하는 웹/WAS(Web Application Server) 서버의 경우 `net.ipv4.tcp_syncookies = 1`, `net.ipv4.tcp_max_syn_backlog = 8192 이상`, `net.core.somaxconn = 4096 이상`으로 튜닝 표준 수립.
- 로드밸런서 레벨의 L4/L7 오프로딩 아키텍처 : 클라이언트와 백엔드 서버 간 직접 Handshake를 맺지 않고, 고성능 리버스 프록시/ADC 장비가 클라이언트 세션을 종단하고 백엔드와는 커넥션 풀을 영구 유지하여 백엔드 오버헤드 최소화.
