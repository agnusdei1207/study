---
title: "NoSQL(Not Only SQL)"
author: "agnusdei1207"
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

## 연관 키워드

- NoSQL(Not Only SQL), RDBMS, CAP 정리, BASE, Scale-Out, 샤딩(Sharding), 복제(Replication)
- Key-Value, Document, Column-Family, Graph, Quorum, Polyglot Persistence, Saga 패턴, CQRS

## Ⅰ. NoSQL의 개요

- 핵심 요약 : 고정 스키마와 수직 확장의 한계를 극복하는 수평 확장형 비관계형 분산 데이터 저장소 기술.
- 개념 : RDBMS(Relational Database Management System)의 엄격한 ACID(Atomicity, Consistency, Isolation, Durability) 트랜잭션 및 고정 스키마의 한계를 극복하고, 수평적 확장(Scale-Out)과 고성능 읽기·쓰기를 지원하는 비관계형 분산 데이터 저장소 기술.
- 배경 및 필요성 :
  1. 웹 스케일 트래픽과 대규모 동시 접속의 처리 부담.
  2. 비정형·반정형 데이터의 급증과 유연한 스키마 변경 요구.
  3. 고가의 단일 대형 서버(Scale-Up) 대신 저비용 범용 노드 클러스터 구성의 필요.
- 주요 목적 : CAP(Consistency, Availability, Partition Tolerance) 정리 기반의 BASE(Basically Available, Soft-state, Eventually consistent) 특성 채택을 통한 가용성·확장성·처리량 확보.

## Ⅱ. NoSQL의 특징

- 핵심 요약 : 조인 배제·중복 허용·수평 분산·최종 일관성 중심의 패러다임 전환.

1. 정규화 탈피 : 질의 시 고비용 JOIN 연산을 배제하고 데이터 중복을 허용하여 단일 키 조회의 처리량 극대화.
2. 수평 분산 우선 : 샤딩(Sharding)과 복제(Replication) 기반의 범용 노드 클러스터 아키텍처.
3. Schema-less : 스키마 강제성의 부재와 애플리케이션 주도의 유연한 구조 변경.
4. BASE 특성 : Basically Available(가용성 우선), Soft-state(상태 유동성), Eventual Consistency(최종 일관성)의 수용.
5. 4대 데이터 모델 : Key-Value, Document, Column-Family, Graph 저장소의 용도별 특화.

## Ⅲ. NoSQL의 구조 (흐름)

- 핵심 요약 : 4대 데이터 모델의 용도별 분류와 Quorum 기반 분산 정합성 제어 구조.

```text
[ NoSQL 4대 데이터 모델 ]
 ├─ Key-Value Store : Redis, Memcached, DynamoDB
 ├─ Document Store  : MongoDB, Couchbase
 ├─ Column-Family   : Cassandra, HBase
 └─ Graph Store     : Neo4j, Amazon Neptune
```

```text
[ 분산 정합성 Quorum 모델 ]
 N : 전체 복제본 수
 ├─ W : 쓰기 성공 응답 수
 └─ R : 읽기 성공 응답 수
 * 강한 일관성 조건 : W + R > N
 * 빠른 쓰기 최적화 : W = 1, R = N
 * 빠른 읽기 최적화 : W = N, R = 1
```

| 분류 | 데이터 구조 및 특성 | 질의·인덱싱 방식 | 주요 적용 분야 | 대표 솔루션 |
|---|---|---|---|---|
| Key-Value | 유일 키(Key)에 임의의 바이너리·문자열 값 매핑 | O(1) 해시 테이블 기반 조회, 범위 질의 제한 | 캐싱 계층, 세션 저장, 장바구니 | Redis, AWS(Amazon Web Services) DynamoDB |
| Document | JSON(JavaScript Object Notation), BSON(Binary JSON), XML(Extensible Markup Language) 등 계층적 문서 단위 저장 | 내부 필드 보조 인덱스(Secondary Index) 지원 | 콘텐츠 관리, 이커머스 상품 카탈로그 | MongoDB, CouchDB |
| Column-Family | 행 키별 가변적 컬럼 집합(Column Family) 관리 | SSTable(Sorted String Table), LSM-Tree(Log-Structured Merge-Tree) 기반 대규모 쓰기 최적화 | IoT(Internet of Things) 센서 시계열, 대규모 로그 | Apache Cassandra, HBase |
| Graph | 노드(Node), 간선(Edge), 속성(Property)의 관계 모델 | 포인터 기반 인접 노드 탐색(Index-free Adjacency) | 지식 그래프, 추천 시스템, FDS(Fraud Detection System) 탐지 | Neo4j, JanusGraph |

- BASE의 3대 요소 :
  1. Basically Available : 노드 장애 시에도 시스템 전체 가용성 유지 및 특정 파티션 실패의 전체 다운 확산 차단.
  2. Soft-state : 외부 입력이 없어도 백그라운드 데이터 동기화에 의한 시스템 상태의 지속 갱신.
  3. Eventual Consistency : 새로운 갱신이 없는 경우 일정 시간 경과 후 분산 노드 간 데이터 정합성의 일치 상태 수렴.

## Ⅳ. NoSQL과 RDBMS의 비교

- 핵심 요약 : ACID·Scale-Up·SQL 중심의 RDBMS와 BASE·Scale-Out·API 중심의 NoSQL의 워크로드별 선택.

| 비교 항목 | RDBMS(관계형 데이터베이스 관리 시스템) | NoSQL(비관계형 DBMS(Database Management System)) |
|---|---|---|
| 데이터 스키마 | 고정 스키마, 엄격한 DDL(Data Definition Language) 및 도메인 무결성 | Dynamic·Schema-less, 유연한 구조 변경 |
| 트랜잭션 보장 | 엄격한 ACID(원자성, 일관성, 격리성, 영속성) | BASE(최종 일관성, 가용성 중심 트레이드오프) |
| 확장성 모델 | 수직 확장(Scale-Up), 공유 디스크·공유 메모리 | 수평 확장(Scale-Out), 비공유(Shared-Nothing) 클러스터 |
| 질의 언어 | 표준 SQL(복합 JOIN, 집계, 서브쿼리) | API(Application Programming Interface), 선언적 JSON 쿼리, 제한적 키 조회 |
| 병목 요인 | 글로벌 락킹, 인덱스 갱신 경합, 복합 조인 부하 | 네트워크 지연, 최종 일관성 지연, 분산 파티션 핫스팟 |

- 워크로드별 선택 기준 :
  1. RDBMS 적합 : 금융 코어 뱅킹, 결제 정산 등 복합 업무 규칙·무결성이 최우선인 시스템.
  2. NoSQL 적합 : 대규모 실시간 스트리밍 인입, 사용자 프로필·세션 저장, IoT 시계열, 비정형 문서 보관.
  3. Polyglot Persistence : 트랜잭션은 RDBMS, 고속 세션은 Redis, 텍스트 검색은 Elasticsearch, 유연 문서는 MongoDB로 분리 구성하는 다중 저장소 패턴.

## Ⅴ. NoSQL의 장점과 한계

- 핵심 요약 : 저비용 확장성·유연성의 장점과 분산 트랜잭션·거버넌스·핫스팟의 한계.

- 장점
  1. 범용 노드 클러스터 기반의 저비용 수평 확장.
  2. 스키마 변경 없는 유연한 데이터 모델 수용.
  3. 단일 키 기반 고속 읽기·쓰기 처리 성능.

- 한계점 1 : 분산 환경의 트랜잭션 원자성 및 다중 문서 정합성 한계
  - 한계점 : 샤딩 환경에서 분산 2PC(Two-Phase Commit) 적용 시 코디네이터 단일 장애점(SPOF, Single Point of Failure) 및 네트워크 지연에 따른 락 블로킹 병목 발생.
  - 해결 방안 : 사가(Saga) 패턴(Choreography·Orchestration) 기반의 보상 트랜잭션 설계, Kafka 등 비동기 메시지 큐를 통한 이벤트 주도 최종 일관성 수렴.
- 한계점 2 : Dynamic Schema에 따른 데이터 거버넌스 훼손 및 복합 조인 제약
  - 한계점 : 스키마 강제성 부재로 인한 데이터 모델 파편화 및 다중 컬렉션 간 JOIN 불가에 따른 애플리케이션 측 N+1 조회 부하 가중.
  - 해결 방안 : JSON Schema 유효성 검증 레이어 도입, CQRS(Command Query Responsibility Segregation) 적용을 통한 쓰기용 NoSQL과 분석용 RDBMS·DW(Data Warehouse)의 분리, 역정규화(Embedding) 패턴 표준화.
- 한계점 3 : 샤드 키 편향(Hotspot)과 데이터 리밸런싱 부하
  - 한계점 : 순차 증가 키나 특정 범주형 키 선정 시 특정 샤드의 쓰기 I/O 집중, 클러스터 불균형 및 청크 마이그레이션 중 네트워크 대역폭 고갈.
  - 해결 방안 : 복합 해시 키(Compound Hash Key)와 솔팅(Salting) 기법 적용, 가상 노드 기반 일관된 해싱(Consistent Hashing) 도입을 통한 균등 분산 보장.

## Ⅵ. NoSQL에 대한 기술사적 제언

- 핵심 요약 : 질의 패턴 우선 설계, 핫스팟 방지 키 설계, CDC 기반 백업·DR 체계 수립.
- 데이터 모델링 패러다임 역전 수용 : 개념 모델링 후 접근 경로를 정의하는 RDBMS와 달리 애플리케이션의 질의 패턴(Query-Driven)을 먼저 분석한 뒤 키 구조·파티션 키의 역설계 필요.
- 파티션 핫스팟 방지 전략 : 샤드 키(Shard Key) 편향에 따른 특정 노드 트래픽 집중 방지를 위한 복합 해시 키(Hash Key + Range Key) 설계 및 솔팅(Salting) 기법 적용.
- 백업 및 재해복구(DR, Disaster Recovery) 체계 구축 : 최종 일관성 환경에서 시점 일관성(Point-in-Time) 백업 확보가 어려운 점을 감안한 분산 스냅샷과 CDC(Change Data Capture) 로그 기반 정합성 검증 체계의 사전 수립.

## Ⅶ. 결론

- 핵심 요약 : NoSQL은 CAP·BASE 기반의 수평 확장형 저장소로 워크로드에 맞는 다중 저장소 전략이 핵심.
- 요약 : 4대 데이터 모델과 Quorum 정합성 제어를 통한 웹 스케일 데이터 처리 체계.
- 시사점 : RDBMS와의 역할 분담과 Polyglot Persistence 관점의 아키텍처 설계 필요.
