---
author: "Codex"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
extra:
  keyword_grade: "서브"
  model: "GPT-6"
  question_no: "039"
sidebar:
  badge:
    text: "서브"
    variant: "note"
  label: "039. OLAP"
  order: 39
tags:
  - "notes-data"
title: "OLAP (Online Analytical Processing) 및 MOLAP·ROLAP·HOLAP"
weight: 39
---

## 지식 로드맵 내 현재 위치

데이터 활용·분석 → 데이터 웨어하우스·비즈니스 인텔리전스 → OLAP

## 30초 인출

- 본질: **OLAP(Online Analytical Processing)는** 축적된 데이터를 여러 업무 차원으로 탐색·집계해 분석하는 처리 방식.
- 메커니즘: 분석 질의 → 차원·측정값 기준 집계와 탐색 → 표·보고서·시각화 결과.
- 통찰: 한계: 한 질의의 응답만 빠르게 하려고 사전 집계를 늘리면 저장·갱신 비용 증가 → 방안: 실제 질의 빈도·갱신 주기로 집계를 선별하고 상세 조회 비용 시험

<details>
<summary>핵심 용어</summary>

- **OLAP(Online Analytical Processing)** : 데이터의 차원별 분석과 집계를 대화형으로 수행하는 처리 방식.
- **차원(Dimension)** : 시간·지역·제품처럼 측정값을 나누어 분석하는 관점.
- **측정값(Measure)** : 매출액·수량처럼 집계하거나 비교하는 수치.
- **롤업(Roll-up)** : 상세 수준의 값을 상위 차원 수준으로 요약하는 연산.
- **드릴다운(Drill-down)** : 요약된 값을 하위 차원 수준으로 세분하는 연산.
- **ROLAP(Relational OLAP)** : 관계형 데이터베이스의 테이블을 이용해 다차원 분석을 수행하는 방식.
- **MOLAP(Multidimensional OLAP)** : 다차원 데이터 구조와 집계를 활용하는 분석 방식.
- **HOLAP(Hybrid OLAP)** : 관계형 저장과 다차원 집계 구조를 함께 사용하는 방식.

</details>

---

## 2~4교시 예상문제 (25점)

> OLAP의 다차원 분석 구조와 주요 연산을 설명하고, ROLAP·MOLAP·HOLAP의 차이와 도입 시 고려사항을 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. OLAP의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **OLAP는** 축적된 데이터를 여러 차원으로 탐색·집계해 분석하는 처리 방식 |
| 목적 | 업무 현황·추세·구성의 다각도 분석과 의사결정 지원 |

## Ⅱ. OLAP의 특징

| 특징 | 의미 |
|---|---|
| 다차원 탐색 | 동일 측정값을 시간·지역·상품 등의 축으로 재집계 |
| 계층 수준 이동 | 연도·월·일 등 요약과 상세 사이 이동 |
| 집계 비용 교환 | 사전 집계로 질의 지연을 줄이는 대신 저장·갱신 비용 증가 |

## Ⅲ. 다차원 데이터 구조와 탐색 메커니즘

```text
사실(Fact): 매출 측정값 + 시간·지역·상품 키
                │           │       │
                └ 시간 차원 ─ 지역 차원 ─ 상품 차원
                         ↓ 차원 조합별 집계
                 월·지역 매출 ↔ 상품·연도 매출
```

**차원 계층을 따른 집계 변경**

```text
일·상품·지역 매출 ── Roll-up(일→월) ──→ 월·상품·지역 매출
        ↑                                  │
        └──── Drill-down(월→일) ───────────┘
지역 고정(Slice) → 특정 지역만 조회
지역·상품 조건(Dice) → 선택한 교차 부분집합 조회
```

## Ⅳ. OLAP 연산과 구현 방식 비교

| 연산 | 데이터 관점의 변화 |
|---|---|
| Roll-up | 상세 차원 계층을 상위로 묶어 요약 |
| Drill-down | 요약 결과를 하위 차원으로 펼침 |
| Slice | 한 차원의 값을 고정해 부분 분석 |
| Dice | 여러 차원 조건을 적용해 부분 집합 분석 |
| Pivot | 분석 축을 바꾸어 행·열 배치 전환 |

**구현 구조 비교**

| 구분 | ROLAP | MOLAP | HOLAP |
|---|---|---|---|
| 저장 기반 | 관계형 테이블 | 다차원 데이터 구조 | 관계형 상세와 다차원 집계 병용 |
| 집계 활용 | 질의 시 관계형 연산 중심 | 미리 계산한 집계를 활용할 수 있음 | 요약은 다차원, 상세는 관계형으로 나눌 수 있음 |
| 고려사항 | 질의·조인 성능과 관계형 저장 규모 | 사전 처리·저장공간·갱신 비용 | 두 구조의 동기화·운영 복잡도 |

제품과 구성에 따라 집계·갱신 동작과 성능은 달라지므로, 단일 방식이 항상 더 빠르거나 확장성이 높다고 일반화하지 않음.

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 드문 질의까지 사전 집계하면 저장·갱신 비용 증가 | 실제 질의 빈도·갱신 주기로 필요한 집계만 선별 |
| 집계 응답만 시험하면 상세 조회·데이터 변경 비용 누락 | 대표 상세 질의와 갱신 부하를 함께 시험 |

## Ⅵ. 제언

가장 자주 쓰는 차원·측정값 질의부터 선정하고 사전 집계의 응답 개선과 갱신 비용을 같은 부하에서 비교.

## 출제 이력과 검증 출처

- 참고 문항: 제122회 관련 문항으로 기존 정리되어 있으나 공식 문제지 원문은 미확보, 직접 기출로 단정하지 않음
- [IBM, What is OLAP?](https://www.ibm.com/think/topics/olap)
- [Microsoft Learn, Partition storage modes and processing](https://learn.microsoft.com/en-us/analysis-services/multidimensional-models-olap-logical-cube-objects/partitions-partition-storage-modes-and-processing?view=sql-analysis-services-2025)
- [Kimball Group, The Data Warehouse Toolkit](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-toolkit/)

## 연결 토픽

- 연관 토픽: [스타 스키마](./137_star_schema.md) · [데이터 레이크](./007_data_lake.md) · [BI](./154_bi.md)
