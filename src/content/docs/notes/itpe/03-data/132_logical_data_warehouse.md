---
title: "논리적 DW 아키텍처"
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

## Ⅰ. 유연한 데이터 분석 환경을 위한 논리적 DW 아키텍처 개요

### 가. 논리적 DW 아키텍처(Logical Data Warehouse Architecture)의 정의
- **논리적 DW(Data Warehouse) 아키텍처** : 정형 비즈니스 데이터(EDW, Enterprise Data Warehouse), 빅데이터 레이크(Hadoop/S3), 실시간 이벤트 스트림(Kafka), 클라우드 SaaS(Software as a Service) 데이터 등 분산되고 이질적인 저장소들을 하나의 논리적 **데이터 패브릭** (Data Fabric)으로 결합하여, 사용자에게 단일한 논리적 액세스 지점을 제공하는 전사 데이터 플랫폼 아키텍처.
- 모놀리식 단일 저장소의 한계를 극복하고 아키텍처의 민첩성(Agility)과 비용 효율성을 동시에 달성함.

---

## Ⅱ. 논리적 DW 아키텍처의 4대 핵심 빌딩 블록

```text
[ 논리적 DW 아키텍처 4대 구성 블록 ]
+-------------------------------------------------------------------------+
| [1. 서비스 및 분석 소비 계층]                                            |
| - 셀프서비스 BI, Ad-hoc 대화형 SQL, 머신러닝 피처 서빙                  |
+-------------------------------------------------------------------------+
| [2. 연합 쿼리 및 가상화 계층 (Federated Execution & Semantic Layer)]    |
| - 분산 옵티마이저, 푸시다운(Pushdown), 데이터 계보(Lineage), 캐싱       |
+-------------------------------------------------------------------------+
| [3. 데이터 거버넌스 및 보안 계층]                                        |
| - RBAC/ABAC 단일 보안 정책 강제, 데이터 카탈로그, PII 마스킹             |
+-------------------------------------------------------------------------+
| [4. 이종 분산 스토리지 계층]                                             |
| - 엔터프라이즈 DW | 클라우드 객체 스토리지 | NoSQL/시계열 | 실시간 스트림 |
+-------------------------------------------------------------------------+
```

### 가. 블록별 핵심 기술 사양

| 구성 블록 | 핵심 기술 컴포넌트 | 담당 기능 및 아키텍처 역할 |
| :--- | :--- | :--- |
| **연합 쿼리 엔진** | Trino, Apache Calcite, Starburst | 이종 DBMS(Database Management System) 간의 SQL(Structured Query Language) 문법 차이를 추상화하고 최적의 분산 실행 계획 수립 |
| **의미 계층 (Semantic)** | Cube.js, dbt Semantic Layer | 비즈니스 메트릭(매출, 활성 유저 등)의 계산 공식을 중앙 단일화하여 지표 일관성 확보 |
| **통합 보안 게이트웨이** | Apache Ranger, Immuta | 저장소 위치와 무관하게 사용자 역할에 따른 전사 동적 컬럼 마스킹 및 행 수준 보안(RLS, Row-Level Security) 강제 |
| **고속 버퍼/캐시** | Alluxio, Apache Arrow Flight | 원격 스토리지(S3(Simple Storage Service) 등)의 읽기 지연을 극복하기 위한 분산 인메모리 티어링 |

---

## Ⅲ. 쿼리 최적화의 핵심: 코스트 기반 푸시다운(CBO Pushdown)

### 가. 쿼리 푸시다운 메커니즘

```text
[ 비효율적 가상화 (전체 데이터 네트워크 전송) ]
[LDW Engine] <=== (1억 건 전체 테이블 전송) === [Oracle DW: 1억 건]
- LDW 엔진 메모리 폭발, 네트워크 포화

[ 쿼리 푸시다운 적용 (스마트 최적화) ]
[LDW Engine] ---> [WHERE date >= '2026-01-01' 집계 푸시다운] ---> [Oracle DW]
             <=== (집계 결과 1,000건만 전송) <==================+
```

---

## Ⅳ. 논리적 DW 아키텍처 구축 시 주요 한계점 및 해결 방안

- 이종 엔진 간 연산 특성 차이로 인한 분산 쿼리 최적화기(Optimizer)의 한계 :
  - 한계점 : Presto, Trino, Denodo 등 데이터 가상화 엔진이 각 원천 소스(RDBMS(Relational Database Management System), 객체 스토리지, NoSQL(Not Only SQL))의 인덱스, 통계정보, 함수 지원 여부를 완벽히 반영하지 못해 비효율적 풀 스캔 발생.
  - 해결 방안 : 커넥터별 통계정보 수집기(Catalog Stats Collector) 고도화, **동적 파티션 프루닝** (Dynamic Partition Pruning) 및 **런타임 필터링** (Runtime Filtering) 엔진 활성화.
- 글로벌 데이터 보안 및 거버넌스(접근 제어) 정책의 일관성 보장 난제 :
  - 한계점 : 소스 시스템마다 제각각인 보안 권한 모델(RBAC(Role-Based Access Control), ABAC(Attribute-Based Access Control))을 논리적 가상화 레이어에서 단일화하여 적용할 때 데이터 누수(Data Leakage) 및 감사 추적 단절 발생.
  - 해결 방안 : 전사 통합 거버넌스 솔루션(Apache Ranger, Immuta) 연계를 통한 컬럼 레벨 마스킹 및 **행 레벨 필터링** (Row-level Security) 중앙 통제.
- 복잡한 비즈니스 로직 연산 시 가상화 서버 **메모리 고갈** (OOM, Out of Memory) :
  - 한계점 : 대규모 정렬, 윈도우 함수, 다중 조인이 포함된 무거운 쿼리가 가상화 코디네이터 노드로 집중될 경우 스필(Spill to Disk) 또는 OOM 크래시 빈발.
  - 해결 방안 : **워크로드 관리** (WLM: Workload Management) 기반 쿼리 리소스 쿼터제 시행, 무거운 집계 워크로드는 dbt 기반 물리적 ELT(Extract, Load, Transform) 테이블 생성으로 유연한 하이브리드 운영.

## Ⅴ. 성공적인 논리적 DW 구축을 위한 실무 제언

- 데이터 캐싱 계층의 정교한 **무효화** (Invalidation) 전략 : 분산 쿼리 응답 속도를 높이기 위해 적용한 가상화 캐시가 원천 시스템의 갱신 사항을 제때 반영하지 못하면 분석 데이터 불일치가 발생하므로, **CDC(Change Data Capture)** (Debezium) 이벤트를 수신하여 원천 데이터 변경 시 해당 논리 뷰 캐시만 즉시 무효화하는 이벤트 기반 캐시 제어를 구현해야 함.
- **Data Mesh** 거버넌스와의 연계 : 논리적 DW 아키텍처는 기술적 가상화에 그치지 않고, 각 도메인 팀이 자체 데이터를 '**데이터 제품** (Data as a Product)'으로 등록하고 가상화 계층을 통해 전사 공유하는 페더레이션 거버넌스(Data Mesh)의 기술적 실행 플랫폼으로 포지셔닝할 것을 제언함.
