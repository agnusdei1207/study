---
title: "MOLAP (Multidimensional OLAP) (MOLAP: Multidimensional Online Analytical Processing)"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 다차원 배열 기반의 초고속 분석, MOLAP의 개요

### 가. MOLAP(Multidimensional OLAP)의 정의
- **MOLAP** : 데이터 웨어하우스의 데이터를 관계형 테이블(RDBMS, Relational Database Management System) 대신, 다차원 공간 데이터를 저장하기 위해 특별히 고안된 **다차원 데이터베이스** (MDDB, Multidimensional Database)의 **다차원 배열** (Multidimensional Array) 큐브(Cube) 구조에 저장하고 **사전 집계** (Pre-aggregation)하여 초고속 분석을 제공하는 OLAP(Online Analytical Processing) 기술.

---

## Ⅱ. MOLAP의 핵심 내부 저장 구조: 다차원 큐브(Hypercube)

### 가. 다차원 배열 인덱싱 메커니즘

```text
[ 3차원 데이터 큐브 (시간 x 지역 x 상품) ]
               /-----------------/| (노트북)
              /                 //| (스마트폰)
             /-----------------// |
            |                 | | |
   (서울)   |   매출 데이터   | |/ (TV)
   (부산)   |   [배열 원소]   | /
            |-----------------|/
              (1분기) (2분기)
- 관계형 테이블의 JOIN 연산이 완전히 배제됨
- Array[시간][지역][상품] 메모리 오프셋 계산만으로 $O(1)$ 즉시 데이터 조회!
```

### 나. MOLAP vs ROLAP 심층 비교 매트릭스

| 비교 항목 | MOLAP (Multidimensional OLAP) | ROLAP (Relational OLAP) |
| :--- | :--- | :--- |
| **기저 저장 엔진** | 전용 다차원 데이터베이스 (MDDB) | 관계형 데이터베이스 (RDBMS - 스타 스키마) |
| **집계 시점** | 배치 적재 시점에 모든 차원 조합 사전 전면 집계 | 질의 런타임 시점에 SQL(Structured Query Language) 쿼리를 통해 동적 계산 |
| **조회 응답 속도** | 극도로 빠름 ($O(1)$ 배열 직접 접근) | 데이터 규모 및 조인 복잡도에 따라 가변적 |
| **확장성 (Scalability)** | **큐브 폭발** (Cube Explosion)로 인해 수십 GB 내외 한계 | 페타바이트급 무제한 수평 확장 가능 |
| **상세 데이터(Raw) 추적** | 사전 집계 큐브 위주이므로 로우 레벨 상세 조회 제약 | 최하위 트랜잭션 행(Row)까지 완벽한 드릴다운 지원 |

---

## Ⅲ. MOLAP의 한계점·문제점(큐브 폭발·희소성) 및 해결 방안

### 가. 큐브 폭발(Cube Explosion)의 발생 원리
- 차원의 수($D$)와 각 차원의 속성 카디널리티($C$)가 증가함에 따라 가능한 모든 집계 셀(Cell)의 수가 기하급수적으로 폭증:
  $$\text{Total Cells} = \prod_{i=1}^D C_i$$
- 10개 차원에 각 100개 항목만 있어도 $100^{10} = 10^{20}$개의 셀이 생성되어 디스크와 메모리가 고갈됨.

### 나. 희소성(Sparsity) 압축 기술
- 실제로 판매가 발생하지 않은 비어 있는 셀(Empty Cell)이 전체 큐브의 대부분을 차지하므로, 0이나 NULL 셀을 저장하지 않고 실제 데이터가 존재하는 셀의 좌표만 **희소 행렬** (Sparse Matrix) 압축 포맷(CSR, Compressed Sparse Row / CSC, Compressed Sparse Column)으로 저장.

---

## Ⅳ. 현대 클라우드 분석 환경에서의 실무 제언

- **HOLAP** (Hybrid Online Analytical Processing) 및 인메모리 큐브로의 진화 : 현대 엔터프라이즈 환경에서는 순수 독립형 MOLAP을 단독 구축하지 않고, 상위 고빈도 요약 집계 대시보드는 **인메모리 MOLAP 큐브** (Power BI(Business Intelligence) VertiPaq 엔진)로 고속 서빙하고, 상세 데이터는 ROLAP(Snowflake, BigQuery)으로 직접 페더레이션하는 하이브리드 아키텍처를 구축해야 함.
- 사전 집계 범위의 휴리스틱 최적화 : 모든 가능한 $2^N$개 차원 조합을 전부 사전 큐브화하는 무모한 설계를 지양하고, 사용자의 실제 쿼리 로그를 분석하여 핵심 차원 조합(파레토 법칙)만 선별적으로 집계하는 적응형 큐브 빌드 파이프라인을 운영할 것을 제언함.
