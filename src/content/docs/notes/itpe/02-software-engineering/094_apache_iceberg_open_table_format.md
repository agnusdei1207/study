---
title: "Apache Iceberg / 오픈 테이블 포맷(레이크하우스)"
author: "agnusdei1207"
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

## 연관 키워드

- Apache Iceberg, 오픈 테이블 포맷(OTF, Open Table Format), 데이터 레이크하우스(Data Lakehouse), ACID 트랜잭션
- 타임 트래블(Time Travel), 스키마 진화(Schema Evolution), Delta Lake, Apache Hudi, 벤더 락인(Vendor Lock-in)

## Ⅰ. Apache Iceberg와 오픈 테이블 포맷의 개요

- 핵심 요약 : 객체 스토리지 위 데이터 파일에 RDBMS 수준 트랜잭션과 고성능 쿼리를 제공하는 테이블 포맷.
- 개념 : Apache Iceberg는 대규모 분산 객체 스토리지(S3(Simple Storage Service), GCS(Google Cloud Storage), HDFS(Hadoop Distributed File System)) 상의 대용량 페타바이트급 데이터 파일(Parquet, ORC(Optimized Row Columnar))에 대해 RDBMS(Relational Database Management System) 수준의 ACID(Atomicity, Consistency, Isolation, Durability) 트랜잭션, 고성능 쿼리, 스키마 진화(Schema Evolution), 타임 트래블(Time Travel)을 제공하는 고성능 오픈 소스 테이블 포맷.
- 배경 및 필요성 : 전통적 데이터 레이크(Hive 메타스토어 방식)의 디렉터리 기반 파티셔닝 한계(느린 파일 리스팅, 원자성 부재, 일관성 결여)와 데이터 웨어하우스(DW, Data Warehouse)의 높은 스토리지 비용의 동시 해결, 데이터 레이크하우스(Data Lakehouse)의 핵심 엔진 부상.
- 대표 3대 오픈 테이블 포맷(OTF, Open Table Format) :
  1. Apache Iceberg
  2. Delta Lake
  3. Apache Hudi

## Ⅱ. Apache Iceberg의 특징

- 핵심 요약 : 계층형 메타데이터와 스냅샷 격리, 숨겨진 파티셔닝 기반의 엔진 독립적 테이블 포맷.

1. 카탈로그-테이블 메타데이터-매니페스트-데이터 파일의 계층형 메타데이터 구조.
2. 모든 읽기 작업의 스냅샷 격리(Snapshot Isolation) 기준 수행.
3. 숨겨진 파티셔닝(Hidden Partitioning)에 따른 쿼리 시 파티션 컬럼 명시 불요화.
4. Spark, Trino, Flink, Dremio 등 다중 엔진 지원의 높은 엔진 독립성.
5. Copy-on-Write(CoW)와 Merge-on-Read(MoR)의 병행 지원 삭제·갱신 메커니즘.

## Ⅲ. Apache Iceberg의 구조 (흐름)

- 핵심 요약 : 카탈로그 포인터에서 데이터 파일까지 이어지는 계층형 메타데이터 탐색 구조.
- Iceberg 계층형 메타데이터 아키텍처.

```text
[ Iceberg Catalog ]
 - 최신 테이블 메타데이터 포인터 관리
   │
   ▼
[ Table Metadata (v1, v2) ]
 - 스키마, 파티션 스펙, 스냅샷 히스토리
   │
   ▼
[ Manifest List ]
 - 스냅샷 시점의 Manifest 파일 목록
   │
   ▼
[ Manifest Files ]
 - Data File 목록, 컬럼별 Min/Max 통계
   │
   ▼
[ Data Files (.parquet) ]
 - 실제 원천 데이터 블록 (스토리지 저장)
```

- 스냅샷 격리(Snapshot Isolation) : 읽기 작업의 격리된 특정 스냅샷 기준 수행, 백그라운드 대량 쓰기·삭제 진행 중에도 해당 스냅샷의 일관된 데이터 조회. 직렬화 가능성이나 전체 ACID 보장과의 구분 필요.
- 숨겨진 파티셔닝(Hidden Partitioning) : 일자(day), 시(hour) 등 변환 파티션의 엔진 내부 자동 처리, 쿼리 시 복잡한 파티션 컬럼 명시에 따른 오류 방지.

## Ⅳ. 오픈 테이블 포맷 3대 기술의 비교

- 핵심 요약 : 엔진 독립성, 워크로드 최적점, 삭제·갱신 메커니즘의 상이성.
- 레이크하우스 구현 배경 대조.

```text
[ 데이터 레이크 ]       개방 포맷·저비용, ACID 부재
[ 데이터 웨어하우스 ]   ACID·고성능, 폐쇄 포맷·고비용
        ↓ 두 세계의 결합
[ 데이터 레이크하우스 ] 개방 포맷 + ACID (Iceberg, Delta Lake, Hudi)
```

| 비교 항목 | Apache Iceberg | Delta Lake | Apache Hudi |
|---|---|---|---|
| 주도 기업/생태계 | 넷플릭스 주도 / Apache 재단 | Databricks 주도 / Linux 재단 | Uber 주도 / Apache 재단 |
| 엔진 독립성 | 최고(Spark, Trino, Flink, Dremio 등 완벽 지원) | Spark 중심(최근 Delta Universal Format 확장) | Spark, Flink 중심 |
| 최적 활용 워크로드 | 대규모 애드혹 분석 쿼리, 배치 분석 | Databricks 중심의 통합 레이크하우스 | 스트리밍 데이터 인제스천, 레코드 단위 고속 Upsert |
| 삭제/업데이트 메커니즘 | Copy-on-Write(CoW) 및 Merge-on-Read(MoR) | Copy-on-Write 중심 | Merge-on-Read에 극도로 특화 |

## Ⅴ. Apache Iceberg의 장점과 한계

- 핵심 요약 : 개방성·트랜잭션·시점 조회의 장점, 소형 파일·동시성 충돌·카탈로그 파편화의 한계.
- 장점
  1. 개방형 포맷 기반 벤더 락인(Vendor Lock-in) 방지와 엔진 자유 스위칭.
  2. 객체 스토리지 비용 효율 위에서의 ACID 트랜잭션 및 타임 트래블 제공.
  3. 숨겨진 파티셔닝을 통한 쿼리 편의성과 안정성 확보.
- 한계점 1 : 소형 파일(Small Files) 폭증 및 메타데이터 비대화
  - 한계점 : 스트리밍 인제스천·잦은 변경(Upsert) 작업 시 작은 Parquet 파일과 메타데이터 JSON(JavaScript Object Notation)/Avro 스냅샷의 누적, 쿼리 계획 수립 지연.
  - 해결 방안 : 정기적 콤팩션(Compaction/RewriteDataFiles)과 스냅샷 만료(ExpireSnapshots) 배치 잡 자동화 운영, 정렬 키(Sort Order) 최적화.
- 한계점 2 : 동시 쓰기 시 낙관적 동시성 제어(OCC, Optimistic Concurrency Control) 충돌로 인한 커밋 실패
  - 한계점 : 다수 분산 엔진(Spark, Flink, Trino)의 동일 파티션 동시 수정 시 충돌 발생, 긴 트랜잭션의 롤백과 리소스 낭비.
  - 해결 방안 : 쓰기 볼륨이 큰 파이프라인의 메시지 큐 기반 순차 쓰기 버퍼 도입, 파티셔닝 전략 재설계(Hidden Partitioning 최적화)를 통한 충돌 도메인 분리.
- 한계점 3 : 카탈로그 구현체 파편화에 따른 호환성·거버넌스 난제
  - 한계점 : Hive Metastore, AWS(Amazon Web Services) Glue, JDBC(Java Database Connectivity), Nessie 등 카탈로그 간 메타데이터 연동 방식 차이, 멀티 클라우드 레이크하우스 구성 복잡화.
  - 해결 방안 : 표준 Iceberg REST(Representational State Transfer) Catalog 사양 준수 엔터프라이즈 통합 카탈로그(Polaris, Unity Catalog 등) 도입, 엔진 독립적 거버넌스 확립.

## Ⅵ. 엔터프라이즈 레이크하우스 구축을 위한 기술사적 제언

- 핵심 요약 : 개방형 포맷 표준 채택을 통한 벤더 독립성 확보와 메타데이터 유지보수 자동화.
- 엔진 독립성을 통한 벤더 락인(Vendor Lock-in) 방지 : 상용 클라우드 DW(Snowflake, BigQuery, Databricks) 독점 포맷 종속 배제, 개방형 표준 Apache Iceberg 포맷의 스토리지 표준 채택과 이기종 쿼리 엔진(Trino + Spark) 자유 스위칭 아키텍처 구축.
- 메타데이터 최적화 및 가비지 컬렉션(Compaction)의 주기적 수행 : 빈번한 스트리밍 쓰기 기인 소형 파일(Small Files)·미사용 스냅샷 메타데이터 누적 대비, 정기적 파일 병합(Data Compaction)과 스냅샷 만료(Expire Snapshots) 유지보수 자동화 필수.

## Ⅶ. 결론

- 핵심 요약 : Apache Iceberg는 레이크하우스 시대의 개방형 표준 테이블 포맷.
- 요약 : 계층형 메타데이터와 스냅샷 격리로 데이터 레이크의 유연성과 웨어하우스의 신뢰성을 결합.
- 시사점 : 콤팩션 자동화, 동시성 충돌 설계, 표준 카탈로그 거버넌스가 대규모 도입 성공의 핵심 관리 포인트.
