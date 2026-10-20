---
title: "EDA(이벤트 기반 아키텍처)와 2대 토폴로지(브로커·중재자) (EDA: Event-Driven Architecture)"
author: "agnusdei1207"
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

## 연관 키워드

- EDA(Event-Driven Architecture), 이벤트 생산자(Event Producer), 이벤트 브로커(Event Broker), 이벤트 소비자(Event Consumer)
- 브로커 토폴로지, 중재자 토폴로지, 코레오그래피(Choreography), 오케스트레이션(Orchestration), 사가 패턴(Saga Pattern), 멱등성(Idempotency), Transactional Outbox

## Ⅰ. EDA의 개요

- 핵심 요약 : 유의미한 상태 변화인 이벤트의 감지·발행·전달·소비로 시스템을 구성하는 비동기 분산 아키텍처 스타일.
- 개념 : 시스템 내부 또는 외부에서 발생한 유의미한 상태 변화인 이벤트(Event)를 감지, 생성(발행), 전달, 소비하는 비동기 분산 아키텍처 스타일(EDA, Event-Driven Architecture).
- 배경 및 필요성 : 동기식 REST(Representational State Transfer)/RPC(Remote Procedure Call) 호출 방식의 서비스 간 강결합, 응답 대기에 따른 성능 저하, 한 서비스 장애의 전체 전파인 연쇄 장애(Cascading Failure) 문제의 근본적 극복.
- 핵심 3요소 : 이벤트 생산자(Event Producer), 이벤트 브로커(Event Broker/Channel), 이벤트 소비자(Event Consumer).

## Ⅱ. EDA의 특징

- 핵심 요약 : 비동기 메시징 기반의 낮은 결합도와 브로커·중재자 2대 토폴로지의 선택적 운용.

1. 비동기 메시징 : 생산자와 소비자 간 응답 대기 없는 발행-구독(Publish-Subscribe) 통신.
2. 낮은 결합도 : 생산자가 소비자의 존재를 알지 못하는 느슨한 결합(Loose Coupling).
3. 브로커 토폴로지(Broker Topology) : 중앙 조정자 없는 연쇄적 이벤트 전파(코레오그래피, Choreography) 방식, 단순 이벤트 알림 및 실시간 데이터 스트리밍에 최적.
4. 중재자 토폴로지(Mediator Topology) : 중재자(오케스트레이터)의 단계별 워크플로우 통제, 다단계 트랜잭션 처리 및 에러 시 보상 트랜잭션(Saga) 조율에 필수.
5. 결과적 일관성(Eventual Consistency) : 즉시 일관성 대신 최종 데이터 정합성을 지향하는 트레이드오프 구조.

## Ⅲ. EDA의 구조 (흐름)

- 핵심 요약 : 중앙 제어 없는 브로커 토폴로지와 중앙 오케스트레이션형 중재자 토폴로지의 이원 구조.
- 브로커 토폴로지(Broker Topology).

```text
[ Producer ] -> [ Event Broker (Kafka) ]
    │
    ▼ (Consumer A 소비 후 재발행)
[ Event Broker ] -> [ Consumer B ]
(자율적 분산, 높은 반응성, 중앙 제어기 없음)
```

- 중재자 토폴로지(Mediator Topology).

```text
[ Producer ] -> [ Initial Event ]
    │
    ▼
[ Event Mediator (중재자) ]
    ├─> [작업 1]
    ├─> [작업 2]
    └─> [작업 3]
(복잡한 다단계 워크플로우, 단계별 실행 이벤트 지시)
```

## Ⅳ. 브로커 토폴로지와 중재자 토폴로지의 비교

- 핵심 요약 : 분산 자율 제어의 확장성 극대화형과 중앙 집중 제어의 흐름 가시성형의 선택 기준.

| 비교 항목 | 브로커 토폴로지 (Broker) | 중재자 토폴로지 (Mediator) |
|---|---|---|
| 제어 방식 | 분산 자율 제어 (코레오그래피, Choreography) | 중앙 집중 제어 (오케스트레이션, Orchestration) |
| 결합도 | 극도로 낮음 (생산자는 소비자를 전혀 모름) | 중간 (중재자가 워크플로우 단계를 알고 있음) |
| 확장성 및 성능 | 극도로 높음 (중앙 병목 없음) | 중재자 성능에 따라 제한 가능 |
| 트랜잭션 복잡도 | 전체 워크플로우 추적 및 에러 처리 곤란 | 전체 흐름 가시성 우수, 롤백/보상 트랜잭션 용이 |
| 대표 솔루션 | Apache Kafka, AWS(Amazon Web Services) SNS(Simple Notification Service)/SQS, RabbitMQ | Camunda, AWS Step Functions, Temporal |

## Ⅴ. EDA의 장점과 한계

- 핵심 요약 : 낮은 결합도와 확장성·반응성의 이점, 결과적 일관성과 이벤트 중복·스키마 호환성의 한계.
- 장점

  1. 극도로 낮은 결합도에 기반한 독립적 확장 및 높은 반응성.
  2. 부분 장애의 전파 차단을 통한 연쇄 장애(Cascading Failure) 완화.
  3. 실시간 데이터 스트리밍 및 이벤트 재처리의 용이성.
- 한계점 1 : 결과적 일관성(Eventual Consistency) 및 분산 트랜잭션 추적성 결여
  - 한계점 : ACID(Atomicity, Consistency, Isolation, Durability) 트랜잭션 부재로 인한 시스템 전반 최종 데이터 정합성 보장 지연, 비동기 파이프라인 장애 시 원인 추적 난해.
  - 해결 방안 : 사가 패턴(Saga Pattern, 코레오그래피/오케스트레이션) 적용 및 보상 트랜잭션 구현, W3C(World Wide Web Consortium) Trace Context 표준 기반 분산 추적(OpenTelemetry) 전파.
- 한계점 2 : 이벤트 중복 발행 및 순서 역전(Out-of-Order Delivery)
  - 한계점 : 분산 브로커의 At-Least-Once 전달 정책 및 파티션 간 네트워크 지연으로 인한 동일 이벤트 중복 처리 또는 역순 수신 시 데이터 오염.
  - 해결 방안 : Transactional Outbox 및 Inbox 패턴 구현, 컨슈머 단 멱등성(Idempotency) 보장 키 설계, 동일 비즈니스 엔티티 단위 파티션 키(Partition Key) 고정.
- 한계점 3 : 이벤트 스키마 진화(Schema Evolution)에 따른 호환성 파손
  - 한계점 : 이벤트 생산자의 필드 변경·삭제 시 구독 중인 다수 비동기 컨슈머 서비스에서 역직렬화 에러 발생.
  - 해결 방안 : Schema Registry(Confluent/Apicurio) 도입을 통한 Avro/Protobuf 스키마의 하위 및 양방향 호환성(Full Compatibility) 규칙의 CI/CD(Continuous Integration/Continuous Delivery) 파이프라인 강제 검증.

## Ⅵ. EDA 구축에 대한 기술사적 제언

- 핵심 요약 : 멱등성 보장 설계와 트랜잭셔널 아웃박스 패턴의 표준 적용.
- 최종 일관성(Eventual Consistency) 및 멱등성(Idempotency) 보장 : 네트워크 지연에 따른 이벤트 중복 수신이나 순서 역전 발생 가능성을 고려하여, 소비자의 고유 이벤트 ID(UUID, Universally Unique Identifier) 기반 중복 제거 테이블 운영 및 멱등 처리 설계 필수.
- 트랜잭셔널 아웃박스 패턴(Transactional Outbox Pattern) 적용 : 로컬 DB(Database) 트랜잭션 커밋과 메시지 브로커 이벤트 발행 간 원자성(Atomicity) 보장을 위해, DB의 Outbox 테이블 우선 기록 후 Debezium 등 CDC(Change Data Capture) 도구를 통한 카프카 비동기 발행 패턴 구현 권장.

## Ⅶ. 결론

- 핵심 요약 : EDA는 결합도 최소화와 확장성을 얻는 대신 일관성·추적성 설계를 요구하는 아키텍처 스타일.
- 요약 : 이벤트의 비동기 발행-소비 구조와 브로커·중재자 2대 토폴로지의 상황별 선택 체계.
- 시사점 : 사가 패턴 기반 보상 트랜잭션, 멱등성·아웃박스 패턴, 스키마 레지스트리 거버넌스가 안정적 EDA 운영의 3대 축.
