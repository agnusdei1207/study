---
sidebar:
  order: 49
  label: "049. 팬텀 충돌 (Phantom Conflict)"
  badge:
    text: "A"
    variant: note
title: "팬텀 충돌 (Phantom Conflict) 및 방지 기법 (Next-Key Lock, Predicate Lock)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 49
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "049"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>트랜잭션·동시성 제어</span><strong>팬텀 충돌 (Phantom Conflict)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-box" role="img" aria-label="팬텀 충돌 발생 타임라인 및 넥스트 키 락 차단 메커니즘도">
<svg viewBox="0 0 520 230" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-pt" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
    <filter id="shadow-pt" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="rgba(0,0,0,0.1)"/>
    </filter>
  </defs>

  <!-- 타임라인 헤더 -->
  <rect x="15" y="15" width="235" height="30" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="132" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">트랜잭션 1 (T1: 조회 트랜잭션)</text>

  <rect x="270" y="15" width="235" height="30" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5"/>
  <text x="387" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">트랜잭션 2 (T2: 삽입 트랜잭션)</text>

  <!-- 단계 1: T1 조회 -->
  <rect x="15" y="52" width="235" height="42" rx="4" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="25" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)">① SELECT * WHERE 강좌ID = 'CS101'</text>
  <text x="25" y="82" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-accent, #2563eb)">결과: A, B (2건) ── 개별 행 Row Lock(S) 획득</text>

  <!-- 단계 2: T2 삽입 침투 -->
  <path d="M 250 73 L 270 105" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2 2" marker-end="url(#arrow-pt)"/>

  <rect x="270" y="100" width="235" height="44" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="#ef4444" stroke-width="1.5"/>
  <text x="280" y="116" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#ef4444">② INSERT INTO ... VALUES ('CS101', 'C')</text>
  <text x="280" y="130" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)">C는 신규 행(Gap)! T1의 행 락 우회하여 삽입 성공!</text>

  <!-- 단계 3: T1 재조회 및 팬텀 발현 -->
  <path d="M 387 144 L 132 154" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2 2" marker-end="url(#arrow-pt)"/>

  <rect x="15" y="150" width="235" height="42" rx="4" fill="rgba(239, 68, 68, 0.08)" stroke="#ef4444" stroke-width="1.5"/>
  <text x="25" y="166" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#ef4444">③ SELECT * WHERE 강좌ID = 'CS101'</text>
  <text x="25" y="180" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#ef4444">결과: A, B, C (3건 출현! ── 팬텀 충돌 발생)</text>

  <!-- 하단 해결책 바 -->
  <rect x="15" y="198" width="490" height="24" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="260" y="214" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">방지 메커니즘: 넥스트 키 락 (Next-Key Lock = 레코드 락 + 갭 락)으로 인덱스 빈 공간(Gap) 원천 봉쇄</text>
</svg>
</div>

- 본질: **트랜잭션이 특정 범위 조건(Predicate)으로 조회한 후 동일 트랜잭션 내에서 재조회할 때, 타 트랜잭션의 신규 삽입(INSERT) 또는 삭제(DELETE)로 인해 이전 결과 집합에 없던 유령(Phantom) 레코드가 나타나거나 사라져 직렬성을 위반하는 동시성 이상 현상**
- 암기: `행-동-팬-직` (개별 행 락 한계, 동적 집합 충돌, 팬텀 리드 유발, 직렬화 격리 요구) / `갭-넥-서-스` (갭 락, 넥스트 키 락, 서술어 락, 스냅샷 격리)
- 판단축:
  - **Non-Repeatable Read**: 이미 존재하는 특정 단일 행의 컬럼 '값'이 타 트랜잭션의 UPDATE에 의해 변경됨 (Row Lock으로 방지 가능)
  - **Phantom Conflict**: 조건절을 만족하는 '집합의 크기(카디널리티)'가 타 트랜잭션의 INSERT/DELETE에 의해 변경됨 (Row Lock으로 방지 불가, Gap/Predicate Lock 필요)
- 주의: 단순 MVCC(다중 버전 동시성 제어)의 일관된 읽기(Consistent Read)는 일반 SELECT 문의 팬텀 리드를 언두 로그(Undo Log)로 은폐하지만, `SELECT ... FOR UPDATE` 같은 비관적 락 조회나 UPDATE/DELETE 직접 실행(Current Read) 시에는 갭 락(Gap Lock)이 없으면 여전히 팬텀 충돌이 발현됨
---

## 1교시 예상문제 (10점)

> 팬텀 충돌 (Phantom Conflict) 및 방지 기법 (Next-Key Lock, Predicate Lock)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. 팬텀 충돌의 정의 및 발생 원인

- **정의**: 트랜잭션 내 동일 조건의 범위 검색 시, 타 트랜잭션의 신규 INSERT/DELETE로 인해 이전 결과 집합에 없던 유령(Phantom) 행이 나타나 직렬성을 위반하는 동시성 이상
- **발생 원인**: 기존 행 락(Row Lock)은 물리적으로 존재하지 않는 인덱스 간격(Gap)의 미래 레코드를 잠글 수 없음

### 2. 팬텀 충돌 발생 메커니즘 및 락 해결 구조

- **발생 타임라인 요약**:
  - T1: `SELECT WHERE age >= 20;` (기존 행 A, B에 Row S-Lock 획득)
  - T2: `INSERT VALUES (C, 25);` (C는 신규 Gap이므로 T1의 락을 우회하여 성공)
  - T2 커밋 후 T1 재조회 시 신규 C 출현 $\rightarrow$ 팬텀 충돌 발생

| 락킹 해결 기법 | 동작 메커니즘 | 특징 및 적용 환경 |
|---|---|---|
| **서술어 락 (Predicate Lock)** | WHERE 조건식 자체를 락 테이블에 등록 | 이론상 완벽 방지, 조건 교집합 판정 오버헤드 극심 |
| **넥스트 키 락 (Next-Key Lock)** | 인덱스 레코드 락 + 선행 인덱스 갭 락 결합 | 실무 표준 (MySQL InnoDB Repeatable Read 기본값) |

### 3. 차별화 제언

- 단순 SELECT는 MVCC 스냅샷으로 팬텀을 방지하고, Current Read 환경의 선착순 트래픽은 **Redis 원자적 연산(`DECR`)과 유니크 인덱스**를 결합하여 DB 갭 락 데드락을 원천 차단함
---

## 2~4교시 예상문제 (25점)

> 트랜잭션 동시성 제어에서 발생하는 팬텀 충돌(Phantom Conflict)의 발생 원인과 메커니즘을 설명하고, 이를 해결하기 위한 서술어 락(Predicate Lock), 넥스트 키 락(Next-Key Lock) 및 격리 수준(Isolation Level)별 대응 방안을 비교 설명하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 행 기반 락의 한계를 드러내는 팬텀 충돌(Phantom Conflict) 개요

- 발생 배경:
  - 전통적인 2단계 락킹 프로토콜(2PL)은 이미 디스크에 존재하는 물리적 데이터 블록 또는 개별 행(Row)에 락을 설정함
  - 그러나 질의문(Query)은 특정 조건을 만족하는 '동적 집합'을 대상으로 수행되는 경우가 대부분임
  - 아직 쓰이지 않은 '미래의 레코드'는 식별자가 없으므로 기존 행 락(Row Lock)으로는 잠글 수 없는 구조적 공백(Gap)이 발생함
- 팬텀 충돌의 정의: 하나의 트랜잭션(T1) 내에서 일정한 검색 조건으로 복수의 행을 읽은 후, 다른 트랜잭션(T2)이 해당 조건에 부합하는 새로운 행을 삽입(INSERT)하거나 삭제(DELETE)하고 커밋함으로써, T1이 동일 질의를 재실행했을 때 유령(Phantom) 데이터가 나타나 직렬성을 훼손하는 동시성 이상 현상

#### 한줄 요약

- 범위 검색 조건 만족 집합에 타 트랜잭션이 신규 레코드를 삽입함으로써 동일 트랜잭션 내 재조회 결과가 달라지는 직렬성 위반 이상 현상임

### Ⅱ. 팬텀 충돌 발생 메커니즘 및 단계별 타임라인

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

#### 한줄 요약

- 기존 레코드에만 락을 건 틈을 타 인덱스 갭(Gap)에 신규 행이 삽입·커밋되어 재검색 시 카디널리티 불일치를 초래함

### Ⅲ. 팬텀 충돌 방지를 위한 핵심 락킹(Locking) 메커니즘

<div class="itpe-diagram-box" role="img" aria-label="서술어 락 대 넥스트 키 락 메커니즘 비교도">
<svg viewBox="0 0 520 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <!-- 인덱스 키 공간 및 넥스트 키 락 -->
  <text x="20" y="22" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">[InnoDB 넥스트 키 락의 인덱스 구간 잠금 구조]</text>

  <!-- 인덱스 축선 -->
  <line x1="30" y1="70" x2="490" y2="70" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="2"/>

  <!-- 노드 10 -->
  <circle cx="120" cy="70" r="12" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2"/>
  <text x="120" y="74" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">10</text>

  <!-- 노드 20 -->
  <circle cx="240" cy="70" r="12" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2"/>
  <text x="240" y="74" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">20</text>

  <!-- 노드 30 -->
  <circle cx="360" cy="70" r="12" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2"/>
  <text x="360" y="74" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">30</text>

  <!-- Supremum 가상 레코드 -->
  <rect x="440" y="58" width="55" height="24" rx="4" fill="var(--sl-color-gray-6, #f8fafc)" stroke="#10b981" stroke-width="1.5"/>
  <text x="467" y="74" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="#10b981" text-anchor="middle">Supremum</text>

  <!-- 넥스트 키 락 구간 표시 -->
  <rect x="35" y="95" width="95" height="30" rx="4" fill="rgba(37, 99, 235, 0.1)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1"/>
  <text x="82" y="114" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">Next-Key Lock 1: (-∞, 10]</text>

  <rect x="135" y="95" width="115" height="30" rx="4" fill="rgba(37, 99, 235, 0.1)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1"/>
  <text x="192" y="114" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">Next-Key Lock 2: (10, 20]</text>

  <rect x="255" y="95" width="115" height="30" rx="4" fill="rgba(37, 99, 235, 0.1)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1"/>
  <text x="312" y="114" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">Next-Key Lock 3: (20, 30]</text>

  <rect x="375" y="95" width="120" height="30" rx="4" fill="rgba(16, 185, 129, 0.1)" stroke="#10b981" stroke-width="1"/>
  <text x="435" y="114" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="#10b981" text-anchor="middle">Supremum Lock: (30, +∞)</text>

  <!-- 하단 수식 설명 -->
  <rect x="20" y="135" width="480" height="35" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="260" y="151" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Next-Key Lock 공식 = 간격 (K_{i-1}, K_i] 잠금 (앞선 Gap + 자기 자신 레코드 결합)</text>
  <text x="260" y="163" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">서술어 락(Predicate Lock)은 WHERE 조건 자체를 잠그나 NP-Hard 복잡성으로 인해 넥스트 키 락이 실무 표준 채택</text>
</svg>
</div>

### 1. 서술어 락 (Predicate Lock)

- 개념: 데이터베이스에 저장된 실제 행이 아니라, 질의문의 **검색 조건(Predicate, WHERE 조건식)** 자체를 락 테이블에 등록하여 잠그는 방식
- 동작 방식: 타 트랜잭션이 INSERT, UPDATE, DELETE를 시도할 때, 수정 대상 행이 기존에 등록된 서술어 락의 조건식을 만족하는지 검사하여 만족하면 대기(Wait)시킴
- 한계점: 복잡한 조건식(Subquery, 정규표현식, 조인 등) 간의 교집합 판정은 극심한 연산 오버헤드를 유발하여 상용 RDBMS에서는 거의 미구현

### 2. 넥스트 키 락 (Next-Key Lock, MySQL InnoDB 표준)

- 개념: **레코드 락(Record Lock)**과 해당 레코드 바로 앞의 **갭 락(Gap Lock)**을 하나로 묶어 잠그는 복합 락 형태
- 구성 요소:
  - **레코드 락(Record Lock)**: B+Tree 인덱스에 존재하는 실제 인덱스 엔트리에 설정하는 락
  - **갭 락(Gap Lock)**: 인덱스 엔트리와 엔트리 사이의 빈 간격(Gap)에 설정하여 새로운 인덱스 엔트리의 진입(INSERT)을 차단
  - **Next-Key Lock 공식**: 레코드 $K_i$에 대한 넥스트 키 락은 간격 $(K_{i-1}, K_i]$를 잠금 (앞선 간격과 자기 자신 레코드 포함)
- **Supremum Pseudo-record**: 인덱스의 최대값보다 큰 상위 범위를 잠그기 위해 페이지 끝에 존재하는 가상 레코드(Supremum)에 갭 락을 설정하여 무한대 범위 $(K_{max}, +\infty)$까지 방어

#### 한줄 요약

- 서술어 락이 조건식 자체를 잠그는 이론적 모델이라면, 넥스트 키 락은 B+Tree 인덱스 간격을 잠가 실용성을 확보한 엔지니어링 구현체임

### Ⅳ. 트랜잭션 격리 수준(Isolation Level) 및 MVCC와의 상관관계

### 1. ANSI/ISO SQL-92 표준 vs 상용 DBMS의 팬텀 처리 비교

| 격리 수준 (Isolation Level) | Dirty Read 방지 | Non-Repeatable Read 방지 | Phantom Read 방지 | 상용 DBMS 구현 방식 (MySQL InnoDB vs Oracle/PostgreSQL) |
|:---|:---:|:---:|:---:|:---|
| **Read Uncommitted** | 불가 | 불가 | 불가 | 거의 사용되지 않음 (Oracle 미지원) |
| **Read Committed** | **보장** | 불가 | 불가 | 대부분의 상용 DB 기본값. MVCC로 각 질의마다 최신 스냅샷 생성 |
| **Repeatable Read** | **보장** | **보장** | **표준: 불가<br>InnoDB: 보장** | MySQL 기본값. MVCC 스냅샷 + Next-Key Lock 결합으로 **팬텀 리드까지 완전 방지** |
| **Serializable** | **보장** | **보장** | **보장** | 순수 2PL 또는 SSI(Serializable Snapshot Isolation)로 직렬성 강제 |

### 2. MVCC 환경에서 스냅샷 읽기(Snapshot Read)와 현재 읽기(Current Read)의 차이

- **스냅샷 읽기 (Consistent Non-Locking Read)**:
  - 일반적인 `SELECT` 문 실행 시 락을 걸지 않고, 트랜잭션 시작 시점의 시스템 트랜잭션 ID(Read View)를 기준으로 언두 세그먼트(Undo Log)의 과거 버전을 읽음
  - 따라서 중간에 다른 트랜잭션이 INSERT 커밋을 하더라도 T1의 스냅샷에는 보이지 않아 **팬텀 리드가 자동으로 은폐됨**
- **현재 읽기 (Current / Locking Read)**:
  - `SELECT ... FOR UPDATE`, `UPDATE`, `DELETE` 실행 시 발생
  - 현재 시점의 가장 최신 커밋된 데이터를 읽어야 하므로 Undo Log가 아닌 **실제 인덱스 블록을 조회하고 락을 획득**함
  - 이때 **Next-Key Lock(갭 락)**이 없으면 다른 트랜잭션의 신규 INSERT 데이터가 그대로 걸려들며 팬텀 충돌이 수면 위로 드러남

#### 한줄 요약

- 일반 조회는 MVCC 언두 스냅샷으로 팬텀을 숨기지만, 쓰기 및 락 조회의 Current Read에서는 넥스트 키 락이 있어야만 팬텀을 차단할 수 있음

### Ⅴ. Non-Repeatable Read vs Phantom Conflict 상세 비교

| 비교 항목 | Non-Repeatable Read (비반복 읽기) | Phantom Conflict (팬텀 충돌) |
|:---|:---|:---|
| **발생 원인 행위** | 기존 튜플에 대한 `UPDATE` 및 `DELETE` | 기존에 없던 인덱스 간격에 대한 `INSERT` (또는 `DELETE`) |
| **데이터 객체 상태** | 물리적으로 이미 존재하는 데이터 블록 내 레코드 | 쿼리 실행 전에는 물리적으로 존재하지 않던 가상 데이터 |
| **락의 보호 영역** | **Record Lock (행 잠금)** | **Gap Lock / Next-Key Lock (간격 잠금)** 또는 Predicate Lock |
| **감지되는 불일치** | 특정 키 값 레코드의 데이터 컬럼 속성값 변조 | 질의 결과 집합의 카디널리티(Row Count) 및 구성 튜플 목록 변화 |
| **SQL 표준 격리 수준** | `Repeatable Read` 이상에서 방지 보장 | `Serializable` 수준에서만 방지 보장 명시 (InnoDB는 RR 방어) |

#### 한줄 요약

- 비반복 읽기는 단일 행의 속성값 변경이고, 팬텀 충돌은 범위 조건 집합의 원소 개수(카디널리티) 변화임

### Ⅵ. 실무 아키텍처 적용 사례 및 장애 예방 패턴

### 1. 전형적 장애 사례: 수강신청/선착순 이벤트 정원 초과 버그

```sql
-- [취약한 동시성 제어 패턴]
BEGIN;
SELECT COUNT(*) FROM enrollment WHERE course_id = 'CS1001'; -- (현재 29명)
-- 애플리케이션: if (count < 30) { INSERT 진행 }
INSERT INTO enrollment (course_id, user_id) VALUES ('CS1001', 'user_99');
COMMIT;
-- 10개 스레드가 동시 실행 시 모두 count=29를 읽고 INSERT 성공 -> 정원 39명 등록 참사!
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

#### 한줄 요약

- 선착순 로직은 부모 행 비관적 락이나 Redis 원자 연산으로 방어하고, 갭 락 데드락은 Read Committed 전환 또는 유니크 인덱스로 해소함

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 팬텀 충돌의 본질은 "존재하지 않는 미래의 튜플을 어떻게 잠글 것인가"라는 동시성 제어의 근본적 딜레마에 있다. 많은 개발자가 "우리 DBMS는 Repeatable Read니까 팬텀 리드가 없다"고 맹신하다가, `SELECT ... FOR UPDATE`나 배치 UPDATE 문 같은 Current Read 상황에서 발생하는 정합성 깨짐이나 갭 락 데드락으로 야간 장애를 겪는다. 엔지니어의 핵심 역량은 엔진 격리 수준의 환상을 깨고, (1) 비관적 잠금 직렬화, (2) 애플리케이션 분산 락(Redis), (3) 유니크 인덱스 기반 갭 축소의 3중 방어망을 구축하는 데 있다.

> **[나라면 이렇게 쓴다]**
> 25점 답안 3단락 차별화로 "다계층 동시성 방어 아키텍처(Multi-tier Concurrency Defense)"를 제시하겠다. DB 엔진의 무거운 넥스트 키 락에 전적으로 의존하는 안티패턴을 지양하고, 1계층 인메모리 Redis 원자적 연산(`DECR/SETNX`)으로 트래픽의 90%를 선제 차단하고, 2계층 애플리케이션 낙관적 락(`version`), 3계층 핵심 금융 정산 구간의 배타적 넥스트 키 락 적용으로 이어지는 계층형 방어 구조를 제시함으로써 고성능과 무결성을 동시에 잡는 아키텍트의 시야를 입증한다.

### 실전 답안용 기술사적 제언

- **[격리 수준 맹신에 따른 실무 정합성 파탄 및 갭 락 데드락 한계]**: Repeatable Read 격리 수준에서도 Current Read 시 팬텀 발생 및 불필요한 갭 락 경합으로 인한 교착 상태 발생
- **[실무 최적화 방안]**: 동시성 트래픽이 집중되는 선착순/정원 로직은 Redis 원자적 분산 락으로 앞단 차단하고, DB 계층은 유니크 인덱스로 갭 잠금 최소화
- **[격리 수준 및 인덱스 튜닝]**: 고빈도 트랜잭션 세션은 `READ COMMITTED`로 격리 수준을 하향 조정하고, 필요 구간에만 명시적 비관적 락을 선별 적용

<div class="itpe-flow-map" role="group" aria-label="팬텀 충돌 방지 및 동시성 최적화 4단계 흐름">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">1</div>
    <div class="itpe-flow-step__title">현행 한계</div>
    <div class="itpe-flow-step__desc">단순 행 락의 미래 튜플 잠금 불가로 팬텀 리드 및 정원 초과 버그 발생</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">2</div>
    <div class="itpe-flow-step__title">개선 방안</div>
    <div class="itpe-flow-step__desc">Next-Key Lock(Record+Gap) 적용 및 Redis 원자적 분산 락 다계층 방어</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">3</div>
    <div class="itpe-flow-step__title">검증 기준</div>
    <div class="itpe-flow-step__desc">동시 INSERT 시 집계 오차 0건, 트랜잭션 데드락 발생률 0.001% 미만</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">4</div>
    <div class="itpe-flow-step__title">실행 효과</div>
    <div class="itpe-flow-step__desc">금융·예약 시스템 직렬성 100% 보장 및 DB 락 경합 지연 60% 단축</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- 정보관리기술사 제135회 1교시 11번: 팬텀충돌(Phantom Conflict)
- 컴퓨터시스템응용기술사 제121회 1교시: 트랜잭션 격리수준과 동시성 이상 현상
- MySQL 8.0 Reference Manual, "InnoDB Locking - Next-Key Locks and Phantom Rows"
- Jim Gray & Andreas Reuter, *Transaction Processing: Concepts and Techniques*

## 연결 토픽

- [동시성 제어](./009_concurrency_control/) · [격리 수준(Isolation Level)](./020_isolation_level/) · [인덱스(Index)](./047_index/) · [확장성 해싱](./050_extendible_hashing/)
