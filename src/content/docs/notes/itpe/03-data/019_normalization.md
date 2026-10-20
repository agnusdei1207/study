---
title: "정규화"
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

- 정규화(Normalization), 함수적 종속성(FD, Functional Dependency), 이상 현상(Anomaly), 데이터 중복(Data Redundancy), 무손실 분해(Lossless Decomposition)
- 제1정규형(1NF), 제2정규형(2NF), 제3정규형(3NF), BCNF(Boyce-Codd Normal Form), 종속성 보존(Dependency Preservation), 반정규화

## Ⅰ. 정규화의 개요

- 핵심 요약 : 중복 최소화와 함수적 종속성 기반 분해를 통해 이상 현상을 원천 방지하는 데이터베이스 설계 프로세스.
- 개념 : 관계형 데이터베이스 설계에서 중복 데이터(Data Redundancy)를 최소화하고 함수적 종속성(FD)을 기반으로 테이블을 논리적으로 분해하여 데이터 이상 현상(Anomaly)을 원천 방지하는 프로세스, 정규화(Normalization).
- 배경 및 필요성 : 에드가 F. 커드(E.F. Codd)가 제안한 이론 체계, 비정규화 테이블의 중복과 종속 문제로 인한 데이터 품질 저하 방지 필요.
- 주요 목적 : 무손실 분해(Lossless Decomposition)와 종속성 보존(Dependency Preservation)을 지향하는 논리적 데이터 모델 품질 확보.

## Ⅱ. 정규화의 특징

- 핵심 요약 : 중복 제거, 종속성 기반 단계적 분해, 3대 이상 현상 방지, 단계별 정규형 체계.

1. 중복 데이터 최소화를 통한 저장 공간 절감 및 일관성 확보.
2. 함수적 종속성(FD) 기반의 논리적 테이블 분해.
3. 무손실 분해(Lossless Decomposition)와 종속성 보존(Dependency Preservation) 지향.
4. 삽입·삭제·수정 3대 이상 현상(Anomaly)의 원천 방지.
5. 1NF부터 BCNF, 4NF, 5NF까지의 단계적 정규형 체계.

## Ⅲ. 정규화의 구조 (흐름)

- 핵심 요약 : 비정규 릴레이션에서 BCNF까지의 단계적 분해 흐름과 이상 현상 제거 구조.

```text
[ 정규화 단계 요약 ]
[비정규 릴레이션]
       |
       v  (원자값이 아닌 도메인 분해)
    [ 제1정규형 (1NF) ] : 모든 속성은 원자값(Atomic Value)
       |
       v  (부분 함수 종속성 제거)
    [ 제2정규형 (2NF) ] : 기본키의 진부분집합에 종속되는 속성 분리 (완전 함수 종속)
       |
       v  (이행적 함수 종속성 제거: X -> Y, Y -> Z)
    [ 제3정규형 (3NF) ] : 기본키가 아닌 일반 속성에 종속되는 속성 분리
       |
       v  (비사소한 함수 종속의 결정자가 슈퍼키인지 확인)
    [ BCNF (보이스-코드) ] : 모든 비사소한 함수 종속 X -> Y에서 X는 슈퍼키(Superkey)
```

- 비정규화 테이블의 3대 이상 현상.

```text
[ 3대 이상 현상 (Anomaly) ]
1. 삽입 이상 (Insertion) : 새 데이터 등록 시 불필요한 속성값(NULL 불가)까지 강제 입력
2. 삭제 이상 (Deletion)  : 특정 레코드 삭제 시 의도하지 않은 유용한 정보의 연쇄 삭제
3. 수정 이상 (Update)    : 중복 데이터 중 일부만 수정되어 릴레이션 내 불일치(모순) 발생
```

- 고차 정규형 : 제4정규형(4NF, Fourth Normal Form)은 비사소한 다치 종속성(MVD, Multivalued Dependency $X \twoheadrightarrow Y$) 제거, 제5정규형(5NF, Fifth Normal Form; PJNF, Projection-Join Normal Form)은 무손실 조인 종속성(JD, Join Dependency) 제거.
- 무손실 조인 분해 조건 : 릴레이션 $R$을 $R_1, R_2$로 분해 시 $R_1 \bowtie R_2 = R$ 만족, 수학적 판정 조건은 $(R_1 \cap R_2 \rightarrow R_1)$ 또는 $(R_1 \cap R_2 \rightarrow R_2)$ 중 적어도 하나 성립(공통 속성이 어느 한쪽의 슈퍼키).
- 종속성 보존(Dependency Preservation) : 분해된 릴레이션들의 함수 종속성 집합 합집합이 원래 종속성 집합을 모두 커버, BCNF는 종속성 보존 실패 가능으로 실무에서 3NF 절충 선택 사례 다수.

## Ⅳ. 정규형 단계별 비교

- 핵심 요약 : 정규형별 위반 조건, 변환 규칙, 해결되는 이상 현상의 차이.

| 정규형 | 위반 조건 및 문제 구조 | 변환 규칙 및 조치 | 해결되는 이상 현상 |
|---|---|---|---|
| 제1정규형 (1NF, First Normal Form) | 컬럼이 다중값(Repeating Group) 또는 복합값 보유 | 반복 그룹 분리, 모든 도메인의 단일 원자값 재구성 | 다중값으로 인한 검색·조작 불가 해결 |
| 제2정규형 (2NF, Second Normal Form) | 복합 기본키(PK, Primary Key)의 일부분에 종속되는 속성 존재 (부분 함수 종속) | 부분 종속 컬럼들의 별도 릴레이션 분리 (완전 함수 종속화) | 복합키 일부만 알 때의 삽입·삭제 이상 |
| 제3정규형 (3NF, Third Normal Form) | 기본키가 아닌 일반 속성에 다른 일반 속성 종속 ($X \rightarrow Y, Y \rightarrow Z$) | 이행 종속 속성($Y \rightarrow Z$)의 별도 릴레이션 분리 | 일반 속성 갱신 시 발생하는 수정 이상 |
| BCNF (Boyce-Codd Normal Form) | 비사소한 함수 종속의 결정자가 슈퍼키가 아님 | 슈퍼키가 아닌 결정자 포함 종속 관계의 무손실 분해 | 다수 후보키 중첩 시 발생하는 잔여 이상 |

## Ⅴ. 정규화의 장점과 한계

- 핵심 요약 : 이상 현상 방지·무결성 확보의 장점, 다중 조인 부하·종속성 보존 실패·모델 경직성의 한계.
- 장점
  1. 삽입·삭제·수정 이상 현상의 원천 방지.
  2. 중복 제거를 통한 데이터 일관성 및 저장 효율 확보.
  3. 명확한 종속성 구조를 통한 스키마 확장성 향상.
- 한계점 1 : 과도한 테이블 분해로 인한 다중 JOIN 부하 및 조회 성능 저하
  - 한계점 : 3NF 또는 BCNF까지의 엄격 정규화 시 단순 업무 조회에도 5~10개 이상 다중 JOIN 유발, 인덱스 스캔·메모리 소트 오버헤드로 TPS(Transactions Per Second) 급락.
  - 해결 방안 : 워크로드 분석 기반 조회 빈도가 극도로 높은 핵심 트랜잭션의 선별적 반정규화(중복 컬럼, 집계 테이블) 적용 및 읽기 캐시(Redis) 계층화.
- 한계점 2 : 고차 정규화(BCNF, 4NF) 과정에서의 함수적 종속성 보존 실패
  - 한계점 : BCNF 분해 시 기존 함수 종속성 전체의 보존 실패, INSERT/UPDATE 시 관계 간 무결성 검증용 무거운 외래키 JOIN 필요.
  - 해결 방안 : 종속성 보존 필수 도메인에서 무리한 BCNF 분해 대신 3NF 수준 절충(Trade-off) 및 애플리케이션 트랜잭션 로직 보완.
- 한계점 3 : 동적 스키마 변경 및 애자일 개발 환경에서의 모델 경직성
  - 한계점 : 엄격한 참조 관계·제약조건으로 인해 비즈니스 요구사항 변경 시 다수 테이블 DDL(Data Definition Language) 수정 및 마이그레이션 다운타임 유발.
  - 해결 방안 : 반정형 속성의 JSON(JavaScript Object Notation)/JSONB 하이브리드 컬럼 타입 선별 적용, 유연한 NoSQL(Not Only SQL)/도큐먼트 저장소 혼용 Polyglot Persistence 구축.

## Ⅵ. 정규화에 대한 기술사적 제언

- 핵심 요약 : OLTP와 OLAP 워크로드별 모델링 전략 차별화와 3NF 표준 기반 선별적 반정규화.
- OLTP(Online Transaction Processing) vs OLAP(Online Analytical Processing) 전략 차별화 : 트랜잭션 정합성 중심 OLTP 시스템의 BCNF/3NF까지 엄격 정규화, 대규모 읽기·다차원 분석 목적 OLAP/DW(Data Warehouse) 환경의 스타 스키마 형태 의도적 역정규화 설계 필요.
- 과도한 정규화에 따른 성능 저하 예방 : 정규화 레벨 상승에 따른 조인(JOIN) 횟수·I/O 오버헤드 증가 감안, 실무 표준은 3NF로 삼고 병목 쿼리가 입증된 테이블에 한한 선별적 반정규화 적용 권장.

## Ⅶ. 결론

- 핵심 요약 : 정규화는 데이터 품질과 무결성의 이론적 기반이나, 성능과의 균형 판단이 수반되어야 하는 설계 원칙.
- 요약 : 함수적 종속성 기반 단계적 분해와 무손실 분해·종속성 보존 원칙을 통한 이상 현상 제거.
- 시사점 : 3NF 표준 유지, 워크로드 기반 선별적 반정규화, Polyglot Persistence 보완을 통한 품질과 성능의 균형 설계 필요.
