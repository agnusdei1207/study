---
title: "MQTT(Message Queuing Telemetry Transport)"
author: "Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-network"]
sidebar:
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

네트워크 → 메시지 기반 IoT 통신 → MQTT

## 30초 인출

- 본질: **MQTT(Message Queuing Telemetry Transport)** 는 발행자와 구독자를 브로커로 연결하는 경량 메시징 프로토콜
- 메커니즘: 토픽 구독 관계에 따라 브로커가 메시지를 전달하고, QoS 수준으로 전달 확인 방식을 선택

<details>
<summary>핵심 용어</summary>

- **MQTT(Message Queuing Telemetry Transport):** 발행·구독 방식으로 메시지를 교환하는 경량 프로토콜
- **브로커(Message Broker):** 연결된 클라이언트를 관리하고 토픽 구독에 따라 메시지를 전달하는 중계 서버
- **토픽(Topic):** 발행 메시지와 구독을 연결하는 계층형 문자열 이름
- **QoS(Quality of Service):** MQTT 메시지 전달 확인 수준
- **LWT(Last Will and Testament):** 비정상 연결 종료를 브로커가 감지할 때 게시하는 사전 등록 메시지
- **Retained Message:** 특정 토픽의 마지막 retained 발행 메시지를 새 구독자에게 전달하도록 보관하는 메시지

</details>

---

## 1교시 예상문제 (10점)

> MQTT의 개념과 발행·구독 구조 및 전달 수준을 설명하시오. (예상)

---

## 1교시 10점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **MQTT(Message Queuing Telemetry Transport)** 는 브로커를 통해 발행자와 구독자 간 메시지를 전달하는 경량 프로토콜 |
| 목적 | 연결된 장치·응용 사이의 비동기 메시지 교환 지원 |

## Ⅱ. 발행·구독과 **QoS(Quality of Service)**

```text
발행자
   ↓ 토픽에 메시지 게시
브로커
   ↓ 구독 토픽에 맞춰 전달
구독자

QoS 0: 최대 한 번 · 확인 없음
QoS 1: 최소 한 번 · 중복 가능
QoS 2: 정확히 한 번 전달 교환
```

제언: 메시지 중요도와 중복 처리 능력에 맞춰 QoS를 선택

---

## 2~4교시 예상문제 (25점)

> MQTT의 구성과 메시지 전달 절차를 설명하고, QoS·세션·보안 설정을 설계할 때의 고려사항을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **MQTT(Message Queuing Telemetry Transport)** 는 브로커를 통해 발행자와 구독자 간 메시지를 전달하는 경량 프로토콜 |
| 목적 | 연결된 장치·응용 사이의 비동기 메시지 교환 지원 |

## Ⅱ. 구성과 메시지 흐름

```text
발행 클라이언트
       ↓ PUBLISH(topic, payload)
브로커
       ↓ 구독 토픽 일치
구독 클라이언트
```

| 구성요소 | 역할 |
|---|---|
| Publisher | 토픽을 지정해 메시지 발행 |
| Broker | 연결·인증·토픽 구독 관리와 메시지 전달 |
| Subscriber | 관심 토픽을 구독해 일치 메시지 수신 |
| 고정 헤더 | 최소 2바이트이며 패킷 유형·남은 길이 정보 포함 |

## Ⅲ. **QoS(Quality of Service)** 전달 교환

```text
QoS 0
송신 측 ── PUBLISH ──▶ 수신 측
확인 교환 없음

QoS 1
송신 측 ── PUBLISH ──▶ 수신 측
송신 측 ◀── PUBACK ─── 수신 측
미확인 시 재전송·중복 가능

QoS 2
송신 측 ── PUBLISH ──▶ 수신 측
송신 측 ◀── PUBREC ─── 수신 측
송신 측 ── PUBREL ────▶ 수신 측
송신 측 ◀── PUBCOMP ── 수신 측
프로토콜 단계 교환으로 정확히 한 번 전달
```

| 수준 | 보장 의미 | 적용 판단 |
|---|---|---|
| QoS 0 | 최대 한 번 | 일부 손실을 허용하는 빈번한 상태 보고 |
| QoS 1 | 최소 한 번 | 전달 확인이 중요하고 수신 측 중복 처리가 가능한 경우 |
| QoS 2 | 프로토콜 전달 정확히 한 번 | 중복 억제가 중요하고 추가 교환 비용을 감당할 경우 |

QoS 보장은 MQTT 전달 교환의 의미이며, 업무 처리의 부작용까지 자동으로 정확히 한 번 수행한다는 뜻은 아님

## Ⅳ. 세션·보안·운영 고려

| 기능·경계 | 고려사항 |
|---|---|
| **Retained Message** | 토픽별로 새 구독자에게 전달할 최신 보관 메시지 관리 |
| **LWT(Last Will and Testament)** | 비정상 종료 때 게시할 메시지와 정상 종료 구별 |
| 세션·오프라인 메시지 | 만료·저장·재접속 정책과 브로커 자원 사용의 균형 |
| 접근 통제 | 인증과 토픽 단위 게시·구독 권한 설정 |
| 대량 연결 | 연결 수, 메시지율, 브로커 장애 시 세션 복구 용량 검토 |

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| QoS를 높게 잡으면 모든 토픽에서 불필요한 재전송·상태 보관 비용이 증가하고, 낮게 잡으면 중요한 메시지의 손실 가능성이 커짐 | 메시지 유형별 손실 허용도·중복 처리 가능성·전송 비용을 구분한 QoS 정책을 두고 실제 장애 조건에서 검증 |

## 출제 이력과 검증 출처

- 제108회 1교시 관련 문항은 공식 문제지 원문을 확보하지 못해 회차·문구를 검증하지 못함.
- [OASIS MQTT Version 5.0 Specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)
- [OASIS MQTT Version 3.1.1 Specification](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html)
