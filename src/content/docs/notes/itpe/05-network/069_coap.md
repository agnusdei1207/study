---
title: "CoAP(Constrained Application Protocol)"
author: "Antigravity"
date: "2026-09-24T21:00:00+09:00"
tags:
  - "notes-network"
sidebar:
  label: "069. CoAP(Constrained Application Protocol)"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

네트워크 → 제약 장치 웹 통신 및 IoT 프로토콜 → **CoAP(Constrained Application Protocol)**

## 30초 인출

- 본질: **CoAP(Constrained Application Protocol)** : 8비트 MCU 및 저전력 손실 네트워크(LLN/6LoWPAN) 등 자원이 극도로 제한된 IoT 노드 환경에서 웹 표준 RESTful 아키텍처를 4바이트 바이너리 헤더로 경량 구현한 IETF 표준 프로토콜 (RFC 7252)
- 메커니즘: 비연결형 UDP 기반 위에 4가지 메시지 유형(CON, NON, ACK, RST)과 2계층 분리(메시지 계층 + 요청/응답 계층) 구조로 동작하며, Observe 옵션을 통한 이벤트 구독 지원
- 통찰: UDP 기반 경량 통신 이면에 패킷 손실 시 지수 백오프 재전송 지연과 DTLS 핸드셰이크 단편화 한계 극복을 위해 CoCoA 혼잡 제어 및 OSCORE 응용 계층 종단간 암호화 연계 필수

<details>
<summary>핵심 용어</summary>

- **CON (Confirmable)** : 신뢰성 있는 전송을 위해 수신측으로부터 반드시 ACK 회신을 요구하며 미수신 시 재전송을 수행하는 메시지 유형
- **NON (Non-confirmable)** : 신뢰성 검증 없이 1회 전송하고 수신 확인을 요구하지 않는 주기적 센서 데이터용 경량 메시지 유형
- **Piggybacked Response** : 클라이언트의 CON 요청에 대해 수신 확인 ACK 헤더 내부에 애플리케이션 응답 페이로드를 동봉하여 1번에 회신하는 방식
- **Separate Response** : 서버 처리에 시간이 걸릴 때 빈 ACK(Empty ACK)를 먼저 보내 타임아웃을 방지한 후 별도의 CON/NON 메시지로 결과를 전달하는 방식
- **Observe (RFC 7641)** : 클라이언트가 특정 URI 자원을 관찰(구독) 등록하면 자원 상태 변경 시 서버가 자율적으로 통지하는 경량 Pub/Sub 확장
- **OSCORE (RFC 8613)** : DTLS 대신 응용 계층 수준에서 CBOR 및 COSE 표준을 활용해 엔드투엔드 페이로드를 암호화하는 초경량 보안 표준

</details>

---

## 2~4교시 예상문제 (25점)

> 저전력 경량 IoT 기기를 위한 CoAP(Constrained Application Protocol)의 프로토콜 아키텍처와 4바이트 헤더 구조를 설명하고, 메시지 교환 방식(Piggybacked vs Separate) 및 신뢰성/보안(DTLS 한계와 OSCORE) 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. CoAP의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 전력, 메모리, 연산 능력이 극히 제한된 IoT 센서 노드들이 기존 웹(HTTP) 인프라와 원활히 연동될 수 있도록 RESTful 구조를 UDP 기반 4바이트 초경량 바이너리 헤더로 재설계한 IETF 표준 통신 프로토콜 (RFC 7252) |
| 목적 | 수십 KB 메모리의 초소형 MCU에서 웹 API(GET/POST/PUT/DELETE)를 지원하고 패킷 오버헤드를 극소화하여 배터리 수명 10년 이상 보장 |

## Ⅱ. CoAP의 특징 및 4바이트 바이너리 헤더 구조

| 헤더 필드 | 비트 크기 | 세부 기능 및 엔지니어링 특징 |
|---|---|---|
| **Ver (버전)** | 2 bits | CoAP 프로토콜 버전 명시 (표준 기본값 `01` = 버전 1) |
| **T (메시지 유형)** | 2 bits | `00`: CON(확인형), `01`: NON(비확인형), `10`: ACK(응답), `11`: RST(리셋) |
| **TKL (토큰 길이)** | 4 bits | 헤더 뒤에 이어지는 Token 필드의 바이트 길이 명시 (0~8 바이트) |
| **Code (기능 코드)** | 8 bits | 상위 3비트 클래스(c)와 하위 5비트 상세(dd)로 구분 (`c.dd` 표기)<br/>- 0.01~0.04: GET, POST, PUT, DELETE 요청 메서드<br/>- 2.05(Content), 4.04(Not Found) 등 REST 상태 코드 |
| **Message ID** | 16 bits | 메시지의 중복 수신 감지 및 CON과 ACK 간의 물리적 일치 식별자 |
| **Token (토큰, 옵션)** | 0 ~ 8 bytes | 비동기 환경에서 요청(Request)과 응답(Response)을 논리적으로 매핑 |
| **Options (옵션 헤더)** | 가변 길이 | URI-Path, Content-Format, Observe, Max-Age 등 TLV 형태로 추가 |

## Ⅲ. CoAP 계층 아키텍처 및 2계층 상호작용 프로세스

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ CoAP 2계층 구조 및 메시지 교환 프로세스 ]          │
│                                                                        │
│   [응용 계층 (REST)]     GET /sensors/temp ──► [2.05 Content, 23.5℃]   │
│                                  │                                     │
│   [CoAP 요청/응답 계층]  Request / Response (Token 매핑)               │
│                                  │                                     │
│   [CoAP 메시지 전송 계층] Reliable (CON/ACK) vs Unreliable (NON)       │
│                                  │                                     │
│   [전송 계층 (L4)]       UDP (기본 포트: 5683, DTLS 포트: 5684)        │
│                                                                        │
│   [시나리오 A: Piggybacked 응답]       [시나리오 B: Separate 응답]       │
│   Client                 Server        Client                 Server   │
│     │ CON [MID=10, GET]    │             │ CON [MID=20, GET]    │      │
│     ├─────────────────────►│             ├─────────────────────►│      │
│     │                      │             │ ACK [MID=20, Empty]  │      │
│     │ ACK [MID=10, 2.05]   │             │◄─────────────────────┤ (즉시)│
│     │◄─────────────────────┤             │                      │ (연산)│
│     │ (한 번에 응답 완결!) │             │ CON [MID=55, 2.05]   │      │
│     │                      │             │◄─────────────────────┤      │
│     │                      │             │ ACK [MID=55, Empty]  │      │
│     │                      │             ├─────────────────────►│      │
└────────────────────────────────────────────────────────────────────────┘
```

| 교환 방식 | 메시지 흐름 | 세부 동작 및 활용처 |
|---|---|---|
| **Piggybacked Response** | CON 요청 ──►<br/>◄── ACK + 응답 | 서버가 요청을 즉시 처리할 수 있을 때 ACK 헤더 안에 응답 본문을 직접 실어 전송 (네트워크 왕복 1회로 자원 극대화) |
| **Separate Response** | CON 요청 ──►<br/>◄── Empty ACK<br/>◄── CON 응답<br/>ACK 회신 ──► | 센서 측정에 수 초 이상 소요될 때 클라이언트 타임아웃을 방지하기 위해 빈 ACK를 먼저 보낸 후, 준비 완료 시 별도 트랜잭션 응답 |
| **Non-confirmable (NON)**| NON 요청 ──► | 주기적인 센서 텔레메트리(온도, 조도) 보고 시 손실을 감수하고 확인 응답 없이 1회 송출 |

## Ⅳ. CoAP vs MQTT vs HTTP/1.1 비교

| 비교 항목 | IETF RFC 7252 CoAP | OASIS / ISO MQTT | W3C / IETF HTTP/1.1 |
|---|---|---|---|
| **기저 전송 프로토콜**| **UDP (기본 5683)** | TCP (기본 1883) | TCP (기본 80/443) |
| **통신 패러다임** | **Request/Response (RESTful)** + Observe | Publish/Subscribe (브로커 중심) | Request/Response (클라이언트-서버) |
| **최소 헤더 크기** | **4 바이트 (초경량 바이너리)** | 2 바이트 (바이너리) | 수백 바이트 이상 (텍스트 문자열) |
| **자원 제약 환경 적합성**| **최고 (8비트 MCU, 수 KB RAM)** | 우수 (중소형 임베디드 리눅스) | 불량 (고성능 PC/서버 전용) |
| **메시지 신뢰성 제어**| CON (재전송), NON | QoS 0, QoS 1, QoS 2 (3단계) | TCP 계층 신뢰성에 전적 의존 |
| **기본 보안 프로토콜**| DTLS (UDP 기반 TLS) | TLS / SSL (TCP) | TLS / HTTPS |

## Ⅴ. CoAP 운영 시 핵심 엔지니어링 한계와 방안

| 한계 | 방안 |
|---|---|
| 열악한 저전력 무선망(6LoWPAN)에서 CON 메시지 유실 시 기본 재전송 알고리즘이 지수 백오프(RTO=2초, 4초, 8초, 16초)로 동작하여 최대 4회 재전송 시 수십 초간 세션이 정체되고 실시간 제어 마감시간 실패 발생 | 왕복 지연시간(RTT)의 편차를 실시간 측정하여 가변 RTO를 동적으로 산출하는 고급 혼잡 제어 알고리즘인 CoCoA(CoAP Congestion Control Advanced, RFC 8968)를 탑재하여 불필요한 백오프 지연 단축 |
| 전송 보안을 위해 DTLS를 적용할 경우, 최초 핸드셰이크 시 교환되는 X.509 공개키 인증서 체인의 크기가 6LoWPAN 물리 MTU(127바이트)를 크게 초과하여 과도한 단편화(Fragmentation) 및 패킷 손실로 연결 수립 실패 | X.509 인증서 대신 원시 공개키(Raw Public Key) 또는 사전 공유 키(PSK) 방식을 채택하고, 전송 계층 터널링 대신 페이로드 레벨에서 CBOR 객체를 경량 암호화하는 OSCORE(RFC 8613) 표준으로 전환 |
| 1024바이트 이상의 펌웨어 바이너리(FOTA)나 대용량 로그 전송 시 UDP 단편화로 인해 단 1개 조각만 유실되어도 전체 패킷이 폐기되는 재전송 비효율 발생 | 상위 계층에서 페이로드를 협상된 크기(64B~1024B)의 개별 블록으로 잘게 쪼개어 번호를 매겨 순차 전송하고 손실된 특정 블록만 선택 재전송하는 Block-wise Transfer(RFC 7959) 옵션 적용 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
스마트 빌딩 및 산업용 사물인터넷(IIoT) 구축 시, 단말 센서망은 배터리 소모를 극소화하기 위해 CoAP을 사용하고 기존 엔터프라이즈 클라우드는 HTTP/JSON을 사용하는 경우가 일반적이므로, 경계 구간에 CoAP-to-HTTP 크로스 프록시(Reverse Proxy)를 배치하여 메서드 및 미디어 타입(CBOR ↔ JSON) 상호 변환 파이프라인 수립 권장

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│               [ CoAP - HTTP 크로스 프록시 연계 아키텍처 ]              │
│                                                                        │
│   [초저전력 스마트 센서]                        [클라우드 웹 서버]     │
│   (배터리 구동, 6LoWPAN)                        (AWS / Azure REST API) │
│          │                                                ▲            │
│          ▼ CoAP 프로토콜 (UDP)                             │ HTTP (TCP) │
│   ┌───────────────────────────────────────────────────────┴──────────┐ │
│   │               CoAP - HTTP 게이트웨이 (Cross Proxy)                │ │
│   │  - CoAP 헤더 파싱 (GET /temp, Type: CON, Token: 0x4A)            │ │
│   │  - 미디어 변환: CBOR 바이너리 페이로드 ──► JSON 텍스트 변환      │ │
│   │  - 보안 변환: OSCORE / DTLS 복호화 ──► HTTPS / TLS 1.3 암호화     │ │
│   └──────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| CoAP 메시지 교환 모드 | 통신 방식 | 신뢰성 보장 여부 | 네트워크 대역폭 소모 | 최적 적용 유스케이스 |
|---|---|---|---|---|
| **Piggybacked 모드** | 동기식 1-RTT | 보장 (ACK 내 본문 동봉) | 최소 (2개 패킷으로 완결) | 단순 센서 데이터 단발성 조회 |
| **Separate 모드** | 비동기 2-RTT | 보장 (중간 빈 ACK + CON) | 중간 (4개 패킷 소모) | 액추에이터 구동, 연산 지연 작업 |
| **Non-confirmable (NON)**| 단방향 브로드캐스트 | 미보장 (Fire-and-forget) | 극소 (단일 패킷 송출) | 실시간 환경 센서(온습도) 텔레메트리 |
| **Observe 모드** | 이벤트 기반 푸시 | 보장 또는 미보장 선택 | 매우 우수 (폴링 트래픽 제거) | 화재 감지기, 도어락 상태 침입 감시 |

## 출제 이력과 검증 출처

- 정보관리기술사 108회 1교시: IoT 표준 프로토콜 CoAP의 개념 및 HTTP와의 비교
- 컴퓨터시스템응용기술사 115회 2교시: 제약 장치를 위한 CoAP 아키텍처와 메시지 신뢰성 보장 기술
- RFC 7252: The Constrained Application Protocol (CoAP)
- RFC 7641: Observing Resources in the Constrained Application Protocol
- RFC 7959: Block-Wise Transfers in the Constrained Application Protocol

## 연결 토픽

- 상위 토픽: [055 M2M 통신](./055_m2m.md)
- 연관 토픽: [070 MQTT](./070_mqtt.md), [072 WSN](./072_wsn.md)
