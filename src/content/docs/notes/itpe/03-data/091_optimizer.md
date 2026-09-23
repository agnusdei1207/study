---
sidebar:
  order: 91
  label: "091. 옵티마이저 (RBO·CBO)"
  badge:
    text: "A"
    variant: note
title: "데이터베이스 옵티마이저(Optimizer) 아키텍처 및 RBO와 CBO 비교 분석"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 91
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "091"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터베이스 튜닝·최적화</span><strong>옵티마이저 (RBO·CBO)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" role="img" aria-label="데이터베이스 옵티마이저 엔진 5단계 최적화 파이프라인">
  <defs>
    <marker id="optArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="220" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Row 1: SQL -> Parser -> Transformer -->
  <rect x="20" y="20" width="110" height="55" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
  <text x="75" y="42" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">사용자 질의</text>
  <text x="75" y="60" text-anchor="middle" font-size="9.5" fill="var(--sl-color-gray-2, #64748b)">선언적 SQL 문</text>

  <path d="M 130 47 L 150 47" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#optArr)"/>

  <rect x="155" y="20" width="160" height="55" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.2"/>
  <text x="235" y="42" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">1. 질의 파서 (Parser)</text>
  <text x="235" y="60" text-anchor="middle" font-size="9.5" fill="var(--sl-color-text, #334155)">Syntax / Semantic 검사</text>

  <path d="M 315 47 L 335 47" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#optArr)"/>

  <rect x="340" y="20" width="160" height="55" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.2"/>
  <text x="420" y="42" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">2. 질의 변환기 (Trans)</text>
  <text x="420" y="60" text-anchor="middle" font-size="9.5" fill="var(--sl-color-text, #334155)">뷰 머징·서브쿼리 언네스팅</text>

  <!-- Flow down to Row 2 -->
  <path d="M 420 75 L 420 95 L 420 110" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#optArr)"/>

  <!-- Row 2: Code Gen <- Cost Estimator <- Plan Gen -->
  <rect x="340" y="115" width="160" height="55" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.2"/>
  <text x="420" y="137" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">3. 대안 생성기 (Plan Gen)</text>
  <text x="420" y="155" text-anchor="middle" font-size="9.5" fill="var(--sl-color-text, #334155)">접근경로·조인기법 조합</text>

  <path d="M 340 142 L 320 142" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#optArr)"/>

  <rect x="155" y="105" width="160" height="75" rx="6" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="235" y="127" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #1e40af)">4. 비용 산정기 (Cost)</text>
  <text x="235" y="145" text-anchor="middle" font-size="9.5" fill="var(--sl-color-text, #1e293b)">선택도·카디널리티 계산</text>
  <text x="235" y="162" text-anchor="middle" font-size="9" fill="var(--sl-color-accent, #2563eb)">통계정보(CBO Data Dict)</text>

  <path d="M 155 142 L 135 142" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#optArr)"/>

  <rect x="20" y="115" width="110" height="55" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.2"/>
  <text x="75" y="137" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">5. 계획 생성기</text>
  <text x="75" y="155" text-anchor="middle" font-size="9.5" fill="var(--sl-color-text, #334155)">최저 비용 플랜 채택</text>

  <!-- Output: Execution Plan -->
  <text x="260" y="205" text-anchor="middle" font-size="10" font-weight="600" fill="var(--sl-color-text, #0f172a)">결과: 최적 실행 계획(Execution Plan) $\rightarrow$ SQL 실행 엔진(Row-source Engine)</text>
</svg>
</div>

- 본질: **사용자가 제출한 비절차적(Declarative) SQL 문을 해석하여 최소의 디스크 I/O와 CPU 연산 비용으로 최단 시간에 결과를 반환하도록 데이터 접근 경로(Access Path)와 조인 알고리즘을 결정하고 최적의 실행 계획(Execution Plan)을 수립하는 DBMS 핵심 연산 엔진**
- 암기: `파-변-대-비-생` (파서, 변환기, 대안생성기, 비용산정기, 생성기) / `선-카-비` (선택도, 카디널리티, 비용 계산)
- 판단축:
  - **RBO(규칙 기반)**: 15개 고정 규칙 순위표 기반 경로 선정, 통계정보 불필요하나 데이터 분포 무시로 비효율 극심
  - **CBO(비용 기반)**: 데이터 딕셔너리 통계(테이블 블록 수, Distinct 수, 히스토그램)를 기반으로 I/O 및 CPU 예상 비용을 계산하여 최저 비용 경로 선택
  - **적응형 최적화(Adaptive)**: 런타임 통계 피드백(Cardinality Feedback)을 통해 실행 도중 플랜을 동적 전환
- 주의: CBO 환경에서 통계정보가 오래되거나 바인드 변수의 편향(Skewed Data)으로 인해 '바인드 피킹(Bind Peeking)' 왜곡이 발생하면 최악의 풀스캔(FTS) 플랜이 캐시될 위험이 존재함
---

## 1교시 예상문제 (10점)

> 데이터베이스 옵티마이저(Optimizer) 아키텍처 및 RBO와 CBO 비교 분석의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### [문제] 옵티마이저 (Optimizer)

#### 1. 옵티마이저(Optimizer)의 정의
- 사용자가 제출한 비절차적 SQL을 해석하여 최소 비용(I/O, CPU)으로 최단 시간 내 결과를 반환하도록 최적의 실행 계획(Execution Plan)을 생성하는 DBMS 핵심 엔진

#### 2. 옵티마이저 5단계 아키텍처 및 CBO/RBO 비교

| 최적화 단계 | 주요 역할 | 산출물 |
|:---|:---|:---|
| **1. 구문 분석 (Parser)** | 문법(Syntax) 및 의미(Semantic) 검사 | 파스 트리 (Parse Tree) |
| **2. 질의 변환 (Transformer)** | 뷰 머징, 서브쿼리 언네스팅 등 쿼리 재작성 | 변환된 내부 SQL |
| **3. 대안 생성 (Plan Gen)** | 인덱스 스캔, 조인 순서 및 기법(NL/Hash) 조합 | 후보 실행 계획군 |
| **4. 비용 산정 (Estimator)** | 딕셔너리 통계 기반 선택도·카디널리티·비용 계산 | 각 후보별 Cost 수치 |
| **5. 계획 생성 (Code Gen)** | 최저 비용 플랜 확정 및 바이너리 트리 생성 | 최종 Execution Plan |

- **RBO vs CBO 핵심 비교**: RBO는 15개 고정 순위(ROWID 1위, FTS 15위) 기반으로 데이터 분포를 무시하나, CBO는 딕셔너리 통계 기반으로 I/O 및 CPU 예상 비용을 수치화하여 최적 플랜을 동적 결정

#### 3. 최신 동향: 적응형 쿼리 최적화 (Adaptive Optimization)
- 런타임 실행 통계를 실시간 피드백받아 NL 조인에서 Hash 조인으로 동적 전환하여 플랜 왜곡 방지
---

### 핵심 관계

| 최적화 단계 | 구성 모듈 | 핵심 역할 및 수행 메커니즘 |
|:---|:---|:---|
| **1. 구문 분석 (Parsing)** | **Query Parser** | SQL 문법 검사(Syntax), 테이블·컬럼 실존 여부 및 접근 권한 검사(Semantic), SQL 해시값 생성 및 라이브러리 캐시 검색 |
| **2. 질의 변환 (Transformation)** | **Query Transformer** | 의미적으로 동일하지만 더 효율적인 내부 SQL로 재작성 (서브쿼리 Unnesting, 뷰 머징(View Merging), 조건절 푸시다운) |
| **3. 대안 생성 (Plan Generation)** | **Plan Generator** | 인덱스 스캔(Unique, Range, Full) 및 풀 테이블 스캔, 조인 순서(Driving/Driven)와 조인 기법(NL, SMJ, Hash Join) 후보 조합 생성 |
| **4. 비용 산정 (Cost Estimation)** | **Cost Estimator** | 딕셔너리 통계(카디널리티, 컬럼 히스토그램, 클러스터링 팩터)를 바탕으로 각 후보 플랜의 디스크 I/O 블록 수 및 CPU 연산 시간 산정 |
| **5. 계획 생성 (Code Generation)** | **Code Generator** | 가장 낮은 비용으로 평가된 후보를 최종 채택하여 실행 엔진이 처리할 수 있는 형태의 Row-source 트리(실행 계획)로 변환 |

---

## 2~4교시 예상문제 (25점)

> 데이터베이스 옵티마이저(Optimizer)의 아키텍처와 주요 구성요소 및 최적화 5단계 과정을 설명하고, 규칙 기반 옵티마이저(RBO)와 비용 기반 옵티마이저(CBO)의 메커니즘 차이점과 RBO의 한계점을 제시하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 선언적 언어를 절차적 실행으로 변환하는 옵티마이저 개요

#### 한줄 요약: SQL 질의를 물리적 블록 접근 알고리즘으로 매핑하여 최소 자원 소모의 실행 계획을 생성하는 데이터베이스 내부 최적화 두뇌

- **배경**: 관계형 데이터베이스(RDBMS)의 SQL은 '어떤 데이터(What)'를 얻을지만 기술하는 선언적 언어이므로, '어떻게(How)' 가져올 것인가는 DBMS 내부 엔진이 스스로 판단해야 함
- **정의**: SQL 구문을 수신하여 문법·의미를 분석하고, 다양한 접근 경로와 조인 방식 중 가장 적은 비용(Cost)이 소요되는 실행 계획(Execution Plan)을 생성하는 소프트웨어 서브시스템
- **진화 과정**: RBO(고정 규칙, Oracle 9i 이전) $\rightarrow$ CBO(통계 기반 비용 계산, 현대 표준) $\rightarrow$ Adaptive Query Optimization(실행 시점 동적 보정, 최신 트렌드)

### Ⅱ. 옵티마이저 내부 아키텍처 및 최적화 5단계 과정

#### 한줄 요약: 파싱 $\rightarrow$ 질의 변환 $\rightarrow$ 플랜 생성 $\rightarrow$ 비용 산정 $\rightarrow$ 코드 생성의 정밀 파이프라인

| 최적화 단계 | 구성 모듈 | 핵심 역할 및 수행 메커니즘 |
|:---|:---|:---|
| **1. 구문 분석 (Parsing)** | **Query Parser** | SQL 문법 검사(Syntax), 테이블·컬럼 실존 여부 및 접근 권한 검사(Semantic), SQL 해시값 생성 및 라이브러리 캐시 검색 |
| **2. 질의 변환 (Transformation)** | **Query Transformer** | 의미적으로 동일하지만 더 효율적인 내부 SQL로 재작성 (서브쿼리 Unnesting, 뷰 머징(View Merging), 조건절 푸시다운) |
| **3. 대안 생성 (Plan Generation)** | **Plan Generator** | 인덱스 스캔(Unique, Range, Full) 및 풀 테이블 스캔, 조인 순서(Driving/Driven)와 조인 기법(NL, SMJ, Hash Join) 후보 조합 생성 |
| **4. 비용 산정 (Cost Estimation)** | **Cost Estimator** | 딕셔너리 통계(카디널리티, 컬럼 히스토그램, 클러스터링 팩터)를 바탕으로 각 후보 플랜의 디스크 I/O 블록 수 및 CPU 연산 시간 산정 |
| **5. 계획 생성 (Code Generation)** | **Code Generator** | 가장 낮은 비용으로 평가된 후보를 최종 채택하여 실행 엔진이 처리할 수 있는 형태의 Row-source 트리(실행 계획)로 변환 |

### Ⅲ. RBO와 CBO 비교 분석

#### 한줄 요약: 하드코딩된 15개 규칙 우선순위를 따르는 RBO와 통계 정보 기반 실제 자원 비용을 계산하는 CBO의 대조

| 비교 항목 | 규칙 기반 옵티마이저 (RBO) | 비용 기반 옵티마이저 (CBO) |
|:---|:---|:---|
| **최적화 기준** | 사전 정의된 15개 고정 규칙 우선순위 (Rank) | 예상되는 시스템 자원 소모량(I/O, CPU, 메모리) 총합 비용 |
| **통계 정보** | 전혀 사용하지 않음 (수집 불필요) | 필수적 (테이블 건수, 블록 수, 히스토그램, 시스템 통계) |
| **주요 결정 요인** | 연산자 형태, 인덱스 유무, FROM/WHERE절 기술 순서 | 데이터 선택도(Selectivity), 카디널리티(Cardinality), 비용(Cost) |
| **인덱스 스캔 판단** | 인덱스가 존재하면 데이터의 99%를 조회해도 인덱스 사용 | 손익분기점(약 10~15%) 초과 시 Full Table Scan 채택 |
| **조인 순서 결정** | FROM절의 가장 우측 테이블을 Driving 테이블로 선택 | 카디널리티가 작은 테이블을 탐색하여 최적 드라이빙 선정 |
| **개발자 의존도** | 극도로 높음 (개발자가 규칙을 고려하여 SQL을 튜닝) | 상대적으로 낮음 (옵티마이저가 지능적 판단, 필요시 힌트 활용) |
| **현대 DBMS 지원** | 공식 폐기(Deprecated) 또는 레거시 유지 | 모든 현대 RDBMS의 표준 기본 엔진 |

### Ⅳ. CBO의 핵심 수학적 모델: 선택도, 카디널리티, 비용 계산

#### 한줄 요약: 선택도(Selectivity)에서 시작하여 카디널리티(Cardinality)를 거쳐 I/O와 CPU를 결합한 총 비용(Cost) 도출

### 1. 선택도 (Selectivity)
- 조건절을 만족하는 행의 비율 ($0 \le Selectivity \le 1$)
- 컬럼 히스토그램이 없는 등치 조건 ($col = val$):
  $$Selectivity = \frac{1}{NDV(Number\ of\ Distinct\ Values)}$$
- 부등호 조건 ($col \ge val$):
  $$Selectivity = \frac{Max - val}{Max - Min}$$

### 2. 카디널리티 (Cardinality)
- 조건절을 적용한 후 결과 집합으로 반환될 것으로 예상되는 행(Row)의 수:
  $$Cardinality = Total\ Rows \times Selectivity$$

### 3. 총 비용 (Cost) 산출 모델
- 오라클/PostgreSQL 표준 CBO 비용 함수:
  $$Cost = (Single\ Block\ Read \times Single\_Time) + (Multi\ Block\ Read \times Multi\_Time) + \frac{CPU\ Cycles}{CPU\_Frequency}$$
- 클러스터링 팩터(Clustering Factor)가 우수할수록 Single Block I/O 비용이 대폭 감소함

### Ⅴ. RBO의 15개 우선순위 규칙 및 구조적 한계점

#### 한줄 요약: 인덱스의 존재만을 절대선으로 여기는 RBO의 15계층 순위와 치명적 병목 원인

| 순위 (Rank) | RBO 접근 경로 (Access Path) 규칙 |
|:---:|:---|
| **Rank 1** | Single Row by ROWID (디스크 물리 주소 직접 접근) |
| **Rank 2** | Single Row by Cluster Join |
| **Rank 3** | Single Row by Hash Cluster Key with Unique or PK |
| **Rank 4** | Single Row by Unique or Primary Key |
| **Rank 5** | Cluster Join |
| **Rank 6** | Hash Cluster Key |
| **Rank 7** | Indexed Cluster Key |
| **Rank 8** | Composite Index Scan (결합 인덱스) |
| **Rank 9** | Single Column Index Scan (단일 컬럼 인덱스) |
| **Rank 10** | Bounded Range Search on Indexed Columns (`BETWEEN`, `LIKE 'A%'`) |
| **Rank 11** | Unbounded Range Search on Indexed Columns (`>`, `>=`) |
| **Rank 12~14** | Sort Merge Join, MAX/MIN on Index, ORDER BY on Index |
| **Rank 15** | **Full Table Scan** (가장 낮은 최후 순위) |

- **RBO의 3대 치명적 한계**:
  1. **데이터 편향 무시**: 1,000만 건 중 999만 건이 'Y'인 플래그 컬럼이라도 인덱스가 있으면 무조건 인덱스를 타서 999만 번의 Random Single I/O 유발
  2. **코딩 순서 종속성**: WHERE절에 동등 순위의 조건이 여러 개 있을 경우, 나중에 기술된 조건을 우선 평가하여 플랜이 뒤바뀜
  3. **신기술 수용 불가**: 해시 조인(Hash Join), 비트맵 인덱스, 파티션 프루닝 등 비용 기반 메커니즘을 지원할 수 없음

### Ⅵ. 실무 최적화 장애 요인 및 극복 방안 (Troubleshooting)

#### 한줄 요약: 바인드 피킹 왜곡, 통계정보 부재, 힌트 남발로 인한 장애를 해결하는 실무 지침

| 장애 현상 | 발생 원인 | 기술적 해결 방안 |
|:---|:---|:---|
| **바인드 피킹 (Bind Peeking) 왜곡** | 최초 하드 파싱 시 입력된 바인드 변수 값에만 최적화된 플랜이 캐시되어 이후 다른 값 조회 시 성능 급락 | ACS(Adaptive Cursor Sharing) 활성화, 쿼리 분리(`CASE`문 분기), 리터럴 치환 |
| **통계 정보 노후화로 인한 풀스캔** | 대량 배치 적재 후 통계 갱신이 누락되어 과거 작은 카디널리티 기준으로 잘못된 Nested Loops Join 선택 | DBMS_STATS 자동 수집 잡 스케줄링, 변경 임계치(Stale 10%) 감지 수집 |
| **힌트(Hint) 남발 및 플랜 고착** | 임시방편으로 인덱스 힌트를 강제(`/*+ INDEX(...) */`)하여 향후 데이터가 급증해도 인덱스 스캔 고정 | 힌트 격리, SPM(SQL Plan Management) 및 SQL 베이스라인을 통한 안정적 플랜 캡처 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 옵티마이저는 완벽한 전지전능의 존재가 아니다. CBO는 단지 데이터 딕셔너리에 등록된 통계 정보를 기반으로 수학적 확률(선택도, 카디널리티)을 계산하는 시뮬레이터일 뿐이다. 통계 정보가 왜곡되어 있거나 바인드 변수가 극단적 편향값을 가질 때(Bind Peeking) 옵티마이저는 최악의 결정을 내린다. 현대 DBMS는 이러한 정적 한계를 극복하기 위해 실행 중에 플랜을 자가 치유하는 '적응형 쿼리 최적화(Adaptive Optimization)'로 진화하고 있다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 5단계 파이프라인(파-변-대-비-생)과 CBO 핵심 공식(선택도, 카디널리티, 비용)을 컴팩트하게 제시하겠다. 2교시 25점형이라면 RBO의 한계점과 CBO 수학적 메커니즘을 상호 비교한 뒤, 실무에서 빈번한 바인드 피킹 장애 해결책(ACS, SPM)과 런타임에 NL 조인과 Hash 조인을 동적 전환하는 Adaptive Query Optimization 메커니즘을 제언에 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 정적 CBO는 쿼리 컴파일 시점의 추정치에 의존하므로, 복합 조건 간 상관관계(Correlated Columns) 누락이나 편향 데이터 유입 시 실제 카디널리티와 수천 배 오차가 발생하여 시스템 행(Hang) 장애 유발.
- **대응 (개선 방안)**: DBMS 12c/19c 이상의 적응형 플랜(Adaptive Plans)을 활성화하여 런타임 버퍼 누적치가 임계치를 초과할 경우 NL 조인에서 Hash 조인으로 자동 전환하고, 확장 통계(Extended Statistics) 및 다중 컬럼 히스토그램 구축.
- **검증 (검증 기준)**: SPM(SQL Plan Management)을 통한 플랜 변동성 0% 통제, 통계정보 Stale 비율 10% 이하 자동 수집 주기 준수, 핵심 배치 SQL 비용 변동 모니터링.
- **효과 (실행 효과)**: 예기치 않은 실행계획 변경에 따른 운영 장애 90% 예방, DBA 수동 힌트 튜닝 공수 60% 절감, 시스템 처리량 안정화.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">정적 통계 오차 및 바인드 피킹 왜곡으로 인한 실행계획 급변 장애</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">적응형 쿼리 플랜(Adaptive Plans) 도입 및 다중 컬럼 확장 통계 적용</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">SPM 플랜 고정률 100%, Stale 통계 10% 미만 유지, ACS 커서 공유 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">플랜 왜곡 장애 90% 감축, 수작업 힌트 공수 절감, 처리 성능 안정화</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제127회 정보관리 2교시: 데이터베이스 옵티마이저(Optimizer)의 역할과 주요 구성요소 및 최적화 과정, RBO와 CBO 비교
  - 제81회, 105회 기출
- **검증 출처**:
  - Oracle Database Concepts & SQL Tuning Guide (19c/23ai Optimizer Architecture)
  - 조시형, "친절한 SQL 튜닝", 디비안
---

## 연결 토픽

- 상위 토픽: [088. 데이터베이스 튜닝 (Database Tuning)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/088_database_tuning.md)
- 연관 토픽: [047. 인덱스 (Index)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index.md), [098. 정적 SQL vs 동적 SQL](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/098_dynamic_sql.md)
