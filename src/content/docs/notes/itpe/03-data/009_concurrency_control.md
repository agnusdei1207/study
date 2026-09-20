---
sidebar:
  order: 9
  label: "009. 동시성 제어"
  badge:
    text: "A · 핵심 · 96%"
    variant: note
title: "동시성 제어 (Concurrency Control)"
author: "OpenAI Codex"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-data"
weight: 9
extra:
  model: "GPT-5"
  keyword_grade: "A"
  grade_basis: "03-data canonical 목록 A"
  question_no: "009"
  source_status: "학습핵심"
  source_history: "정보관리 공식 기출 미확인"
  priority: 96
  priority_note: "직렬가능성·2PL·Timestamp·OCC·MVCC·교착상태로 확장 가능"
---

## 전체 로드맵 내 현재 위치

```text
[01 IT 전략] → [02 SW 공학] → [▶ 03 데이터] → [04 컴퓨터 시스템]
      → [05 네트워크] → [06 보안] → [07 최신기술] → [08 법규·정책]
```

과목 내 현재 키워드: 03 데이터 → 동시성 제어

## 큰 그림과 30초 인출

```text
T1: Read ─ Write ─ Commit
T2:    Read ─ Write ─ Commit
          │ 상호 간섭
          ▼
 [직렬가능성·회복가능성 보장]
          │
   Lock / Timestamp / OCC / MVCC
          │
  일관성 ↔ 동시 처리량 균형
```

- 본질: **여러 트랜잭션을 동시에 실행하면서 직렬 실행과 동등한 결과와 회복 가능한 스케줄을 보장하는 제어기술**
- 4대 기법: 2PL, Timestamp Ordering, OCC, MVCC
- 암기: `락-시-낙-버` = 락 → 시간순서 → 낙관적 검증 → 다중버전

## 예상문제

> 데이터베이스 동시성 제어의 필요성과 이상현상, 직렬가능성을 설명하고 2PL·Timestamp·OCC·MVCC를 비교하여 실무 적용방안을 논하시오. (25점)

## Ⅰ. 병행처리의 일관성을 보장하는 동시성 제어 개요

- 정의: 동시성 제어는 복수 트랜잭션의 연산 순서를 조정하여 데이터 일관성과 격리성을 지키면서 병행 처리량을 확보하는 기법
- 목적: Lost Update·Dirty Read·Non-repeatable Read·Phantom Read 등 간섭 방지와 직렬가능성 보장
- 필요성: 완전 직렬 실행은 일관되지만 처리량이 낮고, 무제어 병행 실행은 빠르나 데이터 결과가 실행 순서에 따라 달라짐

## Ⅱ. 동시성 제어의 목표와 대표 이상현상

| 목표·현상 | 의미 | 통제 관점 |
|---|---|---|
| 직렬가능성 | 병행 결과가 어떤 직렬 스케줄과 동등 | 충돌/뷰 직렬가능성 |
| 회복가능성 | 읽은 값을 쓴 선행 트랜잭션 이후 커밋 | Commit 의존성 |
| Lost Update | 뒤의 쓰기가 앞의 갱신을 덮음 | Write 충돌·버전 검사 |
| Dirty Read | 미커밋 값을 다른 트랜잭션이 읽음 | 가시성·격리 수준 |
| Non-repeatable Read | 같은 행 재조회 결과가 달라짐 | 행 버전·Lock 유지 |
| Phantom Read | 같은 조건 재조회 시 행 집합이 달라짐 | 범위/Predicate 통제 |

## Ⅲ. 직렬가능성과 4대 제어기법

```text
T1 ──RW 충돌──▶ T2
T2 ──WR 충돌──▶ T3       선행그래프에 Cycle 없음 → 충돌 직렬가능
```

| 기법 | 핵심 원리 | 강점 | 한계 |
|---|---|---|---|
| 2PL | Lock 획득 확장단계 후 해제 축소단계 | 직렬가능성 보장·직관적 | 대기·교착상태 |
| Timestamp | 트랜잭션 시간순서에 맞지 않는 연산 중단 | 교착 없음 | 충돌 시 재시작 증가 |
| OCC | Read-Validate-Write, 커밋 전 충돌 검증 | 충돌 적을 때 무대기 | 충돌 많으면 롤백 비용 |
| MVCC | 여러 버전과 Snapshot 가시성 제공 | Read-Write 경합 감소 | 버전 정리·쓰기 충돌·구현 차이 |

- Strict 2PL은 Commit/Abort까지 배타 Lock을 유지하여 Dirty Read와 연쇄 Rollback을 막음
- MVCC도 모든 이상현상을 자동 제거하는 것은 아니며 격리 수준과 DBMS 구현에 따라 Write Skew 등을 별도 통제

## Ⅳ. 트랜잭션 요청에서 회복까지의 제어 흐름

```text
① Begin → ② Read/Write 요청 → ③ Lock·Timestamp·Snapshot 검사
 → ④ 허용/대기/Abort → ⑤ Commit 검증·로그 확정 → ⑥ Lock/Version 정리
```

| 단계 | 통제사항 | 결과 |
|---|---|---|
| 접근판정 | 객체·범위·버전·충돌 확인 | 실행/대기/재시도 |
| 실행 | Undo/Redo와 가시성 유지 | 격리된 변경 |
| Commit | 제약·충돌·로그 지속성 검증 | 변경 확정 |
| Abort | Undo·버전 폐기·자원 해제 | 원자적 복구 |
| 사후정리 | 오래된 버전·Lock·대기열 정리 | 자원 회수 |

## Ⅴ. 제어기법의 적용 비교

| 판단축 | 2PL | Timestamp | OCC | MVCC |
|---|---|---|---|---|
| 충돌 가정 | 중간~높음 | 순서 위반 시 중단 | 낮음 | 읽기 많음 |
| 대기 | 있음 | 없음 | 실행 중 없음 | 읽기 대기 적음 |
| 실패비용 | 교착·Timeout | 재시작 | 검증 실패 Rollback | 버전·쓰기 충돌 |
| 적합업무 | 강한 갱신 통제 | 순서기반 시스템 | 짧은 저충돌 갱신 | OLTP 읽기·쓰기 혼합 |
| 핵심튜닝 | Lock 범위·순서·시간 | 재시도·Timestamp | 충돌구간·버전 | Snapshot·정리·격리 |

- 선택 기준: 읽기/쓰기 비율, 충돌 빈도, 트랜잭션 길이, 오류 비용, 재시도 가능성을 함께 고려

## Ⅵ. 일관성과 처리량의 균형을 위한 실무 고려사항

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 교착상태 | 트랜잭션별 Lock 순서 상이 | 접근순서 표준화, 짧은 트랜잭션, 탐지·희생자 재시도 | 순환대기 감소 |
| Lock 경합·TPS 저하 | 넓은 범위·장시간 Transaction | 적절한 인덱스, Batch 분할, 외부 I/O 분리 | Lock 보유시간 축소 |
| MVCC 버전 누적 | 장기 Snapshot·정리 지연 | 장기질의 통제, Vacuum/Garbage Collection 감시 | 저장·조회 성능 유지 |
| Lost Update | 읽은 뒤 조건 없이 덮어쓰기 | 버전컬럼·조건부 Update·낙관적 검증 | 갱신 충돌 탐지 |
| 분산 이중갱신 | DB 경계 밖 동시 실행 | 단일 Writer·분산합의·멱등성·업무 보상 | 서비스 간 정합성 확보 |

## Ⅶ. DBMS 기본기법과 업무 불변식을 함께 설계하는 결론

- **[격리수준-업무 불변식-재시도 정책의 결합]**: 격리수준 이름만 선택하면 복합 업무조건의 Write Skew와 분산 갱신을 놓칠 수 있음
- 나라면: 계좌 잔액·재고와 같은 불변식을 명시하고 제약·조건부 갱신·Lock 범위를 설계한 뒤 Deadlock/Serialization Failure를 멱등하게 재시도

#### 한줄 요약

- 동시성 제어의 완성은 충돌을 없애는 것이 아니라 오류 없이 재시도하고 업무 불변식을 끝까지 지키는 상태임

## 1교시 10점 답안 발췌

```text
병행 트랜잭션 → 충돌 검사 → 실행/대기/Abort → Commit·회복
                    Lock / Timestamp / OCC / MVCC
```

| 기법 | 핵심 |
|---|---|
| 2PL | 확장·축소, 직렬성, 교착 위험 |
| Timestamp | 시간순서 위반 시 재시작 |
| OCC | 실행 후 Commit 전 충돌검증 |
| MVCC | Snapshot 버전으로 Read-Write 경합 감소 |

- 차별화: 격리수준뿐 아니라 업무 불변식·조건부 갱신·멱등 재시도를 함께 설계

## 출제 이력과 검증 출처

- [PostgreSQL Documentation, Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html)

## 학습 체크

- [ ] 직렬가능성과 회복가능성을 구분함
- [ ] 4대 기법을 원리·대기·실패비용·적합업무로 비교함
- [ ] MVCC가 모든 이상현상을 제거하지 않음을 씀
- [ ] 결론에서 업무 불변식과 멱등 재시도를 제언함

## 연결 토픽

- [격리 수준](./020_isolation_level/) · [트랜잭션](./078_transaction/) · [팬텀 충돌](./049_phantom_conflict/) · [ACID](./151_acid/)
