---
title: "MQTT(Message Queuing Telemetry Transport)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  question_no: "070"
  keyword_grade: "응용"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- MQTT(Message Queuing Telemetry Transport), 발행-구독(Publish-Subscribe), 브로커(Broker), 토픽(Topic)
- QoS(Quality of Service), LWT(Last Will and Testament), Retained Message, Keep Alive
- 와일드카드(Wildcard), 공유 구독(Shared Subscription), 세션 만료 간격(Session Expiry Interval)
- SPOF(Single Point of Failure), mTLS, ACL(Access Control List)

## Ⅰ. MQTT의 개요

- 핵심 요약 : 대역이 좁고 불안정한 망에서 다수 기기의 메시지를 중개 서버 경유로 주고받는 국제 표준 프로토콜.
- 개념 : OASIS(Organization for the Advancement of Structured Information Standards) 표준이자 ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission) 20922로 제정된 **발행-구독** (Publish-Subscribe, 송신자와 수신자가 주제를 통해 간접 연결되는 메시징 모델) 기반 경량 메시징 프로토콜 (MQTT, Message Queuing Telemetry Transport)로, 발행자와 구독자를 **브로커** (Broker, 메시지를 중개하는 중앙 서버)가 중개.
- 배경 및 필요성 : 요청-응답 방식은 장치마다 상대 주소와 연결을 유지해야 해서 단말 수가 늘수록 배터리와 대역 낭비가 커짐. 다수 장치가 데이터를 올리고 필요한 시스템만 받는 구조가 필요.
- 주요 목적 : 최소 2바이트 헤더의 전송 효율, 송수신자의 시간·공간 분리, 3단계 **QoS** (Quality of Service, 서비스 품질 수준) 선택을 통한 전달 신뢰성 확보.

## Ⅱ. MQTT의 특징 및 장점

- 핵심 요약 : 브로커 중심의 분리 구조와 경량 헤더, 세션 상태 기능이 대규모 단말 운영 효율로 이어지는 구조.

1. 발행-구독 분리 : 발행자와 구독자가 서로의 주소를 몰라도 브로커가 **토픽** (Topic, 슬래시로 계층을 나눈 주제 이름) 기준으로 전달 → 단말 증설에도 연결 구조 불변.
2. 시공간 분리 : 구독자가 오프라인이어도 지속 세션으로 브로커가 메시지 보관 → 단말 접속 단절 구간의 유실 감소.
3. 경량 헤더 : 최소 2바이트 고정 헤더 → 협대역 망에서도 낮은 오버헤드.
4. 단계별 신뢰성 : QoS 0~2를 메시지 중요도에 맞춰 선택 → 전력 절감과 전달 보장의 균형.
5. 상태 감시 : **유언 메시지** (LWT, Last Will and Testament, 비정상 단절 시 브로커가 대신 공지하는 메시지), **보관 메시지** (Retained Message, 토픽의 최신값을 저장해 신규 구독자에게 즉시 제공), Keep Alive(생존 확인 주기 신호) → 장애 감지와 최신 상태 제공.

## Ⅲ. MQTT의 구조 (흐름)

- 핵심 요약 : 발행자가 토픽에 메시지를 올리면 브로커가 구독 필터에 맞춰 구독자에게 전달하는 구조.
- **와일드카드** (Wildcard) : 단계 매칭용 `+`와 하위 전체 매칭용 `#`의 두 종류 필터 문자.

```text
[ 발행-구독 전달 흐름 ]

온도 센서 (발행자)
   ↓ PUBLISH factory/line1/temp
MQTT 브로커
   ↓ 토픽 필터 매칭
구독자 A : factory/+/temp (관제)
구독자 B : factory/# (클라우드 수집)
```

```text
[ QoS 2 완전 4단계 교환 ]

발행자 → 브로커 : PUBLISH
발행자 ← 브로커 : PUBREC (수신 기록)
발행자 → 브로커 : PUBREL (해제 요청)
발행자 ← 브로커 : PUBCOMP (완료)
```

- QoS 2는 PUBLISH, PUBREC, PUBREL, PUBCOMP의 4패킷 교환으로 중복 없는 1회 전달을 보장하는 수준.

## Ⅳ. MQTT QoS 레벨의 비교

- 핵심 요약 : 전달 보장 수준이 올라갈수록 패킷 교환과 오버헤드가 함께 늘어나므로 메시지 성격에 따른 선택 필요.

| QoS 레벨 | 보장 수준 | 패킷 교환 | 오버헤드 | 적합 용도 |
| --- | --- | --- | --- | --- |
| QoS 0 | 최대 1회 (At most once) | PUBLISH 1회, 확인 없음 | 최소 | 주기적 온도·조도 측정치 |
| QoS 1 | 최소 1회 (At least once) | PUBLISH → PUBACK | 중간 (중복 가능) | 임계치 초과 경보 |
| QoS 2 | 정확히 1회 (Exactly once) | PUBLISH, PUBREC, PUBREL, PUBCOMP | 높음 (왕복 2회) | 결제·제어 명령 |

- 선택 기준 :
  1. 유실이 허용되는 주기 데이터는 QoS 0으로 전력·대역 절감.
  2. 중복은 허용되나 유실은 안 되는 경보는 QoS 1.
  3. 중복과 유실 모두 불가한 거래·제어 메시지는 QoS 2.

## Ⅴ. MQTT의 한계와 방안

- 핵심 요약 : 중앙 브로커 집중과 토픽·보안 설계 부실이 주요 한계이며, 클러스터링과 접근 통제 체계로 관리.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 브로커 병목과 단일 장애점(SPOF) | 대규모 단말의 동시 접속 집중 → 시스템 전체 중단 위험 | 클러스터링 지원 브로커 도입과 로드밸런서 분산 배치 | 동시 접속 수, 자원 사용률 |
| 토픽 설계·권한 관리 복잡 | 계층 설계 부실 시 와일드카드 남용과 과잉 권한 발생 | 토픽 네이밍 규칙 수립과 **ACL** (Access Control List, 접근 제어 목록)의 토픽 단위 자동화 | 과잉 권한 계정 수 |
| TCP 재연결 비용 | 이동 단말의 반복 단절 시 연결·TLS(Transport Layer Security) 재수립 부담 | MQTT 5.0의 세션 만료 간격(Session Expiry Interval) 조정, UDP 기반 MQTT-SN(MQTT for Sensor Networks) 검토 | 재연결 횟수, 재연결 소요 시간 |

## Ⅵ. MQTT에 대한 기술사적 제언

- 핵심 요약 : MQTT 5.0 기능 활용, 제로 트러스트 보안 체계, 에지-백엔드 2계층 파이프라인의 3축 제안.

1. 운영 조직은 MQTT 5.0의 **공유 구독** (Shared Subscription, 하나의 구독을 여러 소비자가 나눠 처리하는 기능)으로 후단 소비자의 부하를 분산하고, 이유 코드(Reason Code) 기반 진단으로 장애 원인 파악 시간을 줄여야 한다.
2. 보안 조직은 브로커 접속에 상호 TLS(mTLS) 인증과 토큰 기반 토픽 권한을 적용하고 페이로드 종단 간 암호화를 기본값으로 두어 제로 트러스트 원칙을 단말 영역까지 확장해야 한다.
3. 플랫폼 조직은 현장 에지의 경량 브로커와 백엔드 스트리밍 플랫폼(Apache Kafka 등)을 브리지로 연결하는 2계층 파이프라인으로 수집·분석 역할을 분리해야 한다.

## Ⅶ. 결론

- 핵심 요약 : MQTT는 발행-구독 분리와 QoS 선택으로 제약 망의 대규모 단말 데이터를 모으는 표준 메시징 프로토콜.
- 브로커가 전체 체계의 중심축이므로 브로커의 가용성 설계가 도입 효과를 결정하는 변수가 됨.
