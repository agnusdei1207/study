---
title: "데이터 레이크(데이터 늪 포함)"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 플랫폼에서 대규모 분석 저장소 및 데이터 레이크로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 저장·플랫폼</span>
  <strong>데이터 레이크(데이터 늪 포함)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 정형·반정형·비정형 데이터를 가공 없이 원형(Raw) 그대로 대규모 객체 스토리지에 유연하게 저장하고, 분석 시점에 스키마를 정의(Schema-on-Read)하는 분산 분석 데이터 플랫폼
- 아키텍처: 메달리온(Medallion) 구조: Bronze(Raw 원본) $\to$ Silver(정제·표준화) $\to$ Gold(비즈니스 집계)
- 늪 방지: 메타데이터 카탈로그, 데이터 계보(Lineage), Data Owner 지정, 보존 주기(TTL) 통제

<div class="itpe-flow-map" role="img" aria-label="데이터 수집에서 메달리온 아키텍처 및 데이터 늪 방지로 이어지는 체계">
  <div class="itpe-flow-node"><strong>다양한 데이터 원천</strong><small>RDBMS · 웹로그 · IoT 센서 · 이미지/음성</small></div>
  <div class="itpe-flow-arrow">↓<small>Batch · CDC · Kafka Streaming</small></div>
  <div class="itpe-flow-node">
    <strong>메달리온 레이크 아키텍처</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Bronze (Raw)</strong><span>수집 원형 그대로 불변 보존 (Schema-on-Read)</span></div>
      <div class="itpe-flow-branch"><strong>Silver (Refined)</strong><span>결측치 정제 · 표준화 · Parquet 포맷 변환</span></div>
      <div class="itpe-flow-branch"><strong>Gold (Curated)</strong><span>업무 도메인별 집계 및 Data Product 제공</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>거버넌스 & 데이터 늪(Data Swamp) 방어</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>거버넌스</strong><span>데이터 카탈로그 · Data Lineage · RBAC/ABAC</span></div>
      <div class="itpe-flow-branch"><strong>늪 방지</strong><span>다크 데이터 제거 · 수명주기(TTL) · Data Contract</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Lakehouse & AI/BI 활용</strong></div>
</div>

## 예상문제

> 대용량 이기종 데이터 수용을 위한 데이터 레이크(Data Lake)의 개념, 메달리온 아키텍처(Bronze/Silver/Gold) 및 Schema-on-Read 메커니즘을 설명하고, 메타데이터 부재로 인한 '데이터 늪(Data Swamp)' 발생 원인과 거버넌스 기반 방지 대책을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **데이터 늪(Data Swamp)** | 메타데이터·품질·소유권 통제 결여로 데이터의 출처와 내용을 파악할 수 없게 된 폐기물 저장소 상태 | Ⅵ 실무 대책, Ⅶ 결론 |
| **메달리온 아키텍처(Medallion Architecture)** | Bronze(원시), Silver(정제), Gold(비즈니스 가공)의 계층형 데이터 레이크 정제 파이프라인 | Ⅲ 아키텍처 |

## Ⅰ. 대규모 이종 데이터 수용소, 데이터 레이크(Data Lake)의 개요

> **한줄 요약:** 데이터 레이크는 정형·비정형 원시 데이터를 원형 그대로 보존하고 분석 시 구조를 정의하는 유연한 저장 플랫폼임.

- 정의: 정형 관계형 데이터뿐 아니라 로그, JSON, 오디오, 비디오 등 반정형·비정형 데이터를 확장 가능한 객체 스토리지(S3, HDFS 등)에 원본 그대로 저장하는 중앙 집중식 저장소
- 등장 배경: 전통적 DW의 사전 모델링(Schema-on-Write) 방식은 고비용 ETL과 비정형 데이터 수용 불가로 인해 AI/ML 및 빅데이터 분석 요구 지원에 한계 노출
- 핵심 가치: 원본 데이터 영구 보존을 통한 재생산성 확보, 컴퓨팅과 스토리지의 독립적 분리(Decoupling), 다양한 분석 엔진(Spark, Presto, Flink)의 공통 스토리지 공유

## Ⅱ. 데이터 레이크의 핵심 특징 및 메커니즘

> **한줄 요약:** Schema-on-Read, 저장-연산 분리, 메달리온 정제 흐름을 통해 확장성과 분석 유연성을 극대화함.

| 특징 | 동작 원리 및 메커니즘 | 실무적 기여 |
|---|---|---|
| **Schema-on-Read** | 데이터를 적재(Load)할 때는 스키마를 강제하지 않고, 질의(Read) 시점에 구조 해석 | 수집 파이프라인 지연 최소화 및 신속한 데이터 적재 |
| **저장·컴퓨팅 분리** | 저비용 객체 스토리지(S3 등)와 탄력적 쿼리 엔진(Trino/Spark) 분리 | 데이터 급증 시 스토리지 비용 최적화 및 독립적 스케일아웃 |
| **다양한 포맷 수용** | Raw(CSV, JSON) $\to$ 열 지향 압축 포맷(Parquet, ORC) $\to$ 오픈 테이블 포맷(Iceberg) | 데이터 압축률 향상 및 컬럼 기반 초고속 분석 질의 |
| **다양한 워크로드 지원** | SQL 기반 정형 질의, 스트리밍 실시간 처리, 비정형 AI/LLM 모델 학습 동시 지원 | 전사 분석 인프라의 단일 진입점(Single Source) 역할 |

## Ⅲ. 메달리온(Medallion) 참조 아키텍처

> **한줄 요약:** Bronze(원천 원본), Silver(정제·결합), Gold(비즈니스 집계)의 3계층 정제 파이프라인을 구축함.

<div class="itpe-pipeline" role="img" aria-label="메달리온 3단계 아키텍처">
  <div class="itpe-pipeline-node"><strong>Bronze Layer</strong><small>Raw 원본 적재</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Silver Layer</strong><small>정제 · 검증 · 표준화</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Gold Layer</strong><small>비즈니스 집계 · Mart</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Serving</strong><small>BI 대시보드 · AI/ML</small></div>
</div>

| 계층 (Layer) | 데이터 상태 및 가공 수준 | 데이터 포맷 및 처리 활동 | 대상 사용자 |
|---|---|---|---|
| **Bronze (Raw)** | 원천 시스템 데이터의 불변 복사본 (Append-only) | 원본 JSON, CSV, CDC 로그 그대로 적재 | 데이터 엔지니어, 감사팀 |
| **Silver (Cleansed)** | 결측치 정제, 표준 용어 적용, 중복 제거, 데이터 조인 | Parquet, Delta/Iceberg 포맷, 스키마 강제 | 데이터 분석가, ML 엔지니어 |
| **Gold (Curated)** | 비즈니스 KPI 도출, 차원 모델링(Star Schema), 집계 | 최종 정제된 고성능 분석 테이블 | 현업 비즈니스 부서, 임원진 |

## Ⅳ. 데이터 웨어하우스(DW) vs 데이터 레이크 vs 레이크하우스 비교

> **한줄 요약:** 레이크는 유연성, DW는 정합성을 담당하며, 레이크하우스는 두 장점을 통합한 차세대 패러다임임.

| 비교 기준 | 데이터 웨어하우스 (DW) | 데이터 레이크 (Data Lake) | 데이터 레이크하우스 (Lakehouse) |
|---|---|---|---|
| **데이터 유형** | 정형 데이터 (정제된 트랜잭션) | 정형, 반정형, 비정형 데이터 전반 | 정형, 반정형, 비정형 데이터 전반 |
| **스키마 적용** | Schema-on-Write (사전 모델링) | Schema-on-Read (질의 시점 해석) | Schema-on-Write + Schema Evolution |
| **트랜잭션 보장** | 엄격한 ACID 보장 | 기본 미지원 (파일 시스템 한계) | 오픈 테이블 포맷(Iceberg, Delta) 기반 ACID 지원 |
| **스토리지 비용** | 고비용 고성능 블록/SAN 스토리지 | 초저비용 대규모 객체 스토리지 | 저비용 객체 스토리지 기반 메타데이터 캐싱 |
| **주요 워크로드** | 정형 SQL, BI 보고서, OLAP | 탐색적 분석, 대규모 데이터 처리, ML 학습 | BI 보고서, 고속 SQL, 실시간 스트리밍, ML 통합 |

## Ⅴ. 데이터 늪(Data Swamp) 발생 원인 및 위험성

> **한줄 요약:** 메타데이터 없는 무분별한 저장은 레이크를 검색 불가능한 쓰레기장인 '데이터 늪'으로 전락시킴.

- 정의: 데이터 레이크에 저장된 데이터에 대한 메타데이터, 소유권, 데이터 계보, 품질 관리가 이루어지지 않아, 데이터의 존재 여부와 가치를 파악할 수 없게 된 기능 마비 상태
- 4대 주요 발생 원인:
  1. **메타데이터 부재**: 파일의 생성 일시, 스키마, 출처(Lineage)가 카탈로그에 기록되지 않음
  2. **Data Ownership 부재**: 데이터 적재 후 유지보수 및 폐기 책임을 지는 주체가 없음
  3. **다크 데이터(Dark Data) 누적**: 한 번 쓰고 버려진 임시 파일 및 중복 데이터가 무한 방치됨
  4. **보안 및 규제 통제 상실**: 개인정보(PII) 포함 여부 및 접근 이력이 추적되지 않음

## Ⅵ. 데이터 늪 방지를 위한 4대 거버넌스 대책

> **한줄 요약:** 카탈로그 자동화, 계보 추적, 수명주기(TTL) 관리, 데이터 계약으로 늪화를 원천 차단함.

| 영역 | 구체적 대책 및 구현 기법 | 실무적 통제 효과 |
|---|---|---|
| **메타데이터 카탈로그** | AWS Glue, Apache Atlas 연계 자동 크롤링 및 태깅 | 전사 검색 가능한 데이터 자산 사전 구축 |
| **데이터 계보 (Lineage)** | OpenLineage 및 dbt 기반 데이터 흐름 추적 파이프라인 구성 | 원천 변경에 따른 영향도 분석 및 감사 추적 |
| **수명주기 정책 (FinOps)** | 객체 스토리지 Lifecycle(Hot $\to$ Cold $\to$ Glacier $\to$ 삭제) 수립 | 다크 데이터 자동 소멸 및 클라우드 비용 절감 |
| **데이터 계약 (Data Contract)** | 상류 시스템과 하류 레이크 간 스키마 및 SLA 사전 계약 | 스키마 파손 및 저품질 데이터 유입 원천 차단 |

## Ⅶ. 결론 및 기술사적 제언

> **한줄 요약:** 데이터 레이크의 성패는 수집량에 있지 않고 오픈 테이블 포맷과 레이크하우스 거버넌스 완성도에 있음.

- [핵심 통찰]: 단순히 '모든 데이터를 모아두면 언젠가 가치가 생길 것'이라는 기대는 막대한 클라우드 청구서와 데이터 늪만을 남김. 데이터 레이크는 수집 시점부터 '누가, 왜, 어떤 목적으로 소비할 것인가'가 정의된 Data Product 기반으로 운영되어야 함.
- 나라면: 파일 기반 레이크의 한계를 극복하기 위해 Apache Iceberg를 공통 테이블 포맷으로 도입하여 ACID 트랜잭션, 타임 트래블(Time Travel), 파티션 진화를 보장하고, Great Expectations를 CI/CD에 통합하여 Silver 계층 진입 전 품질 검증에 실패한 데이터는 자동으로 Quarantined 영역으로 격리하는 무결성 파이프라인을 구축하겠음.

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 데이터 레이크는 정형·비정형 원시 데이터를 원형 그대로 저비용 객체 스토리지에 저장하고, Schema-on-Read를 통해 분석하는 분산 데이터 플랫폼임.

### 2. 핵심 메커니즘 / 체계
```text
Raw Sources ──▶ [Bronze: 원본] ──▶ [Silver: 정제] ──▶ [Gold: 비즈니스]
                   │
                   ▼
[데이터 늪 방지] Data Catalog + OpenLineage + Lifecycle TTL + Data Contract
```
- 거버넌스 결여 시 데이터 늪(Data Swamp)으로 전락하므로 메달리온 파이프라인과 메타데이터 통제가 필수적임.

### 3. 차별화 제언
- 파일 단위 레이크의 정합성 한계를 돌파하기 위해 Apache Iceberg/Delta Lake 기반 레이크하우스(Lakehouse)로 고도화해야 함.

## 출제 이력과 검증 출처

- 출제 이력: 제139회·137회 정보관리기술사 기출, 제119회 KPC 모의고사
- 검증 출처: Databricks Medallion Architecture Guide, AWS Data Lake Governance Best Practices

## 학습 체크

- [ ] 데이터 레이크와 DW, 레이크하우스의 핵심 차이(스키마 적용 시점, ACID 등)를 비교할 수 있는가?
- [ ] 메달리온 아키텍처(Bronze, Silver, Gold)의 계층별 특성을 설명할 수 있는가?
- [ ] 데이터 늪(Data Swamp)의 발생 원인과 4대 거버넌스 해결책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [데이터 거버넌스](./006_data_governance.md)
- 연관 토픽: [로지컬 데이터웨어하우스(LDW)](./132_logical_data_warehouse.md), [빅데이터 플랫폼 아키텍처](./135_big_data_platform_architecture.md), [ELK 스택](./116_elk_stack.md)
- 다음 토픽: [데이터 표준화(공공 DB 표준화 지침·테이블 정의서 포함)](./008_data_standardization.md)
