---
title: "SCTP(Stream Control Transmission Protocol)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. SCTP(Stream Control Transmission Protocol)의 개요

- **개념** : TCP의 신뢰성 있는 연결 지향 스트림 전송 특성과 UDP의 메시지 경계 보존(Message-oriented) 특성을 결합하고, 다중 홈(Multi-Homing) 및 다중 스트림(Multi-Streaming) 기능을 지원하여 회선 장애 시 무중단 세션 유지와 헤드오브라인 블로킹(HoL Blocking)을 방지하는 전송 계층(L4) 프로토콜(RFC 4960).
- **배경 및 필요성** : 통신 사업자망의 SS7 전화 신호(Signaling)를 IP 네트워크 상에서 무손실·무중단으로 전송(SIGTRAN)하기 위해 개발되었으며, 단일 IP 연결에 의존하는 TCP의 회선 단절 취약성과 단일 큐 블로킹 한계를 극복하기 위해 제정됨.
- **핵심 목적** : 통신 회선 물리적 장애 시 무중단 페일오버(Fault-Tolerant Multi-Homing), 다중 스트림 분리를 통한 HoL 블로킹 제거, 4-Way 핸드셰이크 쿠키 메커니즘을 통한 SYN 플러딩 서비스 거부 공격(DoS) 원천 차단.

## Ⅱ. SCTP(Stream Control Transmission Protocol)의 핵심 아키텍처 및 동작 메커니즘

SCTP는 호스트 간 논리적 연선인 '결합(Association)'을 수립하고, 패킷 내에 공통 헤더와 복수의 청크(Chunk: 제어/데이터)를 다중화하여 전송하는 아키텍처로 작동함.

```text
[ SCTP 패킷 구조 및 멀티호밍 / 멀티스트리밍 메커니즘 ]

1. SCTP 패킷 포맷 (청크 기반 다중화)
+-----------------------------------------------------------------+
| 공통 헤더 (Common Header: 발신/수신 포트, 검증 태그 32b, CRC-32c)|
+-----------------------------------------------------------------+
| Chunk 1: INIT, INIT ACK, SACK, HEARTBEAT 등 (제어 청크)        |
+-----------------------------------------------------------------+
| Chunk 2: DATA Chunk (Stream ID, Stream Sequence Number, Payload)|
+-----------------------------------------------------------------+

2. 멀티호밍 (Multi-Homing: 이중 물리 경로 무중단 페일오버)
   호스트 A (Association)                               호스트 B
   [ IP A1 (Primary Link) ] <==== 주 통신 경로 ======> [ IP B1 ]
          │ (하트비트로 헬스체크)
          ▼ (주 회선 단절 시)
   [ IP A2 (Backup Link)  ] <==== 즉시 무중단 절체 ===> [ IP B2 ]

3. 멀티스트리밍 (Multi-Streaming: 헤드오브라인 블로킹 제거)
   Association 내부:
    - Stream 0: [ Msg 1 ] [ Msg 2(손실!) ] [ Msg 3(대기) ]  --> 스트림 0만 일시 지연
    - Stream 1: [ Msg A ] [ Msg B ] [ Msg C ] ------------> 스트림 1은 지연 없이 즉시 수신!
```

- **결합(Association)** : 양단 호스트의 복수 IP 주소 집합 간에 맺어지는 포괄적 전송 세션으로, 물리 링크가 단절되어도 세션이 끊기지 않고 유지됨.
- **멀티호밍(Multi-Homing)** : 단일 호스트에 할당된 다중 NIC 카드 및 IP를 단일 결합에 바인딩하여, Primary 경로 장애 발생 시 백업 IP 경로로 커널 레벨에서 즉각 무손실 페일오버 수행.
- **멀티스트리밍(Multi-Streaming)** : 하나의 결합 내에 독립된 다중 논리 스트림(Stream ID)을 생성하여, 한 스트림에서 패킷 손실이 발생해도 다른 스트림의 데이터 전달이 중단되지 않음(HoL 차단).
- **메시지 지향(Message-Oriented) 청크** : 바이트 스트림 방식의 TCP와 달리 응용 계층의 메시지 경계(Boundary)를 그대로 보존하여 별도의 패킷 프레이밍 처리 불필요.
- **4-Way 핸드셰이크 & 상태 쿠키(State Cookie)** : 연결 수립 시 서버가 상태를 저장하지 않고 서명된 쿠키(Cookie)를 반환하여 클라이언트 검증 후 자원을 할당함으로써 SYN Flooding 공격 무력화.

## Ⅲ. SCTP(Stream Control Transmission Protocol)의 세부 구성 요소 및 비교 분석

| 비교 항목 | TCP (전송 제어 프로토콜) | UDP (사용자 데이터그램) | SCTP (스트림 제어 전송 프로토콜) |
|---|---|---|---|
| **신뢰성 보장** | 완전 보장 (ACK, 재전송) | 미보장 (Best-Effort) | 완전 보장 (선택적 비신뢰 PR-SCTP도 지원)|
| **전송 단위** | 연속된 바이트 스트림 | 독립된 데이터그램 메시지 | 메시지 경계 보존 청크 (Chunk) |
| **연결 모델** | 1:1 유니캐스트 (단일 IP 쌍)| 비연결형 (유니/멀티/브로드)| 1:1 Association (복수 IP 멀티호밍) |
| **헤드오브라인(HoL)**| 심각 (단일 패킷 손실 시 전체 대기)| 없음 (독립 패킷) | 없음 (멀티스트림 독립 큐 처리) |
| **연결 수립 방식** | 3-Way Handshake (SYN 취약) | 핸드셰이크 없음 | 4-Way Handshake with State Cookie |
| **오류 검출 부호** | 16-bit Checksum (단순 덧셈) | 16-bit Checksum (선택적) | 32-bit CRC-32c (강력한 다항식 검출)|

- SCTP는 통신 캐리어급 고가용성을 목표로 탄생하여 멀티호밍과 보안 쿠키를 완벽히 구현했으며, 5G 코어망과 WebRTC의 핵심 전송 엔진으로 활약 중임.

## Ⅳ. SCTP(Stream Control Transmission Protocol)의 주요 한계점 및 해결 방안

- **기존 레거시 NAT 게이트웨이 및 방화벽 미들박스의 SCTP 패킷 드롭** :
  - **한계점** : 인터넷 상의 대다수 저가 공유기 및 방화벽이 TCP/UDP만 인식하고 SCTP 프로토콜 번호(132)를 차단하여 E2E 연결 실패.
  - **해결 방안** : 표준 RFC 6951 기반의 UDP 캡슐화(SCTP-over-UDP, 포트 9899) 적용으로 레거시 방화벽 통과.
- **운영체제 커널의 기본 소켓 API 지원 및 개발자 생태계 부족** :
  - **한계점** : 윈도우, 임베디드 OS 등에서 커널 레벨 SCTP 스택 미지원으로 일반 애플리케이션 개발 난항.
  - **해결 방안** : usrsctp 등 크로스 플랫폼 사용자 공간(User-space) 오픈소스 라이브러리 채택.
- **웹 브라우저 환경에서의 HTTP/3(QUIC)과의 기능 중복 및 경쟁** :
  - **한계점** : 멀티스트리밍과 연결 마이그레이션 기능을 제공하는 QUIC이 웹 전송 표준을 선점하여 범용 웹 채택 정체.
  - **해결 방안** : 범용 웹은 QUIC에 일임하고, SCTP는 통신사 5G 코어 시그널링과 WebRTC 데이터 채널에 특화 집중.

## Ⅴ. SCTP(Stream Control Transmission Protocol) 적용 및 발전을 위한 기술사적 제언

- **5G 코어망(5GC) 차세대 제어 인터페이스(NGAP & S1AP) 인프라 고가용성 유지** : 기지국(gNB)과 이동성 관리 엔티티(AMF) 간의 시그널링 링크에 SCTP 멀티호밍을 필수 구성하여 무중단 텔코 코어 운영.
- **WebRTC DataChannel(RTCDataChannel) 엔진의 무손실 대용량 P2P 최적화** : 브라우저 간 P2P 데이터 전송 시 DTLS 보안 터널 상에서 동작하는 SCTP(RFC 8831) 파라미터를 튜닝하여 고속 파일 공유 지원.
- **금융 망 및 증권 체결 시스템의 초신뢰 전송 백본으로 활용 검토** : 통신 회선 장애 시 TCP의 수 초 소요 재접속 지연을 배제하고 밀리초 단위 물리 링크 자동 우회를 달성하기 위해 증권 전용선에 SCTP 채택 권장.
