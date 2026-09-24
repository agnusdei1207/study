---
sidebar:
  order: 113
  label: "113. CAP·PACELC 이론"
  badge:
    text: "기초"
    variant: note
title: "CAP 정리 및 PACELC 이론을 적용한 분산 데이터 저장소 아키텍처"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 113
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "113"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>분산 데이터베이스·고가용성</span><strong>CAP·PACELC 이론</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 230" width="100%" height="auto" role="img" aria-label="CAP 정리와 PACELC 이론 트레이드오프 결정 구조">
  <defs>
    <marker id="pacArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="230" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Left: CAP Triangle -->
  <g transform="translate(20, 18)">
    <rect width="215" height="194" rx="7" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="215" height="26" rx="7" fill="#f8fafc"/>
    <text x="107" y="18" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-2, #475569)">1. CAP 정리 (장애 중심)</text>

    <!-- Triangle polygon -->
    <polygon points="107,45 40,140 174,140" fill="none" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="2"/>

    <!-- Vertex C -->
    <circle cx="107" cy="45" r="14" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)"/>
    <text x="107" y="49" text-anchor="middle" font-size="10" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">C</text>

    <!-- Vertex A -->
    <circle cx="40" cy="140" r="14" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)"/>
    <text x="40" y="144" text-anchor="middle" font-size="10" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">A</text>

    <!-- Vertex P -->
    <circle cx="174" cy="140" r="14" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)"/>
    <text x="174" y="144" text-anchor="middle" font-size="10" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">P</text>

    <!-- Bottom Caption -->
    <text x="107" y="168" text-anchor="middle" font-size="9" font-weight="700" fill="#dc2626">물리 분산 시 P는 필수 전제</text>
    <text x="107" y="182" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #334155)">실질적 선택: <tspan font-weight="700">CP</tspan> (HBase) vs <tspan font-weight="700">AP</tspan> (Cassandra)</text>
  </g>

  <!-- Right: PACELC Framework -->
  <g transform="translate(255, 18)">
    <rect width="245" height="194" rx="7" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
    <rect width="245" height="26" rx="7" fill="var(--sl-color-accent, #dbeafe)"/>
    <text x="122" y="18" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #1e40af)">2. PACELC 확장 (평상시 반영)</text>

    <!-- Partition Branch (P) -->
    <rect x="15" y="38" width="215" height="65" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)"/>
    <text x="25" y="54" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">If Partition (P) : 장애 상황</text>
    <text x="35" y="70" font-size="8.5" fill="var(--sl-color-text, #1e293b)">• <tspan font-weight="700" fill="#2563eb">PC</tspan> : 일관성 사수 (HBase, Spanner)</text>
    <text x="35" y="85" font-size="8.5" fill="var(--sl-color-text, #1e293b)">• <tspan font-weight="700" fill="#2563eb">PA</tspan> : 가용성 사수 (Cassandra, DynamoDB)</text>

    <!-- Normal Branch (Else, E) -->
    <rect x="15" y="112" width="215" height="68" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)"/>
    <text x="25" y="128" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">Else (E) : 99.9% 평상시 정상 상태</text>
    <text x="35" y="145" font-size="8.5" fill="var(--sl-color-text, #1e293b)">• <tspan font-weight="700" fill="#1d4ed8">EL</tspan> : 지연시간 최소화 (비동기 복제)</text>
    <text x="35" y="160" font-size="8.5" fill="var(--sl-color-text, #1e293b)">• <tspan font-weight="700" fill="#1d4ed8">EC</tspan> : 엄격한 일관성 (동기화 지연 감수)</text>

    <text x="122" y="196" text-anchor="middle" font-size="8" font-weight="600" fill="var(--sl-color-accent, #1e40af)">대표: PC/EC (금융 원장), PA/EL (SNS/로그)</text>
  </g>
</svg>
</div>

- 본질: **물리적 분산 데이터 환경에서 네트워크 분할(P)은 불가피하므로 일관성(C)과 가용성(A) 중 하나를 선택해야 한다는 CAP 정리를 확장하여, 네트워크 분할(P) 시에는 가용성(A)과 일관성(C)의 상충을, 정상 상태(Else)에서는 지연시간(Latency)과 일관성(Consistency)의 상충을 체계화한 분산 시스템 아키텍처 설계 이론**
- 암기: `일-가-분` (Consistency, Availability, Partition Tolerance) / `피-씨-피-에이 / 이-엘-이-씨` (PC/EC, PA/EL) / `쿼-알-더-엔` (Quorum: $R + W > N$)
- 판단축:
  - **PC/EC (예: Bigtable, HBase, Spanner)**: 분할 시에도 일관성을 보장하고, 평상시에도 지연시간을 감수하며 강력한 일관성(Strong Consistency) 유지 (금융/결제)
  - **PA/EL (예: Cassandra, DynamoDB)**: 분할 시 가용성을 극대화하고, 평상시에는 복제 지연을 허용하여 초저지연 읽기/쓰기 보장 (SNS/로그 수집)
- 주의: 실무에서 네트워크 일시 지연(Latency)을 CAP의 파티션 단절(P)로 오판하여 불필요하게 가용성을 포기하거나 서비스를 중단시키지 않도록 장애 감지 임계치(Heartbeat Timeout) 튜닝이 필수적임
---

## 1교시 예상문제 (10점)

> CAP 정리 및 PACELC 이론을 적용한 분산 데이터 저장소 아키텍처의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### [문제] CAP 정리 vs PACELC 이론

#### 1. CAP 정리와 PACELC 이론의 개념
- **CAP 정리**: 분산 환경에서 일관성(C), 가용성(A), 분할용인(P) 중 최대 2개만 만족 가능하다는 기본 정리
- **PACELC 이론**: 장애 시(If P: A vs C)와 평상 시(Else: L vs C)의 2단계 트레이드오프를 규명한 확장 모델

#### 2. PACELC 4대 모델 비교 및 대표 DBMS

| 분류 유형 | 장애 시 (Partition) | 평상 시 (Else) | 대표 DBMS 및 최적 도메인 |
|:---|:---:|:---:|:---|
| **PC/EC** | 일관성 (C) 사수 | 일관성 (C) 사수 | Google Spanner, HBase (금융, 원장) |
| **PC/EL** | 일관성 (C) 사수 | 저지연 (L) 우선 | MongoDB, Redis (인증 세션, 캐시) |
| **PA/EL** | 가용성 (A) 사수 | 저지연 (L) 우선 | Cassandra, DynamoDB (SNS, 피드, 로그) |

#### 3. 분산 일관성 제어 방안 (Quorum)
- 쿼럼 크기와 복제 프로토콜, 읽기·쓰기 경로를 함께 검토하며, $R+W>N$은 해당 시스템의 정족수 정의와 장애 가정이 맞을 때 적용
---

### 핵심 관계

| CAP 분류 | 시스템 특성 및 동작 방식 | 포기 속성 | 대표 솔루션 |
|:---|:---|:---|:---|
| **CP (Consistency + Partition)** | 네트워크 단절 발생 시 동기화되지 않은 노드는 클라이언트 요청을 차단하거나 에러를 반환하여 데이터 불일치를 원천 방지 | Availability (가용성) | Google Cloud Spanner, Apache HBase, MongoDB, Redis |
| **AP (Availability + Partition)** | 노드 간 단절이 발생하더라도 각 노드는 자신이 가진 데이터를 바탕으로 무조건 정상 응답을 반환하고 추후 비동기 동기화 | Consistency (일관성) | Apache Cassandra, Amazon DynamoDB, CouchDB |
| **CA (Consistency + Availability)** | 네트워크 단절이 전혀 없는 환경에서만 성립 가능 (분산 시스템에서는 비현실적) | Partition Tolerance (분할용인) | 전통적 단일 노드 RDBMS (Oracle, MySQL 단일 인스턴스) |

---

## 2~4교시 예상문제 (25점)

> 분산 데이터베이스 환경에서 데이터의 신뢰성과 성능을 결정하는 CAP 정리의 개념과 한계점을 기술하고, 이를 정상 상태까지 확장한 PACELC 이론의 매트릭스 구조와 대표 DBMS 분류 및 비즈니스 요건별 NoSQL 선정 기준을 제시하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 분산 시스템의 근본적 트레이드오프: CAP 정리 개요

#### 한줄 요약: 분산 네트워크 환경에서 일관성(C), 가용성(A), 분할 용인(P)의 3가지 속성을 동시에 모두 만족하는 것은 불가능하다는 Eric Brewer의 기본 정리

- **배경**: 단일 중앙 집중식 RDBMS의 한계를 극복하기 위해 수천 대의 상용 서버로 수평 확장(Scale-out)하는 NoSQL 분산 환경이 도래하면서 노드 간 통신 단절 문제 직면
- **정의**: 분산 데이터베이스 시스템은 네트워크 분할 상태에서 선형화 가능한 일관성과 모든 요청에 대한 가용성을 동시에 제공할 수 없다는 결과
  1. **Consistency (일관성)**: 모든 노드는 어느 시점에 접근하더라도 가장 최근에 갱신된 최신 데이터를 동일하게 조회해야 함
  2. **Availability (가용성)**: 일부 노드에 장애가 발생하더라도 모든 정상 노드는 오류 없이 항상 응답(Read/Write)을 반환해야 함
  3. **Partition Tolerance (분할 용인)**: 노드 간 네트워크 패킷 유실이나 단절이 발생해도 시스템 전체는 중단 없이 동작해야 함
- **핵심 통찰**: 물리적 네트워크에서 통신 단절(P)은 피할 수 없는 물리 현상이므로, 분산 시스템은 사실상 **CP** 또는 **AP** 중 하나를 선택해야 함 (CA는 단일 인스턴스 RDBMS에만 해당)

### Ⅱ. CAP 3대 속성의 상세 메커니즘과 분류 모델

#### 한줄 요약: 분할 발생 시 최신 데이터를 제공하지 못하면 에러를 뱉는 CP와, 구버전 데이터를 반환하더라도 가용성을 유지하는 AP의 양립

- **네트워크 단절(Partition) 발생 상황**:
  - 클라이언트 1이 노드 A에 $x=10$ 쓰기 성공 후, 노드 A와 노드 B 간 네트워크 단절 발생
  - 클라이언트 2가 노드 B에 $x$ 읽기 요청 수행 시:
    - **CP 선택**: 노드 B는 노드 A의 최신 변경을 동기화받지 못했으므로 에러 반환 (가용성 포기, 일관성 사수)
    - **AP 선택**: 노드 B는 동기화되지 않은 과거 데이터($x=5$)를 즉시 반환 (일관성 포기, 가용성 사수)

| CAP 분류 | 시스템 특성 및 동작 방식 | 포기 속성 | 대표 솔루션 |
|:---|:---|:---|:---|
| **CP (Consistency + Partition)** | 네트워크 단절 발생 시 동기화되지 않은 노드는 클라이언트 요청을 차단하거나 에러를 반환하여 데이터 불일치를 원천 방지 | Availability (가용성) | Google Cloud Spanner, Apache HBase, MongoDB, Redis |
| **AP (Availability + Partition)** | 노드 간 단절이 발생하더라도 각 노드는 자신이 가진 데이터를 바탕으로 무조건 정상 응답을 반환하고 추후 비동기 동기화 | Consistency (일관성) | Apache Cassandra, Amazon DynamoDB, CouchDB |
| **CA (Consistency + Availability)** | 네트워크 단절이 전혀 없는 환경에서만 성립 가능 (분산 시스템에서는 비현실적) | Partition Tolerance (분할용인) | 전통적 단일 노드 RDBMS (Oracle, MySQL 단일 인스턴스) |

### Ⅲ. CAP 이론의 구조적 한계와 PACELC 이론의 탄생

#### 한줄 요약: CAP 정리가 간과한 99.9%의 '정상 상태(Else)'에서 지연시간(Latency)과 일관성(Consistency)의 상충 관계를 정립한 Daniel Abadi의 확장 모델

$$\text{If } [P] \implies [A] \text{ vs } [C], \quad [E]\text{lse} \implies [L] \text{ vs } [C]$$

- **CAP의 3대 한계점**:
  1. **네트워크 정상 상태 침묵**: 네트워크 분할(P)은 1년에 몇 분 발생하지 않는 비정상 상태인데, 99.9% 정상 상태에서의 시스템 행동 규칙을 설명하지 못함
  2. **지연시간(Latency) 무시**: 분산 환경에서 일관성을 유지하기 위해 모든 복제본에 동기화 쓰기를 수행하면 지연시간이 폭증하여 시스템 성능이 붕괴되는 현상을 반영 못함
  3. **이분법적 극단성**: 일관성을 '강한 일관성'과 '완전한 불일치'의 이분법으로 취급하여 현실적인 중간 단계인 최종 일관성(Eventual Consistency)을 설명 불가

### Ⅳ. PACELC 이론의 4대 아키텍처 매트릭스 비교

#### 한줄 요약: 장애 시(PC/PA)와 평상 시(EC/EL)를 조합하여 분산 데이터베이스를 4가지 유형으로 명확히 분류

| 분류 유형 | 장애 시 (Partition) | 평상 시 (Else) | 핵심 동작 메커니즘 | 대표 데이터베이스 |
|:---|:---:|:---:|:---|:---|
| **PC/EC** | Consistency (일관성) | Consistency (일관성) | 장애 시 에러 반환, 평상시 모든 복제본에 2PC/Raft 동기화 쓰기를 수행하여 엄격한 일관성 보장 | Google Spanner, HBase, CockroachDB |
| **PC/EL** | Consistency (일관성) | Latency (저지연) | 네트워크 분할 시 가용성을 포기하지만, 평상시에는 마스터 1곳에만 동기화하고 슬레이브는 비동기 복제하여 빠른 응답 | MongoDB, Redis (Master-Slave 구성) |
| **PA/EL** | Availability (가용성) | Latency (저지연) | 분할 시에도 구버전 데이터를 반환하며 서비스 유지, 평상시에도 비동기 복제를 통해 초저지연 읽기/쓰기 실현 | Apache Cassandra, DynamoDB, Riak |
| **PA/EC** | Availability (가용성) | Consistency (일관성) | 분할 시에는 일단 응답을 허용하지만, 평상시에는 복제본 동기화 완료를 기다려 일관성을 유지 (이론적 조합) | 매우 드묾 (일부 커스텀 동기화 엔진) |

### Ⅴ. 분산 일관성 조절 메커니즘: 쿼럼(Quorum) 합의 모델

#### 한줄 요약: 읽기 노드 수($R$)와 쓰기 노드 수($W$)의 합이 전체 복제본 수($N$)를 초과하도록 설정하여 강력한 일관성을 튜닝하는 기법

$$R + W > N \implies \text{Strong Consistency (강한 일관성 보장)}$$

- 전체 복제본 수 $N = 3$일 때:
  - 쓰기 쿼럼 $W = 2$ (2개 노드 기록 성공 시 트랜잭션 완료)
  - 읽기 쿼럼 $R = 2$ (2개 노드에서 읽어 최신 타임스탬프 채택)
  - 정족수 중첩만으로 강한 일관성이 자동 보장되는 것은 아니며, 복제 순서·버전·쓰기 승인 규칙을 함께 확인
- **Sloppy Quorum & Hinted Handoff**: 일시적 네트워크 장애로 쿼럼 충족이 불가능할 때, 다른 건강한 임의 노드에 쓰기를 임시 위임(Hinted Handoff)하여 가용성을 보장하는 AP 기법
- **Read Repair & Anti-Entropy**: 읽기 시점에 노드 간 버전 불일치가 감지되면 백그라운드에서 최신 데이터로 복구(Read Repair)하거나 Merkle Tree를 비교하여 능동 동기화(Anti-Entropy)

### Ⅵ. 실무 적용 시 NoSQL 데이터베이스 선정 가이드라인

#### 한줄 요약: 비즈니스 도메인의 금융적 위험도와 트랜잭션 특성에 따라 PACELC 모델을 매핑

| 비즈니스 도메인 | 권장 모델 | 선정 사유 및 아키텍처 설계 포인트 |
|:---|:---:|:---|
| **코어 뱅킹·주식 거래** | **PC/EC** | 잔액 불일치는 치명적 금융 사고로 직결. Raft/Paxos 기반 분산 합의 및 Spanner의 TrueTime 트랜잭션 적용 필수 |
| **e커머스 장바구니/카탈로그** | **PA/EL** | 1초라도 장바구니 페이지가 멈추면 매출 이탈 발생. 최종 일관성을 수용하고 애플리케이션 레벨 충돌 해결(CRDT) 적용 |
| **실시간 관측성 로그 수집** | **PA/EL** | 초당 수만 건의 로그가 유입되므로 저지연 쓰기가 절대적. 유실이나 시차는 허용 가능 |

### Ⅶ. 기술사적 제언

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 분산 NoSQL 도입 시 CAP의 극단적 이분법만 고려하여 평상시 지연시간(Latency) 상충을 간과함에 따라, 무리한 동기 복제로 인한 응답 지연 또는 과도한 비동기 복제로 인한 데이터 손실 발생.
- **대응 (개선 방안)**: PACELC 프레임워크에 기반하여 업무 도메인별(원장계 PC/EC, 조회계 PA/EL)로 분산 저장소를 분리하고, 쿼럼 파라미터($R, W, N$)를 동적으로 튜닝하며, 충돌 해결을 위한 CRDT 데이터 구조 도입.
- **검증 (검증 기준)**: 네트워크 분할 시 SLA 응답 성공률 99.99% 준수(AP 영역), 원장 데이터 복제 불일치 0건 검증(CP 영역), 쿼럼 읽기/쓰기 레이턴시 10ms 이내 유지.
- **효과 (실행 효과)**: 대규모 분산 장애 시 서비스 다운타임 0건 달성, 글로벌 트랜잭션 지연시간 60% 단축, 금융급 데이터 정합성과 가용성의 동시 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">CAP 이분법적 설계로 평상시 지연시간(L) 무시 및 복제 지연 데이터 손실</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">PACELC 기반 도메인 격리 + 쿼럼 튜닝(R+W&gt;N) 및 CRDT 적용</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">분할 시 가용성 99.99%, 원장 불일치 0건, 쿼럼 응답 10ms 이내</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">장애 다운타임 0건, 글로벌 트랜잭션 60% 가속, 정합성·가용성 달성</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제126회 정보관리 2교시: 분산 데이터베이스 환경에서의 CAP 이론과 PACELC 이론을 비교하고 NoSQL 선정 기준 제시
  - 제93회, 제117회 기출
- **검증 출처**:
  - Eric Brewer, "CAP twelve years later: How the 'rules' have changed", Computer (2012)
  - Daniel Abadi, "Consistency Tradeoffs in Modern Distributed Database System Design: CAP is Only Part of the Story", IEEE Computer (2012)
---

## 연결 토픽

- 상위 토픽: [001. NoSQL (Not Only SQL)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/001_nosql.md)
- 연관 토픽: [051. 고가용성(HA) 아키텍처](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/051_ha_architecture.md), [118. MongoDB](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/118_mongodb.md)
