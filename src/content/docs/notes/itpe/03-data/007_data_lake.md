---
title: "데이터 레이크"
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

- 데이터 레이크(Data Lake), Schema-on-Read, ELT, 메달리온(Medallion) 아키텍처, 데이터 스웜프(Data Swamp)
- 오픈 테이블 포맷(Open Table Format), ACID, 레이크하우스(Lakehouse), FinOps

## Ⅰ. 데이터 레이크의 개요

- 핵심 요약 : 정형·반정형·비정형 원천 데이터를 원본 포맷 그대로 저장하는 중앙 집중식 대용량 저장소.
- 개념 : 정형은 RDBMS(Relational Database Management System) 테이블, 반정형은 JSON(JavaScript Object Notation)·XML(Extensible Markup Language)·로그, 비정형은 이미지·영상·텍스트 등을 포함한 대규모 원천 데이터를 변환 없이 원래 포맷 그대로(Raw Format) 저렴한 대용량 객체 스토리지에 저장하는 중앙 집중식 저장소.
- 배경 및 필요성 :
  1. 데이터 웨어하우스(DW, Data Warehouse)의 정형 중심·고비용 저장 한계.
  2. 데이터 과학자의 탐색적 데이터 분석(EDA, Exploratory Data Analysis)과 머신러닝 파이프라인의 원본 데이터 수요.
  3. 저장 시점의 스키마 강제 없이 유연한 적재 필요.
- 주요 목적 : Schema-on-Read 패러다임 기반의 저비용 대용량 통합 데이터 저장·활용 기반 구축.

## Ⅱ. 데이터 레이크의 특징

- 핵심 요약 : 원본 선적재·읽기 시점 스키마 적용·오픈 포맷 기반의 유연한 저장 구조.

1. Schema-on-Read : 저장 시점의 스키마 강제 없이 데이터를 읽는 시점의 스키마 적용.
2. 선적재(ELT) : 추출 후 원천 그대로 적재(Extract, Load, Transform)하고 분석 시점에 변환.
3. 원본(Raw) 보존 : 정형·반정형·비정형 전 유형 데이터의 원래 포맷 저장.
4. 경제성 : 저렴한 대용량 객체 스토리지 기반의 확장형 저장.
5. 오픈 테이블 포맷 지원 : Apache Iceberg, Delta Lake, Apache Hudi의 ACID(Atomicity, Consistency, Isolation, Durability) 보장, 타임 트래블, 스키마 진화.

## Ⅲ. 데이터 레이크의 구조 (흐름)

- 핵심 요약 : Bronze-Silver-Gold 3단계 메달리온 아키텍처와 스토리지·엔진·포맷의 기술 스택.

```text
[ 메달리온(Medallion) 아키텍처 ]
 [ Bronze (Raw) ]      - 원천 원본, 감사·리니지
    │
    ▼
 [ Silver (Cleansed) ] - 결측치 정제, 표준화
    │
    ▼
 [ Gold (Curated) ]    - 비즈니스 집계·서빙
```

| 계층 | 데이터 성격 | 처리 작업 및 스토리지 포맷 | 주요 사용자 |
|---|---|---|---|
| Bronze(Raw Zone) | 외부 원천에서 수집된 비정제 데이터 원본 | Append-only 스트리밍·배치 적재, 원시 JSON·CSV·Parquet | 데이터 엔지니어 |
| Silver(Refined Zone) | 중복 제거, 결측치 보정, 스키마 유효성 검증 완료 | 파케이(Parquet) 압축, 파티셔닝, 역정규화 테이블 | 데이터 엔지니어, 데이터 과학자 |
| Gold(Curated Zone) | 도메인별 비즈니스 로직·집계 규칙 반영 데이터 | 차원 모델링(Fact/Dim), 고속 서빙 뷰 | BI(Business Intelligence) 분석가, 비즈니스 현업, 임원 대시보드 |

- 핵심 기술 스택 :
  1. 스토리지 계층 : AWS(Amazon Web Services) S3(Simple Storage Service), Google Cloud Storage, Azure ADLS(Azure Data Lake Storage) Gen2, Apache Ozone.
  2. 연산·처리 엔진 : Apache Spark, Trino(Presto), Flink, DuckDB.
  3. 오픈 테이블 포맷(Open Table Format) : Apache Iceberg, Delta Lake, Apache Hudi.

## Ⅳ. 데이터 웨어하우스·데이터 레이크·레이크하우스의 비교

- 핵심 요약 : Schema-on-Write의 DW, Schema-on-Read의 데이터 레이크, 양자의 결합인 레이크하우스.

| 비교 항목 | DW(Data Warehouse) | 데이터 레이크 | 레이크하우스(Lakehouse) |
|---|---|---|---|
| 스키마 적용 시점 | Schema-on-Write | Schema-on-Read | Schema-on-Read + 테이블 포맷의 스키마 강제 |
| 적재 방식 | 정제·변환 후 적재(ETL, Extract, Transform, Load) | 원본 선적재(ELT) | ELT 기반 + ACID 트랜잭션 |
| 데이터 유형 | 고품질 정형 데이터 | 정형·반정형·비정형 전체 | 전체 유형 + 큐레이션 계층 |
| 주요 활용 | 빠른 SQL(Structured Query Language) 분석 | 탐색적 분석(EDA), 머신러닝 파이프라인 | 단일 플랫폼 통합 분석·서빙 |
| 강점 | 신뢰성·분석 성능 | 유연성·경제성 | ACID 신뢰성과 레이크 경제성의 결합 |

- 선택 기준 : 엄격한 무결성·표준 리포팅은 DW, 원본 보존·탐색·ML은 데이터 레이크, 단일 플랫폼 통합은 레이크하우스.

## Ⅴ. 데이터 레이크의 장점과 한계

- 핵심 요약 : 유연성·경제성의 장점과 데이터 스웜프·소형 파일·ACID 부재·비용 통제의 한계.

- 장점
  1. 저비용 대용량 원본 데이터의 통합 수집·보존.
  2. 스키마 제약 없는 유연한 적재와 탐색·ML 지원.
  3. 오픈 포맷 기반의 벤더 종속성 최소화.

```text
[ 데이터 늪(Data Swamp) 변질 경로 ]
 무분별한 적재 (No Governance)
 + 메타데이터 부재
 + 접근 권한 통제 실패
    │
    ▼
 데이터 위치·정합성 상실, 사용 불가
```

- 한계점 1 : 데이터 스웜프(Data Swamp) 변질
  - 한계점 : 거버넌스 부재의 무분별한 적재, 메타데이터 부재, 접근 권한 통제 실패로 데이터 위치·정합성 상실 및 사용 불가 상태로 변질.
  - 해결 방안 : 적재 파이프라인 연계 자동 메타데이터·카탈로그 등록(AWS Glue, Apache Atlas), ILM(Information Lifecycle Management) 기반 아카이브 티어링·폐기, Silver 계층 승격 시 유효성 검증 통과 의무화.
- 한계점 2 : 소형 파일(Small File Problem) 누적에 따른 메타스토어 병목
  - 한계점 : 실시간 스트리밍 인입 시 수 킬로바이트(KB, Kilobyte) 단위 파티션 파일의 수백만 개 양산으로 HDFS(Hadoop Distributed File System) 네임노드 메모리 고갈 및 S3 리스팅·스캔 성능 급락.
  - 해결 방안 : 파일 압축(Compaction) 자동화 데몬 운영, Apache Iceberg·Delta Lake의 자동 파일 병합(Auto-Optimize, Bin-packing) 파이프라인 적용.
- 한계점 3 : 멀티 리더·라이터 환경의 ACID 부재 및 정합성 붕괴
  - 한계점 : 객체 스토리지 기반 단순 파일 덤프 구조에서 동시 쓰기의 덮어쓰기(Overwrite) 충돌 및 부분 실패(Partial Write) 시 불완전 파일 잔류.
  - 해결 방안 : 트랜잭션 로그(WAL, Write-Ahead Logging) 기반 스냅샷 격리를 지원하는 오픈 테이블 포맷(Apache Iceberg, Delta Lake) 도입을 통한 ACID 보장 및 타임 트래블(Time Travel) 구현.
- 한계점 4 : 스토리지 비용의 기하급수적 증가 및 FinOps 통제 부재
  - 한계점 : 보관 주기·수명주기 정책 없는 무분별한 영구 보관으로 클라우드 스토리지 청구 비용 급증 및 미사용 콜드 데이터 방치.
  - 해결 방안 : 객체 스토리지 수명주기 규칙(Lifecycle Policy) 기반 티어링(Standard → Infrequent Access → Glacier), Parquet·ORC(Optimized Row Columnar) 등 컬럼 기반(columnar) 포맷과 Snappy·ZSTD 압축 표준화.

## Ⅵ. 데이터 레이크 발전 방향에 대한 기술사적 제언

- 핵심 요약 : 레이크하우스 수렴, 행·열 수준 접근 통제, FinOps 상시화.
- 레이크하우스(Lakehouse)로의 아키텍처 수렴 : DW의 신뢰성(ACID 트랜잭션, 고성능 인덱싱)과 데이터 레이크의 유연성·경제성을 단일 플랫폼에 결합한 데이터 레이크하우스(Delta Lake, Iceberg 기반) 아키텍처 도입 가속.
- 데이터 보안 및 세밀한 접근 통제 : 객체 단위가 아닌 행·열 수준(Row/Column-level) 및 태그 기반 접근 제어(PBAC, Policy-Based Access Control) 체계(Apache Ranger, AWS Lake Formation) 수립을 통한 컴플라이언스 위험의 선제 차단.
- 비용 최적화(FinOps) 병행 : Parquet 변환을 통한 높은 비율의 스토리지 압축, Z-Order 인덱싱을 통한 쿼리 스캔량 최소화 정책의 상시화.

## Ⅶ. 결론

- 핵심 요약 : 데이터 레이크는 Schema-on-Read 기반의 경제적 저장소로 거버넌스·포맷·비용 관리가 성공 조건.
- 요약 : 메달리온 아키텍처와 오픈 테이블 포맷 기반의 원본 보존·단계적 품질화 체계.
- 시사점 : 데이터 스웜프 방지 거버넌스와 레이크하우스·FinOps 중심의 진화 전략 필요.
