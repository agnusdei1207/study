---
title: "OLAP(Online Analytical Processing)"
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

- OLAP(Online Analytical Processing), OLTP(Online Transaction Processing), 데이터 웨어하우스(DW, Data Warehouse), 다차원 큐브(Cube)
- 롤업(Roll-up), 드릴다운(Drill-down), 슬라이싱(Slicing), 다이싱(Dicing), 피보팅(Pivoting), ROLAP(Relational OLAP), MOLAP(Multidimensional OLAP), HOLAP(Hybrid OLAP)

## Ⅰ. OLAP(Online Analytical Processing)의 개요

- 핵심 요약 : 다차원 구조의 데이터 웨어하우스에 대화식 접근하여 다각도 분석을 지원하는 의사결정 지원 기술.
- 개념 : 최종 사용자(경영진, 데이터 분석가)가 다차원(Multidimensional) 구조로 구성된 대규모 데이터 웨어하우스(DW, Data Warehouse)에 접근하여 대화식으로 신속하게 다양한 관점의 비즈니스 데이터 분석을 지원하는 소프트웨어 기술, OLAP(Online Analytical Processing).
- 배경 및 필요성 : 단건 트랜잭션 중심의 OLTP(Online Transaction Processing)로는 전략적 의사결정용 대규모 집계·다차원 조회의 충족 불가.
- 주요 목적 : 다차원 분석과 트렌드 파악을 통한 경영진·분석가의 전략적 의사결정 지원.

## Ⅱ. OLAP의 특징

- 핵심 요약 : 읽기 위주 워크로드와 5대 다차원 연산이 결합된 분석 전용 처리 구조.

1. 역정규화된 다차원 모델(스타/스노우플레이크 스키마) 기반의 데이터 구성.
2. 수백만 건 이상 대규모 집계(SUM, AVG) 및 복합 조인 질의 처리.
3. 읽기 위주(Read-Heavy) 워크로드와 주기적 일괄 배치 적재.
4. 다차원 큐브 대상 요약·세분화·단면 추출·하위 큐브 적출·관점 회전 등의 5대 다차원 연산 제공.
5. 관계형 기반 ROLAP(Relational OLAP), 다차원 배열 기반 MOLAP(Multidimensional OLAP), 하이브리드 HOLAP(Hybrid OLAP)의 3대 구현 유형.

## Ⅲ. OLAP의 구조 (흐름)

- 핵심 요약 : 다차원 큐브 연산 체계와 ETL(Extract, Transform, Load) 기반 적재 후 OLAP 서버 질의 처리의 흐름.
- 다차원 큐브(Cube) 기본 연산.

```text
[ OLAP 다차원 큐브(Cube) 기본 연산 ]
      [2026년 1분기 전국 노트북 매출 큐브]
                   |
     +-------------+-------------+
     | (드릴다운)                 | (롤업)
     v                           v
  [1월 서울 강남구 노트북 매출]    [2026년 연간 전사 총매출]
```

- 5대 다차원 연산 상세.

| 연산 기법 | 동작 메커니즘 | 구체적 적용 사례 |
| :--- | :--- | :--- |
| 롤업 (Roll-up) | 세부 데이터에서 상위 계층(차원)으로 집계 요약 (소분류 $\rightarrow$ 대분류) | 일별 매출 $\rightarrow$ 월별 매출 $\rightarrow$ 연간 매출 집계 |
| 드릴다운 (Drill-down) | 요약된 집계 데이터에서 하위 계층으로 세분화하여 상세 조회 | 전국 단위 매출 $\rightarrow$ 시/도 단위 $\rightarrow$ 매장별 매출 파고들기 |
| 슬라이싱 (Slicing) | 다차원 큐브의 한 차원을 특정 값으로 고정하여 2차원 단면 추출 | 전체 큐브 중 '2026년' 데이터만 잘라내어 분석 |
| 다이싱 (Dicing) | 여러 차원에서 특정 조건의 작은 하위 큐브(Sub-cube) 적출 | '서울' 지역 + '2026년 1분기' + '스마트폰' 품목만 추출 |
| 피보팅 (Pivoting) | 보고서의 행과 열의 차원을 서로 맞바꾸어 시각적 관점 재배치 | 행(지역), 열(분기) 테이블을 행(분기), 열(지역)로 회전 |

- 전사 아키텍처 흐름.

```text
[ OLAP 아키텍처 흐름 ]
[운영 시스템(OLTP)] --> [ETL(Extract, Transform, Load)] --> [데이터 웨어하우스(DW)]
                                                                  |
                                                                  v
                                          [OLAP 서버(사전 집계 큐브)] --> [분석 도구(대화식 다차원 질의)]
```

## Ⅳ. OLTP와 구현 유형의 비교

- 핵심 요약 : 트랜잭션 처리(OLTP)와 분석 처리(OLAP)의 목적 분리, 저장 구조에 따른 ROLAP·MOLAP·HOLAP의 선택 기준.
- OLTP(Online Transaction Processing)와 OLAP의 대조.

| 비교 항목 | OLTP (On-Line Transaction Processing) | OLAP (On-Line Analytical Processing) |
| :--- | :--- | :--- |
| 시스템 목적 | 일상적 비즈니스 트랜잭션의 정확하고 신속한 처리 | 전략적 의사결정을 위한 다차원 분석 및 트렌드 파악 |
| 데이터 모델 | 정규화된 3NF(Third Normal Form) 모델 (무결성 중심, 중복 최소화) | 역정규화된 다차원 모델 (스타/스노우플레이크 스키마) |
| 주요 쿼리 형태 | 소수 레코드 대상의 단건 INSERT, UPDATE, 키 기반 SELECT | 수백만 건 이상의 대규모 집계(SUM, AVG), 복합 조인 |
| 트랜잭션 격리 | 엄격한 ACID(Atomicity, Consistency, Isolation, Durability) 보장 (동시성 제어 중요) | 읽기 위주(Read-Heavy), 주기적 일괄 배치 적재 |

- 구현 유형별(ROLAP/MOLAP/HOLAP) 대조.

| 비교 항목 | ROLAP (Relational OLAP) | MOLAP (Multidimensional OLAP) | HOLAP (Hybrid OLAP) |
| :--- | :--- | :--- | :--- |
| 데이터 저장소 | 관계형 데이터베이스 (RDBMS, Relational Database Management System) | 전용 다차원 배열 큐브 (MDBMS, Multidimensional Database Management System) | 상세는 RDBMS, 집계는 MDDB(Multidimensional Database) |
| 사전 집계 수준 | 질의 시점의 동적 계산 위주 | 데이터 적재 시점의 사전 전면 집계 | 상위 집계만 사전 큐브화 |
| 쿼리 응답 속도 | 중간 (인덱스 및 집계 테이블 튜닝 의존) | 극도로 빠름 ($O(1)$ 배열 인덱싱) | 집계는 빠르고 상세는 보통 |
| 데이터 확장성 | 테라~페타바이트급 무제한 확장 | 큐브 폭발(Cube Explosion)로 용량 한계 | 대용량과 고속 성능의 절충 |

## Ⅴ. OLAP의 장점과 한계

- 핵심 요약 : 다차원 신속 분석의 장점과 큐브 폭발·배치 지연·JOIN 병목의 한계 공존.
- 장점
  1. 다양한 관점의 대화식 다차원 분석을 통한 의사결정 품질 향상.
  2. 사전 집계 큐브 기반 대규모 데이터의 신속한 응답.
- 한계점 1 : 다차원 큐브(Cube) 생성 시 데이터 폭발(Data Explosion) 및 스토리지 고갈
  - 한계점 : MOLAP 환경에서 차원(Dimension)과 계층(Hierarchy) 증가에 따른 사전 집계 큐브의 희소 행렬(Sparsity) 기인 저장 공간 기하급수적 폭증.
  - 해결 방안 : 자주 질의되는 상위 레벨만 선별 집계하는 부분 사전 집계(Partial Pre-aggregation) 적용, 컬럼나 스토리지(ClickHouse, DuckDB) 기반의 동적 질의 처리.
- 한계점 2 : 배치 적재 지연으로 인한 실시간 분석(Real-time Analytics) 불가
  - 한계점 : 야간 ETL 배치 주기 의존에 따른 최신 수 분~수 초 내 트랜잭션 데이터의 즉시 분석 큐브 반영 불가 시차 발생.
  - 해결 방안 : 람다/카파 아키텍처 도입, 실시간 OLAP 엔진(Apache Pinot, Apache Druid)을 통한 스트리밍 인입 동시 다차원 슬라이스/다이스 질의 제공.
- 한계점 3 : 복잡한 비정형 질의 시 ROLAP 엔진의 RDBMS 성능 저하
  - 한계점 : 스타 스키마 기반 질의 시 수억 건 팩트 테이블과 다차원 차원 테이블 간 반복적 대규모 JOIN에 따른 DBMS(Database Management System) I/O 병목 유발.
  - 해결 방안 : 대화형 분석 전용 MPP(Massively Parallel Processing) 분산 쿼리 엔진(Trino, Snowflake) 채택, Z-Order 인덱싱 및 프로젝션 캐시 구축.

## Ⅵ. OLAP에 대한 기술사적 제언

- 핵심 요약 : 분산 컬럼 지향 엔진으로의 수렴과 실시간 스트리밍 OLAP 체계 구축.
- 컬럼형 스토리지와 분산 쿼리 엔진으로의 수렴 : 데이터 증가에 따른 MOLAP 큐브 배치 시간 한계 극복, ClickHouse, DuckDB, Trino, Snowflake와 같은 분산 컬럼 지향 DBMS 기반 ROLAP으로의 진화.
- 실시간 스트리밍 OLAP 도입 : 사후 일괄 배치 분석 탈피, Apache Pinot, Apache Druid를 활용한 Kafka 스트림 데이터 인입 즉시 수초 이내 실시간 다차원 OLAP 분석 체계 구축.

## Ⅶ. 결론

- 핵심 요약 : OLAP은 대규모 다차원 분석의 표준이며 클라우드 네이티브 실시간 엔진으로 진화 중.
- 요약 : OLTP와의 목적 분리를 바탕으로 다차원 큐브 연산으로 전략적 의사결정을 지원하는 분석 전용 계층.
- 시사점 : 큐브 폭발·배치 지연·JOIN 병목을 컬럼형 분산 엔진과 스트리밍 OLAP으로 보완하는 아키텍처 선택 필요.
