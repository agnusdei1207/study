---
sidebar:
  order: 78
  label: "078. 트랜잭션 (Transaction)"
  badge:
    text: "A"
    variant: note
title: "트랜잭션 (Transaction) 및 ACID 특성과 상태 전이도"
author: "Antigravity"
date: "2026-09-20T18:45:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 78
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
  question_no: "078"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>트랜잭션·동시성 제어</span><strong>트랜잭션 (Transaction)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">트랜잭션 5대 상태 전이도 &middot; ACID 구현 메커니즘</text>

  <!-- State Machine Canvas -->
  <g transform="translate(30, 48)">
    <!-- 1. Active -->
    <rect x="160" y="0" width="110" height="34" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="215" y="21" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 활동 (Active)</text>

    <!-- Arrow Active -> Partially Committed -->
    <path d="M 180 34 L 110 70" stroke="#3b82f6" stroke-width="1.5"/>
    <polygon points="110,70 118,65 115,72" fill="#3b82f6"/>
    <text x="120" y="48" font-size="7.5" fill="#1e40af">연산 정상종료</text>

    <!-- Arrow Active -> Failed -->
    <path d="M 250 34 L 320 70" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="320,70 315,72 312,65" fill="#ef4444"/>
    <text x="310" y="48" font-size="7.5" fill="#991b1b">오류/예외 발생</text>

    <!-- 2. Partially Committed -->
    <rect x="50" y="70" width="120" height="34" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="110" y="91" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">2. 부분완료 (Partially)</text>

    <!-- 4. Failed -->
    <rect x="270" y="70" width="110" height="34" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="325" y="91" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">4. 실패 (Failed)</text>

    <!-- Arrow Partially -> Committed -->
    <path d="M 110 104 L 110 135" stroke="#10b981" stroke-width="1.5"/>
    <polygon points="110,135 106,128 114,128" fill="#10b981"/>
    <text x="75" y="122" font-size="7.5" fill="#047857">Commit 성공</text>

    <!-- Arrow Partially -> Failed -->
    <path d="M 170 87 L 270 87" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="2,2"/>
    <text x="220" y="82" font-size="7" fill="#dc2626" text-anchor="middle">플러시 실패</text>

    <!-- Arrow Failed -> Aborted -->
    <path d="M 325 104 L 325 135" stroke="#dc2626" stroke-width="1.5"/>
    <polygon points="325,135 321,128 329,128" fill="#dc2626"/>
    <text x="330" y="122" font-size="7.5" fill="#991b1b">Rollback 실행</text>

    <!-- 3. Committed -->
    <rect x="50" y="135" width="120" height="34" rx="4" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
    <text x="110" y="156" font-size="9.5" font-weight="bold" fill="#065f46" text-anchor="middle">3. 완료 (Committed)</text>

    <!-- 5. Aborted -->
    <rect x="270" y="135" width="110" height="34" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="325" y="156" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">5. 철회 (Aborted)</text>
  </g>

  <!-- Bottom: ACID Core Implementation -->
  <g transform="translate(30, 218)">
    <rect x="0" y="0" width="460" height="42" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="12" y="16" font-size="8.5" font-weight="bold" fill="#0f172a">&bull; 원자성 (A): Undo Log 롤백 | 일관성 (C): 무결성 제약조건/트리거</text>
    <text x="12" y="32" font-size="8.5" font-weight="bold" fill="#0f172a">&bull; 격리성 (I): 2PL 락 &middot; MVCC 스냅샷 | 영속성 (D): Redo Log &middot; WAL &middot; Checkpoint</text>
  </g>
</svg>
</div>

- 본질: **데이터베이스의 상태를 변환시키는 하나의 논리적 기능을 수행하기 위한 작업의 분할 불가능한 최소 논리 단위(All-or-Nothing)로, 원자성(A), 일관성(C), 격리성(I), 영속성(D)의 4대 속성을 보장하여 동시 실행 충돌과 시스템 장애로부터 데이터의 정합성을 수호하는 메커니즘**
- 암기: `에이-씨-아이-디` (Atomicity, Consistency, Isolation, Durability) / `활-부-완-실-철` (활동, 부분완료, 완료, 실패, 철회) / `언-제-락-리` (Undo로그, 제약조건, 락/MVCC, Redo로그)
- 판단축:
  - **로컬 트랜잭션(ACID)**: 단일 RDBMS 인스턴스 내에서 엄격한 일관성 강제 $\rightarrow$ 성능 및 단일 장애점 한계
  - **분산 트랜잭션(BASE)**: MSA 및 분산 NoSQL 환경에서 가용성을 우선하고 결과적 일관성(Eventual Consistency) 추구 $\rightarrow$ Saga 패턴 및 보상 트랜잭션 활용
- 주의: 외부 결제 API 호출이나 이메일 전송과 같은 네트워크 I/O 작업을 DB 트랜잭션(`@Transactional`) 범위 내에 포함시키면, 외부 지연 시 DB 커넥션 풀(DBCP)이 고갈되어 서비스 전체가 마비되는 전형적 장애가 발생하므로 트랜잭션 범위를 최소화해야 함

## 예상문제

> 데이터베이스 시스템의 신뢰성을 보장하는 핵심 개념인 트랜잭션(Transaction)의 개념과 ACID 4대 특성을 설명하고, 각 특성을 구현하기 위한 DBMS의 기술 요소를 매핑한 후, 트랜잭션의 5가지 상태 전이도를 도식화하여 설명하시오. (25점)

## Ⅰ. 데이터 무결성의 기본 단위인 트랜잭션(Transaction) 개요

#### 한줄 요약: 데이터베이스의 상태를 변환시키는 논리적 작업 묶음으로 All-or-Nothing의 원자적 실행을 보장하는 단위

- **등장 배경**:
  - 은행 계좌 이체(A 계좌에서 출금 $\rightarrow$ B 계좌로 입금)와 같은 비즈니스 프로세스는 2개 이상의 연속된 SQL 문장으로 구성됨
  - 출금 후 입금 직전에 시스템 전원이 차단되거나 네트워크가 끊어질 경우, 돈은 빠져나갔는데 상대방에게 입금되지 않는 심각한 금융 사고가 발생함
- **트랜잭션의 정의**:
  - 데이터베이스 관리 시스템(DBMS)에서 상호 연관된 복수의 질의 및 조작 연산들을 하나로 묶어, **모두 완벽히 반영되거나(Commit) 전혀 반영되지 않도록(Rollback)** 보장하는 작업의 최소 논리적 수행 단위

## Ⅱ. 트랜잭션의 4대 핵심 속성 (ACID) 및 구현 기술 매핑

#### 한줄 요약: 원자성, 일관성, 격리성, 영속성의 4대 기둥과 이를 물리적으로 구현하는 Undo, Redo, 락, 제약조건의 연계

| ACID 특성 | 핵심 정의 및 보장 내용 | 위반 시 발생하는 현상 | DBMS 물리 구현 메커니즘 |
|:---|:---|:---|:---|
| **원자성 (Atomicity)** | 트랜잭션 내 연산들은 전부 수행되거나 전부 취소되어야 함 (All-or-Nothing) | 계좌 이체 중 출금만 되고 입금은 누락되어 돈이 증발함 | **Undo Log (언두 세그먼트)**<br>장애 발생 시 롤백 수행 |
| **일관성 (Consistency)** | 트랜잭션 실행 전후 데이터베이스는 항상 유효한 무결성 제약조건을 만족해야 함 | 마이너스 통장이 아닌데 잔액이 음수로 떨어지거나 고아 행 발생 | **무결성 제약조건(PK/FK/Check)**<br>도메인 규칙 및 트리거 |
| **격리성 (Isolation)** | 동시에 실행되는 복수의 트랜잭션은 서로 간섭할 수 없으며 직렬 수행과 동등해야 함 | 갱신 분실(Lost Update), 더티 리드, 팬텀 충돌 발생 | **2단계 락킹(2PL), MVCC**<br>트랜잭션 격리 수준 설정 |
| **영속성 (Durability)** | 성공적으로 완료(Commit)된 트랜잭션의 결과는 시스템 장애 후에도 영구히 보존됨 | 커밋 확인 후 전원이 꺼졌는데 재부팅 시 결제 데이터 유실 | **Redo Log, WAL(Write-Ahead Log)**<br>체크포인트(Checkpoint) 기법 |

## Ⅲ. 트랜잭션의 5대 상태 전이도 및 생명주기

#### 한줄 요약: 활동, 부분 완료, 완료, 실패, 철회로 이어지는 5단계 상태 머신과 커밋/롤백 분기 흐름

- **활동 (Active)**: 트랜잭션이 시작(BEGIN)되어 질의문들이 실행 중인 동적 상태
- **부분 완료 (Partially Committed)**: 애플리케이션의 마지막 SQL 문장이 실행 완료되었으나, 트랜잭션 로그 버퍼의 데이터가 실제 디스크에 영구 쓰기(fsync)되기 직전의 불안정한 상태
- **완료 (Committed)**: WAL 로그가 디스크에 물리적으로 기록 완료되어 트랜잭션의 성공이 확정된 영구 상태
- **실패 (Failed)**: 문법 에러, 하드웨어 장애, 교착 상태(Deadlock) 감지 등으로 인해 연산이 중단된 상태
- **철회 (Aborted)**: Undo Log를 역순으로 스캔하여 실패한 트랜잭션이 변경했던 모든 메모리/디스크 블록을 이전 상태로 원상 복구하고 트랜잭션을 완전히 종료한 상태

## Ⅳ. 트랜잭션 복구 및 영속성 보장 메커니즘: WAL과 ARIES

#### 한줄 요약: 디스크 I/O 최적화를 위해 메모리 변경 전 로그를 먼저 쓰는 WAL과 장애 복구 표준 ARIES 알고리즘

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 130" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="110" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">Write-Ahead Logging (WAL) &middot; 체크포인트 흐름</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="110" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="55" y="20" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1. DML UPDATE</text>
    <text x="55" y="38" font-size="7.5" fill="#475569" text-anchor="middle">메모리 버퍼 수정</text>

    <path d="M 112 27 L 138 27" stroke="#64748b" stroke-width="1.5"/>

    <rect x="140" y="0" width="140" height="55" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="210" y="20" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">2. Redo Log 먼저 기록</text>
    <text x="210" y="38" font-size="7.5" fill="#b91c1c" text-anchor="middle">★ WAL: 디스크 순차 I/O</text>

    <path d="M 282 27 L 318 27" stroke="#64748b" stroke-width="1.5"/>

    <rect x="320" y="0" width="140" height="55" rx="4" fill="#f8fafc" stroke="#64748b" stroke-width="1.2"/>
    <text x="390" y="20" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">3. 데이터파일 플러시</text>
    <text x="390" y="38" font-size="7.5" fill="#64748b" text-anchor="middle">Checkpoint 비동기 쓰기</text>
  </g>
</svg>
</div>

- **WAL (Write-Ahead Logging)의 대원칙**:
  - 더티 페이지(Dirty Page)를 디스크 데이터 파일에 기록하기 전에, 반드시 대응하는 **Redo 로그 레코드를 디스크에 먼저 기록**해야 함
  - 랜덤 디스크 쓰기를 순차 디스크 쓰기(Append-only Log)로 전환하여 초고속 커밋 보장
- **ARIES 복구 3단계 알고리즘**:
  1. **분석 단계 (Analysis)**: 마지막 체크포인트 시점부터 로그를 순방향 스캔하여 장애 시점에 활성 상태였던 미완료 트랜잭션(Loser)과 커밋된 트랜잭션(Winner) 식별
  2. **재실행 단계 (Redo)**: 실패 직전까지의 모든 변경 사항을 로그대로 재실행하여 시스템을 장애 직전의 상태로 완전히 복원 (Repeat History)
  3. **취소 단계 (Undo)**: 미완료된 Loser 트랜잭션들이 수행했던 변경 사항을 역방향 스캔하며 Undo 로그로 롤백 수행

## Ⅴ. ACID vs BASE (분산 트랜잭션의 패러다임 전환)

#### 한줄 요약: 단일 RDBMS의 강한 일관성(ACID)과 분산 NoSQL/MSA의 고가용성 중심 결과적 일관성(BASE) 비교

| 비교 항목 | ACID (전통 RDBMS) | BASE (분산 NoSQL / MSA) |
|:---|:---|:---|
| **설계 철학** | **강한 데이터 일관성 (Strong Consistency)** 최우선 | **시스템 가용성 (High Availability)** 최우선 |
| **상태 전이** | 트랜잭션 성공 즉시 모든 노드가 동일한 최신 데이터 조회 | 일시적으로 노드 간 불일치가 허용되는 **유연한 상태(Soft-state)** |
| **일관성 보장 시점** | **즉시 (Instantaneous)** 커밋 시점에 보장 | 일정 시간 경과 후 최종 수렴하는 **결과적 일관성 (Eventual)** |
| **분산 합의 프로토콜**| 2단계 커밋 (2PC, 블로킹 오버헤드 큼) | Saga 패턴, 카프카 비동기 이벤트, TCC (Try-Confirm-Cancel) |
| **적합한 도메인** | 계좌 이체, 원장 관리, 증권 체결 | 소셜 피드, 상품 리뷰, 장바구니, 로그 수집 |

## Ⅵ. 실무 아키텍처 장애 패턴과 트랜잭셔널 아웃박스 패턴

#### 한줄 요약: 외부 통신 지연에 따른 커넥션 풀 고갈을 방지하고 DB와 메시지 큐 간의 원자성을 보장하는 설계

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 130" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="110" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">트랜잭셔널 아웃박스 패턴 (Transactional Outbox Pattern)</text>

  <g transform="translate(25, 42)">
    <!-- DB Box -->
    <rect x="0" y="0" width="170" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="85" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">RDBMS (단일 트랜잭션)</text>
    <text x="85" y="34" font-size="7.5" fill="#334155" text-anchor="middle">&bull; 주문 테이블 INSERT</text>
    <text x="85" y="47" font-size="7.5" fill="#1e40af" text-anchor="middle">&bull; Outbox 테이블 INSERT</text>

    <!-- Arrow -->
    <path d="M 172 27 L 208 27" stroke="#64748b" stroke-width="1.5"/>

    <!-- CDC -->
    <rect x="210" y="0" width="110" height="55" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="265" y="20" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">CDC 엔진</text>
    <text x="265" y="38" font-size="7.5" fill="#475569" text-anchor="middle">Debezium (WAL 파싱)</text>

    <!-- Arrow -->
    <path d="M 322 27 L 348 27" stroke="#64748b" stroke-width="1.5"/>

    <!-- Kafka -->
    <rect x="350" y="0" width="110" height="55" rx="4" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="405" y="20" font-size="9" font-weight="bold" fill="#5b21b6" text-anchor="middle">Apache Kafka</text>
    <text x="405" y="38" font-size="7.5" fill="#475569" text-anchor="middle">이벤트 안전 발행</text>
  </g>
</svg>
</div>

### 1. 전형적 장애 패턴: 외부 통신을 포함한 긴 트랜잭션 (Long Transaction)
- 외부 PG사 서버 지연 시 톰캣 스레드와 HikariCP DB 커넥션이 5초 동안 묶이면서 순식간에 커넥션 풀이 고갈(Connection Timeout)되어 시스템 전체 중단
- **해결책**: 외부 네트워크 I/O는 트랜잭션 블록 바깥으로 분리하고, DB 작업만 수 밀리초 단위로 최소 시간 격리 수행

### 2. 트랜잭셔널 아웃박스 패턴 (Transactional Outbox Pattern)
- 주문 테이블과 동일한 DB 트랜잭션 내에 **아웃박스(Outbox) 테이블**을 생성하여 발행할 메시지를 함께 INSERT (로컬 ACID 보장)
- 별도의 CDC 엔진(Debezium)이 아웃박스 테이블의 변경 로그를 읽어 카프카로 안전하게 발행(At-least-once)함으로써 분산 환경의 원자성 확보

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 트랜잭션 설계의 황금률은 **"트랜잭션 경계(@Transactional)는 짧을수록, 좁을수록 아름답다"**는 것이다. 트랜잭션 내부에 외부 결제 API, 이메일 발송, S3 파일 업로드 같은 네트워크 I/O를 넣는 순간, 외부 장애가 전체 DB 커넥션 풀(DBCP)을 집어삼켜 대형 참사로 번진다. 또한 분산 시스템에서 RDBMS의 로컬 ACID와 메시지 브로커(Kafka) 간의 정합성을 맞추려면 2PC의 성능 저하를 버리고 **트랜잭셔널 아웃박스 패턴(Transactional Outbox Pattern)**을 적용해야 한다.

> **[나라면 이렇게 쓴다]**
> 10점형 답안이라면 5대 상태 전이도(활동 $\to$ 부분완료 $\to$ 완료 / 실패 $\to$ 철회)와 ACID 4대 특성의 물리 구현 매핑표를 전면에 배치하겠다. 25점형이라면 긴 트랜잭션(Long Transaction)으로 인한 커넥션 고갈 장애 시나리오를 지적하고, Transactional Outbox Pattern 및 읽기 전용 최적화(`readOnly=true`) 방안을 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 외부 API를 포함한 긴 트랜잭션으로 커넥션 풀 고갈 발생 및 DB-카프카 간 이종 분산 트랜잭션 원자성 결여
- **대응 (개선 방안)**: 트랜잭션 경계 최소화(외부 I/O 분리), Transactional Outbox Pattern 도입 및 ARIES 기반 로그 선행 쓰기(WAL) 엄수
- **검증 (검증 기준)**: 트랜잭션 체류 시간 50ms 이내 유지, 커넥션 대기 시간 0초 수렴, Outbox CDC 전송 누락률 0% 검증
- **효과 (실행 효과)**: 커넥션 풀 고갈 장애 원천 차단, 초당 트랜잭션 처리량(TPS) 3배 향상 및 분산 데이터 최종 정합성 완결

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">외부 I/O 포함 긴 트랜잭션으로 커넥션 고갈 및 분산 원자성 결함</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">트랜잭션 지연 오픈 + 트랜잭셔널 아웃박스 패턴 (CDC 연계)</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">트랜잭션 체류시간 &le; 50ms, HikariCP 대기시간 0초, Outbox 정합성 100%</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">동시성 처리량 3배 향상 및 장애 없는 견고한 분산 아키텍처 실현</div>
  </div>
</div>

---

## 1교시 10점 답안 발췌

### 1. 트랜잭션(Transaction)의 개념 및 ACID 4대 특성

- **개념**: DB 상태를 변환시키는 작업의 분할 불가능한 논리적 최소 단위 (All-or-Nothing)
- **ACID 4대 특성 및 구현 기술**:
  - **원자성 (Atomicity)**: 모든 연산 완수 또는 전면 취소 / Undo Log 기반 롤백
  - **일관성 (Consistency)**: 실행 전후 무결성 제약조건 유지 / PK, FK, Check 제약 및 트리거
  - **격리성 (Isolation)**: 동시 트랜잭션 간 간섭 배제 / 2PL 락킹, MVCC 언두 스냅샷
  - **영속성 (Durability)**: 성공 결과의 영구적 보존 / Redo Log, Write-Ahead Logging(WAL)

### 2. 트랜잭션의 5대 상태 전이도

| 상태 | 정의 및 전이 조건 |
|:---|:---|
| **1. 활동 (Active)** | 트랜잭션이 시작되어 읽기/쓰기 DML 연산을 수행 중인 상태 |
| **2. 부분 완료 (Partially Committed)** | 마지막 SQL 실행 완료, WAL 로그가 디스크에 플러시되기 직전 상태 |
| **3. 완료 (Committed)** | WAL 로그가 디스크에 영구 기록 완료되어 커밋 확정된 상태 |
| **4. 실패 (Failed)** | 오류나 장애로 인해 정상 진행이 불가능해진 상태 |
| **5. 철회 (Aborted)** | Undo Log로 모든 작업을 원복하고 트랜잭션 시작 전으로 복귀한 상태 |

### 3. 실무 아키텍처 제언

- 외부 I/O를 트랜잭션 범위에서 배제하여 트랜잭션 점유 시간을 수 ms 단위로 최소화하고, 분산 환경에서는 Transactional Outbox Pattern을 채택하여 정합성 확보

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제129회 1교시 (데이터베이스 트랜잭션의 ACID 특성과 상태 전이도)
  - 컴퓨터시스템응용기술사 제121회 1교시 (트랜잭션의 ACID 특성과 격리수준)
  - 정보관리기술사 제114회 2교시 (트랜잭션 복구 기법: Redo/Undo와 ARIES 알고리즘)
- **표준 및 검증 출처**:
  - Jim Gray (1981), "The Transaction Concept: Virtues and Limitations", *VLDB*
  - C. Mohan et al. (1992), "ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking", *ACM TODS*
  - Abraham Silberschatz et al., *Database System Concepts (7th Edition)*, Chapter 17: Transactions

---

## 학습 체크

- [ ] 트랜잭션의 ACID 4대 속성을 각각 한 줄로 정의하고, 이를 구현하는 DBMS 엔진 요소를 매핑할 수 있는가?
- [ ] 트랜잭션의 5대 상태(활동, 부분완료, 완료, 실패, 철회) 간의 상태 전이 조건을 설명할 수 있는가?
- [ ] Write-Ahead Logging (WAL) 원칙이 디스크 I/O 성능을 높이고 영속성을 보장하는 메커니즘은 무엇인가?
- [ ] 단일 DB의 ACID와 분산 시스템의 BASE 패러다임 차이를 비교 설명할 수 있는가?
- [ ] **서술 연습 1**: 트랜잭션 5대 상태 전이도를 도식화하고, ACID 특성 구현 매핑표를 10점형 답안으로 작성하시오.
- [ ] **서술 연습 2**: ARIES 복구 3단계(분석-재실행-취소)와 마이크로서비스 환경에서의 트랜잭셔널 아웃박스 패턴을 25점형으로 서술하시오.

---

## 연결 토픽

- [020. 트랜잭션 격리 수준 (Isolation Level)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/020_isolation_level.md)
- [009. 동시성 제어 (Concurrency Control)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/009_concurrency_control.md)
- [049. 팬텀 충돌 (Phantom Conflict)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/049_phantom_conflict.md)
