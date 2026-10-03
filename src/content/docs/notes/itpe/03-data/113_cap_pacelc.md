---
title: "CAP·PACELC 정리"
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

## Ⅰ. 분산 데이터 시스템의 한계를 규정한 이론적 초석 개요

### 가. CAP 정리(CAP Theorem)의 정의
- 에릭 브루어(Eric Brewer) 교수가 제안하고 세스 길버트와 낸시 린치가 수학적으로 증명한 정리.
- 분산 데이터 시스템은 **일관성** (Consistency), **가용성** (Availability), **분할 내구성** (Partition Tolerance)의 3가지 특성을 모두 동시에 만족하는 것은 불가능하며, 반드시 2가지만을 선택 할 수밖에 없다는 이론.

### 나. PACELC 정리로의 확장 배경
- CAP 정리는 오직 '**네트워크 분할** (Partition) 장애' 상황만을 다루며, 시스템이 정상적인 평상시(Else) 상태일 때 직면하는 **지연 시간** (Latency)과 일관성(Consistency) 간의 본질적 트레이드오프 를 설명하지 못하는 한계가 있어 다니엘 아바디(Daniel Abadi) 교수가 **PACELC** 로 확장함.

---

## Ⅱ. CAP 정리의 3대 속성 및 선택 분류

```text
[ CAP 정리 트라이앵글 ]
                  Consistency (강한 일관성)
                         / \
                        /   \
                       /  CP \
                 CA  /       \
                    /         \
                   /    AP     \
  Availability ---+-------------+--- Partition Tolerance
 (고가용성)                           (분할 내구성)
```

| 속성 | 정의 | 네트워크 분할(P) 발생 시의 선택 트레이드오프 |
| :--- | :--- | :--- |
| **Consistency (C)** | 모든 노드는 어느 노드로 접근하든 항상 최신의 동일한 데이터를 읽어야 함 (단일 시스템처럼 동작) | CP 시스템 선택 : 노드 간 데이터 동기화가 불가능하면, 일관성을 지키기 위해 차라리 읽기/쓰기 요청을 거부(에러 반환) 함 |
| **Availability (A)** | 일부 노드에 장애가 발생하더라도 정상 노드는 반드시 모든 요청에 대해 성공 응답을 반환해야 함 | AP 시스템 선택 : 노드 간 데이터가 일치하지 않더라도, 시스템 가동을 위해 약간 오래된 데이터라도 일단 응답 함 |
| **Partition Tolerance (P)** | 노드 간 네트워크 패킷 손실이나 단절이 발생하더라도 시스템 전체 동작이 유지되어야 함 | 물리적 분산 환경에서 네트워크 단절(P)은 피할 수 없는 현실이므로, 실질적 선택지는 CP vs AP 임 |

---

## Ⅲ. PACELC 정리의 분석 프레임워크

### 가. PACELC의 정의 수식
$$\mathbf{P} \text{ (Partition)} \rightarrow [\; \mathbf{A} \text{ (Availability)} \; \mathbf{vs} \; \mathbf{C} \text{ (Consistency)} \;] \quad \mathbf{E} \text{ (Else)} \rightarrow [\; \mathbf{L} \text{ (Latency)} \; \mathbf{vs} \; \mathbf{C} \text{ (Consistency)} \;]$$

```text
[ PACELC 의사결정 트리 ]
네트워크 분할 장애가 발생했는가? (Partition)
   |-- YES : 가용성(A)을 택할 것인가, 일관성(C)을 택할 것인가?
   +-- NO (Else 평상시) : 지연 시간(L)을 단축할 것인가, 일관성(C)을 보장할 것인가?
```

### 나. 대표 분산 데이터베이스의 PACELC 분류 매트릭스

| 분류 | 대표 DBMS | 평상시 동작 (Else) | 분할 시 동작 (Partition) | 적합한 업무 도메인 |
| :--- | :--- | :--- | :--- | :--- |
| **PC / EC** | **Google Spanner, CockroachDB** | 완벽한 동기 복제로 일관성 보장 (L 희생) | 분할 발생 시 정합성 위해 가용성 차단 (A 희생) | 금융 거래, 원장 관리, 글로벌 결제 정산 |
| **PA / EL** | **Amazon DynamoDB, Apache Cassandra** | 비동기 복제로 극도의 초저지연 읽기/쓰기 (C 희생) | 분할 발생 시에도 모든 노드가 계속 서비스 (C 희생) | 소셜 미디어 피드, 장바구니, IoT 실시간 로그 |
| **PC / EC** (HBase), **PA / EC** (MongoDB) | HBase, MongoDB (기본 설정) | 강한 일관성 우선 | 프라이머리 선출 전까지 쓰기 차단 | 실시간 통계 분석, 마스터 기준 데이터 |

---

## Ⅳ. CAP·PACELC 정리 적용 시 주요 한계점 및 해결 방안

- 평상시(Else)의 지연시간(Latency)과 일관성 트레이드오프 간과 :
  - 한계점 : 전통적 CAP 정리에 매몰되어 네트워크 분할이 없는 평상시 정상 가동 상태에서 동기식 복제로 인한 지연시간(Latency) 증가 문제를 설계 시 간과.
  - 해결 방안 : PACELC 정리를 기준으로 시스템을 평가(예: MongoDB의 PA/EC, Cassandra의 PA/EL), 읽기/쓰기별 **동적 일관성 레벨** (Tunable Consistency: QUORUM, LOCAL_QUORUM) 설정.
- **최종 일관성** (Eventual Consistency) 채택 시 비즈니스 정합성 훼손 :
  - 한계점 : 고가용성(AP)을 위해 최종 일관성을 수용할 경우, 사용자가 자신의 쓰기를 즉시 읽지 못하는 일관성 위반(Read-Your-Writes 불만족) 및 금융 잔액 왜곡 발생.
  - 해결 방안 : **세션 일관성** (Session Consistency), **단조 읽기** (Monotonic Read), **인과적 일관성** (Causal Consistency) 등 클라이언트 관점의 보장 메커니즘을 서비스 성격에 맞게 선택적 적용.
- 정적 **CAP** 분류의 한계와 비즈니스 도메인별 세분화 부재 :
  - 한계점 : 전체 데이터베이스를 획일적으로 CP 또는 AP 시스템으로 규정하여 결제, 조회, 로깅 등 도메인별 상이한 요구사항을 유연하게 수용 실패.
  - 해결 방안 : **폴리그랏 퍼시스턴스** (Polyglot Persistence) 아키텍처 도입, **CQRS** (명령-조회 책임 분리)를 적용하여 쓰기는 CP(RDBMS), 조회는 AP(NoSQL/Search)로 이원화.

## Ⅴ. 분산 시스템 아키텍처 설계를 위한 실무 제언

- 단일 분류의 맹신 탈피 (조절 가능한 일관성 활용) : Cassandra나 DynamoDB 등 현대 분산 DB는 고정된 AP/CP가 아니며, 클라이언트가 질의 시점에 읽기/쓰기 **쿼럼** ($W+R > N$)을 설정하여 튜닝 가능한 일관성(Tunable Consistency)을 제공하므로 업무 중요도별로 일관성 수준을 동적 제어해야 함.
- 분산 원장의 최종 일관성(CRDT) 도입 : AP 시스템에서 네트워크 분할 복구 후 서로 다르게 갱신된 노드 간 데이터 충돌을 사람의 개입 없이 수학적으로 자동 병합하기 위해, **충돌 없는 복제 데이터 타입** (CRDT, Conflict-free Replicated Data Type)을 적극 검토할 것을 제언함.
