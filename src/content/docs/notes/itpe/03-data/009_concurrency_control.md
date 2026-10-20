---
title: "동시성 제어"
author: "agnusdei1207"
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

## 연관 키워드

- 동시성 제어(Concurrency Control), 트랜잭션, 직렬 가능성(Serializability), 로킹(Locking), 2PL
- 타임스탬프 순서화, 낙관적 병행 제어, MVCC, 교착상태(Deadlock), 격리 수준(Isolation Level)

## Ⅰ. 동시성 제어의 개요

- 핵심 요약 : 다중 트랜잭션의 병행 실행에서 무결성·일관성을 지키며 직렬 가능성을 보장하는 기술.
- 개념 : 다중 사용자(Multi-User) DBMS(Database Management System) 환경에서 여러 트랜잭션이 데이터베이스를 동시에 공유 접근할 때 데이터의 무결성(Integrity)과 일관성(Consistency)을 파괴하지 않으면서 트랜잭션을 병행 실행하도록 제어하는 기술.
- 배경 및 필요성 :
  1. 갱신 분실(Lost Update) : T1의 갱신을 T2가 덮어써서 T1의 변경 소실.
  2. 모순성(Inconsistency) : T1 수행 중 T2의 일부 갱신으로 불일치 상태의 조회.
  3. 연쇄 복귀(Cascading Rollback) : T1 롤백 시 T1의 미커밋 데이터를 읽은 T2의 연쇄 롤백 필요.
  4. 비재현성(Unrepeatable Read) : 한 트랜잭션 내 동일 데이터 재조회 값의 불일치.
- 주요 목적 : 직렬 가능성(Serializability) 보장, 즉 각 트랜잭션이 순차 실행된 것과 동일한 결과의 생성.

## Ⅱ. 동시성 제어의 특징

- 핵심 요약 : 직렬 가능성 목표 아래 로킹·타임스탬프·낙관적 제어·MVCC의 4대 기법 구성.

1. 직렬 가능성 목표 : 병행 실행 결과의 순차 실행 결과와의 동일성 보장.
2. 4대 이상 현상의 방지 대상 : 갱신 분실, 모순성, 연쇄 복귀, 비재현성.
3. 상호 보완적 4대 기법 : 로킹, 타임스탬프 순서화, 낙관적 병행 제어, 다중 버전 동시성 제어(MVCC, Multi-Version Concurrency Control).
4. 격리 수준과의 연계 : 트랜잭션 격리 수준(Isolation Level) 설정을 통한 정합성·성능의 균형.

```text
[ 4대 동시성 이상 현상 ]
 1. 갱신 분실 (Lost Update)        : T1의 갱신을 T2가 덮어써서 T1의 변경 소실
 2. 모순성 (Inconsistency)         : T2의 부분 갱신으로 T1이 불일치 상태를 조회
 3. 연쇄 복귀 (Cascading Rollback) : T1 롤백 시 미커밋 데이터를 읽은 T2의 연쇄 롤백 필요
 4. 비재현성 (Unrepeatable Read)   : 한 트랜잭션 내 동일 데이터의 재조회 값 불일치
```

## Ⅲ. 동시성 제어의 구조 (흐름)

- 핵심 요약 : 2단계 로킹 규약의 단계 구조와 MVCC의 무차단 읽기 원리, 교착상태의 예방·회피·탐지 전략.

```text
[ 2PL vs Strict 2PL 단계 비교 ]
 Basic 2PL  : [확장 단계: Lock 획득] → (최대 락 도달) → [축소 단계: Unlock 수행]
 Strict 2PL : [확장 단계: Lock 획득] → [모든 X-Lock을 커밋/롤백 시점까지 유지 후 일괄 해제]
              * Strict 2PL은 연쇄 복귀 문제의 원천 차단
```

```text
[ MVCC 기반 무차단 읽기(Non-blocking Read) 원리 ]
 T1 (Write) : Row A의 새 버전 V2 생성 (Commit 대기)
 T2 (Read)  : Row A 요청 → T1의 락과 무관하게
              이전 버전 V1(Undo Segment) 즉시 반환 (대기 없음)
```

- 교착상태(Deadlock) 해결 전략 :
  1. 예방(Prevention) : 타임스탬프 기반의 Wait-Die(오래된 트랜잭션 대기)와 Wound-Wait(오래된 트랜잭션 선점 취소).
  2. 회피(Avoidance) : 자원 할당 그래프(WFG, Wait-For Graph) 기반의 사이클 발생 가능성 사전 차단(은행가 알고리즘).
  3. 탐지·복구(Detection & Recovery) : WFG 주기적 사이클 탐지 후 희생자(Victim) 선정 롤백.

## Ⅳ. 동시성 제어 4대 기법의 비교

- 핵심 요약 : 확실한 차단의 로킹, 순서 고정의 타임스탬프, 읽기 최적화의 낙관적 제어, 무차단 읽기의 MVCC.

| 제어 기법 | 동작 원리 및 메커니즘 | 직렬성 보장 방식 | 주요 장단점 |
|---|---|---|---|
| 로킹(Locking) | 데이터 항목 접근 전 Lock 획득, 완료 후 Unlock(공유락(Shared Lock, S-Lock), 배타락(Exclusive Lock, X-Lock)) | 2단계 로킹 규약(2PL, Two-Phase Locking) 준수(확장 단계 획득, 축소 단계 해제) | 구현 직관적·충돌 차단 확실 / 교착상태(Deadlock) 발생 가능, 동시성 저하 |
| 타임스탬프 순서화(Timestamp Ordering) | 트랜잭션 시작 시 고유 타임스탬프 TS(T) 부여, 읽기·쓰기 타임스탬프와 비교 | 직렬 순서의 진입 순서(TS) 고정, 규칙 위반 시 Abort 후 재시작 | 교착상태 완전 배제 / 연쇄 복귀 위험, 잦은 Abort로 처리량 저하 |
| 낙관적 병행 제어(Optimistic/Validation) | 수행 중 락 없이 로컬 작업 후 커밋 시점의 충돌 검증(판독 → 확인 → 기록) | 유효성 검사 단계에서 읽기 셋·쓰기 셋의 겹침 확인 | 읽기 위주 환경에서 높은 처리량 / 쓰기 충돌 빈번 시 롤백 비용 급증 |
| 다중 버전 동시성 제어(MVCC) | 갱신 시 원본을 덮어쓰지 않는 신규 버전 생성, 타임스탬프 또는 SCN(System Change Number)과 함께 보관 | 읽기 작업의 트랜잭션 시작 시점 스냅샷 버전 참조(읽기-쓰기 락 차단 배제) | 읽기·쓰기의 상호 블로킹 없음(Oracle, PostgreSQL 표준) / 언두·버전 스토리지 관리 오버헤드 |

## Ⅴ. 동시성 제어의 장점과 한계

- 핵심 요약 : 무결성 보장·무차단 읽기의 장점과 교착상태·Abort 폭포·언두 누적의 한계.

- 장점
  1. 다중 트랜잭션 병행 환경의 무결성·일관성 보장.
  2. MVCC 기반 읽기-쓰기 무차단을 통한 동시 처리량 향상.
  3. 워크로드 특성별 기법 선택의 유연성.

- 한계점 1 : 비관적 락(Pessimistic Lock) 기반 직렬화의 교착상태 및 병목
  - 한계점 : 엄격한 2PL 환경에서 트랜잭션 간 자원 점유 순서 불일치 시 데드락 빈발, 락 에스컬레이션(Lock Escalation)에 따른 동시 처리량 급락.
  - 해결 방안 : 자원 획득 순서의 전사적 표준화(글로벌 정렬 순서 준수), 락 타임아웃(Lock Timeout) 설정 및 Wait-Die·Wound-Wait 알고리즘 기반 교착상태 선제 예방.
- 한계점 2 : 낙관적 동시성 제어(OCC, Optimistic Concurrency Control)의 Abort 폭포
  - 한계점 : 검증(Validation) 단계 충돌 시 트랜잭션 롤백 구조로 핫스팟 데이터 경합 시 재시도(Retry) 루프에 따른 시스템 리소스 낭비 심화.
  - 해결 방안 : 분산 카운터(Distributed Counter)와 파티셔닝 기반 경합 분산, 지수 백오프(Exponential Backoff with Jitter) 재시도 전략의 결합.
- 한계점 3 : MVCC 환경의 언두(Undo)·가비지 데이터 누적 및 성능 저하
  - 한계점 : 장기 실행 트랜잭션(Long-running Query) 존재 시 이전 버전 레코드의 미정리로 PostgreSQL의 Table Bloat, Oracle의 ORA-01555(Snapshot Too Old) 발생.
  - 해결 방안 : 트랜잭션 실행 시간 임계치 모니터링·자동 킬(Kill) 정책, VACUUM 튜닝(PostgreSQL autovacuum worker 최적화) 및 Undo 세그먼트 동적 확장.

## Ⅵ. 고성능 동시성 제어 설계를 위한 기술사적 제언

- 핵심 요약 : 격리 수준의 전략적 튜닝, 트랜잭션 단위 최소화, 분산 락의 선별 도입.
- 트랜잭션 격리 수준(Isolation Level)의 전략적 튜닝 : 기본값(Repeatable Read 또는 Read Committed)의 맹목적 의존 지양, 단순 집계·통계 쿼리의 낮은 격리 수준 또는 스냅샷 읽기 적용을 통한 락 경합 방지.
- 트랜잭션 단위 최소화 : 트랜잭션 블록 내 외부 API(Application Programming Interface) 호출, 파일 I/O, 무거운 연산 등 지연 요소의 일체 배제를 통한 락 유지 시간의 밀리초(ms) 단위 이하 축소.
- 분산 환경의 분산 락(Distributed Lock) 활용 : 마이크로서비스 아키텍처(MSA, Microservice Architecture)에서 DB(Database) 단일 로킹 불가 환경의 Redis Redlock 또는 Zookeeper 기반 임계 영역 제어의 선별적 도입.

## Ⅶ. 결론

- 핵심 요약 : 동시성 제어는 직렬 가능성 보장과 처리량 확보의 균형 설계가 핵심.
- 요약 : 4대 기법(로킹·타임스탬프·낙관적·MVCC)의 특성과 교착상태 3단 대응 전략.
- 시사점 : 워크로드별 기법·격리 수준 선택과 트랜잭션 최소화 설계 필요.
