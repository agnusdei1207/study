---
title: "데이터 레이크(데이터 늪 포함)"
category: "03-data"
tags:
  - "데이터레이크"
  - "DataLake"
  - "데이터늪"
  - "DataSwamp"
  - "SchemaOnRead"
  - "메달리온"
  - "Lakehouse"
date: "2026-09-20T23:50:43+09:00"
author: "Codex"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 플랫폼에서 대규모 분석 저장소 및 데이터 레이크로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 저장·플랫폼</span>
  <strong>데이터 레이크(데이터 늪 포함)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 다양한 원천의 정형·반정형·비정형 데이터를 가공 없이 원형(Raw) 그대로 대규모 객체 스토리지에 유연하게 적재하고, 분석 시점에 스키마를 정의(Schema-on-Read)하는 분산 빅데이터 저장·분석 플랫폼
- 메커니즘: 멀티소스 수집 $\rightarrow$ Bronze(Raw 원본 보존) $\rightarrow$ Silver(정제·표준화) $\rightarrow$ Gold(비즈니스 가공) 메달리온 정제 $\rightarrow$ 카탈로그·계보 통제 $\rightarrow$ 레이크하우스 서빙
- 산출물: 메달리온 계층 데이터셋(Parquet/Iceberg) · 메타데이터 카탈로그 · OpenLineage 계보 지도 · 스토리지 수명주기(TTL) 규칙서

<div class="itpe-flow-map" role="img" aria-label="데이터 레이크 메달리온 파이프라인 및 데이터 늪 방지 판정 체계">
  <div class="itpe-flow-node">
    <strong>1단계: 대규모 이종 원천 데이터 수집 (Bronze)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>보존</strong><span>RDBMS, 웹로그, IoT 센서, 이미지 데이터를 원형 그대로 불변 적재 (Schema-on-Read)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 결측치 정제 및 표준화 변환 (Silver)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>정제</strong><span>오류 정제, 중복 제거, 컬럼 표준화 및 Parquet/ORC 압축 컬럼 포맷 변환</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 비즈니스 도메인 집계 및 제품화 (Gold)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>모델링</strong><span>도메인별 스타 스키마 구축, 차원 모델링 및 Data Product 패키징</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 메타데이터 및 거버넌스 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>카탈로그에 메타데이터가 등록되고 Data Owner가 지정되어 '데이터 늪' 위험이 없는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (공식 서비스 승격)</strong>
      <span>전사 Data Catalog 등록 $\rightarrow$ AI/ML 피처 스토어 및 셀프서비스 BI 대시보드 쿼리 오픈</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (데이터 늪 / 다크 데이터)</strong>
      <span>승격 차단 및 격리 $\rightarrow$ 자동 크롤러 메타데이터 태깅 및 스토리지 수명주기(TTL) 강제 적용</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Schema-on-Read`: 데이터를 저장할 때는 스키마를 강제하지 않고 원본 그대로 적재한 뒤, 데이터를 읽어 쿼리하는 시점에 스키마를 동적으로 부여하는 방식
- `Medallion Architecture`: 데이터 레이크 내부를 Bronze(원시 데이터) $\rightarrow$ Silver(정제 데이터) $\rightarrow$ Gold(비즈니스 가공 데이터)로 계층화하여 데이터 품질을 단계적으로 승격시키는 파이프라인
- `Data Swamp(데이터 늪)`: 메타데이터 관리 부재, 계보 추적 불가, 소유자 부재로 인해 데이터의 가치를 잃어버리고 방치된 쓰레기통 상태의 데이터 레이크
- `Data Lineage`: 데이터가 생성된 원천부터 수집, 가공, 변환되어 최종 분석 리포트에 도달하기까지의 전 과정을 시각적으로 추적하는 계보
- `Data Lakehouse`: 데이터 레이크의 저비용 확장성과 데이터 웨어하우스의 ACID 트랜잭션 및 고성능 SQL 엔진을 융합한 차세대 아키텍처

</details>

## 예상문제

> 대용량 이기종 데이터 수용을 위한 데이터 레이크(Data Lake)의 개념, 메달리온 아키텍처(Bronze/Silver/Gold) 및 Schema-on-Read 메커니즘을 설명하고, 메타데이터 부재로 인한 '데이터 늪(Data Swamp)' 발생 원인과 거버넌스 기반 방지 대책을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **메달리온 아키텍처** | Bronze(Raw), Silver(Cleansed), Gold(Curated), Parquet, Iceberg | Ⅲ 아키텍처 |
| **데이터 늪(Data Swamp)** | 다크 데이터, 메타데이터 카탈로그 부재, Data Ownership 결여 | Ⅴ·Ⅵ |
| **데이터 레이크하우스** | 스토리지/컴퓨팅 분리, ACID 트랜잭션, 타임 트래블(Time Travel) | Ⅳ·Ⅶ |

## Ⅰ. 대규모 이종 데이터 수용소, 데이터 레이크(Data Lake)의 개요

> 데이터 레이크는 정형·비정형 원시 데이터를 원형 그대로 보존하고 분석 시 구조를 정의하는 유연한 저장 플랫폼임.

- 정의: 정형 RDBMS 데이터뿐 아니라 로그, JSON, 오디오, 비디오 등 반정형·비정형 데이터를 확장 가능한 객체 스토리지(S3, HDFS 등)에 원본 그대로 저장하는 중앙 집중식 저장소
- 등장 배경: 전통적 DW의 사전 스키마 정의(Schema-on-Write) 방식은 고비용 ETL과 비정형 데이터 수용 불가로 인해 AI/ML 및 빅데이터 분석 요구 지원에 한계 노출
- 핵심 가치: 원본 데이터 영구 보존을 통한 재생산성 확보, 컴퓨팅과 스토리지의 독립적 분리(Decoupling), 다양한 분석 엔진(Spark, Presto, Flink)의 공통 스토리지 공유

## Ⅱ. Schema-on-Write(DW) vs Schema-on-Read(Data Lake) 비교

> 데이터에 스키마 구조를 부여하는 시점의 차이가 분석 민첩성과 데이터 유연성을 결정함.

```text
[Schema-on-Write (DW)]     원천 데이터 ──(비용 높은 ETL)──> [고정 스키마 DB] ──> SQL 쿼리
[Schema-on-Read (Lake)]    원천 데이터 ──(저비용 적재)──> [객체 스토리지] ──(쿼리 시 스키마 부여)──> 분석
```

| 비교 항목 | Schema-on-Write (전통 DW) | Schema-on-Read (데이터 레이크) |
|---|---|---|
| **스키마 적용 시점** | 데이터베이스 적재(Write) 시점에 스키마 강제 | 데이터를 조회 및 분석(Read)하는 시점에 스키마 정의 |
| **수집 데이터 형태** | 사전에 정제된 정형(Structured) 데이터 위주 | 정형, 반정형(JSON, XML), 비정형(이미지, 로그) 모두 수용 |
| **초기 적재 비용** | 고비용의 사전 모델링 및 무거운 ETL 파이프라인 필수 | 저비용의 신속한 원천 데이터 ELT/직접 적재 |
| **데이터 정합성** | 매우 높음 (DBMS의 엄격한 무결성 제약조건 보장) | 원본 상태로 보존되어 데이터 품질 편차 존재 |
| **활용 유연성** | 정해진 비즈니스 리포트 및 BI 분석에 한정 | 머신러닝/딥러닝, 데이터 과학, 탐색적 데이터 분석(EDA) 최적 |

## Ⅲ. 메달리온(Medallion) 정제 구조 예시

> Bronze·Silver·Gold는 원시→정제→활용 데이터를 나누는 통용 설계 패턴이며, 제품·조직의 품질 기준에 맞게 계층을 조정함.

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│  Bronze (Raw)   │ ───>  │ Silver (Refined)│ ───>  │  Gold (Curated) │
│ - 원본 불변 보존│       │ - 결측치/중복제거│       │ - 도메인 스타스키마│
│ - Append-only   │       │ - Parquet 압축  │       │ - Data Product  │
└─────────────────┘       └─────────────────┘       └─────────────────┘
```

1. **Bronze 계층 (Raw Zone)**:
   - 원천 시스템에서 수집된 변경되지 않은 원시 데이터를 시간순으로 누적 보존 (Append-only)
   - 스키마 변경 시에도 원본이 유지되므로 언제든지 하류 데이터를 재처리(Reprocessing) 가능
2. **Silver 계층 (Refined Zone)**:
   - 결측치 처리, 데이터 유형 표준화, 암호화 처리 및 컬럼 지향 포맷(Parquet, ORC)으로 변환
   - 부서 간 공통으로 참조할 수 있는 엔터프라이즈 통합 데이터 뷰 제공
3. **Gold 계층 (Curated / Aggregated Zone)**:
   - 특정 비즈니스 도메인(재무, 마케팅)에 최적화된 집계 테이블 및 피처 스토어(Feature Store) 구축
   - 셀프서비스 BI 보고서 및 최종 머신러닝 추론 서빙

## Ⅳ. 데이터 웨어하우스 vs 데이터 레이크 vs 데이터 레이크하우스

> 세 저장소 아키텍처의 핵심 특성을 대비함.

| 비교 기준 | 데이터 웨어하우스 (DW) | 데이터 레이크 (Data Lake) | 데이터 레이크하우스 (Lakehouse) |
|---|---|---|---|
| **저장 데이터** | 정형 데이터 위주 | 모든 형태 (정형, 반정형, 비정형) | 모든 형태 (정형, 비정형 통합) |
| **스토리지 비용** | 고비용 (고성능 전용 스토리지) | 초저비용 (클라우드 객체 스토리지) | 초저비용 (오픈 테이블 포맷 기반 객체 스토리지) |
| **ACID 트랜잭션** | 완벽 지원 | 미지원 (단순 파일 저장소) | 완벽 지원 (Delta Lake, Apache Iceberg) |
| **스토리지/연산** | 밀결합 (Scale-Up 위주) | 완전 분리 (독립적 Scale-Out) | 완전 분리 (다양한 쿼리 엔진 연계) |
| **최적 활용 영역** | 전통 기업 경영 분석, BI 대시보드 | 빅데이터 수집, 데이터 과학, AI 연구 | BI 대시보드 + AI/ML 통합 플랫폼 |

## Ⅴ. 데이터 늪(Data Swamp) 발생 원인 및 위험성

> 거버넌스가 결여된 데이터 레이크는 거대한 데이터 쓰레기장으로 전락함.

```text
[데이터 무차별 적재] ──> [메타데이터 누락] ──> [내용 파악 불가] ──> [데이터 늪 (Data Swamp)]
                                                                           │
                                                                           ▼
                                                             [다크 데이터 누적 & 비용 폭증]
```

- **메타데이터 부재**: 파일의 생성자, 비즈니스 의미, 스키마 이력이 카탈로그에 기록되지 않아 검색 불가
- **Data Ownership 부재**: 데이터 적재 후 품질 모니터링과 수명주기 폐기를 책임지는 도메인 오너 부재
- **다크 데이터(Dark Data) 누적**: 분석 가치가 없거나 중복된 임시 파일이 삭제되지 않고 방치되어 스토리지 비용 폭증
- **보안 및 규제 위반**: 개인정보(PII) 포함 여부와 접근 통제(RBAC)가 적용되지 않아 법적 과징금 리스크 노출

## Ⅵ. 데이터 레이크 문제점·대응책

> 카탈로그·계보·수명주기·데이터 계약을 결합하여 검색 불가·품질 저하·다크 데이터 위험을 줄임.

| 통제 영역 | 구체적 실행 대책 | 실무적 통제 효과 |
|---|---|---|
| **메타데이터 카탈로그** | AWS Glue, Apache Atlas 연계 자동 크롤링 및 비즈니스 태깅 | 전사 검색 가능한 데이터 자산 사전 구축 |
| **데이터 계보 (Lineage)** | OpenLineage 및 dbt 기반 데이터 흐름 추적 파이프라인 구성 | 원천 변경에 따른 영향도 분석 및 감사 추적 |
| **수명주기 정책 (FinOps)** | 객체 스토리지 Lifecycle(Hot $\to$ Cold $\to$ Glacier $\to$ 삭제) 수립 | 다크 데이터 자동 소멸 및 클라우드 비용 절감 |
| **데이터 계약 (Data Contract)** | 상류·하류 간 스키마·품질 기준 합의 | 호환되지 않는 변경·저품질 유입 감소 |

## Ⅶ. 기술사적 제언: 레이크하우스로의 진화와 개방형 테이블 포맷

> "데이터 레이크의 가치는 단순히 쌓아둔 테라바이트가 아니라, 신뢰할 수 있는 거버넌스 하에서 즉시 쿼리할 수 있는 가용성에 있다."

### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 수집량이 아니라 발견 가능성·신뢰성·소유권이 레이크의 가치를 결정한다. 소비 목적 없는 원본 축적은 늪을 만든다.
- `나라면`: 수집 시 Data Contract와 Owner를 등록하고 Silver 진입 전에 스키마·품질·민감정보 Gate를 통과시키겠다.

### 실전 답안용 기술사적 제언
- 판정: 카탈로그 검색 가능성, Lineage 추적성, 품질 SLA 준수 여부가 입증된 데이터셋만 상위 계층(Silver/Gold)으로 승격함
- 대안: Apache Iceberg 기반 오픈 테이블 포맷 도입 $\rightarrow$ 객체 스토리지 상의 ACID 트랜잭션 및 타임 트래블(Time Travel) 구현
- 검증: 메타데이터 카탈로그 등록률 100%, 미사용 다크 데이터 비율 10% 미만 통제
- 효과: 데이터 늪 전락을 원천 예방하고, BI 분석가와 AI 연구원이 단일 저장소를 안전하게 공유하는 통합 레이크하우스 완성

```text
[현행 한계] ─────────> [개선 방안] ─────────> [검증 기준] ─────────> [실행 효과]
데이터 늪화           메달리온 & Iceberg     카탈로그 등록률 100%    ACID 트랜잭션 보장
다크 데이터 방치       FinOps 수명주기(TTL)   다크 데이터 < 10%       스토리지 TCO 40% 절감
```

## 1교시 10점 답안 발췌

```text
1. 데이터 레이크(Data Lake) 및 데이터 늪(Data Swamp)의 정의
- 데이터 레이크: 모든 형태의 원시 데이터를 가공 없이 객체 스토리지에 저장하고 Schema-on-Read로 분석하는 플랫폼
- 데이터 늪: 메타데이터와 거버넌스 결여로 데이터의 출처와 내용을 파악할 수 없게 된 방치된 저장소 상태

2. 메달리온 아키텍처 및 늪 방지 대책
┌─────────────────────────────────────────────────────────────┐
│ Bronze (Raw 불변 보존) → Silver (정제/표준화) → Gold (비즈니스)│
├─────────────────────────────────────────────────────────────┤
│ 늪 방지 대책:                                               │
│  - 메타데이터 카탈로그 (Glue/Atlas) 및 Data Lineage 자동화  │
│  - Data Contract 체결로 스키마 파손 방지                    │
│  - 스토리지 수명주기(TTL) 정책으로 다크 데이터 자동 제거    │
└─────────────────────────────────────────────────────────────┘

3. 기술사적 제언: 레이크하우스(Lakehouse)로의 진화
- Apache Iceberg/Delta Lake 도입으로 저비용 객체 스토리지 상에서 ACID 트랜잭션과 고성능 SQL 분석을 동시 달성
```

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제137·139회 확인 · 제119회는 KPC 보조자료이며 공식 원문 미확보
- **표준 및 레퍼런스**: [AWS Data Lake Architecture Guide](https://aws.amazon.com/what-is/data-lake/), Databricks Medallion Architecture Whitepaper, Apache Iceberg Documentation

## 학습 체크

- [ ] [Ⅰ 개요]: Schema-on-Read 관점의 데이터 레이크 정의와 등장 배경을 기술하였는가?
- [ ] [Ⅱ 비교]: Schema-on-Write(DW)와 Schema-on-Read(Lake)의 차이를 비교하였는가?
- [ ] [Ⅲ 아키텍처]: Bronze, Silver, Gold 메달리온 3계층의 정제 파이프라인을 제시하였는가?
- [ ] [Ⅴ·Ⅵ 통제]: 데이터 늪의 4대 원인과 메타데이터/Lineage/TTL 기반 방지 대책을 기술하였는가?

## 연결 토픽

- [데이터 거버넌스](./006_data_governance.md) · [로지컬 데이터웨어하우스(LDW)](./132_logical_data_warehouse.md) · [빅데이터 플랫폼 아키텍처](./135_big_data_platform_architecture.md) · [데이터 표준화](./008_data_standardization.md)
