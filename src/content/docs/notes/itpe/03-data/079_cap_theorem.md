---
sidebar:
  order: 79
  label: "079. CAP 이론 (CAP Theorem)"
  badge:
    text: "기출 · 76%"
    variant: note
title: "CAP 이론 (CAP Theorem)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:44:00+09:00"
tags:
  - "notes-data"
weight: 79
extra:
  model: "Gemini 3.8 Flash"
  question_no: "079"
  source_status: "기출"
  source_history: "126회, 93회"
  priority: 76
  priority_note: "[출제(KPC):126] · 이전(KPC):93"
---

## 답안 골격
```text
[CAP 이론] ◀━━ 머리: Ⅶ 내 의견 (네트워크 단절(P) 불가피성 인식 하에 비즈니스 도메인별 CP(금융)와 AP(SNS)의 이원화 채택)
 ┃
 ┣━ Ⅰ 개요 ───── 분산 데이터 시스템에서 일관성(C), 가용성(A), 파티션 허용성(P)의 3대 속성을 동시에 모두 만족하는 것은 불가능하다는 정리
 ┣━ Ⅱ 특징 ───── 브루어(Eric Brewer) 제창 · 네트워크 분할(P) 필수 전제 · 2가지 속성 선택 강제 · PACELC 이론으로의 확장
 ┣━ Ⅲ 구조 ───── 일관성(Consistency, 선형성) / 가용성(Availability, 무조건 응답) / 파티션 허용성(Partition Tolerance, 망 단절 허용)
 ┣━ Ⅳ 흐름 ───── ① 분산 노드 간 네트워크 단절(P) 발생 → ② C 선택 시: 미동기 노드 쓰기 거부(A 포기, CP 시스템) / A 선택 시: 불일치 감수하고 응답(C 포기, AP 시스템)
 ┣━ Ⅴ 비교 ───── CP 시스템 vs AP 시스템 (HBase, Redis Cluster, ZooKeeper vs Cassandra, DynamoDB, CouchDB)
 ┗━ Ⅵ 실무 ───── 정상 상황(P가 아닐 때)의 지연시간(Latency) 트레이드오프 설명 불가 (PACELC 필요)
```
- 필수 키워드: 브루어(Eric Brewer) · 일관성(Consistency) · 가용성(Availability) · 파티션 허용성(Partition Tolerance) · CP 시스템 · AP 시스템 · PACELC
- 배점 전략: 10점 = Ⅰ → Ⅲ 벤다이어그램 도식 → Ⅴ CP vs AP 비교표 / 25점 = Ⅰ~Ⅶ, Ⅳ 네트워크 단절 시나리오 증명 및 PACELC 이론 확장
- 기출: 126회 `분산 데이터베이스 시스템에서 CAP 이론의 개념과 CP, AP 시스템 비교` → Ⅰ 개념 + Ⅲ 3대 요소 + Ⅴ CP/AP 비교 및 대표 NoSQL

## 한 줄 본질
- 분산 노드 간 물리적 네트워크 단절(Partition) 발생의 불가피성 → 최신 데이터 보장을 위해 에러를 낼 것인가(CP), 구버전이라도 응답할 것인가(AP)의 양자택일 강제 → 아키텍처 방향성 확립 / 양자 동시 달성 불가

## 핵심 그림
```text
[CAP 이론의 3대 요소와 네트워크 분할(P) 시의 선택]

              [ 일관성 (Consistency) ]
                    /        \
                   /    CA    \   (CA는 분산 환경에서 불가능!)
                  /  (단일 RDB) \
                 /              \
 [가용성 (Availability)] ─────── [파티션 허용성 (Partition)]
           (AP 시스템)                  (CP 시스템)
        (Cassandra, Dynamo)          (HBase, ZooKeeper)

 * 네트워크 분할(P) 발생 시:
   노드1과 노드2 사이의 통신 케이블이 끊어졌을 때:
   - CP 선택: 노드2에 동기화할 수 없으므로 쓰기 요청에 "Error" 반환 (가용성 포기)
   - AP 선택: 노드1에만 쓰고 "성공" 반환, 노드2는 과거 데이터 응답 (일관성 포기)
```

## 핵심 용어
- 선형 일관성(Linearizability / Consistency): 어떤 노드에 쓰기가 완료된 직후, 분산 시스템 내의 다른 어떤 노드에서 읽더라도 반드시 그 최신 값을 반환해야 하는 성질
- 파티션 허용성(Partition Tolerance): 분산 노드 간에 네트워크 패킷이 유실되거나 통신이 완전히 두절되어도 시스템 전체가 동작을 멈추지 않는 성질

## 핵심 통찰
- "CAP 중 2개를 자유롭게 고를 수 있다"는 것은 가장 흔한 오해임 → 네트워크는 언제든 끊어질 수 있으므로 분산 시스템에서 'P(파티션 허용성)'는 선택이 아닌 '필수 전제'
- 따라서 현실의 선택지는 오직 'CP(일관성)'냐 'AP(가용성)'냐 둘 중 하나임
- CAP 이론의 맹점: 네트워크 장애(P)는 1년 중 0.1%에 불과함 → 네트워크가 정상인 99.9%의 평상시에는 일관성과 지연시간(Latency) 사이에 어떤 절충을 할 것인가를 설명하지 못해 'PACELC 이론'으로 진화함

## 딸려 나오는 하위 토픽
| 하위 토픽 | 상위 구조 속 위치 | 한 줄 |
|---|---|---|
| PACELC 이론 | CAP의 정상 상태 확장 | 분산 환경에서 Partition(P) 시 A or C, Else(E, 정상 시)에는 Latency(L) or Consistency(C)를 절충 |
| 결과적 일관성(Eventual Consistency) | AP 시스템의 타협점 | 쓰기 즉시는 불일치하더라도 네트워크가 복구되면 일정 시간 후 모든 노드가 결국 일치 상태에 도달 |

## 이웃 토픽과 구분
- CAP의 C vs ACID의 C: CAP의 C = 여러 노드 간의 데이터 복제 시점 일치성(Single-copy consistency) / ACID의 C = 트랜잭션 전후에 비즈니스 규칙 및 무결성 제약이 깨지지 않는 상태

## 문제·원인·대책
- 적용 상황: 글로벌 분산 클라우드 데이터 스토어 설계
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 대륙 간 해저 케이블 지연 시 결제 시스템이 멈추거나 중복 결제 발생 | 결제 시스템에 무분별한 AP 분산 스토어 적용 | 결제·계좌는 강력한 CP(Spanner/Raft) 스토어로 분리 구축 | 금융 데이터 정합성 100% 보장 |
| 소셜 미디어 피드 조회 시 네트워크 순시 단절로 전면 에러 화면 출력 | 피드 타임라인에 불필요한 엄격한 CP 제약 적용 | 피드 조회를 AP 기반 결과적 일관성(Cassandra)으로 전환 | 네트워크 장애 시에도 무중단 서비스 제공 |

## 이렇게 출제된다
- 제126회: "분산 시스템의 CAP 이론의 개념, 3대 요소의 의미, 그리고 네트워크 분할 상황에서 CP 시스템과 AP 시스템의 동작 차이 및 대표 솔루션을 비교하시오." → 요구 포인트: Ⅰ 개념 + Ⅲ C, A, P 정의 + Ⅳ 망 분할 시나리오 + Ⅴ CP(HBase) vs AP(Cassandra) 비교표

## 내 의견
- [단일 시스템 내 CAP 혼합 적용] 서비스 전체를 통째로 CP나 AP로 규정하는 이분법 탈피 필요 → 나라면: 하나의 전자상거래 플랫폼 내에서도 회원 인증과 결제는 CP(PostgreSQL/Raft)로 격리하고, 상품 리뷰와 장바구니, 최근 본 상품은 AP(DynamoDB)로 분리하는 도메인별 폴리글랏(Polyglot) 아키텍처 수립

## 찾아볼 것
- Daniel Abadi가 제창한 PACELC 이론과 MongoDB, Cassandra의 PACELC 매핑 분류
