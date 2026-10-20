---
title: "무결성 제약"
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

- 무결성 제약(Integrity Constraint), 개체 무결성(Entity Integrity), 참조 무결성(Referential Integrity), 도메인 무결성(Domain Integrity), 사용자 정의 무결성(User-Defined Integrity)
- 기본키(PK, Primary Key), 외래키(FK, Foreign Key), 고아 레코드(Orphan Record), RESTRICT, CASCADE, SET NULL, SET DEFAULT, Saga 패턴

## Ⅰ. 무결성 제약의 개요

- 핵심 요약 : 데이터의 정확성·일관성·유효성을 보장하기 위해 데이터 변경 시 강제되는 규칙과 조건의 총체.
- 개념 : 데이터베이스에 저장된 데이터의 정확성(Accuracy), 일관성(Consistency), 유효성(Validity)을 보장하기 위해 삽입(Insert), 수정(Update), 삭제(Delete) 시 준수되어야 하는 규칙과 조건의 총체, 무결성 제약(Integrity Constraint).
- 배경 및 필요성 : 권한 없는 사용자나 비정상적 트랜잭션 오류로 인한 데이터베이스의 왜곡·모순 상태 전이 방지, 외래키 단절에 따른 고아 레코드(Orphan Record) 생성 억제 필요.
- 주요 목적 : 비즈니스 룰의 데이터 모델 계층 강제를 통한 애플리케이션 버그 방어선 구축 및 데이터 신뢰성 확보.

## Ⅱ. 무결성 제약의 특징

- 핵심 요약 : 개체·참조·도메인·사용자 정의 4대 무결성과 참조 옵션 기반의 데이터 품질 방어 체계.

1. 개체 무결성(Entity Integrity) : 기본키(Primary Key) 구성 속성의 널(NULL) 값 불가 및 중복 불가(유일성 만족).
2. 참조 무결성(Referential Integrity) : 외래키(Foreign Key) 값은 참조 릴레이션의 기본키 값 또는 NULL.
3. 도메인 무결성(Domain Integrity) : 속성값의 사전 정의된 데이터 타입, 길이, 허용 범위(CHECK) 준수.
4. 사용자 정의 무결성(User-Defined Integrity) : 업무 특성상 요구되는 복합 비즈니스 규칙(TRIGGER, ASSERTION 등) 준수.
5. 참조 무결성 유지 옵션 (부모 레코드 삭제·수정 시).
   1. RESTRICT / NO ACTION : 자식 테이블 참조 중인 경우 부모 레코드 삭제·수정 거부.
   2. CASCADE : 부모 레코드 삭제·수정 시 참조 자식 레코드의 연쇄 삭제·수정.
   3. SET NULL : 부모 레코드 삭제 시 자식 외래키 컬럼 값의 NULL 자동 변경.
   4. SET DEFAULT : 부모 레코드 삭제 시 자식 외래키 컬럼 값의 사전 정의 기본값 변경.

## Ⅲ. 무결성 제약의 구조 (흐름)

- 핵심 요약 : DML 처리 경로상의 제약 검증과 위반 시 롤백, DB 계층과 애플리케이션 계층의 이원화 구조.

```text
[ 무결성 제약 검증 흐름 ]
DML 요청 (INSERT / UPDATE / DELETE)
        ↓
제약조건 검사 (PK / FK / CHECK / TRIGGER)
        ↓              ↓
      통과           위반
        ↓              ↓
     COMMIT     에러 반환 및 ROLLBACK
```

- 구현 계층 이원화 구조.

```text
[ 무결성 구현 계층 ]
(A) DB 계층 강제 (FK, CHECK, TRIGGER)
     - 선언적 무결성 강제 적용, 쓰기 오버헤드, 샤딩 곤란
(B) 앱 계층 강제 (ORM, 서비스 로직)
     - DB 부하 분산, 유연한 수평 확장, 앱 버그 시 데이터 오염 위험
```

- DB(Database) 계층은 선언적 제약의 강제 적용 담당, 애플리케이션 계층은 ORM(Object-Relational Mapping) 및 서비스 로직 기반 유효성 검증 분담.

## Ⅳ. 무결성 유형 및 구현 계층의 비교

- 핵심 요약 : 4대 무결성의 규칙·구현 기법·위반 동작 차이와 DB 계층 대비 애플리케이션 계층의 트레이드오프.
- 4대 무결성 제약조건 상세 비교.

| 무결성 종류 | 핵심 규칙 및 정의 | 데이터베이스 구현 기법 | 위반 시 DBMS(Database Management System) 동작 |
|---|---|---|---|
| 개체 무결성 (Entity Integrity) | 기본키(Primary Key)를 구성하는 어떤 속성도 널(NULL) 불가, 중복 불가 | `PRIMARY KEY` 제약조건 선언 (내부적으로 Unique B-Tree 인덱스 생성) | ORA-00001 (Unique constraint violated), Not Null 위반 에러 발생 후 롤백 |
| 참조 무결성 (Referential Integrity) | 외래키(Foreign Key) 값은 참조 릴레이션의 기본키 값과 일치하거나 널(NULL) | `FOREIGN KEY` 제약조건 선언 (`REFERENCES parent(pk)`) | 자식에 없는 부모값 삽입 차단, 자식이 참조 중인 부모 삭제 차단 |
| 도메인 무결성 (Domain Integrity) | 속성에 입력되는 모든 값의 정의된 도메인(원자값) 범위 만족 | 데이터 타입(VARCHAR, INT), `NOT NULL`, `CHECK` 제약조건 | 범위 이탈 값 입력 시 타입 불일치 또는 Check 제약조건 위반 에러 |
| 사용자 정의 무결성 (User-Defined) | 개체·참조·도메인 제약 외 업무 특성상 요구되는 복합 비즈니스 규칙 준수 | 데이터베이스 트리거(`TRIGGER`), 트랜잭션 로직, 애플리케이션 검증 | 비즈니스 예외 발생 후 트랜잭션 강제 Abort |

- 무결성 강제 계층별 비교.

| 비교 항목 | 데이터베이스 계층 (FK, PK, Check) | 애플리케이션 계층 (Spring, Django, ORM) |
|---|---|---|
| 정합성 보장성 | 100% 보장 (어떤 경로로 직접 SQL(Structured Query Language)을 실행해도 무결성 유지) | 다중 애플리케이션·직접 쿼리 수행 시 정합성 파괴 가능 |
| 성능 및 쓰기 지연 | 외래키 검증용 부모 테이블 추가 읽기 I/O 발생 | 락킹 및 I/O 최소화를 통한 대규모 고성능 쓰기 지원 |
| 분산 환경 지원 | 분산 DB 및 샤딩 환경에서 테이블 간 FK 제약 불가 | 서비스 경계를 넘는 정합성의 Saga 패턴 기반 유연 제어 |

## Ⅴ. 무결성 제약의 장점과 한계

- 핵심 요약 : 데이터 품질 방어선·고아 레코드 억제의 장점, 쓰기 성능·분산 환경·트리거 남용의 한계.
- 장점
  1. 애플리케이션 버그·우회 경로와 무관한 데이터 품질 방어선 확보.
  2. 외래키 단절 억제를 통한 데이터 신뢰성 및 일관성 유지.
  3. 비즈니스 룰의 데이터 모델 계층 내재화를 통한 일관된 품질 관리.
- 한계점 1 : DBMS 제약조건(FK, Check) 적용에 따른 대용량 쓰기 성능 저하
  - 한계점 : 대규모 INSERT/UPDATE 배치 시 매 건마다 부모 테이블 B+Tree 인덱스 탐색 및 락 획득으로 인한 I/O 병목 및 초당 트랜잭션 수(TPS, Transactions Per Second) 급감.
  - 해결 방안 : 대량 데이터 로더(Bulk Loader) 작업 시 제약조건 일시 비활성화(Disable Novalidate) 후 작업 완료 시점의 병렬 활성화, 애플리케이션 계층 유효성 검증 분담.
- 한계점 2 : 마이크로서비스(MSA, Microservice Architecture) 및 분산 DB 환경에서의 외래키 무결성 붕괴
  - 한계점 : 서비스별 DB 분리(Database per Service) 아키텍처에서 물리적 외래키 제약 설정 불가로 서비스 간 참조 무결성 단절 발생.
  - 해결 방안 : 사가(Saga) 패턴 기반 오케스트레이션 적용, 비동기 CDC(Change Data Capture, Debezium)와 Outbox 패턴 활용 최종적 참조 무결성(Eventual Referential Integrity) 보장.
- 한계점 3 : 복잡한 업무 규칙 표현의 한계 및 트리거 남용 시 디버깅 난제
  - 한계점 : 기본 SQL 제약(PK, FK, Check)만으로 다중 행·테이블 간 복합 검증이 어려워 트리거 남용 시 연쇄 동작의 사이드 이펙트 추적 불가.
  - 해결 방안 : 복합 도메인 무결성의 도메인 주도 설계(DDD, Domain-Driven Design) 애그리게잇(Aggregate) 루트 내부 캡슐화, 데이터베이스의 기본 제약 집중.

## Ⅵ. 무결성 제약에 대한 기술사적 제언

- 핵심 요약 : 대용량 쓰기 시스템의 외래키 완화 전략과 마이그레이션 시 제약조건 비활성화·복원 절차 표준화.
- 대용량 트랜잭션 시스템의 외래키 완화 전략 : 초당 수만 건 쓰기가 발생하는 커머스 주문·로그 시스템에서는 물리적 외래키 제약의 의도적 제거 및 인덱스만 유지, 애플리케이션 트랜잭션과 비동기 정합성 배치 검증 체계의 이원화 권장.
- 데이터 마이그레이션 시 제약조건 일시 비활성화 : 수천만 건 초기 적재 시 `DISABLE NOVALIDATE` 옵션과 고속 로드(Direct Path Insert) 적용, 적재 완료 시점의 병렬 검증(`ENABLE NOVALIDATE`) 복원을 통한 작업 시간 단축 권장.

## Ⅶ. 결론

- 핵심 요약 : 무결성 제약은 데이터 품질의 최후 방어선이나, 성능·분산 환경·복합 규칙 조건에 따른 선택적 적용이 필요한 개념.
- 요약 : 4대 무결성과 참조 옵션을 통해 삽입·수정·삭제 전 과정의 데이터 정확성·일관성·유효성 보장.
- 시사점 : 구현 계층 이원화, Saga·CDC 기반 최종 무결성 보장, 제약조건 비활성화 절차 표준화를 통한 확장성과 품질의 균형 확보 필요.
