---
title: "EDA(이벤트 기반 아키텍처)와 2대 토폴로지(브로커·중재자)"
author: "Antigravity"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 이벤트 기반 아키텍처(EDA)의 개요

- **개념** : 시스템 내부 또는 외부에서 발생한 유의미한 상태 변화인 '이벤트(Event)'를 감지, 생성(발행), 전달, 소비하는 비동기 분산 아키텍처 스타일.
- **배경 및 필요성** : 동기식 REST/RPC 호출 방식의 서비스 간 강결합, 응답 대기로 인한 성능 저하, 한 서비스의 장애가 전체로 전파되는 연쇄 장애(Cascading Failure) 문제를 근본적으로 극복.
- **핵심 3요소** : 이벤트 생산자(Event Producer), 이벤트 브로커(Event Broker/Channel), 이벤트 소비자(Event Consumer).

## Ⅱ. EDA 2대 토폴로지: 브로커(Broker)와 중재자(Mediator)

```text
   [ 1. 브로커 토폴로지 (Broker) ] ──────── 단순 이벤트 체인, 중앙 제어기 없음
    [ Producer ] ──> [ Event Broker (Kafka) ] ──> [ Consumer A ] ──> [ Event Broker ] ──> [ Consumer B ]
    (자율적 분산, 높은 반응성)

   [ 2. 중재자 토폴로지 (Mediator) ] ────── 복잡한 다단계 워크플로우, 중앙 오케스트레이션
    [ Producer ] ──> [ Initial Event ]
                            │
                            ▼
                  [ Event Mediator (중재자) ]
                  ┌─────────┼─────────┐
                  ▼         ▼         ▼
               [작업 1]   [작업 2]   [작업 3]
```

- **브로커 토폴로지 (Broker Topology)** :
  - 중앙의 조정자 없이 이벤트 브로커를 통해 이벤트가 사슬처럼 연쇄적으로 전파(Choreography 방식).
  - 결합도가 극도로 낮고 확장성이 뛰어나 단순 이벤트 알림 및 실시간 데이터 스트리밍에 최적.
- **중재자 토폴로지 (Mediator Topology)** :
  - 초기 이벤트를 수신한 '중재자(오케스트레이터)'가 전체 워크플로우를 통제하며 각 소비자에게 실행 이벤트를 단계별로 지시.
  - 다단계 트랜잭션 처리, 에러 발생 시 보상 트랜잭션(Saga) 조율, 복잡한 비즈니스 프로세스에 필수.

## Ⅲ. 브로커 토폴로지와 중재자 토폴로지의 비교

| 비교 항목 | 브로커 토폴로지 (Broker) | 중재자 토폴로지 (Mediator) |
|---|---|---|
| 제어 방식 | 분산 자율 제어 (코레오그래피, Choreography) | 중앙 집중 제어 (오케스트레이션, Orchestration) |
| 결합도 | 극도로 낮음 (생산자는 소비자를 전혀 모름) | 중간 (중재자가 워크플로우 단계를 알고 있음) |
| 확장성 및 성능 | 극도로 높음 (중앙 병목 없음) | 중재자 성능에 따라 제한될 수 있음 |
| 트랜잭션 복잡도 | 전체 워크플로우 추적 및 에러 처리가 어려움 | 전체 흐름 가시성 우수, 롤백/보상 트랜잭션 용이 |
| 대표 솔루션 | Apache Kafka, AWS SNS/SQS, RabbitMQ | Camunda, AWS Step Functions, Temporal |

## Ⅳ. EDA(이벤트 기반 아키텍처)의 주요 한계점 및 해결 방안

- **결과적 일관성(Eventual Consistency) 및 분산 트랜잭션 추적성 결여** :
  - **한계점** : ACID 트랜잭션의 부재로 인해 시스템 전반의 최종 데이터 정합성 보장이 지연되며, 비동기 파이프라인 내 장애 발생 시 원인 추적이 극도로 난해.
  - **해결 방안** : 사가 패턴(Saga Pattern, 코레오그래피/오케스트레이션) 적용 및 보상 트랜잭션 구현, W3C Trace Context 표준 기반 분산 추적(OpenTelemetry) 전파.
- **이벤트 중복 발행 및 순서 역전(Out-of-Order Delivery)** :
  - **한계점** : 분산 브로커의 At-Least-Once 전달 정책 및 파티션 간 네트워크 지연으로 인해 동일 이벤트 중복 처리 또는 이벤트 역순 수신 시 데이터 오염.
  - **해결 방안** : Transactional Outbox 및 Inbox 패턴 구현, 컨슈머 단 멱등성(Idempotency) 보장 키 설계, 동일 비즈니스 엔티티 단위의 파티션 키(Partition Key) 고정.
- **이벤트 스키마 진화(Schema Evolution)에 따른 호환성 파손** :
  - **한계점** : 이벤트 생산자가 필드를 변경하거나 삭제할 때 이벤트를 구독하는 수많은 비동기 컨슈머 서비스에서 역직렬화 에러 발생.
  - **해결 방안** : Schema Registry(Confluent/Apicurio)를 도입하여 Avro/Protobuf 스키마의 하위 및 양방향 호환성(Full Compatibility) 규칙을 CI/CD 파이프라인에서 강제 검증.

## Ⅴ. EDA 구축 시 기술사적 제언

- **최종 일관성(Eventual Consistency) 및 멱등성(Idempotency) 보장** : 분산 이벤트 환경에서는 네트워크 지연으로 인한 이벤트 중복 수신이나 순서 역전이 발생할 수 있으므로, 소비자는 고유 이벤트 ID(UUID) 기반의 중복 제거 테이블을 두고 멱등하게 처리하도록 설계 필수.
- **트랜잭셔널 아웃박스 패턴(Transactional Outbox Pattern) 적용** : 로컬 DB 트랜잭션 커밋과 메시지 브로커 이벤트 발행 간의 원자성(Atomicity)을 보장하기 위해, DB의 Outbox 테이블에 이벤트를 먼저 기록하고 CDC(Debezium)를 통해 카프카로 비동기 발행하는 패턴 구현 권장.
