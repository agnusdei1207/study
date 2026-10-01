---
title: "Apache Iceberg / 오픈 테이블 포맷(레이크하우스)"
author: "Antigravity"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. Apache Iceberg와 오픈 테이블 포맷의 개요

- **개념** : 대규모 분산 객체 스토리지(S3, GCS, HDFS) 상에 저장된 대용량 페타바이트급 데이터 파일(Parquet, ORC)에 대해 RDBMS 수준의 ACID 트랜잭션, 고성능 쿼리, 스키마 진화(Schema Evolution), 타임 트래블(Time Travel)을 제공하는 고성능 오픈 소스 테이블 포맷.
- **배경 및 필요성** : 전통적 데이터 레이크(Hive 메타스토어 방식)의 디렉터리 기반 파티셔닝 한계(느린 파일 리스팅, 원자성 부재, 일관성 결여)와 데이터 웨어하우스(DW)의 높은 스토리지 비용 문제를 동시에 해결하는 '데이터 레이크하우스(Data Lakehouse)'의 핵심 엔진으로 부상.
- **대표 3대 오픈 테이블 포맷** : Apache Iceberg, Delta Lake, Apache Hudi.

## Ⅱ. Apache Iceberg 계층형 메타데이터 아키텍처

```text
   [ Iceberg Catalog ] ─────── 최신 테이블 메타데이터 포인터 관리
          │
          ▼
   [ Table Metadata (v1, v2) ] ─ 스키마, 파티션 스펙, 스냅샷 히스토리 보유
          │
          ▼
   [ Manifest List ] ───────── 스냅샷 시점의 Manifest 파일 목록 (파티션 통계)
          │
          ▼
   [ Manifest Files ] ──────── 실제 Data File 목록 및 컬럼별 Min/Max 통계 메트릭
          │
          ▼
   [ Data Files (.parquet) ] ── 실제 원천 데이터 블록 (스토리지에 저장)
```

- **스냅샷 격리 (Snapshot Isolation)** : 모든 읽기 작업은 격리된 특정 스냅샷을 기준으로 수행되어, 백그라운드에서 대량의 쓰기/삭제 작업이 진행 중이어도 읽기 쿼리는 완벽한 일관성(ACID) 보장.
- **숨겨진 파티셔닝 (Hidden Partitioning)** : 사용자가 쿼리 시 복잡한 파티션 컬럼을 명시하지 않아도, 일자(day), 시(hour) 등 변환 파티션을 엔진이 내부적으로 자동 처리하여 쿼리 오류 방지.

## Ⅲ. 오픈 테이블 포맷 3대 기술 비교

| 비교 항목 | Apache Iceberg | Delta Lake | Apache Hudi |
|---|---|---|---|
| 주도 기업/생태계 | 넷플릭스 주도 / Apache 재단 | Databricks 주도 / Linux 재단 | Uber 주도 / Apache 재단 |
| 엔진 독립성 | 최고 (Spark, Trino, Flink, Dremio 등 완벽 지원) | Spark 중심 (최근 Delta Universal Format 확장) | Spark, Flink 중심 |
| 최적 활용 워크로드 | 대규모 애드혹 분석 쿼리, 배치 분석 | Databricks 중심의 통합 레이크하우스 | 스트리밍 데이터 인제스천, 레코드 단위 고속 Upsert |
| 삭제/업데이트 메커니즘 | Copy-on-Write (CoW) 및 Merge-on-Read (MoR) | Copy-on-Write 중심 | Merge-on-Read에 극도로 특화 |

## Ⅳ. 엔터프라이즈 레이크하우스 구축 시 기술사적 제언

- **엔진 독립성을 통한 벤더 락인(Vendor Lock-in) 방지** : 특정 상용 클라우드 DW(Snowflake, BigQuery, Databricks)의 독점 포맷에 종속되지 않도록, 개방형 표준인 Apache Iceberg 포맷을 스토리지 표준으로 채택하여 이기종 쿼리 엔진(Trino + Spark)을 자유롭게 스위칭하는 유연한 데이터 아키텍처 구축.
- **메타데이터 최적화 및 가비지 컬렉션(Compaction) 주기적 수행** : 빈번한 스트리밍 쓰기로 인해 작은 파일(Small Files)과 미사용 스냅샷 메타데이터가 누적되면 쿼리 성능이 급격히 저하되므로, 정기적인 파일 병합(Data Compaction) 및 스냅샷 만료(Expire Snapshots) 유지보수 자동화 필수.
