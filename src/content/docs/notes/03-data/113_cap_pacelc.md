---
sidebar:
  order: 113
  label: "113. CAP·PACELC"
  badge:
    text: "기출 · 70%"
    variant: note
title: "CAP·PACELC"
author: "Gemini 3.8 Flash"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-data"
weight: 113
extra:
  model: "Gemini 3.8 Flash"
  question_no: "113"
  source_status: "기출"
  source_history: "126회"
  priority: 70
  priority_note: "[출제(KPC):126]"
---

## 답안 골격
```text
[CAP · PACELC] ◀━━ 머리: Ⅶ 내 의견 (장애 시 CP/AP 선택과 평시 분산 복제 시 PC/EC 지연시간 트레이드오프 설계)
 ┃
 ┣━ Ⅰ 개요 ───── 분산 데이터베이스에서 일관성(C), 가용성(A), 네트워크 단절(P) 간의 불가피한 상충과 평시 지연시간(L)까지 확장한 이론적 프레임워크
 ┣━ Ⅱ 특징 ───── 분산 시스템 3대 속성 중 동시 2개만 선택 가능(CAP) · 장애(P) 시와 정상(E) 시의 선택 분리(PACELC) · NoSQL 아키텍처 선정의 절대 기준
 ┣━ Ⅲ 구조 ───── CAP: Consistency, Availability, Partition Tolerance / PACELC: if Partition (A or C) Else (Latency or Consistency)
 ┣━ Ⅳ 흐름 ───── ① 네트워크 단절(P) 발생 여부 감지 → ② 분절 시: 응답 거부(CP) or 비일관 응답(AP) 선택 → ③ 정상 복구 시: 동기 복제(PC/EC) or 비동기 복제(PA/EL) 작동
 ┣━ Ⅴ 비교 ───── CAP vs PACELC / CP(HBase) vs AP(Cassandra) vs PC/EC(RDBMS) vs PA/EL(DynamoDB)
 ┗━ Ⅵ 실무 ───── 네트워크 지연을 CAP의 P로 오판하여 불필요한 시스템 중단 / 금융 트랜잭션에 AP 시스템을 도입해 마이너스 잔고 사고
```
- 필수 키워드: CAP 정리 · PACELC · 일관성(Consistency) · 가용성(Availability) · 네트워크 분절(Partition) · 지연시간(Latency) · 최종 일관성(Eventual Consistency)
- 배점 전략: 10점 = Ⅰ → Ⅲ CAP 벤다이어그램 및 PACELC 매트릭스 도식 → Ⅴ 대표 분산 DB 매핑 비교 / 25점 = Ⅰ~Ⅶ, Ⅳ 분할/평시 상태 전이 메커니즘 및 Ⅵ 업무 요건별 아키텍처 선택 가이드
- 기출: 126회 `분산 데이터베이스 환경에서의 CAP 이론과 PACELC 이론을 비교하고, NoSQL 데이터베이스 선정 기준을 제시하시오.` → Ⅰ 정의 + Ⅲ CAP/PACELC 상세 구조 + Ⅴ 비교표 + Ⅵ 시스템 선정 기준

## 한 줄 본질
- 물리적 분산 환경에서 네트워크 단절(P)은 불가피함 → 분할 발생 시 C와 A 중 하나를 포기하고, 평상시에도 일관성(C) 유지를 위해 지연(L)을 감수할지 선택 → 시스템 목적에 부합하는 분산 아키텍처 확립 / 만능 분산 시스템은 존재 불가

## 핵심 그림
```text
[CAP 이론의 한계와 PACELC 확장 프레임워크 매핑]

  [1. CAP 정리의 현실]                     [2. PACELC 확장 매트릭스]
      분산 환경에서 P는 필수 선택!            장애 시와 정상 시의 트레이드오프를 2단계로 분리

          Consistency                             If Partition (장애 시)
             /   \                               ┌────────────────────────────────┐
            /     \                              │  PC (Consistency) : 일관성 보장│
      CA(불가)     \                             │  PA (Availability): 가용성 보장│
          /         \                            └────────────────┬───────────────┘
         /     P     \                                            │ Else (정상 시)
  Availability ────── Partition Tolerance        ┌────────────────▼───────────────┐
      (AP)              (CP)                     │  EC (Consistency) : 지연 감수  │
                                                 │  EL (Latency)     : 빠른 응답  │
                                                 └────────────────────────────────┘
```

## 핵심 용어
- 분할 허용(Partition Tolerance): 노드 간 통신 패킷이 유실되거나 지연되어 네트워크가 둘 이상으로 쪼개져도 시스템 전체가 동작을 유지하는 성질
- 최종 일관성(Eventual Consistency): 새로운 갱신이 발생하지 않는 한, 일정 시간이 흐른 뒤 모든 분산 복제본의 데이터가 결국 동일해지는 약한 일관성 모델

## 핵심 통찰
- 현실의 분산 네트워크에서 패킷 유실과 스위치 단절은 필연적이므로 'P'는 선택 사항이 아닌 필수 전제임 → 따라서 실질적인 선택지는 오직 'CP'냐 'AP'냐의 양자택일임
- CAP 정리는 '네트워크 분할(P)이 일어났을 때'만 설명한다는 치명적 결함이 있음 → 실제 시스템은 99.9% 정상 상태(E)로 운영되는데, 평상시 성능을 좌우하는 지연시간(Latency)을 다루기 위해 PACELC 이론이 탄생
- 결제·계좌 이체는 지연이 발생하더라도 일관성을 지켜야 하므로 PC/EC(또는 CP), SNS 좋아요나 실시간 로그 수집은 데이터가 살짝 틀려도 즉시 응답해야 하므로 PA/EL을 채택

## 이웃 토픽과 구분
- CAP vs ACID의 C: CAP의 C(Consistency) = 분산된 모든 노드에서 '동일한 시점에 항상 최신 데이터를 읽을 수 있는가'(단일 시스템 이미지, Linearizability) / ACID의 C = 트랜잭션 전후로 '정의된 무결성 제약조건을 만족하는가'

## 문제·원인·대책
- 적용 상황: 글로벌 다중 리전(Multi-Region) 쇼핑몰 주문 및 재고 시스템 구축
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 태평양 해저 케이블 단절 시 해외 지사 노드의 상품 구매가 전면 마비 | 순수 CP 시스템(MongoDB 강력한 읽기) 구성으로 분할 시 가용성 포기 | 주문 접수는 AP(Eventual Consistency)로 분리하고 사후 보상 트랜잭션(Saga) 적용 | 무중단 주문 접수 가용성 99.999% 확보 |
| 정상 상태에서 미국-한국 간 동기 복제로 인해 API 응답 시간이 500ms로 급증 | 평시 일관성(EC)을 강제하여 네트워크 RTT 지연이 그대로 클라이언트에 전달 | 정상 시 빠른 응답을 주는 EL(비동기 복제)로 전환하고 쿼럼(Quorum) $W+R > N$ 조율 | 응답 지연 500ms에서 30ms로 단축 |

## 이렇게 출제된다
- 제126회: "분산 데이터베이스 시스템의 핵심 이론인 CAP 이론과 PACELC 이론의 개념을 설명하고, 두 이론의 관계 및 NoSQL 데이터베이스 선정 시 고려사항을 서술하시오." → 요구 포인트: CAP 3대 속성 + PACELC 4개 분기 구조 + CAP의 한계점과 PACELC의 보완점 + DB 제품별(HBase, Cassandra, MongoDB) 매핑

## 내 의견
- [기계적 CP/AP 이분법 설계 지양] 개발팀이 DB 제품을 선정할 때 카산드라는 무조건 AP, 몽고DB는 무조건 CP라고 단정 짓고 시스템 전체를 획일적으로 설계하는 오류 빈발 → 나라면: NoSQL의 튜너블 일관성(Tunable Consistency) 파라미터(Read/Write Quorum)를 활용하여, 동일 DB 클러스터 내에서도 금융 결제 컬럼은 $W=ALL, R=QUORUM$으로 CP 모드로 돌리고, 조회 로그는 $W=1, R=ONE$으로 AP 모드로 분리 운영하는 하이브리드 아키텍처 수립

## 찾아볼 것
- 분산 시스템의 쿼럼 복제 모델에서 강력한 일관성을 보장하기 위한 부등식($W + R > N$)과 슬로피 쿼럼(Sloppy Quorum)
