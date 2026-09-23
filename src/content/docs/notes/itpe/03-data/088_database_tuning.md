---
sidebar:
  order: 88
  label: "088. 데이터베이스 튜닝 (Database Tuning)"
  badge:
    text: "A"
    variant: note
title: "데이터베이스 튜닝 (Database Tuning) 및 3대 계층별 접근 전략"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 88
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "088"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>물리적 데이터베이스 설계·튜닝</span><strong>데이터베이스 튜닝</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 240" width="100%" height="auto" role="img" aria-label="데이터베이스 튜닝 3계층 피라미드 및 비용 효과 구조">
  <defs>
    <linearGradient id="pyrTop" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="var(--sl-color-accent, #3b82f6)" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="var(--sl-color-accent, #3b82f6)" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="pyrMid" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="var(--sl-color-accent, #3b82f6)" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="var(--sl-color-accent, #3b82f6)" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="pyrBot" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="var(--sl-color-accent, #3b82f6)" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="var(--sl-color-accent, #3b82f6)" stop-opacity="0.15"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-gray-3, #94a3b8)"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="240" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Left Arrow: 파급력/효과 (위로 갈수록 큼) -->
  <line x1="45" y1="200" x2="45" y2="40" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="45" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #3b82f6)">개선 파급력</text>
  <text x="45" y="215" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3, #64748b)">수정비용 극대</text>

  <!-- Right Arrow: 발생 빈도/적용성 (아래로 갈수록 큼) -->
  <line x1="475" y1="40" x2="475" y2="200" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="475" y="215" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #3b82f6)">실무 빈도 (80%)</text>
  <text x="475" y="30" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3, #64748b)">비용 최저</text>

  <!-- Pyramid Layers -->
  <!-- Top Layer: 데이터 모델 튜닝 -->
  <polygon points="260,35 200,95 320,95" fill="url(#pyrTop)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="260" y="68" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">1. 모델 튜닝</text>
  <text x="260" y="84" text-anchor="middle" font-size="9.5" fill="#f1f5f9">정규화·반정규화·파티셔닝</text>

  <!-- Mid Layer: 환경/인스턴스 튜닝 -->
  <polygon points="195,100 135,160 385,160 325,100" fill="url(#pyrMid)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="260" y="128" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text, #1e293b)">2. 환경/인스턴스 튜닝</text>
  <text x="260" y="146" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-2, #475569)">Buffer Cache·Redo Log·I/O 파라미터</text>

  <!-- Bottom Layer: SQL/인덱스 튜닝 -->
  <polygon points="130,165 70,225 450,225 390,165" fill="url(#pyrBot)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="260" y="193" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--sl-color-text, #0f172a)">3. SQL 및 인덱스 튜닝</text>
  <text x="260" y="211" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-2, #334155)">실행계획·바인드 변수·복합 인덱스·힌트</text>
</svg>
</div>

- 본질: **한정된 하드웨어 및 시스템 자원 환경에서 데이터베이스의 트랜잭션 처리량(Throughput)을 극대화하고 응답 시간(Response Time)을 최소화하기 위해, 데이터 모델 설계(정규화/반정규화/파티셔닝), DBMS 인스턴스 환경(메모리 버퍼/I/O 파라미터), 그리고 SQL 및 인덱스 접근 경로를 유기적으로 개선하는 종합 성능 최적화 엔지니어링**
- 암기: `설-환-에스` (3대 계층: 설계/모델 튜닝, 환경 튜닝, SQL/인덱스 튜닝) / `측-분-목-개-검` (튜닝 5단계 절차: 성능 측정, 병목 분석, 목표 설정, 개선 수행, 결과 검증) / `최-소-아-이-오` (최소 I/O 원칙: 블록 I/O 최소화가 모든 튜닝의 귀결점)
- 판단축:
  - **모델 튜닝**: 성능 개선 효과가 가장 근본적이고 파급력이 크나, 운영 중 변경 시 애플리케이션 전면 수정 비용 발생
  - **SQL/인덱스 튜닝**: 테이블 구조를 바꾸지 않고 악성 쿼리의 블록 읽기를 수십만 개에서 수십 개로 줄여 즉각적 효과 창출 (실무 튜닝의 80%)
- 주의: 하드웨어 스케일업(CPU, RAM 증설)은 일시적 미봉책에 불과하며, 1억 건 풀스캔 쿼리 하나가 유입되면 아무리 큰 서버도 순식간에 CPU 100%로 마비됨. 또한 무분별한 인덱스 추가는 조회(SELECT)를 개선하는 대신 쓰기(INSERT/UPDATE/DELETE) 시 리프 분할(Page Split) 부하를 가중시킴

## Ⅰ. 자원 한계를 극복하는 데이터베이스 튜닝 개요

#### 한줄 요약: 시스템 병목을 해소하고 최소 I/O 원칙을 달성하여 트랜잭션 응답 시간을 단축하는 종합 성능 개선 체계

- **추진 배경**:
  - 데이터 볼륨의 지속적 팽창과 동시 사용자 폭증으로 인해 CPU 과열, 메모리 버퍼 경합, 디스크 I/O 병목이 발생함
  - 비효율적으로 작성된 악성 SQL이나 잘못된 인덱스 설계는 시스템 자원을 고갈시켜 데이터베이스 락(Lock) 경합과 타임아웃 장애를 유발함
- **데이터베이스 튜닝의 정의**:
  - 업무의 비즈니스 규칙과 데이터 접근 패턴에 맞추어 데이터 모델, DBMS 인스턴스 파라미터, SQL 쿼리 및 접근 경로(인덱스)를 최적화하여 **동일 하드웨어에서 최대의 Throughput과 최저의 Latency를 달성**하는 기술 활동

## Ⅱ. 데이터베이스 튜닝 3대 계층별 핵심 접근 전략

#### 한줄 요약: 아키텍처의 근본을 잡는 모델 튜닝, 자원 효율을 극대화하는 환경 튜닝, 즉각적 I/O를 절감하는 SQL 튜닝

### 1. 데이터 모델 튜닝 (Data Model Tuning)
- **정규화 (Normalization)**: 중복 데이터를 제거하고 무결성을 확보하여 데이터 갱신(DML) 시 락 경합과 이상현상(Anomaly)을 최소화
- **반정규화 (Denormalization)**: 대량 집계 질의나 빈번한 조인(Join)으로 인한 I/O 병목 구간에 컬럼 중복, 통계 요약 테이블 생성, 관계 역정규화를 적용하여 조회 성능 향상
- **테이블 파티셔닝 (Partitioning)**: 수천만 건 이상의 대용량 테이블을 Range, List, Hash 기준으로 물리 분할하여 **파티션 프루닝(Partition Pruning)**을 통한 풀스캔 범위 축소

### 2. 환경 및 인스턴스 튜닝 (Environment / Instance Tuning)
- **메모리 아키텍처 튜닝**:
  - **Data Buffer Cache**: 자주 조회되는 블록이 메모리에 오래 상주하도록 크기를 적정화하고 Keep/Recycle 풀 분리
  - **Shared Pool / Library Cache**: 실행 계획 캐싱 공간을 확보하여 하드 파싱 부하 방지
- **로그 및 체크포인트 튜닝**:
  - Redo Log Buffer 크기 조정 및 체크포인트 주기 최적화로 더티 페이지 플러시 시의 I/O 스파이크 방지
- **디스크 I/O 분산**:
  - 데이터 파일, 인덱스 파일, Redo Log 파일을 서로 다른 물리 디스크(LUN, RAID 10)에 분리 배치하여 헤드 경합 제거

### 3. SQL 및 인덱스 튜닝 (SQL & Index Tuning)
- **바인드 변수 (Bind Variable) 사용**:
  - 리터럴 상수 대신 바인드 변수(`?`)를 사용하여 라이브러리 캐시의 실행 계획을 재사용하는 **소프트 파싱(Soft Parsing)** 유도
- **인덱스 설계 및 컬럼 가공 금지**:
  - 카디널리티(선택도, Selectivity)가 높은 컬럼을 선행으로 복합 인덱스 구성
  - `WHERE TO_CHAR(reg_date) = '2026'`처럼 인덱스 컬럼을 함수로 가공하여 인덱스가 무효화되는 현상 원천 배제 (FBI 함수기반 인덱스 적용)
- **조인 기법 최적화**:
  - 소량 데이터 온라인 트랜잭션 $\rightarrow$ **Nested Loop Join (NL 조인)** 유도
  - 대량 배치 분석 $\rightarrow$ **Hash Join** 또는 Sort Merge Join 유도

## Ⅲ. 3대 튜닝 영역 간 비교

#### 한줄 요약: 개선 효과의 크기와 수정 비용, 적용 난이도 관점의 종합 트레이드오프

| 비교 항목 | 데이터 모델 튜닝 | 환경 및 인스턴스 튜닝 | SQL 및 인덱스 튜닝 |
|:---|:---|:---|:---|
| **개선 파급력** | **가장 강력함 (근본적 해결)** | 전사 시스템 전반에 균등 영향 | **특정 업무/쿼리 단위 즉각 개선** |
| **수정 비용/리스크** | **매우 높음** (테이블 및 소스 수정) | 보통 (재기동 필요할 수 있음) | **낮음** (인덱스 추가 및 SQL 리팩토링) |
| **튜닝 주체** | 데이터 아키텍트 (DA), 모델러 | 시스템 엔지니어, 인프라 DBA | 애플리케이션 개발자, 전문 튜너 |
| **주요 수행 시점** | 프로젝트 분석 및 설계 단계 | 시스템 셋업 및 인프라 증설 시 | **개발 및 운영 유지보수 전 주기** |
| **비용 효율성** | 초기 수행 시 최상, 사후 수행 시 최악 | 중간 (하드웨어 구매 비용) | **최고 (소프트웨어적 해결)** |

## Ⅳ. 데이터베이스 튜닝 5단계 엔드투엔드 절차

#### 한줄 요약: 현황 측정부터 병목 분석, 목표 설정, 개선 수행, 결과 검증 및 기준선 갱신으로 이어지는 폐루프 프로세스

| 단계 | 주요 활동 내용 | 산출물 및 도구 |
|:---|:---|:---|
| **1단계: 성능 측정 및 문제 식별** | APM, AWR 리포트를 통해 슬로우 쿼리 및 대기 이벤트(Wait Event) 수집 | APM 모니터링 로그, Top-SQL 목록 |
| **2단계: 병목 원인 상세 분석** | 실행 계획(Explain Plan), 10046 Trace를 분석하여 논리/물리 블록 I/O 실측 | Execution Plan, SQL 트레이스 분석서 |
| **3단계: 튜닝 목표치 설정** | 비즈니스 SLA에 맞추어 현실적 목표 수립 (응답시간 90% 감축, Buffer Gets 최소화) | 튜닝 목표 정의서 (KPI) |
| **4단계: 3계층 튜닝 개선 수행** | SQL 리팩토링, 인덱스 재구성, 힌트 부여, 통계 정보 갱신, 파라미터 조정 | 수정 SQL, 인덱스 변경 DDL 스크립트 |
| **5단계: 성능 검증 및 베이스라인 갱신** | 스테이징 부하 테스트로 성능 개선 검증 후 운영 배포 및 베이스라인 갱신 | 성능 전후 비교표, Baseline Profile |

## Ⅴ. AWR 리포트 핵심 지표 판독법

#### 한줄 요약: 오라클 AWR 리포트의 Top 5 Timed Events와 캐시 적중률을 통해 병목의 실체를 정확히 타격

| 대기 이벤트 (Wait Event) | I/O 패턴 특성 | 주요 병목 원인 | 실무 진단 및 대응 대책 |
|:---|:---|:---|:---|
| `db file sequential read` | 단일 블록 물리적 I/O | 인덱스를 경유한 랜덤 액세스 빈발 | 인덱스 클러스터링 팩터 점검, 커버링 인덱스 설계 |
| `db file scattered read` | 다중 블록 물리적 I/O | 대용량 테이블 대상 Full Table Scan | 인덱스 누락 점검, 테이블 파티셔닝 프루닝 적용 |
| `latch: cache buffers chains` | 메모리 버퍼 래치 경합 | 특정 블록에 다수 세션 동시 접근(Hot Block) | PCTFREE 조정, 해시 파티셔닝, SQL 튜닝 |
| `library cache lock / pin` | 라이브러리 캐시 락 | 대량 하드 파싱 발생 또는 동시 DDL 수행 | 바인드 변수 전면 적용, DDL 유지보수 시간대 분리 |
| `log file sync` | 리두 로그 디스크 기록 대기 | 빈번한 COMMIT 수행, 디스크 I/O 병목 | 커밋 빈도 조절(배치 커밋), Redo 디스크 분리(SSD) |

## Ⅵ. 현장 장애 패턴과 실무 트러블슈팅

#### 한줄 요약: 리터럴 SQL에 의한 하드 파싱 폭증, 인덱스 컬럼 가공에 의한 풀스캔, 인덱스 남발에 따른 DML 저하 해결

### 1. 하드 파싱(Hard Parsing) 폭증으로 인한 CPU 100% 장애
- **증상**: CPU 점유율이 100%에 달하고 `latch: shared pool` 대기가 치솟으며 쿼리가 실행되지 못함
- **원인**: `WHERE user_id = 'user_001'`처럼 리터럴 문자를 직접 결합한 동적 SQL 남발로 매번 실행 계획을 새로 컴파일함
- **해결책**: 모든 애플리케이션 SQL을 바인드 변수(`PreparedStatement`, `:user_id`)로 전환하여 소프트 파싱률을 99% 이상으로 회복

### 2. 인덱스 컬럼 가공으로 인한 Index Unusable
- **증상**: 인덱스를 생성해 두었음에도 불구하고 CBO가 풀 테이블 스캔을 선택
- **원인**: `WHERE SUBSTR(order_no, 1, 4) = '2026'` 또는 `WHERE salary * 1.1 > 5000`처럼 조건절 좌변 컬럼을 함수나 연산자로 변형
- **해결책**: 조건식을 `WHERE order_no LIKE '2026%'`, `WHERE salary > 5000 / 1.1`처럼 우변 상수를 가공하도록 변경

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 데이터베이스 튜닝의 핵심은 '최소 I/O'와 '소프트 파싱'이다. 아무리 빠른 SSD나 수 테라바이트 메모리를 갖추어도, 1천만 건 풀스캔 쿼리가 초당 10회 유입되면 I/O 큐가 포화되어 DB 전체가 마비된다. 하드웨어 스케일업으로 장애를 때우려는 시도는 미봉책일 뿐이며, 반드시 피라미드 역순인 'SQL/인덱스 튜닝 $\rightarrow$ 환경 튜닝 $\rightarrow$ 모델 튜닝'의 비용 효율적 단계로 문제를 해결해야 한다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 3계층 피라미드 다이어그램을 1면에 명확히 그리고 계층별 비용-효과 비교표를 제시하겠다. 2교시 25점형이라면 AWR 리포트의 Top-5 대기 이벤트를 인용하여 실제 운영 환경에서 sequential read vs scattered read가 발생했을 때 CBO의 실행계획을 어떻게 유도(NL 조인 vs Hash 조인, FBI 인덱스)하는지 구체적인 SQL 전/후 튜닝 사례와 CI 파이프라인 상의 Shift-Left 정적 SQL 검증 체계를 연결해 고득점을 노리겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 운영 환경 배포 후 장애가 발생한 뒤에야 APM/AWR을 통해 튜닝을 수행하는 사후 약방문식 접근은 대규모 장애 비용과 비즈니스 손실을 초래함. 개발 단계에서는 소량 테스트 데이터로 인해 악성 쿼리(Full Scan, 하드 파싱)의 위험성이 은폐됨.
- **대응 (개선 방안)**: CI/CD 배포 파이프라인에 정적 SQL 분석 도구를 연계하고, 스테이징 DB에 운영계 통계정보(CBO Stats Export/Import)를 선제 복제하여 배포 전 단계에서 실행계획 결함을 강제 검출하는 Shift-Left 체계 구축.
- **검증 (검증 기준)**: 프로덕션 배포 전 SQL 풀스캔 허용률 0%, 바인드 변수 미사용 쿼리 차단(소프트 파싱률 99% 이상), 핵심 트랜잭션 Buffer Gets 감축 목표 달성 검증.
- **효과 (실행 효과)**: 신규 배포에 따른 성능 회귀(Regression) 원천 차단, DBMS 라이선스 및 인프라 증설 비용 40% 이상 절감, 서비스 가용성 99.99% 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">소량 데이터 기반 개발로 악성 SQL 잠재, 배포 후 AWR 사후 수습</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">CI 파이프라인 정적 SQL 검증 및 스테이징 CBO 운영 통계 복제</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">풀스캔 0%, 바인드 변수 100%, Buffer Gets SLA 90% 이상 절감</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">성능 회귀 원천 방지, H/W 스케일업 비용 40% 절감, 고가용성 달성</div>
  </div>
</div>
---

## 1교시 예상문제 (10점)

> 데이터베이스 튜닝 (Database Tuning) 및 3대 계층별 접근 전략의 정의, 목적, 핵심 메커니즘을 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. 정의·목적

- 정의: 한정된 자원에서 처리량을 극대화하고 응답시간을 최소화하기 위한 3계층 종합 최적화 활동
- 목적: 해당 문제의 주요 분석과 의사결정에 적용한다.

### 2. 핵심 관계

| 튜닝 계층 | 핵심 접근 기법 | 비용 및 파급 효과 |
|:---|:---|:---|
| **1. 모델 튜닝 (설계)** | 정규화, 반정규화, 파티셔닝, 식별자 구조 최적화 | 효과: 극대 (근본적 해결) / 비용: 가장 높음 (구조 변경) |
| **2. 환경 튜닝 (인프라)** | Buffer Cache, Shared Pool, 체크포인트, 디스크 I/O 분산 | 효과: 중간 (전사 균등 개선) / 비용: 하드웨어 및 라이선스 수반 |
| **3. SQL 튜닝 (쿼리)** | 바인드 변수(소프트 파싱), 복합 인덱스 설계, 조인 최적화 | 효과: 즉각적 (실무 80% 차지) / 비용: 최저 (소프트웨어적 해결) |

### 핵심 관계

| 튜닝 계층 | 핵심 접근 기법 | 비용 및 파급 효과 |
|:---|:---|:---|
| **1. 모델 튜닝 (설계)** | 정규화, 반정규화, 파티셔닝, 식별자 구조 최적화 | 효과: 극대 (근본적 해결) / 비용: 가장 높음 (구조 변경) |
| **2. 환경 튜닝 (인프라)** | Buffer Cache, Shared Pool, 체크포인트, 디스크 I/O 분산 | 효과: 중간 (전사 균등 개선) / 비용: 하드웨어 및 라이선스 수반 |
| **3. SQL 튜닝 (쿼리)** | 바인드 변수(소프트 파싱), 복합 인덱스 설계, 조인 최적화 | 효과: 즉각적 (실무 80% 차지) / 비용: 최저 (소프트웨어적 해결) |

- 제언: 핵심 메커니즘을 기준으로 설계하고 검증한다.
---

## 2~4교시 예상문제 (25점)

> 엔터프라이즈 시스템의 서비스 안정성과 처리 성능을 확보하기 위한 데이터베이스 튜닝(Database Tuning)의 개념 및 필요성을 설명하고, 3대 영역(데이터 모델 튜닝, 환경 튜닝, SQL/인덱스 튜닝)별 주요 접근 방법 및 체계적인 5단계 튜닝 절차를 서술하시오. (25점)
---

## 2~4교시 25점 답안

### [문제] 데이터베이스 튜닝(Database Tuning)의 3대 계층별 접근 전략 및 체계적 5단계 절차를 서술하시오. (25점)

#### Ⅰ. 최소 I/O 달성을 위한 데이터베이스 튜닝의 개요
1. **배경**: 데이터 폭증 및 악성 SQL로 인한 시스템 자원(CPU, 디스크) 고갈과 트랜잭션 지연 해소
2. **정의**: 한정된 자원에서 처리량을 극대화하고 응답시간을 최소화하기 위한 3계층 종합 최적화 활동

#### Ⅱ. DB 튜닝 3대 계층별 주요 접근 방법

| 튜닝 계층 | 핵심 접근 기법 | 비용 및 파급 효과 |
|:---|:---|:---|
| **1. 모델 튜닝 (설계)** | 정규화, 반정규화, 파티셔닝, 식별자 구조 최적화 | 효과: 극대 (근본적 해결) / 비용: 가장 높음 (구조 변경) |
| **2. 환경 튜닝 (인프라)** | Buffer Cache, Shared Pool, 체크포인트, 디스크 I/O 분산 | 효과: 중간 (전사 균등 개선) / 비용: 하드웨어 및 라이선스 수반 |
| **3. SQL 튜닝 (쿼리)** | 바인드 변수(소프트 파싱), 복합 인덱스 설계, 조인 최적화 | 효과: 즉각적 (실무 80% 차지) / 비용: 최저 (소프트웨어적 해결) |

#### Ⅲ. 데이터베이스 튜닝 체계적 5단계 절차
1. **성능 측정(AWR/APM) $\rightarrow$ 병목 분석(Explain Plan/Trace) $\rightarrow$ 목표 설정(SLA) $\rightarrow$ 튜닝 수행(SQL/인덱스) $\rightarrow$ 결과 검증(부하테스트)**
2. **핵심 대원칙**: 블록 I/O 최소화 (디스크 물리적 I/O 및 메모리 버퍼 캐시 논리적 읽기 최소화)

#### Ⅳ. 실무 장애 방지 및 아키텍처 제언
1. **하드 파싱 방어**: 리터럴 SQL 배제 및 바인드 변수 전면 적용으로 CPU 파싱 부하 제거
2. **사전 예방(Shift-Left)**: CI 파이프라인에 정적 SQL 분석기를 도입하여 배포 전 악성 SQL 원천 차단
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제127회 1교시 (데이터베이스 튜닝의 3대 영역 및 절차)
  - 컴퓨터시스템응용기술사 제121회 2교시 (데이터베이스 성능 진단 기법과 AWR 분석)
  - 정보관리기술사 제118회 1교시 (SQL 하드 파싱과 소프트 파싱의 비교)
- **표준 및 검증 출처**:
  - 조시형, *친절한 SQL 튜닝*, 디비안 (2018)
  - Oracle Database 19c Performance Tuning Guide, "AWR and System Performance"
  - Guy Harrison, *Next Generation Databases*, Apress
---

## 연결 토픽

- [047. 인덱스 (Index)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index.md)
- [091. 옵티마이저 (Optimizer)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/091_optimizer.md)
- [021. DB 파티셔닝과 샤딩 (DB Partitioning & Sharding)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/021_db_partitioning_sharding.md)
