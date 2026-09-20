---
sidebar:
  order: 112
  label: "112. 빅데이터 (Big Data)"
  badge:
    text: "C"
    variant: note
title: "빅데이터(Big Data) 5V 특성 및 엔드투엔드 분산 데이터 플랫폼 아키텍처"
author: "OpenAI Codex"
date: "2026-09-20T19:25:00+09:00"
tags:
  - "notes-data"
weight: 112
extra:
  model: "GPT-5"
  keyword_grade: "C"
  question_no: "112"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>빅데이터 플랫폼·인프라</span><strong>빅데이터 (Big Data)</strong></div>

## 큰 그림과 30초 인출

```text
[엔터프라이즈 빅데이터 엔드투엔드 처리 파이프라인 아키텍처]

 [1. 수집 계층 (Ingestion)]       [2. 저장 계층 (Storage)]       [3. 처리·분석 계층 (Engine)]     [4. 서빙·시각화 (Serving)]
 ┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
 │ - Kafka (스트리밍 이벤트)│ ──► │ - Data Lake (S3, HDFS) │ ──► │ - Batch: Apache Spark  │ ──► │ - BI 대시보드 (Superset)│
 │ - Debezium CDC (DB로그)│      │ - Lakehouse (Iceberg)  │      │ - Stream: Apache Flink │      │ - 쿼리 엔진 (Trino)    │
 │ - Fluentd (서버 로그)  │      │ - NoSQL / Vector DB    │      │ - SQL on Hadoop (Hive) │      │ - ML/LLM 추론 모델 서빙│
 └────────────────────────┘      └────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

- 본질: **기존 단일 RDBMS의 스케일업(Scale-up) 방식으로 감당할 수 없는 초대용량(Volume), 고속 생성(Velocity), 비정형 다변성(Variety)을 갖는 데이터를 저비용 범용 x86 클러스터에서 분산 병렬 처리하고, 데이터 정확성(Veracity)을 통제하여 비즈니스 가치(Value)를 창출하는 데이터 엔지니어링 생태계**
- 암기: `볼-벨-바-베-발` (5V: Volume, Velocity, Variety, Veracity, Value) / `수-저-처-분-서` (수집, 저장, 처리, 분석, 서빙) / `람-카` (람다 vs 카파 아키텍처)
- 판단축:
  - **Schema-on-Write (전통 DW)**: 데이터 적재 시점에 엄격한 정규화 스키마를 강제, 정합성 우수하나 비정형 수용 불가
  - **Schema-on-Read (빅데이터 Lake)**: 원천 원형(Raw) 그대로 적재 후 분석 시점에 스키마를 동적으로 부여, 유연성 극대화
- 주의: 데이터 카탈로그와 메타데이터 거버넌스 없이 원천 데이터를 무제한 적재할 경우, 데이터의 위치와 신뢰도를 아무도 알 수 없는 **데이터 늪(Data Swamp)**으로 전락하여 인프라 비용만 낭비됨

## 예상문제

> 데이터 기반 의사결정의 핵심 기반인 빅데이터(Big Data)의 5V 특성을 설명하고, 수집-저장-처리-분석-서빙으로 이어지는 엔드투엔드 빅데이터 플랫폼의 참조 아키텍처 및 람다(Lambda)와 카파(Kappa) 아키텍처의 차이점을 기술하시오. (25점)

## Ⅰ. 데이터 경제 시대를 견인하는 빅데이터 개요

#### 한줄 요약: 비정형 데이터의 폭증과 분산 컴퓨팅 기술의 융합으로 방대한 원천 데이터로부터 실시간 비즈니스 통찰을 창출하는 엔지니어링 체계

- **배경**: 모바일, IoT, SNS, 로그 등 매일 테라바이트급 비정형 데이터가 쏟아져 나오며, 기존 고비용 유닉스 어플라이언스와 RDBMS 중심 아키텍처의 한계 노정
- **정의**: 대규모 데이터셋(수십 테라~페타바이트 이상)을 수평 확장(Scale-out) 가능한 분산 파일 시스템과 메모리 기반 병렬 연산 엔진을 통해 실시간 수집·저장·분석하는 인프라 및 기술 총체
- **패러다임 전환**: 값비싼 스케일업 서버 $\rightarrow$ 저가 상용 x86 노드의 분산 클러스터링(Hadoop $\rightarrow$ Spark $\rightarrow$ Cloud Native Lakehouse)

## Ⅱ. 빅데이터의 핵심 5V 특성

#### 한줄 요약: 초기 3V(규모, 속도, 다양성)에서 데이터 신뢰성(Veracity)과 사업적 가치(Value)로 진화

```text
  ┌─────────────────────────────────────────────────────────────┐
  │                   빅데이터 5대 핵심 차원 (5V)               │
  └─────────────────────────────────────────────────────────────┘
          │              │              │              │              │
  ┌───────▼──────┐┌──────▼──────┐┌──────▼──────┐┌──────▼──────┐┌──────▼──────┐
  │  1. Volume   ││ 2. Velocity ││  3. Variety ││ 4. Veracity ││   5. Value   │
  │  (규모·용량) ││  (생성속도) ││  (다양성)   ││  (정확성)   ││  (비즈니스가치)
  ├──────────────┤├──────────────┤├──────────────┤├──────────────┤├──────────────┤
  │ 테라~페타급  ││ 실시간 센서/ ││ 정형/반정형/ ││ 노이즈 정제/ ││ ROI 창출/   │
  │ 데이터 분산  ││ 스트리밍 로그││ 텍스트/영상  ││ 데이터 신뢰성││ 데이터 자산화│
  └──────────────┘└──────────────┘└──────────────┘└──────────────┘└──────────────┘
```

| 5V 차원 | 핵심 개념 및 특징 | 적용 기술 및 도전 과제 |
|:---|:---|:---|
| **1. Volume (규모)** | 물리적 단일 디스크에 담을 수 없는 페타바이트(PB)급 대용량 데이터 | HDFS, AWS S3, Google Cloud Storage, 분산 샤딩 |
| **2. Velocity (속도)** | 데이터가 실시간 초당 수십만 건 단위로 고속 생성되고 유입되는 속도 | Apache Kafka, Apache Flink, Spark Streaming |
| **3. Variety (다양성)** | RDBMS 테이블(정형)을 넘어 JSON/XML(반정형), 텍스트/영상/오디오(비정형) 포맷 공존 | Schema-on-Read, NoSQL, Vector DB, 객체 스토리지 |
| **4. Veracity (정확성)** | 수집 데이터 내 노이즈, 왜곡, 이상치, 결측치를 정제하여 신뢰성 확보 | 데이터 프로파일링, 이상치 탐지, 데이터 클렌징 |
| **5. Value (가치)** | 방대한 데이터를 처리하여 최종적으로 기업 수익 및 공공 가치 창출 | 머신러닝/DL 모델링, 개인화 추천, 사기 탐지(FDS) |

## Ⅲ. 빅데이터 플랫폼 4대 계층 참조 아키텍처

#### 한줄 요약: 수집, 분산 저장, 연산 처리, 서빙 및 거버넌스의 유기적 파이프라인

```text
 [1. 수집 계층] ──► [2. 저장 계층] ──► [3. 처리·분석 계층] ──► [4. 서빙·활용 계층]
  - Apache Kafka     - AWS S3 / HDFS     - Apache Spark (배치)     - Trino / Presto
  - Debezium CDC     - Apache Iceberg    - Apache Flink (스트림)   - Superset / Tableau
  - Logstash / Beats - Delta Lake        - MLlib / PyTorch         - REST API / Feature Store
```

1. **수집 계층 (Ingestion)**:
   - 다양한 데이터 원천(DB 트랜잭션 로그, 애플리케이션 로그, IoT 센서, 외부 API)으로부터 배치 및 실시간 스트림 데이터 인제스천
   - Kafka(분산 큐), Debezium(CDC), Fluentd/Logstash 활용
2. **저장 계층 (Storage)**:
   - 스키마에 구애받지 않고 원형(Raw) 데이터를 보관하는 저비용 대용량 객체 스토리지(S3)
   - ACID 트랜잭션을 지원하는 오픈 테이블 포맷(Apache Iceberg, Delta Lake) 결합
3. **처리 및 분석 계층 (Processing & Analytics)**:
   - 인메모리 분산 연산 엔진(Apache Spark)을 통한 대용량 데이터 변환(ETL)
   - 실시간 저지연 스트림 프로세싱(Apache Flink)
4. **서빙 및 활용 계층 (Serving & Visualization)**:
   - 대화형 분산 SQL 쿼리 엔진(Trino)을 통한 고속 데이터 조회
   - Feature Store(Feast)를 통한 머신러닝 피처 서빙 및 BI 대시보드 표출

## Ⅳ. 실시간 빅데이터 스트리밍 아키텍처: 람다 vs 카파

#### 한줄 요약: 배치와 스트림을 분리하는 람다(Lambda)와 단일 스트림 파이프라인으로 통합한 카파(Kappa)의 비교

```text
 [람다 아키텍처 (Lambda Architecture)]
                      ┌──► [Speed Layer (Flink)]  ──► [Real-time View] ──┐
  데이터 유입 ──► Kafka │                                                ├──► Serving (병합 조회)
                      └──► [Batch Layer (Spark)]  ──► [Batch View] ──────┘
  * 단점: 배치와 스트림 로직을 이중으로 구현·유지보수해야 함

 [카파 아키텍처 (Kappa Architecture)]
  데이터 유입 ──► Kafka (충분한 보관 주기) ──► [단일 Stream Layer (Flink)] ──► Serving View
  * 장점: 단일 코드베이스로 실시간 처리 및 과거 데이터 재처리(Replay) 통합
```

| 비교 항목 | 람다 아키텍처 (Lambda) | 카파 아키텍처 (Kappa) |
|:---|:---|:---|
| **설계 철학** | 실시간 레이어(Speed)와 배치 레이어(Batch)의 병렬 분리 | **모든 데이터를 실시간 스트림의 연속으로 취급** |
| **코드베이스** | 동일 비즈니스 로직을 스트림(Flink)과 배치(Spark)로 **이중 개발** | 단일 스트림 프로세싱 엔진(Flink/Spark Streaming)으로 **단일화** |
| **과거 데이터 재처리** | 배치 레이어에서 HDFS 원천 데이터를 일괄 재실행 | Kafka 토픽의 오프셋(Offset)을 0으로 되돌려 **스트림 Replay** |
| **시스템 복잡도** | 매우 높음 (두 레이어 결과의 병합 뷰 필요) | 상대적으로 낮음 (단일 파이프라인) |
| **적용 제약** | 복잡한 머신러닝 전수 학습 등 배치가 불가피한 경우 | Kafka의 장기 데이터 보관 비용 및 이벤트 순서 보장 필요 |

## Ⅴ. 전통적 데이터 웨어하우스(DW) vs 빅데이터 플랫폼

#### 한줄 요약: 스키마 온 라이트의 정형 DW와 스키마 온 리드의 비정형 빅데이터 레이크의 대조

| 비교 항목 | 전통적 데이터 웨어하우스 (DW) | 빅데이터 플랫폼 (Data Lake / Lakehouse) |
|:---|:---|:---|
| **데이터 형태** | 정형 데이터 위주 (RDBMS 테이블) | 정형, 반정형(JSON), 비정형(텍스트, 이미지) 모두 수용 |
| **스키마 시점** | **Schema-on-Write** (적재 전 스키마 사전 정의) | **Schema-on-Read** (적재는 원형, 읽을 때 스키마 파싱) |
| **스토리지 비용** | 고비용 전용 스토리지 어플라이언스 (Exadata) | 저비용 클라우드 객체 스토리지 (S3, GCS) |
| **확장성** | 수직 확장(Scale-up) 중심 (확장 비용 고가) | 수평 확장(Scale-out) 중심 (무제한 선형 확장) |
| **주요 사용자** | 경영진, 현업 비즈니스 분석가 (BI 리포트) | 데이터 엔지니어, 데이터 사이언티스트 (ML, AI) |

## Ⅵ. 실무 운영 이슈 및 트러블슈팅 (Troubleshooting)

#### 한줄 요약: 데이터 늪(Data Swamp) 방지, 작은 파일(Small Files) 문제, 파티션 Skew 해결

| 장애 요인 | 근본 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **데이터 늪 (Data Swamp) 전락** | 메타데이터 관리와 카탈로그 없이 S3에 마구 적재하여 데이터 미아 발생 | DataHub, AWS Glue 카탈로그 강제, 데이터 소유권(Data Ownership) 명시 |
| **작은 파일 문제 (Small Files Problem)** | 스트리밍 적재 시 수 KB짜리 파일 수백만 개가 생성되어 네임노드/S3 I/O 병목 | Apache Iceberg / Delta Lake의 `Compaction` 작업을 주기적 실행하여 128MB 단위 병합 |
| **데이터 편향 (Data Skew)** | 특정 파티션 키(예: 특정 국가 ID)에 데이터가 90% 몰려 Spark 태스크 1개만 지연 | Salting(임의의 난수 접미사 추가)을 통해 파티션을 재분산하여 병렬성 복원 |

## Ⅶ. 기술사적 제언: '데이터 레이크하우스(Data Lakehouse)'와 데이터 메시(Data Mesh)

#### 한줄 요약: DW의 신뢰성과 데이터 레이크의 유연성을 결합하고, 전사 중앙 집중을 탈피하여 도메인 탈중앙화로 전환

```text
 [빅데이터 아키텍처의 최종 진화형: Lakehouse + Data Mesh]
  - Storage Layer: 저비용 클라우드 S3 위에 Apache Iceberg 오픈 테이블 포맷
                   (ACID 트랜잭션, 타임 트래블, 스키마 진화 보장)
  - Org & Governance: 중앙 IT팀 독점에서 -> 도메인별 자율 데이터 제품(Data Product)으로 분산
                      (Data Mesh 원칙: 도메인 소유권, 셀프 서비스 플랫폼, 연합 거버넌스)
```

- 과거에는 원천 데이터를 레이크(S3)에 쌓고 다시 DW(Snowflake, Redshift)로 복제하는 비효율이 존재했음
- 현대 엔터프라이즈는 **Apache Iceberg**를 도입하여 단일 객체 스토리지 위에서 직접 ACID 트랜잭션을 구현하는 **데이터 레이크하우스(Data Lakehouse)**로 인프라를 일원화하고 있음

---

## 1교시 10점 답안 발췌

```text
1. 빅데이터(Big Data)의 정의
  - 기존 단일 RDBMS로 처리가 불가능한 대규모, 고속, 다양한 형태의 데이터를 분산 컴퓨팅 기술로 수집·저장·분석하는 데이터 엔지니어링 체계.

2. 빅데이터 5V 특성 및 플랫폼 아키텍처
  가. 5V 특성: Volume(규모), Velocity(속도), Variety(다양성), Veracity(신뢰성), Value(가치).
  나. 4단 아키텍처:
    - 수집(Kafka/CDC) -> 저장(S3 Data Lake/Iceberg) -> 처리(Spark 배치/Flink 스트림) -> 서빙(Trino/BI).

3. 스트리밍 아키텍처: Lambda vs Kappa
  - Lambda: Batch Layer와 Speed Layer를 이중 구축하여 정확성과 실시간성 동시 만족.
  - Kappa: 단일 스트림 엔진(Flink)으로 일원화하고 Kafka 오프셋 Replay로 과거 데이터 재처리 통합.
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제113회, 제107회, 제101회, 제98회, 제96회 기출 (합숙·모의 14회 최빈출)
- **검증 출처**:
  - Martin Kleppmann, "Designing Data-Intensive Applications", O'Reilly
  - Nathan Marz & James Warren, "Big Data: Principles and best practices of scalable realtime data systems", Manning

---

## 학습 체크

- [ ] 빅데이터 5V(Volume, Velocity, Variety, Veracity, Value)의 의미와 엔지니어링 과제를 설명할 수 있는가?
- [ ] 빅데이터 플랫폼 4대 계층(수집-저장-처리-서빙)의 대표 오픈소스 솔루션을 제시할 수 있는가?
- [ ] 람다(Lambda) 아키텍처와 카파(Kappa) 아키텍처의 구조적 차이점과 장단점을 비교할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-007 데이터 레이크](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/007_data_lake.md)
- 연관 토픽: [03-116 ELK 스택](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/116_elk_stack.md), [03-001 NoSQL](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/001_nosql.md)
