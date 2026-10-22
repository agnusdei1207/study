---
title: "MongoDB"
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

**MongoDB**, **BSON**, **복제셋(Replica Set)**, **샤딩(Sharding)**, **임베딩/참조**, **WiredTiger**, **NoSQL**

## Ⅰ. 개요

- 핵심 요약 : **MongoDB**는 BSON 문서 포맷과 수평 확장·고가용성을 기본 내장한 문서 지향 NoSQL.
- 목적 : 동적 스키마·대규모 트래픽 환경의 유연한 데이터 저장.
- 배경 : RDBMS 엄격 DDL 제약 → 빈번한 구조 변경·대규모 트래픽 서비스 필요.
- 특징 : BSON, Replica Set, Sharding, 임베딩/참조 모델링.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **문서 지향·수평 확장·고가용성**으로 현대 웹/앱에 최적.
- **동적 스키마** : DDL 제약 없이 필드 자유 추가.
- **수평 확장** : Sharding으로 데이터 분산.
- **고가용성** : Replica Set 자동 페일오버.
- **임베딩** : 단일 문서 원자적 갱신, 조회 성능 극상.
- **풍부한 쿼리** : Aggregation Pipeline.

## Ⅲ. 복제셋·샤딩 흐름

- 핵심 요약 : **Replica Set(P-S-S)** 고가용성 + **Sharded Cluster** 수평 확장.
- mongos : 쿼리 라우터, 샤드 키 범위 확인.
- Config Server : 샤드 메타데이터 (3대 이상).
- Shard : 실제 데이터 분할 저장 (각 샤드도 Replica Set).

```text
[ MongoDB Replica Set (P-S-S) ]

[Primary] (쓰기/기본 읽기)
   /       \
  v         v
[Secondary 1] [Secondary 2]
   - Primary 장애 시 Raft 투표로 자동 승격
```

```text
[ MongoDB Sharded Cluster ]

[App] ---> [mongos (라우터)] <---> [Config Servers]
                  |
     +------------+------------+
     |                         |
     v                         v
[Shard A (Replica Set)]   [Shard B (Replica Set)]
(Chunk: 0~50만)           (Chunk: 50만~100만)
```

## Ⅳ. 임베딩 vs 참조 비교

- 핵심 요약 : **조회 성능·원자성·문서 크기** 트레이드오프.

| 항목 | 임베딩 (Embedded) | 참조 (Referenced) |
|---|---|---|
| 데이터 구조 | 부모 내 하위 배열 포함 | 별도 컬렉션 + _id 참조 |
| 조회 성능 | 단일 I/O 극상 | $lookup/다중 쿼리 |
| 원자성 | 단일 문서 원자적 갱신 | 다중 문서 트랜잭션 |
| 문서 크기 | 16MB 한계 위험 | 한계 자유 |
| 적합 관계 | 1:1, 유한 1:N | 1:다수(수천+), M:N |

## Ⅴ. 한계와 방안

- 핵심 요약 : **16MB 한계·핫스팟·Write Stall**을 서브셋/버킷·해시 샤드·WiredTiger 튜닝으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 16MB BSON 한계 초과 | 무제한 하위 배열 임베딩 | 서브셋/버킷 패턴, 참조 모델 분리 | 문서 크기 |
| 샤드 키 핫스팟 | 단조 증가 키로 쓰기 집중 | 복합/해시 샤드 키, 점보 청크 모니터링 | 샤드별 부하 |
| Write Stall | 더티 캐시 20% 초과로 쓰기 차단 | 캐시 크기 최적화, Write Concern 분리, NVMe | 쓰기 레이턴시 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **WiredTiger 튜닝·샤드 키 설계·모델링 패턴**으로 안정적 운영.
- WiredTiger : 캐시 크기 명시 고정, OOM 방지.
- 샤드 키 : 카디널리티 높고 고른 복합/해시 키, 단조 증가 회피.
- 모델링 : 증가율에 따른 임베딩/참조 선택, 서브셋/버킷 패턴.

## Ⅶ. 결론

- 핵심 요약 : MongoDB는 **문서 지향·수평 확장·고가용성**이 강점, 샤드 키·모델링이 핵심.
- 답안에는 Replica Set, Sharding, 임베딩/참조, 한계·대응을 연결.
- 참고 : [MongoDB Manual](https://www.mongodb.com/docs/manual/).