---
title: "트랜잭션 격리 수준"
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

## Ⅰ. 트랜잭션 동시성과 정합성의 균형, 격리 수준(Isolation Level) 개요

### 가. 트랜잭션 격리 수준의 정의
- ANSI/ISO SQL 표준(SQL-92)에서 정의한 것으로, 동시에 실행 중인 여러 트랜잭션 간에 한 트랜잭션이 변경한 데이터를 다른 트랜잭션이 어느 수준까지 볼 수 있도록 허용할 것인가를 결정하는 제어 기준.
- 격리성(Isolation)을 높이면 데이터 정합성이 완벽해지나 시스템 동시성(Throughput)이 급감하고, 격리성을 낮추면 성능은 향상되나 다양한 읽기 이상(Read Phenomena)이 발생함.

### 나. 격리 수준 미비 시 발생하는 3대 전통적 읽기 이상 현상

```text
[ 3대 전통 읽기 이상 현상 ]
1. Dirty Read            : T1이 커밋하지 않은 미확정 변경 데이터를 T2가 읽음 (T1 롤백 시 유령 데이터가 됨)
2. Non-Repeatable Read   : T1이 동일 데이터를 두 번 읽는 사이에 T2가 수정/삭제 후 커밋하여 값이 달라짐
3. Phantom Read          : T1이 범위 조건을 두 번 조회하는 사이에 T2가 새 행을 삽입하여 없던 행이 나타남
```

---

## Ⅱ. ANSI SQL 4대 트랜잭션 격리 수준 및 허용 이상 현상

### 가. 4대 격리 수준 매트릭스 비교

```text
[ 격리 수준과 동시성/정합성 트레이드오프 ]
격리 수준 높음 (정합성 극대화, 동시성 저하)
    ^
    |  [ SERIALIZABLE ]      : Dirty Read (X) | Non-Repeatable Read (X) | Phantom Read (X)
    |  [ REPEATABLE READ ]   : Dirty Read (X) | Non-Repeatable Read (X) | Phantom Read (O*)
    |  [ READ COMMITTED ]    : Dirty Read (X) | Non-Repeatable Read (O) | Phantom Read (O)
    |  [ READ UNCOMMITTED ]  : Dirty Read (O) | Non-Repeatable Read (O) | Phantom Read (O)
    v
격리 수준 낮음 (동시성 극대화, 이상현상 노출)
```

| 격리 수준 (Isolation Level) | Dirty Read | Non-Repeatable Read | Phantom Read | 구현 메커니즘 (로킹 / MVCC) |
| :--- | :--- | :--- | :--- | :--- |
| **READ UNCOMMITTED** | **발생 가능** | **발생 가능** | **발생 가능** | 공유락(S-Lock) 없이 읽기 수행, 배타락(X-Lock) 데이터도 즉시 읽음 |
| **READ COMMITTED** | 방지됨 | **발생 가능** | **발생 가능** | 커밋된 데이터만 읽기 허용. 읽기 시 S-Lock을 걸고 조회 완료 즉시 해제하거나, 쿼리 시작 시점의 MVCC 스냅샷 참조 (오라클, PG 기본값) |
| **REPEATABLE READ** | 방지됨 | 방지됨 | **발생 가능** | 트랜잭션 종료 시까지 S-Lock 유지, 또는 트랜잭션 시작 시점의 MVCC 스냅샷을 트랜잭션 끝까지 고정 (MySQL InnoDB 기본값) |
| **SERIALIZABLE** | 방지됨 | 방지됨 | 방지됨 | 완벽한 직렬 실행 보장. 넥스트 키 락(Next-Key Lock)으로 범위 잠금 또는 SSI(Serializable Snapshot Isolation) 적용 |

*참고: MySQL InnoDB의 경우 REPEATABLE READ 수준에서도 MVCC Undo 로그 기반 스냅샷 읽기와 넥스트 키 락을 통해 일반적인 Phantom Read를 대부분 차단함.

---

## Ⅲ. 현대 DBMS의 스냅샷 격리(Snapshot Isolation) 및 갱신 손실

### 가. 스냅샷 격리(Snapshot Isolation, SI)의 특성
- 트랜잭션 시작 시점의 일관된 데이터베이스 스냅샷 버전을 기반으로 읽기 수행 $\rightarrow$ 읽기 작업은 어떤 락도 요구하지 않음.
- **First-Committer-Wins 원칙** : 두 트랜잭션이 동일 데이터 항목을 동시에 갱신하려 할 때, 먼저 커밋한 트랜잭션만 성공하고 나중 트랜잭션은 롤백(Abort)됨으로써 갱신 분실(Lost Update) 방지.

### 나. 쓰기 편향(Write Skew) 이상 현상

```text
[ 쓰기 편향(Write Skew) 발생 메커니즘 ]
조건: 의사는 최소 1명 이상 대기해야 함 (현재 A, B 2명 대기 중)
T1 (의사 A) : 대기 의사 수 조회 (2명 확인) ---> A 대기 해제 커밋
T2 (의사 B) : 대기 의사 수 조회 (2명 확인) ---> B 대기 해제 커밋
결과: 대기 의사가 0명이 되어 제약조건 위반 발생! (스냅샷 격리에서도 SERIALIZABLE 없이는 방지 불가)
```

---

## Ⅳ. 트랜잭션 격리 수준 설정의 주요 한계점 및 해결 방안

- **동시성(Throughput)과 일관성(Consistency) 간의 상충 트레이드오프** :
  - **한계점** : 격리 수준을 최고 수준(Serializable)으로 설정 시 락 경합 및 트랜잭션 롤백 폭증으로 시스템 처리량이 붕괴되며, 낮추면 더티 리드/팬텀 리드 발생.
  - **해결 방안** : 비즈니스 도메인별 차등 격리 수준 적용(금융 결제는 Serializable/Repeatable Read, 단순 로그/조회는 Read Committed), 낙관적 검증 기법 병행.
- **스냅샷 격리(Snapshot Isolation) 환경에서의 쓰기 편향(Write Skew) 이상** :
  - **한계점** : MVCC 기반 Snapshot Isolation(PostgreSQL/Oracle)은 팬텀 리드를 방지하지만 서로 다른 행을 수정하는 교차 트랜잭션 시 일관성 제약조건 위배 발생.
  - **해결 방안** : 명시적 배타 락(`SELECT FOR UPDATE`)을 통한 직렬화 유도, 또는 직렬성 스냅샷 격리(SSI, Serializable Snapshot Isolation) 엔진 활성화.
- **DBMS 벤더별 격리 수준 구현 메커니즘의 비표준적 파편화** :
  - **한계점** : ANSI SQL 표준 정의와 달리 MySQL(InnoDB)은 갭 락(Gap Lock)으로 팬텀을 방지하고 Oracle은 Read Uncommitted를 지원하지 않는 등 이기종 DB 전환 시 버그 유발.
  - **해결 방안** : 애플리케이션 프레임워크 차원에서 격리 수준 종속 로직을 추상화하고 이종 DBMS 마이그레이션 시 동시성 충돌 통합 테스트 케이스 의무화.

---

## Ⅴ. 엔터프라이즈 환경에서의 격리 수준 설정 실무 제언

- **기본 격리 수준의 최적 선택** : 대다수 글로벌 OLTP 시스템은 동시성 처리량 확보를 위해 **READ COMMITTED** 를 표준으로 사용하고, 특정 중요 트랜잭션(잔액 차감 등)에 한해서만 비관적 락(`SELECT ... FOR UPDATE`)이나 원자적 조건 갱신(`UPDATE SET balance = balance - 100 WHERE balance >= 100`)을 결합하는 것이 정석임.
- **분산 데이터베이스 격리 수준 검증** : 클라우드 네이티브 Spanner, CockroachDB 등 NewSQL 도입 시 글로벌 시계 동기화(TrueTime, HLC)를 기반으로 진정한 직렬성(Strict Serializable)을 제공하는지, 완화된 세션 일관성(Read-your-writes)인지 확인하고 아키텍처를 설계할 것을 제언함.
