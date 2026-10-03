---
title: "CoAP(Constrained Application Protocol)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. CoAP(Constrained Application Protocol)의 개요

- 개념 : 8비트 마이크로컨트롤러, 수 킬로바이트의 초저용량 RAM/플래시 메모리, 극심한 패킷 손실률을 가진 제약적 IoT 환경(Constrained Nodes and Networks)을 위해 **IETF CoRE** 워킹그룹에서 제정한 **경량 웹 전송 프로토콜** (RFC 7252).
- 배경 및 필요성 : 전통적인 HTTP/TCP 스택은 3-Way Handshake, 장황한 텍스트 기반 헤더, 연결 유지 오버헤드로 인해 배터리 전원 기반의 초소형 센서 기기에 적용 불가.
- 핵심 목적 : HTTP RESTful 아키텍처(GET, POST, PUT, DELETE) 모델을 그대로 계승하면서도 **비연결형 UDP** 기반 4바이트 고정 헤더를 채택하여 초경량화 및 웹 생태계와의 원활한 게이트웨이 상호 연동 달성.

## Ⅱ. CoAP의 핵심 아키텍처 및 동작 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ CoAP 2계층 추상화 및 4바이트 바이너리 헤더 ]       │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 응용 계층 (Application) : RESTful 자원 모델 (URI, GET/POST)    │   │
│   ├────────────────────────────────────────────────────────────────┤   │
│   │ CoAP 서브 레이어 2: 요청/응답 (Request/Response)               │   │
│   │  - 메서드 코드, 응답 코드(2.05 Content, 4.04 Not Found)       │   │
│   ├────────────────────────────────────────────────────────────────┤   │
│   │ CoAP 서브 레이어 1: 메시지 (Messages) - 비동기 메시징 및 신뢰성│   │
│   │  - CON (Confirmable)   - NON (Non-Confirmable)                 │   │
│   │  - ACK (Acknowledgement) - RST (Reset)                         │   │
│   ├────────────────────────────────────────────────────────────────┤   │
│   │ 전송 계층: UDP (포트 5683) / DTLS (포트 5684)                  │   │
│   └────────────────────────────────────────────────────────────────┘   │
│                                                                        │
│   [ CoAP 기본 4바이트 바이너리 헤더 구조 ]                             │
│   0                   1                   2                   3        │
│   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1    │
│  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+     │
│  |Ver| T |  TKL  |      Code     |          Message ID           |     │
│  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+     │
│  - Ver (2bit: 버젼)  - T (2bit: CON, NON, ACK, RST 타입)               │
│  - TKL (4bit: 토큰 길이) - Code (8bit: 메서드/응답코드)                │
│  - Message ID (16bit: 중복 검출 및 매칭)                               │
└────────────────────────────────────────────────────────────────────────┘
```

- 2계층 분리 구조 :
  - **메시지 계층 (Messages Layer)** : UDP 상에서 패킷 재전송 및 중복 제거를 통해 신뢰성을 선택적으로 부여하는 기본 전송 계층.
  - **요청/응답 계층 (Request/Response Layer)** : 토큰(Token)을 매칭하여 REST 메서드(Request)와 상태 응답(Response)을 처리하는 계층.
- 4가지 메시지 유형 (Message Types) :
  - **CON (Confirmable)** : 반드시 상대방의 ACK 응답을 받아야 하는 신뢰성 메시지 (미수신 시 지수 백오프 재전송).
  - **NON (Non-Confirmable)** : 센서 주기 측정치처럼 ACK 응답을 요구하지 않는 전송 (유실 허용).
  - **ACK (Acknowledgement)** : CON 메시지 수신 성공 승인 (응답 데이터를 피기백(Piggybacked)하여 회신 가능).
  - **RST (Reset)** : 메시지 파싱 실패나 컨텍스트 유실 시 연결 재설정을 알리는 오류 응답.

## Ⅲ. CoAP의 핵심 확장 기능 및 MQTT와의 비교 분석

| 비교 항목 | CoAP (Constrained Application Protocol) | MQTT (Message Queuing Telemetry Transport) |
|---|---|---|
| 표준화 기구 | IETF (RFC 7252) | OASIS / ISO (ISO/IEC 20922) |
| 통신 모델 | 1:1 Request/Response (클라이언트-서버) | 1:N Publish/Subscribe (중앙 브로커 기반) |
| 전송 프로토콜 | UDP (포트 5683) | TCP (포트 1883) |
| 기본 헤더 크기 | 4 Byte 고정 바이너리 헤더 | 2 Byte 고정 바이너리 헤더 |
| 자원 탐색 | 자율 자원 발견 지원 (`/.well-known/core`)| 브로커 내 사전 토픽 설계 의존 |
| 구독 모델 | Observe 확장 옵션 (RFC 7641 지원) | 자체 표준 기능 (Topic Subscribe) |
| 보안 프로토콜 | DTLS (UDP 기반 암호화) / OSCORE | TLS/SSL (TCP 기반 암호화) |
| 적합한 환경 | 센서-액추에이터 1:1 직접 제어, 배터리 극소 기기| 데이터 수집 관제, 다자간 메시지 브로드캐스트 |

- **자원 관찰 (Observe Option, RFC 7641)** : 클라이언트가 특정 URI 자원에 Observe 옵션을 걸어 등록하면, 서버(센서)는 상태가 변경될 때마다 알림(Notification)을 비동기 푸시하여 지속적인 폴링 부하 해소.
- **블록 단위 전송 (Blockwise Transfers, RFC 7959)** : UDP MTU(보통 1280바이트 이하)를 초과하는 대용량 펌웨어(FOTA)나 이미지 데이터를 작은 블록 번호 단위로 분할하여 안정적 전송.

## Ⅳ. CoAP의 주요 한계점 및 해결 방안

- UDP 특성상 NAT 게이트웨이의 짧은 매핑 타임아웃 :
  - 한계점 : 가정용 공유기나 셀룰러 NAT 장비가 비활성 UDP 포트 매핑을 수십 초 만에 삭제하여 외부에서 배터리 절전형 IoT 단말로의 인바운드 접속 불가.
  - 해결 방안 : 클라이언트가 주기적 경량 Keep-Alive 핑을 송출하거나, 역방향 연결 프록시(CoAP Forward Proxy)를 중계 거점으로 배치.
- DTLS 핸드셰이크의 패킷 단편화 및 연산 부담 :
  - 한계점 : 보안을 위한 DTLS 인증서 교환 과정에서 패킷 크기가 커져 단편화 발생 및 마이크로컨트롤러 메모리 한계 초과.
  - 해결 방안 : 전송 계층 전체를 암호화하는 대신 응용 계층 페이로드만 종단 간(E2E) 선택 암호화하는 경량 `OSCORE (RFC 8613)` 표준 적용.

## Ⅴ. CoAP 적용 및 발전을 위한 기술사적 제언

- Matter 표준 및 스마트홈 인프라로의 적극 활용 : 스레드(Thread / IEEE 802.15.4) 무선 메시 네트워크 기반 스마트홈 표준인 Matter의 애플리케이션 계층 통신 기반으로 CoAP 생태계를 통합 확장.
- HTTP/CoAP 크로스 프록시(Cross-Proxy) 표준화 구축 : 기존 클라우드 웹 서비스(REST API)와 현장 IoT 센서 간의 변환 오버헤드를 줄이기 위해, HTTP 메서드와 상태 코드를 1:1 투명하게 매핑하는 고성능 게이트웨이 배치.
- LPWAN(NB-IoT) 환경에서의 CoAP 최적화 : 통신사 셀룰러 NB-IoT 망의 Non-IP Data Delivery(NIDD) 및 UDP 전송에 CoAP 바이너리 압축을 결합하여 가스/수도 원격 검침 단말 배터리 수명 15년 달성.
