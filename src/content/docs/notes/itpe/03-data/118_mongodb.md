---
sidebar:
  order: 118
  label: "118. MongoDB"
  badge:
    text: "C"
    variant: note
title: "MongoDB 문서 지향(Document-Oriented) NoSQL 아키텍처 및 샤딩·복제 체계"
author: "OpenAI Codex"
date: "2026-09-20T19:35:00+09:00"
tags:
  - "notes-data"
weight: 118
extra:
  model: "GPT-5"
  keyword_grade: "C"
  question_no: "118"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>NoSQL·비정형 데이터베이스</span><strong>MongoDB</strong></div>

## 큰 그림과 30초 인출

```text
[MongoDB 분산 샤딩(Sharding) 클러스터 및 복제셋(Replica Set) 아키텍처]

       ┌────────────────────────┐
       │   클라이언트 (App)     │
       └───────────┬────────────┘
                   │ BSON 쿼리 요청
       ┌───────────▼────────────┐        ┌───────────────────────────────┐
       │     Mongos (라우터)    │◄──────►│ Config Server (메타데이터 쿼럼)│
       └─────┬────────────┬─────┘        └───────────────────────────────┘
             │            │
      샤드키 │            │ 샤드키
      분기   ▼            ▼ 분기
  ┌─────────────────┐  ┌─────────────────┐
  │  Shard A        │  │  Shard B        │
  │  (Replica Set)  │  │  (Replica Set)  │
  │  ┌───────────┐  │  │  ┌───────────┐  │
  │  │  Primary  │  │  │  │  Primary  │  │
  │  └─────┬─────┘  │  │  └─────┬─────┘  │
  │   복제 │(Oplog) │  │   복제 │(Oplog) │
  │  ┌─────▼─────┐  │  │  ┌─────▼─────┐  │
  │  │ Secondary │  │  │  │ Secondary │  │
  │  └───────────┘  │  │  └───────────┘  │
  └─────────────────┘  └─────────────────┘
```

- 본질: **JSON 형태의 유연한 BSON(Binary JSON) 문서 모델을 기반으로 복잡한 계층형 데이터를 RDBMS의 테이블 조인 없이 단일 문서에 중첩(Embedding)하거나 참조(Referencing)하여 초고속으로 처리하고, 복제셋(Replica Set)을 통한 자동 무중단 장애 복구와 샤딩(Sharding)을 통한 수평 확장(Scale-out)을 제공하는 오픈소스 NoSQL 데이터베이스**
- 암기: `비-몽-컨-샤` (BSON, Mongos 라우터, Config Server, Shard Replica Set) / `임-참-애-와` (임베딩 vs 참조, 애그리게이션 파이프라인, WiredTiger 엔진)
- 판단축:
  - **Embedding (중첩)**: 1:1 또는 유한한 1:N 관계에서 함께 읽히는 데이터, 단일 I/O로 고속 반환
  - **Referencing (참조)**: 1:N에서 N이 수천 건 이상 무한 증가하거나(M:N 관계), 빈번한 독립 수정이 필요한 경우
- 주의: 단일 BSON 문서의 최대 크기는 **16MB**로 엄격히 제한되므로, 무한히 누적되는 로그나 댓글을 배열로 중첩할 경우 문서 크기 초과 에러가 발생하므로 버킷 패턴(Bucket Pattern)이나 참조 모델로 분리해야 함

## 예상문제

> 대용량 비정형 데이터 처리를 위한 문서 지향(Document-oriented) NoSQL 데이터베이스인 MongoDB의 개념과 핵심 특징을 설명하고, 분산 샤딩(Sharding) 클러스터의 3대 구성요소와 데이터 모델링 기법(Embedding vs Referencing)을 비교하시오. (25점)

## Ⅰ. 유연한 스키마와 수평 확장을 제공하는 MongoDB 개요

#### 한줄 요약: 테이블 대신 컬렉션, 행 대신 BSON 문서를 사용하여 스키마 제약 없이 대규모 객체를 고속 처리하는 문서 지향 NoSQL

- **배경**: 애자일 개발 환경에서 잦은 스키마 변경 시 RDBMS의 DDL 락(Lock) 병목이 발생하고, 복잡한 1:N 계층 데이터를 표현하기 위해 수많은 조인(Join) 연산으로 성능이 저하되는 문제 봉착
- **정의**: C++로 작성된 크로스 플랫폼 문서 지향 NoSQL로, 스키마리스(Schema-less) 특성과 WiredTiger 스토리지 엔진을 기반으로 고성능 읽기/쓰기를 제공하는 데이터베이스
- **데이터 모델링 기본 단위**:
  - RDBMS Database $\rightarrow$ MongoDB Database
  - RDBMS Table $\rightarrow$ MongoDB **Collection (컬렉션)**
  - RDBMS Row $\rightarrow$ MongoDB **Document (BSON 문서)**
  - RDBMS Column $\rightarrow$ MongoDB **Field (필드)**

## Ⅱ. MongoDB의 4대 핵심 아키텍처 특성

#### 한줄 요약: BSON 이진 포맷, WiredTiger 스토리지 엔진, 자동 복제셋, 수평 샤딩의 결합

```text
  ┌─────────────────────────────────────────────────────────────┐
  │                 MongoDB 4대 핵심 아키텍처 특성              │
  └─────────────────────────────────────────────────────────────┘
          │                      │                      │
  ┌───────▼──────────┐   ┌───────▼──────────┐   ┌───────▼──────────┐
  │ 1. BSON 포맷     │   │ 2. WiredTiger    │   │ 3. Replica Set   │
  ├──────────────────┤   ├──────────────────┤   ├──────────────────┤
  │ - JSON의 이진화  │   │ - 기본 스토리지  │   │ - Primary-Sec    │
  │ - 빠른 인코딩/   │   │ - 문서 레벨 동시성│  │ - Raft 기반 자동 │
  │   파싱, 날짜지원 │   │ - Snappy 압축    │   │   선출 Failover  │
  └──────────────────┘   └──────────────────┘   └──────────────────┘
```

1. **BSON (Binary JSON)**: JSON의 가독성과 텍스트 직렬화 오버헤드를 극복하기 위해 길이 접두사(Length Prefix)와 타입 태그를 추가하여 초고속 파싱과 인덱싱을 지원하는 이진 포맷
2. **WiredTiger 스토리지 엔진**: 문서 레벨 동시성 제어(Document-level Concurrency)와 체크포인트 메커니즘을 지원하며, Snappy/Zlib 알고리즘으로 디스크 사용량을 60~80% 압축
3. **고가용성 복제셋 (Replica Set)**: 홀수 개(보통 3노드)로 구성되어 Primary 노드 장애 시 2초 이내에 Secondary 중 하나를 새로운 Primary로 자동 선출(Election)
4. **수평적 샤딩 (Sharding)**: 단일 노드의 용량을 초과하는 페타바이트급 데이터를 샤드 키(Shard Key)를 기준으로 여러 샤드 서버에 청크(Chunk) 단위로 자동 분산

## Ⅲ. 분산 샤딩(Sharding) 클러스터의 3대 핵심 구성요소

#### 한줄 요약: 클라이언트 요청을 라우팅하는 Mongos, 메타데이터를 보관하는 Config Server, 데이터를 담는 Shard 노드

| 구성요소 | 핵심 역할 | 분산 동작 메커니즘 |
|:---|:---|:---|
| **Mongos (Query Router)** | 샤딩 클러스터의 단일 진입점(Gateway) | 클라이언트의 BSON 쿼리를 수신하여 Config Server의 메타데이터를 참조한 후, 해당 데이터가 존재하는 특정 샤드로 요청을 라우팅하고 결과를 취합(Merge) |
| **Config Server** | 클러스터 메타데이터 저장소 | 어떤 청크(Chunk)가 어느 샤드에 저장되어 있는지 범위와 매핑 정보를 관리. 자체 3노드 복제셋(Raft)으로 완벽한 일관성(CP) 유지 |
| **Shard Nodes** | 실제 파티션 데이터 저장 노드 | 전체 데이터의 하위 분할 청크들을 보관. 각 샤드 노드 자체는 장애 방지를 위해 3개 이상의 노드로 구성된 **독립된 Replica Set**으로 구축 |

## Ⅳ. MongoDB 데이터 모델링 전략: Embedding vs Referencing

#### 한줄 요약: 조인을 없애고 한 번에 읽는 비정규화 중첩(Embedding)과 관계를 분리하는 정규화 참조(Referencing)의 트레이드오프

```text
 [1. Embedding 패턴: 1개 문서로 통합]
  {
    _id: "user1",
    name: "홍길동",
    addresses: [
      { city: "서울", street: "강남대로" },
      { city: "성남", street: "판교로" }
    ]
  } -> 단 1회의 디스크 I/O로 완결 (초고속 읽기)

 [2. Referencing 패턴: ID를 통한 외래 참조]
  { _id: "user1", name: "홍길동" }
  { _id: "addr1", userId: "user1", city: "서울" }
  -> $lookup (조인) 수행 필요, 데이터 무한 증가 수용 가능
```

| 비교 항목 | 중첩 모델 (Embedding) | 참조 모델 (Referencing) |
|:---|:---|:---|
| **관계 표현** | 단일 BSON 문서 내부에 배열이나 서브 도큐먼트로 포함 | 문서 간에 `_id`를 외래키(FK)처럼 저장하고 분리 |
| **I/O 성능** | **단 1회의 디스크 읽기로 모든 데이터 조회 (초고속)** | 연관 데이터 조회 시 `$lookup` 조인 또는 애플리케이션 추가 조회 필요 |
| **원자성 (ACID)** | **단일 문서 업데이트는 락 없이 완벽한 원자성 보장** | 다중 문서 트랜잭션 필요 (성능 저하 수반) |
| **문서 크기 제한** | 16MB 한도 초과 위험 존재 | 16MB 제한으로부터 완벽히 자유로움 |
| **적합한 관계** | 1:1 관계, 유한하고 적은 수의 1:N 관계 (댓글 100개 미만) | 1:N에서 N이 수천 건 이상 폭증하거나 N:M 다대다 관계 |

## Ⅴ. RDBMS vs MongoDB vs Redis 3대 데이터베이스 비교

#### 한줄 요약: 엄격한 정규화의 RDBMS, 유연한 문서 저장의 MongoDB, 초고속 인메모리 캐시의 Redis

| 비교 항목 | RDBMS (PostgreSQL) | MongoDB | Redis |
|:---|:---|:---|:---|
| **데이터 모델** | 2차원 관계형 테이블 (행/열) | **문서 지향 (BSON Document)** | 인메모리 키-값 (Key-Value) 및 자료구조 |
| **스키마 특성** | 엄격한 정적 스키마 (Schema-on-Write) | **동적 스키마 (Schema-less)** | 스키마 없음 |
| **트랜잭션 (ACID)** | 전사 다중 테이블 완전 지원 (기본) | 단일 문서 기본, 다중 문서 트랜잭션 지원 | 트랜잭션(MULTI/EXEC) 일부 지원 |
| **확장 방식** | 수직 확장(Scale-up), 읽기 복제본 | **수평 샤딩(Scale-out) 기본 내장** | 레디스 클러스터(샤딩) |
| **주요 사용 사례** | 금융, 결제, ERP 코어 원장 | 콘텐츠 관리, 카탈로그, IoT 로그, 모바일 백엔드 | 세션 저장소, 캐싱, 실시간 순위표, 메시지 브로커 |

## Ⅵ. 실무 운영 이슈 및 트러블슈팅 (Troubleshooting)

#### 한줄 요약: 샤드 키 단조 증가로 인한 Hotspot, 점보 청크(Jumbo Chunk), 메모리 부족 방지

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **샤드 핫스팟 (Hotspot)** | `_id`(ObjectId)나 생성일자처럼 단조 증가하는 키를 샤드 키로 설정하여 특정 샤드 1개에만 쓰기 폭증 | 카디널리티가 높은 복합 샤드 키 선정 또는 **Hashed Shard Key** 적용 |
| **점보 청크 (Jumbo Chunk)** | 샤드 키 값이 동일한 데이터가 64MB 청크 제한을 초과하여 분할(Split) 불가 상태 발생 | 세부 식별자를 추가하여 샤드 키를 복합 키(`{ country: 1, userId: 1 }`)로 재설계 |
| **16MB 문서 초과 에러** | 사용자의 활동 로그나 알림 목록을 단일 문서 내 무한 배열로 누적 | 버킷 패턴(Bucket Pattern)을 적용하여 100건 단위로 문서를 분할 저장하거나 GridFS 활용 |

## Ⅶ. 기술사적 제언: 현대적 멀티모달 데이터베이스로서의 진화

#### 한줄 요약: 단순 문서 저장소를 넘어 시계열(Time Series), 벡터 검색(Atlas Vector Search), 스트림 처리를 통합하는 플랫폼화

```text
 [MongoDB Atlas의 통합 엔지니어링 생태계]
  - Document Store: BSON 기반 트랜잭션 데이터베이스
  - Vector Search: LLM 임베딩 벡터 내장 인덱싱 (HNSW 지원) -> 별도 Vector DB 도입 불필요
  - Time Series: IoT 센서 시계열 최적화 컬렉션 내장
  - Search Nodes: Lucene 기반 전문 검색(Full-text) 통합
```

- 과거에는 NoSQL을 "보조적인 비정형 저장소"로 치부했으나, 현대 MongoDB는 **ACID 다중 문서 분산 트랜잭션**을 완성하고 **Atlas Vector Search**를 내장하여 RAG 파이프라인의 핵심 백엔드로 자리매김함
- RDBMS와 무조건적인 대체가 아닌, 코어 금융 원장은 PostgreSQL로, 서비스 계층의 카탈로그와 AI 지식 베이스는 MongoDB로 이원화하는 **폴리글랏 퍼시스턴스(Polyglot Persistence)**가 현대 소프트웨어 아키텍처의 정답임

---

## 1교시 10점 답안 발췌

```text
1. MongoDB의 정의
  - BSON 문서 포맷을 채택하여 복잡한 계층 데이터를 테이블 조인 없이 저장하고, 샤딩과 복제셋으로 수평 확장을 제공하는 문서 지향 NoSQL.

2. 분산 샤딩 클러스터 아키텍처 및 3대 구성요소
  가. 아키텍처:
    - Client -> Mongos(라우터) -> Config Server(메타데이터 참조) -> Shard Nodes(복제셋 데이터 분산).
  나. 3대 구성요소:
    - Mongos(쿼리 라우팅 및 결과 취합), Config Server(청크 매핑 메타데이터), Shard(실제 파티션 복제셋).

3. 데이터 모델링 기법 비교
  - Embedding(중첩): 1회 I/O 고속 조회 및 단일 문서 원자성, 16MB 한도 주의.
  - Referencing(참조): $lookup 조인 필요하나 무제한 대용량 및 M:N 관계에 적합.
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제127회 정보관리 2교시: 문서 지향 NoSQL인 MongoDB의 특징과 아키텍처 및 데이터 모델링 기법
- **검증 출처**:
  - Shannon Bradshaw et al., "MongoDB: The Definitive Guide (3rd Edition)", O'Reilly
  - MongoDB Manual, "Sharding Architecture and Data Modeling Concepts"

---

## 학습 체크

- [ ] MongoDB 분산 샤딩의 3대 구성요소(Mongos, Config Server, Shard)의 역할을 설명할 수 있는가?
- [ ] Embedding(중첩)과 Referencing(참조)의 장단점 및 16MB 한계에 대한 대응책을 제시할 수 있는가?
- [ ] 단조 증가 샤드 키의 핫스팟 문제와 해시 샤드 키(Hashed Shard Key)의 해결 원리를 설명할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-001 NoSQL](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/001_nosql.md)
- 연관 토픽: [03-045 샤딩(Sharding)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/045_sharding.md), [03-113 CAP·PACELC 이론](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/113_cap_pacelc.md)
