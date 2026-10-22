---
title: "빅데이터 플랫폼 아키텍처"
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

**빅데이터 플랫폼**, **5계층**, **Lakehouse**, **Kafka**, **Iceberg**, **Data Mesh**, **DataOps**, **OpenLineage**

## Ⅰ. 개요

- 핵심 요약 : **빅데이터 플랫폼 아키텍처**는 원천에서 서빙까지 엔드투엔드 데이터 파이프라인의 통합 기술 구조.
- 목적 : 대규모 정형·반정형·비정형 데이터 수집·저장·처리·분석·서빙.
- 배경 : 분산 환경 데이터 폭증 → 통합 플랫폼 필요.
- 특징 : 5계층, Lakehouse, DataOps, 거버넌스.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **5계층**으로 원천→수집→저장→처리→서빙을 분리.
- **원천** : OLTP, IoT, 로그, SaaS.
- **수집·버퍼** : Kafka, CDC(Debezium), Airbyte.
- **스토리지** : Iceberg/Delta + S3 (Lakehouse).
- **처리** : Spark, Flink, Trino.
- **서빙** : BI, AI/ML, REST API.

## Ⅲ. 아키텍처 흐름

- 핵심 요약 : **원천 → 수집 → 스토리지 → 처리 → 서빙** 5계층.
- 횡단 관리 : 메타데이터 카탈로그, 계보(OpenLineage), 보안(Ranger), DataOps.

```text
[ 빅데이터 플랫폼 5계층 ]

[5. 서빙] BI, AI/ML, REST, Text2SQL
        ^
[4. 처리] Spark, Flink, Trino
        ^
[3. 스토리지] Iceberg/Delta + S3 (Lakehouse)
        ^
[2. 수집] Kafka, CDC, Airbyte
        ^
[1. 원천] OLTP, IoT, 로그, SaaS
```

## Ⅳ. 계층별 비교

- 핵심 요약 : **계층별 역할·기술·요구사항**.

| 계층 | 기술 | 핵심 기능 |
|---|---|---|
| 원천 | Oracle, PostgreSQL, IoT | 이종 프로토콜 지원 |
| 수집·버퍼 | Kafka, Debezium | 완충, CDC, 역압 제어 |
| 스토리지 | Iceberg, S3, Delta | ACID, 타임 트래블, 무제한 확장 |
| 처리 | Spark, Flink, Trino | 인메모리 분산 병렬 |
| 서빙 | PostgreSQL, Redis, ClickHouse | 서브세컨드 조회 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **스트림/배치 정합성·셔플 병목·중앙 병목**을 통합 파이프라인·외부 셔플·Data Mesh로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 스트림/배치 정합성 | 카디널리티 불일치로 지표 신뢰성 저하 | 통합 스트림-배치, Iceberg ACID | 정합성 오차 |
| 셔플 병목 | 노드 간 셔플로 처리량 저하 | 외부 셔플(Celeborn), Bucketing | 잡 지연 |
| 중앙 병목 | 모든 파이프라인이 중앙팀에 집중 | Data Mesh, 셀프서비스 인프라 | 리드타임 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **Lakehouse 단일화·Data Mesh 전환**으로 현대화.
- Lakehouse : S3 + Iceberg로 DW/AI 워크로드 단일 스토리지.
- Data Mesh : 도메인 팀이 데이터 제품 자체 서빙.
- Airflow/Dagster 오케스트레이션, DataHub/Amundsen 카탈로그.

## Ⅶ. 결론

- 핵심 요약 : 빅데이터 플랫폼은 **5계층 + Lakehouse + Data Mesh**로 현대화.
- 답안에는 5계층, 거버넌스, 한계·대응, 실무 제언을 연결.
- 참고 : [Apache Iceberg](https://iceberg.apache.org/).