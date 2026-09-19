---
sidebar:
  order: 1
  label: "001. NoSQL"
  badge:
    text: "기출 · 100%"
    variant: note
title: "NoSQL"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-data"
weight: 1
extra:
  question_no: "001"
  source_status: "기출"
  source_history: "133회, 128회, 124회, 117회, 114회, 93회"
  priority: 100
  priority_note: "[출제:133] · [출제(KPC):124,128] · 이전(KPC):93,114,117"
---

## 답안 골격
```text
[NoSQL] ◀━━ 머리: Ⅶ 내 의견 (단일 저장소 탈피 → Polyglot Persistence 및 읽기 전용 뷰 분리)
 ┃
 ┣━ Ⅰ 개요 ───── RDBMS의 정규화·ACID 스케일업 한계 → 비정형 대용량 분산 확장을 위한 BASE 모델
 ┣━ Ⅱ 특징 ───── Schema-less · 수평 확장성(Scale-out) · 최종 일관성(Eventual Consistency)
 ┣━ Ⅲ 구조 ───── Key-Value / Document / Column-family / Graph 데이터 모델
 ┣━ Ⅳ 흐름 ───── ① 도메인 분석 → ② 쿼리 관점 데이터 모델링 → ③ 테이블 설계 → ④ 튜닝
 ┣━ Ⅴ 비교 ───── RDBMS vs NoSQL (정규화·ACID vs 비정규화·BASE)
 ┗━ Ⅵ 실무 ───── 샤드 불균형 / 데이터 중복 갱신 이상 / 최종 일관성 지연
```
- 필수 키워드: BASE · CAP 이론 · Key-Value · Document · Column-family · Eventual Consistency
- 배점 전략: 10점 = Ⅰ → Ⅲ 4대 유형 도식 → Ⅵ 한 행 / 25점 = Ⅰ~Ⅶ, 앞 1/3에 Ⅲ 4대 유형 도식 및 Ⅳ 모델링 절차
- 기출: 133회 `NoSQL 유형과 모델링 절차` → Ⅲ 유형 + Ⅳ 모델링 절차 / 128회 `NoSQL의 3가지 구조` → Ⅲ 구조

## 한 줄 본질
- RDBMS의 고정 스키마와 조인 연산 병목 → 스키마 제약을 해제하고 조회 패턴에 맞춰 데이터를 중복 저장 → 수평 확장성과 초고속 I/O 확보 / 트랜잭션 무결성과 즉시 일관성 양보

## 핵심 그림
```text
[Key-Value]         [Document]          [Column-Family]     [Graph]
+-------+-------+   +----------------+  +----------------+  (A)--[Rel]--> (B)
| Key   | Value |   | ID: "001"      |  | Row: "user01"  |      \        /
+-------+-------+   | { name: "kim", |  |  cf1: age=20   |       [Edge]
| "k1"  | "val" |   |   tags: [...] }|  |  cf2: role=mgr |        v
+-------+-------+   +----------------+  +----------------+       (C)
  Redis, DynamoDB     MongoDB, CouchDB    Cassandra, HBase    Neo4j, OrientDB
```

## 핵심 용어
- BASE: 완벽한 즉시 일관성 대신 가용성과 유연한 상태 전이를 허용해 대규모 확장을 가능하게 하는 상태 모델
- Polyglot Persistence: 업무 특성에 따라 RDBMS(결제), Document(상품 카탈로그), Cache(세션)를 혼용해 배치하는 저장소 구조

## 핵심 통찰
- NoSQL의 모델링은 데이터 중심이 아니라 쿼리 중심 → RDBMS는 정규화 후 다양한 질의를 SQL로 해결하지만, NoSQL은 자주 던지는 조회 형태대로 테이블을 역정규화해 구성
- 수평 확장은 공짜가 아님 → 샤드 키(Partition Key) 설계가 잘못되면 특정 노드로 트래픽이 몰리는 핫스팟(Hotspot)이 발생해 단일 노드 장애로 전파
- 최종 일관성은 '지금 읽으면 옛날 값일 수 있음'을 내포 → 계좌 이체나 재고 관리처럼 즉각 정합성이 필수적인 코어 업무에는 단독 적용 부적합

## 딸려 나오는 하위 토픽
| 하위 토픽 | 상위 구조 속 위치 | 한 줄 |
|---|---|---|
| CAP 이론 | 분산 데이터 저장소 기본 법칙 | 네트워크 분할 발생 시 일관성(C)과 가용성(A) 중 하나를 택해야 함 |
| PACELC | CAP의 정상 상태 확장 이론 | 분탈(P) 시 A-C 절충, 평상시(E) 지연시간(L)과 일관성(C) 절충 |

## 이웃 토픽과 구분
- NoSQL vs NewSQL: NoSQL = 트랜잭션을 포기하고 확장성 극대화 / NewSQL = 분산 아키텍처 위에서 분산 합의(Raft, Paxos)로 완벽한 ACID 보장

## 문제·원인·대책
- 적용 상황: 대규모 이커머스 트래픽 환경의 주문 및 장바구니 시스템
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 특정 샤드에 읽기/쓰기 집중 및 지연 급증 | 타임스탬프 등 순차 증가 키를 샤드 키로 설정 | 해시 기반 복합 샤드 키(Salt 추가) 적용 | 노드 간 데이터 및 요청 균등 분산 |
| 동일 데이터의 중복 저장으로 인한 정합성 왜곡 | 쓰기 성능을 위한 과도한 비정규화 | 이벤트 기반 비동기 CDC(Kafka/Debezium) 연동 동기화 | 백그라운드에서 최종 일관성 시간 단축 |

## 이렇게 출제된다
- 제133회 1교시 3번: "NoSQL유형과 모델링 절차를 설명하시오." → 요구 포인트: Ⅲ 4대 유형 도식 + Ⅳ 모델링 4단계 흐름
- 제128회 1교시 6번: "NoSQL의 3 가지 구조" → 요구 포인트: Ⅲ Key-Value, Document, Column-Family 구조 및 특징

## 내 의견
- [무분별한 NoSQL 만능주의 탈피] NoSQL을 트렌드로 도입했다가 조인 불가·데이터 왜곡으로 서비스 신뢰성이 붕괴되는 현상 다수 목격 → 나라면: 금융·회계 트랜잭션은 PostgreSQL 등 RDBMS로 엄격히 통제하고, 대용량 로그 수집·조회 화면은 MongoDB/Cassandra로 분리하는 CQRS 패턴 및 Polyglot Persistence 설계를 표준 아키텍처로 채택

## 찾아볼 것
- DynamoDB의 Global Secondary Index(GSI) 비동기 복제 지연에 따른 정합성 모델
