---
sidebar:
  order: 191
  label: "191. Apache Iceberg"
  badge:
    text: "기출 · 70%"
    variant: note
title: "Apache Iceberg"
tags:
  - "notes-latest_tech"
weight: 191
extra:
  question_no: "191"
  source_status: "기출"
  source_history: "137회"
  priority: 70
  priority_note: "Iceberg 스냅샷•스키마 진화가 최근 출제됨"
date: "2026-09-15T11:40:00+09:00"
---

## Ⅰ. 개요

- **정의**: 대규모 분석 데이터셋을 위해 계층적 메타데이터 트리(Snapshot $\rightarrow$ Manifest List $\rightarrow$ Manifest) 구조로 유효 파일과 스키마를 관리하여 $O(1)$ 초고속 프루닝과 ACID 트랜잭션을 보장하는 오픈 테이블 포맷
- **배경 및 필요성**: 기존 하이브 메타스토어(Hive Metastore)의 디렉터리 경로 기반 파티셔닝으로 인한 디렉터리 리스팅($O(N)$) 병목, 파티션 변경 시 테이블 재작성 부담, 원자 커밋 부재를 극복하고, Trino, Spark, Flink, Snowflake 등 이기종 다중 엔진 간 독립적 스케일링과 무중단 스키마·파티션 진화(Partition Evolution)를 지원하기 위해 도입

## Ⅱ. 특징

- **계층형 매니페스트 트리 구조**: 카탈로그 $\rightarrow$ 메타데이터 파일 $\rightarrow$ 매니페스트 리스트 $\rightarrow$ 매니페스트 파일 $\rightarrow$ 데이터 파일로 이어지는 계층 구조로 파일 리스팅 오버헤드 원천 제거
- **숨은 파티셔닝 (Hidden Partitioning)**: 사용자가 파티션 컬럼을 직접 지정하지 않고 원본 컬럼 필터만 질의해도 엔진이 내부 파티션 변환 함수를 통해 대상 파일 자동 프루닝
- **인플레이스 스키마 및 파티션 진화**: 고유 Field-ID를 기반으로 컬럼 추가/이름 변경 시 데이터 파일 재작성 없이 즉각 반영하며, 데이터 재배치 없이 새로운 파티션 규칙 적용

## Ⅲ. 구조 및 구성요소

```text
[Apache Iceberg 메타데이터 트리 구조]
├── [카탈로그 계층 (Catalog Layer)]
│   └── [REST Catalog (원자적 포인터 교체: Compare-and-Swap)]
├── [메타데이터 계층 (Metadata Layer)]
│   ├── [테이블 메타데이터 (v1.metadata.json: 스키마, 파티션, 스냅샷 목록)]
│   └── [매니페스트 목록 (snap-*.avro: 스냅샷별 매니페스트 파일 목록)]
└── [매니페스트 및 데이터 계층 (Manifest & Data Layer)]
    ├── [매니페스트 파일 (*.avro: 파일 경로, 파티션 멤버십, 컬럼 통계)]
    └── [데이터 및 삭제 파일 (Data Parquet / Delete Files)]
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 계층 | 구성요소 | 역할 및 세부기능 |
|:---|:---|:---|
| 카탈로그 계층 | Iceberg REST Catalog | 최신 테이블 메타데이터 포인터를 원자적으로 교체(Atomic CAS)하여 동시성 트랜잭션 보장 |
| 메타데이터 계층 | 테이블 메타데이터 (`metadata.json`) | 스키마 버전, 파티션 사양, 스냅샷 이력 및 현재 활성 스냅샷 포인터 관리 |
| 매니페스트 계층 | 매니페스트 목록 (`snap-*.avro`) | 각 스냅샷을 구성하는 매니페스트 파일들의 목록과 파티션 범위 요약(Partition Bounds) 보관 |
| 매니페스트 계층 | 매니페스트 파일 (`*.avro`) | 실제 Parquet 데이터 파일의 URI, 추가/삭제 상태, 컬럼별 하한/상한(Min/Max) 통계 저장 |
| 데이터 계층 | 데이터 및 삭제 파일 | 실제 레코드가 저장된 Parquet 파일과 행 단위 갱신/삭제를 위한 Position/Equality Delete 파일 |

## Ⅳ. 흐름도

```text
[현재 스냅샷 조회] (① 쓰기 엔진이 카탈로그에서 최신 테이블 메타데이터 파일 조회)
│
▼
[신규 파일 격리 기록] (② 신규/수정 데이터를 신규 Parquet 및 Delete 파일로 스토리지에 저장)
│
▼
[신규 매니페스트 생성] (③ 추가된 파일들의 경로와 컬럼 통계를 담은 Manifest/Manifest List 파일 작성)
│
▼
[신규 메타데이터 작성] (④ 새로운 스냅샷 ID를 부여한 신규 `metadata.json` 파일 생성)
│
▼
[원자적 포인터 교체] (⑤ 카탈로그에서 CAS 연산으로 기준 버전 확인 후 신규 메타데이터 포인터 갱신)
```

- 분기 결과: CAS 충돌 미발생 시 신규 스냅샷 커밋 성공 및 읽기 엔진에 공개, 타 트랜잭션 선점으로 인한 버전 불일치 시 재시도 또는 롤백

## Ⅴ. 종류 및 비교

| 구분 | Apache Iceberg | Delta Lake | Apache Hudi |
|:---|:---|:---|:---|
| 메타데이터 설계 | 계층적 매니페스트 트리 구조 (Tree-based) | 파일 시스템 기반 순차 JSON 트랜잭션 로그 | 타임라인 기반 파일 슬라이스 및 메타데이터 테이블 |
| 엔진 독립성 | 특정 벤더 종속 없음 (REST 표준, 커뮤니티 주도) | Databricks 및 Spark 중심 (UniForm으로 확장 중) | Apache Spark, Flink 중심 스트리밍 환경 특화 |
| 파티셔닝 지원 | Hidden Partitioning & 무중단 Partition Evolution | 물리 디렉터리 파티셔닝 및 Liquid Clustering 지원 | 디렉터리 파티셔닝 및 가상 키 파티셔닝 지원 |
| 행 단위 삭제 (MoR) | Position Delete & Equality Delete 분리 지원 | Deletion Vectors (Roaring Bitmaps) 지원 | Log File 기반 Merge-on-Read 지원 |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 효과 |
|:---|:---|:---|
| 잦은 스트리밍 쓰기로 인한 Manifest 파일 누적 및 쿼리 플래닝 지연 | 백그라운드 매니페스트 재작성(`rewrite_manifests`) 액션 자동화 | 쿼리 플래닝 시 메타데이터 스캔 비용 대폭 절감 |
| Merge-on-Read 삭제 파일 누적으로 인한 읽기 시점 머지 오버헤드 | 주기적인 `rewrite_data_files` 액션 스케줄링으로 데이터-삭제 파일 병합 | 읽기 질의 I/O 지연 최소화 및 쿼리 성능 복원 |
| 실패한 트랜잭션으로 인한 고아 파일(Orphan Files) 스토리지 비용 낭비 | 스냅샷 만료(`expire_snapshots`) 및 고아 파일 제거(`remove_orphan_files`) 정책 운영 | 불필요한 객체 스토리지 용량 회수 및 비용 최적화 |

## Ⅶ. 결론

- **기술 위상/발전**: 특정 벤더 종속이 없는 개방형 거버넌스와 우수한 확장성을 바탕으로 Snowflake, BigQuery, AWS, Databricks 등 글로벌 데이터 플랫폼 생태계의 공통 스토리지 표준으로 수렴 중
- **실무 적용/통제**: 벤더 중립적인 REST 카탈로그(Polaris 등)를 단일 진실 공급원으로 설정하고, 백그라운드 데이터 파일 컴팩션과 메타데이터 정리 액션을 주기적으로 실행하여 대규모 레이크하우스 성능 유지 필요
