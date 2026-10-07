---
title: "MongoDB"
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

## Ⅰ. 문서 지향(Document-Oriented) NoSQL의 표준, MongoDB 개요

### 가. MongoDB의 정의
- JSON(JavaScript Object Notation) 형태의 동적 스키마를 바이너리로 최적화한 **BSON** (Binary JSON) 문서 포맷으로 데이터를 저장하며, **수평적 확장** (Sharding)과 **고가용성** (Replica Set)을 기본 내장한 대표적인 오픈소스 분산 문서 지향 NoSQL(Not Only SQL) 데이터베이스.
- 관계형 테이블의 엄격한 DDL(Data Definition Language) 제약에서 벗어나, 데이터 구조의 변경이 빈번하고 대규모 트래픽이 발생하는 현대 웹/앱 서비스에 최적화됨.

### 나. RDBMS(Relational Database Management System) 대비 MongoDB의 개념 매핑

```text
[ RDBMS vs MongoDB 용어 매핑 ]
RDBMS Concepts          MongoDB Concepts
--------------------+--------------------
Database            | Database
Table               | Collection
Row (튜플/레코드)   | Document (BSON 객체)
Column (속성)       | Field (Key-Value)
Primary Key         | _id (기본 자동 생성 ObjectId)
JOIN 연산           | Embedded Document (임베딩) 또는 $lookup
```

---

## Ⅱ. MongoDB의 핵심 아키텍처: 복제셋(Replica Set)과 샤딩(Sharding)

### 가. 고가용성을 위한 복제셋(Replica Set) 아키텍처

```text
[ MongoDB Replica Set 토폴로지 (P-S-S 모델) ]
             [Primary Node] (모든 쓰기/기본 읽기 처리)
              /           \
    (복제 로그 Oplog 전송)   (Oplog 동기화)
            v               v
  [Secondary Node 1]    [Secondary Node 2]
    - Primary 장애 시 Raft 기반 하트비트 투표로 Secondary 중 하나를 즉시 Primary로 자동 승격!
```

### 나. 대규모 분산 처리를 위한 샤딩 클러스터 아키텍처

```text
[ MongoDB Sharded Cluster 구조 ]
[App Client] ---> [mongos (쿼리 라우터)] <---> [Config Servers (샤드 메타데이터)]
                          |
         +----------------+----------------+
         |                                 |
         v                                 v
   [Shard A (Replica Set)]           [Shard B (Replica Set)]
   (Chunk: 0 ~ 50만)                 (Chunk: 50만 ~ 100만)
```

- **mongos** : 클라이언트의 질의를 받아 샤드 키 범위를 확인하고 적절한 샤드로 쿼리를 라우팅.
- **Config Server** : 각 샤드에 어떤 청크(Chunk)가 저장되어 있는지 클러스터의 전역 메타데이터를 보관(3대 이상의 복제셋으로 구성).
- **Shard** : 실제 데이터가 분할 저장되는 파티션 노드 (각 샤드 자체도 고가용성을 위해 Replica Set으로 구성).

---

## Ⅲ. MongoDB 데이터 모델링 전략: 임베딩 vs 참조

### 가. 두 모델링 패턴의 트레이드오프

| 비교 항목 | 임베딩 모델 (Embedded / Denormalized) | 참조 모델 (Referenced / Normalized) |
| :--- | :--- | :--- |
| **데이터 구조** | 부모 문서 내부에 자식 문서를 하위 배열로 직접 포함 | 자식 문서를 별도 컬렉션에 두고 부모의 `_id`를 외래키처럼 저장 |
| **조회 성능** | 단 한 번의 읽기 I/O 로 부모와 연관 데이터 동시 조회 (극상) | `$lookup`(조인) 또는 애플리케이션 다중 쿼리 필요 |
| **원자성 보장** | 단일 문서(Document) 단위의 완벽한 원자적 갱신($100\%$) 보장 | 두 컬렉션에 걸친 갱신 시 다중 문서 트랜잭션 오버헤드 |
| **문서 크기 한계** | BSON 단일 문서 최대 크기(16MB) 초과 위험 | 16MB 제한으로부터 자유로움 |
| **적합한 관계** | 1:1 관계, 포함되는 자식 데이터 수가 유한한 1:N (예: 주문-주문항목) | 1:다수(수천 개 이상), M:N 복합 관계 (예: 로그, 팔로워) |

---

## Ⅳ. MongoDB 운영의 주요 한계점 및 해결 방안

- **임베딩** (Embedding) vs **참조** (Referencing) 모델링 오류에 따른 16MB BSON 문서 한계 초과 :
  - 한계점 : 1:N 관계에서 무제한 증가하는 하위 배열을 임베딩 방식으로 설계하여 16MB 문서 크기 제한을 초과하고 패딩 및 메모리 파편화 유발.
  - 해결 방안 : **서브셋 패턴** (Subset Pattern) 및 **버킷 패턴** (Bucket Pattern) 적용, 데이터 증가율에 따라 참조(ID 참조) 모델로 분리 및 양방향 참조 제한.
- 샤딩(Sharding) 키 선정 오류로 인한 데이터 및 트래픽 핫스팟 :
  - 한계점 : 단조 증가하는 타임스탬프나 카디널리티가 낮은 필드를 샤드 키로 지정하여 특정 샤드로 쓰기/읽기 부하가 집중되고 청크(Chunk) 마이그레이션 병목 초래.
  - 해결 방안 : 카디널리티가 높고 쓰기가 고르게 분산되는 **복합 샤드 키** (Compound Key) 또는 **해시 샤드 키** (Hashed Shard Key) 설계, 점보 청크(Jumbo Chunk) 방지 모니터링.
- WiredTiger 스토리지 엔진의 체크포인트 및 캐시 압박에 따른 **쓰기 스톨** (Write Stall) :
  - 한계점 : 대량 쓰기 워크로드에서 더티 캐시(Dirty Cache) 비율이 20%를 초과할 경우 백그라운드 스레드가 애플리케이션 쓰기 스레드를 차단하여 급격한 레이턴시 스파이크 발생.
  - 해결 방안 : WiredTiger 캐시 크기 최적화(`wiredTigerEngineRuntimeConfig`), **쓰기 관심사** (Write Concern: `w:1` vs `w:majority`) 워크로드별 분리, 고성능 NVMe(Non-Volatile Memory Express) SSD(Solid-State Drive) 적용.

## Ⅴ. 엔터프라이즈 MongoDB 운영을 위한 실무 제언

- **WiredTiger** 스토리지 엔진 메모리 튜닝 : MongoDB의 기본 WiredTiger 엔진은 가용 RAM(Random-Access Memory)의 약 50%를 자체 캐시로 점유하고 나머지는 OS(Operating System) 파일시스템 캐시로 활용하므로, 동일 서버에 타 프로세스를 함께 기동할 경우 OOM(Out of Memory) Killer로 인한 DB(Database) 비정상 종료를 방지하기 위해 `storage.wiredTiger.engineConfig.cacheSizeGB`를 명시적으로 고정해야 함.
- **샤드 키** (Shard Key)의 카디널리티 및 단조 증가 방지 : 타임스탬프나 `ObjectId`처럼 단조 증가(Monotonically Increasing)하는 키를 샤드 키로 지정하면 최신 데이터가 무조건 마지막 단일 샤드로만 인입되는 **쓰기 핫스팟** (Write Hotspot)이 발생하므로, 반드시 복합 해시 샤드 키(Hashed Shard Key)를 채택할 것을 제언함.
