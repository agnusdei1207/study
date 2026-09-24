---
sidebar:
  order: 63
  label: "063. 오픈소스 DBMS 전환"
  badge:
    text: "A"
    variant: note
title: "오픈소스 DBMS 전환 (Open Source DBMS Migration) 및 무중단 마이그레이션"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 63
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "063"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터베이스 아키텍처·마이그레이션</span><strong>오픈소스 DBMS 전환</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 270" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="250" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">상용 DBMS $\to$ 오픈소스 DBMS 무중단 마이그레이션 아키텍처</text>

  <!-- Left: Commercial DB -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="130" height="190" rx="6" fill="#ffffff" stroke="#ef4444" stroke-width="1.2"/>
    <rect x="0" y="0" width="130" height="28" rx="6" fill="#fee2e2"/>
    <text x="65" y="19" font-size="10.5" font-weight="bold" fill="#991b1b" text-anchor="middle">기존 상용 DBMS</text>
    <text x="65" y="44" font-size="9" fill="#7f1d1d" text-anchor="middle">(Oracle / MS-SQL)</text>

    <rect x="15" y="55" width="100" height="26" rx="3" fill="#fef2f2" stroke="#fca5a5"/>
    <text x="65" y="72" font-size="8.5" fill="#991b1b" text-anchor="middle">DDL / 스키마 객체</text>

    <rect x="15" y="90" width="100" height="26" rx="3" fill="#fef2f2" stroke="#fca5a5"/>
    <text x="65" y="107" font-size="8.5" fill="#991b1b" text-anchor="middle">대량 원천 데이터</text>

    <rect x="15" y="125" width="100" height="26" rx="3" fill="#fef2f2" stroke="#fca5a5"/>
    <text x="65" y="142" font-size="8.5" fill="#991b1b" text-anchor="middle">트랜잭션 Redo Log</text>

    <text x="65" y="174" font-size="8.5" fill="#64748b" text-anchor="middle">운영 트랜잭션 지속</text>
  </g>

  <!-- Middle: Migration Pipeline -->
  <g transform="translate(180, 50)">
    <!-- 1. Schema Conversion -->
    <path d="M 0 68 L 130 68" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="25" y="56" width="80" height="24" rx="3" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="65" y="72" font-size="8.5" font-weight="bold" fill="#1e40af" text-anchor="middle">1. SCT 변환</text>

    <!-- 2. Bulk Load -->
    <path d="M 0 103 L 130 103" stroke="#10b981" stroke-width="1.5"/>
    <rect x="20" y="91" width="90" height="24" rx="3" fill="#ecfdf5" stroke="#10b981"/>
    <text x="65" y="107" font-size="8.5" font-weight="bold" fill="#065f46" text-anchor="middle">2. 벌크 적재(Load)</text>

    <!-- 3. Realtime CDC -->
    <path d="M 0 138 L 130 138" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="15" y="126" width="100" height="24" rx="3" fill="#f5f3ff" stroke="#8b5cf6"/>
    <text x="65" y="142" font-size="8.5" font-weight="bold" fill="#5b21b6" text-anchor="middle">3. 실시간 CDC 복제</text>

    <!-- 4. Reverse CDC (Rollback) -->
    <path d="M 130 170 L 0 170" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
    <rect x="15" y="158" width="100" height="22" rx="3" fill="#fffbeb" stroke="#f59e0b"/>
    <text x="65" y="173" font-size="8" font-weight="bold" fill="#b45309" text-anchor="middle">4. 역복제 (비상 롤백)</text>
  </g>

  <!-- Right: Open Source DB -->
  <g transform="translate(340, 50)">
    <rect x="0" y="0" width="140" height="190" rx="6" fill="#ffffff" stroke="#2563eb" stroke-width="1.2"/>
    <rect x="0" y="0" width="140" height="28" rx="6" fill="#eff6ff"/>
    <text x="70" y="19" font-size="10.5" font-weight="bold" fill="#1e40af" text-anchor="middle">오픈소스 DBMS</text>
    <text x="70" y="44" font-size="9" fill="#1e40af" text-anchor="middle">(PostgreSQL / MySQL)</text>

    <rect x="15" y="55" width="110" height="26" rx="3" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="70" y="72" font-size="8.5" fill="#1e40af" text-anchor="middle">타깃 스키마 자동생성</text>

    <rect x="15" y="90" width="110" height="26" rx="3" fill="#ecfdf5" stroke="#a7f3d0"/>
    <text x="70" y="107" font-size="8.5" fill="#065f46" text-anchor="middle">초기 베이스라인 구성</text>

    <rect x="15" y="125" width="110" height="26" rx="3" fill="#f5f3ff" stroke="#ddd6fe"/>
    <text x="70" y="142" font-size="8.5" fill="#5b21b6" text-anchor="middle">실시간 동기화 (Lag 0)</text>

    <text x="70" y="174" font-size="8.5" font-weight="bold" fill="#059669" text-anchor="middle">★ Shadow Run &amp; Cutover</text>
  </g>
</svg>
</div>

- 본질: **상용 DBMS(Oracle 등)의 막대한 코어 기반 라이선스 및 유지보수 비용(Vendor Lock-in)을 탈피하고 클라우드 네이티브 환경의 탄력성을 확보하기 위해, 스키마 변환 도구(SCT)와 실시간 변경 데이터 캡처(CDC)를 활용하여 서비스 중단 없이 오픈소스 DBMS(PostgreSQL, MySQL)로 안전하게 이전하는 기술적·관리적 마이그레이션 체계**
- 암기: `분-변-적-복-검-컷` (대상 분석, 스키마 변환, 초기 적재, 실시간 복제, 정합성 검증, 컷오버) / `티-락-클-성` (TCO 절감, 벤더 락인 탈피, 클라우드 유연성, 성능/안정성 확보)
- 판단축:
  - **빅뱅(Big-Bang) 전환**: 일정 시간 시스템을 전면 셧다운 후 일괄 이관 $\rightarrow$ 다운타임 길고 실패 시 롤백 치명적 (중소형 시스템 적합)
  - **무중단 단계적(Phased / CDC) 전환**: 초기 적재 후 CDC로 실시간 동기화 상태를 유지하며 섀도우 런(Shadow Run) 후 수 초 내 컷오버 $\rightarrow$ 무중단 비즈니스 보장 (엔터프라이즈 필수)
- 주의: 오픈소스 DBMS 소프트웨어는 무료이지만, 상용 전용 패키지(PL/SQL, NVL, CONNECT BY, 힌트 절)의 재작성과 CBO 옵티마이저 차이에 따른 쿼리 튜닝 공수가 프로젝트 비용의 70% 이상을 차지하므로 철저한 사전 호환성 진단이 필수적임

## Ⅰ. 벤더 락인을 탈피하는 오픈소스 DBMS 전환 개요

#### 한줄 요약: 막대한 상용 라이선스 비용을 절감하고 클라우드 네이티브 현대화를 실현하기 위한 전략적 데이터베이스 이전 체계

- **추진 배경**:
  - **TCO(총소유비용) 절감 압박**: 상용 DBMS의 CPU 코어당 고액 라이선스 정책 및 매년 발생하는 22% 수준의 유지보수 비용 부담
  - **벤더 종속(Vendor Lock-in) 탈피**: 폐쇄적인 상용 솔루션 구조로 인한 시스템 확장성 및 기술 혁신 제약
  - **클라우드 네이티브 전환**: 컨테이너(K8s) 기반 오토스케일링 및 MSA 환경에서 오픈소스 관리형 DB(Amazon Aurora, Cloud SQL)의 우수한 연동성
- **오픈소스 DBMS 전환의 정의**:
  - 기존 상용 RDBMS에 구축된 데이터 모델, 스키마 객체(테이블, 인덱스, 뷰 등), 저장 프로시저(PL/SQL), 데이터 및 애플리케이션 SQL을 오픈소스 RDBMS로 무손실·무중단 이관하는 종합 엔지니어링 과정

## Ⅱ. 오픈소스 DBMS 전환 6단계 엔드투엔드 절차

#### 한줄 요약: 사전 분석부터 스키마 변환, 초기 적재, 실시간 CDC, 정합성 검증, 최종 컷오버로 이어지는 체계적 이행

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 130" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="110" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">오픈소스 DBMS 무중단 전환 6단계 프로세스</text>

  <g transform="translate(25, 45)">
    <!-- Step 1 -->
    <rect x="0" y="0" width="72" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="36" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 진단/선정</text>
    <text x="36" y="34" font-size="7.5" fill="#475569" text-anchor="middle">PL/SQL 분석</text>
    <text x="36" y="47" font-size="7.5" fill="#64748b" text-anchor="middle">복잡도 매트릭스</text>

    <!-- Step 2 -->
    <rect x="79" y="0" width="72" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="115" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">2. 스키마변환</text>
    <text x="115" y="34" font-size="7.5" fill="#475569" text-anchor="middle">SCT 도구 활용</text>
    <text x="115" y="47" font-size="7.5" fill="#64748b" text-anchor="middle">DDL/타입매핑</text>

    <!-- Step 3 -->
    <rect x="158" y="0" width="72" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="194" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 초기 적재</text>
    <text x="194" y="34" font-size="7.5" fill="#475569" text-anchor="middle">병렬 벌크 로딩</text>
    <text x="194" y="47" font-size="7.5" fill="#64748b" text-anchor="middle">pg_bulkload</text>

    <!-- Step 4 -->
    <rect x="237" y="0" width="72" height="55" rx="4" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="273" y="18" font-size="9" font-weight="bold" fill="#5b21b6" text-anchor="middle">4. 실시간 CDC</text>
    <text x="273" y="34" font-size="7.5" fill="#475569" text-anchor="middle">Redo Log 복제</text>
    <text x="273" y="47" font-size="7.5" fill="#64748b" text-anchor="middle">Debezium/Kafka</text>

    <!-- Step 5 -->
    <rect x="316" y="0" width="72" height="55" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <text x="352" y="18" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">5. 정합성검증</text>
    <text x="352" y="34" font-size="7.5" fill="#475569" text-anchor="middle">Shadow Run</text>
    <text x="352" y="47" font-size="7.5" fill="#64748b" text-anchor="middle">체크섬 대사</text>

    <!-- Step 6 -->
    <rect x="395" y="0" width="75" height="55" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="432" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">6. 최종 컷오버</text>
    <text x="432" y="34" font-size="7.5" fill="#475569" text-anchor="middle">DNS/VIP 절체</text>
    <text x="432" y="47" font-size="7.5" fill="#dc2626" text-anchor="middle">역복제 가동</text>
  </g>
</svg>
</div>

### 1. 단계별 핵심 활동 및 산출물

| 단계 | 주요 수행 내역 | 활용 도구 / 기술 | 핵심 산출물 |
|:---|:---|:---|:---|
| **1. 진단/선정** | DB 오브젝트 전수 조사, 함수 호환성 분석 | AWS SCT Report, ora2pg | 전환 복잡도 매트릭스, TCO 분석서 |
| **2. 스키마 변환** | DDL 변환, 데이터 타입 매핑, 파티셔닝 재구성 | AWS SCT, DBeaver | 타깃 오픈소스 DDL 스크립트 |
| **3. 초기 적재** | 대용량 테이블 병렬 추출 및 Direct Path Load | pg_bulkload, MySQL Loader | 초기 데이터 적재 완료 DB |
| **4. 실시간 복제** | 소스 트랜잭션 로그를 파싱하여 타깃에 반영 | Debezium, Kafka, GoldenGate | 실시간 동기화 상태 파이프라인 |
| **5. 검증/테스트** | 데이터 체크섬 비교, 프로덕션 쿼리 리플레이 | Apache SkyWalking, pgaudit | 데이터 정합성 보고서, 성능 리포트 |
| **6. 컷오버** | DNS/VIP 절체, 쓰기 권한 전환, 비상 롤백 대기 | Keepalived, AWS Route53 | 운영 이관 확인서 |

## Ⅲ. 이기종 DBMS 마이그레이션 핵심 기술 요소

#### 한줄 요약: 스키마 변환 도구(SCT), 트랜잭션 로그 기반 CDC, 섀도우 트래픽을 활용한 무중단 안전망 구축

- **SCT (Schema Conversion Tool)**:
  - 오라클 고유의 데이터 타입(`NUMBER`, `VARCHAR2`, `CLOB`)을 PostgreSQL 표준 타입(`NUMERIC`, `VARCHAR`, `TEXT`)으로 매핑하고 저장 프로시저 자동 변환율 평가
- **CDC (Change Data Capture) 기반 무중단 동기화**:
  - 소스 DB에 쿼리를 날리지 않고 물리적 트랜잭션 로그(Oracle Redo Log, MySQL Binlog, PostgreSQL WAL)를 직접 파싱
  - 소스 시스템의 부하를 1% 미만으로 억제하면서 밀리초 단위로 변경 사항을 캡처하여 오픈소스 DB에 복제
- **역복제(Reverse CDC)를 통한 롤백(Rollback) 안전장치**:
  - 컷오버 완료 직후 신규 오픈소스 DB에서 발생하는 변경 트랜잭션을 구 상용 DB로 거꾸로 복제(Reverse Replication)
  - 만약 오픈소스 DB에서 예상치 못한 치명적 장애가 발생할 경우, 데이터 유실 없이 수 분 내에 구 상용 DB로 트래픽을 원복할 수 있는 안전망 제공

## Ⅳ. 상용 DBMS(Oracle) vs 오픈소스 DBMS(PostgreSQL / MySQL) 심층 비교

#### 한줄 요약: 고비용 올인원 상용 제품과 유연성·확장성을 갖춘 오픈소스 진영의 아키텍처 및 비용 구조 비교

| 비교 항목 | 상용 DBMS (Oracle Database) | 오픈소스 DBMS (PostgreSQL) | 오픈소스 DBMS (MySQL) |
|:---|:---|:---|:---|
| **라이선스 모델** | 상용 라이선스 (코어당 수천만 원) + 연간 유지보수비 | 완전 오픈소스 (PostgreSQL License) | 오픈소스 (GPL / 상용 라이선스) |
| **ANSI SQL 준수율**| 자체 확장 문법 다수 포함 (오라클 방언) | **가장 높은 ANSI SQL 준수율** | 웹/애플리케이션 친화적 표준 준수 |
| **확장성 (Extension)**| 벤더가 제공하는 옵션만 사용 가능 | **pgvector, PostGIS 등 외부 플러그인 무한 확장** | 스토리지 엔진 플러그인 (InnoDB 등) |
| **트랜잭션 동시성** | Undo 세그먼트 기반 MVCC | Multi-version Tuple 기반 MVCC (VACUUM 필요) | Undo Log 기반 MVCC |
| **오라클 호환성** | 원본 | **가장 높음** (EDB Postgres는 95% 호환) | 보통 (일부 문법 차이 큼) |

## Ⅴ. 주요 기술적 난제와 엔지니어링 해결책

#### 한줄 요약: PL/SQL 패키지 변환 공수 폭증, 옵티마이저 실행계획 왜곡, 대량 데이터 이관 병목 극복 전략

### 1. 난제 1: 상용 고유 문법 및 PL/SQL 패키지 변환
- **문제점**: 수천 줄에 달하는 오라클 PL/SQL 패키지, 프로시저, 트리거, 복합 예외 처리는 오픈소스 DB로 자동 변환되지 않음
- **해결책**:
  - **아키텍처 현대화 병행**: DB에 박힌 비즈니스 로직을 백엔드 애플리케이션 계층(Spring Boot Service)으로 이관
  - **오라클 호환 엔진 채택**: PL/SQL 변환 공수가 너무 클 경우, 오라클 문법을 90% 이상 네이티브 지원하는 EDB Postgres Advanced Server를 브릿지로 채택

### 2. 난제 2: CBO(비용 기반 옵티마이저) 실행 계획 차이로 인한 성능 저하
- **문제점**: 오라클에서는 인덱스 레인지 스캔을 타던 복잡한 조인 쿼리가 PostgreSQL 전환 후 해시 조인이나 시퀀셜 스캔으로 풀리며 응답 지연 발생
- **해결책**:
  - PostgreSQL의 `ANALYZE`를 실행하여 통계 정보를 최신화하고, `random_page_cost`, `work_mem` 등 메모리 파라미터 튜닝
  - 필요 시 `pg_hint_plan` 확장을 설치하여 오라클 스타일의 힌트 절을 임시 활용

## Ⅵ. 컷오버(Cutover) 및 롤백 비상 대책 수립 전략

#### 한줄 요약: RTO를 수 분 이내로 단축하는 무중단 컷오버 타임라인과 양방향 CDC를 활용한 무손실 비상 롤백 체계

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 110" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="90" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">무중단 컷오버(Cutover) 타임라인 &amp; 롤백 안전망</text>

  <g transform="translate(25, 42)">
    <!-- T-2h -->
    <circle cx="20" cy="20" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="20" y="24" font-size="8" font-weight="bold" fill="#1e40af" text-anchor="middle">T-2h</text>
    <text x="20" y="46" font-size="7.5" fill="#475569" text-anchor="middle">복제 지연 0</text>

    <path d="M 36 20 L 110 20" stroke="#64748b" stroke-width="1.5"/>

    <!-- T-10m -->
    <circle cx="125" cy="20" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="125" y="24" font-size="8" font-weight="bold" fill="#1e40af" text-anchor="middle">T-10m</text>
    <text x="125" y="46" font-size="7.5" fill="#475569" text-anchor="middle">소스 쓰기제한</text>

    <path d="M 141 20 L 215 20" stroke="#64748b" stroke-width="1.5"/>

    <!-- T (Cutover) -->
    <circle cx="230" cy="20" r="15" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
    <text x="230" y="24" font-size="8.5" font-weight="bold" fill="#991b1b" text-anchor="middle">T (Cut)</text>
    <text x="230" y="46" font-size="7.5" font-weight="bold" fill="#dc2626" text-anchor="middle">VIP 절체</text>

    <path d="M 247 20 L 320 20" stroke="#64748b" stroke-width="1.5"/>

    <!-- T+5m -->
    <circle cx="335" cy="20" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="335" y="24" font-size="8" font-weight="bold" fill="#1e40af" text-anchor="middle">T+5m</text>
    <text x="335" y="46" font-size="7.5" fill="#475569" text-anchor="middle">역복제 가동</text>

    <path d="M 351 20 L 425 20" stroke="#64748b" stroke-width="1.5"/>

    <!-- T+1h -->
    <circle cx="440" cy="20" r="14" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
    <text x="440" y="24" font-size="8" font-weight="bold" fill="#065f46" text-anchor="middle">T+1h</text>
    <text x="440" y="46" font-size="7.5" fill="#065f46" text-anchor="middle">이관 완료</text>
  </g>
</svg>
</div>

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 오픈소스 DBMS 전환 프로젝트의 성패는 **"DB 엔진 교체"가 아니라 "애플리케이션 계층과의 결합도(Decoupling)"**에 달려 있다. DB 안에 거대한 PL/SQL 패키지와 오라클 고유 함수(`NVL`, `DECODE`, `ROWNUM`, `(+)` 외부조인)가 박혀 있다면 아무리 좋은 변환 도구를 써도 프로젝트가 좌초된다. 진정한 클라우드 전환을 위해서는 SQL을 표준화하고 비즈니스 로직을 백엔드 애플리케이션으로 끌어올리는 애플리케이션 리팩토링이 동반되어야 하며, 컷오버 시점에는 반드시 장애를 대비한 **역방향 CDC(Reverse Replication)**를 가동해 두어야 경영진의 의사결정을 이끌어낼 수 있다.

> **[나라면 이렇게 쓴다]**
> 25점형 답안이라면 2단에 6단계 절차와 함께 "Redo Log 기반 CDC 파이프라인(Debezium + Kafka)" 구조도를 명확히 그리고, 4단 제언에 "Reverse CDC를 통한 RPO=0 무손실 롤백 안전망"과 "애플리케이션 Data Access Layer 추상화(JPA/MyBatis 표준화)"를 차별화 포인트로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 상용 벤더 락인과 PL/SQL 고유 문법 종속으로 인한 클라우드 전환 지연 및 빅뱅 방식 전환 실패 시 서비스 마비 위험
- **대응 (개선 방안)**: 트랜잭션 로그 기반 실시간 CDC 파이프라인과 Shadow Run을 도입하고, 컷오버 즉시 역복제(Reverse CDC)를 가동하여 무손실 롤백 안전망 확보
- **검증 (검증 기준)**: CDC 복제 지연(Lag) 1초 미만 수렴 검증, 데이터 체크섬 100% 일치 확인, 컷오버 다운타임 5분 이내(RTO &le; 5m, RPO = 0)
- **효과 (실행 효과)**: DBMS TCO 70% 이상 절감, 특정 벤더 종속 원천 탈피, 클라우드 네이티브 MSA 아키텍처로의 유연한 확장성 확보

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">고액 라이선스 종속, PL/SQL 결합도 심화 및 전환 시 다운타임 위험</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">CDC 기반 무중단 동기화 + Shadow Run 검증 + Reverse CDC 안전망</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">CDC Lag &le; 1s, 데이터 체크섬 100% 일치, RTO &le; 5m, RPO = 0</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">DBMS TCO 70% 절감, 벤더 종속 해소 및 클라우드 네이티브 현대화</div>
  </div>
</div>

---

## 1교시 예상문제 (10점)

> 오픈소스 DBMS 전환 (Open Source DBMS Migration) 및 무중단 마이그레이션의 정의, 목적, 핵심 메커니즘을 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 정의·목적

- 정의: **스키마 변환**: AWS SCT를 활용한 DDL 자동 변환 및 오라클-PostgreSQL 데이터 타입 매핑
- 목적: 상용 DBMS의 비용·종속을 줄이면서 데이터와 서비스의 정합성을 유지해 오픈소스 DBMS로 옮긴다.

### 2. 핵심 관계

| 비교 항목 | 상용 DBMS (Oracle) | 오픈소스 (PostgreSQL) |
|:---|:---|:---|
| **라이선스 비용** | CPU 코어당 고액 영구비용 + 연간 유지보수비 | 완전 무료 커뮤니티 에디션 (TCO 획기적 절감) |
| **SQL 표준 준수** | 자체 오라클 방언 다수 포함 | 엄격한 ANSI SQL 표준 준수 |
| **확장성 (Extension)** | 제한적 상용 옵션 | PostGIS, pgvector 플러그인 무한 확장 |
| **아키텍처 결합도** | PL/SQL 중심 높은 결합도 | 백엔드(Spring) 중심 클라우드 친화적 결합도 |

### 핵심 관계

| 비교 항목 | 상용 DBMS (Oracle) | 오픈소스 (PostgreSQL) |
|:---|:---|:---|
| **라이선스 비용** | CPU 코어당 고액 영구비용 + 연간 유지보수비 | 완전 무료 커뮤니티 에디션 (TCO 획기적 절감) |
| **SQL 표준 준수** | 자체 오라클 방언 다수 포함 | 엄격한 ANSI SQL 표준 준수 |
| **확장성 (Extension)** | 제한적 상용 옵션 | PostGIS, pgvector 플러그인 무한 확장 |
| **아키텍처 결합도** | PL/SQL 중심 높은 결합도 | 백엔드(Spring) 중심 클라우드 친화적 결합도 |

- 제언: 호환성·성능·CDC 동기화를 사전 시험하고 단계별 컷오버와 검증된 롤백 경로를 준비한다.
---

## 2~4교시 예상문제 (25점)

> 최근 기업들의 고비용 상용 DBMS(Oracle 등) 종속성을 탈피하고 클라우드 환경으로 전환하기 위한 오픈소스 DBMS(PostgreSQL, MySQL 등) 전환 수요가 급증하고 있다. 오픈소스 DBMS 전환의 추진 배경과 기대효과를 제시하고, 무중단 마이그레이션 6단계 절차 및 기술적 난제(호환성, 성능, 롤백)에 대한 대응 방안을 설명하시오. (25점)

---

## 2~4교시 25점 답안

### Ⅰ. 오픈소스 DBMS 전환의 추진 배경 및 기대 효과

1. **추진 배경**: 고비용 상용 라이선스/유지보수비 부담(TCO 절감), 벤더 락인 탈피, 클라우드 네이티브 MSA 전환
2. **기대 효과**: TCO 70% 이상 절감, 특정 벤더 종속 배제, 컨테이너 기반 유연한 오토스케일링 인프라 확보

### Ⅱ. 오픈소스 DBMS 무중단 전환 6단계 프로세스

1. **절차**: 대상 진단 $\to$ 스키마 변환(SCT) $\to$ 초기 데이터 적재 $\to$ 실시간 CDC 복제 $\to$ 검증 $\to$ 컷오버
2. **핵심 메커니즘**:
   - **스키마 변환**: AWS SCT를 활용한 DDL 자동 변환 및 오라클-PostgreSQL 데이터 타입 매핑
   - **무중단 복제**: 트랜잭션 Redo Log를 파싱하는 CDC(Debezium)를 통해 실시간 동기화 상태 유지

### Ⅲ. 상용 DBMS vs 오픈소스 DBMS 핵심 비교

| 비교 항목 | 상용 DBMS (Oracle) | 오픈소스 (PostgreSQL) |
|:---|:---|:---|
| **라이선스 비용** | CPU 코어당 고액 영구비용 + 연간 유지보수비 | 완전 무료 커뮤니티 에디션 (TCO 획기적 절감) |
| **SQL 표준 준수** | 자체 오라클 방언 다수 포함 | 엄격한 ANSI SQL 표준 준수 |
| **확장성 (Extension)** | 제한적 상용 옵션 | PostGIS, pgvector 플러그인 무한 확장 |
| **아키텍처 결합도** | PL/SQL 중심 높은 결합도 | 백엔드(Spring) 중심 클라우드 친화적 결합도 |

### Ⅳ. 주요 기술적 난제 극복 및 비상 롤백 전략

1. **PL/SQL 호환성 극복**: 핵심 비즈니스 로직을 백엔드(Spring Boot)로 흡수하고 단기적으로 EDB Postgres 활용
2. **비상 롤백(Rollback) 대책**: 컷오버 즉시 오픈소스 $\to$ 구 상용 DB로 역방향 CDC를 가동하여 신규 시스템 장애 시 데이터 유실 없는 무손실 롤백(RPO=0) 보장
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제138회 2교시 1번 (상용 DBMS의 오픈소스 DBMS 전환 수요 및 전환 방안)
  - 컴퓨터시스템응용기술사 제127회 2교시 (이기종 데이터베이스 마이그레이션 전략 및 CDC)
  - 정보관리기술사 제119회 1교시 (데이터베이스 마이그레이션 시 데이터 정합성 검증 방안)
- **표준 및 검증 출처**:
  - AWS Prescriptive Guidance, "Database Migration Strategy: Migrating from Oracle to PostgreSQL"
  - Debezium Project Documentation, "Change Data Capture for Modern Data Platforms"
  - PostgreSQL Global Development Group Official Documentation (Migration Guide)
---

## 연결 토픽

- [051. 고가용성(HA) 아키텍처 (High Availability Architecture)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/051_ha_architecture.md)
- [047. 인덱스 (Index)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index.md)
- [091. 옵티마이저 (Optimizer)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/091_optimizer.md)
