---
sidebar:
  order: 86
  label: "086. 트랜잭션 격리 수준 4단계"
  badge:
    text: "기출 · 70%"
    variant: note
title: "트랜잭션 격리 수준 4단계 (Transaction Isolation Levels)"
date: "2026-09-07T10:05:00+09:00"
tags:
  - "notes-software"
weight: 86
extra:
  question_no: "086"
  source_status: "기출"
  source_history: "120회, 138회"
  priority: 70
  priority_note: "120•138회 반복, 격리수준•이상현상 중요"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **트랜잭션 격리 수준(Isolation Level)**: 다중 트랜잭션이 동시 실행될 때, 다른 트랜잭션의 변경 사항을 어느 수준까지 격리하여 조회할지 규정한 ANSI/ISO SQL 표준.
- **3대 읽기 이상 현상**: Dirty Read(미커밋 데이터 조회), Non-Repeatable Read(동일 행 재조회 시 값 변경), Phantom Read(범위 재조회 시 유령 행 출현).

</details>

- 정의/개념: 다중 트랜잭션 동시 실행 시 나타나는 읽기 이상 현상을 제어하기 위해 **Read Uncommitted부터 Serializable까지 4단계로 직렬화 수준을 규정**한 동시성 표준
- 배경/필요성: 완벽한 직렬성 강제 시의 **극심한 락 경합 및 동시 처리량 급락과, 제어 부재 시의 3대 읽기 이상 현상(Dirty·Non-Repeatable·Phantom Read) 발생 한계**

#### 한줄 요약
- 4단계 격리 수준과 MVCC/Lock 메커니즘을 통해 동시 처리량과 정합성 간의 최적 균형을 달성한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **Read View(MVCC 스냅샷)**: 트랜잭션이 시작될 때 활성 중인 타 트랜잭션 ID 목록을 캡처하여 일관된 과거 버전을 읽게 해주는 가시성 판정 뷰.
- **Next-Key Lock**: MySQL InnoDB에서 레코드 락(Record Lock)과 갭 락(Gap Lock)을 결합하여 Repeatable Read에서도 팬텀 리드를 원천 방어하는 기술.

</details>

- **ANSI/ISO SQL 92 표준 4단계** 격리 수준 계층화
- 격리 수준 상승에 따른 **Dirty Read, Non-Repeatable Read, Phantom Read 단계적 차단**
- 엔진별 기본값 상이 (MySQL InnoDB: **Repeatable Read**, Oracle/PostgreSQL: **Read Committed**)

#### 한줄 요약
- 레벨 상승에 따라 읽기 이상 현상을 순차 차단하되, 동시 처리 성능과의 트레이드오프를 고려한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **4단계 격리 수준 매트릭스**: Level 0(RU) $\to$ Level 1(RC) $\to$ Level 2(RR) $\to$ Level 3(Serializable).

</details>

```text
[트랜잭션 격리 수준 4단계 체계]
  │
  ├─ [Level 0: Read Uncommitted] (Dirty Read 발생·커밋 전 변경 노출)
  │
  ├─ [Level 1: Read Committed] (Dirty Read 차단·Oracle/PG 기본값)
  │
  ├─ [Level 2: Repeatable Read] (Non-Repeatable Read 차단·MySQL 기본값)
  │
  └─ [Level 3: Serializable] (Phantom Read 차단·완전 직렬화 실행)
```
- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 격리 수준 | Dirty Read | Non-Repeatable Read | Phantom Read | 주요 DBMS 기본값 |
|:---|:---:|:---:|:---:|:---|
| Read Uncommitted (Level 0) | **발생 (위험)** | 발생 | 발생 | 거의 미사용 |
| Read Committed (Level 1) | **차단 (Safe)** | **발생 (허용)** | 발생 | **Oracle, PostgreSQL, SQL Server** |
| Repeatable Read (Level 2) | **차단 (Safe)** | **차단 (Safe)** | 발생 (*InnoDB 차단)| **MySQL (InnoDB Engine)** |
| Serializable (Level 3) | **차단 (Safe)** | **차단 (Safe)** | **차단 (Safe)** | 특수 금융 원장 등 극히 제한적 사용 |

#### 한줄 요약
- 상위 레벨은 하위 레벨이 막던 이상 현상을 그대로 포함하며 하나씩 더 차단하는 누적 구조이므로, 안전성이 단조 증가하는 만큼 잠금 보유 시간과 스냅샷 유지 비용도 같은 순서로 쌓인다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **Undo 체인 역추적**: 대상 레코드의 롤백 포인터(`DB_ROLL_PTR`)를 따라가며 현재 트랜잭션의 Read View에 부합하는 과거 버전을 찾아내는 과정.

</details>

```text
트랜잭션 시작 (TRX_ID 할당)
        │
   [Read View 생성] Repeatable Read는 최초 SELECT 시 1회 고정, Read Committed는 매 쿼리마다 생성
        │
   [레코드 조회] 테이블 레코드의 생성 트랜잭션 ID(`DB_TRX_ID`) 확인
        │
   레코드의 TRX_ID가 현재 Read View보다 최신(미커밋)인가?
   ┌────┴───────────────────────────┐
  예 (아직 커밋 안 됨)              아니오 (이미 커밋 완료됨)
   │                                 │
[Undo Log 역추적]                 [현재 레코드 즉시 반환]
`DB_ROLL_PTR`을 따라 과거          일관된 데이터 읽기 완료
스냅샷 버전을 찾아 반환
```

#### 한줄 요약
- Read View를 트랜잭션 시작 시 한 번만 뜨느냐 문장마다 새로 뜨느냐가 REPEATABLE READ와 READ COMMITTED를 가르며, 스냅샷을 오래 유지할수록 Undo 체인을 길게 되짚는 조회 비용을 대가로 치른다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **2PL vs MVCC**: 읽기/쓰기가 상호 락을 걸고 대기하는 2단계 락킹(2PL)과 Undo 로그 스냅샷으로 읽기와 쓰기가 서로 블로킹하지 않는 MVCC.

</details>

| 비교 항목 | Lock 기반 동시성 제어 (2PL) | MVCC 기반 동시성 제어 (Undo Log) |
|:---|:---|:---|
| 읽기/쓰기 상호작용 | **읽기와 쓰기가 상호 락(S-Lock/X-Lock)으로 블로킹** | **"읽기는 쓰기를 막지 않고, 쓰기는 읽기를 막지 않음"** |
| 동시 처리 성능(TPS)| 락 경합 및 대기로 인해 동시성 낮음 | **스냅샷 조회로 동시 조회 처리량 극대화** |
| 구현 메커니즘 | 공유 락(Shared Lock), 배타 락(Exclusive Lock) | Undo Log 버전 체인, Read View 가시성 판정 |
| 적용 환경 | 완벽한 직렬화가 필요한 Serializable 수준 | 현대 대부분의 RDBMS 기본 엔진 (InnoDB 등) |

#### 한줄 요약
- 2PL은 잠금 기반으로 직렬화하고, MVCC는 스냅샷 기반으로 읽기 성능과 동시성을 극대화한다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **Optimistic Locking(낙관적 락)**: DB 락을 잡지 않고 버전 컬럼(`version = version + 1`)을 대조하여 충돌 시 롤백하는 애플리케이션 레벨 동시성 제어.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| Serializable 적용 시 극심한 락 대기와 TPS 급락 | **Read Committed 기본 채택 + 애플리케이션 낙관적 락(`@Version`)** | 높은 동시성과 갱신 분실(Lost Update) 방지 양립 |
| Repeatable Read에서 동시 갱신 시 쓰기 왜곡(Write Skew) | **비즈니스 검증 쿼리에 `SELECT ... FOR UPDATE`(비관적 락) 명시** | 배타 락 및 갭 락 선점으로 데이터 정합성 보장 |
| 장기 트랜잭션 방치로 인한 Undo 테이블스페이스 폭증 | **트랜잭션 내 외부 API 호출 제거 및 트랜잭션 범위 최소화** | Undo Purge 지연 방지 및 DB 성능 유지 |
| 데드락(Deadlock) 빈발로 인한 트랜잭션 강제 롤백 | **트랜잭션 간 레코드 수정 순서 단일화 및 Lock Timeout 설정** | 교착 상태 사전 예방 및 빠른 장애 복구 |

#### 한줄 요약
- Read Committed + 낙관적 락, `FOR UPDATE` 선별 적용, 트랜잭션 경계 최소화로 튜닝한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **다중 버전 동시성 제어(Multi-Version Concurrency Control, MVCC)**: 데이터 변경 시 이전 스냅샷 버전을 유지하여 읽기와 쓰기 작업이 상호 락 없이 병행 실행되도록 지원하는 동시성 기법.
- **초당 트랜잭션 수(Transactions Per Second, TPS)**: 데이터베이스 엔진이 1초 동안 성공적으로 처리하고 커밋한 트랜잭션의 빈도.

</details>

- **MVCC 기반 스냅샷 격리 및 SSI 알고리즘 결합 진화**: 전통적 락 기반 격리는 언두 로그(Undo Log)를 활용하는 **다중 버전 동시성 제어(MVCC)**로 표준화되었으며, 최신 분산 RDBMS 및 CockroachDB 등에서는 직렬화 잠금 오버헤드 없이 쓰기 왜곡(Write Skew)을 차단하는 직렬화 가능 스냅샷 격리(SSI)로 발전 추세.
- **동시 처리 성능(TPS)과 데이터 무결성의 트레이드오프 통제 결단**: 무조건적인 최고 격리 수준 설정은 락 경합과 교착 상태를 유발하므로, Read Committed 또는 Repeatable Read를 기본 채택하고 갱신 분실 위험 구역에만 비관적 락(`SELECT FOR UPDATE`)이나 낙관적 락(`@Version`)을 국소 적용하는 공학적 절충 필요.

#### 한줄 요약
- 트랜잭션 격리 수준은 MVCC와 SSI 기반의 무잠금 직렬화로 진화하고 있으며, TPS 극대화와 정합성 보장을 위한 선택적 락킹 절충이 핵심이다.
