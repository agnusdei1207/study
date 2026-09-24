---
sidebar:
  order: 70
  label: "070. 참조 무결성 (Referential Integrity)"
  badge:
    text: "기초"
    variant: note
title: "참조 무결성 (Referential Integrity) 및 외래키 연쇄 동작 (CASCADE, RESTRICT)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 70
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "070"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터 모델링·무결성</span><strong>참조 무결성 (Referential Integrity)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">참조 무결성 및 4대 연쇄 동작(Action Rules) 메커니즘</text>

  <!-- Left: Parent Relation (Department) -->
  <g transform="translate(30, 48)">
    <rect x="0" y="0" width="180" height="110" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <rect x="0" y="0" width="180" height="24" rx="5" fill="#eff6ff"/>
    <text x="90" y="16" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">부모 릴레이션: 부서 (Dept)</text>
    <text x="15" y="42" font-size="8.5" font-weight="bold" fill="#1e40af">부서코드(PK) | 부서명</text>
    <line x1="10" y1="48" x2="170" y2="48" stroke="#cbd5e1" stroke-width="1"/>
    <text x="15" y="64" font-size="8.5" fill="#334155">D01           | 플랫폼개발팀</text>
    <text x="15" y="80" font-size="8.5" fill="#334155">D02           | 클라우드운영팀</text>
    <text x="15" y="96" font-size="8.5" fill="#334155">D03           | AI연구팀</text>
  </g>

  <!-- FK Arrow -->
  <path d="M 290 102 L 215 102" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="215,99 210,102 215,105" fill="#2563eb"/>
  <text x="250" y="95" font-size="8" font-weight="bold" fill="#2563eb" text-anchor="middle">FK 참조</text>

  <!-- Right: Child Relation (Employee) -->
  <g transform="translate(290, 48)">
    <rect x="0" y="0" width="200" height="110" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <rect x="0" y="0" width="200" height="24" rx="5" fill="#eff6ff"/>
    <text x="100" y="16" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">자식 릴레이션: 사원 (Emp)</text>
    <text x="12" y="42" font-size="8.5" font-weight="bold" fill="#1e40af">사원ID(PK) | 이름 | 부서코드(FK)</text>
    <line x1="10" y1="48" x2="190" y2="48" stroke="#cbd5e1" stroke-width="1"/>
    <text x="12" y="64" font-size="8.5" fill="#334155">1001       | 김철수 | D01</text>
    <text x="12" y="80" font-size="8.5" fill="#334155">1002       | 이영희 | D01</text>
    <text x="12" y="96" font-size="8.5" fill="#dc2626" font-weight="bold">1003       | 박민수 | D99 (★ 위반!)</text>
  </g>

  <!-- Bottom: 4 Action Rules -->
  <g transform="translate(30, 170)">
    <rect x="0" y="0" width="460" height="88" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <text x="15" y="18" font-size="9.5" font-weight="bold" fill="#0f172a">부모 레코드(예: D01) 삭제 시도 시 4대 연쇄 동작 규칙</text>

    <!-- 4 Mini Boxes -->
    <rect x="15" y="28" width="100" height="48" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="65" y="44" font-size="8.5" font-weight="bold" fill="#1e40af" text-anchor="middle">1. RESTRICT</text>
    <text x="65" y="62" font-size="7.5" fill="#334155" text-anchor="middle">부모 삭제 거부(에러)</text>

    <rect x="125" y="28" width="100" height="48" rx="4" fill="#fee2e2" stroke="#ef4444"/>
    <text x="175" y="44" font-size="8.5" font-weight="bold" fill="#991b1b" text-anchor="middle">2. CASCADE</text>
    <text x="175" y="62" font-size="7.5" fill="#334155" text-anchor="middle">자식도 연쇄 삭제</text>

    <rect x="235" y="28" width="100" height="48" rx="4" fill="#fef3c7" stroke="#f59e0b"/>
    <text x="285" y="44" font-size="8.5" font-weight="bold" fill="#b45309" text-anchor="middle">3. SET NULL</text>
    <text x="285" y="62" font-size="7.5" fill="#334155" text-anchor="middle">자식 FK를 NULL 변경</text>

    <rect x="345" y="28" width="100" height="48" rx="4" fill="#f1f5f9" stroke="#64748b"/>
    <text x="395" y="44" font-size="8.5" font-weight="bold" fill="#334155" text-anchor="middle">4. SET DEFAULT</text>
    <text x="395" y="62" font-size="7.5" fill="#334155" text-anchor="middle">자식 FK 기본값 세팅</text>
  </g>
</svg>
</div>

- 본질: **관계형 데이터베이스(RDBMS)에서 자식 릴레이션의 외래키(FK) 값은 반드시 부모 릴레이션의 기본키(PK) 값으로 실존하거나 NULL이어야 한다는 규칙으로, 부모를 잃어버린 유령 데이터인 고아 레코드(Orphan Record)의 발생을 방지하고 테이블 간 관계 정합성을 보장하는 핵심 무결성 제약**
- 암기: `부-자-외-기` (부모 릴레이션, 자식 릴레이션, 외래키, 기본키) / `레-카-널-디` (RESTRICT, CASCADE, SET NULL, SET DEFAULT)
- 판단축:
  - **물리적 외래키(Physical FK Constraint)**: DBMS 엔진이 DDL로 강제하여 무결성을 100% 보장하나, 매 쓰기마다 부모 검사 락(Lock) 발생 및 샤딩/MSA 환경 분산 불가
  - **논리적 외래키(Logical FK Relationship)**: ERD 상에만 관계를 정의하고 DB 레벨 FK는 생략하여 초고속 쓰기 및 분산 확장성 확보하나, 애플리케이션 결함 시 데이터 오염 위험
- 주의: `ON DELETE CASCADE`는 부모 엔티티 삭제 시 자식 엔티티들을 DBMS가 무차별 연쇄 삭제하므로, 실무에서 관리자의 단순 테스트 삭제나 쿼리 실수로 인해 결제/주문 수백만 건이 영구 삭제되는 참사를 유발할 수 있음. 엔터프라이즈 환경에서는 소프트 딜리트(`is_deleted`) 또는 RESTRICT 적용이 원칙임
---

## 1교시 예상문제 (10점)

> 참조 무결성 (Referential Integrity) 및 외래키 연쇄 동작 (CASCADE, RESTRICT)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 참조 무결성의 정의 및 핵심 목적

- **정의**: 자식 릴레이션의 외래키(FK) 값은 반드시 부모 릴레이션의 기본키(PK) 값과 일치하거나 NULL이어야 한다는 관계 데이터 모델의 무결성 제약
- **목적**: 부모 행 삭제 시 자식 행이 고아 레코드(Orphan Record)로 남는 불일치 이상현상 방지

### 2. 부모 DML 조작에 따른 4대 연쇄 동작 규칙 (Action Rules)

| 제어 옵션 | 부모 행 삭제(DELETE) 시 동작 | 실무 권장 사용처 |
|:---|:---|:---|
| **1. RESTRICT** | 자식 행이 1개라도 존재하면 부모 삭제 명령 전체 거부 (에러) | 금융/원장 등 데이터 삭제가 엄격한 코어 시스템 |
| **2. CASCADE** | 부모 삭제 시 해당 부모를 참조하던 자식 행들을 함께 자동삭제 | 강한 소유 관계 (게시글-첨부파일) |
| **3. SET NULL** | 부모 삭제 시 자식 행의 외래키(FK) 값을 NULL로 자동 변경 | 부서 폐쇄 시 소속 사원의 발령 대기 상태 |
| **4. SET DEFAULT** | 부모 삭제 시 자식 행의 외래키(FK) 값을 기본값(Default) 설정 | 임시 부서, 디폴트 계정 등 대체 키 존재 시 |

### 3. 실무 아키텍처 적용 제언

- **물리 FK vs 논리 FK**: 초고속 분산 환경에서는 성능과 데드락 방지를 위해 논리적 FK 채택
- **참사 예방**: 운영 DB에서 물리적 CASCADE DELETE 금지 및 소프트 딜리트(`is_deleted`) 표준화
---

### 핵심 관계

| 제어 옵션 (DDL 문법) | 부모 행 DELETE 발생 시 동작 | 부모 행 UPDATE 발생 시 동작 | 특징 및 권장 사용처 |
|:---|:---|:---|:---|
| **RESTRICT / NO ACTION**<br>`ON DELETE RESTRICT` | 자식 행이 존재하면 **삭제 명령 전체 거부 (에러)** | 자식 행이 존재하면 **수정 명령 전체 거부 (에러)** | 가장 안전함. 엔터프라이즈 시스템의 기본 표준 |
| **CASCADE**<br>`ON DELETE CASCADE` | 부모를 참조하는 **모든 자식 행을 함께 자동 삭제** | 부모의 변경된 신규 PK 값을 **자식 FK에 자동 반영** | 강한 소유 관계(게시글-첨부파일, 주문-주문상세) |
| **SET NULL**<br>`ON DELETE SET NULL` | 자식 행을 유지하되, **FK 컬럼 값을 NULL로 세팅** | 자식 행을 유지하되, **FK 컬럼 값을 NULL로 세팅** | FK 컬럼이 Nullable이어야 함 (부서 폐쇄 시 발령 대기) |
| **SET DEFAULT**<br>`ON DELETE SET DEFAULT` | 자식 행의 **FK 컬럼 값을 사전에 정의된 기본값 세팅** | 자식 행의 **FK 컬럼 값을 사전에 정의된 기본값 세팅** | 기본값(Default)이 부모 테이블에 실존해야 함 |

---

## 2~4교시 예상문제 (25점)

> 데이터 모델링에서 관계형 데이터베이스의 일관성을 유지하기 위한 참조 무결성(Referential Integrity)의 개념과 구성요소를 설명하고, 부모 및 자식 데이터 조작(DML) 시 발생하는 제약 위반 상황과 4가지 연쇄 제어 규칙(Action Rules)을 비교하시오. (10점 / 25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 관계 데이터 정합성을 보장하는 참조 무결성 개요

#### 한줄 요약: 외래키는 유효한 부모 키를 참조하거나 NULL이어야 한다는 제약으로 고아 레코드 생성을 원천 차단하는 원칙

- **발생 배경**:
  - 데이터베이스가 정규화(Normalization)를 거치면 단일 테이블이 여러 릴레이션으로 분해(Decomposition)됨
  - 분해된 릴레이션 간의 연결고리인 외래키(Foreign Key)에 무효한 값이 입력되거나 부모 행이 무단 삭제되면 비즈니스 데이터의 일관성이 붕괴됨
- **참조 무결성(Referential Integrity)의 정의**:
  - 관계형 모델의 기본 제약조건 중 하나로, 릴레이션 $R_2$(자식)의 외래키 $FK$가 릴레이션 $R_1$(부모)의 기본키 $PK$를 참조할 때, $R_2$의 임의의 튜플에 대해 다음 조건이 반드시 성립해야 함:
    $$\forall t_2 \in R_2, \quad (t_2[FK] = \text{NULL}) \quad \lor \quad (\exists t_1 \in R_1 \text{ such that } t_2[FK] = t_1[PK])$$
- **고아 레코드(Orphan Record)**:
  - 부모 릴레이션의 해당 레코드가 이미 삭제되었음에도 불구하고, 자식 릴레이션에 남아 실존하지 않는 대상을 가리키고 있는 쓰레기 데이터

### Ⅱ. 참조 무결성의 동작 메커니즘 및 위반 시나리오

#### 한줄 요약: 자식의 신규 INSERT/UPDATE 시 부모 존재 검증, 부모의 DELETE/UPDATE 시 자식의 참조 상태 검증

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 135" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="115" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">DML 발생 시 참조 무결성 검증 포인트</text>

  <!-- Left: Child DML -->
  <g transform="translate(30, 42)">
    <rect x="0" y="0" width="220" height="70" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="110" y="18" font-size="9.5" font-weight="bold" fill="#1e40af" text-anchor="middle">[자식 릴레이션 조작 시]</text>
    <text x="12" y="36" font-size="8.5" fill="#334155">&bull; INSERT: 새 FK가 부모 PK에 존재하는가?</text>
    <text x="12" y="52" font-size="8.5" fill="#334155">&bull; UPDATE: 변경 FK가 부모 PK에 존재하는가?</text>
    <text x="12" y="66" font-size="7.5" fill="#dc2626">(불일치 시 즉시 ORA-02291 에러 롤백)</text>
  </g>

  <!-- Right: Parent DML -->
  <g transform="translate(270, 42)">
    <rect x="0" y="0" width="220" height="70" rx="4" fill="#ffffff" stroke="#ef4444" stroke-width="1.2"/>
    <text x="110" y="18" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">[부모 릴레이션 조작 시]</text>
    <text x="12" y="36" font-size="8.5" fill="#334155">&bull; DELETE: 삭제 PK를 참조하는 자식이 있는가?</text>
    <text x="12" y="52" font-size="8.5" fill="#334155">&bull; UPDATE: 수정 PK를 참조하는 자식이 있는가?</text>
    <text x="12" y="66" font-size="7.5" fill="#b91c1c">(연쇄 제어 규칙 Action Rule에 따라 분기)</text>
  </g>
</svg>
</div>

### 1. 자식 릴레이션 조작 시 위반 검증
- **INSERT 위반**: 존재하지 않는 부서코드('D99')를 가진 사원을 삽입하려 할 때, DBMS는 즉시 `ORA-02291(integrity constraint violated - parent key not found)` 에러를 발생시키고 롤백
- **UPDATE 위반**: 기존 사원의 부서코드를 존재하지 않는 부서로 변경할 때 에러 발생

### 2. 부모 릴레이션 조작 시 위반 처리
- 부모 테이블의 특정 행을 삭제하거나 PK 값을 변경하려 할 때, 해당 행을 참조하는 자식 튜플이 1개라도 존재한다면 참조 무결성 충돌이 발생함
- 이때 사전에 DDL로 정의된 **연쇄 제어 규칙(Action Rule)**에 따라 동작이 분기됨

### Ⅲ. 참조 무결성 4대 연쇄 제어 규칙 (Action Rules)

#### 한줄 요약: 부모 튜플의 삭제 및 수정 시 자식 튜플의 생존과 상태 전이를 결정하는 4가지 DDL 옵션

| 제어 옵션 (DDL 문법) | 부모 행 DELETE 발생 시 동작 | 부모 행 UPDATE 발생 시 동작 | 특징 및 권장 사용처 |
|:---|:---|:---|:---|
| **RESTRICT / NO ACTION**<br>`ON DELETE RESTRICT` | 자식 행이 존재하면 **삭제 명령 전체 거부 (에러)** | 자식 행이 존재하면 **수정 명령 전체 거부 (에러)** | 가장 안전함. 엔터프라이즈 시스템의 기본 표준 |
| **CASCADE**<br>`ON DELETE CASCADE` | 부모를 참조하는 **모든 자식 행을 함께 자동 삭제** | 부모의 변경된 신규 PK 값을 **자식 FK에 자동 반영** | 강한 소유 관계(게시글-첨부파일, 주문-주문상세) |
| **SET NULL**<br>`ON DELETE SET NULL` | 자식 행을 유지하되, **FK 컬럼 값을 NULL로 세팅** | 자식 행을 유지하되, **FK 컬럼 값을 NULL로 세팅** | FK 컬럼이 Nullable이어야 함 (부서 폐쇄 시 발령 대기) |
| **SET DEFAULT**<br>`ON DELETE SET DEFAULT` | 자식 행의 **FK 컬럼 값을 사전에 정의된 기본값 세팅** | 자식 행의 **FK 컬럼 값을 사전에 정의된 기본값 세팅** | 기본값(Default)이 부모 테이블에 실존해야 함 |

### Ⅳ. 관계형 데이터베이스 3대 무결성 비교

#### 한줄 요약: 기본키의 유일성을 지키는 개체 무결성, 릴레이션 간 연결을 지키는 참조 무결성, 속성값 범위를 지키는 도메인 무결성

| 무결성 종류 | 핵심 정의 및 제약 규칙 | 대상 오브젝트 | 위반 시 사례 | 대표 DDL 제약조건 |
|:---|:---|:---|:---|:---|
| **개체 무결성 (Entity)** | 릴레이션의 기본키는 절대 NULL일 수 없으며 유일해야 함 | 단일 릴레이션 (기본키) | 주민번호나 사원ID가 NULL이거나 중복 등록됨 | `PRIMARY KEY`<br>(`NOT NULL` + `UNIQUE`) |
| **참조 무결성 (Referential)** | 외래키 값은 유효한 부모의 기본키이거나 NULL이어야 함 | 두 릴레이션 간 (부모-자식) | 존재하지 않는 고객 번호로 주문서가 생성됨 | `FOREIGN KEY ... REFERENCES` |
| **도메인 무결성 (Domain)** | 속성값은 사전 정의된 데이터 타입, 길이, 허용 범위를 만족해야 함 | 개별 속성 (컬럼) | 나이 컬럼에 음수(-5)가 들어가거나 문자열 입력 | `CHECK`, `DEFAULT`, `DATA TYPE` |

### Ⅴ. 물리적 외래키(Physical FK) vs 논리적 외래키(Logical FK) 아키텍처 비교

#### 한줄 요약: 엄격한 DB 강제 무결성과 고성능·확장성을 지향하는 애플리케이션 제어 간의 실무 아키텍처 트레이드오프

| 비교 항목 | 물리적 외래키 (Physical FK) | 논리적 외래키 (Logical FK) |
|:---|:---|:---|
| **제약조건 생성 여부** | 데이터베이스에 `ADD CONSTRAINT ... FOREIGN KEY` 등록 | 물리적 제약조건 없음 (일반 B-Tree 인덱스만 생성) |
| **무결성 강제 주체** | **DBMS 엔진** (위반 시 SQL 즉시 실패) | **애플리케이션(Application) 서비스 로직** |
| **쓰기(INSERT) 성능** | **느림** (부모 테이블 인덱스 조회 및 S-Lock 획득 부하) | **극도로 빠름** (추가적인 참조 테이블 조회 오버헤드 제로) |
| **데드락(Deadlock) 위험** | **높음** (외래키 인덱스 부재 시 테이블 락 또는 부모 락 경합) | **낮음** (DB 레벨의 연쇄 잠금 메커니즘 배제) |
| **분산 환경 지원** | **불가** (DB가 물리적으로 분리된 샤딩/MSA에서 동작 불능) | **최적** (네트워크 API를 통해 서비스 간 무결성 제어) |
| **실무 적용 영역** | 코어 금융 원장, 소규모 일체형 ERP | 대규모 포털, 전자상거래 주문/결제, MSA 아키텍처 |

### Ⅵ. 대규모 트래픽 및 MSA 환경에서의 실무 엔지니어링 패턴

#### 한줄 요약: 대량 배치 시 제약 비활성화, 지연 검사(DEFERRABLE), MSA에서의 Saga 패턴 및 결과적 일관성 확보

### 1. 대용량 데이터 배치 적재 시 제약 비활성화
- 1,000만 건 이상의 데이터를 벌크 인서트할 때 FK 제약이 켜져 있으면 I/O가 10배 이상 폭증함
- 작업 시작 전 FK를 비활성화(`ALTER TABLE ... DISABLE NOVALIDATE CONSTRAINT ...`)하고, 적재 완료 후 일괄 검증 및 활성화(`ENABLE NOVALIDATE`) 수행

### 2. 지연된 제약조건 검사 (Deferred Constraint Checking)
- 순환 참조(Mutual Dependency)가 존재하는 복잡한 트랜잭션에서는 문장 단위가 아닌 트랜잭션 커밋 시점까지 외래키 검증을 유예:
  ```sql
  ALTER TABLE order_item ADD CONSTRAINT fk_order 
  FOREIGN KEY (order_id) REFERENCES orders(id) DEFERRABLE INITIALLY DEFERRED;
  ```

### 3. 마이크로서비스(MSA) 환경의 참조 무결성: Saga 패턴
- 주문 서비스 DB와 회원 서비스 DB가 물리적으로 분리된 환경에서는 RDBMS의 참조 무결성을 사용할 수 없음
- 카프카(Kafka) 이벤트 기반의 **Saga 패턴(Orchestration / Choreography)**을 적용하여 회원 탈퇴 이벤트 발생 시 주문 서비스로 이벤트를 발행하고, 결과적 일관성(Eventual Consistency)으로 관계를 정리

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 참조 무결성은 "순수 DB 모델링의 이상향"과 "현대 대용량 분산 시스템의 현실"이 가장 첨예하게 충돌하는 지점이다. 교과서적으로는 물리적 외래키(Physical FK)를 모든 관계에 걸어야 맞지만, 초당 수만 건의 쓰기가 발생하는 e커머스나 MSA 환경에서는 물리적 FK가 락 경합과 데드락의 주범이 된다. 실무에서는 DB 레벨 FK를 제거하고 인덱스만 생성하는 **논리적 외래키**를 채택하되, 이로 인해 필연적으로 발생하는 고아 레코드를 청소하기 위해 야간에 **정기 데이터 정합성 대사(Data Reconciliation) 배치**를 반드시 파이프라인으로 구축해야 한다.

> **[나라면 이렇게 쓴다]**
> 10점형이라면 부모 DELETE 시 4대 Action Rule(RESTRICT, CASCADE, SET NULL, SET DEFAULT)의 발현 양상을 표와 사례로 명쾌하게 정리하겠다. 25점형이라면 "운영 환경에서 물리적 ON DELETE CASCADE의 위험성"을 경고하고, 소프트 딜리트(`is_deleted`) 표준화 및 MSA 환경에서의 Saga 패턴 기반 결과적 무결성 확보 방안을 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 물리적 FK 강제 시 부모 확인 락으로 인한 쓰기 지연 및 데드락 발생, 반면 물리 FK 미적용 시 고아 레코드 누적 위험
- **대응 (개선 방안)**: 대용량 트랜잭션 테이블은 논리적 FK 및 인덱스를 채택하고, 애플리케이션 계층 소프트 딜리트 표준화 및 야간 정합성 대사 배치 운영
- **검증 (검증 기준)**: 야간 데이터 대사 시 고아 레코드 발생률 0% 검증, 벌크 배치 시 제약 비활성화로 로딩 처리량 5배 향상 확인
- **효과 (실행 효과)**: 대규모 트랜잭션 동시성 확보 및 데드락 원천 차단, 고아 레코드 사전 격리를 통한 비즈니스 데이터 무결성 보장

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">물리적 FK로 인한 락 경합/데드락 및 무분별한 CASCADE 참사 위험</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">논리적 FK 전환 + 소프트 딜리트 표준화 + 야간 정합성 대사 배치</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">고아 레코드 0건 대사, INSERT 레이턴시 50% 단축, 데드락 0건</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">분산 트랜잭션 처리량 극대화 및 엔터프라이즈 데이터 일관성 완결</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제138회 1교시 9번 (정보모델링의 참조 무결성)
  - 컴퓨터시스템응용기술사 제128회 1교시 (관계형 데이터베이스의 무결성 제약조건 3종)
  - 정보관리기술사 제117회 1교시 (외래키 제약조건과 데이터베이스 성능 간의 상관관계)
- **표준 및 검증 출처**:
  - E. F. Codd (1970), "A Relational Model of Data for Large Shared Data Banks", *ACM*
  - ISO/IEC 9075:2016 (SQL Standard - Referential Constraints)
  - Oracle Database 19c Concepts Guide, "Data Integrity: Referential Integrity Constraints"
---

## 연결 토픽

- [013. 무결성 제약 (Integrity Constraint)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/013_integrity_constraint.md)
- [042. 데이터 모델링 (Data Modeling)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/042_data_modeling.md)
- [028. ERD (Entity Relationship Diagram)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/028_erd.md)
