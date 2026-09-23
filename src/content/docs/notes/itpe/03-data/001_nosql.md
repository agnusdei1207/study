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
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
extra:
  model: "GPT-6"
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
---

## 1교시 예상문제 (10점)

> NoSQL의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

```text
1. NoSQL의 정의 및 목적
- 정의: 고정 스키마와 조인을 배제하고, 접근 패턴(Query-First)에 맞춰 유연한 데이터 모델과 수평 확장을 제공하는 비관계형 DBMS
- 목적: Scale-Out 기반 대규모 트래픽 수용 및 고가용성(BASE) 확보

2. 핵심 메커니즘 및 4대 저장 유형
- Query-First 모델링: SLA 정의 → Access Pattern → 모델 선정 → 파티션/쿼럼 설계
- 4대 저장 유형:
  · Key-Value: 단건 초고속 조회, 인메모리 캐시, 세션 관리 (Redis)
  · Document: JSON/BSON 계층 구조, 중첩 속성 인덱싱, 상품 카탈로그 (MongoDB)
  · Column Family: Row Key 기반 동적 열군, 대규모 시계열 로그 (Cassandra)
  · Graph: Node-Edge-Property 관계망 순회, FDS 탐색 (Neo4j)

3. 분산 리스크 통제 대책
- 핫 파티션 방지: 복합 파티션 키 및 솔트(Salt) 기법 적용으로 I/O 분산
- 일관성 보장: Quorum 정책(R + W > N) 및 CDC 기반 Eventual Consistency 수렴
```
---

### 핵심 관계

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **컬럼 패밀리 DB(Column Family DB)** | Row Key, 동적 컬럼 패밀리, 대규모 시계열 쓰기, 분산 NoSQL | Ⅲ·Ⅴ |
| **BASE 원칙** | Basically Available, Soft-state, Eventual consistency, 가용성 절충 | Ⅰ·Ⅱ |
| **Polyglot Persistence** | 업무 도메인별 저장소 분리, 트랜잭셔널 아웃박스, CDC 동기화 | Ⅴ·Ⅶ |

---

## 2~4교시 예상문제 (25점)

> 대규모 비정형 데이터 처리 및 고가용성 분산 환경 구축을 위한 NoSQL의 개념과 4대 핵심 모델(Key-Value, Document, Column Family, Graph)의 특징을 비교하고, Query-First 모델링 5단계 절차 및 RDBMS와의 Polyglot Persistence 구축 방안을 제시하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **컬럼 패밀리 DB(Column Family DB)** | Row Key, 동적 컬럼 패밀리, 대규모 시계열 쓰기, 분산 NoSQL | Ⅲ·Ⅴ |
| **BASE 원칙** | Basically Available, Soft-state, Eventual consistency, 가용성 절충 | Ⅰ·Ⅱ |
| **Polyglot Persistence** | 업무 도메인별 저장소 분리, 트랜잭셔널 아웃박스, CDC 동기화 | Ⅴ·Ⅶ |

### Ⅰ. 대규모 분산 환경의 목적형 데이터베이스, NoSQL의 개요

> NoSQL은 관계형 모델의 스키마 제약과 조인 병목을 해소하기 위해 질의 중심 분산 저장을 지원하며, 성패는 저장 모델보다 접근 패턴과 일관성 요구의 일치로 판정함.

- 정의: 관계형 모델의 엄격한 테이블 스키마와 다중 조인(JOIN) 한계를 벗어나, **Query-First 모델링**과 **수평 분할(Sharding)**을 통해 대규모 트래픽을 처리하는 비관계형 DBMS
- 목적: **Scale-Out** 기반의 선형 처리량 확장과 고가용성 확보를 통한 서비스 지연 최소화
- 배경: 웹 2.0, 빅데이터, 마이크로서비스 확산에 따른 비정형 데이터의 폭발적 증가

### Ⅱ. NoSQL의 4대 핵심 특징 및 메커니즘

> 유연한 스키마·수평 분산·비정규화는 조인 비용을 제거하지만 중복과 정합성 비용을 애플리케이션으로 이동시키므로 Aggregate 경계가 성패를 가름함.

| 특징 | 동작 원리 | 실무적 기여 |
|---|---|---|
| **유연한 스키마(Schema-less)** | 레코드 단위로 속성 구성을 동적으로 확장 | 무중단 데이터 구조 변경 및 개발 민첩성 확보 |
| **선형 수평 확장(Scale-Out)** | 파티션 키 기반 노드 간 데이터 자동 분산(Sharding) | 하드웨어 증설에 비례하는 쓰기·읽기 처리량 확장 |
| **비정규화 모델링(Query-First)** | 질의 패턴에 맞추어 연관 데이터를 단일 문서·열군에 중복 저장 | 분산 환경에서 비용이 큰 다중 노드 조인 원천 제거 |
| **BASE 일관성 절충** | Basically Available, Soft-state, Eventual consistency 적용 | CAP 이론상 네트워크 분할(P) 시 가용성(A) 우선 확보 |

### Ⅲ. 질의 목적에 따른 NoSQL 4대 저장 유형

> 질의 패턴이 단건·계층 문서·동적 열군·다단계 관계 순회 중 무엇인지가 모델 선택 기준이며, 제품 선호보다 주 접근 경로를 먼저 검증해야 함.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Key-Value -->
    <rect x="15" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="15" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="72" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Key-Value</text>
    <rect x="25" y="48" width="95" height="40" rx="4" fill="var(--color-bg-subtle, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="0.8"/>
    <text x="72" y="63" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">Key: "user:101"</text>
    <text x="72" y="77" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">Val: {Session Blob}</text>
    <text x="72" y="110" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #334155)">[단건 초고속 조회]</text>
    <text x="72" y="130" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">O(1) 해시 검색</text>
    <text x="72" y="150" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">인메모리 캐시</text>
    <text x="72" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">Redis, DynamoDB</text>

    <!-- Document -->
    <rect x="140" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="140" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="197" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Document</text>
    <rect x="150" y="48" width="95" height="40" rx="4" fill="var(--color-bg-subtle, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="0.8"/>
    <text x="197" y="63" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">JSON / BSON</text>
    <text x="197" y="77" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">{id, items:[..]}</text>
    <text x="197" y="110" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #334155)">[복합 계층 구조]</text>
    <text x="197" y="130" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">중첩 속성 인덱싱</text>
    <text x="197" y="150" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">상품/CMS 카탈로그</text>
    <text x="197" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">MongoDB, Couchbase</text>

    <!-- Column Family -->
    <rect x="265" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="265" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="322" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Column Family</text>
    <rect x="275" y="48" width="95" height="40" rx="4" fill="var(--color-bg-subtle, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="0.8"/>
    <text x="322" y="63" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">RowKey + Columns</text>
    <text x="322" y="77" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">동적 컬럼 확장</text>
    <text x="322" y="110" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #334155)">[시계열 범위 스캔]</text>
    <text x="322" y="130" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">대규모 쓰기 최적화</text>
    <text x="322" y="150" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">IoT 로그, 메트릭</text>
    <text x="322" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">Cassandra, HBase</text>

    <!-- Graph -->
    <rect x="390" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="390" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="447" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Graph</text>
    <rect x="400" y="48" width="95" height="40" rx="4" fill="var(--color-bg-subtle, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="0.8"/>
    <text x="447" y="63" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">(Node)-[Edge]→(Node)</text>
    <text x="447" y="77" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">인접성 포인터</text>
    <text x="447" y="110" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #334155)">[다단계 관계 순회]</text>
    <text x="447" y="130" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">Index-free Adjacency</text>
    <text x="447" y="150" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">SNS망, FDS 탐지</text>
    <text x="447" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">Neo4j, Neptune</text>
  </svg>
</div>

| 유형 | 데이터 저장 구조 | 적합 질의 패턴 | 대표 적용 분야 | 설계 핵심 요건 |
|---|---|---|---|---|
| **Key-Value** | 유일 Key에 임의 바이너리/문자열 매핑 | 단순 단건 Key 조회 및 저장 | 세션 스토리지, 인메모리 캐시, 장바구니 | 키 해시 분포 균등화 및 만료(TTL) 통제 |
| **Document** | JSON 등 계층 문서 저장 | 복합 속성·중첩 구조 조회 | 상품 카탈로그·CMS | 제품별 문서 크기·임베딩 제약 확인 |
| **Column Family** | Row Key 아래 동적 Column 집합 관리 | 대규모 시계열 쓰기, 특정 열군 범위 검색 | 대용량 로그 수집, IoT 센서 데이터, 통계 집계 | 파티션 키(분산)와 클러스터링 키(정렬) 최적화 |
| **Graph** | Node(개체), Edge(관계), Property로 구성 | 재귀적·다단계 관계 순회(Traversal) | 소셜 네트워크 분석, 이상금융거래 탐지(FDS) | 노드 간 연결 밀도 관리 및 인덱스-프리 인접성 확보 |

### Ⅳ. NoSQL Query-First 모델링 5단계 절차

> 데이터 관계보다 애플리케이션의 Access Pattern을 먼저 고정하며, 각 단계의 산출물이 다음 단계의 파티션·복제 결정을 추적 가능하게 해야 함.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="qf-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <rect x="5" y="5" width="510" height="170" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Step 1 -->
    <rect x="15" y="20" width="85" height="90" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="15" y="20" width="85" height="20" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="57" y="34" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">① SLA 정의</text>
    <text x="57" y="55" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">목표 TPS 도출</text>
    <text x="57" y="70" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">읽기/쓰기 비율</text>
    <text x="57" y="90" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-accent, #0284c7)">[지연 한계]</text>

    <!-- Arrow 1->2 -->
    <line x1="100" y1="65" x2="113" y2="65" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#qf-arrow)"/>

    <!-- Step 2 -->
    <rect x="115" y="20" width="85" height="90" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="115" y="20" width="85" height="20" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="157" y="34" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">② Access 패턴</text>
    <text x="157" y="55" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">화면 질의 전수</text>
    <text x="157" y="70" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">조회 조건 고정</text>
    <text x="157" y="90" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-accent, #0284c7)">[질의 중심]</text>

    <!-- Arrow 2->3 -->
    <line x1="200" y1="65" x2="213" y2="65" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#qf-arrow)"/>

    <!-- Step 3 -->
    <rect x="215" y="20" width="85" height="90" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="215" y="20" width="85" height="20" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="257" y="34" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">③ 모델 매핑</text>
    <text x="257" y="55" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">Aggregate 경계</text>
    <text x="257" y="70" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">4대 저장소 선정</text>
    <text x="257" y="90" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-accent, #0284c7)">[단위 묶음]</text>

    <!-- Arrow 3->4 -->
    <line x1="300" y1="65" x2="313" y2="65" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#qf-arrow)"/>

    <!-- Step 4 -->
    <rect x="315" y="20" width="90" height="90" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="315" y="20" width="90" height="20" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="360" y="34" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">④ 파티션·색인</text>
    <text x="360" y="55" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">Partition Key</text>
    <text x="360" y="70" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">Quorum (R+W&gt;N)</text>
    <text x="360" y="90" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-accent, #0284c7)">[분산 설계]</text>

    <!-- Arrow 4->5 -->
    <line x1="405" y1="65" x2="418" y2="65" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#qf-arrow)"/>

    <!-- Step 5 -->
    <rect x="420" y="20" width="85" height="90" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <rect x="420" y="20" width="85" height="20" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="462" y="34" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">⑤ 정합성 검증</text>
    <text x="462" y="55" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">핫스팟 시뮬레이션</text>
    <text x="462" y="70" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">복제 지연 수렴</text>
    <text x="462" y="90" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">[Quality Gate]</text>

    <!-- Bottom summary -->
    <rect x="15" y="125" width="490" height="35" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="260" y="140" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">핵심 원칙: 엔터티 관계보다 UI 쿼리 경로를 우선 고정하며, 정규화 대신 사전 조인(Pre-join) 중복 허용</text>
    <text x="260" y="152" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">파티션 키 불균형 시 해시 솔트(Salt)를 결합하여 특정 샤드 I/O 병목 원천 차단</text>
  </svg>
</div>

1. **요구 및 SLA 정의**: 워크로드의 읽기/쓰기 비율, 초당 트랜잭션 수(TPS), 허용 지연시간 및 일관성 수준 분석
2. **Access Pattern 식별**: 엔티티 관계보다 화면과 비즈니스 로직에서 실제 호출되는 쿼리 경로와 파라미터를 전수 식별
3. **Aggregate 및 모델 선정**: 한 번에 원자적으로 읽고 쓰는 데이터 묶음(Aggregate)을 정의하고 4대 모델 매핑
4. **파티션 및 색인 설계**: 노드 간 균등 부하 분산을 위한 파티션 키 설정 및 보조 인덱스 최소화 설계
5. **부하 및 정합성 검증**: 시뮬레이션 테스트를 통해 특정 노드 쏠림(Hotspot)과 네트워크 분할 시 복제 수렴 속도 검증

### Ⅴ. RDBMS vs NoSQL 비교 및 Polyglot Persistence

> 금융 원장은 RDBMS의 ACID로, 대규모 사용자 트래픽은 NoSQL의 확장성으로 수용하되 도메인 간 정합성 경계를 명시해야 공존 구조가 안정됨.

| 비교 기준 | RDBMS | NoSQL |
|---|---|---|
| **데이터 모델** | 정형 릴레이션 테이블 (정규화 기반) | Key-Value, Document, Column Family, Graph (비정규화) |
| **트랜잭션 특성** | 다중 레코드·다중 테이블 엄격한 ACID 보장 | 단일 Aggregate 단위 원자성, BASE 중심 최종 일관성 |
| **확장 메커니즘** | Scale-Up(수직 확장), Read Replica 분산 | Sharding 기반 Scale-Out(수평 분산 확장) |
| **질의 방식** | 표준 SQL, 다중 테이블 복합 JOIN 지원 | 목적형 API, 단일 키 질의, 제한된 조인 연산 |
| **스키마 변경** | 엄격한 DDL 적용, 테이블 락 위험 | 무중단 동적 필드 추가 (Schema Flexibility) |

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="pg-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Top: API Gateway -->
    <rect x="35" y="15" width="450" height="30" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.2"/>
    <text x="260" y="34" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">API Gateway / Microservice Domain Routing</text>

    <!-- 3 Arrows Down -->
    <line x1="100" y1="45" x2="100" y2="70" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#pg-arrow)"/>
    <line x1="260" y1="45" x2="260" y2="70" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#pg-arrow)"/>
    <line x1="420" y1="45" x2="420" y2="70" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#pg-arrow)"/>

    <!-- 3 Databases -->
    <rect x="25" y="72" width="150" height="75" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="100" y="90" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">[원장·결제] RDBMS</text>
    <text x="100" y="105" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">PostgreSQL / Oracle</text>
    <text x="100" y="122" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#dc2626">Strict ACID 보장</text>
    <text x="100" y="136" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">금융 원장, 잔액 정합성</text>

    <rect x="185" y="72" width="150" height="75" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="260" y="90" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">[세션·장바구니] Key-Value</text>
    <text x="260" y="105" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">Redis / DynamoDB</text>
    <text x="260" y="122" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#16a34a">Ultra Low Latency</text>
    <text x="260" y="136" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">인메모리 TTL 자동 소멸</text>

    <rect x="345" y="72" width="150" height="75" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="420" y="90" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">[상품카탈로그] Document</text>
    <text x="420" y="105" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">MongoDB / OpenSearch</text>
    <text x="420" y="122" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#ca8a04">Schema Flexibility</text>
    <text x="420" y="136" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">다차원 동적 검색</text>

    <!-- Bottom CDC Synch -->
    <path d="M 175 110 L 183 110" fill="none" stroke="var(--color-primary, #2563eb)" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#pg-arrow)"/>
    <rect x="75" y="158" width="370" height="24" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="0.8"/>
    <text x="260" y="174" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">동기화 통제: RDBMS 트랜잭션 커밋 $\rightarrow$ Debezium CDC $\rightarrow$ Kafka $\rightarrow$ NoSQL 비동기 수렴</text>
  </svg>
</div>

### Ⅵ. NoSQL 문제점·대응책

> 분산 저장소 도입 시 수반되는 핫스팟, 복제 지연, 데이터 불일치 위험을 사전에 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 특정 노드 트래픽 집중 (Hot Partition) | 저카디널리티 키에 랜덤 솔트(Salt) 추가 및 복합 파티션 키 설계 | 클러스터 노드 간 CPU 및 디스크 I/O 균등 분산 달성 |
| 복제 지연으로 인한 옛 데이터 읽기 | 일관성 수준·Quorum·충돌 해결 정책 설정 | 요구한 최신성과 가용성 균형 |
| 비정규화 중복 데이터 간 불일치 | 트랜잭셔널 아웃박스 패턴 및 Kafka-Debezium CDC 동기화 파이프라인 구축 | 분산 이종 저장소 간 최종 일관성(Eventual Consistency) 신속 수렴 |
| 스키마 부재로 인한 데이터 오염 | 애플리케이션 계층 유효성 검증(Schema Validation) 및 버전 태깅 강제 | 불완전한 JSON 데이터 유입 차단 및 하위 호환성 유지 |

### Ⅶ. 기술사적 제언: 일관성과 가용성의 균형 잡힌 Polyglot 설계

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 모든 데이터를 NoSQL로 전환하려는 시도는 RDBMS의 강력한 트랜잭션 보장 능력을 포기하는 우를 범하며, 반대로 모든 워크로드를 RDBMS에 묶어두는 것은 클라우드 분산 확장의 이점을 차단한다. 아키텍처의 성패는 단일 기술 선호가 아니라, 비즈니스 도메인의 오류 비용(Error Cost)과 질의 특성에 맞추어 RDBMS와 NoSQL을 적재적소에 배치하는 **Polyglot Persistence 역량**에서 판가름 난다.

> **[나라면 이렇게 쓴다]**
> 2교시 논술이라면 데이터 도메인의 오류 비용과 SLA를 기준으로 '원장·정산=RDBMS, 캐시·세션=Key-Value, 상품·주문내역=Document, 추천=Graph'로 역할을 분리하겠다. 그리고 도메인 간 정합성은 단순 이중 쓰기(Dual Write)를 엄격히 금지하고, **Kafka와 Debezium을 결합한 트랜잭셔널 아웃박스 패턴(Transactional Outbox Pattern)**으로 비동기 최종 일관성을 달성하는 실전 파이프라인을 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 단일 저장소 획일화 지양, 도메인별 정합성(ACID)과 가용성(BASE) 요구수준 명시 여부를 설계 승인 필수로 판정.
- **대응 방안**: 핵심 원장은 RDBMS의 ACID를 유지하고, 대규모 읽기/조회 트래픽은 CDC 기반 NoSQL Read Model로 분리(CQRS).
- **검증 체계**: 쿼럼 일관성($R+W>N$) 검증 및 카오스 엔지니어링을 통한 네트워크 분할(Split-Brain) 모의 훈련 수행.
- **기대 효과**: 원장의 트랜잭션 무결성을 100% 보존하면서도, 서비스 조회 처리량을 선형적(Scale-Out)으로 10배 이상 증대.

<div class="itpe-flow-map" role="img" aria-label="일관성과 가용성 균형의 Polyglot 아키텍처 거버넌스 파이프라인">
  <div class="itpe-flow-node">
    <strong>도메인 워크로드 분류</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>원장(ACID) vs 조회(BASE) 분리</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>Polyglot 다중 배치</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>적재</strong><span>RDBMS + Document/KV 분산</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node is-current">
    <strong>CDC 동기화 게이트</strong>
    <div class="itpe-step-detail">
      <strong>검증</strong><span>Outbox 패턴 무손실 수렴 검증</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>선형 확장 서비스 오픈</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>결과</strong><span>고가용 무중단 분산 서비스 달성</span></div>
    </div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제133회 확인 · 제123회는 KPC 보조자료이며 공식 원문 미확보
- **검증 출처**: [MongoDB Data Modeling Guide](https://www.mongodb.com/docs/manual/data-modeling/), [Apache Cassandra Architecture Documentation](https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html)

## 연결 토픽

- [샤딩](./045_sharding.md) · [CAP·PACELC 이론](./113_cap_pacelc.md) · [트랜잭션 격리 수준](./020_isolation_level.md) · [데이터 가치평가](./002_data_valuation.md)
