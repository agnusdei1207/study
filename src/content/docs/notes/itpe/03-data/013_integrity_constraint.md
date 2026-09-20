---
title: "무결성 제약(데이터 무결성)"
category: "03-data"
tags:
  - "무결성제약"
  - "개체무결성"
  - "참조무결성"
  - "도메인무결성"
  - "CASCADE"
  - "고아데이터"
date: "2026-09-20T23:02:00+09:00"
author: "기술사 수험생"
extra:
  model: "Antigravity-v2"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터베이스에서 관계형 데이터 모델 및 무결성 제약으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 모델링·RDBMS</span>
  <strong>무결성 제약(데이터 무결성)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 데이터의 정확성(Accuracy), 유효성(Validity), 일관성(Consistency)을 유지하기 위해 DBMS가 데이터 조작(Insert, Update, Delete) 시 자동으로 강제하는 선언적·절차적 불변 규칙
- 메커니즘: DML 요청 $\rightarrow$ 선언적 4대 제약(개체·참조·도메인·키) 검증 $\rightarrow$ 참조 동작 옵션(RESTRICT/CASCADE) 판정 $\rightarrow$ 위배 여부 분기 $\rightarrow$ 커밋/롤백
- 산출물: DDL 제약조건 명세서 · 참조 무결성 ERD 다이어그램 · 외래키(FK) 인덱스 정의서 · 고아 데이터(Orphan) 감사 로그

<div class="itpe-flow-map" role="img" aria-label="데이터 무결성 검증 및 트랜잭션 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: DML 트랜잭션 연산 수신</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>요청</strong><span>Insert, Update, Delete 연산 시도 및 데이터 블록 락(Lock) 획득</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: DBMS 선언적 무결성 엔진 검증</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>개체 무결성</strong><span>기본키(PK) 유일성(Unique) 및 Not Null 규칙 검증</span></div>
      <div class="itpe-flow-branch"><strong>참조 무결성</strong><span>외래키(FK)의 부모 테이블 존재 여부 및 RESTRICT/CASCADE 판정</span></div>
      <div class="itpe-flow-branch"><strong>도메인/키</strong><span>CHECK 조건식, 허용 데이터 타입 및 후보키 UNIQUE 검증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: 무결성 규칙 준수 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>조작 데이터가 모든 릴레이션 무결성 제약을 충족하며 고아 레코드가 발생하지 않는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (물리 디스크 반영)</strong>
      <span>무결성 검증 완료 $\rightarrow$ 트랜잭션 정상 커밋(Commit) 및 WAL 로깅</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (제약조건 위배 / 고아 데이터)</strong>
      <span>즉시 ORA 에러 반환 $\rightarrow$ 트랜잭션 원자적 롤백(Rollback) 및 세션 통보</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Entity Integrity(개체 무결성)`: 기본키(PK)를 구성하는 어떤 속성도 Null 값을 가질 수 없으며, 릴레이션 내에서 유일해야 한다는 규칙
- `Referential Integrity(참조 무결성)`: 외래키(FK) 값은 참조하는 부모 릴레이션의 기본키 값과 일치하거나 Null이어야 한다는 규칙 (고아 레코드 방지)
- `CASCADE`: 부모 테이블의 튜플이 삭제되거나 수정될 때 이를 참조하는 자식 튜플도 연쇄적으로 함께 삭제/수정되는 옵션
- `RESTRICT / NO ACTION`: 자식 테이블에서 참조 중인 부모 튜플의 삭제나 수정을 원천 거부하고 에러를 발생시키는 옵션
- `Declarative Constraint(선언적 제약)`: DDL 문법(PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE)을 통해 DBMS 카탈로그에 직접 정의하는 가장 안전한 제약

</details>

## 예상문제

> 관계형 데이터베이스에서 데이터 무결성(Data Integrity)의 개념과 릴레이션 4대 무결성 제약(개체, 참조, 도메인, 키)을 비교하고, 부모-자식 테이블 간 참조 무결성 유지를 위한 4대 참조 조치(CASCADE, RESTRICT, SET NULL 등) 및 성능 최적화 방안을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **참조 무결성 조치 옵션** | CASCADE(연쇄), RESTRICT(거부), SET NULL, SET DEFAULT | Ⅲ 참조 조치 |
| **선언적 제약 vs 절차적 제약** | DDL 제약조건(PK/FK/CHECK) vs 트리거(Trigger) 및 프로시저 비교 | Ⅳ 구현 방식 |
| **외래키 인덱스와 성능 최적화** | FK 컬럼 인덱스 부재 시 부모 갱신 시 자식 테이블 락(Lock) 경합 해결 | Ⅴ 성능 고려사항 |

## Ⅰ. 데이터 신뢰성을 지키는 제1 방어선, 데이터 무결성 제약의 개요

> 무결성 제약은 데이터의 생성·변형 시 불일치와 오류를 방지하기 위해 DBMS가 강제하는 데이터 규칙임.

- 정의: 데이터베이스 내에 저장된 데이터의 정확성(Accuracy), 일관성(Consistency), 유효성(Validity)을 보장하기 위해 데이터 조작(Insert, Update, Delete) 시 반드시 준수되어야 하는 논리적 제약조건
- 필요성: 애플리케이션 버그나 동시성 경합으로 인해 존재하지 않는 부모 데이터를 참조하거나, 식별자가 중복되는 등 데이터베이스가 오염되는 사태를 데이터 계층에서 원천 차단
- 구현 방식: DBMS 스키마 DDL에 선언하는 선언적 제약(Declarative Constraint)과 트리거/프로시저로 구현하는 절차적 제약(Procedural Constraint)으로 양분

## Ⅱ. 릴레이션 4대 무결성 제약조건 비교

> Codd의 관계형 모델에 기반하여 테이블 설계 시 반드시 반영되어야 하는 불변 규칙 체계임.

| 제약조건 | 핵심 규칙 및 정의 | 위반 시 문제점 | DDL 선언 구문 |
|---|---|---|---|
| **개체 무결성 (Entity)** | 릴레이션의 기본키(PK)는 유일해야 하며, Null 값을 가질 수 없음 | 튜플 간 고유 식별 불가능, 데이터 접근 모호성 발생 | `PRIMARY KEY (col)` |
| **참조 무결성 (Referential)** | 외래키(FK) 값은 부모 테이블의 기본키 값이거나 Null이어야 함 | 부모가 없는 고아 레코드(Orphan Data) 난립 | `FOREIGN KEY REFERENCES` |
| **도메인 무결성 (Domain)** | 속성 값은 사전에 정의된 데이터 타입, 길이, 허용 범위를 만족해야 함 | 비정상 포맷 데이터 유입, 연산 에러 발생 | `CHECK (col > 0), NOT NULL` |
| **키 무결성 (Key)** | 모든 릴레이션은 튜플을 유일하게 식별할 수 있는 최소 1개 이상의 후보키 보유 | 중복 레코드 삽입으로 인한 데이터 무결성 파괴 | `UNIQUE (col)` |

## Ⅲ. 부모-자식 간 참조 무결성 4대 조치 옵션

> 부모 테이블의 레코드 삭제/수정 시 자식 테이블이 취해야 할 무결성 수호 동작을 규정함.

```text
[부모 테이블: 회원(PK)] ──(회원 탈퇴: DELETE 발생!)──> [자식 테이블: 주문(FK)]
  - RESTRICT: 탈퇴 거부! (주문 내역이 있으므로 탈퇴 불가 에러)
  - CASCADE : 회원 탈퇴 시 주문 내역도 함께 연쇄 삭제!
  - SET NULL: 회원 탈퇴 시 주문 내역의 회원ID 컬럼을 NULL로 치환
```

| 참조 동작 옵션 | 부모 데이터 삭제(ON DELETE) 시 동작 | 적합 적용 시나리오 | 주의사항 및 리스크 |
|---|---|---|---|
| **RESTRICT / NO ACTION** | 자식 테이블에서 참조 중인 경우 부모 행 삭제/수정 원천 거부 | 금융 거래 내역, 원장 데이터 (기본 표준) | 자식 데이터를 먼저 수동 정리해야 하는 번거로움 |
| **CASCADE** | 부모 데이터 삭제/수정 시 참조하는 자식 튜플을 연쇄 자동 삭제/수정 | 주문서-주문상세, 게시글-댓글 등 생명주기 일치 시 | 대형 테이블 간 무분별 적용 시 대량 오삭제 발생 |
| **SET NULL** | 부모 데이터 삭제/수정 시 자식 외래키 값을 Null로 자동 갱신 | 회원 탈퇴 후 익명화된 주문 통계 보존 시 | 자식 컬럼이 `NOT NULL` 제약조건인 경우 사용 불가 |
| **SET DEFAULT** | 부모 데이터 삭제/수정 시 자식 외래키 값을 미리 정한 기본값으로 치환 | 관리자 계정 삭제 시 시스템 디폴트 관리자로 이관 | 디폴트 값에 해당하는 부모 레코드가 사전 존재해야 함 |

## Ⅳ. 선언적 제약(Declarative) vs 절차적 제약(Procedural)

> 선언적 제약을 원칙으로 하고, 복합 비즈니스 로직에 한해 절차적 제약으로 보완함.

| 비교 기준 | 선언적 제약 (Declarative Constraints) | 절차적 제약 (Procedural Constraints) |
|---|---|---|
| **구현 수단** | DDL 문법 (PRIMARY KEY, FOREIGN KEY, CHECK 등) | 데이터베이스 트리거(Trigger), 저장 프로시저(SP) |
| **검증 위치** | DBMS 커널 엔진 레벨에서 직접 고속 검증 | 트랜잭션 실행 시 프로시저/트리거 인터럽트 실행 |
| **성능 오버헤드** | 최소화 (인덱스 활용 및 최적화된 내부 C 루틴) | 트리거 컨텍스트 스위칭 및 추가 I/O 부하 유발 |
| **유지보수성** | 스키마 카탈로그에 명시되어 변경 추적 용이 | 복잡하게 얽힌 트리거는 디버깅 및 형상 관리가 극도로 난해 |
| **적용 영역** | 개체, 참조, 단순 값 범위 제약 (기본 원칙) | 두 개 이상 테이블 간 교차 집계 제약, 시계열 검증 |

## Ⅴ. 외래키(FK) 인덱스와 무결성 성능 최적화

> FK 컬럼에 인덱스가 없으면 부모 테이블 갱신 시 자식 테이블 전체에 락(Lock)이 걸려 병목이 발생함.

```text
[부모 테이블 변경] ──(FK 인덱스 부재 시)──> [자식 테이블 Full Table Scan & Table-level Lock!]
                                              ├── 동시 DML 세션 전체 대기 (트랜잭션 지연)
                                              └── 해결책: 자식 테이블 FK 컬럼에 B-Tree 인덱스 필수 생성!
```

1. **외래키 인덱스 필수화**: 부모 행 삭제/수정 시 자식 테이블의 참조 검사를 Full Table Scan 대신 인덱스 레인지 스캔으로 처리하여 락 경합 차단
2. **대량 배치 적재 시 제약조건 통제**: 수억 건의 초기 데이터 적재 시 제약조건을 임시 비활성화(`DISABLE NOVALIDATE`) 후, 적재 완료 후 일괄 검증(`ENABLE VALIDATE`) 전환

## Ⅵ. 데이터 무결성 제약 실무 위험 관리

> 고아 데이터와 참조 검사 병목을 선언 제약, 인덱스 설계, 복구 절차로 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| FK 인덱스 부재로 인한 테이블 락 경합 | 모든 외래키(FK) 컬럼에 B-Tree 인덱스 생성 의무화 | 부모 키 갱신 시 자식 테이블 락 대기 제거 및 조인 성능 향상 |
| CASCADE 남용으로 인한 대량 데이터 오삭제 | 원장성 테이블은 RESTRICT 강제 및 Soft Delete(논리 삭제) 전환 | 실수로 인한 대규모 연쇄 삭제 사고 원천 방지 |
| MSA 분산 DB 환경의 물리적 FK 부재 | 사가 패턴(Saga Pattern) 및 CDC 기반 최종 일관성 검증 파이프라인 | 서비스 독립성과 마이크로서비스 간 정합성 양립 |
| 배치 적재 지연으로 인한 DML 타임아웃 | 대량 적재 시 제약 임시 비활성화 후 `ENABLE VALIDATE` 일괄 검증 | 배치 시간 70% 단축 및 적재 후 100% 무결성 복원 |

## Ⅶ. 기술사적 제언: 애플리케이션 검증의 환상을 버려라

> "성능을 핑계로 DBMS의 무결성 제약을 풀고 애플리케이션으로 검증하겠다는 시도는, 언젠가 반드시 발생할 데이터 오염 사고의 시한폭탄을 설치하는 것과 같다."

### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 성능을 이유로 DBMS의 무결성 제약(PK/FK)을 모두 해제하고 '애플리케이션 코드로 검증하겠다'고 주장하는 개발팀이 종종 있음. 그러나 애플리케이션 버그, 배치 스크립트 직접 실행, 직접 SQL 수정 등의 우회 경로를 통해 고아 데이터가 유입되는 순간 RDBMS의 존재 가치는 완전히 소멸함.
- 나라면: 식별자와 참조 관계에는 선언적 제약을 우선하고, FK 인덱스는 DBMS·조회·부모 변경 패턴을 실측해 선택하며 대량 적재 후 기존 데이터까지 검증하겠음.

### 실전 답안용 기술사적 제언
- 판정: 데이터 무결성은 애플리케이션의 유효성 검증 로직에 위임할 수 없으며, **DBMS 선언적 제약조건으로 최종 방어선**을 구축해야 함
- 대안: 논리/물리 ERD 상의 모든 식별/참조 관계를 DDL 선언적 제약으로 100% 구현 $\rightarrow$ 모든 FK 컬럼 인덱스 생성 $\rightarrow$ MSA 환경은 Saga 보상 트랜잭션 수립
- 검증: DB 감사를 통한 고아 레코드(Orphan) 및 중복키 발생 건수 제로(0건) 유지
- 효과: 애플리케이션 오류 및 직접 DB 접근 수정으로 인한 데이터 오염 위험 완벽 차단

```text
[현행 한계] ─────────> [개선 방안] ─────────> [검증 기준] ─────────> [실행 효과]
애플리케이션 검증 의존 DBMS 선언적 제약 강제  고아 데이터 0건 달성    데이터베이스 무결성 사수
FK 락 경합 병목        FK B-Tree 인덱스 필수화 락 대기 시간 최소화    동시 트랜잭션 처리량 극대화
```

## 1교시 10점 답안 발췌

```text
1. 무결성 제약(Data Integrity Constraint)의 정의 및 목적
- 정의: 데이터의 정확성, 유효성, 일관성을 보증하기 위해 DML 연산 시 DBMS가 강제하는 불변 규칙
- 목적: 고아 데이터 및 중복 데이터 방지를 통한 데이터베이스 신뢰성 확보

2. 릴레이션 4대 무결성 제약 및 참조 조치
┌───────────────┬─────────────────────────────────────────────┐
│ 제약 종류     │ 핵심 규칙 및 DDL 문법                       │
├───────────────┼─────────────────────────────────────────────┤
│ 개체 무결성   │ PK 유일성 및 Not Null (PRIMARY KEY)         │
│ 참조 무결성   │ FK는 부모키이거나 Null (FOREIGN KEY)        │
│ 도메인 무결성 │ 정의된 데이터 타입, 범위 만족 (CHECK)       │
│ 키 무결성     │ 릴레이션 내 최소 1개 이상 후보키 존재 (UNIQUE)│
└───────────────┴─────────────────────────────────────────────┘
- 참조 조치 옵션: RESTRICT(거부), CASCADE(연쇄삭제), SET NULL, SET DEFAULT

3. 실무 제언: FK 컬럼 인덱스 필수화
- 외래키 컬럼에 인덱스를 생성하지 않으면 부모 변경 시 자식 테이블 락(Lock)이 발생하므로 반드시 B-Tree 인덱스를 설계해야 함.
```

## 출제 이력과 검증 출처

- **공식 출제 이력**: 정보관리기술사 제131회 1교시 단답형 (참조 무결성과 CASCADE 옵션), 제122회 2교시 논술형 (관계형 데이터 모델 무결성 제약조건과 외래키 인덱스 최적화)
- **표준 및 레퍼런스**: [PostgreSQL DDL Constraints Documentation](https://www.postgresql.org/docs/current/ddl-constraints.html), [Oracle Database SQL Language Reference (Constraints)](https://docs.oracle.com/en/database/oracle/oracle-database/)

## 학습 체크

- [ ] [Ⅰ 개요]: 데이터 무결성의 정의와 선언적/절차적 제약의 차이를 기술하였는가?
- [ ] [Ⅱ 제약]: 개체, 참조, 도메인, 키 무결성 4대 제약의 개념을 비교표로 정리하였는가?
- [ ] [Ⅲ 조치]: CASCADE, RESTRICT, SET NULL 참조 조치 옵션의 동작 원리를 설명하였는가?
- [ ] [Ⅴ 최적화]: FK 컬럼 인덱스 생성 필요성과 대량 배치 적재 시 제약 비활성화 전략을 기술하였는가?

## 연결 토픽

- [참조 무결성](./070_referential_integrity.md) · [키(Key)](./157_key.md) · [정규화](./019_normalization.md) · [z-검정](./012_z_test.md)
