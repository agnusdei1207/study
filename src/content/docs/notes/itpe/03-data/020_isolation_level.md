---
title: "트랜잭션 격리 수준"
author: "agnusdei1207"
date: "2026-10-25T00:09:56+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 트랜잭션 격리 수준(Isolation Level), ANSI/ISO SQL 표준, 동시성(Concurrency), 정합성(Consistency)
- Dirty Read, Non-Repeatable Read, Phantom Read, MVCC(Multi-Version Concurrency Control), 스냅샷 격리(Snapshot Isolation), 쓰기 편향(Write Skew), SSI(Serializable Snapshot Isolation)

## Ⅰ. 트랜잭션 격리 수준의 개요

- 핵심 요약 : 동시에 실행되는 트랜잭션 사이에서 변경 데이터를 얼마나 볼 수 있는지 정하는 표준 제어 기준.
- 개념 : ANSI(American National Standards Institute)/ISO(International Organization for Standardization)가 SQL(Structured Query Language) 표준(SQL-92)에서 정의한, 한 트랜잭션의 미확정·확정 변경을 다른 트랜잭션이 어느 수준까지 볼 수 있는지 정하는 기준인 **트랜잭션 격리 수준**(Isolation Level).
- 배경 및 필요성 : 격리 수준을 높이면 정합성은 완벽해지지만 동시 처리량이 떨어지고, 낮추면 처리량은 오르지만 읽기 이상 현상이 나타난다. 이 상충을 조절할 기준이 없으면 업무별 정합성 요구를 맞추기 어렵다.
- 주요 목적 : 동시성과 정합성 사이의 균형점을 표준 단계로 제시하여 트랜잭션 처리 품질 기준을 세우는 것.

## Ⅱ. 트랜잭션 격리 수준의 특징

- 핵심 요약 : 4단계 표준 수준, 정합성과 동시성의 트레이드오프, 잠금과 다중 버전 기법의 병행 구조.

1. 표준 4단계 체계 : 네 단계의 수준을 선택 → 업무 요구에 맞는 정합성 강도를 고를 수 있음.
2. 트레이드오프 구조 : 수준이 올라갈수록 정합성은 강화 → 락 대기와 롤백이 늘어 동시성은 저하.
3. 읽기 이상 현상의 차등 방지 : 3대 읽기 이상(Dirty Read, Non-Repeatable Read, Phantom Read)을 수준별로 다르게 막음 → 허용 가능한 이상 현상만 남김.
4. 잠금과 다중 버전 병행 : 공유락(S-Lock)·배타락(X-Lock)과 함께 **MVCC**(Multi-Version Concurrency Control) 스냅샷을 쓰는 구조 → 읽기와 쓰기의 간섭 감소.
5. 벤더별 구현 차이 : MySQL InnoDB의 갭 락(Gap Lock), Oracle의 READ UNCOMMITTED 미지원처럼 표준과 다른 동작 존재 → 이기종 DBMS 간 동작 검증 필요.

## Ⅲ. 트랜잭션 격리 수준의 구조 (흐름)

- 핵심 요약 : 3대 읽기 이상 현상과 4단계 수준의 대응 계층, 그리고 스냅샷 격리의 쓰기 편향 한계.

```text
[ 3대 전통 읽기 이상 현상 ]
Dirty Read : 미확정 변경 값을 읽음
Non-Repeatable Read : 같은 행의 값이 바뀜
Phantom Read : 같은 조건에 새 행이 나타남
```

```text
[ 격리 수준 계층 ]
SERIALIZABLE : 이상 현상 모두 차단
        ↑
REPEATABLE READ : Phantom Read만 발생
        ↑
READ COMMITTED : Dirty Read만 차단
        ↑
READ UNCOMMITTED : 이상 현상 모두 허용
```

- 트랜잭션 시작 시점의 일관된 스냅샷을 읽는 **스냅샷 격리**(Snapshot Isolation)는 읽기 작업에 잠금이 필요 없다. 같은 데이터를 동시에 갱신하면 먼저 커밋한 트랜잭션만 성공하는 First-Committer-Wins 원칙으로 갱신 분실을 막는다.
- 스냅샷 격리에서도 서로 다른 행을 갱신하는 두 트랜잭션이 함께 제약을 깨뜨리는 **쓰기 편향**(Write Skew) 이상이 남는다.

```text
[ 쓰기 편향 발생 과정 ]
제약 : 당직 의사는 최소 1명
T1 : 당직 의사 2명 조회 → A 해제 후 커밋
T2 : 당직 의사 2명 조회 → B 해제 후 커밋
결과 : 당직 의사 0명으로 제약 위반
```

## Ⅳ. 4대 트랜잭션 격리 수준의 비교

- 핵심 요약 : 수준별 허용 이상 현상과 잠금·MVCC 기반 구현 방식의 차이.

| 격리 수준 | Dirty Read | Non-Repeatable Read | Phantom Read | 구현 방식 |
| --- | --- | --- | --- | --- |
| READ UNCOMMITTED | 발생 가능 | 발생 가능 | 발생 가능 | 읽기 잠금 없이 미확정 값까지 읽음 |
| READ COMMITTED | 차단 | 발생 가능 | 발생 가능 | 커밋된 값만 읽으며, 문장 시작 시점의 MVCC 스냅샷 참조 (Oracle, PostgreSQL 기본값) |
| REPEATABLE READ | 차단 | 차단 | 발생 가능 | 트랜잭션 시작 시점의 스냅샷을 끝까지 유지 (MySQL InnoDB 기본값) |
| SERIALIZABLE | 차단 | 차단 | 차단 | 범위 잠금(Next-Key Lock) 또는 SSI로 직렬 실행과 동등한 결과 보장 |

- 참고 : MySQL InnoDB는 REPEATABLE READ에서도 MVCC 스냅샷 읽기와 넥스트 키 락으로 팬텀 읽기 대부분을 막는다.

## Ⅴ. 트랜잭션 격리 수준의 장점과 한계

- 핵심 요약 : 정합성 제어의 표준화와 잠금 없는 읽기가 장점이며, 동시성 상충과 쓰기 편향, 벤더 차이가 한계.

- 장점
  1. 표준화된 정합성 기준으로 이기종 환경에서 공통 언어 확보.
  2. MVCC 스냅샷 읽기로 읽기와 쓰기의 간섭 최소화.
  3. 업무 특성에 따라 수준을 골라 쓸 수 있는 유연성.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 동시성과 정합성의 상충 | 최고 수준은 락 경합과 롤백 증가로 처리량 저하, 낮은 수준은 이상 현상 노출 | 도메인별 차등 격리 수준 적용 (금융 결제 등 핵심 거래는 강한 수준, 단순 조회는 READ COMMITTED), 낙관적 검증 병행 | 롤백률, 락 대기 시간 |
| 스냅샷 격리의 쓰기 편향 | 서로 다른 행을 갱신하는 교차 트랜잭션이 제약을 깨뜨림 | SELECT FOR UPDATE로 명시적 잠금을 걸거나 SSI 엔진 활성화 | 제약 위반 건수 |
| 벤더별 구현 차이 | 갭 락 기반 팬텀 방지, READ UNCOMMITTED 미지원 등으로 DBMS 전환 시 동작 변화 | 프레임워크 계층에서 격리 수준 의존 로직 추상화, 전환 시 동시성 통합 테스트 의무화 | 동시성 테스트 통과율 |

## Ⅵ. 트랜잭션 격리 수준에 대한 기술사적 제언

- 핵심 요약 : 기본 수준은 처리량 중심으로 두고, 정합성이 핵심인 거래에만 명시적 잠금을 결합하며, 분산 환경은 직렬성 보장 여부를 먼저 확인.

대부분의 글로벌 OLTP(Online Transaction Processing) 시스템은 처리량을 확보하기 위해 READ COMMITTED를 기본값으로 두는 것이 현실적이다. 대신 잔액 차감처럼 정합성이 생명인 갱신에는 SELECT ... FOR UPDATE나 조건부 원자 UPDATE를 결합하여 필요한 곳에서만 강하게 막는다.

분산 데이터베이스나 NewSQL을 도입할 때는 엄격한 직렬성(Strict Serializable)을 제공하는지, 세션 수준의 일관성만 보장하는지를 벤더 문서와 검증 테스트로 확인한 뒤 아키텍처를 설계해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 격리 수준은 동시성과 정합성의 균형을 정하는 핵심 기준이며, 벤더 차이와 스냅샷 한계를 함께 이해해야 하는 개념.
- 시사점 : 업무별 차등 적용과 명시적 잠금 보완으로 정합성과 처리량을 함께 확보하는 것이 격리 수준 설계의 요체.
