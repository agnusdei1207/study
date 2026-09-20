---
sidebar:
  order: 49
  label: "049. 팬텀 충돌 (Phantom Conflict)"
  badge:
    text: "A"
    variant: note
title: "팬텀 충돌 (Phantom Conflict) 및 방지 기법 (Next-Key Lock, Predicate Lock)"
author: "OpenAI Codex"
date: "2026-09-20T17:30:00+09:00"
tags:
  - "notes-data"
weight: 49
extra:
  model: "GPT-5"
  keyword_grade: "A"
  question_no: "049"

---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>트랜잭션·동시성 제어</span><strong>팬텀 충돌 (Phantom Conflict)</strong></div>

## 큰 그림과 30초 인출

```text
[팬텀 충돌(Phantom Conflict) 발생 타임라인 및 락 메커니즘]

       트랜잭션 1 (T1)                                 트랜잭션 2 (T2)
 ──────────────────────────────                  ──────────────────────────────
 ① SELECT * FROM 수강신청
    WHERE 강좌ID = 'CS101';
    (결과: 학생A, 학생B (2건))
    * 개별 행 A, B에 Row Lock(S-Lock) 획득
                                                 ② INSERT INTO 수강신청 
                                                    VALUES ('CS101', '학생C');
                                                    * 학생C는 기존에 없던 행(Gap)!
                                                    * T1의 개별 행 락을 우회하여 삽입 성공
                                                 ③ COMMIT;
 ④ SELECT * FROM 수강신청
    WHERE 강좌ID = 'CS101';
    (결과: 학생A, 학생B, 학생C (3건 출현!) ───▶ [팬텀 충돌(Phantom Conflict) 발생!])

 ─────────────────────────────────────────────────────────────────────────────
 [해결 방안]: 갭 락(Gap Lock) + 레코드 락(Record Lock) = 넥스트 키 락(Next-Key Lock)
  - 인덱스 레코드 사이의 빈 공간(Gap)까지 배타적/공유 잠금을 설정하여 신규 INSERT 차단
```

- 본질: **트랜잭션이 특정 범위 조건(Predicate)으로 조회한 후 동일 트랜잭션 내에서 재조회할 때, 타 트랜잭션의 신규 삽입(INSERT) 또는 삭제(DELETE)로 인해 이전 결과 집합에 없던 유령(Phantom) 레코드가 나타나거나 사라져 직렬성을 위반하는 동시성 이상 현상**
- 암기: `행-동-팬-직` (개별 행 락 한계, 동적 집합 충돌, 팬텀 리드 유발, 직렬화 격리 요구) / `갭-넥-서-스` (갭 락, 넥스트 키 락, 서술어 락, 스냅샷 격리)
- 판단축:
  - **Non-Repeatable Read**: 이미 존재하는 특정 단일 행의 컬럼 '값'이 타 트랜잭션의 UPDATE에 의해 변경됨 (Row Lock으로 방지 가능)
  - **Phantom Conflict**: 조건절을 만족하는 '집합의 크기(카디널리티)'가 타 트랜잭션의 INSERT/DELETE에 의해 변경됨 (Row Lock으로 방지 불가, Gap/Predicate Lock 필요)
- 주의: 단순 MVCC(다중 버전 동시성 제어)의 일관된 읽기(Consistent Read)는 일반 SELECT 문의 팬텀 리드를 언두 로그(Undo Log)로 은폐하지만, `SELECT ... FOR UPDATE` 같은 비관적 락 조회나 UPDATE/DELETE 직접 실행(Current Read) 시에는 갭 락(Gap Lock)이 없으면 여전히 팬텀 충돌이 발현됨

## 예상문제

> 트랜잭션 동시성 제어에서 발생하는 팬텀 충돌(Phantom Conflict)의 발생 원인과 메커니즘을 설명하고, 이를 해결하기 위한 서술어 락(Predicate Lock), 넥스트 키 락(Next-Key Lock) 및 격리 수준(Isolation Level)별 대응 방안을 비교 설명하시오. (25점)

## Ⅰ. 행 기반 락의 한계를 드러내는 팬텀 충돌(Phantom Conflict) 개요

#### 한줄 요약: 범위 검색 조건 만족 집합에 타 트랜잭션이 신규 레코드를 삽입함으로써 동일 트랜잭션 내 재조회 결과가 달라지는 직렬성 위반 이상 현상

- **발생 배경**:
  - 전통적인 2단계 락킹 프로토콜(2PL, Two-Phase Locking)은 이미 존재하는 물리적 데이터 블록 또는 개별 행(Row)에 락을 설정함
  - 그러나 질의문(Query)은 특정 조건을 만족하는 '동적 집합'을 대상으로 수행되는 경우가 대부분임
  - 아직 디스크에 쓰이지 않은 '미래의 레코드'는 메모리 상에 식별자가 없으므로 기존 행 락(Row Lock)으로는 잠글 수 없는 구조적 공백이 발생함
- **팬텀 충돌의 정의**: 하나의 트랜잭션(T1) 내에서 일정한 검색 조건으로 복수의 행을 읽은 후, 다른 트랜잭션(T2)이 해당 조건에 부합하는 새로운 행을 삽입(INSERT)하거나 삭제(DELETE)하고 커밋함으로써, T1이 동일한 질의를 다시 실행했을 때 이전에 보이지 않던 유령(Phantom) 데이터가 나타나 일관성을 훼손하는 충돌 현상

```text
[행 락(Row Lock)의 물리적 한계와 Gap의 침투]

 인덱스 키 공간:    [10] ── (빈 공간: Gap) ── [20] ── (빈 공간: Gap) ── [30]
 T1 조건 검색:      WHERE val BETWEEN 10 AND 30;
 T1 획득 락:        Row-Lock(10), Row-Lock(20), Row-Lock(30)
 
 T2 신규 삽입:      INSERT INTO ... VALUES (15);
 침투 경로:         [15]는 10과 20 사이의 Gap! 기존 행 락이 없으므로 T2 즉시 INSERT 성공!
 결과:              T1이 다시 검색하면 [15]가 유령처럼 출현 ──▶ 팬텀 충돌
```

## Ⅱ. 팬텀 충돌 발생 메커니즘 및 단계별 타임라인

#### 한줄 요약: 조건 검색 시 기존 레코드만 잠근 틈을 타 인덱스 갭(Gap)에 신규 튜플이 삽입·커밋되어 재검색 시 집합 불일치를 초래하는 과정

### 1. 단계별 발생 타임라인

| 단계 | 트랜잭션 1 (T1) | 트랜잭션 2 (T2) | 데이터베이스 상태 및 락 현황 | 팬텀 발현 여부 |
|:---:|:---|:---|:---|:---|
| **t1** | `BEGIN;`<br>`SELECT * FROM 계좌 WHERE 잔액 >= 1000;` | - | 계좌 A(1000), B(1500) 인출<br>A, B 행에 공유 락(S-Lock) 획득 | 정상 조회 (2건) |
| **t2** | 비즈니스 로직 연산 수행 중 | `BEGIN;`<br>`INSERT INTO 계좌 VALUES ('C', 1200);` | 계좌 C는 신규 행이므로 기존 S-Lock의 저촉을 받지 않고 삽입 성공 | 잠재적 충돌 생성 |
| **t3** | - | `COMMIT;` | 신규 레코드 C가 영구 반영됨 | 변경 확정 |
| **t4** | `SELECT COUNT(*) FROM 계좌 WHERE 잔액 >= 1000;` | - | **결과: 3건 (A, B, C 출현!)**<br>T1 입장에서는 없던 C가 갑자기 나타남 | **팬텀 리드 (Phantom Read) 발생** |
| **t5** | `COMMIT;` | - | 트랜잭션 직렬성(Serializability) 위반 | 비일관성 잔존 |

### 2. 동시성 제어 이상의 전형적 발현 시나리오

- **집계 불일치 (Sum / Count Anomaly)**: 회계 정산 시 T1이 전체 지점의 매출 합계를 집계하는 동안 T2가 신규 지점 매출을 삽입하여 1차 조회 합계와 2차 검증 합계가 불일치함
- **외래키 제약 및 유일성 제약 우회**: 정원 30명 제한 로직에서 T1과 T2가 동시에 `COUNT(*)`로 29명임을 확인한 후 각각 INSERT를 수행하여 최종 31명이 등록되는 동시성 버그 유발

## Ⅲ. 팬텀 충돌 방지를 위한 핵심 락킹(Locking) 메커니즘

#### 한줄 요약: WHERE 절의 조건 자체를 잠그는 이론적 서술어 락과 인덱스 간격을 물리적으로 차단하는 실무적 넥스트 키 락의 체계

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 팬텀 충돌 방지 락킹 기법의 스펙트럼                        │
└─────────────────────────────────────────────────────────────────────────────┘
      이론적 이상향                                   실무적 엔지니어링 구현
   [서술어 락 (Predicate Lock)]                    [넥스트 키 락 (Next-Key Lock)]
  - WHERE 조건식 자체를 등록하여                   - B+Tree 인덱스의 정렬 순서를 이용
    조건에 부합하는 모든 미래 튜플 차단             - 레코드 락 + 이전 인덱스 갭 락 결합
  - 장점: 인덱스 부재 시에도 완벽 방지             - 장점: $O(\log N)$ 인덱스 탐색 비용으로 해결
  - 단점: 모든 INSERT마다 술어 평가 비용 극심       - 단점: 불필요한 범위 잠금으로 동시성 저하
```

### 1. 서술어 락 (Predicate Lock)
- **개념**: 데이터베이스에 저장된 실제 행이 아니라, 질의문의 **검색 조건(Predicate, WHERE 조건식)** 자체를 락 테이블에 등록하여 잠그는 방식
- **동작 방식**: 타 트랜잭션이 INSERT, UPDATE, DELETE를 시도할 때, 수정 대상 행이 기존에 등록된 서술어 락의 조건식을 만족하는지 검사하여 만족하면 대기(Wait)시킴
- **한계점**:
  - 임의의 복잡한 조건식(Subquery, 정규표현식, 조인 조건 등) 간의 교집합(Intersection) 판정은 NP-Hard 수준의 연산 오버헤드 유발
  - 실제 상용 RDBMS에서는 성능상의 이유로 순수 서술어 락을 거의 구현하지 않음

### 2. 넥스트 키 락 (Next-Key Lock, MySQL InnoDB 기본 메커니즘)
- **개념**: **레코드 락(Record Lock)**과 해당 레코드 바로 앞의 **갭 락(Gap Lock)**을 하나로 묶어 잠그는 복합 락 형태
- **구성 요소**:
  - **레코드 락(Record Lock)**: B+Tree 인덱스에 존재하는 실제 인덱스 엔트리에 설정하는 락
  - **갭 락(Gap Lock)**: 인덱스 엔트리와 엔트리 사이의 빈 간격(Gap)에 설정하는 락으로, 새로운 인덱스 엔트리의 진입(INSERT)을 물리적으로 차단
  - **Next-Key Lock 공식**: 레코드 $K_i$에 대한 넥스트 키 락은 간격 $(K_{i-1}, K_i]$를 잠금 (앞선 간격과 자기 자신 레코드 포함)
- **Supremum Pseudo-record**: 인덱스의 최대값보다 큰 상위 범위를 잠그기 위해 페이지 끝에 존재하는 가상 레코드(Supremum)에 갭 락을 설정하여 무한대 범위 $(K_{max}, +\infty)$까지 방어

```text
[InnoDB Next-Key Lock의 인덱스 키 공간 잠금 예시]

 인덱스 엔트리:        [10]                  [20]                  [30]
 간격(Gap):      (-∞, 10)     (10, 20)              (20, 30)              (30, +∞)
 Next-Key Lock: [  락 1  ]   [     락 2     ]     [     락 3     ]     [  Supremum 락 ]
                (-∞, 10]       (10, 20]              (20, 30]              (30, +∞)
```

## Ⅳ. 트랜잭션 격리 수준(Isolation Level) 및 MVCC와의 상관관계

#### 한줄 요약: SQL 표준 격리 수준별 팬텀 처리 차이와 MVCC 스냅샷 읽기(Consistent Read) 및 Current Read 간의 동작 양상

### 1. ANSI/ISO SQL-92 표준 vs 상용 DBMS의 팬텀 처리 비교

| 격리 수준 (Isolation Level) | Dirty Read 방지 | Non-Repeatable Read 방지 | Phantom Read 방지 | 상용 DBMS 구현 방식 (MySQL InnoDB vs Oracle/PostgreSQL) |
|:---|:---:|:---:|:---:|:---|
| **Read Uncommitted** | 불가 | 불가 | 불가 | 거의 사용되지 않음 (Oracle 미지원) |
| **Read Committed** | **보장** | 불가 | 불가 | 대부분의 상용 DB 기본값. MVCC로 각 질의마다 최신 스냅샷 생성 |
| **Repeatable Read** | **보장** | **보장** | **표준: 불가<br>InnoDB: 보장** | MySQL 기본값. MVCC 스냅샷 + Next-Key Lock 결합으로 **팬텀 리드까지 완전 방지** |
| **Serializable** | **보장** | **보장** | **보장** | 순수 2PL 또는 SSI(Serializable Snapshot Isolation)로 직렬성 강제 |

### 2. MVCC 환경에서 스냅샷 읽기(Snapshot Read)와 현재 읽기(Current Read)의 차이

- **스냅샷 읽기 (Consistent Non-Locking Read)**:
  - 일반적인 `SELECT` 문 실행 시 락을 걸지 않고, 트랜잭션 시작 시점(또는 쿼리 시작 시점)의 시스템 트랜잭션 ID(Read View)를 기준으로 언두 세그먼트(Undo Log)의 과거 버전을 읽음
  - 따라서 중간에 다른 트랜잭션이 INSERT 커밋을 하더라도 T1의 스냅샷에는 보이지 않아 **팬텀 리드가 자동으로 은폐됨**
- **현재 읽기 (Current / Locking Read)**:
  - `SELECT ... FOR UPDATE`, `SELECT ... LOCK IN SHARE MODE`, `UPDATE`, `DELETE` 실행 시 발생
  - 현재 시점의 가장 최신 커밋된 데이터를 읽어야 하므로 Undo Log가 아닌 **실제 인덱스 블록을 조회하고 락을 획득**함
  - 이때 **Next-Key Lock(갭 락)**이 없으면 다른 트랜잭션의 신규 INSERT 데이터가 그대로 걸려들며 팬텀 충돌이 수면 위로 드러남

## Ⅴ. Non-Repeatable Read vs Phantom Conflict 상세 비교

#### 한줄 요약: 이미 존재하는 튜플 컬럼값의 변경(In-place update)과 조건 집합 내 신규 튜플의 진입(Gap insertion)이라는 구조적 차이

```text
┌───────────────────────────────────┬───────────────────────────────────┐
│     Non-Repeatable Read (비반복 읽기)│       Phantom Conflict (팬텀 충돌)    │
├───────────────────────────────────┼───────────────────────────────────┤
│ - 대상: 이미 존재하는 특정 단일 레코드   │ - 대상: 조건(WHERE)에 부합하는 레코드 집합│
│ - 조작: 타 트랜잭션의 UPDATE / DELETE  │ - 조작: 타 트랜잭션의 신규 INSERT / DELETE│
│ - 현상: 동일 레코드의 속성 값이 달라짐 │ - 현상: 결과 집합의 행 개수(건수)가 바뀜 │
│ - 방지: 개별 행 락(Row S-Lock)으로 충분│ - 방지: 갭 락(Gap Lock), 서술어 락 필수  │
│ - 격리: Repeatable Read 수준에서 해결 │ - 격리: Serializable (InnoDB는 RR 해결)│
└───────────────────────────────────┴───────────────────────────────────┘
```

| 비교 항목 | Non-Repeatable Read (Fuzzy Read) | Phantom Conflict (유령 충돌) |
|:---|:---|:---|
| **발생 원인 행위** | 기존 튜플에 대한 `UPDATE` 및 `DELETE` | 기존에 없던 인덱스 간격에 대한 `INSERT` (또는 `DELETE`) |
| **데이터 객체 상태** | 물리적으로 이미 존재하는 데이터 블록 내 레코드 | 쿼리 실행 전에는 물리적으로 존재하지 않던 가상 데이터 |
| **락의 보호 영역** | **Record Lock (행 잠금)** | **Gap Lock / Next-Key Lock (간격 잠금)** 또는 Predicate Lock |
| **감지되는 불일치** | 특정 키 값 레코드의 데이터 컬럼 속성값 변조 | 질의 결과 집합의 카디널리티(Row Count) 및 구성 튜플 목록 변화 |
| **SQL 표준 격리 수준** | `Repeatable Read` 이상에서 방지 보장 | `Serializable` 수준에서만 방지 보장 명시 |

## Ⅵ. 실무 아키텍처 적용 사례 및 장애 예방 패턴

#### 한줄 요약: 정원 초과 방지, 금융 마감 정산, 갭 락 데드락 완화 등 실무 트랜잭션 설계의 핵심 트레이드오프

### 1. 전형적 장애 사례: 수강신청/선착순 이벤트 정원 초과 버그

```sql
-- [취약한 동시성 제어 패턴]
BEGIN;
SELECT COUNT(*) FROM enrollment WHERE course_id = 'CS1001'; -- (현재 29명)
-- 애플리케이션: if (count < 30) { 진행 }
INSERT INTO enrollment (course_id, user_id) VALUES ('CS1001', 'user_99');
COMMIT;
-- 결과: 10개 스레드가 동시 실행 시 모두 count=29를 읽고 INSERT 성공 -> 정원 39명 등록 참사!
```

- **해결 방안 3단계 패턴**:
  1. **비관적 락(Pessimistic Lock) 강제**: 상위 집계 부모 행(Course 테이블)에 `SELECT ... FOR UPDATE`를 걸어 자식 INSERT를 직렬화
  2. **DB 고유 제약조건 및 트리거**: 인덱스 기반 Unique 제약 또는 DB 체크 제약조건 활용
  3. **인메모리 원자적 연산 분산 락**: Redis `INCR` 또는 Redisson 분산 락을 애플리케이션 앞단에 배치하여 DB 유입 전 정원 차단

### 2. 갭 락(Gap Lock)에 의한 실무 데드락(Deadlock) 이슈 및 완화책

- **문제점**:
  - MySQL InnoDB의 Repeatable Read 수준에서는 Next-Key Lock으로 인해 넓은 인덱스 갭이 잠기면서 동시 INSERT 간 상호 Gap Lock 대기로 인한 데드락이 빈발함
  - Gap Lock끼리는 서로 호환(Shared)되지만, 그 Gap 내에 실제 데이터를 쓰려고 할 때 **Insert Intention Lock**과 충돌하여 교착 상태 발생
- **최적화 대책**:
  - **격리 수준 하향 조정**: 글로벌 또는 해당 세션 격리 수준을 `READ COMMITTED`로 전환 (InnoDB는 RC에서 외래키/유일성 검사를 제외하고 Gap Lock을 비활성화함)
  - **인덱스 설계 최적화**: WHERE 조건 컬럼에 완전 일치 고유 인덱스(Unique Index)를 생성하여 갭 락이 단일 레코드 락으로 다운그레이드되도록 유도

## Ⅶ. 데이터 아키텍트 관점의 직렬성 보장 및 동시성 최적화 제언

#### 한줄 요약: 엔진 격리 수준의 맹신을 탈피하고 낙관적 잠금, 애플리케이션 분산 락, 인덱스 정밀 설계를 결합한 다계층 방어 체계 확립

- **격리 수준 추상화의 함정 탈피**:
  - 개발자가 "우리 DB는 Repeatable Read니까 팬텀 리드가 안 일어난다"고 과신하여 단순 SELECT 기반의 유효성 검증을 설계하면, 실무 Current Read나 DML 배치 환경에서 치명적인 정합성 깨짐이 발생함
  - RDBMS 엔진의 동시성 제어 모델(MVCC + 락킹 기법)의 내부 메커니즘을 명확히 이해하고 아키텍처에 반영해야 함
- **다계층 동시성 방어 전략**:
  1. **1계층 (진입점)**: Redis 원자적 연산(`DECR`, `SETNX`)으로 불필요한 DB 경합을 90% 이상 사전 차단
  2. **2계층 (서비스 계층)**: 버전 컬럼(`version`)을 이용한 낙관적 락(Optimistic Lock) 적용으로 락 보유 시간 최소화
  3. **3계층 (DB 엔진 계층)**: 엄격한 데이터 정합성이 요구되는 트랜잭션에 한하여 배타적 넥스트 키 락 적용 및 유니크 인덱스를 통한 갭 최소화

---

## 1교시 10점 답안 발췌

```text
[문제 11] 팬텀 충돌 (Phantom Conflict)

1. 팬텀 충돌의 정의 및 발생 원인
 가. 정의: 트랜잭션 내 동일 조건의 범위 검색 시, 타 트랜잭션의 신규 INSERT/DELETE로
          인해 결과 집합에 없던 유령(Phantom) 행이 나타나 직렬성을 위반하는 동시성 이상
 나. 발생 원인: 기존 행 락(Row Lock)은 존재하지 않는 미래의 레코드 공간을 잠글 수 없음

2. 팬텀 충돌 발생 메커니즘 및 락 해결 구조
 가. 발생 메커니즘 (타임라인)
     T1: SELECT ... WHERE age >= 20; (행 A, B에 Row S-Lock 획득)
     T2: INSERT INTO ... VALUES (C, 25); (C는 기존에 없던 Gap이므로 락 우회 성공)
     T2: COMMIT;
     T1: SELECT ... WHERE age >= 20; (A, B 외에 신규 C 출현 -> 팬텀 충돌!)
 나. 해결 메커니즘: 넥스트 키 락 (Next-Key Lock)
     ┌──────────────────────────────────────────────────────────────┐
     │ 넥스트 키 락 = 레코드 락(Record Lock) + 갭 락(Gap Lock)      │
     │ - 인덱스 레코드 사이의 빈 공간(Gap)까지 잠가 신규 INSERT 차단│
     └──────────────────────────────────────────────────────────────┘

3. 해결 기법 비교 및 완화 전략
 가. 해결 기법 비교
     - 서술어 락(Predicate Lock): WHERE 조건 자체를 잠금 / 이론적 완벽 / 연산 오버헤드 큼
     - 넥스트 키 락(Next-Key Lock): 인덱스 레코드와 앞 간격을 잠금 / 실무 표준(InnoDB)
 나. 실무 완화: 단순 SELECT는 MVCC 스냅샷으로 방지, 경합 극심 시 RC 격리수준 + Redis 분산 락
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제135회 1교시 11번 (팬텀충돌(Phantom Conflict))
  - 컴퓨터시스템응용기술사 제121회 1교시 (트랜잭션 격리수준과 동시성 이상 현상)
  - 정보관리기술사 제114회 2교시 (트랜잭션 격리성 보장 기법과 2PL, MVCC 비교)
- **표준 및 검증 출처**:
  - MySQL 8.0 Reference Manual, "InnoDB Locking - Next-Key Locks and Phantom Rows"
  - Jim Gray & Andreas Reuter, *Transaction Processing: Concepts and Techniques*
  - Abraham Silberschatz et al., *Database System Concepts (7th Edition)*, Chapter 15-16

---

## 학습 체크

- [ ] 팬텀 충돌이 기존 행 락(Row Lock)만으로는 방지될 수 없는 근본적인 구조적 원인은 무엇인가?
- [ ] 서술어 락(Predicate Lock)과 넥스트 키 락(Next-Key Lock)의 개념 및 차이점을 설명할 수 있는가?
- [ ] MySQL InnoDB 엔진에서 레코드 락, 갭 락, 넥스트 키 락의 상호 결합 구조를 도식화할 수 있는가?
- [ ] MVCC 스냅샷 읽기(Consistent Read) 상황에서도 팬텀 충돌이 발현될 수 있는 시나리오(Current Read)를 설명할 수 있는가?
- [ ] **서술 연습 1**: 팬텀 충돌의 발생 메커니즘을 2개 트랜잭션의 타임라인으로 그리고, 넥스트 키 락의 인덱스 구간 잠금 방식을 10점형 답안으로 서술하시오.
- [ ] **서술 연습 2**: Non-Repeatable Read와 Phantom Conflict를 대상 객체, 락 방식, SQL 격리 수준 관점에서 비교표로 작성하시오.

---

## 연결 토픽

- [009. 동시성 제어 (Concurrency Control)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/009_concurrency_control.md)
- [047. 인덱스 (Index)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index.md)
- [050. 확장성 해싱 (Extendible Hashing)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/050_extendible_hashing.md)
