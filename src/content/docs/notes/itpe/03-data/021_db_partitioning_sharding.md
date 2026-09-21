---
title: "데이터베이스 분할 (수평·수직 분할)"
category: "03-data"
tags:
  - "데이터베이스분할"
  - "수평분할"
  - "수직분할"
  - "Partitioning"
  - "Sharding"
  - "파티션프루닝"
  - "파티션인덱스"
date: "2026-09-20T23:10:00+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터베이스에서 물리적 데이터베이스 설계 및 분할로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>물리적 데이터베이스 설계·튜닝</span>
  <strong>데이터베이스 분할 (수평·수직 분할)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 단일 대용량 테이블을 논리적 의미는 온전히 유지한 채 물리적으로 여러 세그먼트·스토리지로 쪼개어, 쿼리 파티션 프루닝(Partition Pruning)을 통한 I/O 병목 해소와 데이터 수명주기(ILM) 관리 용이성을 확보하는 물리 모델링 기법
- 메커니즘: 워크로드 분석 $\rightarrow$ 파티션 키 선정 $\rightarrow$ 수평(Range·List·Hash·Composite) 및 수직(컬럼 분리) 분할 결정 $\rightarrow$ 로컬/글로벌 파티션 인덱스 설계 $\rightarrow$ 프루닝 및 무중단 DDL 검증
- 산출물: 물리 파티션 설계서 · 파티션 인덱스 전략서 · ILM 계층 스토리지 정책서 · 파티션 프루닝 실행계획 검증서

<div class="itpe-flow-map" role="img" aria-label="데이터베이스 분할 설계 및 무결성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 워크로드 분석 및 파티션 키 선정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>WHERE 절 빈번 조건, 데이터 수명주기 폐기 패턴, DML 핫스팟 식별</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 분할 방식(수평 vs 수직) 및 기법 결정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>수평 분할</strong><span>Range(시계열), List(코드), Hash(균등), Composite(복합)</span></div>
      <div class="itpe-flow-branch"><strong>수직 분할</strong><span>핫/콜드 컬럼 분리, LOB 대형 객체 독립 테이블 분리</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 파티션 인덱스(Local vs Global) 구성</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>인덱스</strong><span>무중단 DDL 보장을 위한 Local Partitioned Index 우선 채택</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 파티션 프루닝 및 DDL 영향도 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>WHERE 절에서 불필요한 파티션이 완전 배제(Pruning)되며, 파티션 DROP 시 Global Index가 보존되는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (물리 파티션 DDL 반영)</strong>
      <span>파티션 테이블스페이스 배포 $\rightarrow$ 계층형 스토리지(ILM) 자동 압축 및 아카이빙 연동</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (풀 스캔 발생 / 인덱스 파손)</strong>
      <span>파티션 재설계 $\rightarrow$ 가상 컬럼(Virtual Column) 적용 및 `UPDATE GLOBAL INDEXES` 옵션 보완</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Partition Pruning(파티션 프루닝)`: 옵티마이저가 SQL의 WHERE 조건절을 분석하여 쿼리 대상이 아닌 불필요한 파티션 세그먼트의 I/O를 원천 생략하는 최적화 기법
- `Local Partitioned Index`: 테이블 파티션과 인덱스 파티션이 1:1로 동일하게 분할되는 구조로, 특정 파티션 DROP 시 타 파티션 인덱스에 영향이 없음
- `Global Partitioned Index`: 테이블의 파티션 경계와 무관하게 인덱스 자체의 독립 키로 분할된 구조로, 전역 유일성 보장에 유리하나 파티션 DDL 시 Rebuild 필요
- `Vertical Partitioning(수직 분할)`: 단일 테이블의 열(Column)을 조회 빈도나 데이터 크기(LOB)에 따라 분리하여 단일 디스크 블록 당 유효 행 밀도를 극대화하는 기법
- `ILM(Information Lifecycle Management)`: 데이터의 생성-보관-폐기 주기별로 고성능 NVMe에서 저비용 압축 스토리지로 파티션을 자동 마이그레이션하는 수명주기 관리

</details>

## 예상문제

> 대용량 데이터베이스 환경에서 테이블 분할(Partitioning)의 개념과 필요성을 설명하고, 수평 분할과 수직 분할의 기준, 파티션 인덱스 유형 및 설계 시 고려사항을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **수평 vs 수직 분할** | 행(Row) 단위 분할(Range/List/Hash) vs 열(Column) 단위 핫/콜드 속성 분리 | Ⅱ 분할 메커니즘 |
| **파티션 인덱스 3대 유형** | Local Partitioned, Global Partitioned, Global Non-Partitioned Index DDL 내결함성 | Ⅲ 인덱스 구조 |
| **수평 분할 4대 방식** | Range(시계열), List(코드), Hash(균등), Composite(복합) 결정 절차 | Ⅳ 4대 방식 |
| **파티셔닝 vs 샤딩** | 단일 DBMS 세그먼트 분할(공유자원) vs 복수 인스턴스 분산(Shared-Nothing) | Ⅴ 샤딩 비교 |

## Ⅰ. 대용량 I/O 병목 해소와 고가용성을 위한 데이터베이스 분할 개요

- 정의: **데이터베이스 분할(Database Partitioning)**은 수천만~수억 건의 거대 테이블 또는 인덱스를 관리상·성능상 목적으로 작은 물리적 단위(세그먼트·파일스페이스)로 나누어 저장하되, 애플리케이션에는 단일 논리 테이블로 투명하게 제공하는 기법
- 목적: 쿼리 시 불필요한 파티션 접근을 차단하는 **파티션 프루닝(Partition Pruning)**을 통한 조회 성능 개선 및 백업·복구·삭제 등 관리 작업의 단위 격리
- 필요성: 단일 테이블 크기가 수백 GB~수 TB에 달하면 B*Tree 인덱스 깊이 증가로 탐색 비용이 급증하고, 일괄 삭제(DELETE) 시 트랜잭션 로그 포화 및 락 경합 발생

## Ⅱ. 수평 분할과 수직 분할의 메커니즘 및 특징

| 구분 | 수평 분할 (Horizontal Partitioning) | 수직 분할 (Vertical Partitioning) |
|---|---|---|
| **분할 기준** | 행(Row, Tuple) 단위 분할 | 열(Column, Attribute) 단위 분할 |
| **분할 키** | 날짜, 코드, 일련번호 등 파티션 키 칼럼 | 기본키(PK)를 공유하며 속성 그룹 분리 |
| **핵심 기법** | Range, List, Hash, Composite(Range+Hash 등) | 핫/콜드 컬럼 분리, LOB(CLOB/BLOB) 독립 테이블화 |
| **성능 효과** | 범위 조회 시 특정 파티션만 스캔(Pruning) | 풀 스캔 시 블록당 행 수 증가, I/O 대폭 절감 |
| **주요 적용** | 시계열 로그, 결제/주문 이력, 정산 데이터 | 회원 테이블(기본정보 vs 프로필 사진/상세소개) |
| **트레이드오프** | 파티션 키가 조건절에 없을 시 전체 파티션 브로드캐스트 | 두 분할 속성을 동시 조회 시 JOIN 부하 발생 |

## Ⅲ. 파티션 인덱스(Partitioned Index)의 정적 구조 및 유형

> 테이블 세그먼트와 인덱스 세그먼트 간의 매핑 구조에 따라 가용성과 정비 비용이 결정됨.

<div style="max-width: 520px; margin: 1rem auto;">
<svg viewBox="0 0 520 120" width="100%" height="auto" style="display: block; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect x="0" y="0" width="520" height="120" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Local Partitioned Index -->
  <rect x="15" y="15" width="155" height="90" rx="5" fill="var(--color-primary, #2563eb)" fill-opacity="0.1" stroke="var(--color-primary, #2563eb)" stroke-width="1"/>
  <text x="92" y="34" font-size="11" font-weight="700" fill="var(--color-primary, #1d4ed8)" text-anchor="middle">Local Partitioned</text>
  <text x="92" y="52" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">테이블:인덱스 = 1:1 동등매핑</text>
  <rect x="25" y="62" width="60" height="18" rx="3" fill="var(--color-bg-muted, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="55" y="75" font-size="8" fill="var(--color-text-primary, #0f172a)" text-anchor="middle">Idx P1 ↔ Tbl P1</text>
  <rect x="95" y="62" width="60" height="18" rx="3" fill="var(--color-bg-muted, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="125" y="75" font-size="8" fill="var(--color-text-primary, #0f172a)" text-anchor="middle">Idx P2 ↔ Tbl P2</text>
  <text x="92" y="96" font-size="9" font-weight="700" fill="var(--color-success, #15803d)" text-anchor="middle">파티션 DROP 시 무영향</text>
  <!-- Global Partitioned Index -->
  <rect x="182" y="15" width="155" height="90" rx="5" fill="var(--color-warning, #d97706)" fill-opacity="0.1" stroke="var(--color-warning, #d97706)" stroke-width="1"/>
  <text x="260" y="34" font-size="11" font-weight="700" fill="var(--color-warning, #b45309)" text-anchor="middle">Global Partitioned</text>
  <text x="260" y="52" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">인덱스 자체 독립 키 분할</text>
  <rect x="195" y="62" width="130" height="18" rx="3" fill="var(--color-bg-muted, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="260" y="75" font-size="8" fill="var(--color-text-primary, #0f172a)" text-anchor="middle">Idx P1 (Tbl P1+P2 혼합)</text>
  <text x="260" y="96" font-size="9" font-weight="700" fill="var(--color-error, #b91c1c)" text-anchor="middle">테이블 DDL 시 Rebuild 필요</text>
  <!-- Global Non-Partitioned Index -->
  <rect x="350" y="15" width="155" height="90" rx="5" fill="var(--color-bg-muted, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="427" y="34" font-size="11" font-weight="700" fill="var(--color-text-primary, #0f172a)" text-anchor="middle">Global Non-Partitioned</text>
  <text x="427" y="52" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">전체 테이블 단일 B*Tree</text>
  <rect x="365" y="62" width="125" height="18" rx="3" fill="var(--color-bg-subtle, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="427" y="75" font-size="8" fill="var(--color-text-primary, #0f172a)" text-anchor="middle">단일 전역 인덱스 트리</text>
  <text x="427" y="96" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">단건 최고속 / 정비비용 극대</text>
</svg>
</div>

| 인덱스 유형 | 구조적 특성 | 장점 | 단점 및 관리 비용 |
|---|---|---|---|
| **Local Partitioned Index** | 테이블 파티션과 인덱스 파티션이 1:1 동등 매핑(Equi-partitioned) | 특정 파티션 DROP/TRUNCATE 시에도 타 파티션 인덱스 무영향 | 파티션 키 미포함 쿼리 시 모든 로컬 인덱스 탐색 필요 |
| **Global Partitioned Index** | 테이블 파티션 구조와 무관하게 인덱스 자체의 독립 키로 분할 | 업무 고유 식별자(PK 등)의 전역 유일성 보장에 유리 | 특정 파티션 DDL 작업 시 전체 글로벌 인덱스가 Unusable 상태로 전이 |
| **Global Non-Partitioned** | 파티션된 테이블 전체를 단일 B*Tree 인덱스로 관리 | 전역 단건 조회 성능 최고 | 파티션 관리 작업 시 인덱스 재생성(Rebuild) 비용 극대화 |

## Ⅳ. 수평 분할의 4대 방식과 분할 결정 절차

<div style="max-width: 520px; margin: 1rem auto;">
<svg viewBox="0 0 520 60" width="100%" height="auto" style="display: block; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect x="0" y="0" width="520" height="60" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Step 1 -->
  <rect x="10" y="10" width="90" height="40" rx="4" fill="var(--color-bg-muted, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="55" y="27" font-size="9" font-weight="700" fill="var(--color-text-primary, #0f172a)" text-anchor="middle">1. 워크로드 분석</text>
  <text x="55" y="41" font-size="8" fill="var(--color-text-secondary, #475569)" text-anchor="middle">WHERE절 패턴</text>
  <text x="104" y="34" font-size="11" fill="var(--color-border, #94a3b8)">→</text>
  <!-- Step 2 -->
  <rect x="114" y="10" width="90" height="40" rx="4" fill="var(--color-info, #0284c7)" fill-opacity="0.1" stroke="var(--color-info, #0284c7)" stroke-width="1"/>
  <text x="159" y="27" font-size="9" font-weight="700" fill="var(--color-info, #0284c7)" text-anchor="middle">2. 파티션 키 선정</text>
  <text x="159" y="41" font-size="8" fill="var(--color-text-secondary, #475569)" text-anchor="middle">변동성 낮은 컬럼</text>
  <text x="208" y="34" font-size="11" fill="var(--color-border, #94a3b8)">→</text>
  <!-- Step 3 -->
  <rect x="218" y="10" width="90" height="40" rx="4" fill="var(--color-warning, #d97706)" fill-opacity="0.1" stroke="var(--color-warning, #d97706)" stroke-width="1"/>
  <text x="263" y="27" font-size="9" font-weight="700" fill="var(--color-warning, #b45309)" text-anchor="middle">3. 분할 방식 결정</text>
  <text x="263" y="41" font-size="8" fill="var(--color-text-secondary, #475569)" text-anchor="middle">Range·List·Hash</text>
  <text x="312" y="34" font-size="11" fill="var(--color-border, #94a3b8)">→</text>
  <!-- Step 4 -->
  <rect x="322" y="10" width="90" height="40" rx="4" fill="var(--color-primary, #2563eb)" fill-opacity="0.1" stroke="var(--color-primary, #2563eb)" stroke-width="1"/>
  <text x="367" y="27" font-size="9" font-weight="700" fill="var(--color-primary, #1d4ed8)" text-anchor="middle">4. 스토리지 매핑</text>
  <text x="367" y="41" font-size="8" fill="var(--color-text-secondary, #475569)" text-anchor="middle">I/O 밸런싱 설계</text>
  <text x="416" y="34" font-size="11" fill="var(--color-border, #94a3b8)">→</text>
  <!-- Step 5 -->
  <rect x="426" y="10" width="85" height="40" rx="4" fill="var(--color-success, #16a34a)" fill-opacity="0.1" stroke="var(--color-success, #16a34a)" stroke-width="1"/>
  <text x="468" y="27" font-size="9" font-weight="700" fill="var(--color-success, #15803d)" text-anchor="middle">5. 프루닝 검증</text>
  <text x="468" y="41" font-size="8" fill="var(--color-text-secondary, #475569)" text-anchor="middle">실행계획 확인</text>
</svg>
</div>

| 방식 | 분할 논리 | 적합 업무 | 주의점 |
|---|---|---|---|
| **Range (범위)** | 연속적인 숫자나 날짜 구간 기준 분할 | 일자별 정산, 월별 주문, 연도별 로그 | 최신 파티션에만 쓰기가 몰리는 핫스팟 주의 |
| **List (목록)** | 불연속적인 이산 값(코드, 지역, 사업부) 기준 | 시도별 지사 데이터, 결제수단 코드 | 새 코드 발생 시 파티션 누락 방지 Default 지정 |
| **Hash (해시)** | 해시 함수 결과값에 따라 균등 분할 | 뚜렷한 기준 컬럼이 없고 균등 분산이 필요할 때 | 범위 검색 불가능, 파티션 개수는 2의 거듭제곱($2^n$) 권장 |
| **Composite (복합)** | 주 파티션(Range) + 서브 파티션(Hash/List) | 대용량 주문(월별 Range + 고객ID Hash) | 관리 대상 세그먼트 수가 기하급수적으로 증가 |

## Ⅴ. 단일 DB 파티셔닝과 분산 샤딩(Sharding) 비교

| 비교 항목 | 데이터베이스 파티셔닝 (Partitioning) | 애플리케이션 샤딩 (Sharding) |
|---|---|---|
| **아키텍처 위치** | 단일 DBMS 엔진 내부 세그먼트 분할 | 복수 DBMS 인스턴스 간 물리적 분산 |
| **자원 공유** | CPU, 메모리(Buffer Cache), 트랜잭션 엔진 공유 | 완전한 비공유(Shared-Nothing) 구조 |
| **투명성** | DBMS 엔진이 SQL 파싱 단계에서 프루닝 자동 수행 | 애플리케이션 또는 샤드 미들웨어가 라우팅 담당 |
| **트랜잭션** | 단일 인스턴스 ACID 완전 보장 | 샤드 간 트랜잭션 시 분산 2PC 오버헤드 발생 |
| **JOIN 연산** | 파티션 간 자유로운 SQL JOIN 가능 | 샤드 간 크로스 조인 불가(애플리케이션 병합 필요) |
| **도입 기준** | 수직 확장(Scale-Up) 한계 이전 디스크 I/O 분산 | 단일 서버의 CPU/메모리/커넥션 한계 도달 시 |

## Ⅵ. 테이블 분할 실무 적용 시 주요 장애 요인 및 대책

| 문제 상황 | 근본 원인 | 실무 대책 | 기대 효과 |
|---|---|---|---|
| **파티션 프루닝 실패** (전체 풀 스캔) | WHERE 절 파티션 키 컬럼 가공(`TO_CHAR(date)=...`) 또는 타입 불일치 | 컬럼 가공 금지, 바인드 변수 타입 일치, 가상 컬럼(Virtual Column) 기반 파티셔닝 | 대상 파티션 블록만 직접 스캔 |
| **특정 파티션 디스크 I/O 병목** (Hotspot) | 날짜 기반 Range 분할로 현재 날짜 파티션에 쓰기 집중 | Range-Hash 복합 파티셔닝 적용, SSD 등 고성능 티어 스토리지에 최신 파티션 배치 | 디스크 컨트롤러 큐 병목 해소 |
| **대량 데이터 이관/삭제 지연** | `DELETE FROM table WHERE date < ...` 수행으로 Undo/Redo 폭증 | `ALTER TABLE DROP/TRUNCATE PARTITION` DDL 작업으로 메타데이터만 즉시 정리 | 락 경합 없이 수초 내 데이터 정리 |
| **인덱스 파손 (Index Unusable)** | 파티션 DROP/EXCHANGE 시 Global Index 동기화 누락 | DDL 문장에 `UPDATE GLOBAL INDEXES` 절 명시 또는 Local Index 원칙 준수 | 쿼리 중단 없는 무중단 데이터 파티션 순환 |
| **파티션 키 값 변경에 따른 에러** | UPDATE 문으로 파티션 키 값이 변경되어 타 파티션 이동 필요 | `ENABLE ROW MOVEMENT` 절 활성화 (이동 빈번 시 성능 저하 감시) | 파티션 간 행 자동 재배치 |

## Ⅶ. 기술사적 제언: 성능과 운영 복잡성의 균형을 위한 기술사적 제언

> "파티셔닝은 단순한 물리 분할이 아니라, 핫/콜드 데이터 수명주기(ILM)와 인덱스 무결성을 단일 관리 체계로 묶는 물리 데이터 아키텍처다."

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 파티셔닝은 무한한 만병통치약이 아니다. 수백 개 이상의 과도한 파티션 분할은 딕셔너리 캐시 고갈과 SQL 파싱 시 실행계획 생성 지연을 유발한다.
>
> **[나라면 이렇게 쓴다]**
> 테이블 크기 1,000만 건 이상, 월별 증가량 100만 건 이상인 테이블에 한해 파티셔닝을 제한 적용하겠다. 최신 3개월 데이터는 NVMe 기반 고성능 스토리지의 Local Index 파티션으로 유지하고, 1년 이상 경과 데이터는 압축(Compression) 후 대용량 저비용 스토리지로 마이그레이션하는 계층화 ILM 정책을 수립하겠다.

### 실전 답안용 기술사적 제언

- 판정: 단일 테이블 크기 1,000만 건 이상 및 파티션 프루닝 적용 가능성이 입증되었을 때만 물리 파티셔닝을 승인함
- 대안: 수평(Range-Hash) 복합 파티셔닝 $\rightarrow$ 무중단 관리를 위한 `Local Partitioned Index` 강제 $\rightarrow$ 계층형 스토리지(ILM) 연계
- 검증: 실행계획 상 Partition Pruning 성공률 100% 및 파티션 DROP 시 Global Index Unusable 0건 달성
- 효과: 풀 테이블 스캔 대비 디스크 I/O 90% 이상 절감 및 야간 데이터 정리 배치 시간 수 시간 $\to$ 수 초 단축

<div class="itpe-flow-map" role="img" aria-label="데이터베이스 분할 성능 최적화 및 ILM 연계 로드맵">
  <div class="itpe-flow-node">
    <strong>현행 한계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>I/O 병목</strong><span>대용량 단일 테이블 I/O 경합, 인덱스 비대화, DELETE 시 락/Undo 폭증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>개선 방안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>물리 분할</strong><span>수평/수직 분할, Local Partitioned Index 채택, 계층형 ILM 스토리지 연동</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>검증 기준</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>품질 게이트</strong><span>파티션 프루닝 100% 적중 및 DDL 시 Index Unusable 방지 검증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>실행 효과</strong></span>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass">
        <strong>목표 달성</strong>
        <span>스캔 I/O 90% 감축, 무중단 파티션 순환 및 스토리지 TCO 대폭 절감</span>
      </div>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

1. **데이터베이스 분할의 정의 및 목적**
   - **정의**: 대용량 단일 테이블을 논리 구조 변경 없이 물리 세그먼트 단위로 분할하는 기법
   - **목적**: 파티션 프루닝(Pruning)을 통한 I/O 절감, 인덱스 깊이 축소, 단위 데이터 수명주기(ILM) 관리

2. **수평 분할 vs 수직 분할 핵심 비교**
   - **수평 분할 (Horizontal)**: 행(Row) 단위 분할 (Range, List, Hash, Composite) $\rightarrow$ 범위 스캔 블록 최소화
   - **수직 분할 (Vertical)**: 열(Column) 단위 분할 (핫/콜드 컬럼, LOB 분리) $\rightarrow$ 블록 당 유효 튜플 밀도 증가

3. **파티션 인덱스 및 실무 제언**
   - **Local Partitioned Index**: 테이블과 1:1 동등 분할 $\rightarrow$ 특정 파티션 DROP 시 타 파티션 무영향(권장)
   - **실무 관리**: 파티션 키 컬럼 가공 금지로 프루닝 실패를 방지하고, DDL 시 `UPDATE GLOBAL INDEXES` 명시 필수

## 출제 이력과 검증 출처

- 제138회 공식 문제지: 데이터베이스 분할(수평분할, 수직분할) 개념 및 적용
- 제127회 공식 문제지: 데이터베이스 샤딩 및 분할 기법
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html)
- [PostgreSQL Documentation, Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)

## 학습 체크

- [ ] 수평 분할의 4대 방식(Range, List, Hash, Composite)의 선택 기준을 제시할 수 있는가
- [ ] 수직 분할에서 LOB 및 빈번 접근 컬럼 분리 효과를 설명할 수 있는가
- [ ] Local Partitioned Index와 Global Partitioned Index의 DDL 내결함성 차이를 비교할 수 있는가
- [ ] 파티션 프루닝이 무효화되는 안티패턴과 방지 대책을 작성할 수 있는가
- [ ] Ⅶ 결론에서 ILM(계층화 수명주기 관리)과 연계한 아키텍처 전략을 제시할 수 있는가

## 연결 토픽

- [샤딩](./045_sharding/) · [인덱스(클러스터드·논클러스터드)](./047_index/) · [데이터 모델링](./042_data_modeling/) · [데이터베이스 튜닝](./088_database_tuning/)
