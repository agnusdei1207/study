---
title: "MQTT(Message Queuing Telemetry Transport)"
author: "agnusdei1207"
date: "2026-10-24T22:50:25+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- MQTT(Message Queuing Telemetry Transport), 발행-구독(Publish-Subscribe), 브로커(Broker), 토픽(Topic)
- QoS(Quality of Service), LWT(Last Will and Testament), Retained Message, Keep Alive
- 와일드카드(+, #), 공유 구독(Shared Subscription), MQTT-SN, 세션 만료 간격(Session Expiry Interval)
- 단일 장애점(SPOF, Single Point of Failure), mTLS, ACL(Access Control List), Apache Kafka

## Ⅰ. MQTT의 개요

- 핵심 요약 : 대역폭이 좁고 불안정한 망에서 경량 기기가 **발행-구독** 방식으로 메시지를 주고받는 ISO 표준 프로토콜.
- 개념 : IBM과 Arcom이 개발하고 ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission) 20922로 표준화된 **발행-구독** (Publish-Subscribe) 기반의 경량 메시징 프로토콜 (MQTT, Message Queuing Telemetry Transport).
- 배경 및 필요성 : 원격지의 센서가 위성 등 대역이 제한된 구간을 거쳐 데이터를 보내야 할 때, 기존 요청과 응답 방식은 장치마다 연결을 유지해야 해서 배터리와 대역을 낭비했다. 수많은 장치가 데이터를 발행하고 여러 시스템이 필요한 데이터만 받는 구조가 필요해졌다.
- 핵심 목적 : 최소 2바이트 고정 헤더로 오버헤드를 줄이고, 송신자와 수신자를 시간과 공간 측면에서 분리하며, 3단계 **서비스 품질 수준** (QoS, Quality of Service)으로 전달 신뢰성을 선택.

## Ⅱ. MQTT의 특징 및 장점

- 핵심 요약 : 중앙 브로커를 통한 분리 구조와 가벼운 헤더, 상태 유지 기능이 결합되어 대규모 단말 운영을 쉽게 하는 방식.

1. 발행-구독 분리 : 발행자와 구독자는 서로의 주소를 몰라도 되고, 브로커가 토픽 기준으로 전달 → 단말 수가 늘어도 연결 구조가 복잡해지지 않음.
2. 시간 분리 : 구독자가 오프라인이어도 지속 세션을 쓰면 브로커가 메시지를 보관 → 단말이 잠시 끊겨도 데이터 유실이 줄어듦.
3. 경량 헤더 : 최소 2바이트 고정 헤더 → 대역이 좁은 망에서도 메시지 오버헤드가 작음.
4. 단계별 신뢰성 : QoS 0, 1, 2 중에서 메시지 중요도에 맞춰 선택 → 전력과 대역을 아끼거나 정확한 전달을 보장.
5. 상태 감시 기능 : **유언 메시지** (LWT, Last Will and Testament, 비정상 단절 시 브로커가 대신 알리는 메시지), 보관 메시지, Keep Alive → 장애 감지와 최신 상태 제공.

## Ⅲ. MQTT의 구조 (흐름)

- 핵심 요약 : 발행자가 토픽에 메시지를 올리면 브로커가 와일드카드 규칙으로 구독자에게 전달하는 구조.
- **토픽** (Topic) : 슬래시로 계층을 나눈 주제 이름이다. `+`는 한 단계, `#`는 하위 전체와 매칭되는 **와일드카드** (Wildcard)이다.

```text
[ 발행-구독 흐름 ]

온도 센서 (발행자)
   ↓ PUBLISH factory/line1/temp = 28.5
MQTT 브로커
   ↓ 토픽 필터 매칭
구독자 A : factory/+/temp  (설비 관제)
구독자 B : factory/#       (클라우드 수집)
```

```text
[ QoS 2 교환 흐름 ]

발행자 → 브로커 : PUBLISH
발행자 ← 브로커 : PUBREC (수신 기록)
발행자 → 브로커 : PUBREL (해제 요청)
발행자 ← 브로커 : PUBCOMP (완료)
```

- 발행자 → 브로커 → 구독자 사이의 메시지 저장과 재전송은 브로커가 맡는다. 지속 세션을 쓰는 구독자가 재접속하면 브로커가 세션 상태에 따라 대기 중인 메시지를 전달한다.

## Ⅳ. MQTT QoS 레벨의 비교

- 핵심 요약 : QoS는 전달 보장 수준과 교환 횟수가 함께 늘어나므로, 메시지 중요도와 망의 여건에 따라 고른다.

| QoS 레벨 | 보장 수준 | 패킷 교환 | 네트워크 오버헤드 | 적합 분야 |
| --- | --- | --- | --- | --- |
| QoS 0 | 최대 1회 (At most once) | PUBLISH 한 번, 확인 없음 | 최소 | 주기적인 온도, 조도 등 센서 데이터 |
| QoS 1 | 최소 1회 (At least once) | PUBLISH 후 PUBACK 응답까지 재전송 | 중간 (왕복 1회) | 임계치 초과 같은 경보 이벤트 |
| QoS 2 | 정확히 1회 (Exactly once) | PUBLISH, PUBREC, PUBREL, PUBCOMP | 높음 (왕복 2회) | 결제 거래, 원격 장비 정지 명령 |

- 선택 기준 : 중복 수신이 허용되는지와 유실이 허용되는지를 먼저 정하고, 중복과 유실이 모두 허용되지 않을 때 QoS 2를 쓴다.

## Ⅴ. MQTT의 한계와 방안

- 핵심 요약 : 중앙 브로커 집중과 TCP 재연결 비용이 핵심 한계이며, 브로커 클러스터링과 세션 관리 기능으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 중앙 브로커 병목과 단일 장애점 (SPOF, Single Point of Failure) | 대규모 단말이 한 브로커에 몰리면 CPU와 메모리가 고갈되어 시스템 전체가 중단 | 클러스터링을 지원하는 브로커 (EMQX, HiveMQ 등)를 도입하고 로드밸런서로 분산 배치 | 연결 수, 브로커 자원 사용률 |
| TCP 재연결 비용 | 이동 중 단말이 연결을 잃으면 TCP 연결과 TLS 재수립이 반복되어 배터리가 소모 | MQTT 5.0의 세션 만료 간격을 조정하거나, UDP 기반 MQTT-SN (MQTT for Sensor Networks) 채택 | 재연결 횟수, 재연결 소요 시간 |

## Ⅵ. MQTT 적용 및 발전을 위한 기술사적 제언

- 핵심 요약 : MQTT 5.0 기능 활용, 제로 트러스트 보안, 에지-클라우드 2계층 파이프라인 구축 방향.

1. 운영 조직은 MQTT 5.0의 공유 구독으로 후단 소비자의 부하를 나누고, 이유 코드로 오류 원인을 빠르게 진단할 수 있게 해야 한다.
2. 보안 조직은 브로커 앞단에 상호 TLS (mTLS)를 적용하고, JWT (JSON Web Token) 기반으로 토픽별 접근 제어 목록 (ACL)을 관리하며, 페이로드 종단 간 암호화를 기본값으로 두어야 한다. 이는 제로 트러스트 원칙을 단말 영역까지 넓히는 방법이다.
3. 현장 에지에는 경량 브로커를 두고, 백엔드에는 Apache Kafka 같은 스트리밍 플랫폼을 브리지로 연결하는 2계층 파이프라인이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : MQTT는 발행-구독 분리와 QoS 선택으로 제약 망에서 대규모 단말 데이터를 안정적으로 모으는 표준 프로토콜.
- 시사점 : 브로커가 시스템의 중심이므로, 브로커의 가용성과 접근 통제를 설계하는 일이 MQTT 도입의 성패를 가른다.
