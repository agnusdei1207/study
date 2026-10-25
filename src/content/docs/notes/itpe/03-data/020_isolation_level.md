---
title: "트랜잭션 격리 수준"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- 트랜잭션 격리 수준(Isolation Level), ANSI/ISO SQL 표준, 동시성(Concurrency), 일관성(Consistency)
- Dirty Read, Non-Repeatable Read, Phantom Read
- READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE, MVCC(Multi-Version Concurrency Control)

## Ⅰ. 트랜잭션 격리 수준의 개요

- 핵심 요약 : 동시 실행 트랜잭션 사이에서 다른 트랜잭션의 변경을 어디까지 볼 수 있는지 정하는 표준 단계.
- 개념 : 한 트랜잭션의 미확정·확정 변경을 다른 트랜잭션이 어느 강도까지 읽을 수 있는지 정한 기준 (**트랜잭션 격리 수준**, Isolation Level).
- 배경 및 필요성 : ANSI(American National Standards Institute)와 ISO(International Organization for Standardization)의 SQL(Structured Query Language) 표준이 네 단계로 정의. 격리가 강하면 동시 처리량이 줄고 약하면 읽기 이상이 노출되는 상충의 조절 기준이 필요.
- 주요 목적 : 일관성과 동시성 사이의 균형점을 표준 단계로 제시해 업무별 트랜잭션 품질 기준의 확립.

## Ⅱ. 트랜잭션 격리 수준의 특징 및 장점

- 핵심 요약 : 네 단계 표준 체계와 이상 현상의 차등 차단이 업무 맞춤 정합성 설계를 가능하게 하는 제어 기준.

1. 표준 4단계 체계 : READ UNCOMMITTED에서 SERIALIZABLE까지의 단계 정의 → 업무 요구에 맞는 정합성 강도 선택 효과.
2. 트레이드오프 구조 : 수준 상승에 따른 일관성 강화와 락 대기·롤백 증가 → 정합성·성능의 명시적 균형점 제공 효과.
3. 이상 현상의 차등 차단 : **Dirty Read**(미확정 값의 읽기), **Non-Repeatable Read**(같은 행의 반복 읽기 값 불일치), **Phantom Read**(같은 조건 조회에서의 새 행 출현)를 수준별로 차등 허용 → 불필요한 제약 최소화 효과.
4. 다중 버전 병행 : **MVCC**(Multi-Version Concurrency Control)로 과거 버전 스냅샷을 읽게 하여 읽기-쓰기 간섭 감소 → 잠금 없는 읽기 성능 효과.
5. 벤더 구현 차이 : 기본값과 잠금 방식이 DBMS(Database Management System)마다 다름 → 이기종 환경에서의 동작 검증 필요 시사.

## Ⅲ. 트랜잭션 격리 수준의 구조 (흐름)

- 핵심 요약 : 세 가지 읽기 이상 현상과 네 단계 수준의 차단 계층 구조.

```text
[ 3대 읽기 이상 현상 ]

Dirty Read : 커밋 전의 값을 읽는 현상
Non-Repeatable Read : 같은 행의 값이 조회마다 바뀌는 현상
Phantom Read : 같은 조건의 조회에서 새 행이 나타나는 현상
```

```text
[ 격리 수준 계층 (위로 갈수록 강함) ]

SERIALIZABLE : 세 이상 현상 모두 차단
      ↑
REPEATABLE READ : Phantom Read만 허용
      ↑
READ COMMITTED : Dirty Read만 차단
      ↑
READ UNCOMMITTED : 세 이상 현상 모두 허용
```

- 스냅샷 읽기 : MVCC 기반으로 문장 또는 트랜잭션 시작 시점의 버전을 읽어 잠금 없이 일관된 조회를 제공하는 방식.
- 차단 원리 : 수준 상승에 따라 잠금의 유지 범위와 스냅샷의 유지 시점이 길어지며 이상 현상의 차단 범위 확대.

## Ⅳ. 4단계 격리 수준의 비교

- 핵심 요약 : 수준별 허용 이상 현상과 구현 방식이 다른 네 단계의 표준 격리 수준 체계.

| 격리 수준 | Dirty Read | Non-Repeatable Read | Phantom Read | 구현 방식 |
| --- | --- | --- | --- | --- |
| READ UNCOMMITTED | 허용 | 허용 | 허용 | 잠금 없이 최신 값 조회 |
| READ COMMITTED | 차단 | 허용 | 허용 | 커밋된 값만 읽음 (Oracle, PostgreSQL 기본값) |
| REPEATABLE READ | 차단 | 차단 | 허용 | 트랜잭션 스냅샷 유지 (MySQL InnoDB 기본값) |
| SERIALIZABLE | 차단 | 차단 | 차단 | 범위 잠금 등 직렬 실행과 동등한 결과 보장 |

- 선택 기준 : 조회 중심 업무는 READ COMMITTED를 기본값으로 두는 기준.
- 선택 기준 : 잔액·재고 같은 정합성 필수 갱신은 강한 수준과 명시적 잠금을 결합하는 기준.
- 선택 기준 : DBMS 전환 시 기본값과 잠금 동작의 차이를 테스트로 확인하는 기준.

## Ⅴ. 트랜잭션 격리 수준의 한계와 방안

- 핵심 요약 : 동시성·일관성 상충, 강한 수준의 성능 비용, 벤더 차이가 한계이며 업무별 차등 설계로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 동시성·일관성 상충 | 최고 수준의 락 경합 → 처리량 저하, 낮은 수준의 이상 노출 | 도메인별 차등 수준 적용, 낙관적 검증 병행 | 롤백률, 락 대기 시간 |
| 강한 수준의 성능 비용 | SERIALIZABLE의 범위 잠금 → 대기·교착 증가 | 임계 구역 최소화, 필요 행의 명시적 잠금 | 교착 빈도, 응답 시간 |
| 벤더 구현 차이 | 기본값·잠금 방식의 이질성 → 전환 시 동작 변화 | 격리 수준 의존 로직의 추상화, 동시성 통합 테스트 | 동시성 테스트 통과율 |

## Ⅵ. 트랜잭션 격리 수준에 대한 기술사적 제언

- 핵심 요약 : 기본 수준은 처리량 중심으로 두고 정합성 필수 거래에만 강한 통제를 결합하는 설계 원칙.
- 아키텍처 기준 : 데이터베이스 운영 조직이 업무 도메인별 기본 격리 수준을 아키텍처 표준으로 제정.
- 개발 규약 : 개발 조직이 정합성 필수 갱신의 명시적 잠금 사용을 코딩 규약으로 정착.
- 검증 체계 : 품질 조직이 동시성 시나리오 테스트를 릴리스 승인 절차에 편성.

## Ⅶ. 결론

- 핵심 요약 : 격리 수준은 일관성과 동시성의 균형을 정하는 트랜잭션 설계의 표준 기준.
- 시사점 : 표준 단계의 의미와 벤더 차이의 함께 이해가 업무 맞춤 수준 선택의 전제.
