---
title: "NoSQL(Not Only SQL)"
author: "agnusdei1207"
date: "2026-10-25T00:09:14+09:00"
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

- NoSQL(Not Only SQL), RDBMS, CAP 정리, BASE, Scale-Out, 샤딩(Sharding), 복제(Replication)
- Key-Value, Document, Column-Family, Graph, Quorum, Polyglot Persistence, Saga 패턴, CQRS

## Ⅰ. NoSQL의 개요

- 핵심 요약 : 고정 스키마와 수직 확장의 한계를 넘어 수평 확장과 유연한 데이터 구조를 제공하는 비관계형 분산 저장소.
- 개념 : 관계형 데이터베이스 관리 시스템(RDBMS, Relational Database Management System)의 엄격한 ACID 트랜잭션과 고정 스키마 대신, 수평 확장(Scale-Out)과 고성능 읽기·쓰기를 우선하는 비관계형 분산 데이터 저장소인 **NoSQL** (Not Only SQL).
- 배경 및 필요성 : 웹 규모의 트래픽과 대량 동시 접속을 단일 대형 서버로 감당하기 어려워졌고, 비정형·반정형 데이터가 늘어 스키마를 자주 바꿔야 하는 요구가 커짐.
- 주요 목적 : **CAP 정리** (CAP theorem, 분산 시스템에서 일관성·가용성·분할 내성을 동시에 완전히 보장할 수 없다는 이론)를 전제로 한 **BASE** (Basically Available, Soft-state, Eventual consistency) 특성을 채택해 가용성과 처리량을 확보하는 것.

## Ⅱ. NoSQL의 특징 및 장점

- 핵심 요약 : 조인 배제, 데이터 중복 허용, 수평 분산, 최종 일관성 중심의 설계 전환이 대량 처리와 확장성으로 이어짐.

1. 정규화 완화 : 조회 시 비용이 큰 조인(JOIN)을 피하고 데이터 중복을 허용 → 단일 키 조회의 처리량 향상.
2. **수평 분산** (Scale-Out, 노드를 추가해 처리 용량을 늘리는 방식) : **샤딩** (Sharding, 데이터를 여러 노드에 나누어 저장하는 방식)과 **복제** (Replication, 같은 데이터를 여러 노드에 복사하는 방식) 기반의 범용 노드 클러스터 → 저비용 확장.
3. 스키마 유연성 : 스키마를 데이터베이스가 강제하지 않고 애플리케이션이 구조를 정함 → 변경 요구에 빠르게 대응.
4. BASE 특성 : 가용성을 우선하고 노드 간 데이터는 시간이 지나며 일치하는 최종 일관성을 수용 → 장애 시에도 서비스 지속.
5. 4대 데이터 모델 : **Key-Value**, **Document**, **Column-Family**, **Graph** 저장소로 용도별 특화.

## Ⅲ. NoSQL의 구조 (흐름)

- 핵심 요약 : 4대 데이터 모델이 용도별로 나뉘고, 복제본 응답 조건으로 정합성을 조절하는 구조.
- **Quorum** (복제본 중 쓰기·읽기 응답 수를 정해 정합성을 조절하는 방식) : 아래 도해의 N, W, R 조건으로 일관성 수준을 결정.

```text
[ NoSQL 4대 데이터 모델 ]
 - Key-Value : Redis, DynamoDB
 - Document : MongoDB, Couchbase
 - Column-Family : Cassandra, HBase
 - Graph : Neo4j, JanusGraph
```

```text
[ 복제본 정합성 : Quorum 모델 ]
 N : 전체 복제본 수
 W : 쓰기 성공으로 인정하는 응답 수
 R : 읽기 성공으로 인정하는 응답 수
      ↓
 W + R > N 이면 강한 일관성 보장
```

| 분류 | 데이터 구조와 특성 | 질의·인덱싱 방식 | 주요 적용 분야 | 대표 솔루션 |
| --- | --- | --- | --- | --- |
| Key-Value | 고유 키에 값을 매핑 | 키 기반 빠른 조회, 범위 질의는 제한적 | 캐싱, 세션 저장 | Redis, Amazon DynamoDB |
| Document | JSON(JavaScript Object Notation), BSON(Binary JSON) 등 계층 문서 단위 저장 | 문서 내부 필드에 보조 인덱스 지원 | 콘텐츠 관리, 상품 카탈로그 | MongoDB, Couchbase |
| Column-Family | 행 키별로 가변적인 컬럼 집합을 관리 | LSM-Tree(Log-Structured Merge-Tree) 기반 대량 쓰기 최적화 | 센서 시계열, 대규모 로그 | Apache Cassandra, HBase |
| Graph | 노드, 간선, 속성으로 관계를 표현 | 인접 노드 포인터 탐색 | 추천 시스템, 사기 탐지 | Neo4j, JanusGraph |

- BASE의 세 요소 :
  1. Basically Available : 일부 노드 장애에도 전체 가용성을 유지하고 장애가 전체로 번지지 않도록 격리.
  2. Soft-state : 외부 입력이 없어도 백그라운드 동기화로 상태가 계속 갱신됨.
  3. Eventual consistency : 새 갱신이 멈추면 시간이 지나 노드 간 데이터가 일치하는 상태로 수렴.

## Ⅳ. NoSQL과 RDBMS의 비교

- 핵심 요약 : ACID, Scale-Up, SQL 중심의 RDBMS와 BASE, Scale-Out, API 중심의 NoSQL을 워크로드 특성에 따라 선택.

| 비교 항목 | RDBMS | NoSQL |
| --- | --- | --- |
| 데이터 스키마 | 고정 스키마와 엄격한 DDL(Data Definition Language) | 유연한 구조, 스키마 강제 없음 |
| 트랜잭션 보장 | 원자성, 일관성, 격리성, 영속성의 ACID | BASE, 가용성 중심의 트레이드오프 |
| 확장 방식 | 수직 확장(Scale-Up) | 수평 확장(Scale-Out), 비공유(Shared-Nothing) 클러스터 |
| 질의 방식 | 표준 SQL(Structured Query Language)의 복합 조인과 집계 | API(Application Programming Interface) 호출과 제한적 키 조회 |
| 주요 병목 | 글로벌 락 경합, 인덱스 갱신 부하, 복합 조인 부하 | 네트워크 지연, 최종 일관성 지연, 파티션 핫스팟 |

- 워크로드별 선택 기준 :
  1. RDBMS 적합 : 금융 원장이나 결제 정산처럼 복합 업무 규칙과 무결성이 최우선인 업무.
  2. NoSQL 적합 : 대규모 실시간 인입, 사용자 세션 저장, 센서 시계열, 비정형 문서 보관.
  3. **Polyglot Persistence** (업무 목적별로 여러 종류의 저장소를 조합하는 방식) : 트랜잭션은 RDBMS, 세션은 Redis, 유연한 문서는 MongoDB로 나누어 구성.

## Ⅴ. NoSQL의 한계와 방안

- 핵심 요약 : 분산 트랜잭션의 복잡성, 스키마 부재에 따른 거버넌스 약화, 샤드 키 편향의 한계를 보상 트랜잭션, 데이터 검증, 키 설계로 통제.

- 장점 : 범용 노드 기반의 저비용 수평 확장, 스키마 변경 없는 데이터 수용, 단일 키 기반 고속 처리.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 분산 트랜잭션 한계 | 여러 샤드에 걸친 2PC(Two-Phase Commit)는 코디네이터 장애와 락 대기를 키움 | **Saga 패턴** (분산 트랜잭션을 단계별 로컬 트랜잭션과 보상 트랜잭션으로 나누는 방식)을 적용하고 메시지 큐로 최종 일관성을 맞춤 | 보상 트랜잭션 실패율 |
| 스키마 부재에 따른 거버넌스 약화 | 필드가 제각각 쌓여 데이터 모델이 파편화되고 조인이 어려워 애플리케이션 측 추가 조회가 늘어남 | JSON Schema 기반 검증 계층 도입, **CQRS** (Command Query Responsibility Segregation, 쓰기 모델과 조회 모델을 분리하는 방식) 적용 | 스키마 위반 건수 |
| 샤드 키 편향 | 순차 증가 키나 편중된 범주 키는 특정 샤드에 쓰기가 몰림 | 복합 해시 키와 솔팅(Salting)을 적용하고 **일관된 해싱** (Consistent Hashing, 노드 추가·제거 시 재배치량을 줄이는 해싱 기법) 도입 | 샤드별 부하 편차 |

## Ⅵ. NoSQL 도입에 대한 기술사적 제언

- 핵심 요약 : 질의 패턴을 먼저 정의하고 핫스팟을 막는 키 설계와 백업·재해복구 체계를 함께 세우는 것이 필요하다.
- 데이터 모델링은 개념 모델을 먼저 세우는 RDBMS와 달리 애플리케이션의 질의 패턴을 먼저 분석하고 파티션 키와 문서 구조를 거꾸로 설계해야 한다. 개발 조직은 이 순서를 설계 표준으로 명문화하는 것이 바람직하다.
- 최종 일관성 환경에서는 특정 시점을 보장한 백업이 어려우므로, 운영 조직은 분산 스냅샷과 **CDC** (Change Data Capture, 데이터 변경 이력을 로그로 추출하는 기법)를 함께 두고 재해복구 절차에서 데이터 정합성을 검증하는 체계를 갖춰야 한다.

## Ⅶ. 결론

- 핵심 요약 : NoSQL은 CAP과 BASE 원칙에 기반한 수평 확장형 저장소로, 워크로드에 맞춘 다중 저장소 전략이 핵심.
- 시사점 : RDBMS와 NoSQL의 역할을 나누어 설계하고, 질의 패턴 중심의 키 설계로 확장성과 정합성을 함께 확보하는 것이 중요.
