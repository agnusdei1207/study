---
title: "트랜잭션(ACID)"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 데이터베이스 무결성의 논리적 작업 단위, 트랜잭션의 개요

### 가. 트랜잭션(Transaction)의 정의
- **트랜잭션** : **데이터베이스 관리 시스템** (DBMS)에서 하나의 논리적 기능을 완벽히 수행하기 위해 더 이상 쪼갤 수 없는 일련의 데이터베이스 조작 연산(DML)들의 묶음.
- 시스템 장애나 다중 사용자의 동시 접근 상황에서도 데이터의 일관성과 정합성을 완벽하게 보장하기 위한 원자적 작업 단위.

---

## Ⅱ. 트랜잭션의 4대 핵심 특성(ACID) 심층 분석

```text
[ 트랜잭션 4대 특성 ACID ]
1. 원자성 (Atomicity)   : All or Nothing (모두 실행되거나, 아무것도 실행되지 않음)
2. 일관성 (Consistency) : 실행 전후 데이터베이스는 항상 유효한 제약조건 상태 유지
3. 격리성 (Isolation)   : 동시 실행 트랜잭션들은 서로의 중간 상태를 볼 수 없음
4. 영속성 (Durability)  : 성공적으로 커밋된 결과는 시스템 장애 후에도 영구 보존
```

### 가. ACID 세부 특성 및 DBMS 내부 구현 메커니즘

| 특성 | 핵심 정의 및 보장 원칙 | DBMS 내부 구현 기술 | 실패/장애 시 대응 |
| :--- | :--- | :--- | :--- |
| **원자성 (Atomicity)** | 트랜잭션에 포함된 모든 연산이 완벽히 성공(Commit)하거나, 단 하나라도 실패하면 전체가 취소(Rollback)되어야 함 | **Undo 로그 (Undo Log / Rollback Segment)** | 실패 시 Undo 로그를 역순으로 실행하여 변경 전 상태로 완벽 복구 |
| **일관성 (Consistency)** | 트랜잭션 실행 전 데이터베이스가 일관된 상태였다면, 실행 후에도 모든 무결성 제약조건(PK, FK, Check 등)을 준수해야 함 | **무결성 제약조건 강제, 데이터베이스 트리거, 직렬성 제어** | 제약조건 위반 트랜잭션은 즉시 Abort 후 롤백 |
| **격리성 (Isolation)** | 여러 트랜잭션이 동시에 실행되더라도, 각 트랜잭션은 다른 트랜잭션이 끼어들지 않은 것처럼 독립적으로 동작해야 함 | **2단계 로킹(2PL), 다중 버전 동시성 제어(MVCC)** | 격리 수준(Read Committed, Repeatable Read 등) 설정으로 제어 |
| **영속성 (Durability)** | 트랜잭션이 일단 성공적으로 커밋되면, 직후에 정전이나 OS 크래시가 발생하더라도 그 결과는 디스크에 영구히 보존되어야 함 | **Redo 로그 (Write-Ahead Logging, WAL), 체크포인트(Checkpoint)** | 재부팅 시 Redo 로그를 재실행(Replay)하여 메모리 미반영 변경 복원 |

---

## Ⅲ. WAL(Write-Ahead Logging)과 트랜잭션 상태 전이

### 가. WAL(Write-Ahead Logging)의 절대 원칙
- 실제 데이터 페이지(Data Page)를 디스크에 플러시(Flush)하기 전에, 반드시 해당 변경에 대한 **로그 레코드** (Redo/Undo Log)를 디스크의 로그 파일에 먼저 영구 기록 해야 함.
- 랜덤 I/O인 데이터 페이지 쓰기를 지연(Lazy Write)시키고, 순차 I/O인 WAL 기록만으로 영속성을 즉시 보장하여 DBMS 성능을 극대화함.

### 나. 트랜잭션 5대 상태 전이도

```text
[ 트랜잭션 상태 전이 다이어그램 ]
[활동 (Active)] ---> (연산 정상 수행) ---> [부분 완료 (Partially Committed)]
       |                                                 |
  (오류 발생)                                       (로그 디스크 기록 성공)
       |                                                 v
       +----------------------------------------> [완료 (Committed)]
       |
       v
 [실패 (Failed)] ---> (Undo 롤백 수행) ---> [철회 (Aborted)]
```

---

## Ⅳ. 트랜잭션 관리의 주요 한계점 및 해결 방안

- 분산 환경(MSA)에서 2단계 커밋(2PC)의 블로킹 및 성능 저하 :
  - 한계점 : 코디네이터(Coordinator) 장애 시 참여 노드들이 락을 유지한 채 블로킹(Blocking)되어 전체 분산 시스템 가용성(Availability) 급감.
  - 해결 방안 : 엄격한 2PC 대신 사가(Saga) 패턴(보상 트랜잭션 기반 최종 일관성) 채택, 아웃박스 패턴(Transactional Outbox)과 이벤트 브로커(Kafka) 결합 비동기 정합성 확보.
- 높은 트랜잭션 격리 수준(Serializable)에 따른 동시성 저하 및 데드락 :
  - 한계점 : 완벽한 격리성 보장을 위해 테이블 및 범위 락(Gap Lock, Next-Key Lock)이 광범위하게 발생하여 TPS 급락 및 락 타임아웃 빈발.
  - 해결 방안 : 격리 수준을 Read Committed 또는 Repeatable Read로 하향 조정하고, 다중 버전 동시성 제어(MVCC) 및 낙관적 락(Optimistic Locking: Version Column) 기법 병행.
- WAL(Write-Ahead Logging) 플러시(fsync) 오버헤드 및 디스크 I/O 병목 :
  - 한계점 : 트랜잭션 지속성(Durability) 보장을 위한 매 커밋 시점의 디스크 fsync 호출로 인해 고성능 쓰기 워크로드에서 스토리지 I/O 병목 유발.
  - 해결 방안 : 그룹 커밋(Group Commit) 메커니즘을 통한 로그 버퍼 일괄 플러시, 고속 NVMe SSD 및 배터리 백업 캐시(BBU/NVDIMM) 기반 스토리지 도입.

## Ⅴ. 분산 환경에서의 트랜잭션 실무 제언

- 분산 환경에서의 BASE와 Saga 패턴 전환 : 마이크로서비스(MSA) 환경에서 네트워크를 가로지르는 글로벌 2PC(Two-Phase Commit)는 심각한 시스템 블로킹을 유발하므로, 엄격한 ACID를 서비스 내부로 국한하고 서비스 간에는 이벤트 기반 보상 트랜잭션(Compensating Transaction) 중심의 **Saga 패턴** 을 채택하여 최종 일관성을 달성해야 함.
- 트랜잭션 바운더리 최소화 원칙 : 트랜잭션 블록(`@Transactional`) 내부에 이메일 발송, 결제 게이트웨이(PG) 외부 HTTP API 호출 등 네트워크 지연 요소를 절대 포함하지 말고, 순수한 DB DML 연산만 격리하여 커넥션 풀 고갈과 락 대기 시간을 방지할 것을 제언함.
