---
sidebar:
  order: 190
  label: "190. 델타 레이크 (Delta Lake)"
  badge:
    text: "기출 · 50%"
    variant: note
title: "델타 레이크 (Delta Lake)"
tags:
  - "notes-latest_tech"
weight: 190
extra:
  question_no: "190"
  source_status: "기출"
  source_history: "137회"
  priority: 50
  priority_note: "Delta Lake 로그•동시성은 제품 비교에 유효함"
date: "2026-09-15T11:40:00+09:00"
---

## Ⅰ. 개요

- **정의**: Parquet 컬럼형 파일 위에 JSON 기반 순차 트랜잭션 로그(`_delta_log`)와 체크포인트를 결합하여 객체 스토리지 환경에서 완전한 ACID 트랜잭션과 시간 여행(Time Travel)을 보장하는 오픈소스 스토리지 계층 포맷
- **배경 및 필요성**: 클라우드 객체 스토리지에 단순 Parquet 파일 저장 시 원자적 커밋 부재로 인한 다중 쓰기 충돌, 작업 실패 시 불완전 파일 잔류, 스키마 불일치 에러를 방지하고, 배치와 실시간 스트리밍(Structured Streaming)을 단일 테이블에서 Exactly-once 정합성으로 통합 처리하기 위해 도입

## Ⅱ. 특징

- **순차 트랜잭션 로그 (`_delta_log`)**: 파일 추가(Add) 및 삭제(Remove) 액션을 순차 JSON 파일로 기록하여 완전한 직렬화 가능(Serializable) ACID 트랜잭션 보장
- **낙관적 동시성 제어 (OCC)**: 쓰기 작업 시 락(Lock) 없이 병렬 처리 후 커밋 시점에 버전 충돌을 검증하여 높은 동시성 지원
- **통합 포맷 지원 (UniForm)**: Delta Lake로 작성된 테이블을 Apache Iceberg 및 Apache Hudi 메타데이터로 자동 변환하여 다중 엔진 호환성 제공

## Ⅲ. 구조 및 구성요소

```text
[Delta Lake 아키텍처]
├── [트랜잭션 로그 계층 (_delta_log/)]
│   ├── [순차 JSON 커밋 로그 (000000.json, 000001.json)]
│   └── [Parquet 체크포인트 파일 (000010.checkpoint.parquet)]
├── [동시성 및 프로토콜 제어 계층]
│   ├── [낙관적 동시성 제어기 (OCC Engine)]
│   └── [유니버설 포맷 생성기 (UniForm)]
└── [데이터 스토리지 계층]
    └── [열 지향 Parquet 파일군 (Data Files)]
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 계층 | 구성요소 | 역할 및 세부기능 |
|:---|:---|:---|
| 트랜잭션 로그 계층 | 순차 커밋 로그 (`_delta_log/*.json`) | 각 트랜잭션의 파일 Add/Remove 액션, 스키마 변경, 통계(Min/Max)를 불변 커밋으로 저장 |
| 트랜잭션 로그 계층 | 체크포인트 (`*.checkpoint.parquet`) | 매 10개 커밋마다 전체 상태를 단일 Parquet로 압축 요약하여 로그 리플레이 비용 최소화 |
| 동시성 제어 계층 | OCC 충돌 검증기 | 다중 쓰기 시 기준 버전과 최신 버전 간의 읽기/쓰기 충돌 여부를 판정하여 원자 커밋 처리 |
| 데이터 저장 계층 | 데이터 파일군 (Data Files) | 실제 행 데이터를 압축된 Parquet 컬럼 파일로 보관하며 Z-Order/Liquid Clustering 적용 |
| 상호운용 계층 | UniForm (Universal Format) | Delta 테이블 변경 시 Iceberg 메타데이터(v1/v2)를 동시 생성하여 Trino/Athena 즉시 질의 지원 |

## Ⅳ. 흐름도

```text
[기준 스냅샷 조회] (① 쓰기 엔진이 최신 체크포인트와 후속 로그를 읽어 현재 상태 파악)
│
▼
[신규 데이터 기록] (② 수정/추가할 레코드를 새로운 Parquet 파일로 스토리지에 격리 작성)
│
▼
[커밋 후보 제출] (③ 변경된 파일 Add/Remove 목록을 담은 신규 버전 JSON 로그 생성 시도)
│
▼
[OCC 충돌 검증] (④ 다른 트랜잭션이 선점 커밋했는지 확인 후 파일 겹침 여부 상호 검증)
│
▼
[원자적 버전 확정] (⑤ 충돌 미발생 시 신규 버전 번호로 확정 저장 및 최신 스냅샷 공개)
```

- 분기 결과: OCC 충돌 미발생 시 즉시 커밋 확정, 동시 수정으로 인한 파티션/파일 충돌 감지 시 롤백 및 자동 재시도(Retry)

## Ⅴ. 종류 및 비교

| 구분 | Delta Lake | Apache Iceberg | Apache Hudi |
|:---|:---|:---|:---|
| 메타데이터 구조 | 순차 JSON 로그 + 체크포인트 (`_delta_log/`) | 계층적 스냅샷 트리 (Metadata $\rightarrow$ Manifest) | 파일 그룹 기반 타임라인 (Timeline Metadata) |
| 주 연계 생태계 | Apache Spark, Databricks, UniForm 다중 엔진 | Trino, Spark, Flink, Snowflake, 개방형 카탈로그 | Spark, Flink 중심 스트리밍 업서트/체인지로그 |
| 동시성 제어 | 낙관적 동시성 제어 (OCC) | 낙관적 동시성 제어 (OCC, Catalog 레벨 원자 커밋) | 낙관적/비관적 동시성 제어 (다중 락 프로바이더) |
| 작은 파일 최적화 | `OPTIMIZE` 명령어 (Compaction + Z-Order) | 백그라운드 리라이트 액션 API 수동/스케줄 실행 | 인라인/비동기 Compaction 내장 지원 |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 효과 |
|:---|:---|:---|
| 빈번한 스트리밍 쓰기로 인한 미세 로그 파일 급증 및 읽기 지연 | 10개 커밋 단위 자동 체크포인트 생성 및 주기적 로그 압축 정책 적용 | 쿼리 시작 시 메타데이터 리플레이 시간 단축 |
| `VACUUM` 과도한 실행으로 인한 Time Travel 조회 실패 및 동시 작업 에러 | 보존 기간(Retention Period) 최소 7일 설정 및 안전 체크 플래그 활성화 | 과거 시점 데이터 재현성 보장 및 진행 중인 읽기 쿼리 중단 방지 |
| 다차원 조회 시 풀스캔 발생 및 스캔 I/O 과다 | Liquid Clustering 및 Z-Ordering 적용하여 관련성 높은 컬럼 블록 정렬 | 파티션 경직성 해소 및 쿼리 필터링 속도 대폭 향상 |

## Ⅶ. 결론

- **기술 위상/발전**: Apache Spark와 Databricks의 핵심 스토리지 엔진으로 출발하여 현재는 리눅스 재단 산하 오픈소스로서 레이크하우스 확산을 주도하고 있으며, Liquid Clustering 및 타 포맷과 호환되는 UniForm을 통해 범용 데이터 레이어로 진화 중
- **실무 적용/통제**: 배치와 스트리밍 파이프라인을 메달리온 아키텍처로 통합하고, 주기적인 `OPTIMIZE` 압축과 `VACUUM` 보존 주기를 정교하게 운영하여 스토리지 비용 절감과 시간 여행 신뢰성을 동시 달성 필요
