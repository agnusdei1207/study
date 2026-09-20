---
title: "NoSQL"
category: "03-data"
tags:
  - "NoSQL"
  - "QueryFirst"
  - "ScaleOut"
  - "BASE"
  - "Polyglot"
  - "Sharding"
date: "2026-09-20T23:50:43+09:00"
author: "Codex"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 요구에서 비관계형 저장소를 거쳐 NoSQL로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>비관계형 저장·수집</span>
  <strong>NoSQL</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 고정된 테이블 스키마와 조인(JOIN) 중심의 RDBMS 한계를 극복하기 위해, 질의 패턴(Query-First)에 맞추어 유연한 데이터 모델과 수평 분산 확장(Scale-Out)을 제공하는 비관계형 데이터베이스 시스템
- 메커니즘: SLA 정의 $\rightarrow$ 애플리케이션 접근 패턴(Access Pattern) 식별 $\rightarrow$ Aggregate 경계 및 4대 저장 모델(Key-Value, Document, Column, Graph) 선정 $\rightarrow$ 파티션/복제본(Sharding/Replica) 설계 $\rightarrow$ 부하 및 최종 일관성 검증
- 산출물: 논리 데이터 모델 다이어그램 · 물리 파티션 스키마 정의서 · 쿼럼(Quorum) 일관성 정책서 · CDC 기반 이벤트 동기화 파이프라인

<div class="itpe-flow-map" role="img" aria-label="NoSQL Query-First 모델링 및 분산 안정성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 업무 SLA 및 접근 패턴(Access Pattern) 식별</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>초당 트랜잭션(TPS), 지연 허용치, 빈번한 읽기/쓰기 쿼리 경로 전수 도출</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: Aggregate 경계 획정 및 4대 저장 모델 매핑</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>선정</strong><span>단건(Key-Value), 계층(Document), 시계열(Column), 관계망(Graph) 모델 매핑</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 샤딩(Sharding) 및 쿼럼(Quorum) 복제 설계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분산</strong><span>파티션 키 분산, 복제 계수(RF), 읽기/쓰기 쿼럼($R + W > N$) 설정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 분산 정합성 및 핫스팟 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>특정 노드에 트래픽이 쏠리지 않고(Hotspot 부재), 복제 지연 시 쿼럼 일관성을 유지하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Scale-Out 프로덕션 배포)</strong>
      <span>분산 클러스터 오픈 $\rightarrow$ 샤드 리밸런싱 및 실시간 지연 관제 적용</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (핫 파티션 / 정합성 왜곡)</strong>
      <span>배포 보류 $\rightarrow$ 파티션 키 솔팅(Salt) 추가 및 CDC/Outbox 비동기 보정 수립</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `NoSQL(Not Only SQL)`: 관계형 단일 모델 대신 질의 목적에 맞는 분산 저장 구조를 선택하는 비관계형 DBMS
- `BASE(Basically Available, Soft-state, Eventual consistency)`: 분할 상황에서 가용성을 우선하고 복제본의 수렴을 관리하는 일관성 모델
- `Query-First`: 엔터티 관계보다 실제 접근 패턴을 먼저 고정하여 파티션과 집계 경계를 설계하는 모델링 기법
- `Polyglot Persistence`: 원장·세션·문서·관계 탐색을 각기 적합한 저장소에 분리 배치하는 아키텍처 원칙
- `Quorum`: $R+W>N$으로 읽기·쓰기 복제본이 겹치게 하는 일관성 조정 방식. 시계 오차·복제 실패·충돌 해결 정책에 따라 최신성은 달라짐
- `CDC(Change Data Capture)`: 데이터베이스의 트랜잭션 로그를 실시간 감지하여 이기종 저장소로 이벤트를 전송·동기화하는 기술

</details>

## 예상문제

> 대규모 비정형 데이터 처리 및 고가용성 분산 환경 구축을 위한 NoSQL의 개념과 4대 핵심 모델(Key-Value, Document, Column Family, Graph)의 특징을 비교하고, Query-First 모델링 5단계 절차 및 RDBMS와의 Polyglot Persistence 구축 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **컬럼 패밀리 DB(Column Family DB)** | Row Key, 동적 컬럼 패밀리, 대규모 시계열 쓰기, 분산 NoSQL | Ⅲ·Ⅴ |
| **BASE 원칙** | Basically Available, Soft-state, Eventual consistency, 가용성 절충 | Ⅰ·Ⅱ |
| **Polyglot Persistence** | 업무 도메인별 저장소 분리, 트랜잭셔널 아웃박스, CDC 동기화 | Ⅴ·Ⅶ |

## Ⅰ. 대규모 분산 환경의 목적형 데이터베이스, NoSQL의 개요

> NoSQL은 관계형 모델의 스키마 제약과 조인 병목을 해소하기 위해 질의 중심 분산 저장을 지원하며, 성패는 저장 모델보다 접근 패턴과 일관성 요구의 일치로 판정함.

- 정의: 관계형 모델의 엄격한 테이블 스키마와 다중 조인(JOIN) 한계를 벗어나, **Query-First 모델링**과 **수평 분할(Sharding)**을 통해 대규모 트래픽을 처리하는 비관계형 DBMS
- 목적: **Scale-Out** 기반의 선형 처리량 확장과 고가용성 확보를 통한 서비스 지연 최소화
- 배경: 웹 2.0, 빅데이터, 마이크로서비스 확산에 따른 비정형 데이터의 폭발적 증가

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

```text
┌─────────────────┬──────────────────┬──────────────────┬─────────────────┐
│   Key-Value     │     Document     │  Column Family   │      Graph      │
│ (단건 고속 조회) │ (JSON 계층 구조) │ (시계열 범위스캔)│(다단계 관계순회)│
└─────────────────┴──────────────────┴──────────────────┴─────────────────┘
```

| 유형 | 데이터 저장 구조 | 적합 질의 패턴 | 대표 적용 분야 | 설계 핵심 요건 |
|---|---|---|---|---|
| **Key-Value** | 유일 Key에 임의 바이너리/문자열 매핑 | 단순 단건 Key 조회 및 저장 | 세션 스토리지, 인메모리 캐시, 장바구니 | 키 해시 분포 균등화 및 만료(TTL) 통제 |
| **Document** | JSON 등 계층 문서 저장 | 복합 속성·중첩 구조 조회 | 상품 카탈로그·CMS | 제품별 문서 크기·임베딩 제약 확인 |
| **Column Family** | Row Key 아래 동적 Column 집합 관리 | 대규모 시계열 쓰기, 특정 열군 범위 검색 | 대용량 로그 수집, IoT 센서 데이터, 통계 집계 | 파티션 키(분산)와 클러스터링 키(정렬) 최적화 |
| **Graph** | Node(개체), Edge(관계), Property로 구성 | 재귀적·다단계 관계 순회(Traversal) | 소셜 네트워크 분석, 이상금융거래 탐지(FDS) | 노드 간 연결 밀도 관리 및 인덱스-프리 인접성 확보 |

## Ⅳ. NoSQL Query-First 모델링 5단계 절차

> 데이터 관계보다 애플리케이션의 Access Pattern을 먼저 고정하며, 각 단계의 산출물이 다음 단계의 파티션·복제 결정을 추적 가능하게 해야 함.

```text
[1단계: 요구·SLA 정의] ──> [2단계: Access Pattern] ──> [3단계: 모델 선정] ──> [4단계: 파티션·색인] ──> [5단계: 부하·정합성]
  처리량(TPS), 지연한계     읽기/쓰기 쿼리 도출       Aggregate 경계 획정      파티션 키·Quorum 설계     핫스팟·복제지연 검증
```

1. **요구 및 SLA 정의**: 워크로드의 읽기/쓰기 비율, 초당 트랜잭션 수(TPS), 허용 지연시간 및 일관성 수준 분석
2. **Access Pattern 식별**: 엔티티 관계보다 화면과 비즈니스 로직에서 실제 호출되는 쿼리 경로와 파라미터를 전수 식별
3. **Aggregate 및 모델 선정**: 한 번에 원자적으로 읽고 쓰는 데이터 묶음(Aggregate)을 정의하고 4대 모델 매핑
4. **파티션 및 색인 설계**: 노드 간 균등 부하 분산을 위한 파티션 키 설정 및 보조 인덱스 최소화 설계
5. **부하 및 정합성 검증**: 시뮬레이션 테스트를 통해 특정 노드 쏠림(Hotspot)과 네트워크 분할 시 복제 수렴 속도 검증

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

## Ⅵ. NoSQL 문제점·대응책

> 분산 저장소 도입 시 수반되는 핫스팟, 복제 지연, 데이터 불일치 위험을 사전에 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 특정 노드 트래픽 집중 (Hot Partition) | 저카디널리티 키에 랜덤 솔트(Salt) 추가 및 복합 파티션 키 설계 | 클러스터 노드 간 CPU 및 디스크 I/O 균등 분산 달성 |
| 복제 지연으로 인한 옛 데이터 읽기 | 일관성 수준·Quorum·충돌 해결 정책 설정 | 요구한 최신성과 가용성 균형 |
| 비정규화 중복 데이터 간 불일치 | 트랜잭셔널 아웃박스 패턴 및 Kafka-Debezium CDC 동기화 파이프라인 구축 | 분산 이종 저장소 간 최종 일관성(Eventual Consistency) 신속 수렴 |
| 스키마 부재로 인한 데이터 오염 | 애플리케이션 계층 유효성 검증(Schema Validation) 및 버전 태깅 강제 | 불완전한 JSON 데이터 유입 차단 및 하위 호환성 유지 |

## Ⅶ. 기술사적 제언: 일관성과 가용성의 균형 잡힌 Polyglot 설계

> NoSQL의 성공은 기술 도입이 아니라 데이터 도메인 경계별 일관성 요구수준에 맞춘 Polyglot 아키텍처와 실패 시 복구 경로에 달려 있음.

### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 모든 데이터를 NoSQL로 전환하려는 시도는 RDBMS의 강력한 트랜잭션 보장 능력을 포기하는 우를 범하며, 반대로 모든 워크로드를 RDBMS에 묶어두는 것은 클라우드 분산 확장의 이점을 차단함.
- `나라면`: 데이터 도메인의 오류 비용과 SLA를 기준으로 '원장·정산=RDBMS, 캐시·세션=Key-Value, 상품·주문내역=Document, 추천=Graph'로 역할을 분리하고, 도메인 간 정합성은 Kafka와 Debezium을 활용한 트랜잭셔널 아웃박스 패턴(Transactional Outbox Pattern)으로 묶어 시스템 복원력을 완성하겠음.

### 실전 답안용 기술사적 제언
- 판정: 데이터 모델보다 도메인별 정합성·지연·장애 허용 수준의 명시 여부가 성패를 가름함
- 대안: 원장과 대규모 조회 영역을 분리하고 Outbox·CDC로 변경 이벤트를 연결함
- 검증: 핫 키, 복제 지연, 재처리 중복을 카오스 엔지니어링 장애 주입과 정합성 대조로 확인함
- 효과: 저장소별 강점을 유지하면서 분산 불일치와 전면 전환 위험을 제한함

```text
[현행 한계] ─────────> [개선 방안] ─────────> [검증 기준] ─────────> [실행 효과]
일괄 전환 위험         Polyglot 저장소 분리   쿼럼 일관성 검증        원장 ACID 보존
접근 패턴 혼재         CDC/Outbox 파이프라인  장애 주입(Chaos) 시험   선형 Scale-Out 달성
```

## 1교시 10점 답안 발췌

```text
1. NoSQL의 정의 및 목적
- 정의: 고정 스키마와 조인을 배제하고, 접근 패턴(Query-First)에 맞춰 유연한 데이터 모델과 수평 확장을 제공하는 비관계형 DBMS
- 목적: Scale-Out 기반 대규모 트랜래픽 수용 및 고가용성(BASE) 확보

2. 핵심 메커니즘 및 4대 저장 유형
┌─────────────────────────────────────────────────────────────┐
│ Query-First 모델링: SLA 정의 → Access Pattern → 모델 선정  │
├───────────────┬─────────────────────────────────────────────┤
│ Key-Value     │ 단건 고속 조회, 인메모리 캐시, 세션 관리    │
│ Document      │ JSON/BSON 계층 구조, 상품 카탈로그          │
│ Column Family │ Row Key 기반 동적 열군, 대규모 시계열 로그  │
│ Graph         │ Node-Edge-Property 관계망 순회, FDS 탐지    │
└───────────────┴─────────────────────────────────────────────┘

3. 분산 리스크 통제 대책
- 핫 파티션 방지: 복합 파티션 키 및 솔트(Salt) 기법 적용
- 일관성 보장: Quorum 정책($R + W > N$) 및 CDC 기반 Eventual Consistency 수렴
```

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제133회 확인 · 제123회는 KPC 보조자료이며 공식 원문 미확보
- **검증 출처**: [MongoDB Data Modeling Guide](https://www.mongodb.com/docs/manual/data-modeling/), [Apache Cassandra Architecture Documentation](https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html)

## 학습 체크

- [ ] [Ⅰ 개요]: NoSQL의 정의와 목적을 Query-First·수평 분할·Scale-Out을 포함해 정확히 기술하였는가?
- [ ] [Ⅲ 저장 유형]: Key-Value, Document, Column Family, Graph 4대 모델의 특성을 비교하였는가?
- [ ] [Ⅳ 모델링]: Query-First 5단계 절차(SLA $\rightarrow$ Access Pattern $\rightarrow$ 모델 $\rightarrow$ 파티션 $\rightarrow$ 검증)를 제시하였는가?
- [ ] [Ⅵ 통제]: 핫 파티션, 복제 지연, 데이터 불일치에 대한 3단 위험 대책을 기술하였는가?

## 연결 토픽

- [샤딩](./045_sharding.md) · [CAP·PACELC 이론](./113_cap_pacelc.md) · [트랜잭션 격리 수준](./020_isolation_level.md) · [데이터 가치평가](./002_data_valuation.md)
