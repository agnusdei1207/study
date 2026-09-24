---
sidebar:
  order: 105
  label: "105. 데이터 프로파일링"
  badge:
    text: "기초"
    variant: note
title: "데이터 프로파일링(Data Profiling) 분석 기법 및 데이터 품질 진단 체계"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 105
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "105"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터 품질관리</span><strong>데이터 프로파일링</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" role="img" aria-label="데이터 프로파일링 3대 분석 차원 및 핵심 지표">
  <!-- Background Card -->
  <rect width="520" height="220" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Top Title Box -->
  <rect x="130" y="15" width="260" height="30" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
  <text x="260" y="34" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">데이터 프로파일링 (Data Profiling)</text>

  <!-- Connectors -->
  <path d="M 260 45 L 260 55" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
  <path d="M 98 55 L 422 55" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
  <path d="M 98 55 L 98 68" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
  <path d="M 260 55 L 260 68" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
  <path d="M 422 55 L 422 68" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>

  <!-- Col 1: 열 분석 -->
  <g transform="translate(18, 68)">
    <rect width="160" height="135" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="160" height="26" rx="6" fill="#f8fafc"/>
    <text x="80" y="18" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">1. 열 (Column) 분석</text>

    <text x="12" y="44" font-size="9" fill="var(--sl-color-text, #1e293b)">• 데이터 타입 및 길이 실측</text>
    <text x="12" y="64" font-size="9" fill="var(--sl-color-text, #1e293b)">• NULL / 결측치 비율</text>
    <text x="12" y="84" font-size="9" fill="var(--sl-color-text, #1e293b)">• 카디널리티 (Distinct 수)</text>
    <text x="12" y="104" font-size="9" fill="var(--sl-color-text, #1e293b)">• 정규식 패턴 준수율</text>
    <text x="12" y="124" font-size="9" fill="var(--sl-color-text, #1e293b)">• 이상치 (IQR / Min·Max)</text>
  </g>

  <!-- Col 2: 구조 분석 -->
  <g transform="translate(180, 68)">
    <rect width="160" height="135" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
    <rect width="160" height="26" rx="6" fill="var(--sl-color-accent, #eff6ff)"/>
    <text x="80" y="18" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">2. 구조 (Structure) 분석</text>

    <text x="12" y="44" font-size="9" fill="var(--sl-color-accent, #1d4ed8)">• PK 후보 키 유일성</text>
    <text x="12" y="64" font-size="9" fill="var(--sl-color-accent, #1d4ed8)">• 함수적 종속성 (A $\rightarrow$ B)</text>
    <text x="12" y="84" font-size="9" fill="var(--sl-color-accent, #1d4ed8)">• 다중 컬럼 간 상관관계</text>
    <text x="12" y="104" font-size="9" fill="var(--sl-color-accent, #1d4ed8)">• 도메인 유효범위 검증</text>
    <text x="12" y="124" font-size="9" fill="var(--sl-color-accent, #1d4ed8)">• 비즈니스 무결성 규칙</text>
  </g>

  <!-- Col 3: 관계 분석 -->
  <g transform="translate(342, 68)">
    <rect width="160" height="135" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="160" height="26" rx="6" fill="#f8fafc"/>
    <text x="80" y="18" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">3. 관계 (Relation) 분석</text>

    <text x="12" y="44" font-size="9" fill="var(--sl-color-text, #1e293b)">• FK 참조 무결성 대사</text>
    <text x="12" y="64" font-size="9" fill="var(--sl-color-text, #1e293b)">• 고아 레코드 (Orphan) 탐색</text>
    <text x="12" y="84" font-size="9" fill="var(--sl-color-text, #1e293b)">• 부모-자식 카디널리티</text>
    <text x="12" y="104" font-size="9" fill="var(--sl-color-text, #1e293b)">• 시스템 간 엔티티 중복</text>
    <text x="12" y="124" font-size="9" fill="var(--sl-color-text, #1e293b)">• 마스터-상세 정합성</text>
  </g>
</svg>
</div>

- 본질: **데이터베이스 내에 실제로 저장된 물리 데이터를 직접 읽고 통계적 기법을 적용하여 데이터의 실제 형식, 값의 분포, 결측률, 이상치, 그리고 테이블 간 참조 무결성 위반 여부를 정량적으로 측정·진단하는 데이터 품질관리(DQM)의 선행 분석 기법**
- 암기: `열-구-관` (3대 분석 차원: 열 분석, 구조 분석, 관계 분석) / `탐-수-규-보고` (프로파일링 절차: 탐색, 수집, 규칙 대조, 리포트)
- 판단축:
  - **문서 vs 실제 데이터**: 데이터 정의서나 메타데이터 문서의 정의를 맹신하지 않고, 실제 물리 블록에 저장된 레코드의 실태를 실측하여 격차(Gap)를 적발
  - **전수 vs 샘플링**: 대용량 운영 DB의 I/O 경합을 피하기 위해 스테이징 복제본을 활용하거나 통계적 샘플링(Bernoulli Sampling) 기법 적용
- 주의: 프로파일링 작업은 테이블 전체에 대한 `COUNT(DISTINCT)`, `GROUP BY`, `MIN/MAX` 등 대규모 집계 연산을 수반하므로, 운영 프로덕션 DB에서 직접 실행 시 CPU 100% 포화 및 서비스 타임아웃을 유발할 수 있어 **읽기 전용 복제본(Read Replica) 또는 ETL 스테이징 서버**에서 실행해야 함
---

## 1교시 예상문제 (10점)

> 데이터 프로파일링(Data Profiling) 분석 기법 및 데이터 품질 진단 체계의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### [문제] 데이터 프로파일링 (Data Profiling)

#### 1. 데이터 프로파일링의 정의
- 원천 데이터의 구조, 값의 분포, 결측률, 무결성 제약 위배 여부를 통계적으로 실측하여 데이터 품질 실태를 파악하는 진단 기법

#### 2. 데이터 프로파일링 3대 분석 차원

| 분석 차원 | 핵심 점검 내용 | 주요 진단 지표 |
|:---|:---|:---|
| **1. 열 (Column) 분석** | 단일 컬럼 속성값의 건전성 실측 | 데이터 타입/길이, NULL율, 카디널리티, 정규식 패턴, IQR 이상치 |
| **2. 구조 (Structure) 분석** | 단일 테이블 내부의 무결성 검증 | PK 후보키 유일성, 함수적 종속성(FD), 다중열 상관관계, 비즈니스 룰 |
| **3. 관계 (Relation) 분석** | 테이블 간 참조 무결성 및 대사 | FK 참조 무결성, 고아 레코드(Orphan), 시스템 간 엔티티 중복 |

#### 3. 실무 수행 시 성능 및 거버넌스 고려사항
- 운영 DB I/O 부하 방지를 위한 Read Replica 분리 실행 및 Airflow-Great Expectations 연계 지속적 품질 게이트(Quality Gate) 구축
---

### 핵심 관계

| 분석 차원 | 주요 분석 항목 | 핵심 진단 지표 및 점검 내용 |
|:---|:---|:---|
| **1. 열 프로파일링 (Column Profiling)** | 데이터 타입, 포맷, 값 분포 | - **결측치 비율**: NULL, 스페이스, `9999-12-31` 등 기본값 비율<br>- **카디널리티**: Distinct 값의 개수, 선택도(Selectivity)<br>- **패턴 분석**: 정규표현식(Regex)을 통한 전화번호, 이메일, 주민번호 포맷 준수율<br>- **값 범위**: Min, Max, 사분위수(IQR)를 통한 극단적 이상치 탐지 |
| **2. 구조 프로파일링 (Structure Profiling)** | 기본키, 함수적 종속성 | - **PK 유일성(Uniqueness)**: 복합키 조합 시 중복 레코드 존재 여부<br>- **함수 종속성(FD)**: 속성 A가 속성 B를 고유하게 결정하는지 실측 ($A \rightarrow B$ 성립률)<br>- **비즈니스 룰**: 예) '종료일자 $\ge$ 시작일자' 규칙 준수율 검증 |
| **3. 관계 프로파일링 (Relationship Profiling)** | 외래키, 고아 데이터 | - **참조 무결성**: 자식 테이블의 FK 값이 부모 테이블의 PK에 실존하는지 대사<br>- **고아 레코드(Orphan Record)**: 부모가 삭제되어 남겨진 쓰레기 데이터 건수<br>- **중복 엔티티**: 서로 다른 시스템 간 동일 고객(동명이인, 전화번호 일치) 병합율 |

---

## 2~4교시 예상문제 (25점)

> 데이터 웨어하우스(DW) 구축 및 데이터 마이그레이션 프로젝트에서 데이터 품질을 보장하기 위한 데이터 프로파일링(Data Profiling)의 개념과 3대 분석 차원(열, 구조, 관계 분석)을 설명하고, 프로파일링 수행 4단계 절차 및 실무 적용 시 고려사항을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 불량 데이터의 침투를 차단하는 데이터 프로파일링 개요

#### 한줄 요약: 데이터 정의서와 실제 데이터 간의 불일치를 실측하여 데이터 정제와 모델링의 신뢰 기준선을 제공하는 품질 진단 기법

- **배경**: 시스템 간 데이터 연계나 차세대 이관 시, 테이블 정의서에는 `NOT NULL`로 정의되어 있으나 실제 데이터의 30%가 공백이거나 비표준 코드가 유입되어 적재가 중단되는 사고 빈발
- **정의**: 원천 데이터 소스를 체계적으로 스캔하여 데이터의 구조, 내용, 통계적 특성, 업무 규칙 준수율을 정량적으로 파악하는 비침습적(Non-invasive) 분석 활동
- **핵심 가치**: 데이터 마이그레이션 오류 조기 발견, DAMA-DMBOK 기반 데이터 거버넌스 품질 지표(유효성, 완전성, 유일성)의 객관적 수치화

### Ⅱ. 데이터 프로파일링의 3대 분석 차원 및 진단 지표

#### 한줄 요약: 단일 컬럼 분석에서 시작하여 테이블 내부 구조, 테이블 간 참조 관계로 진단 범위를 확장

| 분석 차원 | 주요 분석 항목 | 핵심 진단 지표 및 점검 내용 |
|:---|:---|:---|
| **1. 열 프로파일링 (Column Profiling)** | 데이터 타입, 포맷, 값 분포 | - **결측치 비율**: NULL, 스페이스, `9999-12-31` 등 기본값 비율<br>- **카디널리티**: Distinct 값의 개수, 선택도(Selectivity)<br>- **패턴 분석**: 정규표현식(Regex)을 통한 전화번호, 이메일, 주민번호 포맷 준수율<br>- **값 범위**: Min, Max, 사분위수(IQR)를 통한 극단적 이상치 탐지 |
| **2. 구조 프로파일링 (Structure Profiling)** | 기본키, 함수적 종속성 | - **PK 유일성(Uniqueness)**: 복합키 조합 시 중복 레코드 존재 여부<br>- **함수 종속성(FD)**: 속성 A가 속성 B를 고유하게 결정하는지 실측 ($A \rightarrow B$ 성립률)<br>- **비즈니스 룰**: 예) '종료일자 $\ge$ 시작일자' 규칙 준수율 검증 |
| **3. 관계 프로파일링 (Relationship Profiling)** | 외래키, 고아 데이터 | - **참조 무결성**: 자식 테이블의 FK 값이 부모 테이블의 PK에 실존하는지 대사<br>- **고아 레코드(Orphan Record)**: 부모가 삭제되어 남겨진 쓰레기 데이터 건수<br>- **중복 엔티티**: 서로 다른 시스템 간 동일 고객(동명이인, 전화번호 일치) 병합율 |

### Ⅲ. 데이터 프로파일링 표준 4단계 수행 절차

#### 한줄 요약: 대상 선정 $\rightarrow$ 규칙 프로파일링 $\rightarrow$ 이상치 식별 $\rightarrow$ 정제 보고의 선순환 프로세스

| 단계 | 주요 활동 내용 | 산출물 및 기법 |
|:---|:---|:---|
| **1단계: 대상 선정 (Scoping)** | 전사 테이블 중 결함 파급력이 큰 마스터 및 핵심 트랜잭션 식별 | 프로파일링 대상 목록 정의서 |
| **2단계: 지표 수집 (Execution)** | 데이터 타입, NULL율, 카디널리티, 패턴 분포를 집계 쿼리로 실측 | Great Expectations, SQL 수집 스크립트 |
| **3단계: 갭 분석 (Gap Analysis)** | 메타데이터 정의서와 실제 데이터 간의 불일치(타입 불일치, FK 누락) 도출 | 불일치 갭 분석서 (Gap Matrix) |
| **4단계: 결과 보고 및 환류 (Reporting)** | 프로파일링 결과서를 바탕으로 데이터 정제(Cleansing) 룰 확정 및 반영 | 품질 진단 리포트, 데이터 클렌징 룰북 |

### Ⅳ. 데이터 프로파일링 vs 데이터 감사(Audit) vs 데이터 정제(Cleansing)

#### 한줄 요약: 현상을 진단하는 프로파일링, 규정 준수를 확인하는 감사, 오류를 치료하는 정제의 상호 연계

| 비교 항목 | 데이터 프로파일링 (Profiling) | 데이터 감사 (Audit) | 데이터 정제 (Cleansing) |
|:---|:---|:---|:---|
| **수행 목적** | 데이터의 실제 상태와 패턴을 **기술·진단(Diagnosis)** | 정책, 법령, 비즈니스 규칙의 **준수 여부 검증(Verification)** | 발견된 오류 데이터를 **수정·치환·제거(Treatment)** |
| **데이터 변경** | **절대 변경 없음 (Read-Only)** | 변경 없음 (Read-Only) | **실제 데이터 수정 (Update / Delete)** |
| **수행 시점** | 프로젝트 초기, ETL 파이프라인 개발 전 | 정기적 감사 주기, 운영 배포 후 | 프로파일링 및 감사 결과 도출 직후 |
| **산출물** | 컬럼별 통계치, 데이터 분포표, 갭 분석서 | 감사 지적 보고서, 컴플라이언스 점수 | 정제된 데이터셋, 변환 스크립트, 예외 로그 |

### Ⅴ. 오픈소스 기반 현대적 프로파일링 도구 생태계

#### 한줄 요약: 전통적 SQL 수작업 스캔에서 자동화된 Assertions 프레임워크로의 기술 진화

- **Great Expectations (GX)**: 데이터 파이프라인에서 데이터가 갖추어야 할 기댓값(Expectation)을 코드로 정의하고 프로파일링을 자동화하는 업계 표준 오픈소스
- **ydata-profiling (구 Pandas Profiling)**: 단 한 줄의 코드로 Pandas DataFrame의 수치형/범주형 상관관계, 왜도, 결측치를 HTML 리포트로 즉시 렌더링
- **Soda Core**: YAML 기반의 선언적 문법으로 SQL 쿼리 없이 복잡한 테이블 간 프로파일링 지표 수집 지원

### Ⅵ. 실무 운영 이슈 및 극복 방안 (Troubleshooting)

#### 한줄 요약: 운영 DB 성능 부하, 민감 개인정보 노출, 허위 양성(False Positive) 오류 통제

| 장애 요인 | 근본 원인 | 실무 엔지니어링 극복 대책 |
|:---|:---|:---|
| **운영 DB I/O 포화 및 락(Lock)** | 프로덕션 마스터 DB에서 수천만 건 테이블에 `COUNT(DISTINCT)` 실행으로 서비스 마비 | **Read Replica 격리 실행**, 야간 배치 시간대 수행, Bernoulli 샘플링(10% 표본) 적용 |
| **개인정보 침해 위험** | 프로파일링 리포트에 주민번호, 휴대폰번호 실제 데이터가 샘플로 노출 | 프로파일링 결과서 생성 시 민감 식별자 마스킹(`800101-1******`) 필터 강제 |
| **비즈니스 룰 오판 (False Positive)** | 레거시 특수 목적 코드(예: 테스트 계정 `9999`)를 단순 이상치로 오판하여 삭제 | 도메인 전문가 인터뷰 선행, 업무 규칙 예외 목록(White List) 사전 등록 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 많은 데이터 마이그레이션 프로젝트가 실패하는 결정적 이유는 '테이블 정의서'를 믿고 ETL 매핑을 시작하기 때문이다. 10년간 운영된 레거시 시스템의 정의서와 실제 물리 데이터는 100% 불일치한다. `VARCHAR(10)`에 공백 10칸이 차 있거나, 날짜 컬럼에 `0000-00-00`이 들어있는 것은 프로파일링을 돌려보기 전까지는 절대 알 수 없다. 따라서 프로젝트 착수 즉시 실제 물리 데이터를 스캔하는 프로파일링을 선행해야만 일정 지연과 데이터 파손 참사를 막을 수 있다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 3대 분석 차원(열, 구조, 관계) 매트릭스와 프로파일링 vs 감사 vs 정제의 3각 비교표를 핵심으로 작성하겠다. 2교시 25점형이라면 운영 DB 부하 방지를 위한 Read Replica 및 Bernoulli 샘플링 기법을 제시하고, 1회성 분석을 넘어 Airflow-Great Expectations 파이프라인에 인라인 프로파일링 품질 게이트(Quality Gate)를 내재화하는 지속적 데이터 옵저버빌리티(Continuous Data Observability) 아키텍처를 제언하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 차세대 이관 시 메타데이터 정의서에만 의존하여 ETL을 구축함에 따라 결측치, 형식 오류, 고아 레코드로 인한 적재 실패(Abend)가 빈발하고, 운영 프로덕션 DB에서 직접 프로파일링 수행 시 서비스 다운 위험 초래.
- **대응 (개선 방안)**: 읽기 전용 복제본(Read-Only Replica)에서 Great Expectations 기반 사전 프로파일링을 수행하고, Airflow 데이터 인제스천 파이프라인에 인라인 품질 검증 게이트(Circuit Breaker) 구축.
- **검증 (검증 기준)**: 마이그레이션 대상 테이블 프로파일링 100% 완료, 미식별 고아 레코드 발생률 0건, 인라인 검증 시 결측률 임계치(0.1%) 초과 시 파이프라인 즉시 격리.
- **효과 (실행 효과)**: 데이터 이관 실패율 95% 감소, 수작업 데이터 클렌징 일정 60% 단축, 전사 데이터 파이프라인 품질 신뢰도 99.9% 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">문서와 실데이터 불일치로 이관 실패, 운영 DB 프로파일링 시 부하 폭증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">Read Replica 사전 프로파일링 및 Airflow 인라인 품질 게이트 구축</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">프로파일링 커버리지 100%, 고아 레코드 0건, 결측 임계치 0.1% 통제</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">이관 실패율 95% 절감, 클렌징 공수 60% 단축, 고신뢰 파이프라인 구현</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제128회 정보관리 2교시: 데이터 품질 관리를 위한 데이터 프로파일링 기법과 분석 단계
  - 제83회 기출
- **검증 출처**:
  - DAMA International, "DAMA-DMBOK 2nd Edition", Chapter 13 Data Quality
  - 한국지능정보사회진흥원(NIA), "공공데이터 품질관리 매뉴얼 및 가이드라인"
---

## 연결 토픽

- 상위 토픽: [003. 데이터 품질관리 (Data Quality Management)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/003_data_quality_management.md)
- 연관 토픽: [156. 데이터 이관 (Data Migration)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/156_data_migration.md), [013. 무결성 제약조건 (Integrity Constraints)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/013_integrity_constraint.md)
