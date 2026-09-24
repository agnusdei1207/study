---
sidebar:
  order: 134
  label: "134. 빅데이터 분석도구 선택 원칙"
  badge:
    text: "기초"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 134
title: "빅데이터 분석도구 선정 원칙과 지연시간·데이터 규모 기반 의사결정 매트릭스"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "134"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>빅데이터·분석 아키텍처</span><strong>빅데이터 분석도구 선택 원칙</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Matrix Title -->
  <text x="260" y="25" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">지연시간(Latency) vs 데이터 규모(Volume) 2차원 선정 매트릭스</text>

  <!-- Axes -->
  <line x1="60" y1="240" x2="480" y2="240" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="60" y1="40" x2="60" y2="240" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="480" y="255" text-anchor="end" font-size="10" fill="#64748b">데이터 규모 (GB ──► TB ──► PB)</text>
  <text x="50" y="45" text-anchor="end" font-size="10" fill="#64748b">응답 지연</text>

  <!-- Top-Right: Realtime Large (Flink/Pinot) -->
  <rect x="280" y="50" width="190" height="55" rx="6" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
  <text x="375" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">Apache Flink / Pinot</text>
  <text x="375" y="86" text-anchor="middle" font-size="9" fill="#7f1d1d">실시간 스트리밍 &amp; 서브세컨드 OLAP</text>
  <text x="375" y="98" text-anchor="middle" font-size="8" fill="#64748b">초 단위 (ms) ┃ FDS, 실시간 대시보드</text>

  <!-- Middle-Right: Interactive Large (Trino/BigQuery) -->
  <rect x="280" y="115" width="190" height="55" rx="6" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="375" y="135" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">Trino / Snowflake / BigQuery</text>
  <text x="375" y="151" text-anchor="middle" font-size="9" fill="#1e3a8a">대화형 애드혹 SQL &amp; 클라우드 DW</text>
  <text x="375" y="163" text-anchor="middle" font-size="8" fill="#64748b">초~분 단위 ┃ 현업 BI 질의, 가상화</text>

  <!-- Bottom-Right: Batch Large (Spark Core) -->
  <rect x="280" y="180" width="190" height="55" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="375" y="200" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">Apache Spark / Hadoop</text>
  <text x="375" y="216" text-anchor="middle" font-size="9" fill="#78350f">대규모 배치 ETL &amp; 분산 머신러닝</text>
  <text x="375" y="228" text-anchor="middle" font-size="8" fill="#64748b">수 분~시간 단위 ┃ 대용량 정산, 학습</text>

  <!-- Left Side: Small Scale (Python/DuckDB) -->
  <rect x="75" y="140" width="180" height="85" rx="6" fill="#dcfce7" stroke="#10b981" stroke-width="1.5"/>
  <text x="165" y="165" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">Python (DuckDB / Polars)</text>
  <text x="165" y="185" text-anchor="middle" font-size="9" fill="#065f46">단일 노드 인메모리 고속 처리</text>
  <text x="165" y="202" text-anchor="middle" font-size="9" fill="#065f46">수십 GB 미만 ┃ 탐색적 EDA</text>
  <text x="165" y="217" text-anchor="middle" font-size="8" fill="#64748b">분산 오버헤드 없는 극강의 가성비</text>
</svg>
</div>

- 본질: **기업의 비즈니스 분석 목적, 데이터 특성(Volume, Velocity, Variety), 요구 지연시간(SLA), 조직의 엔지니어링 역량 및 총소유비용(TCO)을 종합적으로 평가하여, 특정 기술의 유행이나 벤더 종속에 휘둘리지 않고 최적의 분석 도구를 체계적으로 선별하는 공학적 의사결정 프레임워크**
- 암기: `목-성-역-비-생` (5대 선정 원칙: 목적 적합성, 성능 확장성, 역량 호환성, 비용 TCO, 생태계 성숙도) / `지-규-매` (의사결정 매트릭스: 지연시간 Latency vs 데이터 규모 Volume)
- 판단축:
  - **초저지연 스트리밍 (ms~sec)**: Apache Flink, Kafka Streams, ClickHouse
  - **대화형 애드혹 SQL (sec~min)**: Trino, Snowflake, Google BigQuery
  - **대규모 중량급 배치 (min~hour)**: Apache Spark Core, AWS EMR
  - **소규모 고속 분석 (<100GB)**: 단일 노드 DuckDB, Polars, Python Pandas
- 주의: 데이터 크기가 수십 GB 미만인데 유행을 따라 하둡이나 스파크 분산 클러스터를 띄우면, JVM 기동 및 네트워크 셔플 오버헤드로 인해 단일 노드 DuckDB보다 오히려 10배 더 느리고 비용만 낭비되는 전형적인 '오버엔지니어링' 함정에 빠짐
---

## 1교시 예상문제 (10점)

> 빅데이터 분석도구 선정 원칙과 지연시간·데이터 규모 기반 의사결정 매트릭스의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 비즈니스 목적, 데이터 특성(Volume, Velocity, Variety), SLA, 조직 역량, TCO를 종합 고려하여 최적의 분석 도구를 선별하는 프레임워크 |
| **2. 5대 선정 원칙** | - **목적 적합성**: 배치 vs 스트림 vs 대화형<br/>- **성능/확장성**: 선형 스케일아웃<br/>- **조직 역량**: SQL/Python 스킬셋<br/>- **TCO 최적화**: 인프라/운영비 절감<br/>- **생태계**: 벤더 락인 방지 |
| **3. 의사결정 매트릭스** | - 실시간 초저지연: Flink / Pinot<br/>- 대화형 애드혹 SQL: Trino / Snowflake<br/>- 대규모 배치/ML: Apache Spark<br/>- 소규모 고속 분석: DuckDB / Polars |
| **4. 핵심 주의점** | 100GB 미만 소규모 데이터에 분산 엔진(Hadoop/Spark) 도입 시 발생하는 오버엔지니어링 회피 |
---

### 핵심 관계

| 비교 항목 | Apache Spark | Apache Flink | Trino (Presto) | Snowflake / BigQuery |
|:---|:---|:---|:---|:---|
| **처리 패러다임** | 마이크로 배치 및 대용량 배치 | **진정한 이벤트 단위 스트리밍** | **인메모리 분산 SQL 쿼리** | 완전관리형 서버리스 클라우드 DW |
| **주요 활용 목적** | **대규모 배치 ETL, 분산 ML** | **실시간 FDS, 이벤트 CEP** | **대화형 애드혹 BI 분석, 가상화** | 엔터프라이즈 전사 EDW 및 공유 |
| **지연시간 (Latency)** | 수 초 ~ 수 시간 | **수 밀리초(ms) ~ 수 초** | **수백 ms ~ 수십 초** | 수 초 ~ 수 분 |
| **저장소 의존성** | 자체 스토리지 없음 (HDFS/S3) | 자체 스토리지 없음 (Kafka) | **자체 스토리지 없음 (커넥터 연합)** | 완전 분리형 독점/오픈 스토리지 |
| **장애 복구(FT)** | RDD 계보(Lineage) 재연산 | 비동기 분산 체크포인트(Chandy-Lamport) | 실패 시 쿼리 재실행 | 벤더 클라우드 자동 투명 복구 |
| **운영 난이도** | 중간 (메모리 튜닝 필요) | 높음 (상태 백엔드 RocksDB 관리) | 중간 (코디네이터 노드 관리) | **극히 낮음 (서버리스 관리형)** |

---

## 2~4교시 예상문제 (25점)

> 빅데이터 분석 환경 구축 시 분석 도구(분산 처리 엔진, 대화형 질의 엔진, 분석 툴)를 선정하기 위한 5대 평가 기준을 제시하고, 처리 속도(지연시간) 및 데이터 규모 관점에서의 도구 선정 매트릭스와 TCO 최적화 방안을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 기술 유행을 극복하는 빅데이터 분석도구 선정 개요

#### 한줄 요약: 데이터의 양과 속도, 조직 역량 및 TCO를 정량 평가하여 비즈니스 가치를 극대화하는 최적 도구 선별 체계

- **배경**:
  - 오픈소스와 클라우드 기반 빅데이터 도구가 수백 종으로 난립하면서, 명확한 기준 없이 도입했다가 클라우드 비용 폭증과 운영 역량 부족으로 방치되는 프로젝트 속출
  - "하나의 만능 도구로 모든 분석을 처리할 수 있다"는 환상에서 벗어나, 업무 영역별 최적 도구를 조합하는 실용적 아키텍처 필요
- **정의**: 비즈니스 요구사항을 충족하는 최소 비용-최대 성능의 도구를 도출하기 위해 지연시간, 데이터 볼륨, 연산 복잡도, 유지보수성을 다면 평가하는 공학적 선정 방법론

### Ⅱ. 빅데이터 분석도구 선정을 위한 5대 공학적 평가 원칙

#### 한줄 요약: 목적 적합성, 성능 및 확장성, 조직 역량 호환성, TCO 비용 최적화, 생태계 성숙도

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="10" y="20" width="94" height="120" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="57" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">1. 목적 적합성</text>
  <text x="57" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">Fitness</text>
  <text x="57" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">배치 vs 실시간</text>
  <text x="57" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">정형 vs 비정형</text>
  <text x="57" y="128" text-anchor="middle" font-size="8" fill="#64748b">SLA 지연시간 충족</text>

  <!-- Box 2 -->
  <rect x="112" y="20" width="94" height="120" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="159" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#0284c7">2. 성능·확장성</text>
  <text x="159" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">Scalability</text>
  <text x="159" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">선형 스케일아웃</text>
  <text x="159" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">인메모리 셔플</text>
  <text x="159" y="128" text-anchor="middle" font-size="8" fill="#64748b">페타바이트 수용</text>

  <!-- Box 3 -->
  <rect x="214" y="20" width="94" height="120" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="261" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#059669">3. 조직 역량</text>
  <text x="261" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">Capability</text>
  <text x="261" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">팀 기술 스택</text>
  <text x="261" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">SQL / Python 친화</text>
  <text x="261" y="128" text-anchor="middle" font-size="8" fill="#64748b">학습 곡선 최소화</text>

  <!-- Box 4 -->
  <rect x="316" y="20" width="94" height="120" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="363" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">4. TCO 최적화</text>
  <text x="363" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">Cost</text>
  <text x="363" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">인프라+라이선스</text>
  <text x="363" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">운영 인건비</text>
  <text x="363" y="128" text-anchor="middle" font-size="8" fill="#64748b">서버리스 비용 제어</text>

  <!-- Box 5 -->
  <rect x="418" y="20" width="92" height="120" rx="6" fill="#8b5cf6" fill-opacity="0.1" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="464" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">5. 생태계·종속</text>
  <text x="464" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">Lock-in 방지</text>
  <text x="464" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">오픈소스 커뮤니티</text>
  <text x="464" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">클라우드 이식성</text>
  <text x="464" y="128" text-anchor="middle" font-size="8" fill="#64748b">오픈 포맷 준수</text>
</svg>
</div>

1. **목적 적합성 (Fitness for Purpose)**: 비즈니스가 요구하는 질의 응답 시간(SLA)이 초 단위 실시간인지, 야간 배치 집계인지, 복잡한 ML 추론인지에 따라 엔진 분기
2. **성능 및 확장성 (Scalability & Performance)**: 노드 증설에 따라 처리량이 선형적으로 증가하는지, 메모리 부족(OOM) 시 디스크 스필(Spill)을 안정적으로 지원하는지 평가
3. **조직 역량 및 학습 곡선 (Team Capability & Learning Curve)**: 현업 분석가와 엔지니어가 보유한 스킬셋(SQL, Python, Java/Scala)과의 호환성 검토
4. **TCO (Total Cost of Ownership) 관점의 비용 효율성**: 상용 라이선스뿐만 아니라 클러스터 인프라 비용, 네트워크 아웃바운드 비용, 모니터링 및 운영 인건비 총합 산정
5. **생태계 성숙도 및 벤더 종속성(Lock-in) 배제**: 특정 클라우드 벤더의 독점 기술에 갇히지 않도록 Apache Iceberg 등 오픈 표준 테이블 포맷을 지원하는지 확인

### Ⅲ. 주요 빅데이터 분석 엔진 상세 비교

#### 한줄 요약: 연산 방식과 주력 활용 목적에 따른 스파크, 플링크, 트리노, 클라우드 DW 비교

| 비교 항목 | Apache Spark | Apache Flink | Trino (Presto) | Snowflake / BigQuery |
|:---|:---|:---|:---|:---|
| **처리 패러다임** | 마이크로 배치 및 대용량 배치 | **진정한 이벤트 단위 스트리밍** | **인메모리 분산 SQL 쿼리** | 완전관리형 서버리스 클라우드 DW |
| **주요 활용 목적** | **대규모 배치 ETL, 분산 ML** | **실시간 FDS, 이벤트 CEP** | **대화형 애드혹 BI 분석, 가상화** | 엔터프라이즈 전사 EDW 및 공유 |
| **지연시간 (Latency)** | 수 초 ~ 수 시간 | **수 밀리초(ms) ~ 수 초** | **수백 ms ~ 수십 초** | 수 초 ~ 수 분 |
| **저장소 의존성** | 자체 스토리지 없음 (HDFS/S3) | 자체 스토리지 없음 (Kafka) | **자체 스토리지 없음 (커넥터 연합)** | 완전 분리형 독점/오픈 스토리지 |
| **장애 복구(FT)** | RDD 계보(Lineage) 재연산 | 비동기 분산 체크포인트(Chandy-Lamport) | 실패 시 쿼리 재실행 | 벤더 클라우드 자동 투명 복구 |
| **운영 난이도** | 중간 (메모리 튜닝 필요) | 높음 (상태 백엔드 RocksDB 관리) | 중간 (코디네이터 노드 관리) | **극히 낮음 (서버리스 관리형)** |

### Ⅳ. 분석도구 도입 절차 및 PoC 벤치마크 프레임워크

#### 한줄 요약: 요구사항 정의 $\rightarrow$ 숏리스트 선별 $\rightarrow$ 실측 PoC 벤치마크 $\rightarrow$ TCO 시뮬레이션 $\rightarrow$ 최종 확정

1. **1단계: 요구사항 정량화**: 데이터 일일 인입량, P95 응답시간 목표, 동시 쿼리 사용자 수, 최대 허용 월 예산 명문화
2. **2단계: 숏리스트 도출**: 5대 평가 원칙에 따라 상위 2~3개 후보 엔진 선정 (예: Trino vs Snowflake)
3. **3단계: 실데이터 기반 PoC 벤치마크**:
   - TPC-DS 표준 쿼리셋 및 자사 실제 고비용 집계 쿼리를 대상으로 처리량(Throughput) 및 지연시간(Latency) 실측
   - 부하 테스트(동시 접속 100명) 환경에서의 CPU/메모리 병목 및 스케일아웃 반응 속도 측정
4. **4단계: 3개년 TCO 시뮬레이션**: 인프라 비용 + 쿼리 스캔 비용 + 운영 엔지니어 유지보수 비용 산출
5. **5단계: 아키텍처 확정 및 거버넌스 수립**: 단일 만능주의를 지양하고 배치/스트림/대화형의 다계층 조합 확정

### Ⅴ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 오버엔지니어링 탈피, 클라우드 쿼리 스캔 과금 폭탄 방지, 스킬셋 미스매치 극복

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **소규모 데이터(10GB)에 Spark 클러스터 도입 후 성능 저하** | 클러스터 분산 코디네이션 및 JVM 기동 오버헤드가 실제 연산 시간보다 큼 | 단일 서버용 초고속 컬럼형 엔진인 **DuckDB** 또는 **Polars**로 전면 단순화 |
| **BigQuery/Athena 무제한 쿼리로 수천만 원 과금 폭탄** | 파티션 필터링 없이 수십 TB 테이블을 매번 풀스캔하는 비효율 쿼리 남발 | 날짜 파티셔닝 강제화, 쿼리당 스캔 용량 바이트 상한 설정 및 Trino 캐싱 계층 배치 |
| **조직 스킬셋 불일치로 플랫폼 방치** | SQL 중심 조직에 스칼라(Scala) 기반 분산 스트리밍 프레임워크 억지 도입 | **Flink SQL** 또는 **dbt-Trino** 등 표준 ANSI SQL 인터페이스 환경으로 통합 제공 |

### Ⅵ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 빅데이터 엔지니어링에서 가장 부끄러운 실패는 "기술적으로 너무 앞선 도구를 골라서 망하는 것"이다.
> 데이터가 기껏해야 하루 수십만 건 들어오는데 하둡과 스파크 클러스터를 띄워놓고 엔지니어 세 명이 클러스터 장애 대응에 매달려 있다면, 그것은 완벽한 리소스 낭비다.
> 진정한 기술사의 역량은 화려한 오픈소스 기술 스택을 자랑하는 것이 아니라, **"DuckDB 하나로 해결할 수 있는 문제를 수억 원짜리 분산 클러스터로 키우지 않는 용기"**에 있다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "현대 모던 데이터 스택(MDS)에서의 서버리스(Serverless) 우선주의"를 제언하겠다. 초기 스타트업 및 파일럿 단계에서는 클라우드 서버리스 엔진(Snowflake, BigQuery, DuckDB)으로 인프라 관리 부담을 제로화하여 비즈니스 가치를 검증하고, 데이터가 페타바이트급으로 폭증하고 쿼리 비용이 역전되는 시점에 오픈소스 자립형 엔진(Trino + Iceberg)으로 전환하는 '단계적 도구 전환 로드맵'을 수립하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 빅데이터 분석 플랫폼의 TCO 낭비를 방지하고 엔지니어링 효율을 극대화하기 위해 다차원 평가 매트릭스 기반의 도구 선정이 필수적임.
- **대응**:
  1. **지연시간-데이터 규모 분기**: 초 단위 실시간은 Flink, 대화형 BI는 Trino, 대규모 배치는 Spark로 관심사 명확 분리.
  2. **오버엔지니어링 방지 가드레일**: 100GB 미만 분석 작업은 DuckDB/Polars를 우선 적용하여 분산 오버헤드 원천 제거.
  3. **SQL 중심 인터페이스 통일**: 조직 전반의 학습 비용을 줄이기 위해 모든 분석 엔진에 ANSI SQL 인터페이스 레이어 구축.
- **검증**: 실데이터 기반 TPC-DS 벤치마크 수행 및 3개년 TCO 시뮬레이션을 통한 비용 대비 성능 50% 개선 검증.
- **효과**: 클라우드 인프라 비용 절감, 데이터 파이프라인 장애율 80% 감소 및 셀프서비스 분석 민첩성 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">기술 유행 추종, 소규모 데이터 분산 오버엔지니어링, TCO 폭증</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">지연시간·볼륨 매트릭스 기반 도구 선별, 실측 PoC 벤치마크</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">TPC-DS 벤치마크 통과, 3개년 TCO 절감률 &gt; 40%, SLA 준수</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">비용 효율적인 목적 특화형 빅데이터 분석 생태계 확립</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제126회 정보관리 2교시: 빅데이터 분석 환경 구축 시 분석 도구(소프트웨어/플랫폼)의 선정 기준 및 고려사항
- **검증 출처**:
  - Nathan Marz & James Warren, "Big Data: Principles and best practices of scalable realtime data systems", Manning
  - Kleppmann, Martin, "Designing Data-Intensive Applications", O'Reilly
---

## 연결 토픽

- 상위 토픽: [03-112 빅데이터](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/112_big_data.md)
- 연관 토픽: [03-135 빅데이터 플랫폼 아키텍처](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/135_big_data_platform_architecture.md), [03-116 ELK 스택](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/116_elk_stack.md)
