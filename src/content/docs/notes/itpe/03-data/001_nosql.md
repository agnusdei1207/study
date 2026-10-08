---
title: "NoSQL(Not Only SQL)"
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

## Ⅰ. 대규모 비정형 데이터 처리를 위한 NoSQL의 개요

### 가. NoSQL(Not Only SQL)의 정의
- **NoSQL**(Not Only SQL) : 관계형 데이터 모델(RDBMS, Relational Database Management System)의 엄격한 **ACID**(Atomicity, Consistency, Isolation, Durability) 트랜잭션 및 고정 스키마 한계를 극복하고, **수평적 확장성** (Scale-Out)과 고성능 읽기·쓰기를 지원하는 비관계형 분산 데이터 저장소 기술.
- 웹 스케일 트래픽, 비정형/반정규화 데이터, 유연한 스키마 변경 요구를 수용하기 위해 **CAP**(Consistency, Availability, Partition Tolerance) 정리 기반의 **BASE** (Basically Available, Soft-state, Eventually consistent) 특성을 채택함.

### 나. RDBMS 대비 NoSQL의 주요 패러다임 변화
- **정규화 탈피** : 질의 시 고비용 JOIN 연산을 배제하고 데이터 중복을 허용하여 단일 키 조회의 처리량을 극대화.
- **수평 분산 우선** : 고가의 단일 대형 서버(Scale-Up) 대신 저비용 범용 노드 클러스터 기반의 **샤딩** (Sharding) 및 **복제** (Replication) 아키텍처 구현.

---

## Ⅱ. NoSQL의 핵심 데이터 모델 분류 및 내부 메커니즘

### 가. 4대 데이터 모델 분류 및 특성

```text
[ NoSQL 데이터 모델 분류 ]
+---------------------+---------------------+---------------------+---------------------+
| Key-Value Store     | Document Store      | Column-Family Store | Graph Store         |
+---------------------+---------------------+---------------------+---------------------+
| Key -> Raw Value    | Key -> JSON/BSON    | Row -> ColumnFamily | Node -> Edge -> Node|
| Redis, Memcached    | MongoDB, Couchbase  | Cassandra, HBase    | Neo4j, Amazon Neptune
| 단순 캐싱, 세션 저장 | 카탈로그, CMS       | 대용량 시계열, 로그 | 소셜그래프, 사기탐지 |
+---------------------+---------------------+---------------------+---------------------+
```

| 분류 | 데이터 구조 및 특성 | 대표 질의/인덱싱 방식 | 주요 적용 분야 | 대표 솔루션 |
| :--- | :--- | :--- | :--- | :--- |
| **Key-Value** | 유일 키(Key)에 임의의 바이너리/문자열 값 매핑 | O(1) 해시 테이블 기반 조회, 범위 질의 제한 | 캐싱 계층, 세션 저장, 장바구니 | Redis, AWS(Amazon Web Services) DynamoDB |
| **Document** | 계층적 문서(JSON(JavaScript Object Notation), BSON(Binary JSON), XML(Extensible Markup Language)) 단위 저장 | 내부 필드 보조 인덱스(Secondary Index) 지원 | 콘텐츠 관리, 이커머스 상품 카탈로그 | MongoDB, CouchDB |
| **Column-Family** | 행 키별로 가변적 컬럼 집합(Column Family) 관리 | SSTable(Sorted String Table), LSM-Tree(Log-Structured Merge-Tree) 기반 대규모 쓰기 최적화 | IoT(Internet of Things) 센서 시계열 데이터, 대규모 로그 | Apache Cassandra, HBase |
| **Graph** | 노드(Node), 간선(Edge), 속성(Property) 관계 모델 | 포인터 기반 인접 노드 탐색(Index-free Adjacency) | 지식 그래프, 추천 시스템, FDS(Fraud Detection System) 탐지 | Neo4j, JanusGraph |

### 나. NoSQL의 분산 합의 및 데이터 정합성 메커니즘 (BASE vs ACID)

```text
[ 분산 정합성 Quorum 모델 ]
              N (전체 복제본 수)
              /                 \
     W (쓰기 성공 응답 수)       R (읽기 성공 응답 수)
     
  * 강한 일관성(Strong Consistency) 조건 : W + R > N
  * 빠른 쓰기 최적화 조건             : W = 1, R = N
  * 빠른 읽기 최적화 조건             : W = N, R = 1
```

- **Basically Available** : 노드 장애 발생 시에도 시스템 전체 가용성을 유지하며, 특정 파티션 실패가 전체 다운으로 확산되지 않음.
- **Soft-state** : 외부 입력이 없더라도 백그라운드 데이터 동기화 과정에 의해 시스템 상태가 지속적으로 갱신될 수 있음.
- **Eventual Consistency** : 새로운 갱신이 발생하지 않는 한 일정 시간이 경과하면 분산 노드 간 데이터 정합성이 일치 상태에 수렴함.

---

## Ⅲ. RDBMS와 NoSQL의 비교 분석 및 선택 기준

### 가. RDBMS vs NoSQL 기술 비교

| 비교 항목 | RDBMS (관계형 DBMS(Database Management System)) | NoSQL (비관계형 DBMS) |
| :--- | :--- | :--- |
| **데이터 스키마** | 고정 스키마, 엄격한 DDL(Data Definition Language) 및 도메인 무결성 | Dynamic/Schema-less, 유연한 구조 변경 |
| **트랜잭션 보장** | 엄격한 ACID (원자성, 일관성, 격리성, 영속성) | BASE (최종 일관성, 가용성 중심 트레이드오프) |
| **확장성 모델** | 수직 확장(Scale-Up), 공유 디스크/공유 메모리 | 수평 확장(Scale-Out), 비공유(Shared-Nothing) 클러스터 |
| **질의 언어** | 표준 SQL (복합 JOIN, 집계, 서브쿼리 강력) | API(Application Programming Interface), 선언적 JSON 쿼리, 제한적 키 조회 |
| **병목 요인** | 글로벌 락킹, 인덱스 갱신 경합, 복합 조인 부하 | 네트워크 지연, 최종 일관성 지연, 분산 파티션 핫스팟 |

### 나. 워크로드별 아키텍처 선택 가이드라인
- RDBMS 적합 : 금융 코어 뱅킹, 결제 정산, 복합 업무 규칙 및 무결성이 비즈니스의 최우선인 시스템.
- NoSQL 적합 : 대규모 실시간 스트리밍 인입, 유저 프로필/세션 저장, IoT 시계열 데이터, 비정형 문서 보관.
- **Polyglot Persistence** : 단일 저장소 만능주의를 탈피하고 트랜잭션은 RDBMS, 고속 세션은 Redis, 텍스트 검색은 Elasticsearch, 유연 문서는 MongoDB로 분리 구성하는 다중 저장소 패턴 적용.

---

## Ⅳ. NoSQL 도입·운영 시 주요 한계점 및 해결 방안

- 분산 환경에서의 트랜잭션 원자성 및 다중 문서 정합성 한계 :
  - 한계점 : 샤딩 환경에서 분산 2PC(Two-Phase Commit) 적용 시 코디네이터 단일 장애점(SPOF, Single Point of Failure) 및 네트워크 지연에 따른 락 블로킹 병목 발생.
  - 해결 방안 : 사가(Saga) 패턴(Choreography/Orchestration) 기반의 보상 트랜잭션 설계, 비동기 메시지 큐(Kafka)를 통한 이벤트 주도 최종 일관성(Eventual Consistency) 수렴.
- Dynamic Schema로 인한 데이터 거버넌스 훼손 및 복합 조인 제약 :
  - 한계점 : 스키마 강제성이 없어 애플리케이션 진화에 따라 데이터 모델 파편화 발생 및 다중 컬렉션 간 JOIN 불가로 애플리케이션 측 N+1 조회 부하 가중.
  - 해결 방안 : JSON Schema 유효성 검증 레이어 도입, CQRS(Command Query Responsibility Segregation) 패턴을 적용하여 쓰기는 NoSQL, 복합 분석 질의는 RDBMS/DW(Data Warehouse)로 분리 및 역정규화(Embedding) 패턴 표준화.
- 샤드 키 편향(Hotspot) 및 데이터 리밸런싱 부하 :
  - 한계점 : 순차 증가 키나 특정 범주형 키 선정 시 특정 샤드로 쓰기 I/O가 집중되어 클러스터 불균형 및 청크 마이그레이션 중 네트워크 대역폭 고갈.
  - 해결 방안 : 복합 해시 키(Compound Hash Key) 및 솔팅(Salting) 기법 적용, 가상 노드 기반 일관된 해싱(Consistent Hashing) 도입으로 균등 분산 보장.

---

## Ⅴ. NoSQL 엔터프라이즈 도입 시 고려사항 및 실무 제언

- 데이터 모델링 패러다임 역전 : 개념적 모델링 후 접근 경로를 정의하는 RDBMS와 달리, NoSQL은 **애플리케이션의 질의 패턴** (Query-Driven)을 먼저 분석하고 이에 맞추어 키 구조 및 파티션 키를 역설계해야 함.
- 파티션 핫스팟 방지 전략 : 샤드 키(Shard Key) 편향으로 인해 특정 노드로 트래픽이 집중되는 현상을 방지하기 위해 복합 해시 키(Hash Key + Range Key) 설계 및 솔팅(Salting) 기법 적용 필수.
- 백업 및 재해복구(DR, Disaster Recovery) 체계 구축 : 최종 일관성 환경에서는 시점 일관성(Point-in-Time) 백업 확보가 어려우므로, 분산 스냅샷과 CDC(Change Data Capture) 로그 기반의 정합성 검증 체계를 사전에 수립할 것을 제언함.
