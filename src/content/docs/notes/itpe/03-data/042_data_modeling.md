---
author: "Antigravity"
category: "03-data"
date: "2026-09-20T17:05:00+09:00"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
  question_no: "042"
sidebar:
  badge:
    text: "A"
    variant: "note"
  label: "042. 데이터 모델링"
  order: 42
tags:
  - "notes-data"
title: "데이터 모델링 (Data Modeling) 및 식별·비식별 관계"
weight: 42
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 설계</span><span>데이터베이스 아키텍처·모델링</span><strong>데이터 모델링</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 160" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="160" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Top: Requirement -->
  <rect x="170" y="10" width="180" height="24" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="260" y="26" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">현실 세계 비즈니스 요구사항</text>
  <line x1="260" y1="34" x2="260" y2="44" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-dm)"/>

  <!-- 3 Steps Stack -->
  <rect x="20" y="46" width="480" height="28" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <text x="35" y="64" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">1. 개념 모델링</text>
  <text x="135" y="64" font-size="8.5" fill="var(--color-text, #334155)">주제 영역 정의, 핵심 엔티티(Core Entity) 도출, 개념 ERD (추상화 최고)</text>

  <line x1="260" y1="74" x2="260" y2="82" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-dm)"/>

  <rect x="20" y="82" width="480" height="30" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <text x="35" y="101" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">2. 논리 모델링</text>
  <text x="135" y="101" font-size="8.5" fill="var(--color-primary-dark, #0369a1)">정규화(1NF~BCNF), 식별/비식별 관계, M:N 해소 (DBMS 독립적 SSOT)</text>

  <line x1="260" y1="112" x2="260" y2="120" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-dm)"/>

  <rect x="20" y="120" width="480" height="30" fill="var(--color-success-light, #dcfce7)" stroke="var(--color-success, #16a34a)" stroke-width="1.2" rx="4"/>
  <text x="35" y="139" font-size="9.5" font-weight="bold" fill="var(--color-success-dark, #15803d)">3. 물리 모델링</text>
  <text x="135" y="139" font-size="8.5" fill="var(--color-text, #0f172a)">테이블/컬럼 변환, 데이터 타입, 물리 인덱스, 파티셔닝, 계획된 반정규화</text>

  <defs>
    <marker id="arrow-dm" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <polygon points="0 0, 5 2.5, 0 5" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **복잡한 현실 세계의 비즈니스 규칙과 프로세스 데이터를 개념 $\to$ 논리 $\to$ 물리의 3단계 계층적 추상화를 거쳐 컴퓨터 시스템이 효율적으로 저장·관리할 수 있는 정형화된 데이터베이스 구조로 변환하는 공학적 설계 과정**
- 암기: `개-논-물` (3단계 모델링) / `엔-속-관-식` (4대 구성요소: 엔티티 · 속성 · 관계 · 식별자)
- 식별 vs 비식별 관계 핵심:
  - **식별 관계(Identifying, 실선)**: 부모의 PK가 자식의 PK(주식별자)의 일부로 전속 상속 $\to$ 존재 의존성 강함, 복합키 비대화 위험
  - **비식별 관계(Non-identifying, 점선)**: 부모의 PK가 자식의 일반 속성(FK)으로 전속 상속 $\to$ 느슨한 결합, 외래키 NULL 허용 가능
- 주의: 논리 모델링 단계에서 성능을 핑계로 반정규화를 선반영하지 말 것 (비즈니스 무결성 오염 방지)

## 예상문제

> 관계형 데이터베이스(RDBMS) 구축을 위한 데이터 모델링의 개념과 3단계(개념, 논리, 물리) 수행 절차 및 산출물을 설명하고, 식별 관계와 비식별 관계의 개념, 장단점 및 설계 기준을 논하시오. (25점)

## Ⅰ. 비즈니스 규칙의 정보 자산화를 위한 데이터 모델링 개요

- 정의: **데이터 모델링(Data Modeling)**은 현실 세계의 업무 프로세스와 비즈니스 규칙을 정보화 시스템으로 구현하기 위해, 데이터의 실체와 연관 관계를 분석하여 정형화된 개념적·논리적·물리적 데이터 구조로 설계하고 문서화하는 엔지니어링 활동
- 목적: 업무의 중복을 제거하여 데이터 무결성(Integrity)과 단일 진실 공급원(SSOT)을 확립하고, 시스템 개발 및 유지보수 시 전사적 의사소통 기준선 제공
- 필요성: 명확한 데이터 모델링 없이 시스템을 구축하면 데이터 불일치(Data Drift), 무결성 파괴, 조인 성능 저하 및 잦은 스키마 변경으로 막대한 기술 부채 발생

#### 한줄 요약

- 데이터 모델링은 현실의 비즈니스 규칙을 데이터베이스가 이해할 수 있는 정형화된 논리와 물리 구조로 추상화하는 작업임

## Ⅱ. 데이터 모델링 3단계(개념·논리·물리) 계층 구조 및 특징

| 단계 | 주요 목적 | 핵심 수행 활동 | 대표 산출물 | 주관 주체 |
|---|---|---|---|---|
| **개념 모델링<br>(Conceptual)** | 업무 범위 확정 및 핵심 비즈니스 엔티티 골격 수립 | 1. 주제 영역(Subject Area) 정의<br>2. 핵심 엔티티(Core Entity) 도출<br>3. 엔티티 간 핵심 관계 도출 | 개념 데이터 모델 다이어그램, 엔티티 정의서 | 현업 담당자, 비즈니스 분석가, DA |
| **논리 모델링<br>(Logical)** | 비즈니스 정보 구조와 규칙의 완전하고 명확한 정의 | 1. 모든 세부 속성 및 도메인 정의<br>2. 주식별자 및 대체키 확정<br>3. 관계 차수 및 식별/비식별 관계 결정<br>4. 정규화(1NF~BCNF) 및 M:N 해소 | 논리 ERD, 데이터 사전, 도메인 정의서, 엔티티 관계 기술서 | 데이터 모델러, 데이터 아키텍트(DA) |
| **물리 모델링<br>(Physical)** | 타깃 DBMS 엔진에 최적화된 물리 저장 구조 구현 | 1. 테이블, 컬럼 물리 명칭 부여<br>2. 데이터 타입 및 길이, NULL 제약 설정<br>3. 물리 인덱스, 테이블스페이스, 파티셔닝<br>4. 성능 조율을 위한 계획된 반정규화 | 물리 ERD, 스키마 DDL 스크립트, 저장 공간 산정서 | 데이터베이스 관리자(DBA), 시스템 엔지니어 |

#### 한줄 요약

- 개념 모델은 '무엇을(What)', 논리 모델은 '어떤 규칙으로(Rule)', 물리 모델은 '어떻게 저장할지(How)'를 결정함

## Ⅲ. 논리 모델의 관계 전이: 식별 관계 vs 비식별 관계 심층 비교

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 135" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="135" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Left: Identifying -->
  <rect x="15" y="12" width="240" height="110" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <rect x="15" y="12" width="240" height="22" fill="var(--color-primary-light, #e0f2fe)" rx="4"/>
  <text x="135" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">식별 관계 (Identifying: 실선 ──)</text>
  <text x="25" y="48" font-size="8.5" font-weight="bold" fill="var(--color-text, #0f172a)">부모 [주문] ─── 실선 ───&lt; 자식 [주문상세]</text>
  <text x="25" y="66" font-size="8" fill="var(--color-primary, #0284c7)">• 자식 PK = (#주문번호, #상세순번) 복합키</text>
  <text x="25" y="82" font-size="8" fill="var(--color-text, #334155)">• 부모 없이 자식 홀로 존재 불가 (NOT NULL)</text>
  <text x="25" y="98" font-size="8" fill="var(--color-success-dark, #15803d)">• 장점: 부모 조인 없이 자식 단독 조건 검색</text>
  <text x="25" y="112" font-size="7.5" fill="var(--color-danger, #ef4444)">• 단점: 다계층 상속 시 최하위 복합 PK 비대화</text>

  <!-- Right: Non-identifying -->
  <rect x="265" y="12" width="240" height="110" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2" rx="4"/>
  <rect x="265" y="12" width="240" height="22" fill="var(--color-surface, #f1f5f9)" rx="4"/>
  <text x="385" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #334155)">비식별 관계 (Non-identifying: 점선 ---)</text>
  <text x="275" y="48" font-size="8.5" font-weight="bold" fill="var(--color-text, #0f172a)">부모 [부서] - - - 점선 - - -&lt; 자식 [사원]</text>
  <text x="275" y="66" font-size="8" fill="var(--color-primary, #0284c7)">• 자식 PK = (#사번) / FK = (*부서코드)</text>
  <text x="275" y="82" font-size="8" fill="var(--color-text, #334155)">• 부모 없어도 자식 독립 존재 가능 (NULL 허용)</text>
  <text x="275" y="98" font-size="8" fill="var(--color-success-dark, #15803d)">• 장점: 복합키 비대화 차단, 낮은 결합도</text>
  <text x="275" y="112" font-size="7.5" fill="var(--color-text-muted, #64748b)">• 단점: 부모 속성 조회 시 추가 조인 발생</text>
</svg>
</div>

| 비교 항목 | 식별 관계 (Identifying) | 비식별 관계 (Non-identifying) |
|---|---|---|
| **기본 정의** | 부모 엔티티의 주식별자가 자식 엔티티의 **주식별자(PK) 구성원**으로 상속 | 부모 엔티티의 주식별자가 자식 엔티티의 **일반 속성(FK)**으로 상속 |
| **표기법** | **실선 (Solid Line)** | **점선 (Dashed Line)** |
| **인스턴스 생존 의존성** | 강한 존재 의존성 (부모 없는 자식 인스턴스 존재 불가) | 느슨한 연관성 (부모가 없어도 자식이 독립적으로 존재 가능) |
| **NULL 허용 여부** | PK의 구성원이 되므로 **NULL 절대 불가 (NOT NULL)** | 비즈니스 요건에 따라 **NULL 허용(Optional) 가능** |
| **장점** | 1. 부모 테이블 조인 없이 자식 테이블만으로 부모 ID 조건 검색 가능<br>2. 참조 무결성의 강력한 강제 | 1. 자식 테이블의 PK 컬럼 수가 단순화됨 (인조키 활용 용이)<br>2. 테이블 간 결합도(Coupling)가 낮아 스키마 변경에 유연 |
| **단점** | 1. 계층이 깊어질수록 최하위 자식의 복합 PK 컬럼 수가 기하급수적 비대화<br>2. SQL 조인 조건 복잡성 폭증 | 1. 부모의 세부 정보를 알기 위해 반드시 부모 테이블과의 조인 쿼리 발생<br>2. 무결성 통제 로직 필요 |

#### 한줄 요약

- 식별 관계(실선)는 부모-자식의 생사를 함께하는 강한 결합이고, 비식별 관계(점선)는 외래키로만 느슨하게 연결된 관계임

## Ⅳ. 식별·비식별 관계 선택 및 전환 기준

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 95" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="95" fill="var(--color-surface, #f8fafc)" rx="6" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Left: Identifying Recommendation -->
  <rect x="15" y="12" width="240" height="72" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-primary, #0284c7)" stroke-width="1" rx="4"/>
  <text x="135" y="28" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">식별 관계 채택 권장</text>
  <text x="25" y="46" font-size="8" fill="var(--color-text, #0f172a)">• 단독 존재 불가능한 종속 엔티티 (주문 ──▶ 주문상세)</text>
  <text x="25" y="60" font-size="8" fill="var(--color-text, #0f172a)">• M:N 해소용 교차 테이블 (수강생 ──▶ 수강 ◀── 강의)</text>
  <text x="25" y="74" font-size="8" fill="var(--color-text, #0f172a)">• 1:1 수평/수직 분할 테이블 (회원 ──▶ 회원상세)</text>

  <!-- Right: Non-identifying Recommendation -->
  <rect x="265" y="12" width="240" height="72" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="385" y="28" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #334155)">비식별 관계 전환 권장</text>
  <text x="275" y="46" font-size="8" fill="var(--color-danger, #ef4444)">• 상속 계층이 3단계 이상 깊어지는 경우 (PK 비대화 차단)</text>
  <text x="275" y="60" font-size="8" fill="var(--color-text, #334155)">• 마스터 코드, 부서 등 단순 참조 관계</text>
  <text x="275" y="74" font-size="8" fill="var(--color-text, #334155)">• 자식에 단일 인조키(Auto-increment ID) 적용 시</text>
</svg>
</div>

| 전환 시나리오 | 문제점 | 해결 설계 방안 |
|---|---|---|
| **다계층 식별 상속** | 본부 $\to$ 지사 $\to$ 부서 $\to$ 사원 $\to$ 급여로 이어져 급여 테이블 PK가 5개 복합키로 비대화 | 부서와 사원 단계에서 **비식별 관계(점선)**로 전환하고 사원에 단일 사번(인조키) 부여 |
| **지연된 부모 확정** | 주문서 작성 시 배송기사가 아직 배정되지 않는 비즈니스 예외 | 배송기사-주문 관계를 **선택적 비식별 관계(Optional Non-identifying, NULL 허용)**로 설정 |

#### 한줄 요약

- 1~2단계의 강한 부모-자식은 식별 관계를 쓰고, 3단계 이상이거나 단순 참조 관계는 비식별 관계로 끊어주는 것이 원칙임

## Ⅴ. 논리 데이터 모델에서 물리 데이터 모델로의 변환 규칙

| 논리 모델 구성요소 | 물리 모델 변환 대상 | 물리 설계 시 주요 결정 요소 |
|---|---|---|
| **엔티티 (Entity)** | **테이블 (Table)** | 물리 테이블 명명 규칙, 테이블스페이스 매핑, 예상 데이터 볼륨 |
| **속성 (Attribute)** | **컬럼 (Column)** | 물리 컬럼 명명, 데이터 타입(VARCHAR2, NUMBER), 컬럼 순서, NOT NULL |
| **주식별자 (Primary UID)**| **기본키 제약 (Primary Key)** | PK 인덱스 구조(Unique B*Tree), 클러스터드 여부, 스토리지 파라미터 |
| **관계 (Relationship)** | **외래키 제약 (Foreign Key)** | FK 인덱스 생성(Lock 경합 방지), 삭제 규칙(Cascade, Set Null, Restrict) |
| **다치 속성 / M:N 관계** | **교차 테이블 (Mapping Table)** | 1차 정규형 및 제약조건 준수를 위한 독립 물리 테이블 분해 |
| **비즈니스 제약조건** | **CHECK / DEFAULT 제약** | DBMS 레벨 검증, 기본값 선언, 가상 컬럼(Virtual Column) |

#### 한줄 요약

- 논리 요소는 엔티티$\to$테이블, 속성$\to$컬럼, 식별자$\to$PK, 관계$\to$FK/인덱스로 1:1 대응 매핑됨

## Ⅵ. 데이터 모델링 실무 실패 사례 및 엔지니어링 대책

| 문제 상황 | 근본 원인 | 실무 엔지니어링 대책 | 개선 효과 |
|---|---|---|---|
| **최하위 트랜잭션 테이블의 조인 조건 폭증** | 5단계 이상 식별 관계 상속으로 자식 테이블마다 5~6개 컬럼 복합 PK 누적 | 3단계 이상 엔티티는 **비식별 관계(점선)**로 전환하고 단일 인조 식별자(ID) 부여 | SQL 작성 간소화 및 PK 인덱스 크기 절감 |
| **외래키 인덱스 누락에 따른 테이블 락(Table Lock)** | RDBMS 물리 전환 시 FK 컬럼에 물리적 보조 인덱스를 미생성 | 모든 외래키(FK) 컬럼에 대해 **수동 B*Tree 인덱스 필수 생성** 룰셋 적용 | 부모 테이블 DML 시 자식 테이블 풀 락(Share Lock) 방지 |
| **배포 후 스키마 변경 시 모델 문서 사문화 (Drift)** | 개발자가 운영계 DB에 직접 DDL을 실행하고 ERD 갱신을 생략 | **GitOps 기반 스키마 마이그레이션(Liquibase/Flyway)** 파이프라인 의무화 | DDL 코드와 ERD 문서 100% 동기화 |
| **M:N 관계 미해소 상태로 테이블 생성** | 논리 모델링 검증 누락으로 쉼표(,) 구분자로 복수 데이터를 단일 컬럼에 저장 | CASE 툴 정적 검증기(Validator) 연동, M:N 검출 시 물리 DDL 생성 강제 차단 | 제1정규형(1NF) 준수 및 데이터 정합성 보장 |

#### 한줄 요약

- 식별자 누적 방지, 외래키 인덱스 필수화, DDL Git 형상관리가 데이터 모델링 실무 성공의 핵심임

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 엔터프라이즈 데이터 아키텍처에서 가장 흔하게 범하는 실수는 "조인 성능이 떨어질까 봐" 논리 데이터 모델링 단계부터 정규화를 포기하고 테이블을 비정규화(합체)하는 것이다. 논리 모델은 업무의 규칙과 비즈니스 인과관계를 정의하는 영역이며, 여기서 성능을 핑계로 모델을 오염시키면 향후 비즈니스가 변경되었을 때 데이터 무결성이 무너지고 시스템 전체가 수정 불능 상태에 빠진다.
>
> **[나라면 이렇게 쓴다]**
> "논리는 비즈니스 무결성에 엄격하고, 물리는 시스템 성능에 유연하게 대응한다"는 원칙을 확립하겠다. 논리 모델링 단계에서는 BCNF 정규화와 식별/비식별 관계 기준을 철저히 준수하여 단일 진실 공급원(SSOT)을 확립한다. 물리 모델링 단계에서 실제 예상 TPS와 볼륨을 산정한 후, 초당 수천 건 이상의 병목이 입증된 특정 경로에 한해서만 샤딩, 파티셔닝, 또는 계획된 역정규화를 사유서와 함께 승인하는 **이원화 거버넌스**를 수립하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 식별 관계 남용에 따른 복합 PK 비대화 및 외래키 인덱스 누락으로 인한 테이블 풀 락 발생.
- **대응 (개선 방안)**: 3단계 이상 비식별 관계 전환 및 인조키 부여, 모든 FK 컬럼 인덱스 생성 의무화 및 GitOps DDL 관리.
- **검증 (검증 기준)**: 복합키 컬럼 수 3개 이내 제한 및 외래키 컬럼 보조 인덱스 생성률 100% 정량 검증.
- **효과 (실행 효과)**: 조인 SQL 복잡도 50% 축소 및 부모-자식 DML 동시성 제어 락 경합 제로화 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">현행 한계</div>
    <div class="itpe-flow-desc">식별 관계 남용에 따른 복합키 비대화 및 FK 인덱스 누락 락 병목</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">개선 방안</div>
    <div class="itpe-flow-desc">3단계 이상 비식별 관계 전환 및 외래키 B*Tree 인덱스 필수화</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">검증 기준</div>
    <div class="itpe-flow-desc">PK 컬럼 수 3개 이내 제약 및 FK 인덱스 커버리지 100% 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">실행 효과</div>
    <div class="itpe-flow-desc">조인 쿼리 복잡도 50% 절감 및 DML 동시 트랜잭션 처리량 극대화</div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 데이터 모델링의 정의

- 비즈니스 요구사항과 데이터 규칙을 **개념(주제영역/골격) $\to$ 논리(정규화/무결성) $\to$ 물리(DBMS최적화)** 3단계로 추상화하여 RDBMS 구조로 완성하는 공학적 설계 절차

### 2. 식별 관계 vs 비식별 관계 핵심 비교

- **식별 관계 (실선)**: 부모 PK가 자식의 기본키(PK) 구성원으로 전속 상속 (강한 종속, 부모 없는 자식 불가)
- **비식별 관계 (점선)**: 부모 PK가 자식의 일반 외래키(FK) 속성으로 전속 상속 (느슨한 연관, NULL 허용 가능)

| 구분 | 식별 관계 (Identifying) | 비식별 관계 (Non-identifying) |
|---|---|---|
| 표기 / 키 전속 | 실선 (Solid) / 자식의 **기본키(PK)** 포함 | 점선 (Dashed) / 자식의 **외래키(FK)** 포함 |
| 장점 | 부모 조인 없이 자식 단독 조건 검색 가능 | 복합키 비대화 차단, 느슨한 결합도 |
| 단점 | 계층 심화 시 복합 PK 컬럼 수 폭증 | 부모 속성 조회 시 추가 조인 발생 |
| 적용 권장 | 강한 부모-자식 종속, 교차 엔티티 | 다계층 상속, 단순 코드 참조, 인조키 환경 |

### 3. 차별화 제언

- 3단계 이상 자식 테이블은 **비식별 관계로 전환**하여 복합키 비대화를 방지하고, 모든 외래키 컬럼에 **물리 B*Tree 인덱스를 필히 생성**하여 DML 시 테이블 락 경합을 원천 차단함

## 출제 이력과 검증 출처

- 제133회 4교시 4번: RDBMS를 적용하기 위한 데이터 모델링 (개념·논리·물리 3단계 절차 및 매핑 상세)
- 제128회 1교시: 식별 관계와 비식별 관계 비교
- [Data Modeling Essentials (Graeme Simsion & Graham Witt)](https://www.sciencedirect.com/book/9780126445510/data-modeling-essentials)
- [Oracle Database Concepts, Data Modeling and Relational Database Design](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/introduction-to-oracle-database.html)

## 학습 체크

- [ ] 개념, 논리, 물리 모델링의 목적, 주관 주체, 핵심 산출물을 구분할 수 있는가
- [ ] 식별 관계(실선)와 비식별 관계(점선)의 구조적 차이와 ERD 표기법을 도식화할 수 있는가
- [ ] 식별 관계 남용 시 발생하는 복합 PK 비대화 및 SQL 조인 복잡도 문제를 설명할 수 있는가
- [ ] 논리 모델 요소(엔티티, 속성, 식별자, 관계)의 물리 DB(테이블, 컬럼, PK, FK) 변환 규칙을 아는가
- [ ] Ⅶ 결론에서 논리 모델 무결성 우선 및 통제된 물리 반정규화 전략을 제시할 수 있는가

## 연결 토픽

- [ERD](./028_erd/) · [정규화](./019_normalization/) · [반정규화](./017_denormalization/) · [무결성 제약](./013_integrity_constraint/)
