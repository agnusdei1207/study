---
title: "Apache Iceberg / 오픈 테이블 포맷(레이크하우스)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "Gemini 3.8 Flash (High)"
author: "Antigravity"
lastModified: "2026-03-30T10:00:00+09:00"
---

## 큰 그림과 30초 인출

- **본질**: 오브젝트 스토리지(S3 등)에 분산 저장된 대규모 파일들을 단일 RDBMS 테이블처럼 관리할 수 있도록 3계층 메타데이터 트리로 추상화하여, 완전한 ACID 트랜잭션과 빠른 파일 스킵(Pruning)을 제공하는 오픈 테이블 포맷 기술이다.
- **메커니즘**: 카탈로그 $\rightarrow$ 메타데이터 파일 $\rightarrow$ 매니페스트 리스트 $\rightarrow$ 매니페스트 파일의 계층적 Avro 트리를 유지하며, 쓰기 작업 시 신규 스냅샷을 선작성한 후 카탈로그 포인터를 원자적으로 교체(Atomic Swap)한다.
- **산출물**: 메타데이터 파일(JSON), 매니페스트 리스트(Avro), 매니페스트 파일(Avro), Parquet 데이터 파일, 타임 트래블 스냅샷 이력.

<div class="itpe-flow">
  <div class="itpe-flow-steps">
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>1. Catalog 탐색</strong></span>
      <div class="itpe-step-detail">최신 메타데이터 파일(vN.metadata.json) 포인터 참조</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>2. Manifest List 분석</strong></span>
      <div class="itpe-step-detail">스냅샷에 속한 Manifest 파일 목록 및 파티션 범위 스캔</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>3. Manifest File 프루닝</strong></span>
      <div class="itpe-step-detail">컬럼 Min/Max 통계 기반 불필요 데이터 파일 $O(1)$ 스킵</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node is-current">
      <span class="itpe-keyword"><strong>Quality Gate</strong></span>
      <div class="itpe-step-detail"><strong>판정 질문</strong><span>스냅샷 커밋 간 충돌이 없고 트랜잭션 무결성이 유지되는가?</span></div>
      <div class="itpe-flow-branches">
        <div class="itpe-flow-branch"><strong>통과</strong><span>원자적 포인터 스왑 및 최신 스냅샷 게시</span></div>
        <div class="itpe-flow-branch"><strong>미통과</strong><span>낙관적 동시성 제어(OCC) 재시도 및 충돌 복구</span></div>
      </div>
    </div>
  </div>
</div>

---

## 핵심 메커니즘

### (1) Apache Hive vs Apache Iceberg 비교

| 구분 | 전통적 하이브(Hive) | Apache Iceberg |
|---|---|---|
| **테이블 관리 단위** | 디렉터리(Directory) 레벨 | **파일(File) 레벨** |
| **파일 목록 조회** | S3/HDFS 파일 전체 목록화($O(N)$ 디렉터리 리스팅 병목) | **메타데이터 파일 직접 지정($O(1)$ 다이렉트 스캔)** |
| **트랜잭션(ACID)** | 원자성 없음 (동시 쓰기 시 데이터 불일치 발생) | **완전한 ACID 보장 (스냅샷 격리, 원자적 커밋)** |
| **스키마/파티션 변경** | 테이블 재생성 또는 데이터 전체 마이그레이션 필요 | **데이터 재작성 없는 즉각적 진화(Schema/Partition Evolution)** |
| **파티셔닝 방식** | 쿼리 작성자가 파티션 컬럼을 외워서 조건절 명시 | **히든 파티셔닝(원천 컬럼 질의 시 자동 파티션 프루닝)** |

### (2) Iceberg 3계층 메타데이터 아키텍처
1. **Iceberg Catalog**: 테이블의 현재 상태를 가리키는 최신 메타데이터 파일의 위치를 원자적으로 저장 및 교체 (REST, Nessie, AWS Glue, Hive Metastore 등).
2. **Metadata File (`vN.metadata.json`)**: 테이블 스키마, 파티션 사양, 과거 및 현재 스냅샷 히스토리를 저장.
3. **Manifest List (`snap-N.avro`)**: 특정 스냅샷에 속한 모든 매니페스트 파일 목록과 파티션 범위 요약 정보를 보관.
4. **Manifest File (`m-N.avro`)**: 실제 데이터 파일의 물리적 경로, 파티션 값, 컬럼별 최소/최대값(Min/Max) 통계 정보를 유지하여 쿼리 시 불필요한 파일 스캔을 배제함.

### (3) 오픈 테이블 포맷 3대 기술 비교

| 비교 항목 | Apache Iceberg | Delta Lake | Apache Hudi |
|---|---|---|---|
| **주도 기업/커뮤니티** | **넷플릭스, 애플 / Apache 재단** | Databricks / 오픈소스화 | Uber / Apache 재단 |
| **메타데이터 구조** | **계층적 Avro 트리 (3계층 분리)** | JSON 트랜잭션 로그 + Parquet 체크포인트 | 타임라인(Timeline) + 메타데이터 파일 |
| **엔진 독립성** | **완전 독립 (Spark, Trino, Flink, StarRocks 동등 지원)** | Spark 중심 최적화 (타 엔진 어댑터 의존) | Spark 중심 (Flink 점진 지원) |
| **파티셔닝 유연성** | **히든 파티셔닝 & 파티션 진화 지원** | 명시적 디렉터리 기반 파티션 | 디렉터리 기반 파티션 |
| **주요 워크로드** | 대규모 대화형 OLAP 분석, 멀티 엔진 개방형 DW | Databricks 통합 데이터 파이프라인 | 잦은 Upsert/Delete 중심의 스트리밍 CDC |

---

## 실무 적용 및 도입 체크리스트

1. **컴팩션(Compaction) 스케줄링**: 스트리밍 적재 시 대량 양산되는 1KB~수MB 단위 소형 파일을 128MB~512MB 표준 Parquet 파일로 비동기 병합(`rewriteDataFiles`)하고 있는가?
2. **스냅샷 만료(Snapshot Expiration)**: 과거 타임 트래블용 스냅샷이 무한정 누적되지 않도록 주기적인 `expireSnapshots` 배치 작업을 수행하여 메타데이터 팽창을 방지하는가?
3. **고아 파일(Orphan Files) 정화**: 트랜잭션 실패나 네트워크 오류로 인해 메타데이터에 연결되지 못한 채 스토리지에 방치된 잔여 파일을 자동 삭제(`remove_orphan_files`)하는가?
4. **오픈 카탈로그 연계**: 특정 벤더에 종속되지 않는 REST 카탈로그(Apache Polaris 등)를 배치하여 멀티 클라우드 엔진 간 권한 및 메타데이터를 통합 관리하는가?

---

## 실패 시나리오 및 트러블슈팅

| 위험 | 대책 | 효과 |
|---|---|---|
| **스트리밍 적재로 인한 수천만 개 소형 파일 파편화** | Iceberg 비동기 컴팩션 및 빈 패킹(Bin-packing) 프로시저 상시 가동 | 쿼리 스캔 속도 4배 향상 및 메타데이터 크기 75% 압축 |
| **과거 스냅샷 누적으로 쿼리 플래닝 지연 급증** | 주간 단위 `expireSnapshots` 정책 수립 및 고아 파일 자동 정화 파이프라인 실행 | 쿼리 플래닝 레이턴시 50ms 미만 안정 유지 |
| **개발자의 파티션 함수 오용으로 스토리지 전체 풀스캔 발생** | 원천 타임스탬프 질의 시 내부 변환 함수를 자동 매핑하는 히든 파티셔닝 적용 | 불필요한 전체 스캔 원천 방지 및 I/O 비용 60% 절감 |

---

## 차세대 확장 및 융합

- **스토리지-컴퓨트 완전 분리 개방형 레이크하우스**: 스토리지는 S3/GCS 상의 Apache Iceberg 포맷으로 일원화하고, 컴퓨트는 Spark(배치 ETL), Flink(실시간 스트리밍), Trino(대화형 BI 질의) 등 최적의 엔진을 상호 교체하며 사용하는 완전 개방형 아키텍처가 글로벌 표준으로 확립되었다.
- **통합 오픈 카탈로그(Polaris / Gravitino)**: Snowflake, Databricks 등 주요 벤더들이 Iceberg를 기본 스토리지 포맷으로 지원함에 따라, 다중 벤더 엔진 간에 테이블 메타데이터와 접근 통제를 중재하는 오픈 REST 카탈로그의 중요성이 극대화되고 있다.

---

## 25점형 실전 답안 프레임워크

### 1단락: 오픈 테이블 포맷의 등장 배경 및 Apache Iceberg 개념
- **배경**: 전통적 데이터 레이크(Hive)의 디렉터리 리스팅 성능 병목과 ACID 트랜잭션 부재, 벤더 독점 DW의 높은 비용 및 락인 극복 필요.
- **정의**: 오브젝트 스토리지 상의 Parquet 데이터 파일을 파일 단위 메타데이터 트리로 관리하여 원자적 ACID와 고속 쿼리 프루닝을 지원하는 개방형 테이블 포맷.

### 2단락: Apache Iceberg 3계층 아키텍처 및 공학적 메커니즘
- **아키텍처 도해**: Catalog $\rightarrow$ Metadata File $\rightarrow$ Manifest List $\rightarrow$ Manifest Files $\rightarrow$ Data Files.
- **원자적 커밋과 읽기 최적화 메커니즘**:
  - 쓰기: 신규 매니페스트 생성 후 낙관적 동시성 제어(OCC) 기반 원자적 카탈로그 포인터 스왑.
  - 읽기: Manifest 파일 내부의 컬럼 Min/Max 통계를 이용한 다이렉트 파일 스킵($O(1)$ 탐색).

### 3단락: 오픈 테이블 포맷 3대 기술 비교 및 실무 운영 거버넌스
- **Iceberg vs Delta Lake vs Hudi 3사 비교**: 메타데이터 트리 구조, 엔진 독립성, 파티셔닝 유연성 중심 비교.
- **스몰 파일 및 메타데이터 최적화 기법**: Bin-packing 기반 비동기 컴팩션, 스냅샷 만료 정책, 고아 파일 삭제.

### 4단락: 개방형 데이터 레이크하우스 구축을 위한 기술사적 제언
- **스토리지-컴퓨트 완전 분리와 REST 카탈로그 채택**: 단일 사본(SSOT) 스토리지 위에 Flink/Spark/Trino 멀티 엔진을 유연하게 결합하고, Apache Polaris 오픈 카탈로그 기반의 데이터 거버넌스를 구축할 것을 제언함.

---

## 10점형 핵심 요약

1. **정의**: 오브젝트 스토리지의 파일들을 RDBMS 테이블처럼 추상화하여 ACID 트랜잭션과 고속 분석을 지원하는 오픈 테이블 포맷.
2. **핵심 구조**: Catalog $\rightarrow$ Metadata File(JSON) $\rightarrow$ Manifest List(Avro) $\rightarrow$ Manifest File(Avro) $\rightarrow$ Data Files(Parquet).
3. **실무 핵심**: 히든 파티셔닝으로 사용자 쿼리 실수를 방지하고, 컴팩션 및 스냅샷 만료 관리를 통해 메타데이터와 스몰 파일 팽창을 방어함.
