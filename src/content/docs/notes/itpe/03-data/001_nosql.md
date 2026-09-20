---
title: "NoSQL"
author: "Codex"
date: "2026-09-20T19:29:12+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
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
  <div class="itpe-flow-node"><strong>업무 데이터·질의 특성</strong><small>입력: 질의 빈도 · 지연 허용치 · 정합성 수준</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>저장 모델 분기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>RDBMS</strong><span>판정: 엄격한 ACID · 복잡 조인 · 정규화 원장</span></div>
      <div class="itpe-flow-branch"><strong>NoSQL</strong><span>판정: BASE 기반 · Query-First 모델링 · 수평 확장</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>NoSQL 4대 저장 구조</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>KV</strong><span>처리: Key-Value 고속 단건 조회 · 세션·캐시</span></div>
      <div class="itpe-flow-branch"><strong>Doc</strong><span>처리: JSON/BSON 계층 문서 저장 · 카탈로그</span></div>
      <div class="itpe-flow-branch"><strong>Column</strong><span>처리: Row Key별 동적 열군 · 시계열·로그</span></div>
      <div class="itpe-flow-branch"><strong>Graph</strong><span>처리: Node-Edge-Property 관계 순회 · 추천·이상탐지</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Scale-Out 분산 서비스</strong><small>출력: 워크로드별 저장소와 일관성 정책</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- `NoSQL(Not Only SQL)`: 관계형 단일 모델 대신 질의 목적에 맞는 분산 저장 구조를 선택하는 데이터베이스 계열
- `BASE(Basically Available, Soft state, Eventual consistency)`: 분할 상황에서 가용성을 우선하고 복제본의 수렴을 관리하는 일관성 관점
- `Query-First`: 엔터티 관계보다 실제 접근 패턴을 먼저 고정하여 파티션과 집계 경계를 설계하는 방식
- `Polyglot Persistence`: 원장·세션·문서·관계 탐색을 각기 적합한 저장소에 배치하는 아키텍처 원칙

</details>

## 예상문제

> 대규모 비정형 데이터 처리 및 고가용성 분산 환경 구축을 위한 NoSQL의 개념과 4대 핵심 모델(Key-Value, Document, Column Family, Graph)의 특징을 비교하고, Query-First 모델링 5단계 절차 및 RDBMS와의 Polyglot Persistence 구축 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **컬럼 패밀리 DB(Column Family DB)** | 행 키(Row Key)와 동적 컬럼 패밀리 기반 대규모 쓰기·범위 스캔 특화 분산 NoSQL | Ⅲ 구조·유형 |
| **BASE 원칙** | Basically Available, Soft-state, Eventual consistency 중심의 가용성 절충 메커니즘 | Ⅱ 핵심 특징 |

## Ⅰ. 대규모 분산 환경의 목적형 데이터베이스, NoSQL의 개요

> NoSQL은 관계형 모델의 스키마 제약과 조인 병목을 해소하기 위해 질의 중심 분산 저장을 지원하며, 성패는 저장 모델보다 접근 패턴과 일관성 요구의 일치로 판정함.

- 정의: **NoSQL(Not Only SQL)**은 **Query-First 모델링**과 **수평 분할**로 목적형 데이터 모델을 분산 배치하는 비관계형 DBMS
- 목적: **Scale-Out** 처리량과 **가용성** 확보 → 대규모·가변 워크로드의 지연 통제

## Ⅱ. NoSQL의 4대 핵심 특징 및 메커니즘

> 유연한 스키마·수평 분산·비정규화는 조인 비용을 제거하지만 중복과 정합성 비용을 애플리케이션으로 이동시키므로 Aggregate 경계가 성패를 가름함.

| 특징 | 동작 원리 | 실무적 기여 |
|---|---|---|
| **유연한 스키마(Schema-less)** | 레코드 단위로 속성 구성을 동적으로 확장 | 무중단 데이터 구조 변경 및 개발 민첩성 확보 |
| **선형 수평 확장(Scale-Out)** | 파티션 키 기반 노드 간 데이터 자동 분산(Sharding) | 하드웨어 증설에 비례하는 쓰기·읽기 처리량 확장 |
| **비정규화 모델링(Query-First)** | 질의 패턴에 맞추어 연관 데이터를 단일 문서·열군에 중복 저장 | 분산 환경에서 비용이 큰 다중 노드 조인 원천 제거 |
| **BASE 일관성 절충** | Basically Available, Soft-state, Eventual consistency 적용 | CAP 이론상 네트워크 분할(P) 시 가용성(A) 우선 확보 |

## Ⅲ. 질의 목적에 따른 NoSQL 4대 저장 유형

> 질의 패턴이 단건·계층 문서·동적 열군·다단계 관계 순회 중 무엇인지가 모델 선택 기준이며, 제품 선호보다 주 접근 경로를 먼저 검증해야 함.

<div class="itpe-pipeline" role="img" aria-label="NoSQL 4대 데이터 모델 구조">
  <div class="itpe-pipeline-node"><strong>Key-Value</strong><small>처리: Key로 Value 단건 조회</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Document</strong><small>처리: ID로 JSON/BSON 문서 조회</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Column Family</strong><small>처리: Row Key로 열군 범위 조회</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>Graph</strong><small>처리: Edge를 따라 Node 관계 순회</small></div>
</div>

| 유형 | 데이터 저장 구조 | 적합 질의 패턴 | 대표 적용 분야 | 설계 핵심 요건 |
|---|---|---|---|---|
| **Key-Value** | 유일 Key에 임의 바이너리/문자열 매핑 | 단순 단건 Key 조회 및 저장 | 세션 스토리지, 인메모리 캐시, 장바구니 | 키 해시 분포 균등화 및 만료(TTL) 통제 |
| **Document** | 계층 구조의 JSON/BSON 문서 저장 | 복합 속성 검색 및 중첩 구조 조회 | 상품 카탈로그, CMS 콘텐츠 관리 | 단일 문서 크기(16MB 등) 한계 및 임베딩 vs 참조 판단 |
| **Column Family** | Row Key 아래 동적 Column 집합 관리 | 대규모 시계열 쓰기, 특정 열군 범위 검색 | 대용량 로그 수집, IoT 센서 데이터, 통계 집계 | 파티션 키(분산)와 클러스터링 키(정렬) 최적화 |
| **Graph** | Node(개체), Edge(관계), Property로 구성 | 재귀적·다단계 관계 순회(Traversal) | 소셜 네트워크 분석, 이상금융거래 탐지(FDS), 지식 그래프 | 노드 간 연결 밀도 관리 및 인덱스-프리 인접성 확보 |

## Ⅳ. NoSQL Query-First 모델링 5단계 절차

> 데이터 관계보다 애플리케이션의 Access Pattern을 먼저 고정하며, 각 단계의 산출물이 다음 단계의 파티션·복제 결정을 추적 가능하게 해야 함.

| 단계 | 활동 내용 | 핵심 산출물 |
|---|---|---|
| **1. 요구·SLA 정의** | 처리량(TPS), 허용 지연(Latency), 정합성 요구수준 분석 | 데이터/SLA 분류표 |
| **2. Access Pattern 식별** | 빈번한 읽기/쓰기 질의, 정렬 조건, 검색 파라미터 전수 도출 | 애플리케이션 질의 목록 |
| **3. Aggregate·모델 선정** | 원자적으로 읽고 쓰는 데이터 경계(Aggregate) 획정 및 모델 매핑 | 논리 데이터 모델 다이어그램 |
| **4. Partition·Index 설계** | 데이터 균등 분산을 위한 파티션 키, 복제본 수(RF), 보조 색인 수립 | 물리 스키마 정의서 |
| **5. 부하·정합성 검증** | 핫스팟 노드 발생 여부, 복제 지연(Replication Lag), 페일오버 검증 | 성능 및 정합성 테스트 결과서 |

## Ⅴ. RDBMS vs NoSQL 비교 및 Polyglot Persistence

> 금융 원장은 RDBMS의 ACID로, 대규모 사용자 트래픽은 NoSQL의 확장성으로 수용하되 도메인 간 정합성 경계를 명시해야 공존 구조가 안정됨.

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

> 핫 파티션·복제 지연·비정규화 불일치는 각각 키 분포·수렴 지연·중복 갱신에서 발생하므로 원인별 통제가 필요함.

- 적용 상황: 글로벌 이커머스 서비스의 초당 수만 건 트래픽 분산 처리

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **핫 파티션(Hot Partition)** | 특정 일자·범주 등 저카디널리티 키 사용 | 솔트(Salt) 값 추가, 복합 파티션 키 구성 | 노드 간 I/O 및 디스크 부하 균등 분산 |
| **데이터 불일치(Inconsistency)** | 비정규화 데이터 중복 저장 및 비동기 복제 | 이벤트 기반 CDC(Change Data Capture) 동기화 파이프라인 구축 | 분산 노드 간 최종 일관성 수렴 보장 |
| **오래된 데이터 읽기(Stale Read)** | 슬레이브 노드 복제 지연 발생 | Quorum Read/Write 정책($R + W > N$) 설정 | 읽기 시 최신 버전 데이터 반환 강제 |

## Ⅶ. 결론 및 기술사적 제언

> NoSQL의 성공은 기술 도입이 아니라 데이터 도메인 경계별 일관성 요구수준에 맞춘 Polyglot 아키텍처와 실패 시 복구 경로에 달려 있음.

- [핵심 통찰]: 모든 데이터를 NoSQL로 전환하려는 시도는 RDBMS의 강력한 트랜잭션 보장 능력을 포기하는 우를 범하며, 반대로 모든 워크로드를 RDBMS에 묶어두는 것은 클라우드 분산 확장의 이점을 차단함.
- 나라면: 데이터 도메인의 오류 비용과 SLA를 기준으로 '원장·정산=RDBMS, 캐시·세션=Key-Value, 상품·주문내역=Document, 추천=Graph'로 역할을 분리하고, 도메인 간 정합성은 Kafka와 Debezium을 활용한 트랜잭셔널 아웃박스 패턴(Transactional Outbox Pattern)으로 묶어 시스템 복원력을 완성하겠음.

### 실전 답안용 기술사적 제언

- 판정: 데이터 모델보다 도메인별 정합성·지연·장애 허용 수준의 명시 여부가 성패를 가름함
- 대안: 원장과 대규모 조회 영역을 분리하고 Outbox·CDC로 변경 이벤트를 연결함
- 검증: 핫 키, 복제 지연, 재처리 중복을 장애 주입과 정합성 대조로 확인함
- 효과: 저장소별 강점을 유지하면서 분산 불일치와 전면 전환 위험을 제한함

<div class="itpe-flow-map" role="img" aria-label="NoSQL 도입 제언의 문제 대안 판정 효과 흐름">
  <div class="itpe-flow-node"><strong>일괄 전환 위험</strong><small>문제: 원장 정합성과 접근 패턴의 혼재</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Polyglot 배치</strong><small>대안: 도메인별 저장소 · Outbox · CDC</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>장애 주입 검증</strong><small>판정: 지연·중복·수렴이 허용 범위인지 확인</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>점진 확장</strong><small>효과: 원장 보존 · 병목 분리 · 복구 경로 확보</small></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의 및 목적
- 정의: **NoSQL(Not Only SQL)**은 **Query-First 모델링**과 **수평 분할**로 목적형 데이터 모델을 분산 배치하는 비관계형 DBMS
- 목적: **Scale-Out** 처리량과 **가용성** 확보 → 대규모·가변 워크로드의 지연 통제

### 2. 핵심 메커니즘 / 체계
```text
SLA 정의 → Access Pattern → 모델 선정 → Partition/Replica → 부하 검증
              ├─ Key-Value / Document / Column Family / Graph
              └─ Sharding(Scale-Out) + Quorum($R + W > N$)
```
- Query-First 모델링을 통해 조인을 배제하고, 접근 경로에 최적화된 비정규화 저장을 수행함.

### 3. 실무 제언
- 원장성 데이터는 RDBMS의 ACID를 유지하고, 대규모 트랜래픽 영역에 NoSQL을 배치하는 Polyglot Persistence 및 CDC 기반 비동기 정합성 확보가 필수적임.

## 출제 이력과 검증 출처

- 출제 이력: 제133회 1교시 3번 "NoSQL유형과 모델링 절차를 설명하시오."
- 검증 출처: [MongoDB Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/), [Apache Cassandra Architecture](https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html)

## 학습 체크

- [ ] Ⅰ 개요: NoSQL의 정의와 목적을 Query-First·수평 분할·Scale-Out을 포함해 두 줄로 재현할 수 있는가?
- [ ] Ⅲ 저장 유형: Key-Value·Document·Column Family·Graph를 주 질의 패턴으로 비교할 수 있는가?
- [ ] Ⅳ 모델링: 5단계의 활동과 산출물을 한 쌍으로 연결할 수 있는가?
- [ ] Ⅵ 장애 대책: 핫 파티션·복제 지연·중복 갱신의 원인과 통제를 대응시킬 수 있는가?
- [ ] Ⅶ 제언: 저장소 분리부터 장애 주입 검증까지 판정·대안·효과 흐름을 그릴 수 있는가?

## 연결 토픽

- 이전 토픽: [자료처리·데이터 개요](./index.md)
- 연관 토픽: [샤딩](./045_sharding.md), [CAP·PACELC 이론](./113_cap_pacelc.md), [트랜잭션 격리 수준](./020_isolation_level.md)
- 다음 토픽: [데이터 가치평가·데이터 자산화](./002_data_valuation.md)
