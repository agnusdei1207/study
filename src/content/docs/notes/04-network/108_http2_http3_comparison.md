---
sidebar:
  order: 108
  label: "108. HTTP/2•HTTP/3 비교"
  badge:
    text: "미출 · 50%"
    variant: note
title: "차세대 웹 전송 프로토콜 비교 : HTTP/2 vs HTTP/3"
date: "2026-09-07T14:00:00+09:00"
tags:
  - "notes-network"
weight: 108
extra:
  question_no: "108"
  source_status: "미출"
  source_history: ""
  priority: 50
  priority_note: "RFC 9113(HTTP/2 over TCP) vs RFC 9114(HTTP/3 over QUIC/UDP), HoL Blocking 해결, 0-RTT 및 QPACK"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **HTTP/2 (RFC 9113)**: 단일 TCP 상에서 바이너리 프레이밍과 HPACK 압축으로 스트림을 다중화한 웹 프로토콜.
- **HTTP/3 (RFC 9114)**: UDP 기반의 차세대 전송 계층 프로토콜인 QUIC(RFC 9000) 상에서 독립 스트림 다중화와 0-RTT를 지원하는 표준 웹 프로토콜.

</details>

- 정의/개념: 웹 통신의 지연시간을 단축하고 전송 효율을 대폭 향상하기 위해, 단일 TCP 상에서 바이너리 프레이밍으로 다중 스트림을 전송하는 **HTTP/2**와 UDP 기반 QUIC 위에서 독립 스트림과 0-RTT 연결을 구현한 **HTTP/3**를 하부 전송 계층과 HoL 블로킹 해소 관점에서 비교하는 **IETF 표준 웹 전송 프로토콜**
- 배경/필요성: HTTP/2의 단일 TCP 연결 구조에서 단 1개의 패킷 유실로도 모든 스트림이 일시 정지되는 **TCP 헤드오브라인 블로킹(HoL Blocking) 및 다단계 핸드셰이크 지연 발생**

#### 한줄 요약
- TCP HoL 블로킹을 해결하고 0-RTT 연결 수립과 연결 마이그레이션을 통해 무선망 전송 효율을 제고해야 한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **TCP Head-of-Line Blocking**: TCP의 순차 바이트 스트림 특성으로 인해 중간 패킷 1개가 유실되면 수신 버퍼 큐에서 무관한 다른 모든 HTTP 스트림의 처리가 중단되는 병목.
- **Connection ID (CID) Migration**: IP/Port 4-Tuple 대신 64비트 랜덤 연결 ID를 사용하여 Wi-Fi에서 LTE로 망 전환 시에도 재연결 없이 통신을 지속하는 기술.

</details>

- **독립 스트림**: 손실이 다른 스트림을 차단하지 않음
- **0-RTT·1-RTT**: QUIC에 TLS 1.3 통합
- **Connection ID**: IP 변경에도 연결 상태 유지

#### 한줄 요약
- HoL 블로킹 제거, 0-RTT/1-RTT 신속한 연결, Connection ID 기반 무단절 마이그레이션을 제공한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **HPACK vs QPACK**: 엄격한 단일 스트림 순차 압축(HPACK)과 다중 독립 스트림 간의 순서 역전을 지원하는 비동기 헤더 압축(QPACK).

</details>

```text
[HTTP/2 vs HTTP/3 스택]
  │
  ├─ [HTTP/2 스택 (RFC 9113)] ── HTTP/2 Stack
  │     ├─ [HTTP/2 프레이밍·HPACK] (동기식 HPACK 헤더 압축)
  │     ├─ [TLS 1.2 / 1.3 계층] (TCP+TLS 개별 핸드셰이크)
  │     └─ [TCP 계층] (TCP 신뢰성 제어·HoL 취약)
  └─ [HTTP/3 스택 (RFC 9114)] ── HTTP/3 Stack
        ├─ [HTTP/3 프레임·QPACK] (비동기 순서 역전 지원 QPACK)
        ├─ [QUIC 코어] (TLS 1.3 내장·통합 0-RTT)
        └─ [UDP 계층] (UDP 기반 독립 데이터그램)
```

- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| **전송 계층 프로토콜** | HTTP/2의 **TCP 신뢰성 제어** vs HTTP/3의 **UDP 기반 독립 데이터그램** |
| **연결 및 보안 계층** | HTTP/2의 **TCP+TLS 개별 핸드셰이크** vs HTTP/3의 **QUIC+TLS 1.3 통합 0-RTT** |
| **다중화 구현 방식** | HTTP/2의 **단일 연결 논리 분할** vs HTTP/3의 **QUIC 독립 스트림 분리** |
| **헤더 압축 알고리즘** | HTTP/2의 **동기식 HPACK** vs HTTP/3의 **비동기 순서 역전 지원 QPACK** |
| **연결 식별자** | HTTP/2의 **IP 4-Tuple 바인딩** vs HTTP/3의 **Connection ID 기반 마이그레이션** |

#### 한줄 요약
- QUIC이 전송·암호화·다중화를 한 계층에 합쳐 TCP와 TLS가 따로 치르던 핸드셰이크를 하나로 묶으므로, 계층 분리의 대가였던 연결 수립 왕복이 사라진다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **Alt-Svc (Alternative Services, RFC 7838)**: 서버가 HTTP/2 응답 헤더에 `Alt-Svc: h3=":443"`를 실어 보냄으로써 클라이언트에게 HTTP/3 지원을 알리는 광고 메커니즘.

</details>

```text
[HTTP/3 전환·전송 경로] (진행 ①→⑤, 브라우저 요청에서 진입, QUIC 성립 시 멀티스트림 전송·UDP 차단 시 HTTP/2 폴백)
  │
  ├─ [HTTP/2 최초 접속] (① 기존 TCP 연결로 서버에 접속해 응답 수신)
  │
  ├─ [Alt-Svc 광고 수신] (② 응답 헤더의 Alt-Svc 지시자로 HTTP/3 지원 확인)
  │
  ├─ [QUIC 1-RTT 연결] (③ UDP 443 관통 여부를 판정, 차단 시 HTTP/2 폴백으로 종료)
  │
  ├─ [독립 스트림 병렬 요청] (④ QUIC 성립 시 스트림별로 독립 병렬 요청)
  │
  └─ [선별적 재전송] (⑤ 손실 스트림만 재전송, 나머지 스트림은 진행 유지 후 웹 응답)
```

분기 결과: QUIC은 0-RTT와 스트림 단위 재전송이라는 성능 이점을 얻는 대가로 UDP 443 차단이라는 중간 장비 호환성 리스크를 떠안고, HTTP/2 폴백은 성능 상승분을 포기하는 대신 어떤 방화벽 환경에서도 도달성을 보장한다.

#### 한줄 요약
- UDP 차단 여부에서 QUIC 유지와 HTTP/2 폴백으로 갈리며, 성능 이점을 얻는 대신 중간 장비 호환성이라는 상시 불확실성을 떠안는다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **HTTP/1.1 vs HTTP/2 vs HTTP/3**: 직렬 전송, TCP 다중화, QUIC 기반 완전 독립 다중화.

</details>

| 비교 항목 | HTTP/1.1 | HTTP/2 | HTTP/3 |
|:---|:---|:---|:---|
| 기본 전송 프로토콜 | TCP 텍스트 | TCP 바이너리 | **QUIC·UDP** |
| 연결당 동시 요청 | 1개 | **다중 스트림** | **독립 다중 스트림** |
| 초기 연결 수립 지연 | 2-RTT | 2~3-RTT | **1-RTT·0-RTT** |
| 패킷 유실 시 영향 | 연결 블로킹 | **전체 스트림 HoL** | **해당 스트림만 영향** |
| 모바일 IP 변경 대응 | 재연결 | 재연결 | **CID 마이그레이션** |

#### 한줄 요약
- HTTP/1.1은 직렬 전송, HTTP/2는 TCP 다중화(HoL 잔존), HTTP/3는 QUIC 기반 독립적 초저지연 전송을 제공한다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **Happy Eyeballs v2 (RFC 8305)**: 클라이언트가 UDP 기반 QUIC과 TCP 기반 HTTP/2를 병렬로 동시 시도하여 더 빠르게 응답하는 연결을 선택하는 이중화 알고리즘.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| UDP 443 차단으로 접속 실패 | **Happy Eyeballs·HTTP/2 폴백** | 서비스 도달성 확보 |
| 0-RTT 요청 재생 공격 | **멱등 요청만 Early Data 허용** | 중복 실행 차단 |
| QUIC 암호화로 IPS 가시성 상실 | **엣지 복호화·L7 로깅** | 감사 추적성 확보 |
| UDP 처리로 서버 CPU 증가 | **UDP GSO·eBPF XDP** | 처리 부하 절감 |

#### 한줄 요약
- HTTP/2 폴백으로 가용성을 보장하고, 0-RTT 멱등 제어로 재생 공격을 방어하며, 엣지 복호화로 가시성을 확보한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **WebTransport**: HTTP/3의 QUIC 전송 계층을 활용하여 클라이언트와 서버 간에 단방향/양방향 스트림 및 신뢰성/비신뢰성 데이터그램을 초저지연으로 송수신하는 차세대 웹 통신 API.
- **UDP GSO (Generic Segmentation Offload)**: 사용자 공간에서 대용량 UDP 버퍼를 단일 시스템 콜로 전달하면 커널/NIC 하드웨어에서 MTU 크기로 패킷을 분할 송신하여 CPU 부하를 줄이는 기술.
- **eBPF XDP (eXpress Data Path)**: 리눅스 커널의 네트워크 드라이버 계층에서 패킷이 수신되는 즉시 초고속 필터링 및 리라우팅을 수행하는 인커널 가속 프레임워크.

</details>

- 유선 환경 중심의 TCP 웹 전송 시대를 마감하고 무선 모바일 및 분산 클라우드 환경에 최적화된 **차세대 글로벌 웹 통신 및 API 전송의 핵심 표준 프로토콜(IETF RFC 9114)**로 확고히 정립.
- 실시간 미디어 스트리밍(WebTransport) 및 CDN 엣지 컴퓨팅과의 결합으로 진화하는 가운데, 실무 HTTP/3 도입 시에는 **기업 방화벽의 UDP 443 포트 차단에 대비한 Happy Eyeballs(RFC 8305) 기반 HTTP/2 동적 폴백(Fallback) 보장**, **0-RTT(Early Data) 재생 공격(Replay Attack)을 방지하기 위한 GET 멱등 요청 한정 적용**, **UDP 커널 패킷 오버헤드를 해소하는 UDP GSO(Generic Segmentation Offload) 및 eBPF/XDP 커널 바이패스 가속**을 결합하여 차세대 웹 전송의 신뢰성과 성능을 확보해야 한다.

#### 한줄 요약
- HTTP/3는 QUIC 기반의 독립 스트림과 0-RTT 연결 및 Connection ID를 통해 무선망 웹 전송 성능을 혁신하는 표준 프로토콜로 체계적으로 전환해야 한다.
