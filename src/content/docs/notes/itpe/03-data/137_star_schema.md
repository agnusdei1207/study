---
title: "스타 스키마(Star Schema)의 차원 모델링과 최적화"
author: "agnusdei1207"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Antigravity Professional Engine"
---

## 연관 키워드

**스타 스키마(Star Schema)**, **팩트 테이블(Fact)**, **차원 테이블(Dimension)**, **Kimball**, **SCD(Slowly Changing Dimension)**, **대리키(Surrogate Key)**, **스노우플레이크**

## Ⅰ. 개요

- 핵심 요약 : **스타 스키마**는 팩트 테이블 중심으로 차원 테이블이 방사형 연결된 DW 차원 모델링 표준.
- 목적 : 비즈니스 프로세스의 계량 데이터를 다차원 분석.
- 배경 : Kimball 차원 모델링 이론 기반.
- 특징 : 팩트(측정값) + 차원(컨텍스트), 역정규화, 스타 조인.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **단순 조인·고속 쿼리·비즈니스 친화** 구조.
- **팩트 테이블** : 측정값 + FK, 거대 (Narrow & Deep).
- **차원 테이블** : 컨텍스트 속성, 역정규화 (Wide & Flat).
- **단순 조인** : Fact-Dim 1단계 조인.
- **쿼리 성능** : 스타 조인 최적화.
- **비즈니스 친화** : 분석 관점 명확.

## Ⅲ. 구조 흐름

- 핵심 요약 : **Fact_Sales 중심으로 Dim_Customer/Date/Product/Store 방사형 연결**.
- 스타 vs 스노우플레이크 : 역정규화 vs 부분 정규화.

```text
[ 스타 스키마 방사형 구조 ]

[Dim_Customer]    [Dim_Date]
       \             /
        v           v
   +---------------------+
   | Fact_Sales          |
   | Date_Key (FK)       |
   | Customer_Key (FK)   |
   | Product_Key (FK)    |
   | Store_Key (FK)      |
   | Quantity, Amount    |
   +---------------------+
        ^           ^
       /             \
[Dim_Product]    [Dim_Store]
```

```text
[ 스타 vs 스노우플레이크 ]

스타 : Fact -> Dim (역정규화, 1단계 조인)
스노우플레이크 : Fact -> Dim -> SubDim (정규화, 다단계 조인)
```

## Ⅳ. 팩트 vs 차원 비교

- 핵심 요약 : **저장 내용·볼륨·정규화·형태** 비교.

| 항목 | 팩트 테이블 | 차원 테이블 |
|---|---|---|
| 저장 내용 | 측정값 + FK | 컨텍스트 속성 |
| 예시 | 매출액, 수량 | 고객명, 카테고리, 지역 |
| 볼륨 | 수억~수십억 건 | 수백~수십만 건 |
| 정규화 | FK+측정값만 | 의도적 역정규화 |
| 형태 | Narrow & Deep | Wide & Flat |

- 스타 vs 스노우플레이크 : 역정규화(빠름) vs 정규화(스토리지 절감).

## Ⅴ. 한계와 방안

- 핵심 요약 : **역정규화 갱신 이상·팩트 비대화·M:N 관계**를 SCD·MV·브릿지 테이블로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 역정규화 갱신 이상 | 차원 데이터 갱신 시 중복 컬럼 동시 갱신 필요 | SCD Type 2, MERGE 파이프라인 | 정합성 |
| 팩트 비대화 | 수십억 건 풀 스캔 병목 | 파티셔닝, Materialized View, 컬럼나 | 쿼리 응답 시간 |
| M:N 관계 | 단순 스타로 표현 불가, 이중 집계 | 브릿지 테이블, 가중치 팩터 | 집계 정확도 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **대리키·SCD Type 2**로 조인 성능·이력 보존.
- 대리키(Surrogate Key) : 정수형 일련번호로 조인 속도 향상, 원천 키 변경 격리.
- SCD Type 2 : 이력 보존 (시작일/종료일 + 새 행).
- 파티셔닝 + Materialized View로 대용량 최적화.

## Ⅶ. 결론

- 핵심 요약 : 스타 스키마는 **Kimball 차원 모델링 표준**으로 팩트·차원·SCD·대리키가 핵심.
- 답안에는 팩트/차원 구조, 스타/스노우플레이크 비교, 한계·대응을 연결.
- 참고 : [Kimball Dimensional Modeling](https://www.kimballgroup.com/).