---
sidebar:
  order: 131
  label: "131. 로지컬 DW (Logical Data Warehouse)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 131
title: "로지컬 DW(Logical Data Warehouse) 가상화 아키텍처 및 쿼리 푸시다운 최적화"
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "131"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터 웨어하우스·빅데이터</span><strong>로지컬 DW</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Top: Consumers -->
  <rect x="140" y="15" width="240" height="34" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="260" y="36" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">소비 계층 (BI 도구, SQL 클라이언트, AI/ML)</text>

  <path d="M 260 49 L 260 70" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow131)"/>
  <text x="275" y="62" font-size="10" fill="#64748b">단일 표준 SQL 질의</text>

  <!-- Logical DW Layer -->
  <rect x="25" y="70" width="470" height="90" rx="8" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="260" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">로지컬 DW (Logical Data Warehouse) 가상화 계층</text>
  <rect x="40" y="102" width="135" height="45" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="107" y="120" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">시맨틱 카탈로그</text>
  <text x="107" y="136" text-anchor="middle" font-size="9" fill="#64748b">통합 메타데이터</text>
  <rect x="190" y="102" width="140" height="45" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="260" y="120" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">분산 비용 최적화기</text>
  <text x="260" y="136" text-anchor="middle" font-size="9" fill="#64748b">쿼리 푸시다운 엔진</text>
  <rect x="345" y="102" width="135" height="45" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="412" y="120" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">인메모리 캐시</text>
  <text x="412" y="136" text-anchor="middle" font-size="9" fill="#64748b">빈발 결과셋 가속</text>

  <!-- Pushdown Arrows -->
  <path d="M 107 160 L 107 190" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow131)"/>
  <path d="M 260 160 L 260 190" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow131)"/>
  <path d="M 412 160 L 412 190" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow131)"/>
  <text x="260" y="180" text-anchor="middle" font-size="9" fill="#2563eb">Query Pushdown (필터/집계 하향 전달)</text>

  <!-- Heterogeneous Sources Bottom -->
  <rect x="25" y="190" width="145" height="70" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="97" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">운영계 RDBMS</text>
  <text x="97" y="232" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Oracle, PostgreSQL</text>
  <text x="97" y="248" text-anchor="middle" font-size="9" fill="#64748b">실시간 OLTP 트랜잭션</text>

  <rect x="185" y="190" width="150" height="70" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="260" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="#0284c7">데이터 레이크 / S3</text>
  <text x="260" y="232" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Parquet, Iceberg</text>
  <text x="260" y="248" text-anchor="middle" font-size="9" fill="#64748b">대용량 이력 로그</text>

  <rect x="350" y="190" width="145" height="70" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="422" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">NoSQL / SaaS API</text>
  <text x="422" y="232" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">MongoDB, Salesforce</text>
  <text x="422" y="248" text-anchor="middle" font-size="9" fill="#64748b">반정형 도큐먼트/웹</text>

  <defs>
    <marker id="arrow131" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **데이터를 물리적으로 단일 저장소에 복제·적재(ETL)하지 않고, 분산된 이종 데이터 소스(RDB, Data Lake, NoSQL, SaaS)를 데이터 가상화(Data Virtualization) 기술을 통해 단일한 논리적 뷰로 통합하여 실시간 분석을 지원하는 가트너(Gartner) 제안의 차세대 DW 아키텍처**
- 암기: `가-푸-캐-연` (핵심 기술: 데이터 가상화, 쿼리 푸시다운, 인메모리 캐싱, 연합 쿼리) / `트-데-드-스` (대표 솔루션: Trino, Denodo, Dremio, Starburst)
- 판단축:
  - **전통적 물리 DW**: 대용량 스토리지 복제 적재, T+1 배치 지연, 무거운 ETL 파이프라인 유지보수
  - **로지컬 DW (LDW)**: Zero Data Movement(무복제), 온디맨드 실시간 질의, 쿼리 푸시다운 기반 TCO 절감
- 주의: 서로 다른 원천 시스템 간의 대규모 조인(Cross-database Join) 시 수천만 건 데이터가 네트워크를 타고 가상화 노드로 몰리면 대역폭 고갈과 쿼리 타임아웃이 발생하므로 동적 파티션 프루닝 및 결과 캐싱 필수
---

## 1교시 예상문제 (10점)

> 로지컬 DW(Logical Data Warehouse) 가상화 아키텍처 및 쿼리 푸시다운 최적화의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 분산된 이종 데이터 소스를 물리적으로 복제하지 않고 데이터 가상화 계층을 통해 단일한 논리적 뷰로 통합하는 차세대 DW 아키텍처 |
| **2. 4대 구성요소** | 원천 데이터 소스(RDB/S3/NoSQL), 데이터 가상화 연합 엔진(Trino), 시맨틱 모델/카탈로그, 소비 BI 계층 |
| **3. 쿼리 푸시다운** | 필터(`WHERE`), 컬럼 투영(`SELECT`), 집계(`GROUP BY`)를 원천 DB로 하향 위임하여 네트워크 전송량과 가상화 부하를 극소화 |
| **4. 전통 DW 대비 장점** | 물리적 데이터 복제 제거(Zero Data Movement), 실시간 분석 지원, 파이프라인 변경 민첩성 및 스토리지 TCO 절감 |
---

### 핵심 관계

| 비교 항목 | 전통적 물리 DW (Traditional Physical DW) | 로지컬 DW (Logical DW) |
|:---|:---|:---|
| **데이터 이동 방식** | **물리적 대량 이동 및 중복 복제 (ETL)** | **Zero-Copy 무복제 가상화 (온디맨드 실시간 쿼리)** |
| **데이터 신선도** | T+1 일 단위 또는 시간 단위 배치 지연 | **실시간(Real-time) 즉시 반영** |
| **인프라 비용 (TCO)** | 초대형 물리 스토리지 및 중복 저장 비용 극심 | **스토리지 증설 불필요, 컴퓨팅 가상화 엔진만 운용** |
| **스키마 변경 민첩성** | 파이프라인 재구축 및 스키마 변경에 수개월 소요 | **논리적 뷰(View) 수정만으로 수 분 내 반영** |
| **원천 시스템 부하** | 야간 배치 시간에만 ETL 부하 집중 | **주간 분석 쿼리 시 원천 시스템에 연산 부하 전이 가능** |
| **조인 성능** | 단일 스토리지 내부 조인으로 대용량 고속 처리 | 이종 소스 간 크로스 조인 시 네트워크 병목 발생 위험 |

---

## 2~4교시 예상문제 (25점)

> 가트너(Gartner)가 제안한 로지컬 데이터웨어하우스(LDW, Logical Data Warehouse)의 개념과 구성요소, 쿼리 푸시다운(Query Pushdown) 메커니즘을 설명하고, 전통적인 물리적 DW와의 장단점을 비교하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 물리적 데이터 이동의 한계를 극복하는 로지컬 DW 개요

#### 한줄 요약: 이종 저장소의 데이터를 물리적으로 복제하지 않고 논리적 가상화 계층에서 단일 SQL로 실시간 연합 질의하는 아키텍처

- **배경**:
  - 기업 내 데이터가 클라우드, 온프레미스, SaaS, NoSQL로 파편화되면서 모든 데이터를 중앙 단일 물리 DW로 ETL 적재하는 데 막대한 비용과 시간(수개월) 소요
  - 실시간 의사결정 요구가 증대되었으나 배치 기반 물리 DW는 T+1(하루 전) 데이터만 제공하는 지연 한계 직면
- **정의**: 데이터 가상화, 분산 연합 쿼리(Federated Query), 시맨틱 모델링 기술을 결합하여, 물리적 이동 없이 분산된 원천 데이터를 마치 하나의 거대한 관계형 DW처럼 단일 인터페이스로 제공하는 아키텍처
- **Gartner의 핵심 사상**: "데이터가 위치한 곳에 그대로 두고(In-situ Analysis), 논리적 추상화 계층을 통해 민첩하게 분석하라"

### Ⅱ. 로지컬 DW의 4대 핵심 구성 아키텍처

#### 한줄 요약: 이종 원천 소스, 데이터 가상화 엔진, 시맨틱 레이어, 비즈니스 소비 계층

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="115" height="120" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="72" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 원천 소스</text>
  <text x="72" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">RDBMS, NoSQL</text>
  <text x="72" y="90" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">S3 Lakehouse</text>
  <text x="72" y="110" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">SaaS REST API</text>
  <text x="72" y="130" text-anchor="middle" font-size="9" fill="#64748b">데이터 제자리 유지</text>

  <!-- Box 2 -->
  <rect x="140" y="20" width="115" height="120" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="197" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. 가상화 엔진</text>
  <text x="197" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Trino / Denodo</text>
  <text x="197" y="90" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">분산 연합 쿼리</text>
  <text x="197" y="110" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">쿼리 푸시다운</text>
  <text x="197" y="130" text-anchor="middle" font-size="9" fill="#64748b">고속 인메모리 처리</text>

  <!-- Box 3 -->
  <rect x="265" y="20" width="115" height="120" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="322" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. 시맨틱 계층</text>
  <text x="322" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">비즈니스 용어집</text>
  <text x="322" y="90" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">전사 논리 모델</text>
  <text x="322" y="110" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">접근 제어·보안</text>
  <text x="322" y="130" text-anchor="middle" font-size="9" fill="#64748b">단일 진실 공급원</text>

  <!-- Box 4 -->
  <rect x="390" y="20" width="115" height="120" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="447" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">4. 소비 계층</text>
  <text x="447" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Tableau, PowerBI</text>
  <text x="447" y="90" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">SQL 클라이언트</text>
  <text x="447" y="110" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">AI 모델 서빙</text>
  <text x="447" y="130" text-anchor="middle" font-size="9" fill="#64748b">실시간 대시보드</text>
</svg>
</div>

1. **원천 데이터 소스 계층**: 이기종 온프레미스 RDBMS, 클라우드 객체 스토리지, NoSQL, 외부 SaaS API 등 실제 데이터가 영속 저장된 계층
2. **데이터 가상화 및 연합 쿼리 엔진**: 표준 SQL 구문을 구문 분석(Parse)하고, 이종 소스 간 최적 실행 계획(CBO)을 수립하여 분산 병합하는 핵심 컴퓨팅 엔진
3. **시맨틱 모델 및 카탈로그 계층**: 원천의 복잡한 컬럼명을 표준 비즈니스 용어로 매핑하고 전사 데이터 거버넌스, 역할 기반 접근 제어(RBAC), 데이터 마스킹 수행
4. **소비 및 분석 애플리케이션**: JDBC/ODBC 또는 REST 인터페이스를 통해 단일 DW에 연결하듯 실시간 리포트와 분석 모델을 구동하는 사용자 접점

### Ⅲ. 쿼리 푸시다운(Query Pushdown) 최적화 메커니즘

#### 한줄 요약: 연산 부하와 네트워크 전송량을 줄이기 위해 조건 필터링과 집계를 원천 DB 엔진에 위임하는 핵심 최적화

1. **술어 푸시다운 (Predicate Pushdown)**:
   - `WHERE status = 'PAID' AND order_date >= '2026-01-01'` 조건을 가상화 노드가 아닌 원천 데이터베이스의 SQL 엔진으로 내려보냄
   - 원천 DB의 인덱스를 활용하여 불필요한 레코드의 99%를 원천에서 사전에 차단
2. **프로젝션 푸시다운 (Projection Pushdown)**:
   - 테이블의 수십 개 컬럼 중 SELECT 절에 명시된 3~4개 필수 컬럼만 네트워크로 전송받아 I/O 절감
3. **집계 푸시다운 (Aggregate Pushdown)**:
   - `COUNT()`, `SUM()`, `GROUP BY` 연산을 원천 RDBMS나 분산 엔진에서 완료한 뒤 요약된 통계 결과값만 회신받아 가상화 계층의 CPU 부하 최소화

### Ⅳ. 전통적 물리 DW vs 로지컬 DW(LDW) 상세 비교

#### 한줄 요약: 데이터 물리 복제와 배치성 정적 구조 vs 무복제 실시간 가상화와 고도의 민첩성

| 비교 항목 | 전통적 물리 DW (Traditional Physical DW) | 로지컬 DW (Logical DW) |
|:---|:---|:---|
| **데이터 이동 방식** | **물리적 대량 이동 및 중복 복제 (ETL)** | **Zero-Copy 무복제 가상화 (온디맨드 실시간 쿼리)** |
| **데이터 신선도** | T+1 일 단위 또는 시간 단위 배치 지연 | **실시간(Real-time) 즉시 반영** |
| **인프라 비용 (TCO)** | 초대형 물리 스토리지 및 중복 저장 비용 극심 | **스토리지 증설 불필요, 컴퓨팅 가상화 엔진만 운용** |
| **스키마 변경 민첩성** | 파이프라인 재구축 및 스키마 변경에 수개월 소요 | **논리적 뷰(View) 수정만으로 수 분 내 반영** |
| **원천 시스템 부하** | 야간 배치 시간에만 ETL 부하 집중 | **주간 분석 쿼리 시 원천 시스템에 연산 부하 전이 가능** |
| **조인 성능** | 단일 스토리지 내부 조인으로 대용량 고속 처리 | 이종 소스 간 크로스 조인 시 네트워크 병목 발생 위험 |

### Ⅴ. 로지컬 DW의 대표 기술 솔루션

#### 한줄 요약: 분산 SQL 엔진 기반과 상용 데이터 가상화 전문 플랫폼의 공존

| 솔루션 | 기술 분류 | 핵심 아키텍처 및 특징 |
|:---|:---|:---|
| **Trino (구 PrestoSQL)** | 오픈소스 분산 SQL 연합 쿼리 엔진 | 커넥터(Connector) 아키텍처를 통해 Hive, Iceberg, PG, Kafka를 단일 SQL로 결합하는 사실상 글로벌 표준 |
| **Denodo Platform** | 상용 데이터 가상화(DV) 엔터프라이즈 | 정교한 시맨틱 레이어, 자동 캐싱, 동적 쿼리 최적화 및 완벽한 엔터프라이즈 보안 거버넌스 제공 |
| **Dremio** | 아파치 애로우(Arrow) 기반 오픈소스 엔진 | 컬럼형 인메모리 포맷과 Data Reflections(자동 최적화 요약본)를 활용한 초고속 분석 서빙 |

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 원천 운영계 부하 차단(Read Replica), 대규모 크로스 조인 병목 해소, 지능형 결과 캐싱

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **집계 질의 시 운영계 ERP CPU 100% 포화** | 가상화 엔진의 푸시다운 쿼리가 운영계 Master DB로 직접 전달되어 OLTP 락 유발 | 가상화 소스 엔드포인트를 **읽기 전용 복제본(Read Replica)**으로 강제 분리 |
| **이종 소스 간 조인 시 네트워크 타임아웃** | RDB의 수천만 건과 S3의 수억 건을 조인하면서 대용량 데이터가 가상화 노드로 이동 | 소규모 차원 테이블을 대용량 노드로 브로드캐스트 조인(Broadcast Join)하거나 파티션 프루닝 적용 |
| **동일 대시보드 새로고침 시 반복 부하** | 수십 명의 임직원이 아침마다 동일한 일일 리포트 쿼리를 호출 | 가상화 엔진 내에 **TTL 기반 결과 캐싱(Materialized View/Cache)**을 활성화하여 1초 내 즉시 반환 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 지난 30년간 기업들은 "모든 데이터를 단 하나의 물리적 데이터웨어하우스로 모으겠다"는 거대한 환상에 수천억을 쏟아부었지만, 대부분 실패했다.
> 데이터의 형태와 생성 속도가 너무나 다양해진 현대에 모든 데이터를 한곳에 물리적으로 복제하는 것은 불가능하다.
> 로지컬 DW의 진정한 위대함은 **"데이터의 물리적 소유권을 현업 도메인에 남겨둔 채, 논리적으로만 전사 통합 뷰를 제공하는 데이터 패브릭(Data Fabric)의 핵심 엔진"**이라는 점이다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "극단적 순수 가상화 만능주의의 경계와 하이브리드 레이크하우스(Lakehouse) 결합 모델"을 제언하겠다. 수년간의 대용량 과거 이력 데이터는 오픈 테이블 포맷(Apache Iceberg) 기반의 Data Lakehouse에 물리적으로 적재하고, 최신 트랜잭션 데이터만 운영계 RDB를 직접 가상화하여 결합하는 '하이브리드 로지컬 DW'가 실무에서 가장 성공 확률이 높은 골든 아키텍처임을 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 전사 데이터 파편화 해소와 실시간 분석 요구를 충족하기 위해 데이터 가상화 기반의 로지컬 DW 도입이 타당함.
- **대응**:
  1. **하이브리드 아키텍처 설계**: 정적 대용량 이력은 Iceberg Lakehouse에 물리 적재, 실시간 데이터는 Trino 가상화 연합으로 이원화.
  2. **원천 운영계 격리**: 가상화 쿼리의 OLTP 침범을 방지하기 위해 반드시 Read Replica 및 리소스 거버너(Resource Governor) 설정.
  3. **쿼리 푸시다운 극대화**: Trino 커넥터 최적화를 통해 술어/프로젝션 푸시다운율 90% 이상 유지.
- **검증**: 가상화 쿼리 P95 응답시간 3초 이내 및 운영계 트랜잭션 영향도 0% 검증.
- **효과**: 신규 데이터 소스 연동 기간을 수개월에서 3일 이내로 단축 및 스토리지 TCO 60% 절감.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">물리적 ETL 복제 비용 폭증, T+1 배치 지연, 스키마 경직성</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">데이터 가상화 기반 로지컬 DW 및 쿼리 푸시다운 아키텍처</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">쿼리 푸시다운율 90% 이상, Read Replica 분리, P95 &lt; 3초</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">Zero-Copy 실시간 데이터 분석 실현 및 스토리지 TCO 60% 절감</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제121회 정보관리 2교시: 가트너가 제시한 로지컬 데이터웨어하우스(Logical Data Warehouse)의 개념과 특징 및 전통적 물리 DW와의 비교
- **검증 출처**:
  - Gartner Research, "The Logical Data Warehouse Architecture", Mark A. Beyer
  - Martin Traverso et al., "Presto: SQL on Everything", IEEE ICDE
---

## 연결 토픽

- 상위 토픽: [03-039 OLAP](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/039_olap.md)
- 연관 토픽: [03-007 데이터 레이크](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/007_data_lake.md), [03-132 논리적 데이터 웨어하우스](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/132_logical_data_warehouse.md)
