---
sidebar:
  order: 20
  label: "020. 트랜잭션 격리 수준 (Isolation Level)"
  badge:
    text: "기출 · 91%"
    variant: note
title: "트랜잭션 격리 수준 (Isolation Level)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-data"
weight: 20
extra:
  model: "Gemini 3.8 Flash"
  question_no: "020"
  source_status: "기출"
  source_history: "137회, 134회, 119회"
  priority: 91
  priority_note: "[출제:134,137] · 이전(KPC):119"
---

## 답안 골격
```text
[트랜잭션 격리 수준] ◀━━ 머리: Ⅶ 내 의견 (요구 수준 명시 → 동시성 테스트로 검증)
 ┃
 ┣━ Ⅰ 개요 ───── 완전 직렬 실행 = 대기 비용 → 수준별로 일관성과 동시성 절충
 ┣━ Ⅱ 특징 ───── 수준↑ = 이상현상↓ · 동시성↓
 ┣━ Ⅲ 구조 ───── Read Uncommitted / Read Committed / Repeatable Read / Serializable
 ┣━ Ⅳ 흐름 ───── ① 트랜잭션 시작 → ② 락·스냅샷으로 읽기 → ③ 커밋·롤백
 ┣━ Ⅴ 비교 ───── 수준 × Dirty Read · Non-Repeatable Read · Phantom Read
 ┗━ Ⅵ 실무 ───── Lost Update / 처리량 저하 / 기본 수준 차이
```
- 필수 키워드: 격리성(ACID) · Dirty Read · Non-Repeatable Read · Phantom Read · 락 · MVCC
- 배점 전략: 10점 = Ⅰ → Ⅴ 표 → Ⅵ 한 행 / 25점 = Ⅰ~Ⅶ, 앞 1/3에 Ⅴ 표
- 기출: 137회 `가. 격리 수준 4가지` → Ⅲ, `나. 이상현상` → Ⅴ / 134회 `사례 중심` → Ⅵ 사례

## 한 줄 본질
- 트랜잭션을 모두 직렬로 돌리면 대기 비용이 큼 → 읽기 격리 강도를 4단계로 나눠 허용할 이상현상을 선택 → 동시성 확보 / 낮은 수준일수록 데이터 이상 위험

## 핵심 그림
```text
수준               Dirty Read   Non-Repeatable Read   Phantom Read
Read Uncommitted   발생         발생                  발생
Read Committed     방지         발생                  발생
Repeatable Read    방지         방지                  발생
Serializable       방지         방지                  방지
```

## 핵심 용어
- MVCC: 읽기가 쓰기를 기다리지 않게 하는 장치. 대가는 옛 버전 보관 공간과 정리 비용
- Lost Update: 표준 세 이상현상 밖에서 실무에 가장 자주 터지는 문제. 두 트랜잭션이 같은 값을 읽고 각자 덮어씀

## 핵심 통찰
- 격리 수준 = 일관성과 동시성의 교환 비율 → 수준을 올릴수록 락 대기·직렬화 실패 재시도가 늘어 처리량 감소
- 같은 수준 이름이라도 락 방식이냐 스냅샷 방식이냐에 따라 막는 이상현상이 달라짐 → DBMS를 바꾸면 동작이 바뀔 수 있음
- 대부분의 업무는 Read Committed로 충분 → 재고·잔액처럼 읽고 갱신하는 구간만 명시적 락이나 높은 수준으로 좁혀 적용

## 이웃 토픽과 구분
- 격리 수준 vs 동시성 제어 기법: 격리 수준 = 무엇을 허용할지(요구) / 락·MVCC·타임스탬프 = 어떻게 막을지(구현)

## 문제·원인·대책
- 적용 상황: 주문 폭주 시 재고 차감
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 재고가 실제보다 적게 차감 | 두 트랜잭션이 같은 재고를 읽고 각자 갱신(Lost Update) | 갱신 대상 행 명시적 락 또는 버전 컬럼 낙관적 락 | 나중 갱신이 앞 갱신을 덮지 않음 |
| 전체 Serializable 적용 후 처리량 저하 | 범위 락과 직렬화 실패 재시도 증가 | 필요한 트랜잭션만 수준 상향 | 나머지 트랜잭션의 동시성 유지 |

## 이렇게 출제된다
- 제134회 2교시 6번: "트랜잭션 격리 수준(Transaction Isolation Level) 4가지를 사례 중심으로 설명하시오." → 요구 포인트: Ⅲ 네 수준 + Ⅵ 사례
- 제137회 3교시 4번: "데이터베이스 트랜잭션 격리 수준(Transaction Isolation Level)과 관련하여 아래 사항을 설명하시오. 가. 데이터베이스 트랜잭션 격리 수준 4가지 나. 데이터베이스 트랜잭션 격리 수준에 따라 발생할 수 있는 이상현상" → 요구 포인트: Ⅲ + Ⅴ 표

## 내 의견
- [기본값에 맡긴 격리 수준] ORM·DBMS 기본값 차이로 Lost Update가 운영에서야 드러남 → 나라면: 서비스별 요구 수준을 설계 문서에 명시하고, 두 세션으로 재현하는 동시성 테스트를 배포 파이프라인에 넣어 이상현상 여부를 먼저 확인

## 찾아볼 것
- 스냅샷 격리(Snapshot Isolation)에서 발생하는 쓰기 왜곡(Write Skew)과 대응
