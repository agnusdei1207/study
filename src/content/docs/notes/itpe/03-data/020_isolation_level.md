---
title: "트랜잭션 격리 수준"
author: "agnusdei1207"
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

## 연관 키워드

- 트랜잭션 격리 수준(Isolation Level), ANSI(American National Standards Institute)/ISO(International Organization for Standardization) SQL(Structured Query Language) 표준, 동시성(Concurrency), 정합성(Consistency)
- Dirty Read, Non-Repeatable Read, Phantom Read, MVCC(Multi-Version Concurrency Control), 스냅샷 격리(Snapshot Isolation), 쓰기 편향(Write Skew), SSI(Serializable Snapshot Isolation)

## Ⅰ. 트랜잭션 격리 수준의 개요

- 핵심 요약 : 동시 실행 트랜잭션 간 변경 데이터의 가시성 수준을 결정하는 ANSI/ISO SQL 표준 제어 기준.
- 개념 : ANSI(American National Standards Institute)/ISO(International Organization for Standardization) SQL(Structured Query Language) 표준(SQL-92)에서 정의한, 동시 실행 트랜잭션 간 한 트랜잭션의 변경 데이터를 다른 트랜잭션이 어느 수준까지 볼 수 있는지 결정하는 제어 기준, 트랜잭션 격리 수준(Isolation Level).
- 배경 및 필요성 : 격리성(Isolation) 상향 시 데이터 정합성은 완벽하나 시스템 동시성(Throughput) 급감, 하향 시 성능 향상과 함께 다양한 읽기 이상(Read Phenomena) 발생.
- 주요 목적 : 동시성과 정합성 사이의 균형점 제시를 통한 트랜잭션 처리 품질 기준 확립.

## Ⅱ. 트랜잭션 격리 수준의 특징

- 핵심 요약 : 4단계 표준 수준, 격리성-동시성 트레이드오프, 로킹과 MVCC 병행 구조.

1. ANSI/ISO SQL 표준(SQL-92) 기반의 4단계 격리 수준 체계.
2. 격리 수준 상승에 따른 정합성 강화·동시성 저하의 트레이드오프 구조.
3. 3대 읽기 이상(Dirty Read, Non-Repeatable Read, Phantom Read)의 수준별 방지 차등.
4. 공유락(S-Lock)/배타락(X-Lock) 로킹과 MVCC(Multi-Version Concurrency Control) 스냅샷의 병행 구현.
5. 벤더별 구현 편차 존재 (MySQL 갭 락(Gap Lock), Oracle의 Read Uncommitted 미지원 등).

## Ⅲ. 트랜잭션 격리 수준의 구조 (흐름)

- 핵심 요약 : 3대 읽기 이상 현상과 4대 격리 수준의 계층 구조, 스냅샷 격리의 동작 및 쓰기 편향 한계.

```text
[ 3대 전통 읽기 이상 현상 ]
1. Dirty Read          : T1의 커밋하지 않은 미확정 변경 데이터를 T2가 읽음 (T1 롤백 시 유령 데이터)
2. Non-Repeatable Read : T1의 동일 데이터 2회 읽기 사이 T2가 수정·삭제 후 커밋하여 값 변동
3. Phantom Read        : T1의 범위 조건 2회 조회 사이 T2가 새 행을 삽입하여 없던 행 등장
```

- 격리 수준과 동시성/정합성 트레이드오프.

```text
[ 격리 수준 계층 ]
격리 수준 높음 (정합성 극대화, 동시성 저하)
    ^
    |  [ SERIALIZABLE ]      : Dirty Read (X) | Non-Repeatable Read (X) | Phantom Read (X)
    |  [ REPEATABLE READ ]   : Dirty Read (X) | Non-Repeatable Read (X) | Phantom Read (O*)
    |  [ READ COMMITTED ]    : Dirty Read (X) | Non-Repeatable Read (O) | Phantom Read (O)
    |  [ READ UNCOMMITTED ]  : Dirty Read (O) | Non-Repeatable Read (O) | Phantom Read (O)
    v
격리 수준 낮음 (동시성 극대화, 이상현상 노출)
```

- 스냅샷 격리(Snapshot Isolation, SI) 특성 : 트랜잭션 시작 시점의 일관된 데이터베이스 스냅샷 버전 기반 읽기, 읽기 작업의 락 불요.
- First-Committer-Wins 원칙 : 동일 데이터 항목 동시 갱신 시 먼저 커밋한 트랜잭션만 성공, 나중 트랜잭션의 롤백(Abort) 처리를 통한 갱신 분실(Lost Update) 방지.
- 쓰기 편향(Write Skew) 이상 현상.

```text
[ 쓰기 편향(Write Skew) 발생 메커니즘 ]
조건: 의사는 최소 1명 이상 대기해야 함 (현재 A, B 2명 대기 중)
T1 (의사 A) : 대기 의사 수 조회 (2명 확인) ---> A 대기 해제 커밋
T2 (의사 B) : 대기 의사 수 조회 (2명 확인) ---> B 대기 해제 커밋
결과: 대기 의사 0명으로 제약조건 위반 발생 (스냅샷 격리에서 SERIALIZABLE 없이는 방지 불가)
```

## Ⅳ. 4대 트랜잭션 격리 수준의 비교

- 핵심 요약 : 수준별 허용 이상 현상과 로킹·MVCC 기반 구현 메커니즘의 차이.

| 격리 수준 (Isolation Level) | Dirty Read | Non-Repeatable Read | Phantom Read | 구현 메커니즘 (로킹 / MVCC) |
|---|---|---|---|---|
| READ UNCOMMITTED | 발생 가능 | 발생 가능 | 발생 가능 | 공유락(S-Lock) 없이 읽기 수행, 배타락(X-Lock) 데이터도 즉시 읽음 |
| READ COMMITTED | 방지됨 | 발생 가능 | 발생 가능 | 커밋된 데이터만 읽기 허용. 읽기 시 S-Lock 획득 후 조회 완료 즉시 해제하거나 쿼리 시작 시점 MVCC 스냅샷 참조 (오라클, PG 기본값) |
| REPEATABLE READ | 방지됨 | 방지됨 | 발생 가능 | 트랜잭션 종료 시까지 S-Lock 유지, 또는 트랜잭션 시작 시점 MVCC 스냅샷의 트랜잭션 끝까지 고정 (MySQL InnoDB 기본값) |
| SERIALIZABLE | 방지됨 | 방지됨 | 방지됨 | 성공 트랜잭션 결과의 어떤 직렬 실행과의 동등성 보장(실제 순차 실행 의미 아님). 넥스트 키 락(Next-Key Lock) 범위 잠금 또는 SSI(Serializable Snapshot Isolation) 적용 |

※ 참고: MySQL InnoDB의 경우 REPEATABLE READ 수준에서도 MVCC Undo 로그 기반 스냅샷 읽기와 넥스트 키 락을 통해 일반적인 Phantom Read를 대부분 차단.

## Ⅴ. 트랜잭션 격리 수준의 장점과 한계

- 핵심 요약 : 정합성 제어 표준화와 무잠금 읽기의 장점, 동시성 상충·쓰기 편향·벤더 파편화의 한계.
- 장점
  1. 표준화된 정합성 제어 기준을 통한 이기종 환경 공통 언어 확보.
  2. MVCC 기반 스냅샷 읽기를 통한 읽기-쓰기 간섭 최소화.
  3. 비즈니스 요구에 따른 수준별 유연한 선택 가능.
- 한계점 1 : 동시성(Throughput)과 일관성(Consistency) 간의 상충 트레이드오프
  - 한계점 : 최고 수준(Serializable) 설정 시 락 경합·트랜잭션 롤백 폭증으로 시스템 처리량 붕괴, 하향 시 더티 리드·팬텀 리드 노출.
  - 해결 방안 : 비즈니스 도메인별 차등 격리 수준 적용(금융 결제는 Serializable/Repeatable Read, 단순 로그·조회는 Read Committed), 낙관적 검증 기법 병행.
- 한계점 2 : 스냅샷 격리(Snapshot Isolation) 환경에서의 쓰기 편향(Write Skew) 이상
  - 한계점 : MVCC 기반 Snapshot Isolation(PostgreSQL/Oracle)의 팬텀 리드 방지에도 불구, 서로 다른 행을 수정하는 교차 트랜잭션 시 일관성 제약조건 위배 발생.
  - 해결 방안 : 명시적 배타 락(`SELECT FOR UPDATE`)을 통한 직렬화 유도, 또는 직렬성 스냅샷 격리(SSI, Serializable Snapshot Isolation) 엔진 활성화.
- 한계점 3 : DBMS(Database Management System) 벤더별 구현 메커니즘의 비표준적 파편화
  - 한계점 : ANSI SQL 표준 정의와 달리 MySQL(InnoDB)의 갭 락(Gap Lock) 기반 팬텀 방지, Oracle의 Read Uncommitted 미지원 등 이기종 DB(Database) 전환 시 버그 유발.
  - 해결 방안 : 애플리케이션 프레임워크 차원의 격리 수준 종속 로직 추상화, 이종 DBMS 마이그레이션 시 동시성 충돌 통합 테스트 케이스 의무화.

## Ⅵ. 트랜잭션 격리 수준에 대한 기술사적 제언

- 핵심 요약 : 기본 격리 수준의 표준화와 중요 트랜잭션 락 결합, 분산 데이터베이스 직렬성 검증.
- 기본 격리 수준의 최적 선택 : 대다수 글로벌 OLTP(Online Transaction Processing) 시스템의 동시성 처리량 확보용 READ COMMITTED 표준 채택, 중요 트랜잭션(잔액 차감 등)에 한한 비관적 락(`SELECT ... FOR UPDATE`)이나 원자적 조건 갱신(`UPDATE SET balance = balance - 100 WHERE balance >= 100`) 결합 권장.
- 분산 데이터베이스 격리 수준 검증 : 클라우드 네이티브 Spanner, CockroachDB 등 NewSQL 도입 시 글로벌 시계 동기화(TrueTime, HLC, Hybrid Logical Clock) 기반 진정한 직렬성(Strict Serializable) 제공 여부, 완화된 세션 일관성(Read-your-writes) 여부 확인 후 아키텍처 설계 필요.

## Ⅶ. 결론

- 핵심 요약 : 격리 수준은 동시성과 정합성의 균형을 설계하는 핵심 기준이나, 벤더 편차·스냅샷 한계 이해가 수반되어야 하는 개념.
- 요약 : 4단계 표준 수준과 3대 읽기 이상의 대응 관계, 로킹·MVCC 구현 메커니즘을 통한 트랜잭션 품질 제어.
- 시사점 : 도메인별 차등 적용, SSI·명시적 락 보완, 분산 환경 직렬성 검증을 통한 확장성과 정합성의 균형 확보 필요.
