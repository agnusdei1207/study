---
sidebar:
  order: 81
  label: "081. CRUD 매트릭스 (CRUD Matrix)"
  badge:
    text: "A"
    variant: note
title: "CRUD 매트릭스 (CRUD Matrix) 및 프로세스-데이터 정합성 검증"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 81
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "081"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터 모델링·무결성</span><strong>CRUD 매트릭스</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">CRUD 매트릭스 구조 및 핵심 점검 원칙</text>

  <!-- Table Graphic Canvas -->
  <g transform="translate(30, 48)">
    <!-- Header Row -->
    <rect x="0" y="0" width="110" height="24" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="55" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">프로세스 \ 엔티티</text>

    <rect x="110" y="0" width="70" height="24" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="145" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">고객</text>

    <rect x="180" y="0" width="70" height="24" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="215" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">주문</text>

    <rect x="250" y="0" width="70" height="24" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="285" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">결제</text>

    <rect x="320" y="0" width="70" height="24" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="355" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">배송</text>

    <rect x="390" y="0" width="70" height="24" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="425" y="16" font-size="8" fill="#64748b" text-anchor="middle">행 점검</text>

    <!-- Row 1: 회원가입 -->
    <rect x="0" y="24" width="110" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="10" y="40" font-size="8.5" fill="#334155">1. 회원가입</text>
    <rect x="110" y="24" width="70" height="24" fill="#dbeafe" stroke="#93c5fd"/>
    <text x="145" y="40" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">C</text>
    <rect x="180" y="24" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="215" y="40" font-size="8.5" fill="#94a3b8" text-anchor="middle">-</text>
    <rect x="250" y="24" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="285" y="40" font-size="8.5" fill="#94a3b8" text-anchor="middle">-</text>
    <rect x="320" y="24" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="355" y="40" font-size="8.5" fill="#94a3b8" text-anchor="middle">-</text>
    <rect x="390" y="24" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="425" y="40" font-size="7.5" fill="#047857" text-anchor="middle">OK (C)</text>

    <!-- Row 2: 주문신청 -->
    <rect x="0" y="48" width="110" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="10" y="64" font-size="8.5" fill="#334155">2. 주문신청</text>
    <rect x="110" y="48" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="145" y="64" font-size="8.5" fill="#334155" text-anchor="middle">R</text>
    <rect x="180" y="48" width="70" height="24" fill="#dbeafe" stroke="#93c5fd"/>
    <text x="215" y="64" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">C</text>
    <rect x="250" y="48" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="285" y="64" font-size="8.5" fill="#94a3b8" text-anchor="middle">-</text>
    <rect x="320" y="48" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="355" y="64" font-size="8.5" fill="#94a3b8" text-anchor="middle">-</text>
    <rect x="390" y="48" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="425" y="64" font-size="7.5" fill="#047857" text-anchor="middle">OK (C,R)</text>

    <!-- Row 3: 결제처리 -->
    <rect x="0" y="72" width="110" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="10" y="88" font-size="8.5" fill="#334155">3. 결제처리</text>
    <rect x="110" y="72" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="145" y="88" font-size="8.5" fill="#334155" text-anchor="middle">R</text>
    <rect x="180" y="72" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="215" y="88" font-size="8.5" fill="#334155" text-anchor="middle">U</text>
    <rect x="250" y="72" width="70" height="24" fill="#dbeafe" stroke="#93c5fd"/>
    <text x="285" y="88" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">C</text>
    <rect x="320" y="72" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="355" y="88" font-size="8.5" fill="#94a3b8" text-anchor="middle">-</text>
    <rect x="390" y="72" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="425" y="88" font-size="7.5" fill="#047857" text-anchor="middle">OK (C,R,U)</text>

    <!-- Row 4: 배송지시 -->
    <rect x="0" y="96" width="110" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="10" y="112" font-size="8.5" fill="#334155">4. 배송지시</text>
    <rect x="110" y="96" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="145" y="112" font-size="8.5" fill="#334155" text-anchor="middle">R</text>
    <rect x="180" y="96" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="215" y="112" font-size="8.5" fill="#334155" text-anchor="middle">R</text>
    <rect x="250" y="96" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="285" y="112" font-size="8.5" fill="#334155" text-anchor="middle">R</text>
    <rect x="320" y="96" width="70" height="24" fill="#dbeafe" stroke="#93c5fd"/>
    <text x="355" y="112" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">C</text>
    <rect x="390" y="96" width="70" height="24" fill="#ffffff" stroke="#e2e8f0"/>
    <text x="425" y="112" font-size="7.5" fill="#047857" text-anchor="middle">OK (C,R)</text>

    <!-- Bottom: Column Verification -->
    <rect x="0" y="120" width="110" height="24" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="55" y="136" font-size="8" fill="#64748b" text-anchor="middle">열 점검 (C/R 검사)</text>
    <rect x="110" y="120" width="70" height="24" fill="#f0fdf4" stroke="#86efac"/>
    <text x="145" y="136" font-size="8" font-weight="bold" fill="#15803d" text-anchor="middle">C, R (OK)</text>
    <rect x="180" y="120" width="70" height="24" fill="#f0fdf4" stroke="#86efac"/>
    <text x="215" y="136" font-size="8" font-weight="bold" fill="#15803d" text-anchor="middle">C, R, U (OK)</text>
    <rect x="250" y="120" width="70" height="24" fill="#f0fdf4" stroke="#86efac"/>
    <text x="285" y="136" font-size="8" font-weight="bold" fill="#15803d" text-anchor="middle">C, R (OK)</text>
    <rect x="320" y="120" width="70" height="24" fill="#f0fdf4" stroke="#86efac"/>
    <text x="355" y="136" font-size="8" font-weight="bold" fill="#15803d" text-anchor="middle">C (R누락?)</text>
    <rect x="390" y="120" width="70" height="24" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="425" y="136" font-size="7.5" fill="#1e40af" text-anchor="middle">완전성검사</text>
  </g>

  <!-- Bottom Guidelines -->
  <g transform="translate(30, 205)">
    <rect x="0" y="0" width="460" height="52" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="12" y="18" font-size="8.5" font-weight="bold" fill="#0f172a">&bull; 규칙 1 (전수 C/R): 모든 엔티티는 최소 1개의 'C'(생성)와 1개의 'R'(조회) 필수 (고아/사석 방지)</text>
    <text x="12" y="34" font-size="8.5" font-weight="bold" fill="#0f172a">&bull; 규칙 2 (단일 생성자): 엔티티 'C'는 가급적 1개 프로세스만 전담 (품질 불일치 차단)</text>
    <text x="12" y="48" font-size="8" fill="#475569">&bull; 표기 우선순위: C (Create) &gt; D (Delete) &gt; U (Update) &gt; R (Read)</text>
  </g>
</svg>
</div>

- 본질: **비즈니스 업무 프로세스(Process)와 데이터 모델의 엔티티(Entity) 간의 상호 작용(Create, Read, Update, Delete)을 2차원 표 형태로 매핑하여, 프로세스 정의의 누락과 데이터 모델의 불일치를 사전에 전수 검증하고 시스템 경계 분할 및 테스트 케이스 도출의 근간을 제공하는 품질 검증 도구**
- 암기: `행-열-교-검` (행: 단위 프로세스, 열: 엔티티 타입, 교차점: CRUD 행위, 검증: 전수 C/R 규칙) / `단-고-더` (단일 생성자 원칙, 고아 엔티티 배제, 더미 프로세스 배제)
- 판단축:
  - **CRUD 매트릭스**: 프로세스와 데이터 간의 '정적 연관성' 및 '생성·사용 완전성'을 2차원 표로 전수 감사
  - **데이터 흐름도(DFD)**: 프로세스 간 데이터가 이동하는 '동적 흐름'과 '입출력 파이프라인'을 방향성 그래프로 가시화
- 주의: 프로젝트 초기 엑셀로 한 번 작성된 CRUD 매트릭스는 개발 단계에서 소스코드와 동기화되지 않고 방치되기 쉬우므로, JPA/MyBatis 매퍼와 컨트롤러 어노테이션을 정적 분석하여 CI 빌드 시 자동 검증하는 아키텍처 파이프라인이 수반되어야 함
---

## 1교시 예상문제 (10점)

> CRUD 매트릭스 (CRUD Matrix) 및 프로세스-데이터 정합성 검증의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. CRUD 매트릭스의 개념 및 사용 목적

- **개념**: 업무 프로세스와 엔티티 간의 상관관계(Create/Read/Update/Delete)를 2차원 표로 검증하는 품질 도구
- **사용 목적**:
  - 프로세스와 데이터 모델 간의 누락 및 불일치 사전 검증
  - 엔티티의 생성(C) 및 활용(R) 완전성 감사 (고아/사석 엔티티 차단)
  - 서브시스템(MSA) 경계 분할 및 통합 테스트 시나리오 도출 기준 제공

### 2. CRUD 매트릭스 표현 방법 및 3대 점검 규칙

1. **표현 방법**:
   - **행(Rows)**: 단위 업무 프로세스 (시간 흐름 순 배치)
   - **열(Columns)**: 데이터 모델의 엔티티 타입 (생명주기 순 배치)
   - **셀(Cells)**: C, R, U, D 표기 (단일 표기 시 우선순위: $C > D > U > R$)
2. **3대 점검 규칙**:
   - **규칙 1 (엔티티 점검)**: 모든 엔티티는 반드시 최소 1개의 'C'와 1개의 'R'을 가져야 함
   - **규칙 2 (단일 생성자)**: 엔티티 생성(C)은 원칙적으로 단 1개의 프로세스만 전담
   - **규칙 3 (프로세스 점검)**: 모든 프로세스는 최소 1개 이상의 엔티티를 조작해야 함

### 3. 실무 아키텍처 제언

- 수기 엑셀 작성의 한계를 탈피하여 CI 파이프라인에서 소스코드 정적 분석(AST)을 통해 CRUD 매트릭스를 자동 생성하고 정합성을 검증하는 아키텍처 거버넌스 수립
---

### 핵심 관계

| 점검 규칙 | 주요 점검 내용 | 위반 시 발생하는 결함 | 해결 및 보정 방안 |
|:---|:---|:---|:---|
| **1. 엔티티 점검 (열)** | 모든 엔티티는 최소 1개의 'C'와 1개의 'R'을 가져야 함 | C 누락 시: 미생성 고아 엔티티<br>R 누락 시: 사용 안 되는 사석(Dead) 엔티티 | 데이터 생성 프로세스를 추가하거나, 불필요한 고아/사석 엔티티 폐기 |
| **2. 단일 생성자 원칙** | 특정 엔티티의 'C'는 가급적 단 1개의 프로세스만 전담 | 여러 프로세스가 동시 C 수행 시 생성 로직 파편화 및 정합성 충돌 | 생성 전담 서비스/API를 일원화하여 단일 진입점 구축 |
| **3. 프로세스 점검 (행)** | 모든 프로세스는 최소 1개 엔티티에 C, R, U, D 수행 | 어떤 데이터도 조작하지 않는 더미 프로세스(Dummy Process) 존재 | 업무 재설계를 통해 무의미한 프로세스 통폐합 |

---

## 2~4교시 예상문제 (25점)

> 데이터 모델링 및 소프트웨어 분석·설계 단계에서 사용되는 CRUD 매트릭스(Matrix)의 개념과 사용하는 목적을 설명하고, 매트릭스의 표현 방법(행, 열, 교차점 및 우선순위)과 모델의 완전성을 보장하기 위한 3대 검증 규칙을 서술하시오. (10점 / 25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 프로세스와 데이터의 정합성을 검증하는 CRUD 매트릭스 개요

#### 한줄 요약: 업무 프로세스와 데이터 엔티티를 2차원 행렬로 교차 매핑하여 누락과 불일치를 검증하는 소프트웨어 공학 도구

- **추진 배경**:
  - 시스템 구축 시 현업 기능 요구사항을 분석하는 프로세스 관점(기능 분할도)과 정보 구조를 설계하는 데이터 관점(ERD)이 서로 다른 담당자에 의해 독립적으로 진행되는 경향이 있음
  - 이로 인해 엔티티를 만들어 놓고 생성(Insert)하는 기능이 누락되거나, 화면은 설계되었는데 저장할 DB 테이블이 없는 치명적 설계 불일치가 발생함
- **CRUD 매트릭스의 정의**:
  - 업무 프로세스를 행(Row)으로, 데이터 모델의 엔티티 타입을 열(Column)으로 배치하고, 양자가 교차하는 셀에 **생성(Create), 조회(Read), 수정(Update), 삭제(Delete)**의 발생 여부를 표기한 2차원 연관 분석 행렬

### Ⅱ. CRUD 매트릭스의 구성 요소 및 표현 방법

#### 한줄 요약: 행의 단위 프로세스와 열의 엔티티 타입이 만나는 교차점에 C > D > U > R의 우선순위로 데이터 행위를 표기

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 120" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="100" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">CRUD 매트릭스 구성 요소 및 우선순위 체계</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="145" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="72" y="18" font-size="9.5" font-weight="bold" fill="#1e40af" text-anchor="middle">행 (Rows) - 프로세스</text>
    <text x="72" y="34" font-size="8" fill="#334155" text-anchor="middle">최하위 단위 업무 프로세스</text>
    <text x="72" y="47" font-size="8" fill="#64748b" text-anchor="middle">시간적 업무 흐름 순 배치</text>

    <rect x="160" y="0" width="145" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="232" y="18" font-size="9.5" font-weight="bold" fill="#1e40af" text-anchor="middle">열 (Columns) - 엔티티</text>
    <text x="232" y="34" font-size="8" fill="#334155" text-anchor="middle">ERD 핵심 엔티티 타입</text>
    <text x="232" y="47" font-size="8" fill="#64748b" text-anchor="middle">데이터 라이프사이클 순</text>

    <rect x="320" y="0" width="145" height="55" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="392" y="18" font-size="9.5" font-weight="bold" fill="#1e40af" text-anchor="middle">셀 (Cells) - 표기 우선순위</text>
    <text x="392" y="34" font-size="8.5" font-weight="bold" fill="#dc2626" text-anchor="middle">C &gt; D &gt; U &gt; R</text>
    <text x="392" y="47" font-size="8" fill="#475569" text-anchor="middle">복수 시 병기 or 우선순위</text>
  </g>
</svg>
</div>

### 1. 매트릭스 구성 요소 상세
1. **행(Rows) - 업무 프로세스**:
   - 업무 기능 분할도(FDD)의 최하위 레벨에 위치하는 단위 작업(Activity)을 시간적 업무 흐름 순서대로 위에서 아래로 배열
2. **열(Columns) - 엔티티 타입**:
   - 데이터 모델링(ERD)에서 도출된 핵심 엔티티들을 데이터 라이프사이클 순서(기준 데이터 $\rightarrow$ 기본 엔티티 $\rightarrow$ 중심 엔티티 $\rightarrow$ 행위 엔티티)로 좌에서 우로 배열
3. **교차점(Cells) - 데이터 조작 행위**:
   - 해당 프로세스가 해당 엔티티에 대해 수행하는 데이터베이스 작업(C, R, U, D)을 기재

### 2. 복수 액션 발생 시 표기 원칙
- 한 프로세스에서 동일 엔티티에 대해 복수의 조작이 일어날 경우(예: Read 후 Update):
  - **원칙 1**: `R, U`와 같이 콤마(,)를 병기하여 모든 행위를 정확히 표현
  - **원칙 2 (단일 문자 표기 시)**: 데이터 생명주기에 미치는 중요도에 따라 **$C > D > U > R$** 우선순위 적용 (예: Read 후 Create 수행 시 'C'로 대표 표기)

### Ⅲ. CRUD 매트릭스 핵심 점검 3대 규칙 (Verification Rules)

#### 한줄 요약: 고아 엔티티 방지를 위한 전수 C/R 검사, 중복 충돌을 방지하는 단일 생성자 원칙, 더미 프로세스 배제

| 점검 규칙 | 주요 점검 내용 | 위반 시 발생하는 결함 | 해결 및 보정 방안 |
|:---|:---|:---|:---|
| **1. 엔티티 점검 (열)** | 모든 엔티티는 최소 1개의 'C'와 1개의 'R'을 가져야 함 | C 누락 시: 미생성 고아 엔티티<br>R 누락 시: 사용 안 되는 사석(Dead) 엔티티 | 데이터 생성 프로세스를 추가하거나, 불필요한 고아/사석 엔티티 폐기 |
| **2. 단일 생성자 원칙** | 특정 엔티티의 'C'는 가급적 단 1개의 프로세스만 전담 | 여러 프로세스가 동시 C 수행 시 생성 로직 파편화 및 정합성 충돌 | 생성 전담 서비스/API를 일원화하여 단일 진입점 구축 |
| **3. 프로세스 점검 (행)** | 모든 프로세스는 최소 1개 엔티티에 C, R, U, D 수행 | 어떤 데이터도 조작하지 않는 더미 프로세스(Dummy Process) 존재 | 업무 재설계를 통해 무의미한 프로세스 통폐합 |

### Ⅳ. CRUD 매트릭스 vs 데이터 흐름도(DFD) vs 트랜잭션 매트릭스

#### 한줄 요약: 정적 완전성을 보는 CRUD, 동적 데이터 흐름을 보는 DFD, 실행 볼륨과 빈도를 보는 트랜잭션 매트릭스

| 비교 항목 | CRUD 매트릭스 | 데이터 흐름도 (DFD) | 트랜잭션 매트릭스 |
|:---|:---|:---|:---|
| **분석 관점** | **정적(Static) 연관성** 및 완전성 | **동적(Dynamic) 데이터 흐름** | **정량적(Quantitative) 부하** |
| **표현 형태** | 2차원 표 (행렬) | 방향성 네트워크 그래프 | 2차원 표 + 주기/트래픽 건수 |
| **주요 목적** | 프로세스와 데이터 모델 간 **누락/정합성 감사** | 시스템 간 입력/출력/저장소 **데이터 전달 경로 가시화** | 데이터베이스 용량 산정 및 **I/O 병목 사전 예측** |
| **작성 시점** | 분석 및 논리 모델링 단계 | 요구분석 및 시스템 분석 단계 | 물리 모델링 및 DB 튜닝 단계 |
| **도출 산출물** | 엔티티/프로세스 보정, MSA 경계 | 프로세스 명세서, 인터페이스 정의 | 디스크 I/O 분산 계획, 인덱스 설계 |

### Ⅴ. 시스템 분석·설계 및 아키텍처 관점의 실무 활용 가치

#### 한줄 요약: 마이크로서비스(MSA) 서비스 경계 분할, DB 락 경합 지점 식별, 통합 테스트 케이스 자동화의 근간

### 1. 도메인 주도 설계(DDD) 및 마이크로서비스 경계(Bounded Context) 분할
- CRUD 매트릭스에서 특정 엔티티들에 대해 C와 U를 공유하는 프로세스 군집을 클러스터링
- 응집도가 높은 엔티티-프로세스 그룹을 단일 마이크로서비스로 도출함으로써 서비스 간 불필요한 분산 트랜잭션을 최소화

### 2. 데이터베이스 동시성 락(Lock) 경합 및 트랜잭션 병목 사전 예측
- 특정 핵심 엔티티(예: 재고, 계좌)의 셀에 다수의 프로세스가 'U'(Update)와 'D'(Delete)를 동시에 점유하고 있다면, 해당 테이블은 극심한 락 경합 및 데드락 후보군으로 사전 식별 가능 $\rightarrow$ 비관적 락 또는 Redis 분산 락 설계 선반영

### 3. 통합 테스트(Integration Test) 시나리오 완전성 검증
- 모든 엔티티가 `Create $\rightarrow$ Read $\rightarrow$ Update $\rightarrow$ Delete`의 전 생명주기를 거치는 테스트 시나리오를 빠짐없이 도출할 수 있는 완벽한 가이드라인 제공

### Ⅵ. 프로젝트 현장 장애 패턴과 대응 전략

#### 한줄 요약: 수기 엑셀 문서화로 인한 사장화(Shelfware) 문제를 극복하고 코드 기반 정적 분석으로 지속적 동기화 구현

- **"엑셀에 갇혀 죽어버린 CRUD 매트릭스"**:
  - 분석 단계에서 감리 통과용으로 엑셀 표를 화려하게 채운 뒤, 개발 단계에서 요구사항이 변경되면 코드는 바뀌는데 CRUD 매트릭스는 수정되지 않아 문서와 시스템이 완전히 괴리됨
- **코드 기반 역공학(Reverse Engineering) 파이프라인 구축**:
  - Spring Boot 컨트롤러(`@PostMapping`, `@GetMapping`)와 ORM 레포지토리(JPA `save()`, `findById()`)의 정적 AST(Abstract Syntax Tree)를 파싱
  - 빌드(CI) 시점에 실제 소스코드와 DB 스키마 간의 CRUD 매트릭스를 자동 생성하고, C나 R이 누락된 엔티티가 감지되면 빌드를 실패시키는 자동화 거버넌스 도입

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> CRUD 매트릭스는 단순한 "감리용 엑셀 문서"가 아니라 **"소프트웨어 아키텍처 경계 분할(Bounded Context)과 테스트 완전성을 증명하는 수학적 연관 행렬"**이다. 현업 프로젝트의 가장 큰 병폐는 분석 때 작성한 엑셀 매트릭스가 개발 중 코드와 동기화되지 않고 버려진다는 점이다. 최신 아키텍처에서는 CI/CD 파이프라인에 AST 정적 분석기를 연결하여 소스코드의 Repository 호출부를 스캔해 CRUD 매트릭스를 자동 갱신하고, C나 R이 누락된 고아 테이블이 발견되면 빌드를 중단시키는 **"지속적 CRUD 거버넌스(Continuous Architecture)"**를 확립해야 한다.

> **[나라면 이렇게 쓴다]**
> 10점형이라면 가상의 전자상거래 4개 프로세스 $\times$ 4개 엔티티 표를 그리고 셀 표기 우선순위($C > D > U > R$)와 3대 점검 규칙(C/R 전수, 단일 생성자, 더미 배제)을 명쾌하게 쓰겠다. 25점형이라면 CRUD 클러스터링을 통한 MSA 서비스 경계 분할 기법과 CI 파이프라인 연계 자동화 거버넌스를 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 수기 작성된 CRUD 엑셀의 사장화로 개발 코드와의 괴리 발생 및 미생성 고아 엔티티 방치
- **대응 (개선 방안)**: CI 빌드 파이프라인에 소스코드 AST 정적 분석 기반 CRUD 자동 추출 엔진 구축 및 3대 검증 규칙 자동 게이트웨이화
- **검증 (검증 기준)**: 모든 엔티티의 C/R 충족률 100% 검증, 단일 생성자 위반 0건 유지, 코드-매트릭스 일치도 99% 달성
- **효과 (실행 효과)**: 설계-개발 간 누락 결함 80% 사전 차단, 통합 테스트 시나리오 커버리지 100% 확보 및 감리 통과율 제고

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">수기 엑셀 사장화 및 프로세스-엔티티 간 누락/불일치 방치</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">코드 AST 정적 분석 기반 CRUD 매트릭스 CI 자동 추출 및 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">C/R 충족률 100%, 단일 생성자 준수, 소스코드-ERD 일치도 &ge; 99%</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">설계 누락 결함 80% 감소 및 MSA 서비스 경계 도출 최적화</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제133회 1교시 7번 (데이터모델링에서 CRUD 매트릭스의 목적과 표현 방법)
  - 컴퓨터시스템응용기술사 제121회 1교시 (데이터 모델링 분석 도구와 상관모델링)
  - 정보관리기술사 제110회 2교시 (정보공학 방법론의 프로세스와 데이터 연관 분석)
- **표준 및 검증 출처**:
  - James Martin, *Information Engineering, Book II: Planning & Analysis*, Prentice Hall
  - 한국데이터산업진흥원(K-Data), *SQL 전문가 가이드 - 데이터 모델과 성능*
  - 행정안전부 공공데이터베이스 표준화 관리 지침
---

## 연결 토픽

- [042. 데이터 모델링 (Data Modeling)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/042_data_modeling.md)
- [028. ERD (Entity Relationship Diagram)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/028_erd.md)
- [070. 참조 무결성 (Referential Integrity)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/070_referential_integrity.md)
