---
sidebar:
  order: 20
  label: "020. 트랜잭션 격리 수준"
  badge: { text: "A", variant: note }
title: "트랜잭션 격리 수준 (Isolation Level)"
author: "OpenAI Codex"
date: "2026-09-20T00:25:00+09:00"
tags: ["notes-data"]
weight: 20
extra: { model: "GPT-5", keyword_grade: "A", question_no: "020" }
---

## 지식 로드맵 내 현재 위치
```text
데이터베이스 → 트랜잭션·동시성 → 격리 수준
```

## 큰 그림과 30초 인출
```text
낮은 격리·높은 동시성                         높은 격리·낮은 이상
Read Uncommitted → Read Committed → Repeatable Read → Serializable
 Dirty Read 차단 ─┘  Non-repeatable 차단 ─┘  Phantom·직렬화 이상 차단
```
- 본질: **동시 트랜잭션이 서로의 중간 결과를 어느 범위까지 관찰할지 정한 일관성·동시성 절충 수준**
- 암기: `RU-RC-RR-S`와 `Dirty-Nonrepeatable-Phantom`
- 주의: 실제 보장과 구현은 DBMS의 Lock·MVCC·직렬화 방식에 따라 확인

## 예상문제
> 트랜잭션 격리 수준 4가지와 이상현상을 설명하고 Lock·MVCC 구현 및 업무별 선택 기준을 논하시오. (25점)

## Ⅰ. 동시성 제어의 가시성 계약, 격리 수준 개요
- 정의: 동시에 실행되는 트랜잭션의 읽기·쓰기 결과가 서로에게 보이는 범위를 규정한 수준
- 목적: Dirty Read·Non-repeatable Read·Phantom·직렬화 이상을 통제하면서 처리량 확보
- 관점: ACID의 Isolation을 업무 오류비용과 동시성 요구에 맞게 구현

## Ⅱ. 주요 이상현상
| 이상 | 현상 | 업무 영향 |
|---|---|---|
| Dirty Read | 미커밋 값을 읽음 | 롤백된 값으로 의사결정 |
| Non-repeatable Read | 같은 행 재조회 결과 변경 | 검증 중 값 불일치 |
| Phantom Read | 조건 재조회 시 행 집합 변경 | 집계·범위 규칙 오류 |
| Lost Update | 한 갱신이 다른 갱신을 덮음 | 수량·잔액 손실 |
| Write Skew | 개별 검사는 통과하나 결합 제약 위반 | 당직·한도 규칙 파괴 |

## Ⅲ. ANSI 격리 수준 4단계
| 수준 | Dirty | Non-repeatable | Phantom | 특성 |
|---|---:|---:|---:|---|
| Read Uncommitted | 가능 | 가능 | 가능 | 최대 동시성, 최소 격리 |
| Read Committed | 방지 | 가능 | 가능 | 문장 단위 커밋값 읽기 |
| Repeatable Read | 방지 | 방지 | 구현별 | 트랜잭션 내 행 재조회 일관 |
| Serializable | 방지 | 방지 | 방지 | 직렬 실행과 동등한 결과 지향 |

## Ⅳ. Lock·MVCC 기반 동작
```text
[Lock] 읽기·쓰기 충돌을 대기·차단 → 2PL → 직렬성
[MVCC] 버전·Snapshot으로 읽기와 쓰기 분리 → 충돌 시 검증·재시도
```
| 방식 | 강점 | 비용 |
|---|---|---|
| Lock | 충돌을 명시적으로 차단 | 대기·Deadlock |
| MVCC | 읽기 동시성 향상 | 버전 정리·쓰기 충돌 |
| SSI/직렬화 검증 | 위험 의존성 탐지 | Abort·재시도 증가 |

## Ⅴ. 격리 수준 선택 기준
| 업무 | 권장 관점 | 보완 |
|---|---|---|
| 단순 조회·콘텐츠 | Read Committed 중심 | 낙관적 버전 검사 |
| 주문·재고 | Repeatable/조건부 잠금 | 원자 UPDATE·재시도 |
| 잔액·한도·결산 | Serializable 우선 검토 | 짧은 트랜잭션·멱등성 |
| 분석 Snapshot | 일관된 Snapshot | 장기 버전·지연 관리 |

## Ⅵ. 운영 고려사항
| 문제 | 원인 | 대책 |
|---|---|---|
| Deadlock | 잠금 순서 불일치 | 잠금 순서 표준·짧은 트랜잭션·재시도 |
| 직렬화 실패 | 높은 충돌률 | 지수 Backoff·멱등 처리 |
| 장기 Snapshot | 버전 정리 지연 | Timeout·Batch 분할 |
| 격리 오해 | 표준명만 보고 제품 차이 무시 | DBMS 공식 문서·재현 시험 |

## Ⅶ. 가장 높은 수준보다 오류비용에 맞는 수준을 고르는 결론
- 격리 수준은 성능 옵션이 아니라 업무 불변조건의 실행 계약
- 핵심 원장에는 강한 격리와 원자 연산을, 일반 조회에는 낮은 격리와 충돌 검증을 조합

## 1교시 10점 답안 발췌
```text
RU → RC → RR → Serializable
Dirty 차단 → Non-repeatable 차단 → Phantom·직렬화 이상 차단
구현: Lock 또는 MVCC + 충돌 검증·재시도
```

## 출제 이력과 검증 출처
- 제134회 공식 문제지: 격리 수준 4가지의 사례 관련 출제
- 제137회 공식 문제지: 격리 수준과 이상현상 관련 출제
- [PostgreSQL Documentation, Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [Q-Net 기술사 자료실](https://www.q-net.or.kr/man001.do?gSite=Q)

## 학습 체크
- [ ] 격리 수준 4단계를 순서대로 씀
- [ ] Dirty·Non-repeatable·Phantom을 구분함
- [ ] Lock과 MVCC의 차이를 설명함
- [ ] DBMS별 보장 차이와 재시도를 언급함

## 연결 토픽
- [동시성 제어](./009_concurrency_control/) · [정규화](./019_normalization/) · [무결성 제약](./013_integrity_constraint/)
