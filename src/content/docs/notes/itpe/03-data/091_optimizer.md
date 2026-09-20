---
sidebar:
  order: 91
  label: "091. 옵티마이저 (RBO·CBO)"
  badge:
    text: "B"
    variant: note
title: "데이터베이스 옵티마이저(Optimizer) 아키텍처 및 RBO와 CBO 비교 분석"
author: "OpenAI Codex"
date: "2026-09-20T18:05:00+09:00"
tags:
  - "notes-data"
weight: 91
extra:
  model: "GPT-5"
  keyword_grade: "B"
  question_no: "091"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터베이스 튜닝·최적화</span><strong>옵티마이저 (RBO·CBO)</strong></div>

## 큰 그림과 30초 인출

```text
[데이터베이스 옵티마이저(Optimizer) 엔진 아키텍처 및 처리 흐름]

       [ 사용자 질의 (SQL) ]
                 │
                 ▼
 ┌───────────────────────────────┐
 │ 1. 질의 파서 (Query Parser)   │ : Syntax(문법) / Semantic(의미) 검사, Parse Tree 생성
 └───────────────┬───────────────┘
                 ▼
 ┌───────────────────────────────┐
 │ 2. 질의 변환기 (Transformer)  │ : 서브쿼리 Unnesting, View Merging, 조건절 전이
 └───────────────┬───────────────┘
                 ▼
 ┌───────────────────────────────┐      ┌──────────────────────────────────┐
 │ 3. 대안 생성기 (Plan Gen)     │ ───► │ 4. 비용 산정기 (Cost Estimator)   │
 │   - Access Path 후보 탐색     │      │   - 선택도 (Selectivity)         │
 │   - Join 순서 및 기법 조합    │      │   - 카디널리티 (Cardinality)     │
 └───────────────┬───────────────┘      │   - 통계정보 (Data Dictionary)   │
                 │                      └─────────────────┬────────────────┘
                 ▼                                        │
 ┌───────────────────────────────┐                        │
 │ 5. 실행 계획 생성기           │ ◄──────────────────────┘ (최소 비용 최적 플랜 채택)
 └───────────────┬───────────────┘
                 ▼
      [ 최적 실행 계획 (Plan) ] ───► SQL 실행 엔진 (Execution Engine)
```

- 본질: **사용자가 제출한 비절차적(Declarative) SQL 문을 해석하여 최소의 디스크 I/O와 CPU 연산 비용으로 최단 시간에 결과를 반환하도록 데이터 접근 경로(Access Path)와 조인 알고리즘을 결정하고 최적의 실행 계획(Execution Plan)을 수립하는 DBMS 핵심 연산 엔진**
- 암기: `파-변-대-비-생` (파서, 변환기, 대안생성기, 비용산정기, 생성기) / `선-카-비` (선택도, 카디널리티, 비용 계산)
- 판단축:
  - **RBO(규칙 기반)**: 15개 고정 규칙 순위표 기반 경로 선정, 통계정보 불필요하나 데이터 분포 무시로 비효율 극심
  - **CBO(비용 기반)**: 데이터 딕셔너리 통계(테이블 블록 수, Distinct 수, 히스토그램)를 기반으로 I/O 및 CPU 예상 비용을 계산하여 최저 비용 경로 선택
  - **적응형 최적화(Adaptive)**: 런타임 통계 피드백(Cardinality Feedback)을 통해 실행 도중 플랜을 동적 전환
- 주의: CBO 환경에서 통계정보가 오래되거나 바인드 변수의 편향(Skewed Data)으로 인해 '바인드 피킹(Bind Peeking)' 왜곡이 발생하면 최악의 풀스캔(FTS) 플랜이 캐시될 위험이 존재함

## 예상문제

> 데이터베이스 옵티마이저(Optimizer)의 아키텍처와 주요 구성요소 및 최적화 5단계 과정을 설명하고, 규칙 기반 옵티마이저(RBO)와 비용 기반 옵티마이저(CBO)의 메커니즘 차이점과 RBO의 한계점을 제시하시오. (25점)

## Ⅰ. 선언적 언어를 절차적 실행으로 변환하는 옵티마이저 개요

#### 한줄 요약: SQL 질의를 물리적 블록 접근 알고리즘으로 매핑하여 최소 자원 소모의 실행 계획을 생성하는 데이터베이스 내부 최적화 두뇌

- **배경**: 관계형 데이터베이스(RDBMS)의 SQL은 '어떤 데이터(What)'를 얻을지만 기술하는 선언적 언어이므로, '어떻게(How)' 가져올 것인가는 DBMS 내부 엔진이 스스로 판단해야 함
- **정의**: SQL 구문을 수신하여 문법·의미를 분석하고, 다양한 접근 경로와 조인 방식 중 가장 적은 비용(Cost)이 소요되는 실행 계획(Execution Plan)을 생성하는 소프트웨어 서브시스템
- **진화 과정**: RBO(고정 규칙, Oracle 9i 이전) $\rightarrow$ CBO(통계 기반 비용 계산, 현대 표준) $\rightarrow$ Adaptive Query Optimization(실행 시점 동적 보정, 최신 트렌드)

## Ⅱ. 옵티마이저 내부 아키텍처 및 최적화 5단계 과정

#### 한줄 요약: 파싱 $\rightarrow$ 질의 변환 $\rightarrow$ 플랜 생성 $\rightarrow$ 비용 산정 $\rightarrow$ 코드 생성의 정밀 파이프라인

```text
 [SQL 문]
    │
    ▼
 [Step 1. Parsing]        : Syntax Check, Data Dictionary Semantic Check, 해시값 생성
    │
    ▼
 [Step 2. Query Transform]: 비용 기반 / 휴리스틱 쿼리 재작성 (View Merging, Subquery Unnesting)
    │
    ▼
 [Step 3. Plan Generation]: 테이블 순서, 조인 방식(NL/Sort Merge/Hash), 인덱스 스캔 조합
    │
    ▼
 [Step 4. Cost Estimation]: Data Dictionary 통계 기반 Selectivity -> Cardinality -> Cost 계산
    │
    ▼
 [Step 5. Code Generation]: Row-source Generator를 통해 실행 가능한 바이너리 트리 생성
```

| 최적화 단계 | 구성 모듈 | 핵심 역할 및 수행 메커니즘 |
|:---|:---|:---|
| **1. 구문 분석** | **Query Parser** | SQL의 키워드 및 문법 검사(Syntax), 테이블·컬럼 실존 여부 및 접근 권한 검사(Semantic), SQL 해시값 생성 및 라이브러리 캐시 검색 |
| **2. 질의 변환** | **Query Transformer** | 의미적으로 동일하지만 더 효율적인 내부 SQL로 재작성 (서브쿼리 Unnesting, 뷰 머징(View Merging), 조건절 푸시다운(Predicate Pushdown)) |
| **3. 대안 생성** | **Plan Generator** | 인덱스 스캔(Unique, Range, Full) 및 풀 테이블 스캔, 조인 순서(Driving/Driven)와 조인 기법(NL, SMJ, Hash Join)의 모든 유효 조합 생성 |
| **4. 비용 산정** | **Cost Estimator** | 딕셔너리 통계(카디널리티, 컬럼 히스토그램, 클러스터링 팩터)를 바탕으로 각 후보 플랜의 디스크 블록 읽기 수(I/O Cost) 및 CPU 연산 시간 산정 |
| **5. 계획 생성** | **Code Generator** | 가장 낮은 비용으로 평가된 후보를 최종 채택하여 실행 엔진이 처리할 수 있는 형태의 Row-source 트리(실행 계획)로 변환 |

## Ⅲ. RBO와 CBO 비교 분석

#### 한줄 요약: 하드코딩된 15개 규칙 우선순위를 따르는 RBO와 통계 정보 기반 실제 자원 비용을 계산하는 CBO의 대조

```text
 [RBO: 고정 규칙 지향]
   규칙 순위표(Rank 1~15) ───► 데이터 분포 무시 ───► 인덱스 존재 시 무조건 스캔 채택

 [CBO: 통계 비용 지향]
   테이블/인덱스 통계 ───────► 선택도/카디널리티 계산 ──► I/O + CPU 총 비용 최저 플랜 채택
```

| 비교 항목 | 규칙 기반 옵티마이저 (RBO) | 비용 기반 옵티마이저 (CBO) |
|:---|:---|:---|
| **최적화 기준** | 사전 정의된 15개 고정 규칙 우선순위 (Rank) | 예상되는 시스템 자원 소모량(I/O, CPU, 메모리) 총합 비용 |
| **통계 정보** | 전혀 사용하지 않음 (수집 불필요) | 필수적 (테이블 건수, 블록 수, 히스토그램, 시스템 통계) |
| **주요 결정 요인** | 연산자 형태, 인덱스 유무, FROM/WHERE절 기술 순서 | 데이터 선택도(Selectivity), 카디널리티(Cardinality), 비용(Cost) |
| **인덱스 스캔 판단** | 인덱스가 존재하면 데이터의 99%를 조회해도 인덱스 사용 | 손익분기점(약 10~15%) 초과 시 Full Table Scan 채택 |
| **조인 순서 결정** | FROM절의 가장 우측 테이블을 Driving 테이블로 선택 | 카디널리티가 작은 테이블을 탐색하여 최적 드라이빙 선정 |
| **개발자 의존도** | 극도로 높음 (개발자가 규칙을 고려하여 SQL을 튜닝) | 상대적으로 낮음 (옵티마이저가 지능적 판단, 필요시 힌트 활용) |
| **현대 DBMS 지원** | 공식 폐기(Deprecated) 또는 레거시 유지 | 모든 현대 RDBMS의 표준 기본 엔진 |

## Ⅳ. CBO의 핵심 수학적 모델: 선택도, 카디널리티, 비용 계산

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
  $$Cost = (Single\ Block\ Read\ Count \times Single\_Time) + (Multi\ Block\ Read\ Count \times Multi\_Time) + \frac{CPU\ Cycles}{CPU\_Frequency}$$
- 클러스터링 팩터(Clustering Factor)가 우수할수록 Single Block I/O 비용이 대폭 감소함

## Ⅴ. RBO의 15개 우선순위 규칙 및 구조적 한계점

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
| **Rank 11** | Unbounded Range Search on Indexed Columns (`> `, `>=`) |
| **Rank 12~14** | Sort Merge Join, MAX/MIN on Index, ORDER BY on Index |
| **Rank 15** | **Full Table Scan** (가장 낮은 최후 순위) |

- **RBO의 3대 치명적 한계**:
  1. **데이터 편향 무시**: 1,000만 건 중 999만 건이 'Y'인 플래그 컬럼이라도 인덱스가 있으면 무조건 인덱스를 타서 999만 번의 Random Single I/O 유발
  2. **코딩 순서 종속성**: WHERE절에 동등 순위의 조건이 여러 개 있을 경우, 나중에 기술된 조건을 우선 평가하여 플랜이 뒤바뀜
  3. **신기술 수용 불가**: 해시 조인(Hash Join), 비트맵 인덱스, 파티션 프루닝 등 비용 기반 메커니즘을 지원할 수 없음

## Ⅵ. 실무 최적화 장애 요인 및 극복 방안 (Troubleshooting)

#### 한줄 요약: 바인드 피킹 왜곡, 통계정보 부재, 힌트 남발로 인한 장애를 해결하는 실무 지침

| 장애 현상 | 발생 원인 | 기술적 해결 방안 |
|:---|:---|:---|
| **바인드 피킹 (Bind Peeking) 왜곡** | 최초 하드 파싱 시 입력된 바인드 변수 값에만 최적화된 플랜이 캐시되어 이후 다른 값 조회 시 성능 급락 | ACS(Adaptive Cursor Sharing) 활성화, 쿼리 분리(`CASE`문 분기), 리터럴 치환 |
| **통계 정보 노후화로 인한 풀스캔** | 대량 배치 적재 후 통계 갱신이 누락되어 과거 작은 카디널리티 기준으로 잘못된 Nested Loops Join 선택 | DBMS_STATS 자동 수집 잡 스케줄링, 변경 임계치(Stale 10%) 감지 수집 |
| **힌트(Hint) 남발 및 플랜 고착** | 임시방편으로 인덱스 힌트를 강제(`/*+ INDEX(...) */`)하여 향후 데이터가 급증해도 인덱스 스캔 고정 | 힌트 격리, SPM(SQL Plan Management) 및 SQL 베이스라인을 통한 안정적 플랜 캡처 |

## Ⅶ. 기술사적 제언: 적응형 쿼리 최적화(Adaptive Query Optimization)와 AI

#### 한줄 요약: 정적 사전 추정의 한계를 극복하고 실행 단계에서 플랜을 동적으로 자가 치유하는 차세대 자율형 옵티마이저 체계

```text
 [전통적 CBO: 정적 최적화]
   사전 통계 ──► 플랜 수립 ──► 실행 (실제 카디널리티 폭증 시에도 플랜 변경 불가 ➔ 행 멈춤)

 [적응형 옵티마이저: 동적 자가 치유]
   사전 통계 ──► 플랜 수립 ──► 실행 중 관측 ──► 분기점 도달 ──► 조인 방식 동적 전환 (NL ➔ Hash Join)
```

- **Adaptive Plans**: 조인 시작 전 카디널리티를 관측하여 임계값을 넘어서면 Nested Loop Join에서 Hash Join으로 런타임에 실행 경로 자동 전환
- **Adaptive Statistics**: 부정확한 예측이 발견되면 백그라운드에서 동적 샘플링을 수행하고 지능형 통계 피드백(Cardinality Feedback)을 저장
- **AI/ML 기반 옵티마이저(Learned Optimizer)**: 기존 통계 공식 대신 심층 신경망(Deep Learning)을 활용해 쿼리 패턴과 실제 버퍼 캐시 히트율을 학습하여 인간의 힌트 작성 없이도 최적 경로를 자율 생성하는 방향으로 진화 중

---

## 1교시 10점 답안 발췌

```text
1. 옵티마이저(Optimizer)의 정의
  - 사용자가 제출한 비절차적 SQL을 해석하여 최소 비용(I/O, CPU)으로 최단 시간 내 결과를 반환하도록 최적의 실행 계획(Execution Plan)을 생성하는 DBMS 핵심 엔진.

2. 옵티마이저 5단계 아키텍처 및 CBO/RBO 비교
  가. 최적화 5단계:
    ① 파서(Syntax/Semantic 검사) -> ② 질의 변환기(뷰 머징/언네스팅) -> ③ 대안 생성기(후보 플랜 탐색) -> ④ 비용 산정기(선택도/카디널리티 기반 비용 계산) -> ⑤ 코드 생성기(실행 계획 확정)
  나. RBO vs CBO 비교:
    - RBO: 15개 고정 순위(ROWID 1위, FTS 15위) 기반, 데이터 분포 무시, 현대 DBMS 폐기.
    - CBO: 딕셔너리 통계(NDV, 히스토그램) 기반 비용(Cost) 계산, 선택도에 따른 지능적 경로 선택.

3. 최신 동향: 적응형 쿼리 최적화(Adaptive Optimization)
  - 런타임 실행 통계를 피드백받아 NL 조인에서 Hash 조인으로 동적 전환하여 플랜 왜곡 방지.
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제127회 정보관리 2교시: 데이터베이스 옵티마이저(Optimizer)의 역할과 주요 구성요소 및 최적화 과정, RBO와 CBO 비교
  - 제81회, 105회 기출
- **검증 출처**:
  - Oracle Database Concepts & SQL Tuning Guide (19c/23ai Optimizer Architecture)
  - 조시형, "친절한 SQL 튜닝", 디비안

---

## 학습 체크

- [ ] 옵티마이저의 5단계 처리 과정(파서-변환기-대안생성기-비용산정기-코드생성기)을 서술할 수 있는가?
- [ ] RBO의 15개 규칙 순위와 한계점 3가지를 설명할 수 있는가?
- [ ] CBO의 선택도(Selectivity), 카디널리티(Cardinality), 비용(Cost) 계산 공식을 제시할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-088 데이터베이스 튜닝](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/088_database_tuning.md)
- 연관 토픽: [03-047 인덱스(클러스터드·논클러스터드)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index_clustered_nonclustered.md), [03-098 정적 SQL vs 동적 SQL](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/098_dynamic_sql.md)
