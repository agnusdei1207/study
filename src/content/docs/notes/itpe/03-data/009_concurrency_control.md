---
title: "동시성 제어"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 다중 사용자 환경에서의 트랜잭션 동시성 제어 개요

### 가. 동시성 제어(Concurrency Control)의 정의
- **동시성 제어**는 다중 사용자(Multi-User) DBMS 환경에서 여러 트랜잭션이 데이터베이스를 동시에 공유하여 접근할 때, 데이터의 무결성(Integrity)과 일관성(Consistency)을 파괴하지 않으면서 트랜잭션을 병행 실행하도록 제어하는 기술.
- 직렬 가능성(Serializability)을 보장하여 각 트랜잭션이 순차적으로 실행된 것과 동일한 결과를 생성하도록 보장함.

### 나. 동시성 제어 미비 시 발생하는 4대 데이터 이상 현상

```text
[ 4대 동시성 이상 현상 ]
1. 갱신 분실 (Lost Update)       : T1의 갱신을 T2가 덮어써서 T1의 변경이 사라짐
2. 모순성 (Inconsistency)         : T1 수행 중 T2가 일부만 갱신하여 데이터 불일치 상태를 읽음
3. 연쇄 복귀 (Cascading Rollback) : T1이 롤백될 때 T1의 미커밋 데이터를 읽은 T2도 연쇄 롤백 필요
4. 비재현성 (Unrepeatable Read)   : T1이 한 트랜잭션 내에서 동일 데이터를 두 번 읽을 때 값이 달라짐
```

---

## Ⅱ. 동시성 제어 핵심 기법 및 메커니즘 분석

### 가. 동시성 제어 4대 주요 기법 비교

| 제어 기법 | 동작 원리 및 메커니즘 | 직렬성 보장 방식 | 주요 장단점 |
| :--- | :--- | :--- | :--- |
| **로킹 (Locking)** | 트랜잭션이 데이터 항목 접근 전 Lock을 획득하고 완료 후 Unlock (공유락 S-Lock, 배타락 X-Lock) | **2단계 로킹 규약 (2PL)** 준수 (확장 단계에서만 획득, 축소 단계에서만 해제) | 구현 직관적, 트랜잭션 충돌 차단 확실 / 교착상태(Deadlock) 발생 가능, 동시성 저하 |
| **타임스탬프 순서화 (Timestamp Ordering)** | 각 트랜잭션 시작 시 고유 타임스탬프 $TS(T)$를 부여하고 읽기/쓰기 타임스탬프와 비교 | 직렬 순서가 트랜잭션의 진입 순서($TS$)로 고정됨 (규칙 위반 시 해당 트랜잭션 Abort 후 재시작) | 교착상태 완전 배제 / 연쇄 복귀 위험, 잦은 Abort로 인한 처리량 저하 |
| **낙관적 병행 제어 (Optimistic / Validation)** | 트랜잭션 수행 중에는 아무 락도 걸지 않고 로컬 작업 후 커밋 시점에 충돌 검증 (판독 $\rightarrow$ 확인 $\rightarrow$ 기록) | 유효성 검사 단계에서 읽기 셋과 쓰기 셋의 겹침 여부를 확인 | 트랜잭션 읽기 위주 환경에서 극상의 처리량 / 쓰기 충돌 빈번 시 극심한 롤백 비용 |
| **다중 버전 동시성 제어 (MVCC)** | 데이터 갱신 시 원본을 덮어쓰지 않고 새로운 버전을 생성하여 타임스탬프 또는 SCN과 함께 보관 | 읽기 작업은 트랜잭션 시작 시점의 스냅샷 버전을 참조 (읽기-쓰기 간 상호 락 차단 배제) | 읽기와 쓰기가 서로를 블로킹하지 않음 (오라클, PostgreSQL의 표준) / 언두/버전 스토리지 관리 오버헤드 |

### 나. 2단계 로킹 규약(2PL)과 엄격한 2PL(Strict 2PL)

```text
[ 2PL vs Strict 2PL 단계 비교 ]
- Basic 2PL   : [확장 단계(Growing): Lock만 획득] ---> (최대 락 도달) ---> [축소 단계(Shrinking): Unlock만 수행]
- Strict 2PL  : [확장 단계: Lock 획득] ---> [모든 X-Lock은 트랜잭션 커밋/롤백 시점까지 유지 후 일괄 해제]
                (Strict 2PL은 연쇄 복귀 문제를 원천 차단함)
```

---

## Ⅲ. 교착상태(Deadlock)의 해결 방안 및 MVCC 동작 원리

### 가. 교착상태 해결 전략
- **예방 기법 (Prevention)** : 타임스탬프 기반 Wait-Die(오래된 트랜잭션이 대기), Wound-Wait(오래된 트랜잭션이 선점 취소).
- **회피 기법 (Avoidance)** : 자원 할당 그래프(WFG)를 기반으로 사이클 발생 가능성 사전 차단(은행가 알고리즘).
- **탐지 및 복구 (Detection & Recovery)** : WFG 주기적 사이클 탐지 $\rightarrow$ 희생자(Victim) 선정 후 롤백.

### 나. MVCC(Multi-Version Concurrency Control)의 읽기 일관성 메커니즘

```text
[ MVCC 기반 무차단 읽기(Non-blocking Read) 원리 ]
T1 (Write) : Row A의 새 버전 V2 생성 (Commit 대기)
T2 (Read)  : Row A 요청 ---> T1의 락과 무관하게 이전 버전 V1(Undo Segment) 즉시 반환 (대기 없음)
```

---

## Ⅳ. 동시성 제어 메커니즘의 주요 한계점 및 해결 방안

- **비관적 락(Pessimistic Lock) 기반 직렬화의 교착상태(Deadlock) 및 병목** :
  - **한계점** : 엄격한 2PL(Two-Phase Locking) 환경에서 트랜잭션 간 자원 점유 순서 불일치 시 데드락 빈발 및 락 에스컬레이션(Lock Escalation)으로 동시 처리량 급락.
  - **해결 방안** : 자원 획득 순서의 전사적 표준화(글로벌 정렬 순서 준수), 락 타임아웃(Lock Timeout) 설정 및 Wait-Die / Wound-Wait 알고리즘 기반 교착상태 선제 예방.
- **낙관적 동시성 제어(OCC)의 트래픽 폭증 시 Abort 폭포(Cascading Abort)** :
  - **한계점** : 읽기 후 검증(Validation) 단계에서 충돌이 감지되면 트랜잭션을 롤백하므로, 핫스팟 데이터 경합 시 재시도(Retry) 루프로 인한 시스템 리소스 낭비 심화.
  - **해결 방안** : 분산 카운터(Distributed Counter) 및 파티셔닝 기반 경합 분산, 지수 백오프(Exponential Backoff with Jitter) 재시도 전략 결합.
- **MVCC 환경에서의 언두(Undo)/가비지 데이터 누적 및 성능 저하** :
  - **한계점** : 장기 실행 트랜잭션(Long-running Query) 존재 시 이전 버전의 레코드가 정리되지 않아 PostgreSQL의 Table Bloat, Oracle의 ORA-01555(Snapshot Too Old) 발생.
  - **해결 방안** : 트랜잭션 실행 시간 임계치 모니터링 및 자동 킬(Kill) 정책, 진보된 VACUUM 튜닝(PostgreSQL autovacuum worker 최적화) 및 Undo 세그먼트 동적 확장.

---

## Ⅴ. 고성능 동시성 제어 설계를 위한 실무 제언

- **트랜잭션 격리 수준(Isolation Level)의 전략적 튜닝** : 기본값(Repeatable Read 또는 Read Committed)에 맹목적으로 의존하지 않고, 단순 집계나 통계 쿼리에는 더 낮은 격리 수준을 적용하거나 스냅샷 읽기를 강제하여 락 경합을 방지해야 함.
- **트랜잭션 단위 최소화** : 트랜잭션 블록 내에 외부 API 호출, 파일 I/O, 무거운 연산 등 지연 요소를 일체 배제하여 락 유지 시간을 밀리초(ms) 단위 이하로 극단적으로 축소.
- **분산 환경의 분산 락(Distributed Lock) 활용** : 마이크로서비스 아키텍처(MSA)에서는 DB 단일 로킹이 불가능하므로, Redis Redlock 또는 Zookeeper 기반의 임계 영역 제어를 선별적으로 도입할 것을 제언함.
