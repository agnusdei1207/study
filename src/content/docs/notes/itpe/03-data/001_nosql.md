---
title: "NoSQL"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 요구에서 비관계형 저장소를 거쳐 NoSQL로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>비관계형 저장·수집</span>
  <strong>NoSQL</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 고정 스키마와 조인 중심 관계형 모델을 탈피하여, 질의 패턴에 맞춘 분산 저장으로 수평 확장성과 가용성을 보장하는 비관계형 DBMS
- 유형: Key-Value, Document, Column Family, Graph 4대 모델
- 절차: `업무·SLA 분석 → Access Pattern 정의 → 데이터 모델 선택 → Partition/Replica 설계 → 부하·정합성 검증`

<div class="itpe-flow-map" role="img" aria-label="질의 특성에 따른 RDBMS와 NoSQL 모델 분기 흐름">
  <div class="itpe-flow-node"><strong>업무 데이터·질의 특성</strong></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>저장 모델 분기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>RDBMS</strong><span>엄격한 ACID · 복잡 조인 · 정규화 원장</span></div>
      <div class="itpe-flow-branch"><strong>NoSQL</strong><span>BASE 기반 · Query-First 모델링 · 수평 확장</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>NoSQL 4대 저장 구조</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>KV</strong><span>Key-Value 고속 단건 조회 (세션·캐시)</span></div>
      <div class="itpe-flow-branch"><strong>Doc</strong><span>JSON/BSON 계층 문서 저장 (카탈로그)</span></div>
      <div class="itpe-flow-branch"><strong>Column</strong><span>Row Key별 동적 열군 (시계열·로그)</span></div>
      <div class="itpe-flow-branch"><strong>Graph</strong><span>Node-Edge-Property 관계 순회 (추천·이상탐지)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Scale-Out 분산 서비스</strong></div>
</div>

## 예상문제

> 대규모 비정형 데이터 처리 및 고가용성 분산 환경 구축을 위한 NoSQL의 개념과 4대 핵심 모델(Key-Value, Document, Column Family, Graph)의 특징을 비교하고, Query-First 모델링 5단계 절차 및 RDBMS와의 Polyglot Persistence 구축 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **컬럼 패밀리 DB(Column Family DB)** | 행 키(Row Key)와 동적 컬럼 패밀리 기반 대규모 쓰기·범위 스캔 특화 분산 NoSQL | Ⅲ 구조·유형 |
| **BASE 원칙** | Basically Available, Soft-state, Eventual consistency 중심의 가용성 절충 메커니즘 | Ⅱ 핵심 특징 |

## Ⅰ. 대규모 분산 환경의 목적형 데이터베이스, NoSQL의 개요

> **한줄 요약:** NoSQL은 관계형 모델의 스키마 제약과 조인 병목을 해소하기 위해 질의 중심 분산 저장을 지원하는 데이터베이스 체계임.

- 정의: Key-Value, Document, Column Family, Graph 등의 유연한 데이터 모델을 채택하고, BASE 철학과 샤딩을 통해 Scale-Out 확장을 달성하는 비관계형 DBMS
- 등장 배경: 대규모 트래픽 환경에서 단일 RDBMS의 수직적 확장(Scale-Up) 한계, 스키마 마이그레이션 다운타임, 다중 테이블 조인에 따른 I/O 병목 돌파 필요
- 핵심 가치: 사전 스키마 정의 없이 유연한 데이터 수용, 파티션 분할을 통한 선형적 처리량 증가, 분산 복제를 통한 고가용성 보장

## Ⅱ. NoSQL의 4대 핵심 특징 및 메커니즘

> **한줄 요약:** 유연한 스키마, 수평 분산, 비정규화 조인 제거, BASE 기반 일관성 조절로 성능을 극대화함.

| 특징 | 동작 원리 | 실무적 기여 |
|---|---|---|
| **유연한 스키마(Schema-less)** | 레코드 단위로 속성 구성을 동적으로 확장 | 무중단 데이터 구조 변경 및 개발 민첩성 확보 |
| **선형 수평 확장(Scale-Out)** | 파티션 키 기반 노드 간 데이터 자동 분산(Sharding) | 하드웨어 증설에 비례하는 쓰기·읽기 처리량 확장 |
| **비정규화 모델링(Query-First)** | 질의 패턴에 맞추어 연관 데이터를 단일 문서·열군에 중복 저장 | 분산 환경에서 비용이 큰 다중 노드 조인 원천 제거 |
| **BASE 일관성 절충** | Basically Available, Soft-state, Eventual consistency 적용 | CAP 이론상 네트워크 분할(P) 시 가용성(A) 우선 확보 |

## Ⅲ. 질의 목적에 따른 NoSQL 4대 저장 유형

> **한줄 요약:** 질의 패턴이 단건, 계층 문서, 동적 열군, 다단계 관계 순회인지에 따라 최적 모델을 선택함.

<div class="itpe-pipeline" role="img" aria-label="NoSQL 4대 데이터 모델 구조">
  <div class="itpe-pipeline-node"><strong>Key-Value</strong><small>Key ─▶ Value</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Document</strong><small>ID ─▶ {JSON/BSON}</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Column Family</strong><small>Row Key ─▶ [Col Families]</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Graph</strong><small>Node ─[Edge]─▶ Node</small></div>
</div>

| 유형 | 데이터 저장 구조 | 적합 질의 패턴 | 대표 적용 분야 | 설계 핵심 요건 |
|---|---|---|---|---|
| **Key-Value** | 유일 Key에 임의 바이너리/문자열 매핑 | 단순 단건 Key 조회 및 저장 | 세션 스토리지, 인메모리 캐시, 장바구니 | 키 해시 분포 균등화 및 만료(TTL) 통제 |
| **Document** | 계층 구조의 JSON/BSON 문서 저장 | 복합 속성 검색 및 중첩 구조 조회 | 상품 카탈로그, CMS 콘텐츠 관리 | 단일 문서 크기(16MB 등) 한계 및 임베딩 vs 참조 판단 |
| **Column Family** | Row Key 아래 동적 Column 집합 관리 | 대규모 시계열 쓰기, 특정 열군 범위 검색 | 대용량 로그 수집, IoT 센서 데이터, 통계 집계 | 파티션 키(분산)와 클러스터링 키(정렬) 최적화 |
| **Graph** | Node(개체), Edge(관계), Property로 구성 | 재귀적·다단계 관계 순회(Traversal) | 소셜 네트워크 분석, 이상금융거래 탐지(FDS), 지식 그래프 | 노드 간 연결 밀도 관리 및 인덱스-프리 인접성 확보 |

## Ⅳ. NoSQL Query-First 모델링 5단계 절차

> **한줄 요약:** 데이터 관계가 아닌 애플리케이션의 접근 패턴(Access Pattern)을 먼저 도출하여 역방향으로 저장 구조를 설계함.

| 단계 | 활동 내용 | 핵심 산출물 |
|---|---|---|
| **1. 요구·SLA 정의** | 처리량(TPS), 허용 지연(Latency), 정합성 요구수준 분석 | 데이터/SLA 분류표 |
| **2. Access Pattern 식별** | 빈번한 읽기/쓰기 질의, 정렬 조건, 검색 파라미터 전수 도출 | 애플리케이션 질의 목록 |
| **3. Aggregate·모델 선정** | 원자적으로 읽고 쓰는 데이터 경계(Aggregate) 획정 및 모델 매핑 | 논리 데이터 모델 다이어그램 |
| **4. Partition·Index 설계** | 데이터 균등 분산을 위한 파티션 키, 복제본 수(RF), 보조 색인 수립 | 물리 스키마 정의서 |
| **5. 부하·정합성 검증** | 핫스팟 노드 발생 여부, 복제 지연(Replication Lag), 페일오버 검증 | 성능 및 정합성 테스트 결과서 |

## Ⅴ. RDBMS vs NoSQL 비교 및 Polyglot Persistence

> **한줄 요약:** 금융 원장은 RDBMS의 ACID로, 대규모 사용자 트래픽은 NoSQL의 확장성으로 수용하는 상호보완적 공존 구조를 취함.

| 비교 기준 | RDBMS | NoSQL |
|---|---|---|
| **데이터 모델** | 정형 릴레이션 테이블 (정규화 기반) | Key-Value, Document, Column Family, Graph (비정규화) |
| **트랜잭션 특성** | 다중 레코드·다중 테이블 엄격한 ACID 보장 | 단일 Aggregate 단위 원자성, BASE 중심 최종 일관성 |
| **확장 메커니즘** | Scale-Up(수직 확장), Read Replica 분산 | Sharding 기반 Scale-Out(수평 분산 확장) |
| **질의 방식** | 표준 SQL, 다중 테이블 복합 JOIN 지원 | 목적형 API, 단일 키 질의, 제한된 조인 연산 |
| **스키마 변경** | 엄격한 DDL 적용, 테이블 락 위험 | 무중단 동적 필드 추가 (Schema Flexibility) |

```text
[Polyglot Persistence 아키텍처]
┌────────────────────────────────────────────────────────┐
│                   API 게이트웨이 / MSA                 │
└──────┬───────────────┬─────────────────┬───────────────┘
       ▼               ▼                 ▼
[주문·결제 원장]   [장바구니·세션]    [상품 카탈로그]
   RDBMS            Key-Value          Document
 (Strict ACID)      (Low Latency)   (Schema Flexibility)
```

## Ⅵ. 실무 고려사항 및 장애 대책

> **한줄 요약:** 핫 파티션, 복제 지연, 비정규화 데이터 불일치를 파티션 키 설계와 CDC 기반 동기화로 방어함.

- 적용 상황: 글로벌 이커머스 서비스의 초당 수만 건 트래픽 분산 처리

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **핫 파티션(Hot Partition)** | 특정 일자·범주 등 저카디널리티 키 사용 | 솔트(Salt) 값 추가, 복합 파티션 키 구성 | 노드 간 I/O 및 디스크 부하 균등 분산 |
| **데이터 불일치(Inconsistency)** | 비정규화 데이터 중복 저장 및 비동기 복제 | 이벤트 기반 CDC(Change Data Capture) 동기화 파이프라인 구축 | 분산 노드 간 최종 일관성 수렴 보장 |
| **오래된 데이터 읽기(Stale Read)** | 슬레이브 노드 복제 지연 발생 | Quorum Read/Write 정책($R + W > N$) 설정 | 읽기 시 최신 버전 데이터 반환 강제 |

## Ⅶ. 결론 및 기술사적 제언

> **한줄 요약:** NoSQL의 성공은 기술 도입이 아니라 데이터 도메인 경계별 일관성 요구수준에 맞춘 Polyglot 아키텍처 설계에 달려 있음.

- [핵심 통찰]: 모든 데이터를 NoSQL로 전환하려는 시도는 RDBMS의 강력한 트랜잭션 보장 능력을 포기하는 우를 범하며, 반대로 모든 워크로드를 RDBMS에 묶어두는 것은 클라우드 분산 확장의 이점을 차단함.
- 나라면: 데이터 도메인의 오류 비용과 SLA를 기준으로 '원장·정산=RDBMS, 캐시·세션=Key-Value, 상품·주문내역=Document, 추천=Graph'로 역할을 분리하고, 도메인 간 정합성은 Kafka와 Debezium을 활용한 트랜잭셔널 아웃박스 패턴(Transactional Outbox Pattern)으로 묶어 시스템 복원력을 완성하겠음.

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- NoSQL은 유연한 스키마, 수평 확장성(Scale-Out), 고가용성을 목표로 Key-Value, Document, Column Family, Graph 등 목적형 비관계형 데이터 모델을 채택한 분산 데이터베이스 체계임.

### 2. 핵심 메커니즘 / 체계
```text
SLA 정의 → Access Pattern → 모델 선정 → Partition/Replica → 부하 검증
              ├─ Key-Value / Document / Column Family / Graph
              └─ Sharding(Scale-Out) + Quorum($R + W > N$)
```
- Query-First 모델링을 통해 조인을 배제하고, 접근 경로에 최적화된 비정규화 저장을 수행함.

### 3. 차별화 제언
- 원장성 데이터는 RDBMS의 ACID를 유지하고, 대규모 트랜래픽 영역에 NoSQL을 배치하는 Polyglot Persistence 및 CDC 기반 비동기 정합성 확보가 필수적임.

## 출제 이력과 검증 출처

- 출제 이력: 제133회 정보관리기술사 기출, 제128·124·123회 KPC 모의고사
- 검증 출처: 한국데이터산업진흥원(K-DATA) DMBOK 2.0, Apache Cassandra/MongoDB Architecture Documentation

## 학습 체크

- [ ] NoSQL의 4대 유형(Key-Value, Document, Column Family, Graph)의 구조와 질의 특성을 비교할 수 있는가?
- [ ] Query-First 모델링 5단계 절차를 제시하고 RDBMS 모델링과의 차이를 설명할 수 있는가?
- [ ] 핫 파티션 및 복제 지연에 대한 원인과 Quorum/CDC 기반 해결책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [자료처리·데이터 개요](./index.md)
- 연관 토픽: [샤딩](./045_sharding.md), [CAP·PACELC 이론](./113_cap_pacelc.md), [트랜잭션 격리 수준](./020_isolation_level.md)
- 다음 토픽: [데이터 가치평가·데이터 자산화](./002_data_valuation.md)
