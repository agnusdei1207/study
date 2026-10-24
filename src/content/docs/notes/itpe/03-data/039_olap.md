---
title: "OLAP(Online Analytical Processing)"
author: "agnusdei1207"
date: "2026-10-25T00:10:23+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- OLAP(Online Analytical Processing), OLTP(Online Transaction Processing), 데이터 웨어하우스(DW, Data Warehouse), 다차원 큐브(Cube)
- 롤업(Roll-up), 드릴다운(Drill-down), 슬라이싱(Slicing), 다이싱(Dicing), 피보팅(Pivoting), ROLAP(Relational OLAP), MOLAP(Multidimensional OLAP), HOLAP(Hybrid OLAP)

## Ⅰ. OLAP(Online Analytical Processing)의 개요

- 핵심 요약 : 다차원 구조의 데이터 웨어하우스에 대화식으로 접근해 다각도 분석을 지원하는 의사결정 지원 기술.
- 개념 : 최종 사용자인 경영진과 데이터 분석가가 다차원(Multidimensional) 구조로 구성된 **데이터 웨어하우스**(DW, Data Warehouse)에 접근하여 다양한 관점의 비즈니스 데이터를 대화식으로 분석하는 소프트웨어 기술(**OLAP**, Online Analytical Processing).
- 배경 및 필요성 : 단건 트랜잭션 중심의 OLTP(Online Transaction Processing) 시스템으로는 전략적 의사결정에 필요한 대규모 집계와 다차원 조회를 감당하기 어려움.
- 주요 목적 : 다차원 분석과 추세 파악을 통해 경영진과 분석가의 전략적 의사결정을 지원.

## Ⅱ. OLAP의 특징

- 핵심 요약 : 읽기 위주의 워크로드와 다차원 연산이 결합된 분석 전용 처리 구조.

1. 역정규화된 다차원 모델 : 스타 스키마(Star Schema)나 스노우플레이크 스키마(Snowflake Schema) 기반으로 데이터를 구성 → 분석 질의의 조인 구조가 단순해져 다차원 조회가 빨라짐.
2. 대규모 집계 질의 : 수백만 건 이상의 SUM, AVG 집계와 복합 조인을 처리 → 전사 단위 추세를 한 번의 질의로 파악.
3. 읽기 위주 워크로드 : 주기적인 일괄 배치 적재와 빈번한 조회를 전제로 설계 → 분석 질의의 응답성 확보.
4. 다차원 연산 : 큐브 대상의 요약, 세분화, 단면 추출, 하위 큐브 적출, 관점 회전을 지원 → 관점을 바꿔 가며 대화식으로 탐색.
5. 구현 유형 : 관계형 기반 **ROLAP**(Relational OLAP), 다차원 배열 기반 **MOLAP**(Multidimensional OLAP), 두 방식을 섞은 **HOLAP**(Hybrid OLAP)의 세 유형 → 용량과 응답 속도의 요구에 맞춰 선택.

## Ⅲ. OLAP의 구조 (흐름)

- 핵심 요약 : 운영 데이터가 ETL을 거쳐 데이터 웨어하우스에 적재된 뒤, OLAP 서버가 사전 집계 큐브로 대화식 질의를 처리하는 흐름.

```text
[ OLAP 아키텍처 흐름 ]
운영 시스템 (OLTP)
   ↓
ETL (Extract, Transform, Load)
   ↓ 주기적 적재
데이터 웨어하우스 (DW)
   ↓
OLAP 서버 (사전 집계 큐브)
   ↓
분석 도구 (대화식 다차원 질의)
```

- 다차원 큐브에서 **롤업**, **드릴다운**, **슬라이싱**, **다이싱**, **피보팅**의 다섯 연산을 사용하며, 각 연산의 동작은 다음 표와 같다.

| 연산 기법 | 동작 메커니즘 | 적용 사례 |
| :--- | :--- | :--- |
| 롤업 (Roll-up) | 세부 데이터를 상위 계층으로 집계하여 요약 (소분류 → 대분류) | 일별 매출을 월별, 연간 매출로 집계 |
| 드릴다운 (Drill-down) | 요약된 집계를 하위 계층으로 세분화하여 상세 조회 | 전국 매출을 시·도, 매장별 매출로 파고들기 |
| 슬라이싱 (Slicing) | 한 차원의 값을 고정해 2차원 단면을 추출 | 전체 큐브에서 2026년 데이터만 추출 |
| 다이싱 (Dicing) | 여러 차원의 조건으로 작은 하위 큐브(Sub-cube)를 추출 | 서울, 2026년 1분기, 스마트폰 품목만 추출 |
| 피보팅 (Pivoting) | 행과 열의 차원을 맞바꿔 관점을 재배치 | 행(지역)과 열(분기)을 행(분기)과 열(지역)로 회전 |

```text
[ 롤업과 드릴다운 ]
일별 매출 (가장 세부)
   ↓ 롤업 (상위 집계)
월별 매출
   ↓ 롤업
연간 매출
   ↑ 드릴다운 (하위 세분화)
```

## Ⅳ. OLTP와 OLAP, 구현 유형의 비교

- 핵심 요약 : 트랜잭션 처리(OLTP)와 분석 처리(OLAP)의 목적을 분리하고, 저장 구조에 따라 ROLAP, MOLAP, HOLAP을 고르는 것이 기준.

| 비교 항목 | OLTP (On-Line Transaction Processing) | OLAP (On-Line Analytical Processing) |
| :--- | :--- | :--- |
| 시스템 목적 | 일상적 비즈니스 트랜잭션의 정확하고 신속한 처리 | 전략적 의사결정을 위한 다차원 분석과 추세 파악 |
| 데이터 모델 | 정규화된 3NF(Third Normal Form) 모델, 중복 최소화 | 역정규화된 다차원 모델(스타·스노우플레이크 스키마) |
| 주요 질의 형태 | 소수 레코드 대상의 단건 INSERT, UPDATE, 키 기반 SELECT | 대규모 집계(SUM, AVG)와 복합 조인 |
| 트랜잭션 특성 | ACID(Atomicity, Consistency, Isolation, Durability) 보장과 동시성 제어 중시 | 읽기 위주, 주기적 일괄 배치 적재 |

| 비교 항목 | ROLAP (Relational OLAP) | MOLAP (Multidimensional OLAP) | HOLAP (Hybrid OLAP) |
| :--- | :--- | :--- | :--- |
| 데이터 저장소 | 관계형 데이터베이스 (RDBMS, Relational Database Management System) | 다차원 배열 큐브 (MDBMS, Multidimensional Database Management System) | 상세 데이터는 RDBMS, 집계는 다차원 데이터베이스(MDDB, Multidimensional Database) |
| 사전 집계 수준 | 질의 시점의 동적 계산 위주 | 적재 시점의 사전 집계 | 상위 집계만 사전 큐브화 |
| 쿼리 응답 속도 | 중간 (인덱스와 집계 테이블 튜닝에 의존) | 배열 기반 인덱싱으로 빠른 응답 | 집계는 빠르고 상세 조회는 보통 |
| 데이터 확장성 | 대용량 확장에 유리 | 큐브 폭발로 용량 한계 | 대용량과 고속 성능의 절충 |

## Ⅴ. OLAP의 한계와 방안

- 핵심 요약 : 다차원 신속 분석이라는 장점과 함께 큐브 폭발, 배치 지연, 조인 병목이라는 한계가 공존.
- 장점 : 다양한 관점의 대화식 분석으로 의사결정 품질을 높이고, 사전 집계 큐브로 대규모 데이터에서도 신속히 응답.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| 큐브 폭발 (Cube Explosion) | 차원과 계층이 늘면 사전 집계 조합이 급격히 늘어 저장 공간 고갈 | 자주 질의되는 상위 수준만 선별 집계하는 부분 사전 집계, 컬럼형 스토리지 기반 동적 질의 | 큐브 저장 용량, 집계 적중률 |
| 배치 적재 지연 | 야간 ETL 주기에 묶여 최신 트랜잭션이 분석 큐브에 즉시 반영되지 않음 | 람다(Lambda) 또는 카파(Kappa) 아키텍처, Apache Druid나 Apache Pinot 같은 실시간 OLAP 엔진 | 데이터 반영 지연 시간, 적재 주기 |
| 대규모 조인 병목 | 스타 스키마에서 팩트 테이블과 차원 테이블의 반복 조인이 DBMS(Database Management System)의 입출력 병목 유발 | 분산 MPP(Massively Parallel Processing) 쿼리 엔진(Trino, Snowflake) 채택, 인덱스와 파티션 설계 | 질의 응답 시간, 입출력 대기 시간 |

## Ⅵ. OLAP에 대한 기술사적 제언

- 핵심 요약 : 데이터 증가에 대응해 컬럼 지향 분산 엔진으로 수렴하고, 실시간 스트리밍 OLAP을 병행하는 방향.

1. 데이터 아키텍처 조직은 MOLAP 큐브의 배치 재생성 시간이 한계에 이르면 ClickHouse, DuckDB, Trino, Snowflake 같은 컬럼 지향 분산 엔진 기반의 ROLAP으로 전환을 검토해야 한다.
2. 데이터 플랫폼 조직은 의사결정 주기가 짧은 영역에 한해 Kafka 등 스트림 데이터를 Apache Druid나 Apache Pinot에 즉시 적재하여 실시간 다차원 분석을 제공해야 한다.

## Ⅶ. 결론

- 핵심 요약 : OLAP은 OLTP와 분리된 분석 전용 계층으로서 대규모 다차원 분석의 표준 역할을 하며, 실시간 엔진으로 진화하는 중.
- 시사점 : 큐브 폭발, 배치 지연, 조인 병목을 어떤 엔진으로 보완할지가 OLAP 아키텍처 선택의 핵심임.
