---
title: "메시지 큐(Message Queue)"
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

## Ⅰ. 메시지 큐(Message Queue)의 개요

- 개념 : 분산 시스템 및 마이크로서비스 환경에서 프로세스 간(또는 서비스 간)에 데이터를 안전하고 신뢰성 있게 교환하기 위해, 메시지를 메모리나 디스크의 큐(Queue) 버퍼에 비동기(Asynchronous) 방식으로 저장하고 전달하는 메시지 지향 미들웨어(MOM, Message-Oriented Middleware).
- 배경 및 필요성 : 동기식 HTTP REST 호출의 서비스 간 강결합, 피크 시간대 트래픽 폭증으로 인한 서버 다운(Spike Traffic), 한 서비스의 장애가 전체로 번지는 연쇄 장애 문제를 해결.
- 3대 핵심 가치 : 비동기 처리(Asynchronous), 시스템 간 결합도 완화(Decoupling), 피크 부하 흡수(Buffering / Peak Shaving).

## Ⅱ. 메시지 큐 2대 통신 패턴 및 아키텍처

```text
   [ 1. 점대점 패턴 (Point-to-Point : Queue) ]
    [ Producer ] ──> [ Message Queue ] ──> [ Consumer A ] (단 하나의 소비자가 단일 메시지 독점 소비)
                                       ──> [ Consumer B ] (작업 부하 분산: Worker Queue)

   [ 2. 발행-구독 패턴 (Publish-Subscribe : Topic) ]
    [ Producer ] ──> [ Topic / Exchange ] ──┬──> [ Consumer A (주문 서비스) ]
                                            ├──> [ Consumer B (결제 서비스) ]
                                            └──> [ Consumer C (알림 서비스) ]
                     (동일한 이벤트를 다수의 구독자가 독립적으로 복제 수신)
```

- **점대점 패턴** (Point-to-Point) : 큐에 저장된 메시지는 여러 워커 프로세스 중 단 하나에 의해 수신 및 처리되고 즉시 큐에서 삭제 (작업 분산).
- **발행-구독 패턴** (Pub/Sub) : 생산자가 특정 토픽에 메시지를 발행하면, 해당 토픽을 구독하고 있는 모든 소비자에게 메시지가 브로드캐스트 전달.

## Ⅲ. 대표 메시지 브로커 솔루션 비교 (Kafka vs RabbitMQ)

| 비교 항목 | RabbitMQ | Apache Kafka | AWS SQS |
|---|---|---|---|
| 기반 철학 | 전통적인 고신뢰 스마트 브로커 (AMQP 표준) | 고성능 분산 분산 커밋 로그 (Dumb Broker, Smart Consumer) | 클라우드 완전 관리형 경량 큐 |
| 메시지 보관 방식 | 소비자가 메시지를 읽고 ACK하면 큐에서 즉시 삭제 | 디스크에 로그 세그먼트로 영구 보관 (Retention 기간 유지) | 최대 14일 보관 후 자동 삭제 |
| 재처리 (Replay) | 불가 (이미 소비된 메시지 복구 불가) | 오프셋(Offset)을 뒤로 돌려 과거 이벤트 완벽 재처리 가능 | 불가 |
| 처리 성능 및 처리량 | 초당 수만 건 (라우팅 복잡도에 따라 제한) | 초당 수십만~수백만 건 (Sequential Disk I/O, Zero-Copy) | 초당 수천~수만 건 자동 확장 |
| 라우팅 유연성 | 최고 (Exchange 바인딩 키 기반 세밀한 라우팅) | 단순 토픽 및 파티션 기반 라우팅 | 단순 FIFO 또는 표준 큐 |
| 주 활용 분야 | 복잡한 백엔드 작업 분산, 금융 트랜잭션 | 대규모 실시간 로그 수집, 이벤트 소싱, 실시간 스트리밍 | 클라우드 네이티브 서버리스 비동기 처리 |

## Ⅳ. 메시지 큐(Message Queue)의 주요 한계점 및 해결 방안

- **메시지 중복 전달** (Duplicate Delivery)로 인한 데이터 오염 :
  - 한계점 : 네트워크 분할이나 컨슈머 처리 지연으로 ACK 응답이 유실될 경우 분산 브로커의 At-Least-Once 전달 특성상 동일 메시지가 재수신되어 중복 연산 발생.
  - 해결 방안 : 컨슈머 측 멱등성(Idempotent Consumer) 패턴 구현, 메시지 고유 식별자(ID) 기반 분산 락(Redis) 및 DB 유니크 인덱스 중복 체크 로직 적용.
- 컨슈머 처리 지연에 따른 **큐 적체** (Backpressure) 및 브로커 리소스 고갈 :
  - 한계점 : 생산 속도가 소비 속도를 지속 초과할 경우 메시지가 큐에 누적되어 브로커의 메모리 및 디스크 용량 한계 도달 및 시스템 전체 다운.
  - 해결 방안 : 컨슈머 수평 오토스케일링(KEDA, K8s Event-driven Autoscaling), 배압(Backpressure) 제어 메커니즘 및 디스크 임계치 초과 전 메시지 아카이빙.
- **독성 메시지** (Poison Pill)로 인한 컨슈머 파이프라인 블로킹 :
  - 한계점 : 역직렬화 오류나 비즈니스 예외를 유발하는 잘못된 포맷의 메시지가 지속적으로 재시도(Retry)되면서 후속 메시지 처리가 전면 중단됨.
  - 해결 방안 : 지수 백오프(Exponential Backoff) 기반 최대 재시도 횟수 제한, 실패 메시지를 즉시 격리 분석하는 Dead Letter Queue(DLQ) 아키텍처 필수 구성.

## Ⅴ. 고가용성 메시징 시스템 구축 시 기술사적 제언

- **적어도 한 번** (At-Least-Once) 전송과 소비자 멱등성(Idempotency) 구현 : 네트워크 단절이나 컨슈머 재부팅 시 메시지 중복 수신이 필연적으로 발생하므로, 비즈니스 로직에 Redis나 RDB의 유니크 키를 활용한 멱등성 처리 레이어를 반드시 구현해야 데이터 중복 처리(이중 결제 등)를 방지할 수 있음.
- **데드 레터 큐** (DLQ, Dead Letter Queue) 기반의 독약 메시지(Poison Message) 격리 : 데이터 포맷 오류 등으로 인해 소비자가 계속 예외를 발생시키며 무한 재시도하는 독약 메시지가 발생하면 전체 큐가 정체되므로, 재시도 한도 초과 시 해당 메시지를 DLQ로 즉각 격리하고 관측성 알람을 발송하는 안전망 구축 필수.
