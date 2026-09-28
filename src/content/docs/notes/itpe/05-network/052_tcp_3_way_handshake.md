---
title: "3-way handshake"
author: "Antigravity"
date: "2026-09-24T21:25:00+09:00"
tags:
  - "notes-network"
sidebar:
  label: "052. 3-way handshake"
  badge:
    text: "서브"
    variant: note
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 전송 계층 프로토콜 → **TCP 3-way handshake**

## 30초 인출

- 본질: **TCP 3-way handshake** : TCP(Transmission Control Protocol)에서 양 종단(End-to-End) 간에 신뢰성 있는 가상 전이중 회선을 개설하고 양측의 초기 순서 번호(ISN)를 동기화하는 3단계 연결 수립 절차
- 메커니즘: Client SYN(seq=x) → Server SYN+ACK(seq=y, ack=x+1) → Client ACK(ack=y+1) 교환을 통해 양방향 시퀀스 번호 및 수신 윈도우 크기 확정
- 통찰: 단순 3단계 패킷 교환에 그치지 않고 SYN Backlog 자원 고갈을 유발하는 SYN Flooding 공격 방어를 위한 SYN Cookie 기법과 초기 1-RTT 지연 단축을 위한 TCP Fast Open 연계 필수

<details>
<summary>핵심 용어</summary>

- **ISN (Initial Sequence Number)** : 세션 개시 시 이전 잔존 패킷과의 충돌을 방지하기 위해 4µs 클록과 암호학적 해시를 결합해 무작위로 생성하는 초기 순서 번호
- **SYN Backlog (반개방 큐)** : 서버가 SYN 수신 후 SYN+ACK를 회신하고 최종 ACK를 대기하는 `SYN_RCVD` 상태의 연결 요청들을 보관하는 커널 큐
- **Accept Queue (완료 큐)** : 3-way handshake가 완료되어 `ESTABLISHED` 상태로 전이된 소켓들이 애플리케이션의 `accept()` 시스템 콜 호출을 대기하는 큐
- **SYN Cookie** : SYN Backlog에 상태 메모리(TCB)를 즉시 할당하지 않고, 클라이언트 IP/포트/시간값을 해싱하여 서버 ISN에 부호화하는 DoS 방어 기법
- **TCP Fast Open (TFO)** : 최초 핸드셰이크 시 발급받은 암호화 쿠키를 이용해 후속 재연결 시 SYN 패킷에 직접 데이터를 동봉 전송하는 0-RTT 연결 가속 기술 (RFC 7413)

</details>

---

## 2~4교시 예상문제 (25점)

> TCP 3-way handshake의 연결 수립 메커니즘과 유한 상태 기계(FSM) 전이 과정을 설명하고, SYN Flooding 공격의 원리와 SYN Cookie 방어 메커니즘, 그리고 지연 단축을 위한 TCP Fast Open을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. TCP 3-way handshake의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | TCP 전송 계층에서 통신 개시 전 송수신 양단 간에 가상 회선을 수립하고, 초기 순서 번호(ISN)와 윈도우 크기를 동기화하는 3단계 세션 연결 제어 절차 |
| 목적 | 양방향 전이중(Full-Duplex) 데이터 전송 신뢰성 보장, 과거 세션의 지연 중복 세그먼트 수신 오류 차단, 송수신 버퍼 용량 정합성 확보 |

## Ⅱ. TCP 3-way handshake의 특징 및 제어 플래그

| 제어 항목 | 주요 특징 및 기능 명세 |
|---|---|
| **양방향 신뢰성 검증** | Client→Server, Server→Client 양방향의 송신 및 수신 경로가 모두 정상 동작함을 3개 세그먼트만으로 완벽 검증 |
| **ISN 난수화 생성** | 고정 번호(0)가 아닌 4마이크로초 단위 타이머 클록과 MD5/SHA 해시 기반 난수로 생성하여 세션 하이재킹 공격 원천 차단 |
| **SYN 플래그 (Synchronize)** | 연결 개시 요청을 알리는 1비트 제어 플래그; 시퀀스 번호 공간 1을 소비하여 ACK 회신 유도 |
| **ACK 플래그 (Acknowledgment)**| 직전 상대방 세그먼트의 정상 수신을 확인하고 다음 기대 수신 번호(`Next Expected Seq = Seq + 1`)를 통보 |
| **옵션 파라미터 교환** | MSS(Maximum Segment Size), Window Scale(대역폭 지연 곱 대응), SACK 허용 여부 등 전송 제어 파라미터 사전 협상 |

## Ⅲ. TCP 3-way handshake 연결 수립 절차 및 상태 전이 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│               [ TCP 3-way handshake 상태 전이 및 메시지 교환 ]         │
│                                                                        │
│      [ Client ]                                       [ Server ]       │
│      (CLOSED)                                          (LISTEN)        │
│          │                                                │            │
│          │ 1. [SYN, Seq=x]                                │            │
│          │    (mss=1460, sackOK, wscale=7)                │            │
│          ├───────────────────────────────────────────────►│            │
│     (SYN_SENT)                                            │ (SYN_RCVD) │
│          │                                                │ [SYN Queue]│
│          │ 2. [SYN-ACK, Seq=y, Ack=x+1]                   │            │
│          │    (mss=1460, sackOK, wscale=7)                │            │
│          │◄───────────────────────────────────────────────┤            │
│    (ESTABLISHED)                                          │            │
│          │ 3. [ACK, Seq=x+1, Ack=y+1]                     │            │
│          │    (순수 제어 ACK는 Seq 번호 소모 없음)        │            │
│          ├───────────────────────────────────────────────►│            │
│          │                                          (ESTABLISHED)      │
│          │                                          [Accept Queue]     │
│          │ === 양방향 전이중 데이터 스트림 전송 개시 === │            │
└────────────────────────────────────────────────────────────────────────┘
```

| 교환 단계 | 송신 세그먼트 | 양 종단 상태 변화 | 핵심 수행 작업 |
|---|---|---|---|
| **1단계: 연결 요청** | SYN (Seq=x) | Client: CLOSED → SYN_SENT<br/>Server: LISTEN 유지 | Client가 임의의 ISN(x)을 부여하여 연결 요청; Server는 SYN Backlog에 반개방 상태 기록 |
| **2단계: 수락 및 응답**| SYN+ACK (Seq=y, Ack=x+1) | Client: SYN_SENT 대기<br/>Server: LISTEN → SYN_RCVD | Server가 x를 수신했음을 통보(Ack=x+1)하고, 자신의 독자적 ISN(y)을 실어 동시 응답 |
| **3단계: 최종 확인** | ACK (Seq=x+1, Ack=y+1) | Client: SYN_SENT → ESTABLISHED<br/>Server: SYN_RCVD → ESTABLISHED | Client가 y를 확인(Ack=y+1)하여 회신; 소켓은 Accept Queue로 이관되어 `accept()` 대기 |

## Ⅳ. TCP 3-way handshake(연결 수립) vs 4-way handshake(연결 해제) 비교

| 비교 항목 | 3-way handshake (연결 수립) | 4-way handshake (연결 해제) |
|---|---|---|
| **수행 목적** | 통신 개시를 위한 가상 회선 수립 및 ISN 동기화 | 데이터 송수신 완료 후 전이중 가상 회선의 안전한 종료 |
| **교환 메시지** | SYN → SYN+ACK → ACK (총 3단계) | FIN → ACK → FIN → ACK (총 4단계) |
| **메시지 통합 여부** | Server의 ACK와 SYN이 단일 세그먼트로 통합 결합 | Server 잔여 데이터 송신 완료를 기다려야 하므로 분리 전송 (Half-Close) |
| **주요 종료 상태** | 양 종단 모두 `ESTABLISHED` 상태 도달 | 능동 종료자는 `TIME_WAIT`(2MSL 대기) 후 `CLOSED` 전이 |
| **주요 보안/장애 취약점**| SYN Flooding (SYN Backlog 고갈 공격) | TIME_WAIT 누적에 따른 가용 로컬 포트 고갈(Port Exhaustion) |

## Ⅴ. TCP 3-way handshake의 한계와 방안

| 한계 | 방안 |
|---|---|
| 공격자가 스푸핑된 위조 IP로 대량의 SYN 세그먼트만 발송하고 최종 ACK를 유보하여 서버의 SYN Backlog 큐 메모리를 고갈시키는 SYN Flooding 공격 취약 | 커널 파라미터 `tcp_syncookies=1`을 설정하여 SYN Backlog에 TCB 메모리를 사전 할당하지 않고 클라이언트 IP/포트/타임스탬프와 서버 비밀키 해시로 ISN을 생성하며, 네트워크 앞단 방화벽의 TCP SYN Proxy 기능 연계 |
| 신규 연결 시마다 데이터 전송 전 반드시 1-RTT(왕복 지연 시간)가 소모되어 짧은 단발성 HTTP/HTTPS 요청의 첫 바이트 수신 시간(TTFB)이 구조적으로 지연 | 최초 핸드셰이크 시 암호화 TFO 쿠키를 발급받은 후, 후속 재연결 시 SYN 패킷 페이로드에 즉시 요청 데이터를 동봉하여 0-RTT 데이터 송수신을 구현하는 TCP Fast Open(RFC 7413) 기술 적용 |
| 최종 3단계 ACK 패킷이 네트워크 상에서 유실될 경우 클라이언트는 ESTABLISHED로 오인하여 데이터를 송신하나 서버는 재전송 SYN-ACK를 발송하며 상태 불일치 발생 | 서버의 SYN-ACK 지수 백오프(Exponential Backoff) 재전송 메커니즘을 점검하고, 데이터 수신 시 묵시적 ACK 처리가 가능하도록 커널 TCP 스택의 비정상 세션 타임아웃 정밀 튜닝 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
대규모 트래픽을 처리하는 웹 서버 및 API 게이트웨이 환경에서는 급격한 트래픽 유입 시 반개방 큐 오버플로로 정상 사용자가 드롭되는 현상을 차단하기 위해 리눅스 커널의 `net.ipv4.tcp_max_syn_backlog`와 `net.core.somaxconn` 파라미터를 충분히 증설하고, 로드밸런서(L4/L7) 전면에서 TCP SYN Proxy를 활성화하여 신뢰성이 입증된 유효 연결만 백엔드 서버 풀로 포워딩 권장

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│           [ SYN Flooding 방어를 위한 SYN Cookie 동작 아키텍처 ]         │
│                                                                        │
│   [공격자/클라이언트]                    [서버 커널 (SYN Cookie On)]  │
│          │                                         │                   │
│          │ 1. SYN (위조 IP, Seq=x)                 │                   │
│          ├────────────────────────────────────────►│                   │
│          │                                         │ TCB 메모리 미할당!│
│          │                                         │ ISN = Hash(IP,Port│
│          │ 2. SYN-ACK (Seq=Cookie, Ack=x+1)        │            Time,K)│
│          │◄────────────────────────────────────────┤                   │
│          │                                         │                   │
│          │ 3. ACK (Ack=Cookie+1) [정상 단말만 응답]│                   │
│          ├────────────────────────────────────────►│                   │
│          │                                         │ Cookie - 1 역검증 │
│          │                                         │ 해시 일치 시에만   │
│          │                                         │ 비로소 TCB 할당!  │
│          │                                         │ (Accept Queue 진입)│
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 연결 기술 | 연결 지연 (RTT) | DoS 취약점 및 보안성 | 커널/인프라 지원 요구사항 | 주 활용 분야 |
|---|---|---|---|---|
| **표준 TCP 3-Way** | 1 RTT (데이터 전송 전) | SYN Flood에 취약 (SYN Cookie 보완 필수) | 모든 OS 및 전송 장비 표준 지원 | 전통적 레거시 TCP 통신 전반 |
| **TCP Fast Open (TFO)**| 0 RTT (재연결 시) | 쿠키 기반 재생 공격(Replay Attack) 방어 필요 | 클라이언트/서버 커널 TFO 지원 필수 | 모바일 웹 브라우징, 검색 API |
| **QUIC / HTTP/3** | 0~1 RTT (TLS 1.3 내장) | UDP 기반 연결 ID로 DoS 완화 및 핸드셰이크 단축 | UDP 443 차단 방화벽 환경 우회 고려 필요 | 유튜브 스트리밍, 대규모 클라우드 |

## 출제 이력과 검증 출처

- 정보관리기술사 133회 1교시: TCP 프로토콜의 3-way handshake와 4-way handshake 비교 설명
- 컴퓨터시스템응용기술사 120회 1교시: TCP 연결 수립 및 제어 플래그 동작 원리
- RFC 9293: Transmission Control Protocol (TCP) Specification
- RFC 7413: TCP Fast Open

## 연결 토픽

- 상위 토픽: [017 OSI 7 계층](./017_osi_7_layer.md)
- 연관 토픽: [049 TCP 4-way handshake](./049_tcp_4_way_handshake.md), [048 통신 프로토콜 기본 요소](./048_protocol_elements.md)
