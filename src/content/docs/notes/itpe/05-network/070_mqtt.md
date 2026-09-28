---
title: "MQTT(Message Queuing Telemetry Transport)"
author: "Antigravity"
date: "2026-09-24T21:00:00+09:00"
tags:
  - "notes-network"
sidebar:
  label: "070. MQTT(Message Queuing Telemetry Transport)"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

네트워크 → 메시지 기반 IoT 통신 및 미들웨어 → **MQTT(Message Queuing Telemetry Transport)**

## 30초 인출

- 본질: **MQTT(Message Queuing Telemetry Transport)** : 저대역폭, 고지연, 불안정한 무선 네트워크 환경에서 중앙 브로커(Broker)를 매개로 경량 토픽 기반의 발행-구독(Publish/Subscribe) 메시징을 수행하는 ISO/OASIS 표준 IoT 전송 프로토콜
- 메커니즘: 최소 2바이트 고정 헤더의 초경량 패킷 구조와 3단계 서비스 품질(QoS 0/1/2), 비정상 접속 단절을 통보하는 유언장(LWT), 신규 구독자를 위한 최신 상태 보존(Retained Message) 메커니즘 제공
- 통찰: QoS 1 적용 시 네트워크 단절 후 재전송에 따른 메시지 중복 처리와 대규모 TCP 상시 연결 시 브로커 자원 고갈 한계 극복을 위해 멱등성 컨슈머 패턴과 분산 브로커 클러스터링 연계 필수

<details>
<summary>핵심 용어</summary>

- **Message Broker** : 발행자(Publisher)와 구독자(Subscriber) 사이에서 클라이언트 연결 세션을 관리하고 토픽 트리 필터링을 통해 메시지를 라우팅하는 중앙 허브
- **Topic** : 슬래시(`/`)로 계층화된 UTF-8 문자열 식별자로 단일 레벨 와일드카드(`+`) 및 다중 레벨 와일드카드(`#`)를 활용해 유연한 필터링 지원
- **QoS (Quality of Service)** : 메시지 전달 신뢰성 등급 (QoS 0: 최대 1회/No-ACK, QoS 1: 최소 1회/PUBACK, QoS 2: 정확히 1회/4-way 핸드셰이크)
- **LWT (Last Will and Testament)** : 클라이언트 접속 시 브로커에 사전에 유언 메시지를 등록하여 비정상적인 Keep-Alive 타임아웃 감지 시 브로커가 대리 발행하는 기능
- **Retained Message** : 브로커가 토픽별 마지막 발행 메시지를 메모리에 보관하여 향후 새롭게 해당 토픽을 구독하는 클라이언트에게 즉시 최신 상태를 전달하는 기능

</details>

---

## 2~4교시 예상문제 (25점)

> 사물인터넷(IoT) 표준 메시징 프로토콜인 MQTT의 발행-구독(Pub/Sub) 아키텍처와 패킷 구조를 설명하고, 3단계 QoS(0, 1, 2) 전달 절차 및 대규모 디바이스 수용을 위한 브로커 클러스터링 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. MQTT의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 신뢰성이 낮고 대역폭이 제한된 유무선 네트워크에서 센서 단말과 서버 간에 경량 메시지를 비동기 방식으로 교환하기 위해 IBM이 개발하고 OASIS 및 ISO/IEC 20922로 표준화된 발행-구독 기반의 메시징 프로토콜 |
| 목적 | 패킷 오버헤드 극소화(최소 2바이트), 다대다(M:N) 메시지 브로드캐스팅, 전력 소모 절감 및 신뢰성 있는 IoT 텔레메트리 데이터 수집 |

## Ⅱ. MQTT의 특징 및 초경량 패킷 헤더 구조

| 헤더 구성 요소 | 바이트 크기 | 세부 기능 및 엔지니어링 특징 |
|---|---|---|
| **Control Packet Type** | 4 bits | 패킷 유형 명시 (`CONNECT`, `CONNACK`, `PUBLISH`, `PUBACK`, `SUBSCRIBE`, `PINGREQ` 등 총 14종) |
| **Flags (제어 플래그)** | 4 bits | `DUP`(중복 전송 여부 1bit), `QoS Level`(0~2 2bits), `RETAIN`(브로커 보관 여부 1bit) |
| **Remaining Length** | 1 ~ 4 bytes | 가변 길이 인코딩; 현재 헤더 이후 잔여 데이터의 바이트 길이 (최대 256MB 페이로드 표현) |
| **Variable Header** | 가변 길이 | 패킷 유형별 추가 정보 (Packet Identifier, Topic Name, Connect Flags, Keep Alive 시간) |
| **Payload** | 가변 길이 | 실제 전송되는 애플리케이션 데이터 (JSON, 바이너리, 텍스트 등 형식 제약 없음) |

## Ⅲ. MQTT Pub/Sub 아키텍처 및 3단계 QoS 전달 프로세스

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ MQTT 아키텍처 및 3단계 QoS 전달 프로세스 ]          │
│                                                                        │
│   [Publisher (센서)]         [MQTT Message Broker]    [Subscriber (앱)]│
│          │                             │                      │        │
│          ▼ [QoS 0: At most once (최대 1회 전송, 확인 없음)]            │
│          ├───── PUBLISH ──────────────►├───── PUBLISH ───────►│        │
│          │                             │                      │        │
│          ▼ [QoS 1: At least once (최소 1회 전송, 중복 가능)]           │
│          ├───── PUBLISH (PacketID:1) ─►├───── PUBLISH ───────►│        │
│          │◄──── PUBACK (PacketID:1) ───┤◄──── PUBACK ─────────┤        │
│          │                             │                      │        │
│          ▼ [QoS 2: Exactly once (정확히 1회 전송, 4-Way Handshake)]    │
│          ├───── PUBLISH (PacketID:2) ─►├───── PUBLISH ───────►│        │
│          │◄──── PUBREC (수신 확인) ────┤◄──── PUBREC ─────────┤        │
│          ├───── PUBREL (방출 명령) ───►├───── PUBREL ────────►│        │
│          │◄──── PUBCOMP (완료 통보) ───┤◄──── PUBCOMP ────────┤        │
└────────────────────────────────────────────────────────────────────────┘
```

| QoS 레벨 | 통신 보장 수준 | 제어 메시지 교환 흐름 | 적합한 엔지니어링 활용처 |
|---|---|---|---|
| **QoS 0** | **At most once** (최대 1회) | Handshake 없음 (Fire-and-forget) | 손실되어도 무방한 고주파 환경 센서 데이터 (초당 수회 온도 보고) |
| **QoS 1** | **At least once** (최소 1회) | `PUBLISH` ──► / ◄── `PUBACK` | 데이터 손실이 치명적이나 수신단 멱등성 처리가 가능한 관제 로그 |
| **QoS 2** | **Exactly once** (정확히 1회)| `PUB` ──► `PUBREC` ──► `PUBREL` ──► `PUBCOMP` | 중복 실행 시 금융 사고나 물리 파괴를 야기하는 원격 결제 및 밸브 차단 |

## Ⅳ. MQTT vs CoAP vs HTTP 비교

| 비교 항목 | OASIS MQTT v5.0 | IETF CoAP (RFC 7252) | W3C HTTP/2 |
|---|---|---|---|
| **전송 계층** | **TCP (신뢰성 연결 기반, 1883)** | UDP (비연결형 경량, 5683) | TCP (연결 기반, 443) |
| **통신 패턴** | **중앙 브로커 기반 Publish/Subscribe**| P2P / Client-Server Request-Response | Client-Server Request-Response |
| **헤더 오버헤드** | **최소 2 바이트 (매우 작음)** | 최소 4 바이트 | 수십 바이트 (바이너리 프레이밍) |
| **네트워크 결합도** | 시간/공간/동기화 완전 분리(Decoupled)| 클라이언트와 서버 간 주소 결합 | 클라이언트와 서버 간 강력 결합 |
| **연결 지속성** | Long-lived TCP 상시 연결 (Keep-Alive) | Stateless (필요 시에만 패킷 송출) | 단발성 또는 스트림 다중화 |
| **적용 영역** | 스마트 홈, 커넥티드 카, 공장 센서 관제 | 초저전력 배터리 구동 무선 센서망 | 일반 웹 서비스, 모바일 앱 백엔드 API |

## Ⅴ. MQTT 운영 시 핵심 엔지니어링 한계와 방안

| 한계 | 방안 |
|---|---|
| QoS 1 환경에서 브로커가 메시지를 정상 수신한 후 발송한 `PUBACK`가 무선 채널 불안정으로 클라이언트에 도달하기 전 소켓이 끊어지면, 클라이언트가 재연결 후 동일 메시지(`DUP=1`)를 재전송하여 결제나 제어 명령이 중복 실행되는 부작용 발생 | 발행 메시지 페이로드에 비즈니스 트랜잭션 고유 UUID를 삽입하고, 수신측 컨슈머에서 Redis 분산 캐시를 조회하여 최근 10분 내 동일 UUID가 처리된 이력이 있으면 즉시 스킵하는 멱등성(Idempotent Consumer) 패턴 구현 |
| 수십만 대의 IoT 디바이스가 단일 MQTT 브로커로 상시 TCP Keep-Alive 연결을 유지할 경우 브로커 서버의 소켓 파일 디스크립터(FD) 한계 및 메모리 고갈로 인한 단일 장애점(SPOF) 형성 | 분산 얼랭(Erlang/OTP) 기반의 대규모 동시 접속 아키텍처를 갖춘 EMQX 또는 VerneMQ 브로커 클러스터를 구성하고, 브로커 전면에 L4 Anycast 또는 HAProxy를 배치하여 세션 부하를 수평 분산 |
| 모바일 통신 음영 지역 진입 시 빈번한 3GPP 셀룰러 접속 단절 및 재접속으로 인해 클라이언트-브로커 간 TLS 핸드셰이크와 세션 재협상 오버헤드가 급증하여 통신사 데이터 과금 및 배터리 급속 방전 | MQTT v5.0의 세션 만료 간격(Session Expiry Interval)을 넉넉히 설정하여 단절 후 재접속 시 이전 구독 상태와 미수신 큐 메시지를 즉시 이어받는 세션 재개(Session Resumption) 활성화 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
스마트 팩토리 및 모빌리티 인프라 구축 시, 단순 텔레메트리 수집은 QoS 0 또는 QoS 1을 채택하여 브로커 부하를 억제하고, 원격 펌웨어 업데이트(FOTA)와 긴급 비상 제어 명령에만 선별적으로 QoS 2를 적용해야 하며, 전송 보안을 위해 포트 8883 상의 TLS 1.3 암호화 및 디바이스 X.509 상호 인증(Mutual TLS) 의무화 권장

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│               [ 고가용성 대규모 분산 MQTT 브로커 클러스터 ]            │
│                                                                        │
│   [수십만 IoT 디바이스군]                                              │
│          │                                                             │
│          ▼ L4 로드밸런서 (Keepalived / L4 DSR 부하 분산)                │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │                 EMQX 분산 브로커 클러스터                      │   │
│   │                                                                │   │
│   │   [Broker Node 1] ◄══ Mnesia 분산 DB ══► [Broker Node 2]       │   │
│   │   - 클라이언트 세션 관리                  - 라우팅 테이블 동기화   │   │
│   │   - Shared Subscription (공유 구독)       - 클러스터 헬스체크      │   │
│   └───────┬────────────────────────────────────────────────┬───────┘   │
│           │ Shared Sub: $share/group/telemetry             │           │
│           ▼                                                ▼           │
│   [백엔드 컨슈머 WAS 1]                            [백엔드 컨슈머 WAS 2]│
│   (Redis 기반 멱등성 검증 후 DB 저장)               (Kafka 파이프라인 연계)│
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 구분 | MQTT v3.1.1 (레거시 표준) | MQTT v5.0 (차세대 표준) |
|---|---|---|
| **이유 코드 (Reason Code)** | 단순 성공/실패 여부만 확인 가능 | 모든 ACK 패킷에 세분화된 오류 사유 코드(1바이트) 반환 |
| **사용자 속성 (User Properties)**| 미지원 (페이로드 내부에 직접 정의 필요)| 헤더 레벨에서 사용자 정의 Key-Value 메타데이터 부가 지원 |
| **요청/응답 패턴 (Req/Resp)** | 토픽 규칙으로 수동 구현 | `Response Topic` 및 `Correlation Data` 헤더 표준 내장 |
| **공유 구독 (Shared Sub)** | 벤더별 비표준 확장 | `$share/group/topic` 표준 공유 구독으로 컨슈머 로드밸런싱 |
| **세션 제어 유연성** | Clean Session (True / False 고정) | Clean Start + Session Expiry Interval (초 단위 정밀 제어)|

## 출제 이력과 검증 출처

- 정보관리기술사 108회 1교시: MQTT 프로토콜의 구조, 특징 및 QoS 3단계
- 컴퓨터시스템응용기술사 119회 2교시: 사물인터넷(IoT) 환경에서 CoAP과 MQTT의 비교 및 브로커 설계
- OASIS Standard: MQTT Version 5.0 Specification
- ISO/IEC 20922: Information technology - Message Queuing Telemetry Transport (MQTT) v3.1.1

## 연결 토픽

- 상위 토픽: [055 M2M 통신](./055_m2m.md)
- 연관 토픽: [069 CoAP](./069_coap.md), [062 소켓 통신](./062_socket_communication.md)
