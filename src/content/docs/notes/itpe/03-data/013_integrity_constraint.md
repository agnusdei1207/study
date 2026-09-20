---
title: "무결성 제약(데이터 무결성)"
author: "Codex"
date: "2026-09-20T19:53:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터베이스에서 관계형 데이터 모델 및 무결성 제약으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 모델링·RDBMS</span>
  <strong>무결성 제약(데이터 무결성)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 데이터의 정확성(Accuracy), 유효성(Validity), 일관성(Consistency)을 유지하기 위해 DBMS가 데이터의 삽입·수정·삭제 연산 시 자동으로 강제하는 선언적·절차적 불변 규칙
- 4대 릴레이션 무결성: 개체 무결성(PK Not-Null), 참조 무결성(FK 일치/Null), 도메인 무결성(값 범위), 키 무결성(튜플 유일성) + 사용자 정의 무결성
- 참조 동작 옵션: RESTRICT / NO ACTION(거부), CASCADE(연쇄), SET NULL(널 치환), SET DEFAULT(기본값 치환)

<div class="itpe-flow-map" role="img" aria-label="데이터 무결성 제약조건 및 연산 통제 흐름">
  <div class="itpe-flow-node"><strong>DML 트랜잭션 (Insert / Update / Delete)</strong></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>DBMS 무결성 검증 엔진</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>개체 무결성</strong><span>PK 중복 및 NULL 입력 차단</span></div>
      <div class="itpe-flow-branch"><strong>참조 무결성</strong><span>부모 없는 고아 레코드(FK) 생성 차단</span></div>
      <div class="itpe-flow-branch"><strong>도메인/키</strong><span>타입·범위(CHECK) 및 후보키 유일성(UNIQUE)</span></div>
      <div class="itpe-flow-branch"><strong>업무 무결성</strong><span>트리거 및 비즈니스 로직 제약 검증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>결과 분기 (Commit vs Rollback)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>통과</strong><span>데이터베이스 물리 디스크 반영 (Commit)</span></div>
      <div class="itpe-flow-branch"><strong>위배</strong><span>즉시 에러 반환 및 트랜잭션 원자적 롤백</span></div>
    </div>
  </div>
</div>

## 예상문제

<details><summary>핵심 용어</summary>

- `Entity Integrity`: 기본키의 유일성과 Null 불허 규칙
- `Referential Integrity`: 외래키가 부모키 또는 Null이어야 하는 규칙
- `Domain Integrity`: 타입·범위·형식에 대한 값 규칙
- `CASCADE·RESTRICT`: 부모 변경 시 자식 처리 또는 거부 정책

</details>

> 관계형 데이터베이스에서 데이터 무결성(Data Integrity)의 개념과 릴레이션 4대 무결성 제약(개체, 참조, 도메인, 키)을 비교하고, 부모-자식 테이블 간 참조 무결성 유지를 위한 4대 참조 조치(CASCADE, RESTRICT, SET NULL 등) 및 성능 최적화 방안을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **릴레이션 무결성 제약(Relation Integrity)** | Codd의 관계형 모델에 기반한 개체, 참조, 도메인, 키 무결성 등 관계적 불변 제약조건 | Ⅱ 핵심 분류 |
| **데이터 무결성(Data Integrity)** | 데이터의 라이프사이클 전반에 걸쳐 결점 없이 완전하고 일관된 상태를 유지하는 성질 | Ⅰ 개요 |

## Ⅰ. 데이터 신뢰성을 지키는 제1 방어선, 데이터 무결성 제약의 개요

> 무결성 제약은 데이터의 생성·변형 시 불일치와 오류를 방지하기 위해 DBMS가 강제하는 데이터 규칙임.

- 정의: 데이터베이스 내에 저장된 데이터의 정확성(Accuracy), 일관성(Consistency), 유효성(Validity)을 보장하기 위해 데이터 조작(Insert, Update, Delete) 시 반드시 준수되어야 하는 논리적 제약조건
- 필요성: 애플리케이션 버그나 동시성 경합으로 인해 존재하지 않는 부모 데이터를 참조하거나, 식별자가 중복되는 등 데이터베이스가 오염되는 사태를 데이터 계층에서 원천 차단
- 구현 방식: DBMS 스키마 DDL에 선언하는 선언적 제약(Declarative Constraint)과 트리거/프로시저로 구현하는 절차적 제약(Procedural Constraint)으로 양분

## Ⅱ. 릴레이션 4대 무결성 제약조건 비교

> 개체(PK), 참조(FK), 도메인(Type/Check), 키(Unique)가 RDBMS 무결성의 4대 기둥임.

<div class="itpe-pipeline" role="img" aria-label="릴레이션 무결성 4대 제약">
  <div class="itpe-pipeline-node"><strong>개체 무결성</strong><div class="itpe-step-detail"><span>규칙</span><span>PK Not-Null · Unique</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>참조 무결성</strong><div class="itpe-step-detail"><span>규칙</span><span>FK 일치 또는 Null</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>도메인 무결성</strong><div class="itpe-step-detail"><span>규칙</span><span>데이터 타입 · Check</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>키 무결성</strong><div class="itpe-step-detail"><span>규칙</span><span>후보키 유일성</span></div></div>
</div>

| 제약조건 유형 | 핵심 규칙 및 수학적 정의 | 위배 시 발생하는 문제 | DDL 구현 예시 |
|---|---|---|---|
| **개체 무결성 (Entity)** | 릴레이션의 기본키(PK)는 유일해야 하며 어떠한 경우에도 NULL 값을 가질 수 없음 | 특정 튜플의 고유한 식별이 불가능해져 데이터 중복 및 접근 불가 발생 | `PRIMARY KEY` |
| **참조 무결성 (Referential)** | 외래키(FK) 값은 참조하는 부모 릴레이션의 기본키 값이거나 NULL이어야 함 | 부모가 없는 고아 레코드(Orphan Record)가 발생하여 조인 오류 유발 | `FOREIGN KEY REFERENCES` |
| **도메인 무결성 (Domain)** | 속성에 입력되는 값은 해당 속성에 정의된 도메인(타입, 길이, 범위)에 속해야 함 | 나이 컬럼에 음수 입력, 날짜 컬럼에 문자열 입력 등 데이터 타입 파손 | `CHECK`, `NOT NULL`, 도메인 타입 |
| **키 무결성 (Key)** | 모든 릴레이션은 튜플을 유일하게 식별할 수 있는 하나 이상의 키(후보키)를 가져야 함 | 릴레이션 내에 모든 속성값이 동일한 완전 중복 행(Duplicate Row) 발생 | `UNIQUE` |
| **사용자 정의 무결성** | 4대 기본 제약 외에 비즈니스 업무 규칙(Business Rule)을 만족해야 함 | 결제 금액이 상품 정가보다 크거나, 탈퇴 회원의 주문 상태 변경 등 업무 왜곡 | `TRIGGER`, Stored Procedure |

## Ⅲ. 참조 무결성 유지를 위한 4대 참조 조치 정책

> 부모 레코드 삭제·수정 시 자식 레코드를 연쇄 처리하거나 조작을 거부함.

```sql
CREATE TABLE orders (
  order_id    BIGINT PRIMARY KEY,
  customer_id BIGINT NOT NULL,
  CONSTRAINT fk_orders_customer
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
    ON DELETE RESTRICT     -- 자식이 있으면 부모 삭제 거부
    ON UPDATE CASCADE      -- 부모 키 변경 시 자식 FK 자동 연쇄 갱신
);
```

| 참조 조치 옵션 | 부모 레코드 삭제(Delete) 시 동작 | 부모 레코드 수정(Update) 시 동작 | 권장 적용 업무 도메인 |
|---|---|---|---|
| **RESTRICT / NO ACTION** | 자식 레코드가 하나라도 존재하면 부모 삭제 즉시 거부(Rollback) | 자식 레코드가 참조 중이면 부모 키 수정 즉시 거부 | 금융 원장, 고객 마스터, 결제 트랜잭션 등 핵심 데이터 |
| **CASCADE (연쇄)** | 부모 삭제 시 해당 부모를 참조하는 모든 자식 레코드도 자동 연쇄 삭제 | 부모 키 변경 시 자식의 외래키 값도 동일하게 자동 연쇄 수정 | 주문-주문상세, 게시글-첨부파일 등 생명주기 일치 복합 엔티티 |
| **SET NULL** | 부모 삭제 시 자식의 외래키 컬럼 값을 NULL로 자동 변경 | 부모 키 수정 시 자식의 외래키 값을 NULL로 자동 변경 | 부서-사원(부서 폐지 시 사원의 부서코드를 임시 NULL 지정) |
| **SET DEFAULT** | 부모 삭제 시 자식의 외래키 컬럼 값을 사전에 정의된 기본값으로 변경 | 부모 키 수정 시 자식의 외래키 값을 기본값으로 변경 | 미분류 카테고리(`'000'`)가 존재하는 상품 분류 체계 |

## Ⅳ. 선언적 제약 vs 절차적 제약 비교

> 단순 도메인과 식별자는 DDL 제약으로, 복잡한 시점·교차 테이블 검증은 트리거로 구현함.

| 비교 기준 | 선언적 제약조건 (Declarative Constraint) | 절차적 제약조건 (Procedural Constraint) |
|---|---|---|
| **구현 수단** | SQL DDL 제약조건 키워드 (PK, FK, UNIQUE, CHECK) | Trigger, Stored Procedure, Application Logic |
| **검증 위치** | DBMS 커널 엔진 레벨에서 직접 검사 | 트랜잭션 실행 시 프로시저/트리거 인터럽트 실행 |
| **성능 및 오버헤드** | 매우 빠름 (인덱스 활용 및 최소 CPU 연산) | 트리거 실행에 따른 컨텍스트 스위칭 및 I/O 부하 증가 |
| **유지보수성** | 스키마 카탈로그에 명시되어 변경 추적 용이 | 복잡하게 얽힌 트리거는 디버깅 및 형상 관리가 극도로 난해 |
| **적용 권장** | 개체, 참조, 단순 값 범위 제약 (기본 원칙) | 두 개 이상 테이블 간 교차 집계 제약, 시계열 검증 |

## Ⅴ. 무결성 제약과 시스템 성능 간의 트레이드오프

> 완벽한 무결성 검증은 쓰기 I/O 오버헤드를 유발하므로 대량 적재 시 유연한 튜닝이 필요함.

```text
[외래키(FK) 인덱스 부재 시의 락(Lock) 전파 문제]
  부모 테이블 행 수정/삭제 ──▶ 자식 테이블 전체에 Table Share Lock 발생!
  * 해결책: 자식 테이블의 외래키(FK) 컬럼에 B-Tree 인덱스를 반드시 생성해야 Row-level Lock으로 국소화됨.
```
- **대량 데이터 배치(Batch) 적재 지연**: 수천만 건 데이터를 삽입할 때 매 행마다 PK/FK 제약을 검증하면 성능이 급감함.
  - 대책: `ALTER TABLE ... DISABLE CONSTRAINT`로 제약을 일시 비활성화 $\to$ 고속 Direct Path Load $\to$ 정제 후 `ENABLE NOVALIDATE`로 활성화.

## Ⅵ. 실무 고려사항 및 장애 대책

> 고아 데이터 유입과 외래키 인덱스 누락으로 인한 락 경합을 사전에 통제함.

- 적용 상황: MSA 분산 DB 환경 및 대규모 ERP 마이그레이션

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **자식 테이블 전체 락(Lock) 경합** | 외래키(FK) 컬럼에 전용 B-Tree 인덱스 누락 | FK 컬럼 인덱스 생성 전수 검증 스크립트 가동 | 부모 행 수정 시 자식 테이블 락 전파 원천 차단 |
| **MSA 분산 DB 고아 데이터 발생** | 주문 DB와 회원 DB 분리로 인해 물리적 FK 선언 불가 | 분산 트랜잭션(Saga Pattern) 및 CDC 기반 최종 일관성 검증 파이프라인 | 서비스 독립성과 데이터 정합성 양립 |
| **CASCADE 연쇄 삭제 대참사** | 대형 테이블 간 CASCADE 설정 후 단일 부모 삭제 시 수백만 자식 행 동시 삭제 | 운영 DB에서 ON DELETE CASCADE 금지, 논리적 삭제(Soft Delete: `is_deleted='Y'`) 표준화 | 데이터 오삭제 방지 및 복구력 확보 |

## Ⅶ. 결론 및 기술사적 제언

> 데이터 무결성은 애플리케이션 코드가 아니라 데이터 계층(DBMS)에서 최종 보장되어야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 성능을 이유로 DBMS의 무결성 제약(PK/FK)을 모두 해제하고 '애플리케이션 코드로 검증하겠다'고 주장하는 개발팀이 종종 있음. 그러나 애플리케이션 버그, 배치 스크립트 직접 실행, 직접 SQL 수정 등의 우회 경로를 통해 고아 데이터가 유입되는 순간 RDBMS의 존재 가치는 완전히 소멸함.
- 나라면: 엔터프라이즈 RDBMS 구축 시 모든 식별자와 참조 관계에 선언적 제약(PK, FK)과 FK 전용 인덱스를 100% 필수 강제하고, 대량 적재 시에만 선별적 제약 비활성화/재활성화 파이프라인을 적용하여, 성능과 무결성의 타협 없는 아키텍처 기준선을 확립하겠음.

### 실전 답안용 기술사적 제언
- 판정: 가능한 규칙은 DBMS 선언 제약으로 최종 보장
- 대안: PK·FK·CHECK와 FK 인덱스, 예외 적재 후 전수 검증
- 검증: 고아행·중복키·도메인 위반 0건과 락 대기 측정
- 효과: 우회 경로의 데이터 오염과 쓰기 병목 동시 방지
<div class="itpe-flow-map" role="img" aria-label="무결성 제약 운영 제언"><div class="itpe-flow-node"><strong>현행 한계</strong><span>문제: 애플리케이션 검증 의존</span></div><div class="itpe-flow-arrow">↓</div><div class="itpe-flow-node"><strong>개선안</strong><span>대안: 선언 제약·FK 인덱스</span></div><div class="itpe-flow-arrow">↓</div><div class="itpe-flow-node is-current"><strong>검증·효과</strong><span>판정: 위반 0건·락 대기 측정</span><span>효과: 정합성과 성능 확보</span></div></div>

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 데이터 무결성 제약은 데이터의 정확성, 일관성, 유효성을 보증하기 위해 삽입·수정·삭제 시 DBMS가 강제하는 규칙(개체, 참조, 도메인, 키)임.

### 2. 핵심 메커니즘 / 체계
```text
[개체 무결성] PK: Not Null & Unique
[참조 무결성] FK: 부모 PK 일치 or Null (RESTRICT, CASCADE, SET NULL)
[도메인 무결성] Type, Length, CHECK, NOT NULL
[키 무결성] 후보키 유일성 (UNIQUE)
```
- DDL 선언적 제약으로 1차 통제하고, 복합 규칙은 트리거로 보완함.

### 3. 적용 제언
- 외래키(FK) 컬럼에는 반드시 B-Tree 인덱스를 생성하여 부모 변경 시 자식 테이블 락(Lock) 전파를 방어하고, Soft Delete로 CASCADE 위험을 예방해야 함.

## 출제 이력과 검증 출처

- [PostgreSQL Documentation, Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- [MySQL Reference Manual, Constraints](https://dev.mysql.com/doc/refman/8.4/en/constraints.html)

## 학습 체크

- [ ] 릴레이션 4대 무결성 제약(개체, 참조, 도메인, 키)의 정의와 차이를 설명할 수 있는가?
- [ ] 참조 무결성의 4대 동작 옵션(RESTRICT, CASCADE, SET NULL 등)을 제시할 수 있는가?
- [ ] 외래키(FK) 컬럼에 인덱스를 생성해야 하는 성능적 이유(Lock 전파 방지)를 논할 수 있는가?

## 연결 토픽

- 이전 토픽: [z-검정(z-test)](./012_z_test.md)
- 연관 토픽: [참조 무결성](./070_referential_integrity.md), [키(Key)](./157_key.md), [정규화](./019_normalization.md)
- 다음 토픽: [중심극한정리·대수의 법칙](./014_central_limit_theorem.md)
