---
title: "옵티마이저(Optimizer)"
author: "Antigravity"
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

## Ⅰ. 관계형 DBMS의 두뇌, 옵티마이저(Optimizer)의 개요

### 가. 옵티마이저의 정의
- 사용자가 작성한 **선언적 SQL**(Structured Query Language) 문장을 전달받아, 데이터 딕셔너리에 저장된 **오브젝트 통계정보**와 시스템 자원 환경을 바탕으로 수많은 실행 가능한 데이터 접근 경로(Execution Path) 중에서 가장 적은 시스템 비용(Cost)과 최단 시간으로 수행할 최적의 **실행 계획** (Execution Plan)을 생성하는 DBMS(Database Management System) 핵심 엔진.

### 나. 옵티마이저의 동작 원칙
- 사용자는 "무엇(What)"을 가져올지만 SQL로 선언하고, "어떻게(How)" 가져올지는 옵티마이저가 전적으로 결정함.

---

## Ⅱ. 규칙 기반 옵티마이저(RBO) vs 비용 기반 옵티마이저(CBO)

### 가. RBO와 CBO 패러다임 비교

```text
[ RBO vs CBO 비교 ]
(A) 규칙 기반 옵티마이저 (RBO) : 사전 정의된 15개 우선순위 룰에 따라 기계적 결정 (데이터 볼륨 무시)
(B) 비용 기반 옵티마이저 (CBO) : 데이터 건수, 인덱스 높이, I/O 비용, CPU 연산 비용을 수식 계산하여 최적해 도출
```

| 비교 항목 | 규칙 기반 옵티마이저 (RBO, Rule-Based Optimizer) | 비용 기반 옵티마이저 (CBO, Cost-Based Optimizer) |
| :--- | :--- | :--- |
| **최적화 기준** | 사전에 정의된 엄격한 규칙 우선순위 (Rank 1 ~ 15) | 예상 소요 시간 및 I/O/CPU(Central Processing Unit) 자원 소모 비용 (Cost) |
| **통계 정보 활용** | 테이블 크기, 인덱스 분포 등 통계 정보 전혀 미사용 | 오브젝트(테이블, 인덱스) 및 시스템 통계 정보 필수 활용 |
| **인덱스 판단** | 인덱스가 존재하면 무조건 인덱스 스캔 채택 | 인덱스가 있어도 전체의 상당 비율 이상 조회 시 Full Scan 선택 |
| **현재 위상** | 과거 레거시 시스템 잔재 (현재 대부분 지원 중단) | 현대 모든 상용/오픈소스 RDBMS(Relational Database Management System)의 표준 엔진 |

---

## Ⅲ. CBO의 내부 동작 메커니즘 및 3대 핵심 구성 모듈

### 가. 옵티마이저 3대 서브엔진 구조

```text
[ CBO 내부 처리 프로세스 ]
[사용자 SQL] ---> [1. 쿼리 변환기 (Query Transformer)]
                        - 서브쿼리 언네스팅, 뷰 머징, 조건절 푸시다운
                        |
                        v
                  [2. 비용 예측기 (Estimator)]
                        - 카디널리티(Cardinality), 선택도(Selectivity), Cost 계산
                        |
                        v
                  [3. 계획 생성기 (Plan Generator)]
                        - 조인 순서(순열), 조인 기법, 인덱스 조합 탐색 -> [최적 실행 계획 확정]
```

### 나. 카디널리티(Cardinality)와 선택도(Selectivity) 계산 원리
- **선택도 (Selectivity)** : 조건절에 의해 선택될 것으로 예상되는 데이터의 비율.
  $$\text{Selectivity} = \frac{1}{\text{Distinct Values (NDV)}}$$
- **카디널리티 (Cardinality)** : 해당 연산 수행 후 반환될 것으로 예상되는 행(Row)의 수.
  $$\text{Cardinality} = \text{Total Rows} \times \text{Selectivity}$$

---

## Ⅳ. 옵티마이저(Optimizer)의 주요 한계점 및 해결 방안

- **바인드 피킹** (Bind Peeking)으로 인한 실행 계획 요동 및 서든데스 :
  - 한계점 : 최초 하드 파싱 시점에 바인드 변수 값에 따라 최적화된 실행 계획이 캐시되어, 상이한 분포를 가진 후속 쿼리 실행 시 Full Table Scan 등 비효율 유발.
  - 해결 방안 : **어댑티브 커서 공유** (ACS: Adaptive Cursor Sharing) 활성화, 데이터 편향이 심한 조건절에는 리터럴 SQL 사용 또는 SQL 플랜 베이스라인(SPM, SQL Plan Management) 고정.
- 다중 조건절 및 조인 누적에 따른 **비용(Cost)** 추정 오차의 증폭 :
  - 한계점 : 컬럼 간 독립성 가정 하에 단일 선택도(Selectivity)를 곱하여 계산하므로 상관관계 컬럼이나 다중 조인 시 실제 행 수와 추정 행 수 간 막대한 괴리 발생.
  - 해결 방안 : **확장 통계** (Extended Statistics / 다중 컬럼 히스토그램) 수집, 동적 표본추출(Dynamic Sampling) 활성화, 힌트(LEADING, USE_NL/HASH)를 통한 명시적 유도.
- 대규모 **DDL**(Data Definition Language) 및 배치 후 통계정보 부재 또는 락 경합 :
  - 한계점 : 파티션 교체나 대량 데이터 로드 직후 통계정보가 누락되어 RBO 수준의 최악 플랜 선택, 또는 주간 업무 중 자동 통계 수집 잡 실행으로 라이브러리 캐시 락 경합 발생.
  - 해결 방안 : 배치 직후 증분 통계(Incremental Statistics) 수집 프로세스 내재화, 통계정보 수집 스케줄을 심야 유지보수 윈도우로 제한 및 통계 잠금(Locking Statistics) 기법 적용.

## Ⅴ. 옵티마이저 제어 및 SQL 튜닝 실무 제언

- **옵티마이저 힌트(Hint)** 남용의 함정 : 성능이 느리다고 쿼리마다 `/*+ INDEX(...) */`, `/*+ USE_NL */` 등 힌트를 강제 삽입하면, 향후 데이터 볼륨이 크게 증가했을 때 옵티마이저가 스스로 Hash Join이나 Full Scan으로 변경하지 못해 시스템 장애를 유발함. 힌트는 긴급 장애 조치용으로 한정하고 근본적인 통계정보 갱신과 인덱스 재설계로 해결해야 함.
- **히스토그램(Histogram)** 수집 전략 : 특정 컬럼의 데이터 분포가 심하게 치우쳐 있는(Skewed) 경우(예: 주문상태 대부분이 '배송완료', 극소수만 '결제대기'), 기본 통계로는 평균치만 계산하여 잘못된 실행 계획을 수립하므로, 편향 컬럼에 대해 높이 균형(Height-Balanced) 또는 도수(Frequency) 히스토그램을 명시적으로 수집할 것을 제언함.
