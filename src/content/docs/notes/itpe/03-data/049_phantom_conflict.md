---
title: "팬텀 충돌"
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

## Ⅰ. 트랜잭션 동시성 제어에서의 팬텀 충돌(Phantom Conflict) 개요

### 가. 팬텀 충돌의 정의
- **팬텀 충돌** : 트랜잭션 $T_1$이 특정 검색 조건(범위 조건, Predicate)을 만족하는 데이터 행 집합을 두 번 이상 읽을 때, 트랜잭션 $T_2$가 해당 검색 조건에 부합하는 새로운 행을 삽입(INSERT)하거나 기존 행을 수정하여 조건 범위로 편입시킨 후 커밋함으로써, $T_1$의 후속 조회 결과에 이전에 없던 '유령(Phantom) 행'이 출현하는 현상.
- 전통적인 행 단위 잠금(Row-level Lock)으로는 아직 존재하지 않는 '미래의 레코드'를 잠글 수 없기 때문에 발생하는 동시성 제어의 근본적 한계.

### 나. 일반 비재현 판독(Non-Repeatable Read)과의 차이
- **Non-Repeatable Read** : 이미 존재하는 특정 단일 행의 내용이 변경되거나 삭제되어 두 번째 읽기에서 다른 값을 보게 됨.
- **Phantom Read** : 데이터 행 자체가 새롭게 생겨나거나 사라져서 결과 집합의 행 개수(Count)가 변동됨.

---

## Ⅱ. 팬텀 충돌 발생 메커니즘 및 타임라인 분석

### 가. 팬텀 충돌 발생 시나리오

```text
[ 팬텀 충돌 발생 타임라인 ]
     트랜잭션 T1 (직원 급여 조회)               트랜잭션 T2 (신규 채용)
--------------------------------------------------------------------------------
t1:  BEGIN TRANSACTION;
t2:  SELECT * FROM EMP
     WHERE dept = 'IT' AND sal >= 5000;
     (결과: 3명 반환, 3개 행에 S-Lock)
t3:                                            BEGIN TRANSACTION;
t4:                                            INSERT INTO EMP (id, dept, sal)
                                               VALUES (104, 'IT', 6000);
                                               (T1의 개별 행 락과 충돌 없음 -> 성공!)
t5:                                            COMMIT;
t6:  SELECT * FROM EMP
     WHERE dept = 'IT' AND sal >= 5000;
     (결과: 4명 반환! -> 신규 104번 유령 레코드 출현)
t7:  COMMIT;
```

---

## Ⅲ. 팬텀 충돌 해결 기법의 한계점·문제점 및 해결 방안(인덱스 락 메커니즘)

### 가. 해결 기법 비교

| 해결 기법 | 동작 원리 및 메커니즘 | 장점 | 단점 및 성능 영향 |
| :--- | :--- | :--- | :--- |
| **술어 잠금 (Predicate Lock)** | 쿼리의 조건절(Predicate) 자체를 잠금 대상으로 설정하여 조건을 만족하는 모든 삽입을 원천 차단 | 이론적으로 완벽한 팬텀 방어 | 술어 간의 교집합 판별 연산이 극도로 복잡하여 실제 DBMS 상용 구현 불가 |
| **인덱스 잠금 (Index-Range Lock)** | 검색 조건을 만족하는 인덱스 키 값들을 잠그고, 조건에 해당하는 인덱스 엔트리의 삽입을 차단 | 술어 잠금을 현실적인 B-Tree 인덱스 단위로 단순화 | 인덱스가 존재하지 않으면 전체 테이블 락으로 격상 |
| **넥스트 키 락 (Next-Key Lock)** | **레코드 락(Record Lock)** 과 해당 레코드 바로 앞의 **갭 락(Gap Lock)** 을 결합하여 구간 전체를 잠금 | MySQL InnoDB의 기본 방어 기법, 팬텀 현상 완전 차단 | 불필요한 인접 키 삽입까지 대기하여 동시성 저하 |
| **SSI (Serializable Snapshot Isolation)** | MVCC 스냅샷을 사용하되 트랜잭션 간의 rw-antidependency 사이클을 동적으로 추적하여 충돌 시 롤백 | 락 없는 고속 읽기 지원 (PostgreSQL 등) | 충돌 빈번 시 트랜잭션 Abort 비율 증가 |

### 나. MySQL InnoDB의 넥스트 키 락(Next-Key Lock) 동작

```text
[ 넥스트 키 락의 갭 잠금 구조 ]
인덱스 키 값: ... (10) ---- [GAP 1] ---- (20) ---- [GAP 2] ---- (30) ...
- WHERE id BETWEEN 15 AND 25 조회 시:
  -> 키 20에 대한 레코드 락 + GAP 1 (10 < id < 20) + GAP 2 (20 < id <= 30) 모두 잠금
  -> 다른 트랜잭션이 id=18, id=22를 INSERT하려 할 때 갭 락에 걸려 대기함
```

---

## Ⅳ. 팬텀 충돌 제어를 위한 실무 제언

- 불필요한 SERIALIZABLE 격리 남용 지양 : 팬텀 읽기를 완벽히 방어하기 위해 시스템 전체를 SERIALIZABLE로 설정하면 시스템 전반에 걸친 락 경합과 교착상태(Deadlock)가 폭증하므로, 기본은 READ COMMITTED를 유지하고 일관된 집계가 필수적인 배치 집계는 스냅샷 격리를 활용해야 함.
- 적절한 인덱스 설계 : 범위 잠금이 테이블 전체 잠금으로 확산(Lock Escalation)되는 것을 방지하기 위해, `WHERE` 조건절에 사용되는 컬럼에 반드시 B-Tree 인덱스를 적절히 생성해 둘 것을 제언함.
