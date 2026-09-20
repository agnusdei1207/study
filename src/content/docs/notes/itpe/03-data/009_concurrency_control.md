---
title: "동시성 제어(병행제어)"
category: "03-data"
tags:
  - "동시성제어"
  - "병행제어"
  - "2PL"
  - "MVCC"
  - "OCC"
  - "직렬가능성"
  - "교착상태"
date: "2026-09-20T23:50:43+09:00"
author: "Codex"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터베이스에서 트랜잭션 관리 및 동시성 제어로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>트랜잭션·동시성</span>
  <strong>동시성 제어(병행제어)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 다중 트랜잭션이 데이터베이스를 동시에 공유·접근할 때 상호 간섭으로 인한 데이터 불일치 이상현상을 방지하고, 직렬가능성(Serializability)과 회복가능성(Recoverability)을 보장하는 트랜잭션 통제 메커니즘
- 메커니즘: 동시 트랜잭션 수신 $\rightarrow$ 연산 인터리빙 $\rightarrow$ 제어 기법(2PL·Timestamp·OCC·MVCC) 분기 적용 $\rightarrow$ 선행 그래프(Precedence Graph) 비순환 검증 $\rightarrow$ 커밋/롤백
- 산출물: 트랜잭션 직렬 스케줄 명세서 · 락 매니저(Lock Manager) 대기 큐 · MVCC Undo 세그먼트 · 교착상태(Deadlock) 탐지 그래프

<div class="itpe-flow-map" role="img" aria-label="다중 트랜잭션 동시성 제어 및 직렬가능성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 다중 트랜잭션 인터리빙 연산 수신</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>접근</strong><span>복수 트랜잭션($T_1, T_2$)의 동시 Read/Write 요청 인터리빙</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 4대 동시성 제어 메커니즘 분기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>2PL (로킹)</strong><span>확장기(Lock) $\to$ 축소기(Unlock), Strict 2PL 적용</span></div>
      <div class="itpe-flow-branch"><strong>Timestamp</strong><span>시작 시간순 정렬 강제, Thomas Write Rule</span></div>
      <div class="itpe-flow-branch"><strong>OCC (낙관적)</strong><span>Read $\to$ Validation(검증) $\to$ Write 3단계</span></div>
      <div class="itpe-flow-branch"><strong>MVCC (다중버전)</strong><span>스냅샷 격리, Undo 로그 활용 읽기-쓰기 무차단</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 선행 그래프(Precedence Graph) 비순환 검증</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>검증</strong><span>충돌 직렬성(Conflict Serializability) 충족 여부 위상 정렬 확인</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 직렬가능성 및 회복가능성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>선행 그래프가 비순환(Acyclic)이며, 모든 배타 락이 커밋 시점까지 유지되는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (안전한 커밋 승인)</strong>
      <span>직렬 수행 동등성 확정 $\rightarrow$ 디스크 영속화(WAL Flushed) 및 락 즉시 해제</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (교착상태 / 연쇄 롤백 위험)</strong>
      <span>트랜잭션 중단(Abort) $\rightarrow$ 희생자(Victim) 선정 롤백 후 백오프 재시도</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Serializability(직렬가능성)`: 복수 트랜잭션이 병행 실행된 결과가 어떤 순차적(Serial) 직렬 실행 결과와 정확히 동등함을 보장하는 성질
- `2PL(Two-Phase Locking)`: 락을 획득만 할 수 있는 확장 단계(Growing Phase)와 반납만 할 수 있는 축소 단계(Shrinking Phase)를 분리하는 로킹 규약
- `Strict 2PL`: 트랜잭션이 최종 커밋/어보트될 때까지 모든 배타 락(X-Lock)을 유지하여 연쇄 롤백(Cascading Rollback)을 원천 차단하는 기법
- `OCC(Optimistic Concurrency Control)`: 충돌이 드물 것이라 가정하고 트랜잭션 수행 중 락을 잡지 않다가 커밋 직전 검증(Validation)하는 낙관적 기법
- `MVCC(Multi-Version Concurrency Control)`: 데이터 갱신 시 기존 데이터를 덮어쓰지 않고 Undo 세그먼트에 이전 버전을 남겨 '읽기는 쓰기를 막지 않는' 고성능 기법
- `Lost Update(갱신 손실)`: 두 트랜잭션이 동일 데이터를 동시 갱신할 때 한쪽의 변경 내용이 다른 쪽에 의해 덮어씌워져 유실되는 현상

</details>

## 예상문제

> 데이터베이스에서 다중 트랜잭션 동시 실행 시 발생 가능한 4대 이상현상(Lost Update, Dirty Read 등)을 제시하고, 이를 방지하기 위한 직렬성(Serializability) 이론 및 4대 동시성 제어 기법(2PL, Timestamp, OCC, MVCC)의 동작 원리와 장단점을 비교 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **병행수행 4대 이상현상** | 갱신 손실(Lost Update), 오독(Dirty Read), 반복불가 읽기, 유령 읽기 | Ⅱ 이상현상 |
| **Strict 2PL** | 확장기, 축소기, 커밋 시점 배타 락 해제, 연쇄 롤백 차단 | Ⅲ·Ⅴ 기법 |
| **MVCC 메커니즘** | Undo Log, Read View, 스냅샷 격리(Snapshot Isolation), 진공(Vacuum) | Ⅲ·Ⅵ |

## Ⅰ. 트랜잭션 고립성과 처리량의 균형추, 동시성 제어의 개요

> 동시성 제어는 다중 트랜잭션의 병행 수행 결과를 직렬 수행 결과와 동일하게 보장하는 기술임.

- 정의: 다중 사용자 환경에서 동시에 실행되는 복수 트랜잭션의 인터리빙(Interleaving) 연산을 스케줄링하여, 트랜잭션의 격리성(Isolation)과 일관성(Consistency)을 유지하고 데이터 손상을 방지하는 DBMS 핵심 엔진 기술
- 필요성: 단순 직렬(Serial) 처리는 데이터 정합성은 완벽하나 CPU 및 디스크 I/O 유휴로 시스템 처리량(Throughput)이 급감하며, 무제어 병행 처리는 갱신 손실 등 치명적 불일치 유발
- 목표: 직렬 실행과 동일한 결과를 보장하는 직렬가능성(Serializability) 달성 및 트랜잭션 장애 시 연쇄 복구를 방지하는 회복가능성(Recoverability) 확보

## Ⅱ. 병행수행 제어 결여 시 발생하는 4대 이상현상

> 트랜잭션 격리성이 깨질 때 데이터베이스에 치명적인 데이터 오염이 발생함.

```text
[갱신 손실] T1 쓰기 ───> T2 쓰기 덮어씀 ───> T1 변경분 완전 소실
[오독]     T1 쓰기 ───> T2 읽음 ───> T1 롤백 ───> T2는 무효 데이터(더티) 처리
```

| 이상현상 | 발생 메커니즘 및 시나리오 | 비즈니스 영향도 |
|---|---|---|
| **갱신 손실 (Lost Update)** | $T_1$과 $T_2$가 동일 레코드를 읽고 순차 갱신 시, $T_2$의 커밋이 $T_1$의 갱신을 덮어씀 | 금융 잔액 계산 오류, 좌석 이중 예약 발생 |
| **오독 (Dirty Read)** | $T_1$이 수정한 미완료 데이터를 $T_2$가 읽은 후, $T_1$이 비정상 Abort/Rollback 됨 | 취소된 결제 내역을 기준으로 배송 출하 오류 |
| **반복불가 읽기 (Non-repeatable Read)** | $T_1$이 동일 데이터를 두 번 읽는 도중, $T_2$가 해당 데이터를 수정·커밋하여 값이 달라짐 | 동일 트랜잭션 내에서 조회 결과 불일치 발생 |
| **유령 읽기 (Phantom Read)** | $T_1$이 조건 검색 수행 후, $T_2$가 해당 조건에 부합하는 신규 레코드를 삽입(Insert) 커밋함 | 동일 쿼리 재실행 시 보이지 않던 레코드가 출현 |

## Ⅲ. 동시성 제어 4대 알고리즘 메커니즘 비교

> 충돌 빈도·읽기/쓰기 비율·롤백 비용에 따라 2PL·Timestamp·OCC·MVCC를 선택하며, DBMS별 구현 방식을 확인함.

| 비교 기준 | 2PL (Two-Phase Locking) | 타임스탬프 순서화 | 낙관적 기법 (OCC) | MVCC (Multi-Version) |
|---|---|---|---|---|
| **제어 접근법** | 비관적(Pessimistic) 잠금 제어 | 비관적 시간 정렬 제어 | 낙관적(Optimistic) 사후 검증 | 버전 기반 다중 복사본 제어 |
| **동시성 수준** | 낮음 (락 보유 중 대기 발생) | 중간 (시간순 어긋남 시 롤백) | 높음 (검증 전까지 무대기) | **매우 높음** (읽기-쓰기 무차단) |
| **오버헤드 발생 시점** | 락 획득 및 해제 시점 | 매 읽기/쓰기 시 타임스탬프 갱신 | 트랜잭션 커밋(검증) 시점 | 가비지 컬렉션(Vacuum/Undo) 시점 |
| **교착상태 위험** | 존재 (상호 락 대기 발생) | 없음 (선점/어보트 처리) | 없음 (락 미사용) | 없음 (읽기 연산에 한함) |
| **대표 적용 DBMS** | 전통 RDBMS 트랜잭션 모드 | 분산 Spanner(TrueTime), 학술 | 메모리 DB, 충돌 희박 웹 서비스 | Oracle, PostgreSQL, MySQL(InnoDB) |

## Ⅳ. 직렬가능성(Serializability) 검증: 선행 그래프(Precedence Graph)

> 충돌 직렬성(Conflict Serializability)을 만족하려면 직렬화 그래프에 사이클이 없어야 함.

```text
충돌 조건: 서로 다른 트랜잭션이 동일 데이터 항목에 접근하고, 최소 하나가 Write 연산일 때!
  - Write-Read (WR), Read-Write (RW), Write-Write (WW) 충돌 발생 시 간선(Edge) 연결
```

```text
[정상 스케줄: 비순환 그래프]           [비정상 스케줄: 순환 그래프 (직렬 불가)]
    T1 ───────▶ T2                           T1 ◀──────▶ T2
  (비순환: 직렬가능성 만족)                 (Cycle 발생: 교착 또는 불일치 발생!)
```

- **판정 규칙**: 트랜잭션을 노드(Node)로, 충돌 연산의 선후관계를 방향성 간선(Directed Edge)으로 그린 선행 그래프가 **비순환(Acyclic)**일 때만 충돌 직렬성을 보장함

## Ⅴ. 2PL(Two-Phase Locking) vs MVCC 심층 대비

> 현대 고성능 트랜잭션 엔진의 양대 산맥을 비교 분석함.

```text
[2PL 로킹 메커니즘]
Lock 수
  ▲      확장 단계 (Growing)       축소 단계 (Shrinking)
  │          / ─── 최대 락 보유 ─── ＼
  │        /                         ＼
  └──────/─────────────────────────────＼─────▶ 시간
       (오직 Lock 획득만 가능)       (오직 Unlock만 가능)

[MVCC 스냅샷 격리 메커니즘]
데이터 블록 ──(UPDATE 발생 시)──> [새 튜플 Write (X-Lock)]
                                        │
                                (이전 버전 Undo 포인터)
                                        ▼
                                [Undo 세그먼트 (S-Lock 없는 일관된 읽기 제공)]
```

- **Strict 2PL의 우수성**: 기본 2PL은 조기 언락으로 인해 연쇄 롤백 위험이 있으나, Strict 2PL은 모든 배타 락을 커밋 시점까지 유지하여 엄격한 회복가능성(Strict Recoverability) 보장
- **MVCC의 혁신**: Undo 로그를 활용하여 쿼리 시작 시점의 스냅샷을 읽으므로 읽기 세션이 쓰기 세션을 대기하지 않아 조회 성능 극대화

## Ⅵ. 동시성 제어 문제점·대응책

> 교착상태, 연쇄 롤백, Vacuum 부하를 타임아웃과 스냅샷 격리로 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 복수 트랜잭션 간 교착상태(Deadlock) 빈발 | 자원 접근 순서 표준화(Sorting) 및 Lock Timeout / Wait-For Graph 탐지 | 트랜잭션 무한 대기 원천 차단 및 자동 회복 |
| 락 조기 반납으로 인한 연쇄 롤백 (Cascading Rollback) | **Strict 2PL** 적용 (모든 배타 락을 커밋 시점까지 강제 유지) | 원자적 복구 보장 및 타 트랜잭션 연쇄 취소 예방 |
| MVCC 장기 트랜잭션으로 인한 테이블 팽창 (Bloat) | Auto-Vacuum 적극 튜닝 및 임계치 초과 장기 세션 자동 종료 정책 수립 | 불필요한 데드 튜플 청소 및 인덱스 스캔 속도 정상화 |
| 낙관적 락(OCC) 잦은 충돌로 인한 롤백 폭증 | 충돌 빈도가 높은 핵심 갱신 자원에 대해 선별적 비관 락(`FOR UPDATE`) 전환 | 과도한 재시도로 인한 CPU 부하 및 처리량 저하 방지 |

## Ⅶ. 기술사적 제언: MVCC와 비관 락의 하이브리드 아키텍처

> "완벽한 단일 동시성 제어 기법은 없다. 데이터의 충돌 빈도와 비즈니스 정합성 요건에 맞춘 선별적 결합이 기술사의 해법이다."

### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 동시성 제어는 가장 강한 락을 고르는 문제가 아니라 충돌률과 정합성 요구에 맞는 제어를 선택하는 문제다.
- `나라면`: 잔액처럼 쓰기 충돌 피해가 큰 경로는 명시적 비관 잠금을, 조회 중심 경로는 MVCC를 적용하고 격리 이상을 테스트하겠다.

### 실전 답안용 기술사적 제언
- 판정: 비즈니스 업무 불변식, 읽기/쓰기 트래픽 비율, 충돌 허용 여부를 기준으로 동시성 제어 기법을 분리 적용함
- 대안: 대규모 조회가 집중되는 웹 서비스는 **MVCC 스냅샷 격리**를 기본으로 하고, 금융 계좌 잔액 등 쓰기 충돌 손실이 치명적인 도메인은 **Strict 2PL 기반 비관 잠금**(`SELECT ... FOR UPDATE`)으로 격리
- 검증: 카오스 엔지니어링 동시성 테스트를 통한 갱신 손실 제로(0건) 및 교착상태 발생률 0.01% 이하 유지
- 효과: 높은 트랜잭션 처리량(TPS)과 금융권 수준의 절대적 데이터 무결성 동시 달성

```text
[현행 한계] ─────────> [개선 방안] ─────────> [검증 기준] ─────────> [실행 효과]
전면 락으로 인한 병목  MVCC + Strict 2PL 분리 갱신 손실 0건 달성      초당 처리량(TPS) 극대화
데드락 빈발            트랜잭션 자원 정렬     교착 발생률 < 0.01%     안정적 무결성 보장
```

## 1교시 10점 답안 발췌

```text
1. 동시성 제어(병행제어)의 정의 및 목적
- 정의: 다중 트랜잭션 환경에서 일관성과 고립성을 유지하며 직렬가능성(Serializability)을 보장하는 스케줄링 기술
- 목적: 4대 이상현상(갱신 손실, 오독, 반복불가 읽기, 유령 읽기) 방지 및 처리량 극대화

2. 4대 동시성 제어 기법 핵심 비교
┌───────────────┬─────────────────────────────────────────────┐
│ 기법          │ 동작 원리 및 핵심 특징                      │
├───────────────┼─────────────────────────────────────────────┤
│ 2PL           │ 확장기(Lock 획득) → 축소기(Lock 해제) 규약   │
│ Strict 2PL    │ 모든 배타 락을 커밋 시점까지 유지 (연쇄롤백 방지) │
│ Timestamp     │ 트랜잭션 시작 시간순 정렬 (Thomas Write Rule) │
│ OCC           │ 판독(Read) → 검증(Validation) → 기록(Write)  │
│ MVCC          │ Undo 로그 스냅샷 격리, '읽기는 쓰기를 막지 않음'│
└───────────────┴─────────────────────────────────────────────┘

3. 직렬성 판정 및 실무 제언
- 선행 그래프(Precedence Graph) 비순환(Acyclic) 검증 필수
- 조회는 MVCC, 핵심 쓰기 충돌은 Strict 2PL을 결합한 하이브리드 아키텍처 구축 권고
```

## 출제 이력과 검증 출처

- **기출 근거**: 제121·128·130회는 KPC 보조자료이며 Q-Net 공식 원문 미확보
- **검증 출처**: [PostgreSQL Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html), [MySQL InnoDB Locking and Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-transaction-model.html)

## 학습 체크

- [ ] [Ⅰ 개요]: 직렬가능성과 회복가능성 관점의 동시성 제어 정의를 제시하였는가?
- [ ] [Ⅱ 이상현상]: 갱신 손실, 오독, 반복불가 읽기, 유령 읽기의 발생 원리를 구분하였는가?
- [ ] [Ⅲ 기법]: 2PL, Timestamp, OCC, MVCC 4대 기법의 장단점을 비교표로 정리하였는가?
- [ ] [Ⅳ 직렬성]: 충돌 조건(WR, RW, WW)과 선행 그래프의 비순환 판정 기준을 설명하였는가?

## 연결 토픽

- [트랜잭션 격리 수준](./020_isolation_level.md) · [트랜잭션(ACID)](./078_transaction.md) · [팬텀 충돌](./049_phantom_conflict.md) · [데이터 표준화](./008_data_standardization.md)
