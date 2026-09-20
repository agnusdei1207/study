---
title: "동시성 제어(병행제어)"
author: "Codex"
date: "2026-09-20T19:41:27+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터베이스에서 트랜잭션 관리 및 동시성 제어로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>트랜잭션·동시성</span>
  <strong>동시성 제어(병행제어)</strong>
</div>

<details>
<summary>핵심 용어</summary>

- `Serializability`: 병행 스케줄 결과가 어떤 직렬 스케줄과 동등하다는 정확성 기준
- `2PL(Two-Phase Locking)`: 락 획득과 해제를 확장·축소 단계로 분리하는 제어
- `OCC(Optimistic Concurrency Control)`: 읽기 후 커밋 전 충돌을 검증하는 낙관적 제어
- `MVCC(Multi-Version Concurrency Control)`: 시점별 버전을 제공해 읽기와 쓰기 경합을 줄이는 제어
- `Recoverability`: 선행 트랜잭션 결과 확정 순서를 지켜 안전하게 복구 가능한 성질

</details>

## 큰 그림과 30초 인출

- 본질: 다중 트랜잭션이 데이터베이스를 동시에 공유·접근할 때 상호 간섭으로 인한 데이터 불일치 이상현상을 방지하고, 직렬가능성(Serializability)과 회복가능성(Recoverability)을 보장하는 트랜잭션 통제 메커니즘
- 4대 기법: 로킹(2PL), 타임스탬프 순서화(Timestamp Ordering), 낙관적 검증(OCC), 다중버전 제어(MVCC)
- 4대 이상현상: 갱신 손실(Lost Update), 오독(Dirty Read), 반복불가 읽기(Non-repeatable Read), 유령 읽기(Phantom Read)

<div class="itpe-flow-map" role="img" aria-label="다중 트랜잭션 충돌과 4대 동시성 제어 기법 분기">
  <div class="itpe-flow-node"><strong>동시 트랜잭션 요청 ($T_1, T_2, \dots$)</strong><div class="itpe-step-detail"><span>처리</span><span>Read · Write 연산 인터리빙</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>동시성 제어 4대 알고리즘 분기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>2PL (로킹)</strong><span>확장기(Lock 획득) $\to$ 축소기(Lock 반납) · Strict 2PL</span></div>
      <div class="itpe-flow-branch"><strong>Timestamp</strong><span>트랜잭션 시작 시간순 실행 · Thomas Write Rule</span></div>
      <div class="itpe-flow-branch"><strong>OCC (낙관적)</strong><span>Read $\to$ Validation $\to$ Write 3단계 검증</span></div>
      <div class="itpe-flow-branch"><strong>MVCC (다중버전)</strong><span>스냅샷 격리 · 읽기는 쓰기를 막지 않음 (Undo Log)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>직렬가능성(Serializability) 보장</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>충돌 직렬성</strong><span>선행 그래프(Precedence Graph) 비순환(Acyclic)</span></div>
      <div class="itpe-flow-branch"><strong>회복가능성</strong><span>연쇄 롤백(Cascading Rollback) 방지</span></div>
    </div>
  </div>
</div>

## 예상문제

> 데이터베이스에서 다중 트랜잭션 동시 실행 시 발생 가능한 4대 이상현상(Lost Update, Dirty Read 등)을 제시하고, 이를 방지하기 위한 직렬성(Serializability) 이론 및 4대 동시성 제어 기법(2PL, Timestamp, OCC, MVCC)의 동작 원리와 장단점을 비교 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **병행제어(Concurrency Control)** | 데이터베이스 무결성과 격리성을 지키며 시스템 처리량을 극대화하는 트랜잭션 스케줄링 | Ⅰ 개요, Ⅲ 기법 |
| **Strict 2PL (엄격한 2단계 로킹)** | 트랜잭션이 완료(Commit/Abort)될 때까지 모든 배타 락(X-Lock)을 유지하여 연쇄 롤백을 차단하는 기법 | Ⅲ 기법 세부 |

## Ⅰ. 트랜잭션 고립성과 처리량의 균형추, 동시성 제어의 개요

> 동시성 제어는 다중 트랜잭션의 병행 수행 결과를 직렬 수행 결과와 동일하게 보장하는 기술임.

- 정의: 다중 사용자 환경에서 동시에 실행되는 복수 트랜잭션의 인터리빙(Interleaving) 연산을 스케줄링하여, 트랜잭션의 격리성(Isolation)과 일관성(Consistency)을 유지하고 데이터 손상을 방지하는 DBMS 핵심 엔진 기술
- 필요성: 단순 직렬(Serial) 처리는 데이터 정합성은 완벽하나 CPU 및 디스크 I/O 유휴로 시스템 처리량(Throughput)이 급감하며, 무제어 병행 처리는 갱신 손실 등 치명적 불일치 유발
- 목표: 직렬 실행과 동일한 결과를 보장하는 직렬가능성(Serializability) 달성 및 트랜잭션 장애 시 연쇄 복구를 방지하는 회복가능성(Recoverability) 확보

## Ⅱ. 병행 제어 결여 시 발생하는 4대 이상현상

> 미제어 동시 실행은 갱신 손실, 오독, 불일치 분석, 유령 레코드 생성을 야기함.

| 이상현상 | 발생 메커니즘 | 구체적 장애 사례 |
|---|---|---|
| **갱신 손실 (Lost Update)** | 트랜잭션 $T_1$의 갱신 결과를 트랜잭션 $T_2$가 덮어써서 $T_1$의 변경이 무효화됨 | 잔액 100만원 계좌에 A가 10만원 입금 중, B가 20만원 출금하여 A의 입금 기록이 유실됨 |
| **오독 / 더티 리드 (Dirty Read)** | $T_1$이 수정한 미커밋(Uncommitted) 데이터를 $T_2$가 읽은 후, $T_1$이 롤백됨 | 미확정 주문 내역을 읽어 배송 처리했으나 결제 실패로 주문이 취소되어 손실 발생 |
| **반복불가 읽기 (Non-repeatable Read)** | $T_1$이 동일 데이터를 두 번 읽는 사이에 $T_2$가 해당 데이터를 수정·커밋하여 값이 바뀜 | 동일 트랜잭션 내에서 고객 등급을 조회할 때마다 VIP와 일반으로 다르게 조회됨 |
| **유령 읽기 (Phantom Read)** | $T_1$이 범위 조건을 만족하는 행 집합을 재조회하는 사이에 $T_2$가 신규 행을 삽입(Insert)함 | $T_1$이 특정 부서 인원수를 집계(10명)한 후 보너스를 지급하려 재조회 시 11명으로 증가 |

## Ⅲ. 동시성 제어 4대 기법 동작 원리 및 메커니즘

> 락(2PL), 시간(타임스탬프), 검증(OCC), 버전(MVCC)의 서로 다른 메커니즘으로 충돌을 통제함.

<div class="itpe-pipeline" role="img" aria-label="동시성 제어 4대 기법">
  <div class="itpe-pipeline-node"><strong>2PL</strong><div class="itpe-step-detail"><span>방식</span><span>Locking 기반</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Timestamp</strong><div class="itpe-step-detail"><span>방식</span><span>시간순서화</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>OCC</strong><div class="itpe-step-detail"><span>방식</span><span>낙관적 검증</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>MVCC</strong><div class="itpe-step-detail"><span>방식</span><span>다중버전 스냅샷</span></div></div>
</div>

| 기법 | 핵심 동작 원리 및 규칙 | 교착상태(Deadlock) 여부 | 주요 장점 및 한계 |
|---|---|---|---|
| **2PL (2단계 로킹)** | **확장 단계(Growing)**: 락 획득만 가능<br>**축소 단계(Shrinking)**: 락 해제만 가능 | **발생 가능**<br>(교착 탐지 및 예방 필요) | 직렬가능성 완벽 보장하나, 락 경합으로 인한 대기 및 교착상태 처리 오버헤드 존재 |
| **타임스탬프 순서화 (Timestamp)** | 트랜잭션 시작 시 부여된 $TS(T)$ 순서로 데이터 읽기($R\text{-}TS$)와 쓰기($W\text{-}TS$) 허용 | **발생 불가**<br>(대기 없이 즉시 Abort) | 교착상태가 없으나 충돌 빈번 시 연쇄 롤백(Cascading Rollback) 및 재시작 비용 큼 |
| **낙관적 검증 (OCC)** | **Read $\to$ Validation $\to$ Write** 3단계 수행, 트랜잭션 종료 시 충돌 검증 | **발생 불가** | 충돌이 적은 읽기 위주 환경에서 락 오버헤드 0, 쓰기 충돌 시 롤백 비용 급증 |
| **다중버전 제어 (MVCC)** | 데이터 갱신 시 기존 행을 덮어쓰지 않고 Undo 세그먼트에 새 버전을 생성 | 쓰기-쓰기 충돌 시에만 잠금 | **"읽기는 쓰기를 블록하지 않고, 쓰기는 읽기를 블록하지 않음"**, 언두 영역 관리 부담 |

## Ⅳ. 직렬가능성(Serializability) 이론 및 판정

> 트랜잭션 충돌 연산 순서에 사이클이 없으면 충돌 직렬성(Conflict Serializability)을 만족함.

```text
[충돌 연산(Conflict Operation)의 3요소]
1. 서로 다른 트랜잭션 소속 ($T_1 \neq T_2$)
2. 동일한 데이터 항목 접근 ($Q$)
3. 최소 하나 이상의 쓰기 연산 포함 (Read-Write, Write-Read, Write-Write)

[직렬성 검증: 선행 그래프 (Precedence Graph)]
  T1 ──(Write Q)──▶ T2 (Read Q)
  T2 ──(Write R)──▶ T3 (Read R)
  * 그래프 내 사이클(Cycle)이 없으면(DAG 형태) 충돌 직렬성 만족 확정!
```

## Ⅴ. 4대 동시성 제어 기법 종합 비교

> 비관적 환경은 Strict 2PL, 읽기 집약 분산 환경은 MVCC가 현대 DBMS의 표준임.

| 비교 기준 | 2PL (Two-Phase Locking) | 타임스탬프 순서화 | 낙관적 기법 (OCC) | MVCC (Multi-Version) |
|---|---|---|---|---|
| **제어 접근법** | 비관적(Pessimistic) 잠금 제어 | 비관적 시간 정렬 제어 | 낙관적(Optimistic) 사후 검증 | 버전 기반 다중 복사본 제어 |
| **동시성 수준** | 낮음 (락 보유 중 대기 발생) | 중간 (시간순 어긋남 시 롤백) | 높음 (검증 전까지 무대기) | **매우 높음** (읽기-쓰기 무차단) |
| **오버헤드 발생 시점** | 락 획득 및 해제 시점 | 매 읽기/쓰기 시 타임스탬프 갱신 | 트랜잭션 커밋(검증) 시점 | 가비지 컬렉션(Vacuum/Undo) 시점 |
| **대표 적용 DBMS** | 전통 RDBMS 트랜잭션 모드 | 분산 Spanner(TrueTime), 학술 | 메모리 DB, 충돌 희박 웹 서비스 | Oracle, PostgreSQL, MySQL(InnoDB) |

## Ⅵ. 실무 고려사항 및 장애 대책

> 교착상태, 연쇄 롤백, Vacuum 부하를 타임아웃과 스냅샷 격리로 통제함.

- 적용 상황: 대규모 트래픽이 몰리는 수강신청 및 금융 계좌이체 시스템의 동시성 제어

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **교착상태(Deadlock) 빈발** | 복수 자원에 대해 서로 다른 순서로 배타 락(X-Lock) 요청 | 자원 접근 순서 표준화(Sorting) 및 Lock Timeout / Wait-For Graph 탐지 | 트랜잭션 무한 대기 차단 |
| **연쇄 롤백 (Cascading Rollback)** | 기본 2PL에서 락을 조기 반납하여 더티 데이터를 다른 트랜잭션이 참조 | **Strict 2PL** 적용 (모든 X-Lock을 커밋 시점까지 유지) | 원자적 복구 및 연쇄 취소 원천 차단 |
| **MVCC 테이블 팽창(Bloat)** | 장기 실행 트랜잭션으로 인해 오래된 버전 튜플 삭제 불가 | Auto-Vacuum 튜닝, 장기 실행 트랜잭션 자동 킬(Kill) 정책 수립 | 디스크 낭비 방지 및 고속 인덱스 스캔 복원 |

## Ⅶ. 결론 및 기술사적 제언

> 현대 DBMS는 MVCC와 2PL을 결합하여 읽기 성능과 쓰기 정합성을 동시에 달성함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 동시성 제어는 가장 강한 락을 고르는 문제가 아니라 충돌률과 정합성 요구에 맞는 제어를 선택하는 문제다.
- `나라면`: 잔액처럼 쓰기 충돌 피해가 큰 경로는 명시적 비관 잠금을, 조회 중심 경로는 MVCC를 적용하고 격리 이상을 테스트하겠다.

### 실전 답안용 기술사적 제언

- 판정: 업무 불변식, 읽기·쓰기 비율, 충돌률, 허용 재시도 비용으로 제어 방식 선택
- 대안: 핵심 갱신은 Strict 2PL, 충돌 희박 단기 갱신은 OCC, 조회는 MVCC로 분리
- 검증: 직렬성 테스트, 교착·재시도율, 장기 트랜잭션, P95 지연을 부하 시험에서 측정
- 효과: 데이터 정합성을 유지하면서 불필요한 락 대기와 버전 팽창 억제

<div class="itpe-flow-map" role="img" aria-label="동시성 제어 선택과 검증 흐름">
  <div class="itpe-flow-node"><strong>업무 조건</strong><span>문제: 불변식·충돌률·재시도 비용 상이</span></div><div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>제어 선택</strong><span>대안: Strict 2PL·OCC·MVCC 분리 적용</span></div><div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>부하 검증</strong><span>판정: 직렬성·교착·지연·버전 정리 기준 충족</span></div><div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>운영 효과</strong><span>효과: 정합성과 처리량 균형</span></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 동시성 제어(병행제어)는 다중 트랜잭션 환경에서 데이터 일관성과 격리성을 유지하며 직렬가능성(Serializability)을 보장하는 DBMS 스케줄링 기술임.

### 2. 핵심 메커니즘 / 체계
```text
[트랜잭션 연산] ──▶ [직렬성 검증] 선행그래프 비순환(Acyclic)
                       │
                       ├─ 2PL: 확장(Lock) ── 축소(Unlock)
                       ├─ Timestamp: 시작순서 강제 (Thomas Rule)
                       ├─ OCC: Read ── Validate ── Write
                       └─ MVCC: Undo 기반 스냅샷 격리 (읽기/쓰기 분리)
```
- 갱신손실, 오독, 반복불가읽기, 유령읽기 4대 이상현상을 방지함.

### 3. 적용 제언
- 현대 엔터프라이즈는 MVCC 기반 무차단 읽기를 기본으로 하고, 쓰기 충돌 핵심 영역에만 Strict 2PL을 선별 적용하는 하이브리드 전략이 필수적임.

## 출제 이력과 검증 출처

- [PostgreSQL Documentation, Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html)
- [MySQL Reference Manual, InnoDB Locking and Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-transaction-model.html)

## 학습 체크

- [ ] Ⅰ·Ⅱ 개념·이상: 목표 2개와 Lost Update·Dirty Read·Non-repeatable Read·Phantom Read를 재현한다.
- [ ] Ⅲ 기법: 2PL·Timestamp·OCC·MVCC를 대기, 롤백, 버전 비용으로 비교한다.
- [ ] Ⅳ·Ⅴ 직렬성·선택: 충돌 조건 3개와 선행 그래프 비순환 판정을 설명한다.
- [ ] Ⅵ·Ⅶ 운영: 교착·연쇄 롤백·버전 팽창 대책과 업무별 선택 기준을 제시한다.

## 연결 토픽

- 이전 토픽: [데이터 표준화](./008_data_standardization.md)
- 연관 토픽: [트랜잭션 격리 수준](./020_isolation_level.md), [팬텀 충돌](./049_phantom_conflict.md), [트랜잭션(ACID)](./078_transaction.md)
- 다음 토픽: [이상치(탐지 기법·노이즈 구분 포함)](./010_outlier.md)
