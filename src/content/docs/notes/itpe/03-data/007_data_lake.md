---
title: "데이터 레이크"
author: "agnusdei1207"
date: "2026-10-25T00:09:44+09:00"
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

- 데이터 레이크(Data Lake), Schema-on-Read, ELT, 메달리온(Medallion) 아키텍처, 데이터 스웜프(Data Swamp)
- 오픈 테이블 포맷(Open Table Format), ACID, 레이크하우스(Lakehouse), FinOps

## Ⅰ. 데이터 레이크의 개요

- 핵심 요약 : 정형·반정형·비정형 원천 데이터를 원본 포맷 그대로 저장하는 중앙 집중식 대용량 저장소.
- 개념 : 정형 데이터(RDBMS(Relational Database Management System) 테이블), 반정형 데이터(JSON(JavaScript Object Notation)·XML(Extensible Markup Language)·로그), 비정형 데이터(이미지·영상·텍스트)를 변환 없이 원래 포맷 그대로 저렴한 객체 스토리지에 모아 두는 중앙 집중식 저장소인 **데이터 레이크** (Data Lake).
- 배경 및 필요성 :
  1. 데이터 웨어하우스(DW, Data Warehouse)는 정형 중심이고 저장 비용이 높아 원본 보관에 한계가 있음.
  2. 데이터 과학자의 탐색적 데이터 분석(EDA, Exploratory Data Analysis)과 머신러닝 파이프라인이 원본 데이터를 요구함.
  3. 저장 시점에 스키마를 강제하지 않는 유연한 적재가 필요함.
- 주요 목적 : **Schema-on-Read** (읽는 시점에 스키마를 적용하는 방식) 기반의 저비용 대용량 통합 저장 기반을 구축.

## Ⅱ. 데이터 레이크의 특징 및 장점

- 핵심 요약 : 원본 선적재, 읽기 시점 스키마 적용, 오픈 포맷 기반의 유연한 저장 구조.

1. Schema-on-Read : 저장 시점의 스키마 강제 없이 읽는 시점에 스키마를 적용 → 적재 속도와 탐색 유연성 확보.
2. 선적재 **ELT** (Extract, Load, Transform) : 추출한 데이터를 원천 그대로 적재하고 분석 시점에 변환 → 원본 재가공의 자유도 확보.
3. 원본(Raw) 보존 : 전 유형 데이터를 원래 포맷으로 저장 → 재처리와 감사 추적 가능.
4. 경제성 : 저렴한 대용량 객체 스토리지 기반의 확장형 구조 → 대용량 보관 비용 절감.
5. 오픈 테이블 포맷 지원 : Apache Iceberg, Delta Lake, Apache Hudi가 **ACID** (Atomicity, Consistency, Isolation, Durability) 트랜잭션, 타임 트래블, 스키마 진화를 파일 위에 구현 → 레이크의 신뢰성 보완.

## Ⅲ. 데이터 레이크의 구조 (흐름)

- 핵심 요약 : Bronze-Silver-Gold 3단계 **메달리온 아키텍처** (Medallion Architecture)를 따라 원본에서 서빙 데이터로 품질을 단계적으로 높이는 구조.

```text
[ 메달리온 아키텍처 ]

 Bronze (Raw): 원천 원본, 감사·리니지
          ↓
 Silver (Cleansed): 결측 정제, 표준화
          ↓
 Gold (Curated): 비즈니스 집계·서빙
```

| 계층 | 데이터 성격 | 처리 작업 및 스토리지 포맷 | 주요 사용자 |
|---|---|---|---|
| Bronze(Raw Zone) | 외부 원천에서 수집된 비정제 원본 | 추가 전용(Append-only) 적재, JSON·CSV·Parquet 원본 | 데이터 엔지니어 |
| Silver(Refined Zone) | 중복 제거, 결측 보정, 스키마 유효성 검증 완료 | Parquet 압축, 파티셔닝, 정제된 테이블 | 데이터 엔지니어, 데이터 과학자 |
| Gold(Curated Zone) | 도메인별 비즈니스 로직과 집계 규칙 반영 | 차원 모델링(Fact/Dimension), 고속 서빙 뷰 | BI(Business Intelligence) 분석가, 임원 |

- 핵심 기술 스택 :
  1. 스토리지 계층 : AWS S3(Simple Storage Service), Google Cloud Storage, Azure ADLS(Data Lake Storage) Gen2, Apache Ozone.
  2. 연산·처리 엔진 : Apache Spark, Trino, Flink, DuckDB.
  3. 오픈 테이블 포맷 : Apache Iceberg, Delta Lake, Apache Hudi.

## Ⅳ. 데이터 웨어하우스·데이터 레이크·레이크하우스의 비교

- 핵심 요약 : 쓰기 시점에 스키마를 적용하는 DW, 읽기 시점에 적용하는 데이터 레이크, 두 방식을 결합한 **레이크하우스** (Lakehouse)로 구분.

| 비교 항목 | DW(Data Warehouse) | 데이터 레이크 | 레이크하우스(Lakehouse) |
|---|---|---|---|
| 스키마 적용 시점 | Schema-on-Write | Schema-on-Read | Schema-on-Read와 테이블 포맷의 스키마 강제 |
| 적재 방식 | 정제·변환 후 적재(ETL) | 원본 선적재(ELT) | ELT 기반과 ACID 트랜잭션 |
| 데이터 유형 | 고품질 정형 데이터 | 정형·반정형·비정형 전체 | 전체 유형과 큐레이션 계층 |
| 주요 활용 | 빠른 SQL 분석 | 탐색적 분석, 머신러닝 | 단일 플랫폼 통합 분석·서빙 |
| 강점 | 신뢰성, 분석 성능 | 유연성, 경제성 | ACID 신뢰성과 레이크 경제성의 결합 |

- 선택 기준 : 엄격한 무결성과 표준 리포팅은 DW, 원본 보존·탐색·머신러닝은 데이터 레이크, 단일 플랫폼 통합은 레이크하우스가 적합.

## Ⅴ. 데이터 레이크의 한계와 방안

- 핵심 요약 : 거버넌스 부재에 따른 스웜프 변질, 소형 파일, ACID 부재, 비용 증가를 거버넌스 자동화와 테이블 포맷, FinOps로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| **데이터 스웜프** (Data Swamp) 변질 | 무분별한 적재, 메타데이터 부재, 접근 통제 실패로 위치와 정합성을 잃음 | 적재 파이프라인에서 자동 메타데이터 등록(AWS Glue, Apache Atlas), ILM 기반 아카이브·폐기, Silver 승격 시 유효성 검증 의무화 | 카탈로그 등록률, 미사용 데이터 비율 |
| **소형 파일 문제** (Small File Problem) | 실시간 인입으로 작은 파티션 파일이 대량 생성되어 메타스토어와 스캔 성능 저하 | 파일 압축(Compaction) 자동화, Apache Iceberg·Delta Lake의 자동 파일 병합 | 파일당 평균 크기, 쿼리 응답 시간 |
| 멀티 라이터 환경의 ACID 부재 | 동시 쓰기 충돌과 부분 실패로 불완전 파일이 잔류 | 트랜잭션 로그(WAL, Write-Ahead Logging) 기반 스냅샷 격리의 오픈 테이블 포맷 도입, 타임 트래블 구현 | 쓰기 충돌 건수, 복구 소요 시간 |
| 스토리지 비용 급증 | 보관 주기 없는 영구 보관으로 청구 비용 증가와 콜드 데이터 방치 | 수명주기 규칙에 따른 계층 이동, Parquet·ORC 컬럼 포맷과 압축 표준화 | 테라바이트당 비용, 콜드 데이터 비율 |

```text
[ 데이터 스웜프 변질 경로 ]

 무분별한 적재 (거버넌스 부재)
 + 메타데이터 부재
 + 접근 권한 통제 실패
          ↓
 데이터 위치·정합성 상실, 사용 불가
```

## Ⅵ. 데이터 레이크 발전 방향에 대한 기술사적 제언

- 핵심 요약 : 레이크하우스로의 수렴, 행·열 수준 접근 통제, 상시 비용 최적화.
- DW의 신뢰성과 레이크의 유연성·경제성을 함께 갖춘 레이크하우스 구조로 수렴하는 방향이 현실적임.
- 객체 단위 접근 통제를 넘어 행·열 수준과 태그 기반 정책 접근 제어(PBAC, Policy-Based Access Control) 체계를 세워 컴플라이언스 위험을 사전에 차단하는 것이 필요함.
- 컬럼 기반 포맷 변환과 정렬 기반 인덱싱으로 쿼리 스캔량을 줄이는 정책을 상시 운영하는 FinOps 활동을 설계 단계부터 포함하는 것이 바람직함.

## Ⅶ. 결론

- 핵심 요약 : 데이터 레이크는 Schema-on-Read 기반의 경제적 저장소이며, 거버넌스·포맷·비용 관리가 성공 조건인 체계.
- 시사점 : 데이터 스웜프를 막는 거버넌스와 레이크하우스·FinOps 중심의 진화 전략을 함께 설계해야 함.
