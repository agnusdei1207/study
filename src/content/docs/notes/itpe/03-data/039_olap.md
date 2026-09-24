---
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
extra:
  keyword_grade: "기초"
  model: "GPT-6"
  question_no: "039"
sidebar:
  badge:
    text: "기초"
    variant: "note"
  label: "039. OLAP"
  order: 39
tags:
  - "notes-data"
title: "OLAP (Online Analytical Processing) 및 MOLAP·ROLAP·HOLAP"
weight: 39
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 활용·분석</span><span>데이터 웨어하우스·비즈니스 인텔리전스</span><strong>OLAP</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 170" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="170" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Top: OLTP to DW -->
  <rect x="15" y="10" width="140" height="26" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="85" y="27" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">운영계 트랜잭션 (OLTP)</text>

  <line x1="155" y1="23" x2="200" y2="23" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-olap)"/>

  <rect x="205" y="10" width="300" height="26" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <text x="355" y="27" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">데이터 웨어하우스 (DW): 스타 스키마 &amp; 다차원 큐브</text>

  <!-- Middle: 5 OLAP Operations -->
  <line x1="260" y1="36" x2="260" y2="48" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-olap)"/>

  <rect x="20" y="48" width="480" height="42" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="260" y="65" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">[OLAP 5대 다차원 분석 연산]</text>
  <text x="260" y="80" text-anchor="middle" font-size="8.5" fill="var(--color-primary-dark, #0369a1)">• 롤업(요약) • 드릴다운(상세) • 슬라이싱(단면) • 다이싱(부분큐브) • 피보팅(축회전)</text>

  <!-- Bottom 3 Architectures -->
  <line x1="260" y1="90" x2="260" y2="102" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-olap)"/>

  <rect x="15" y="104" width="155" height="52" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="92" y="121" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">ROLAP (관계형)</text>
  <text x="92" y="135" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">관계형 DB 직접 질의</text>
  <text x="92" y="147" text-anchor="middle" font-size="7.5" fill="var(--color-primary-dark, #0369a1)">대용량 무제한 확장성</text>

  <rect x="182" y="104" width="155" height="52" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="260" y="121" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">MOLAP (다차원)</text>
  <text x="260" y="135" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">다차원 배열 사전 계산</text>
  <text x="260" y="147" text-anchor="middle" font-size="7.5" fill="var(--color-success-dark, #15803d)">초고속 밀리초 응답</text>

  <rect x="350" y="104" width="155" height="52" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <text x="427" y="121" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">HOLAP (혼합형)</text>
  <text x="427" y="135" text-anchor="middle" font-size="8" fill="var(--color-text, #334155)">상위 요약(M) + 상세(R)</text>
  <text x="427" y="147" text-anchor="middle" font-size="7.5" fill="var(--color-primary-dark, #0369a1)">속도와 확장성 균형</text>

  <defs>
    <marker id="arrow-olap" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **최종 사용자가 대규모 비즈니스 데이터를 다차원(Multi-dimensional) 관점에서 대화식(Interactive)으로 분석하고 신속하게 의사결정을 내릴 수 있도록 지원하는 데이터 웨어하우스 분석 처리 체계**
- 암기: `롤-드-슬-다-피` = 롤업(상위 요약) · 드릴다운(하위 상세) · 슬라이싱(단면) · 다이싱(작은 큐브) · 피보팅(차원축 회전)
- 3대 아키텍처: `ROLAP(확장성/관계형)` vs `MOLAP(고속 응답/다차원 배열/큐브 폭증)` vs `HOLAP(하이브리드)`
- 현대적 진화: 레거시 정적 큐브(Pre-aggregation)에서 **컬럼형 분산 쿼리 엔진(ClickHouse, Snowflake, DuckDB)** 기반의 온디맨드 실시간 OLAP로 패러다임 전환
---

## 1교시 예상문제 (10점)

> OLAP (Online Analytical Processing) 및 MOLAP·ROLAP·HOLAP의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. OLAP의 정의

- 데이터 웨어하우스의 다차원 모델(Cube)을 기반으로 의사결정자가 대화식으로 데이터를 분석하는 **온라인 분석 처리 기술**

### 2. 다차원 연산 및 3대 아키텍처 비교

- **5대 연산**: 롤업(요약) $\to$ 드릴다운(상세) $\to$ 슬라이싱(단면) $\to$ 다이싱(부분 큐브) $\to$ 피보팅(축 회전)

| 구분 | ROLAP (관계형) | MOLAP (다차원) | HOLAP (혼합형) |
|---|---|---|---|
| 기반 엔진 | 관계형 DB (스타 스키마) | 전용 다차원 배열 큐브 | 큐브(상위) + RDBMS(하위) |
| 집계 시점 | 쿼리 시 동적 집계 중심 | 사전 완제 계산 (Pre-calculated) | 상위 계층만 선별 사전 집계 |
| 장단점 | 대용량 확장성 우수 / 속도 한계 | 초고속 응답 / 큐브 폭증 위험 | 성능과 확장성의 절충 |

### 3. 차별화 제언

- 사전 집계 배치 지연을 해소하기 위해 **컬럼 지향 엔진(ClickHouse/DuckDB)** 기반의 온디맨드 벡터화 연산을 결합하여 **실시간 Zero-Cube OLAP**를 구현함
---

## 2~4교시 예상문제 (25점)

> 데이터 웨어하우스 환경에서 다차원 데이터 분석을 지원하는 OLAP(Online Analytical Processing)의 개념을 설명하고, 다차원 큐브의 4대 핵심 연산과 ROLAP, MOLAP, HOLAP의 구조적 차이 및 최신 현대적 모던 데이터 스택(MDS) 관점의 발전 방향을 논하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 대화식 다차원 의사결정 지원 인프라, OLAP 개요

- 정의: **OLAP(Online Analytical Processing)**은 다차원 데이터 모델(Cube)을 기반으로 사용자가 정형화되지 않은 복잡한 집계 및 추세 분석 쿼리를 대화형(Interactive)으로 수행하여 신속하게 비즈니스 통찰을 도출하는 기술 체계
- 목적: 운영계 RDBMS(OLTP)의 부하를 차단하고, 수억 건의 이력 데이터를 시간, 조직, 제품 등 다양한 업무 차원(Dimension)별로 즉시 요약·대조할 수 있는 분석 환경 제공
- 필요성: 단순 RDBMS에서 대규모 GROUP BY 및 다중 테이블 조인을 수행하면 쿼리 지연이 수십 초~수 분에 달하여 경영진의 실시간 대시보드 및 탐색적 분석이 불가능함

#### 한줄 요약

- OLAP는 단건 트랜잭션을 처리하는 OLTP와 달리, 다차원 큐브를 통해 대규모 데이터를 다각도에서 즉각 분석하는 시스템임

### Ⅱ. OLTP vs OLAP의 핵심 특성 비교

| 비교 항목 | OLTP (Online Transaction Processing) | OLAP (Online Analytical Processing) |
|---|---|---|
| **주요 목적** | 일상적 비즈니스 트랜잭션의 실시간 처리 | 전략적 의사결정을 위한 다차원 분석 및 보고 |
| **데이터 모델** | 3차 정규형(3NF/BCNF) 정규화 모델 (중복 최소화) | 스타 스키마, 스노우플레이크, 다차원 큐브 (비정규화) |
| **데이터 성격** | 최신 현재 데이터 (Current), 잦은 단건 갱신 | 과거 장기 이력 데이터 (Historical), 읽기 전용 |
| **트랜잭션 단위** | 짧고 단순한 INSERT/UPDATE/DELETE (ACID) | 복잡한 다중 집계 및 범위 스캔 쿼리 (SELECT) |
| **응답성 요건** | 수 밀리초($ms$) 단위 즉각 처리, 높은 동시성 | 대화식 탐색 지원 (수 초 이내 복합 집계 완료) |
| **핵심 지표** | 초당 트랜잭션 수 (TPS), 데이터 무결성 | 쿼리 처리량(Throughput), 응답 지연(Latency) |

#### 한줄 요약

- OLTP는 '데이터의 정확한 기록과 갱신'이 핵심이고, OLAP는 '기록된 데이터의 다각도 통찰 인출'이 핵심임

### Ⅲ. 다차원 모델(Cube)의 정적 구조와 5대 핵심 연산

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 120" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="120" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Left: Cube Illustration -->
  <rect x="20" y="15" width="170" height="90" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <rect x="20" y="15" width="170" height="22" fill="var(--color-primary-light, #e0f2fe)" rx="4"/>
  <text x="105" y="30" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">다차원 큐브 (Cube)</text>
  <text x="105" y="52" text-anchor="middle" font-size="8" fill="var(--color-text, #0f172a)">• 팩트: 매출액, 수량</text>
  <text x="105" y="68" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">• 시간 차원 (연/월/일)</text>
  <text x="105" y="82" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">• 지역 차원 (시도/지점)</text>
  <text x="105" y="96" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">• 상품 차원 (분류/품목)</text>

  <!-- Right: 5 Operations -->
  <rect x="205" y="15" width="300" height="90" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="215" y="32" font-size="8.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">1. 롤업 (Roll-up)</text>
  <text x="320" y="32" font-size="8" fill="var(--color-text, #334155)">: 세부에서 상위로 요약 (일 ──▶ 월 ──▶ 년)</text>

  <text x="215" y="48" font-size="8.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">2. 드릴다운 (Drill-down)</text>
  <text x="320" y="48" font-size="8" fill="var(--color-text, #334155)">: 상위 집계에서 세부 분해 (년 ──▶ 월 ──▶ 일)</text>

  <text x="215" y="64" font-size="8.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">3. 슬라이싱 (Slicing)</text>
  <text x="320" y="64" font-size="8" fill="var(--color-text, #334155)">: 특정 1개 차원을 고정하여 2차원 평면 절단</text>

  <text x="215" y="80" font-size="8.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">4. 다이싱 (Dicing)</text>
  <text x="320" y="80" font-size="8" fill="var(--color-text, #334155)">: 복수 차원 구간 선택으로 작은 서브 큐브 추출</text>

  <text x="215" y="96" font-size="8.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">5. 피보팅 (Pivoting)</text>
  <text x="320" y="96" font-size="8" fill="var(--color-text, #334155)">: 행과 열의 축을 맞바꾸어 관점을 90도 회전</text>
</svg>
</div>

| 구성요소 | 개념 및 정의 | 스키마 구현 요소 |
|---|---|---|
| **팩트 테이블 (Fact Table)** | 분석의 중심이 되는 정량적 측정값(Measure)과 차원 테이블의 외래키(FK)들의 집합 | 매출액, 판매수량, 결제단가, 접속시간 |
| **차원 테이블 (Dimension Table)** | 팩트 데이터를 분류, 그룹화, 필터링하는 관점(Context)을 제공하는 기준 속성들의 집합 | 일자/분기(시간), 시도/지점(지역), 분류/품목(상품) |

#### 한줄 요약

- OLAP 연산은 롤업으로 넓게 보고, 드릴다운으로 깊게 파고들며, 슬라이싱·다이싱·피보팅으로 각도를 바꾸어 입체적으로 분석함

### Ⅳ. OLAP 3대 구현 아키텍처 심층 비교: ROLAP vs MOLAP vs HOLAP

| 비교 항목 | ROLAP (Relational OLAP) | MOLAP (Multidimensional OLAP) | HOLAP (Hybrid OLAP) |
|---|---|---|---|
| **저장 엔진** | 관계형 데이터베이스 (RDBMS) | 다차원 데이터베이스 (MDDBMS) | 다차원 큐브 + 관계형 DB 복합 |
| **저장 방식** | 스타/스노우플레이크 스키마 테이블 | $N$차원 배열(Dense/Sparse Array) | 상위 집계는 큐브, 상세 팩트는 RDBMS |
| **사전 계산 수준** | 뷰 및 인덱스 활용, 쿼리 시 동적 집계 | 모든 가능한 차원 조합을 **사전 완제 집계** | 상위 요약 데이터만 선별 사전 집계 |
| **조회 응답 속도** | 대용량 시 느림 ($I/O$ 조인 부하) | **가장 빠름** (밀리초 단위 응답) | 상위는 초고속, 상세 조회는 보통 |
| **데이터 확장성** | **수십 TB 이상 무제한 확장 우수** | 차원 증가 시 **큐브 폭증(Explosion)** 취약 | ROLAP의 확장성과 MOLAP의 속도 절충 |
| **갱신 용이성** | 실시간 적재 및 DML 갱신 용이 | 데이터 변경 시 전체 큐브 재생성 필요 | RDBMS 파티션 단위 증분 적재 가능 |
| **대표 제품** | Oracle Exadata, PostgreSQL, Presto | Cognos, MS SSAS, Oracle Essbase | SAP BW, MicroStrategy, Mondrian |

#### 한줄 요약

- ROLAP는 확장성과 갱신이 유연하고, MOLAP는 사전 계산으로 응답이 가장 빠르며, HOLAP는 둘의 장점을 결합한 하이브리드임

### Ⅴ. 다차원 모델링 스키마 구조: 스타 스키마 vs 스노우플레이크 스키마

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 115" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="115" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Left: Star Schema -->
  <rect x="15" y="12" width="240" height="90" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <rect x="15" y="12" width="240" height="22" fill="var(--color-primary-light, #e0f2fe)" rx="4"/>
  <text x="135" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">스타 스키마 (Star Schema)</text>
  <text x="135" y="48" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-text, #0f172a)">[중앙 팩트 테이블] ── [비정규화 차원들]</text>
  <text x="135" y="66" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">차원 테이블 1개 계층만 조인</text>
  <text x="135" y="82" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-success-dark, #15803d)">조인 수 최소화로 쿼리 성능 극대화 (표준)</text>

  <!-- Right: Snowflake Schema -->
  <rect x="265" y="12" width="240" height="90" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <rect x="265" y="12" width="240" height="22" fill="var(--color-surface, #f1f5f9)" rx="4"/>
  <text x="385" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #334155)">스노우플레이크 (Snowflake Schema)</text>
  <text x="385" y="48" text-anchor="middle" font-size="8.5" fill="var(--color-text, #0f172a)">[팩트] ── [차원] ── [정규화 하위차원]</text>
  <text x="385" y="66" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">차원 테이블 3NF 정규화 (가지치기 형태)</text>
  <text x="385" y="82" text-anchor="middle" font-size="8" fill="var(--color-danger, #ef4444)">다단계 조인으로 쿼리 지연 위험</text>
</svg>
</div>

| 구분 | 스타 스키마 (Star Schema) | 스노우플레이크 스키마 (Snowflake Schema) |
|---|---|---|
| **차원 테이블 정규화**| 비정규화(Denormalized) 상태 유지 | 제3정규형(3NF)으로 부분 정규화 |
| **스키마 형태** | 중앙 팩트 주위를 차원이 감싸는 단순 별 모양 | 차원이 하위 차원으로 가지를 치는 복잡한 눈송이 모양 |
| **쿼리 복잡도** | 단순 (단일 레벨 조인으로 성능 극대화) | 복잡 (차원 간 다단계 조인 필요로 쿼리 저하) |
| **저장 공간** | 데이터 중복 존재로 약간 증가 | 데이터 중복 제거로 디스크 절감 |
| **실무 권장** | **OLAP 및 데이터 마트 표준 모델 (조회 최적화)**| 차원 속성이 방대하여 갱신 관리가 중요한 특수 환경 |

#### 한줄 요약

- DW 환경에서는 저장 공간 절약보다 쿼리 조인 단순화가 우선이므로 스타 스키마가 산업계 표준으로 채택됨

### Ⅵ. OLAP 구축 시 실무 장애 요인 및 엔지니어링 대책

| 문제 상황 | 근본 원인 | 실무 엔지니어링 대책 | 개선 효과 |
|---|---|---|---|
| **큐브 빌드 배치 작업 타임아웃** | 차원 수 증가(10개 이상)로 인한 MOLAP 데이터 폭증 (Data Explosion) | 희소성(Sparsity) 제어, 필요 상위 차원만 선별 집계하는 **HOLAP 전환** | 배치 수행 시간 70% 단축 |
| **원천 데이터 변경 시 분석 지연** | 하루 1회 야간 배치로 큐브를 재생성하여 실시간 데이터 미반영 | **증분 큐브 빌드(Incremental Build)** 또는 실시간 스트리밍 레이어(Kafka+Flink) 연계 | 준실시간(Near Real-time) 분석 보장 |
| **대용량 팩트 테이블 풀스캔 병목** | ROLAP 환경에서 수십억 건 팩트 테이블 직접 쿼리 | **구체화 뷰(Materialized View)** 생성 및 파티션 프루닝, 컬럼형 인덱스 적용 | 팩트 조회 성능 10배 이상 향상 |
| **비즈니스 변경에 따른 스키마 경직성**| 레거시 큐브 구조 변경 시 모든 리포트 템플릿 손상 | 시맨틱 레이어(Semantic Layer, dbt Metric) 추상화로 물리 스토리지 결합도 분리 | 변경 민첩성 확보 |

#### 한줄 요약

- 큐브 폭증 억제, 구체화 뷰 활용, 시맨틱 레이어 도입이 안정적 OLAP 운영의 3대 요소임

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 전통적인 다차원 큐브(MOLAP)는 "모든 가능한 차원 조합을 미리 계산해 둔다"는 철학에 기반하므로, 차원이 10개만 넘어가도 계산해야 할 셀의 수가 수십억 개로 폭증하는 '큐브 폭증(Data Explosion)'과 밤샘 배치 작업의 늪에 빠진다. 이는 초 단위로 데이터가 유입되고 실시간 의사결정이 요구되는 현대 비즈니스 환경과 완전히 불일치한다.
>
> **[나라면 이렇게 쓴다]**
> 현대 모던 데이터 스택(MDS) 환경에서는 무거운 사전 집계 큐브를 전면 퇴출하고, 분산 컬럼 지향 쿼리 엔진(**ClickHouse, DuckDB, Snowflake**) 기반의 **'Zero-Cube Real-time OLAP 아키텍처'**를 구축하겠다. Parquet 포맷 기반의 SIMD 벡터화 연산과 데이터 스키핑 인덱스(Data Skipping Index)를 적용하여, 사전에 큐브를 깎아두지 않고도 원천 팩트 데이터에서 직접 수억 건의 다차원 집계를 수십 밀리초 내에 처리하는 온디맨드 분석 엔진을 설계하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: MOLAP의 사전 계산 큐브 폭증으로 인한 야간 배치 타임아웃 및 실시간 스트리밍 데이터 분석 불가.
- **대응 (개선 방안)**: 정적 큐브 제거 후 ClickHouse/Snowflake 기반 분산 컬럼 스토리지 및 벡터화 SIMD 연산 도입.
- **검증 (검증 기준)**: 수억 건 팩트 집계 쿼리 레이턴시 50ms 이내 유지 및 스토리지 공간 70% 압축 절감 검증.
- **효과 (실행 효과)**: 야간 배치 큐브 생성 부하 100% 제거 및 실시간 이벤트 스트리밍 즉시 다차원 분석 실현.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">현행 한계</div>
    <div class="itpe-flow-desc">차원 증가 시 큐브 폭증 및 배치 지연으로 실시간 분석 불가</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">개선 방안</div>
    <div class="itpe-flow-desc">Zero-Cube 지향 분산 컬럼 엔진 및 벡터화 온디맨드 쿼리 도입</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">검증 기준</div>
    <div class="itpe-flow-desc">수억 행 집계 50ms 이내 응답 및 스토리지 70% 압축 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">실행 효과</div>
    <div class="itpe-flow-desc">무거운 큐브 빌드 배치 폐지 및 스트리밍 즉시 대화형 분석 보장</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- 제122회 공식 문제지: 다차원 분석 및 ROLAP, MOLAP, HOLAP을 비교하여 설명하시오
- [The Data Warehouse Toolkit (Ralph Kimball & Margy Ross)](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-toolkit/)
- [Codd, E. F., et al. (1993). Providing OLAP to User-Analysts: An IT Mandate](https://en.wikipedia.org/wiki/Online_analytical_processing)

## 연결 토픽

- [스타 스키마](./137_star_schema/) · [데이터 레이크](./007_data_lake/) · [논리적 데이터웨어하우스(LDW)](./132_logical_data_warehouse/) · [BI(Business Intelligence)](./154_bi/)
