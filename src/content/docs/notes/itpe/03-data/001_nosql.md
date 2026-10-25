---
title: "NoSQL(Not Only SQL)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- NoSQL(Not Only SQL), RDBMS(Relational Database Management System), CAP 정리, BASE, 최종 일관성(Eventual Consistency)
- 수평 확장(Scale-Out), 샤딩(Sharding), 복제(Replication), Quorum
- Key-Value, Document, Column-Family, Graph, Polyglot Persistence, ACID

## Ⅰ. NoSQL의 개요

- 핵심 요약 : 고정 스키마와 조인을 벗어나 수평 확장과 가용성을 우선하는 비관계형 분산 데이터베이스.
- 개념 : 관계형 모델 대신 키·문서·컬럼·그래프 등 유연한 데이터 모델로 대용량 데이터를 분산 저장·처리하는 비관계형 데이터베이스인 **NoSQL** (Not Only SQL).
- 배경 및 필요성 : 웹 규모 서비스의 폭증하는 트래픽과 비정형 데이터를 단일 고사양 서버의 수직 확장으로 감당하기 곤란하고, 스키마 변경이 잦은 반복 개발 환경이 확산.
- 주요 목적 : **CAP 정리** (CAP Theorem, 일관성(Consistency)·가용성(Availability)·분할 내성(Partition Tolerance)을 동시에 완전히 보장할 수 없다는 이론)의 전제 아래 가용성과 처리량을 우선하는 **BASE** (Basically Available, Soft-state, Eventual Consistency) 특성 확보.

## Ⅱ. NoSQL의 특징 및 장점

- 핵심 요약 : 스키마 유연성·수평 분산·조인 배제·최종 일관성의 설계 전환이 대량 처리 능력으로 연결.

1. 스키마 유연성 : 데이터 구조를 애플리케이션이 정의 → 필드 추가·변경에 대한 신속한 대응.
2. 수평 확장(Scale-Out) : 범용 서버를 노드 단위로 추가 → 저비용의 선형적 용량 확장. 데이터 분할은 **샤딩** (Sharding, 데이터를 여러 노드에 나누어 저장하는 방식), 가용성 확보는 **복제** (Replication, 같은 데이터를 여러 노드에 복사하는 방식)로 구현.
3. 조인 배제와 비정규화 : 조회 패턴에 맞춘 데이터 중복 저장 → 다중 테이블 조인 부하 제거와 응답 시간 단축.
4. 최종 일관성 : 갱신이 멈추면 복제본이 일치 상태로 수렴하는 **최종 일관성** (Eventual Consistency) 수용 → 일부 노드 장애에서도 서비스 지속.
5. 4대 데이터 모델 : Key-Value, Document, Column-Family, Graph의 용도별 특화 → 워크로드 적합도 향상.

## Ⅲ. NoSQL의 구조 (흐름)

- 핵심 요약 : 4대 데이터 모델의 용도별 분화와 샤딩·복제의 이중 구조.

```text
[ NoSQL 4대 데이터 모델 ]

Key-Value     : 캐시·세션 (Redis)
Document      : 문서·카탈로그 (MongoDB)
Column-Family : 로그·시계열 (Cassandra)
Graph         : 관계 탐색 (Neo4j)
   ↓ 용도별 조합 운영
Polyglot Persistence
```

```text
[ 샤딩과 복제의 이중 구조 ]

전체 데이터 (컬렉션)
   ↓ 샤딩 : 키 기반 분할
샤드 1 · 샤드 2 · 샤드 3
   ↓ 복제 : 샤드별 복제본
Primary + Replica 구성
```

- 4대 모델 구성요소 : Key-Value는 키와 값의 단순 매핑, Document는 JSON(JavaScript Object Notation) 문서 단위 저장, Column-Family는 행 키별 컬럼 집합 관리, Graph는 노드·간선·속성의 관계 표현.
- 정합성 제어 : 복제본의 읽기·쓰기 응답 수 기준인 **Quorum** 방식으로 일관성 수준 조절 → 성능과 정합성의 균형.

## Ⅳ. NoSQL과 RDBMS의 비교

- 핵심 요약 : 무결성 중심의 RDBMS와 확장성 중심의 NoSQL의 워크로드별 분담.

| 비교 축 | RDBMS | NoSQL |
| --- | --- | --- |
| 데이터 모델 | 정규화된 테이블과 관계 | 키·문서·컬럼·그래프 |
| 스키마 | 사전 정의된 고정 스키마 | 애플리케이션 정의의 유연 구조 |
| 일관성 모델 | **ACID** (Atomicity, Consistency, Isolation, Durability) 트랜잭션 | BASE 기반의 최종 일관성 |
| 확장 방식 | 수직 확장(Scale-Up) 중심 | 수평 확장(Scale-Out) 중심 |
| 질의 방식 | SQL(Structured Query Language)의 조인·집계 | 키 조회와 API 호출 중심 |
| 적합 워크로드 | 결제·원장 등 무결성 최우선 업무 | 실시간 인입·세션·비정형 데이터 |

- 선택 기준 : 복합 트랜잭션과 무결성이 최우선이면 RDBMS, 대량 인입과 유연 구조가 우선이면 NoSQL을 채택하고 목적별 저장소 조합인 **Polyglot Persistence** (업무 목적별로 여러 저장소를 조합하는 설계 방식)로 통합.

## Ⅴ. NoSQL의 한계와 방안

- 핵심 요약 : 읽기 불일치, 트랜잭션 부재, 샤드 편향을 정합성 수준 조정·업무 분리·키 설계로 일대일 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 최종 일관성의 읽기 불일치 | 복제본 반영 지연으로 직전 값 조회 가능 | Quorum 기준 조정, 정합성 민감 데이터는 강한 일관성 저장소로 분리 | 복제 지연 시간 |
| 다중 키 트랜잭션 부재 | 여러 키 갱신 시 애플리케이션 보상 로직 필요 | 트랜잭션 업무의 RDBMS 분리, 원자성 필요 데이터의 문서 내 중첩 구조화 | 트랜잭션 실패율 |
| 샤드 키 설계 편향 | 순차 증가 키의 특정 샤드 쏠림(핫스팟) | 복합·해시 기반 샤드 키 설계와 솔팅(Salting) 적용 | 샤드별 부하 편차 |

## Ⅵ. NoSQL 도입에 대한 기술사적 제언

- 핵심 요약 : 질의 패턴 중심 설계의 표준화, 저장소 선정 심의, 백업·복구 체계의 병행.
- 개발 조직 : 테이블 설계에 앞서 질의 패턴을 정의하는 접근을 설계 표준으로 명문화.
- 아키텍처 조직 : 업무 유형별 저장소 선정 기준과 다중 저장소 조합의 심의 절차를 거버넌스에 반영.
- 운영 조직 : 특정 시점 백업과 복제본 정합성 검증을 포함한 재해복구 절차 수립.

## Ⅶ. 결론

- 핵심 요약 : NoSQL은 CAP·BASE 원칙 위에서 수평 확장과 유연성을 제공하는 저장소 체계임.
- 업무의 무결성 요구와 확장 요구를 구분해 저장소를 배치하는 설계가 데이터 아키텍처의 기본형.
