---
title: "트랜잭션 격리 수준 (Isolation Level)"
category: "03-data"
tags:
  - "트랜잭션격리수준"
  - "IsolationLevel"
  - "ReadCommitted"
  - "RepeatableRead"
  - "Serializable"
  - "MVCC"
  - "WriteSkew"
date: "2026-09-20T23:09:00+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터베이스에서 트랜잭션 동시성 제어 및 격리 수준으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>트랜잭션·동시성</span>
  <strong>트랜잭션 격리 수준 (Isolation Level)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 동시에 실행되는 여러 트랜잭션 간에 변경 중인 데이터의 가시성(Visibility) 범위를 정의하여, 데이터 일관성과 시스템 동시성(처리량) 사이의 균형점을 제공하는 ANSI/ISO SQL 표준 규약
- 메커니즘: 트랜잭션 격리 수준 설정 $\rightarrow$ Lock 또는 MVCC(스냅샷) 가시성 적용 $\rightarrow$ 4대 이상현상(Dirty Read·Non-repeatable Read·Phantom Read·Write Skew) 차단 $\rightarrow$ 일관된 커밋
- 산출물: 격리 수준별 이상현상 방지 매트릭스 · MVCC 스냅샷 격리 모델 명세서 · 비관 잠금(FOR UPDATE) 설계서 · 교착상태 및 직렬화 실패 모니터링 로그

<div class="itpe-flow-map" role="img" aria-label="트랜잭션 격리 수준 및 가시성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 업무 도메인 정합성 요구 분석</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>단순 조회, 장바구니, 결제/원장, 좌석 예약 등 업무별 정합성-동시성 요구 수집</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: ANSI 4대 격리 수준 매핑</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Read Uncommitted</strong><span>Dirty Read 허용, 락 미사용 (최대 동시성)</span></div>
      <div class="itpe-flow-branch"><strong>Read Committed</strong><span>커밋된 튜플만 읽음, 오라클/PostgreSQL 기본값</span></div>
      <div class="itpe-flow-branch"><strong>Repeatable Read</strong><span>트랜잭션 내 동일 조회 보장, MySQL InnoDB 기본값</span></div>
      <div class="itpe-flow-branch"><strong>Serializable</strong><span>직렬 수행과 동등 보장, 팬텀 읽기 및 Write Skew 원천 차단</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: Lock 및 MVCC 스냅샷 가시성 적용</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>제어</strong><span>공유/배타 락 제어 또는 Undo 로그 스냅샷(Snapshot Isolation) 읽기</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 비즈니스 불변식 및 이상현상 방지 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>선택된 격리 수준이 금융 원장 불변식을 충족하며, Write Skew 등 직렬화 이상이 발생하지 않는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (격리 수준 채택)</strong>
      <span>트랜잭션 실행 승인 $\rightarrow$ 정합성 보장 및 고속 동시 처리(TPS) 달성</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (정합성 왜곡 / 직렬화 실패)</strong>
      <span>트랜잭션 롤백 $\rightarrow$ 격리 수준 상향(Serializable) 또는 `SELECT FOR UPDATE` 배타 락 적용</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Dirty Read`: 다른 트랜잭션이 수정 중이지만 아직 커밋되지 않은(Uncommitted) 변경 데이터를 읽어 발생하는 이상현상
- `Non-repeatable Read`: 동일 트랜잭션 내에서 같은 쿼리를 두 번 실행했을 때, 중간에 다른 트랜잭션이 값을 수정·커밋하여 조회 결과가 달라지는 현상
- `Phantom Read`: 동일 트랜잭션 내에서 범위 조회를 두 번 실행했을 때, 중간에 다른 트랜잭션이 신규 레코드를 삽입·커밋하여 없던 행이 나타나는 현상
- `Write Skew(쓰기 왜곡)`: 두 트랜잭션이 각각 서로 다른 행을 수정하지만 결합 제약조건(예: 두 의사 중 최소 1명은 당직 유지)을 동시에 위배하는 현상
- `Snapshot Isolation(스냅샷 격리)`: 트랜잭션 시작 시점의 일관된 DB 스냅샷을 읽도록 하여 읽기 작업이 락 없이 완벽한 Repeatable Read를 달성하는 MVCC 기법

</details>

## 예상문제

> 데이터베이스 트랜잭션의 ACID 속성 중 고립성(Isolation)을 보장하기 위한 ANSI/ISO SQL 표준의 4대 트랜잭션 격리 수준(Read Uncommitted, Read Committed, Repeatable Read, Serializable)을 비교하고, 각 수준에서 방지되는 이상현상(Dirty Read, Non-repeatable Read, Phantom Read, Write Skew)과 DBMS 제품별 구현 차이(Lock vs MVCC)를 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **ANSI 격리 수준 4단계** | Read Uncommitted, Read Committed, Repeatable Read, Serializable 비교 | Ⅲ 격리 수준 |
| **Write Skew와 SSI** | 스냅샷 격리의 맹점인 쓰기 왜곡과 직렬화 가능 스냅샷(Serializable Snapshot Isolation) | Ⅳ 이상현상 심층 |
| **DBMS별 기본 격리 수준** | Oracle/PostgreSQL(Read Committed), MySQL InnoDB(Repeatable Read) 구현 차이 | Ⅴ 제품별 비교 |

## Ⅰ. 동시성 제어의 가시성 계약, 트랜잭션 격리 수준의 개요

> 격리 수준은 완전한 고립성을 추구할 때 발생하는 성능 저하를 방지하기 위해, 허용 가능한 이상현상의 범위를 정의한 실무적 타협선임.

- 정의: 다중 사용자 환경에서 복수의 트랜잭션이 동시에 실행될 때, 특정 트랜잭션이 수행한 데이터 변경 사항이 다른 트랜잭션에 노출되는 고립(Isolation)의 강도를 규정한 수준
- 배경: ACID 원칙 중 격리성(Isolation)을 100% 만족시키는 직렬(Serializable) 모드는 동시성(Concurrency)과 시스템 처리량을 심각하게 훼손하므로 단계별 절충안 필요
- 목적: 비즈니스 도메인의 정합성 요구에 맞추어 성능(동시성)과 무결성(일관성) 사이의 최적 균형점 제공

## Ⅱ. 병행수행 시 발생하는 4대 주요 이상현상

> 격리 수준이 낮을수록 더 많은 데이터 오염 현상이 허용됨.

| 이상현상 | 발생 시나리오 및 메커니즘 | 방지 가능한 최소 격리 수준 |
|---|---|---|
| **오독 (Dirty Read)** | $T_1$이 튜플을 수정한 후 커밋하기 전에 $T_2$가 해당 값을 읽었으나, $T_1$이 롤백되어 무효한 데이터를 읽게 됨 | **Read Committed** |
| **반복불가 읽기 (Non-repeatable Read)** | $T_1$이 특정 튜플을 조회한 후, $T_2$가 해당 튜플을 수정·커밋함에 따라 $T_1$이 재조회 시 다른 값을 읽게 됨 | **Repeatable Read** |
| **유령 읽기 (Phantom Read)** | $T_1$이 범위 조건으로 다중 튜플을 조회한 후, $T_2$가 해당 조건에 부합하는 새 튜플을 삽입·커밋하여 재조회 시 없던 행이 출현 | **Serializable** (InnoDB는 Next-Key Lock으로 RR에서도 방지) |
| **쓰기 왜곡 (Write Skew)** | 스냅샷 격리에서 두 트랜잭션이 서로 다른 행을 수정하여 개별적으로는 성공하나, 전체 비즈니스 불변식이 깨지는 현상 | **Serializable (SSI)** |

## Ⅲ. ANSI/ISO SQL 표준 격리 수준 4단계 비교

> 표준 정의와 실제 DBMS 제품의 구현 메커니즘을 함께 이해해야 함.

<div style="max-width: 520px; margin: 1rem auto;">
<svg viewBox="0 0 520 100" width="100%" height="auto" style="display: block; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect x="0" y="0" width="520" height="100" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- RU -->
  <rect x="12" y="15" width="112" height="70" rx="5" fill="var(--color-bg-muted, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="68" y="35" font-size="10" font-weight="700" fill="var(--color-text-primary, #0f172a)" text-anchor="middle">Read Uncommitted</text>
  <text x="68" y="53" font-size="9" fill="var(--color-error, #b91c1c)" text-anchor="middle">Dirty Read 허용</text>
  <text x="68" y="70" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">동시성 최상 / 정합성 최하</text>
  <!-- Arrow -->
  <text x="130" y="55" font-size="12" fill="var(--color-border, #94a3b8)">→</text>
  <!-- RC -->
  <rect x="140" y="15" width="112" height="70" rx="5" fill="var(--color-info, #0284c7)" fill-opacity="0.1" stroke="var(--color-info, #0284c7)" stroke-width="1"/>
  <text x="196" y="35" font-size="10" font-weight="700" fill="var(--color-info, #0284c7)" text-anchor="middle">Read Committed</text>
  <text x="196" y="53" font-size="9" fill="var(--color-success, #15803d)" text-anchor="middle">Dirty Read 차단</text>
  <text x="196" y="70" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">Oracle·PG 기본값</text>
  <!-- Arrow -->
  <text x="258" y="55" font-size="12" fill="var(--color-border, #94a3b8)">→</text>
  <!-- RR -->
  <rect x="268" y="15" width="112" height="70" rx="5" fill="var(--color-primary, #2563eb)" fill-opacity="0.1" stroke="var(--color-primary, #2563eb)" stroke-width="1"/>
  <text x="324" y="35" font-size="10" font-weight="700" fill="var(--color-primary, #1d4ed8)" text-anchor="middle">Repeatable Read</text>
  <text x="324" y="53" font-size="9" fill="var(--color-success, #15803d)" text-anchor="middle">반복 읽기 보장</text>
  <text x="324" y="70" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">MySQL InnoDB 기본값</text>
  <!-- Arrow -->
  <text x="386" y="55" font-size="12" fill="var(--color-border, #94a3b8)">→</text>
  <!-- Serializable -->
  <rect x="396" y="15" width="112" height="70" rx="5" fill="var(--color-warning, #d97706)" fill-opacity="0.12" stroke="var(--color-warning, #d97706)" stroke-width="1"/>
  <text x="452" y="35" font-size="10" font-weight="700" fill="var(--color-warning, #b45309)" text-anchor="middle">Serializable</text>
  <text x="452" y="53" font-size="9" fill="var(--color-success, #15803d)" text-anchor="middle">Phantom·Skew 차단</text>
  <text x="452" y="70" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">정합성 최상 / 동시성 최하</text>
</svg>
</div>

| 격리 수준 (Isolation Level) | Dirty Read | Non-repeatable Read | Phantom Read | 주요 구현 메커니즘 | 대표 기본 적용 DBMS |
|---|:---:|:---:|:---:|---|---|
| **Read Uncommitted** | **발생** | **발생** | **발생** | 공유 락(S-Lock) 미사용, 배타 락 무시 읽기 | 실무 사용 거의 전무 |
| **Read Committed** | **방지** | **발생** | **발생** | 쿼리 실행 시점마다 새 MVCC 스냅샷(Read View) 생성 | Oracle, PostgreSQL, SQL Server |
| **Repeatable Read** | **방지** | **방지** | **발생** (표준 기준)| 트랜잭션 시작 시점의 단일 MVCC 스냅샷 유지 | MySQL (InnoDB 엔진) |
| **Serializable** | **방지** | **방지** | **방지** | 2PL 잠금(인덱스 넥스트-키 락) 또는 SSI 검증 | 고정밀 금융/원장 시스템 |

## Ⅳ. 스냅샷 격리의 한계: 쓰기 왜곡(Write Skew) 메커니즘

> MVCC 기반의 Repeatable Read는 유령 읽기는 막아도 쓰기 왜곡(Write Skew)을 완벽히 방어하지 못함.

<div style="max-width: 520px; margin: 1rem auto;">
<svg viewBox="0 0 520 140" width="100%" height="auto" style="display: block; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <rect x="0" y="0" width="520" height="140" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Top Banner: Invariant Rule -->
  <rect x="15" y="10" width="490" height="24" rx="4" fill="var(--color-primary, #2563eb)" fill-opacity="0.1" stroke="var(--color-primary, #2563eb)" stroke-width="1"/>
  <text x="260" y="26" font-size="10" font-weight="700" fill="var(--color-primary, #1d4ed8)" text-anchor="middle">비즈니스 불변식: 병원에 최소 1명의 의사는 반드시 당직(On-call)을 서야 함</text>
  <!-- Tx 1 -->
  <rect x="15" y="42" width="235" height="52" rx="4" fill="var(--color-info, #0284c7)" fill-opacity="0.08" stroke="var(--color-info, #0284c7)" stroke-width="1"/>
  <text x="132" y="58" font-size="10" font-weight="700" fill="var(--color-info, #0284c7)" text-anchor="middle">트랜잭션 1 (의사 A 당직 취소)</text>
  <text x="132" y="73" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">당직 수 2명 확인 $\to$ 의사 A 취소 커밋</text>
  <text x="132" y="86" font-size="9" fill="var(--color-info, #0284c7)" text-anchor="middle">(대상 행: 의사 A 레코드만 수정)</text>
  <!-- Tx 2 -->
  <rect x="270" y="42" width="235" height="52" rx="4" fill="var(--color-warning, #d97706)" fill-opacity="0.08" stroke="var(--color-warning, #d97706)" stroke-width="1"/>
  <text x="387" y="58" font-size="10" font-weight="700" fill="var(--color-warning, #b45309)" text-anchor="middle">트랜잭션 2 (의사 B 당직 취소, 동시)</text>
  <text x="387" y="73" font-size="9" fill="var(--color-text-secondary, #475569)" text-anchor="middle">당직 수 2명 확인 $\to$ 의사 B 취소 커밋</text>
  <text x="387" y="86" font-size="9" fill="var(--color-warning, #b45309)" text-anchor="middle">(대상 행: 의사 B 레코드만 수정)</text>
  <!-- Bottom: Failure Result -->
  <rect x="15" y="100" width="490" height="30" rx="4" fill="var(--color-error, #dc2626)" fill-opacity="0.1" stroke="var(--color-error, #dc2626)" stroke-width="1"/>
  <text x="260" y="120" font-size="11" font-weight="700" fill="var(--color-error, #b91c1c)" text-anchor="middle">결과: 서로 다른 행 수정으로 충돌 감지 실패 $\to$ 당직 0명 불변식 파괴 (Write Skew!)</text>
</svg>
</div>

- **해결 방안**:
  1. 비관적 명시 잠금: 조회 시 `SELECT ... FOR UPDATE`로 대상 레코드 전체에 배타 락 강제
  2. **직렬화 가능 스냅샷(SSI: Serializable Snapshot Isolation)**: 트랜잭션 간의 읽기-쓰기 의존성 그래프(Dependency Graph)를 추적하여 사이클 발생 시 한쪽을 자동 롤백

## Ⅴ. 주요 DBMS 제품별 격리 수준 구현 차이

> 동일한 'Repeatable Read'라 하더라도 오라클과 MySQL의 내부 구현과 동작이 다름.

| 비교 항목 | Oracle Database | PostgreSQL | MySQL (InnoDB) |
|---|---|---|---|
| **기본 격리 수준** | **Read Committed** | **Read Committed** | **Repeatable Read** |
| **지원 격리 수준** | Read Committed, Serializable | RC, RR, Serializable | RU, RC, RR, Serializable |
| **Repeatable Read 구현**| 미지원 (Serializable로 대체) | Snapshot Isolation 기반 (Write Skew 가능) | MVCC + **Next-Key Lock** (Phantom Read 자동 방지) |
| **Serializable 구현** | Snapshot Isolation (엄밀히 직렬성 아님)| **SSI (Serializable Snapshot Isolation)** | 2PL 기반 공유 락 강제 변환 |

## Ⅵ. 트랜잭션 격리 수준 실무 위험 관리

> 동시성 저하와 교착상태, 정합성 파손을 업무별로 차등 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| Serializable 적용 시 교착상태 및 직렬화 실패 폭증 | 트랜잭션 내 쿼리 실행 순서 표준화 및 지수 백오프(Exponential Backoff) 재시도 | 락 대기 최소화 및 일시적 충돌 트랜잭션 자동 복구 |
| Read Committed에서 갱신 손실(Lost Update) 발생 | 원자적 연산(`UPDATE account SET bal = bal - 100`) 또는 비관 락(`FOR UPDATE`) | 동시 수정 시 덮어쓰기 유실 원천 방지 |
| 긴 트랜잭션으로 인한 MVCC 언두(Undo) 공간 고갈 | 트랜잭션 타임아웃 설정 및 대량 배치를 작은 청크(Chunk) 단위 분할 | 테이블 팽창(Bloat) 방지 및 DB 락 다운 차단 |
| DBMS 제품별 격리 동작 차이로 인한 버그 | DB 마이그레이션 시 격리 수준별 회귀 테스트(Jepsen 검증) 수행 | 엔진 교체에 따른 정합성 붕괴 사고 예방 |

## Ⅶ. 기술사적 제언: 도메인 격리 수준 분리와 명시적 잠금 전략

> "모든 트랜잭션을 Serializable로 돌리는 것은 무책임한 성능 포기이며, 무조건 Read Committed를 고집하는 것은 잠재적 금융 사고의 방조다."

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 실제 실무에서 가장 위험한 것은 격리 수준의 이름만 믿고 제품의 내부 동작을 검증하지 않는 것이다. 예를 들어 MySQL InnoDB의 RR은 넥스트-키 락 덕분에 팬텀 리드가 방지되지만, PostgreSQL의 RR은 SSI가 아니면 쓰기 왜곡이 발생한다.
>
> **[나라면 이렇게 쓴다]**
> 기본 격리 수준은 성능이 우수한 Read Committed를 채택하되, 잔액 차감이나 좌석 예약처럼 동시 수정이 치명적인 도메인 서비스 메서드에는 `SELECT ... FOR UPDATE` 기반의 비관적 락을 선별 적용하는 '격리 수준 하이브리드' 전략을 수립하겠다.

### 실전 답안용 기술사적 제언

- 판정: 트랜잭션 격리 수준은 전사 단일 설정을 지양하고, **비즈니스 오류 비용(Error Cost)과 동시성 요구도(TPS)**에 따라 서비스 단위로 세분화하여 판정함
- 대안: 대다수 조회/일반 비즈니스는 **Read Committed**로 처리율 극대화 $\rightarrow$ 금융 잔액/결산 트랜잭션은 **명시적 배타 락(`FOR UPDATE`) 또는 Serializable** 강제
- 검증: 카오스 엔지니어링 동시성 부하 시험을 통한 갱신 손실 0건 및 데드락 발생률 0.01% 이하 확인
- 효과: 고성능 TPS를 달성하면서도 금융권 수준의 절대적 데이터 무결성 보장

<div class="itpe-flow-map" role="img" aria-label="트랜잭션 격리 수준 하이브리드 전략 및 무결성 확보 로드맵">
  <div class="itpe-flow-node">
    <strong>현행 한계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>위험 상존</strong><span>전사 일괄 RC 적용 시 갱신 손실·Write Skew 발생, 일괄 직렬화 시 락 병목</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>개선 방안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>하이브리드 분리</strong><span>일반 업무 RC(MVCC) 고속화 + 원장/예약 핵심 업무 선별적 `FOR UPDATE`·Serializable</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>검증 기준</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>품질 게이트</strong><span>갱신 손실 0건 달성 및 데드락 발생률 0.01% 이하 통과</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>실행 효과</strong></span>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass">
        <strong>목표 달성</strong>
        <span>원장 무결성 100% 사수 및 초당 트랜잭션 처리량(TPS) 극대화 동시 달성</span>
      </div>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

1. **트랜잭션 격리 수준(Isolation Level)의 정의 및 목적**
   - **정의**: 동시 실행되는 트랜잭션 간 데이터 변경 가시성 범위를 규정하여 정합성과 동시성을 절충하는 수준
   - **목적**: 4대 이상현상(Dirty Read, Non-repeatable Read, Phantom Read, Write Skew) 차단

2. **ANSI 4대 격리 수준 및 이상현상 방지 매트릭스**
   - **Read Uncommitted**: 락 미사용, 3대 이상현상 모두 발생 (최대 동시성)
   - **Read Committed**: 커밋된 데이터만 조회, Dirty Read 방지 (Oracle/PostgreSQL 기본)
   - **Repeatable Read**: 트랜잭션 내 일관된 스냅샷, Non-repeatable Read 방지 (MySQL InnoDB는 Next-Key Lock으로 Phantom도 차단)
   - **Serializable**: 직렬 수행 보장, Phantom Read 및 Write Skew 원천 차단 (최고 정합성)

3. **실무 제언: Write Skew 방지 및 하이브리드 전략**
   - **한계**: Repeatable Read에서도 서로 다른 행 수정 시 Write Skew가 발생할 수 있음
   - **대책**: 일반 업무는 Read Committed로 처리율을 높이고, 금융 원장 및 좌석 예약은 `SELECT ... FOR UPDATE` 비관 락 또는 Serializable을 선별 적용하는 하이브리드 아키텍처 필수 권고

## 출제 이력과 검증 출처

- **공식 출제 이력**: 정보관리기술사 제130회 1교시 단답형 (격리 수준과 이상현상), 제121회 2교시 논술형 (스냅샷 격리와 Write Skew, ANSI 격리 수준 비교)
- **표준 및 레퍼런스**: ANSI/ISO SQL-92 Isolation Levels, [PostgreSQL Documentation on Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [MySQL InnoDB Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html)

## 학습 체크

- [ ] [Ⅰ 개요]: 동시성과 일관성의 절충 관점에서 트랜잭션 격리 수준의 정의를 기술하였는가?
- [ ] [Ⅱ 이상]: Dirty Read, Non-repeatable Read, Phantom Read, Write Skew의 발생 원리를 구분하였는가?
- [ ] [Ⅲ 수준]: ANSI 4대 격리 수준(RU, RC, RR, Serializable)의 이상현상 방지 매트릭스를 제시하였는가?
- [ ] [Ⅳ 왜곡]: 스냅샷 격리 하에서 발생하는 Write Skew 메커니즘과 해결책을 설명하였는가?

## 연결 토픽

- [동시성 제어](./009_concurrency_control.md) · [팬텀 충돌](./049_phantom_conflict.md) · [트랜잭션(ACID)](./078_transaction.md) · [정규화](./019_normalization.md)
