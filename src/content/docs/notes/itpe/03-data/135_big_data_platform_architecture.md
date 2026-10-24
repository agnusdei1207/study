---
title: "빅데이터 플랫폼 아키텍처"
author: "agnusdei1207"
date: "2026-10-25T00:19:25+09:00"
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

- 빅데이터 플랫폼, 5계층, Lakehouse, Apache Kafka, Apache Iceberg
- Data Mesh, DataOps, OpenLineage, CDC(Change Data Capture), 메타데이터 카탈로그

## Ⅰ. 빅데이터 플랫폼 아키텍처의 개요

- 핵심 요약 : 원천 데이터에서 서빙까지 엔드투엔드 데이터 파이프라인을 다섯 계층으로 연결한 통합 기술 구조.
- 개념 : 대규모 정형·반정형·비정형 데이터를 수집, 저장, 처리, 분석, 서빙하는 기술 구조 (**빅데이터 플랫폼**).
- 배경 및 필요성 : 분산된 원천에서 데이터가 빠르게 늘어나면서 시스템별 개별 처리는 중복 적재와 정합성 문제를 낳으므로 통합 플랫폼이 필요함.
- 주요 목적 : 데이터 자산을 재사용 가능한 형태로 분석 조직과 서비스에 공급.

## Ⅱ. 빅데이터 플랫폼 아키텍처의 특징 및 장점

- 핵심 요약 : 계층별로 역할을 분리해 장애와 변경의 영향 범위를 줄이고, 계층마다 기술을 교체할 수 있는 구조.

1. 원천 계층 : OLTP(Online Transaction Processing) 시스템, IoT(Internet of Things) 기기, 로그, SaaS(Software as a Service) 애플리케이션에서 데이터가 발생 → 이종 원천을 하나의 흐름으로 묶는 출발점.
2. 수집·버퍼 계층 : **Apache Kafka** 같은 메시지 브로커와 CDC(Change Data Capture, 변경 데이터 캡처)로 변경분을 전달 → 원천 시스템 부하를 완충.
3. 스토리지 계층 : **Lakehouse** (데이터 레이크의 저비용 저장과 데이터 웨어하우스의 관리 기능을 결합한 저장 구조) → Apache Iceberg 같은 테이블 포맷으로 ACID(Atomicity, Consistency, Isolation, Durability) 트랜잭션과 타임 트래블을 제공.
4. 처리 계층 : Apache Spark, Apache Flink, Trino로 배치, 스트림, 대화식 질의를 분산 병렬 처리 → 처리 방식별 최적 엔진 선택.
5. 서빙 계층 : BI(Business Intelligence) 대시보드, AI(Artificial Intelligence)·ML(Machine Learning) 모델, REST(Representational State Transfer) API로 결과를 제공 → 의사결정과 서비스에 직접 연결.

## Ⅲ. 빅데이터 플랫폼 아키텍처의 구조 (흐름)

- 핵심 요약 : 원천에서 서빙까지 다섯 계층이 단방향으로 흐르고, 그 전체를 가로지르는 관리 영역이 함께 작동하는 구조.

```text
[ 5계층 데이터 흐름 ]

[1. 원천] OLTP, IoT, 로그, SaaS
      ↓
[2. 수집] Kafka, CDC
      ↓
[3. 스토리지] Iceberg·Delta on S3
      ↓
[4. 처리] Spark, Flink, Trino
      ↓
[5. 서빙] BI, AI/ML, REST API
```

```text
[ 횡단 관리 영역 ]

    메타데이터 카탈로그 (검색·정의)
    데이터 계보 (OpenLineage)
    접근 제어·보안 (Apache Ranger)
    DataOps (파이프라인 자동화)
```

- 횡단 관리 : 메타데이터 카탈로그, 데이터 계보, 접근 제어, 운영 자동화가 다섯 계층 모두에 걸쳐 적용됨.
- **DataOps** (데이터 파이프라인의 개발·배포·품질 관리를 자동화하는 운영 방식) : 파이프라인 변경을 테스트와 함께 반복 배포하는 체계.

## Ⅳ. 계층별 기술 비교

- 핵심 요약 : 계층마다 요구하는 기능이 달라 기술 선택 기준도 계층별로 따로 정해야 함.

| 계층 | 대표 기술 | 핵심 기능 |
| --- | --- | --- |
| 원천 | Oracle, PostgreSQL, IoT 장비 | 이종 프로토콜 수집 |
| 수집·버퍼 | Kafka, Debezium | 완충, CDC, 역압(backpressure) 제어 |
| 스토리지 | Iceberg, Delta Lake, Amazon S3 | ACID 트랜잭션, 타임 트래블, 객체 스토리지 기반 확장 |
| 처리 | Spark, Flink, Trino | 인메모리 분산 병렬 처리 |
| 서빙 | PostgreSQL, Redis, ClickHouse | 초 미만 응답 조회 |

## Ⅴ. 빅데이터 플랫폼 아키텍처의 한계와 방안

- 핵심 요약 : 스트림과 배치의 정합성, 셔플 병목, 중앙 집중 병목을 통합 처리 구조, 외부 셔플, 도메인 분산 소유로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 스트림·배치 정합성 | 두 경로의 처리 결과가 달라 지표 신뢰성 저하 | 스트림과 배치를 통합한 처리, Iceberg ACID 트랜잭션 | 정합성 오차율 |
| 셔플 병목 | 노드 간 셔플이 집중되어 처리량 저하 | 외부 셔플 서비스(Apache Celeborn) 도입, 버케팅(bucketing)으로 셔플 감소 | 잡 지연 시간 |
| 중앙 병목 | 모든 파이프라인 요청이 중앙 데이터팀에 집중 | **Data Mesh** (도메인 팀이 데이터를 제품 단위로 소유·서빙하는 분산 구조), 셀프서비스 인프라 | 요청 리드타임 |

## Ⅵ. 빅데이터 플랫폼 아키텍처에 대한 기술사적 제언

- 핵심 요약 : Lakehouse로 저장 체계를 단일화하고 Data Mesh로 소유 구조를 전환해 플랫폼을 현대화하는 방향이 바람직함.

1. 저장 체계는 Lakehouse 방식으로 단일화하면 DW(Data Warehouse)와 AI 워크로드가 같은 스토리지를 공유해 중복 복제 비용을 줄일 수 있다.
2. 중앙팀 병목이 두드러지는 조직이라면 도메인 팀이 데이터 제품을 직접 생산하고 서빙하도록 Data Mesh 원칙을 단계적으로 도입하는 것이 좋다.
3. 오케스트레이션과 카탈로그 도구를 조직 표준으로 정해 파이프라인 운영 편차를 줄이는 것이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : 빅데이터 플랫폼은 다섯 계층, Lakehouse 저장 구조, Data Mesh 소유 구조가 결합된 현대화 방향으로 설계함.
- 시사점 : 기술 자체보다 계층 경계와 데이터 소유 책임을 명확히 하는 것이 플랫폼의 지속 가능성을 결정함.
