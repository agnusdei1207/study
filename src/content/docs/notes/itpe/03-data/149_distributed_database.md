---
sidebar:
  order: 149
  label: "149. 분산 데이터베이스(Distributed Database)"
  badge:
    text: "A"
    variant: note
title: "분산 데이터베이스 (Distributed Database System)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 149
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "149"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>분산 아키텍처</span><span>분산 데이터베이스</span><strong>분산 트랜잭션과 5대 투명성</strong></div>

## 큰 그림과 30초 인출

```text
[분산 데이터베이스 시스템 아키텍처 및 5대 투명성]

  [사용자 / 응용 프로그램] (단일 논리 DB로 인식: 5대 투명성)
           │
  ┌────────▼────────────────────────────────────────────────────────┐
  │ 분산 트랜잭션 관리자 (GTM / Global Coordinator)                 │
  │  ① 위치 투명성(Location)   : 물리 저장 위치 은닉               │
  │  ② 분할 투명성(Division)   : 수평/수직 샤딩 은닉               │
  │  ③ 복제 투명성(Replication): 다중 노드 사본 은닉               │
  │  ④ 병행 투명성(Concurrency): 상호 간섭 없는 동시성             │
  │  ⑤ 장애 투명성(Failure)    : 부분 장애 시 무중단 서비스        │
  └────────┬──────────────────────┬──────────────────────┬──────────┘
           │ 2PC: Prepare / Commit │                      │
  ┌────────▼─────────┐   ┌────────▼─────────┐   ┌────────▼─────────┐
  │  로컬 노드 A     │   │  로컬 노드 B     │   │  로컬 노드 C     │
  │  (샤드 1 / 서울) │   │  (샤드 2 / 도쿄) │   │  (샤드 3 / 미국) │
  └──────────────────┘   └──────────────────┘   └──────────────────┘
```

- 본질: **물리적으로 분산된 여러 컴퓨터 노드에 네트워크를 통해 데이터를 분할 또는 복제하여 저장하면서도, 사용자에게는 하나의 통합된 단일 데이터베이스처럼 투명하게 서비스하고 ACID 분산 트랜잭션을 보장하는 고가용·고확장 데이터 관리 시스템**
- 암기: `위-분-복-병-장` (5대 투명성: 위치, 분할, 복제, 병행, 장애) / `준-실` (2PC: Prepare, Commit)
- 판단축:
  - **집중형 DB**: 단일 노드 수직 확장(Scale-up), 트랜잭션 단순, 단일 장애점(SPOF) 위험.
  - **분산 DB (RDBMS/NewSQL)**: 수평 확장(Scale-out), 5대 투명성 보장, 2PC/합의 프로토콜(Raft/Paxos) 기반 엄격한 글로벌 ACID 일관성.
  - **NoSQL**: 가용성과 분할 내성 우선(CAP 정리의 AP 계열), 최종 일관성(Eventual Consistency) 채택.
- 주의: 분산 트랜잭션을 보장하는 2단계 커밋(2PC)은 코디네이터 장애 시 참여 노드가 락을 쥔 채 멈추는 블로킹(Blocking) 결함이 존재하므로, 실무에서는 Raft 기반 NewSQL 또는 사가(Saga) 패턴을 적극 검토함
---

## 1교시 예상문제 (10점)

> 분산 데이터베이스 (Distributed Database System)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **정의** | 물리적으로 분산된 노드에 데이터를 분할·복제 저장하면서 논리적으로 단일 DB로 인식되도록 제어하는 시스템 |
| **5대 투명성** | ① 위치(물리 IP 은닉) ② 분할(샤딩 은닉) ③ 복제(다중 사본 은닉) ④ 병행(동시성 간섭 배제) ⑤ 장애(노드 고장 감춤) |
| **2PC 프로토콜** | 1단계 준비(Prepare: WAL 기록 및 락 점유) $\rightarrow$ 2단계 커밋(Commit: 만장일치 확인 후 영구 반영) |
| **2PC 한계와 극복** | 코디네이터 장애 시 참여 노드 블로킹 발생 $\rightarrow$ 과반수 합의 기반 NewSQL(Raft) 및 MSA 사가(Saga) 패턴으로 극복 |
| **실무 제언** | 코어 금융 원장은 Raft 기반 분산 NewSQL로 원자성 확보, 비즈니스 서비스 간은 비동기 사가 오케스트레이션 적용 |
---

### 핵심 관계

| 투명성 유형 | 핵심 개념 및 은닉 대상 | 실현 기술 및 메커니즘 |
|:---|:---|:---|
| **1. 위치 투명성 (Location)** | 데이터가 물리적으로 어느 서버(IP, Host)에 위치하는지 알 필요 없이 논리적 객체 이름만으로 접근 | 분산 글로벌 데이터 딕셔너리(GDD), 네임 서버 매핑 |
| **2. 분할 투명성 (Division)** | 단일 테이블이 수평(Horizontal) 또는 수직(Vertical)으로 여러 샤드에 분할 저장된 사실을 은닉 | 분산 질의 최적화기(Optimizer), 샤딩 라우팅 룰 |
| **3. 복제 투명성 (Replication)** | 동일한 데이터가 가용성을 위해 여러 노드에 사본으로 중복 적재되어 있음을 인지하지 못하게 함 | 마스터-슬레이브 복제 동기화, Raft 로그 복제 |
| **4. 병행 투명성 (Concurrency)** | 다수의 분산 트랜잭션이 동시에 실행되어도 상호 간섭 없이 직렬화 가능(Serializable)하게 제어 | 분산 락 매니저(DLM), 분산 타임스탬프 순서화 |
| **5. 장애 투명성 (Failure)** | 특정 노드나 네트워크 링크에 고장이 발생해도 트랜잭션 원자성이 유지되고 대체 경로로 우회 | 자동 장애 조치(Failover), 2PC/3PC 회복 프로토콜 |

---

## 2~4교시 예상문제 (25점)

> 분산 데이터베이스(Distributed Database)의 개념과 5가지 투명성(Transparency)을 설명하고, 분산 트랜잭션의 원자성을 보장하기 위한 2단계 커밋(2PC)의 처리 절차, 한계점 및 현대 NewSQL의 합의 알고리즘(Raft/Paxos)과 사가(Saga) 패턴을 통한 극복 방안을 논하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 분산 데이터베이스(Distributed Database)의 개요

#### 한줄 요약: 여러 물리 노드에 데이터를 분산 배치하면서도 논리적으로는 단일 데이터베이스처럼 투명하게 제어하는 시스템

- **배경**:
  - 단일 서버의 CPU, 메모리, 스토리지 용량 한계(Scale-up 한계)와 단일 장애점(SPOF) 극복 필요
  - 글로벌 지사 분산 환경에서 데이터 접근 지연(Latency)을 단축하고 서비스 무중단 고가용성 달성 요구
- **정의**:
  - 논리적으로는 하나의 일관된 데이터베이스이지만, 물리적으로는 컴퓨터 네트워크로 연결된 이기종 또는 동기종의 여러 독립 사이트에 분할·저장되어 있는 데이터 집합 및 이를 관리하는 DBMS
- **핵심 가치**:
  - 노드 증설을 통한 무제한 선형적 수평 확장(Scale-out)
  - 국소 사이트 장애 발생 시에도 서비스 연속성을 유지하는 장애 격리(Fault Tolerance)

### Ⅱ. 분산 데이터베이스의 5대 투명성 (Transparency)

#### 한줄 요약: 사용자가 분산 환경의 물리적 복잡성을 전혀 인지하지 못하도록 은닉하는 5대 설계 원칙

<div class="itpe-diagram-box">
  <div class="itpe-diagram-header">
    <span class="itpe-tag">아키텍처 다이어그램</span>
    <span class="itpe-title">분산 데이터베이스 5대 투명성 및 분산 트랜잭션 코디네이션</span>
  </div>
  <div class="itpe-diagram-body">
    <svg class="itpe-svg" viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-dist" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--color-text, #333)" />
        </marker>
      </defs>
      <!-- 상단: 클라이언트 -->
      <rect x="160" y="12" width="200" height="38" rx="4" fill="var(--color-bg-secondary, #f0f4f8)" stroke="var(--color-border, #0284c7)" stroke-width="1.5" />
      <text x="260" y="32" font-size="12" font-weight="bold" text-anchor="middle" fill="var(--color-text, #111)">사용자 / 애플리케이션</text>
      <text x="260" y="44" font-size="9" text-anchor="middle" fill="var(--color-text-muted, #555)">단일 논리 RDBMS로 인식 (SELECT / UPDATE)</text>

      <path d="M 260 50 L 260 75" stroke="var(--color-primary, #0284c7)" stroke-width="2" marker-end="url(#arrow-dist)" />

      <!-- 중단: 분산 코디네이터 및 5대 투명성 박스 -->
      <rect x="20" y="80" width="480" height="90" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5" />
      <text x="260" y="100" font-size="13" font-weight="bold" text-anchor="middle" fill="#1d4ed8">글로벌 분산 트랜잭션 코디네이터 (5대 투명성 계층)</text>
      <!-- 투명성 뱃지들 -->
      <rect x="35" y="112" width="80" height="46" rx="3" fill="#ffffff" stroke="#93c5fd" stroke-width="1" />
      <text x="75" y="130" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">1. 위치 투명성</text>
      <text x="75" y="145" font-size="8" text-anchor="middle" fill="#64748b">물리 IP 은닉</text>

      <rect x="125" y="112" width="80" height="46" rx="3" fill="#ffffff" stroke="#93c5fd" stroke-width="1" />
      <text x="165" y="130" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">2. 분할 투명성</text>
      <text x="165" y="145" font-size="8" text-anchor="middle" fill="#64748b">샤딩 분할 은닉</text>

      <rect x="215" y="112" width="85" height="46" rx="3" fill="#ffffff" stroke="#93c5fd" stroke-width="1" />
      <text x="257" y="130" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">3. 복제 투명성</text>
      <text x="257" y="145" font-size="8" text-anchor="middle" fill="#64748b">다중 사본 은닉</text>

      <rect x="310" y="112" width="80" height="46" rx="3" fill="#ffffff" stroke="#93c5fd" stroke-width="1" />
      <text x="350" y="130" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">4. 병행 투명성</text>
      <text x="350" y="145" font-size="8" text-anchor="middle" fill="#64748b">동시성 상호 간섭 배제</text>

      <rect x="400" y="112" width="85" height="46" rx="3" fill="#ffffff" stroke="#93c5fd" stroke-width="1" />
      <text x="442" y="130" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">5. 장애 투명성</text>
      <text x="442" y="145" font-size="8" text-anchor="middle" fill="#64748b">노드 고장 감춤</text>

      <!-- 2PC 프로토콜 화살표 -->
      <path d="M 100 170 L 100 205" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrow-dist)" />
      <path d="M 260 170 L 260 205" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrow-dist)" />
      <path d="M 420 170 L 420 205" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrow-dist)" />
      <text x="260" y="193" font-size="10" font-weight="bold" text-anchor="middle" fill="#059669">2단계 커밋 (2PC: Prepare ──► Commit)</text>

      <!-- 하단: 물리 분산 노드들 -->
      <rect x="25" y="210" width="150" height="55" rx="4" fill="var(--color-bg, #ffffff)" stroke="var(--color-border, #0284c7)" stroke-width="1.5" />
      <text x="100" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="var(--color-text, #111)">로컬 사이트 A (서울)</text>
      <text x="100" y="246" font-size="9" text-anchor="middle" fill="var(--color-text-muted, #555)">고객 샤드 #1 / Local DBMS</text>

      <rect x="185" y="210" width="150" height="55" rx="4" fill="var(--color-bg, #ffffff)" stroke="var(--color-border, #0284c7)" stroke-width="1.5" />
      <text x="260" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="var(--color-text, #111)">로컬 사이트 B (도쿄)</text>
      <text x="260" y="246" font-size="9" text-anchor="middle" fill="var(--color-text-muted, #555)">고객 샤드 #2 / Local DBMS</text>

      <rect x="345" y="210" width="150" height="55" rx="4" fill="var(--color-bg, #ffffff)" stroke="var(--color-border, #0284c7)" stroke-width="1.5" />
      <text x="420" y="230" font-size="11" font-weight="bold" text-anchor="middle" fill="var(--color-text, #111)">로컬 사이트 C (미국)</text>
      <text x="420" y="246" font-size="9" text-anchor="middle" fill="var(--color-text-muted, #555)">고객 샤드 #3 / Local DBMS</text>
    </svg>
  </div>
  <div class="itpe-diagram-footer">
    사용자는 중앙의 코디네이터를 통해 5대 투명성 혜택을 받으며, 물리적 분산 노드들은 2PC로 원자성을 동기화함
  </div>
</div>

| 투명성 유형 | 핵심 개념 및 은닉 대상 | 실현 기술 및 메커니즘 |
|:---|:---|:---|
| **1. 위치 투명성 (Location)** | 데이터가 물리적으로 어느 서버(IP, Host)에 위치하는지 알 필요 없이 논리적 객체 이름만으로 접근 | 분산 글로벌 데이터 딕셔너리(GDD), 네임 서버 매핑 |
| **2. 분할 투명성 (Division)** | 단일 테이블이 수평(Horizontal) 또는 수직(Vertical)으로 여러 샤드에 분할 저장된 사실을 은닉 | 분산 질의 최적화기(Optimizer), 샤딩 라우팅 룰 |
| **3. 복제 투명성 (Replication)** | 동일한 데이터가 가용성을 위해 여러 노드에 사본으로 중복 적재되어 있음을 인지하지 못하게 함 | 마스터-슬레이브 복제 동기화, Raft 로그 복제 |
| **4. 병행 투명성 (Concurrency)** | 다수의 분산 트랜잭션이 동시에 실행되어도 상호 간섭 없이 직렬화 가능(Serializable)하게 제어 | 분산 락 매니저(DLM), 분산 타임스탬프 순서화 |
| **5. 장애 투명성 (Failure)** | 특정 노드나 네트워크 링크에 고장이 발생해도 트랜잭션 원자성이 유지되고 대체 경로로 우회 | 자동 장애 조치(Failover), 2PC/3PC 회복 프로토콜 |

### Ⅲ. 분산 트랜잭션 제어 프로토콜: 2단계 커밋(2PC)

#### 한줄 요약: 코디네이터 주도하에 준비(Prepare)와 실행(Commit)의 2단계를 거쳐 전원 합의를 달성하는 원자성 프로토콜

```text
[2단계 커밋 (Two-Phase Commit, 2PC) 시퀀스]

  코디네이터 (Coordinator)               참여 노드들 (Cohort / Participants)
           │                                          │
    [1단계: Prepare Phase]                            │
           │ ─── 1. Prepare (준비 요청) ───────────► │
           │                                          │ (WAL 기록, 락 점유)
           │ ◄── 2. Vote-Commit (준비 완료 응답) ──── │
           │                                          │
    [2단계: Commit Phase]                             │
           │ (전원 찬성 시 글로벌 커밋 확정)         │
           │ ─── 3. Global Commit (커밋 실행 지시) ──► │
           │                                          │ (실제 커밋 및 락 해제)
           │ ◄── 4. Acknowledgment (완료 응답) ────── │
```

### 1. 2PC의 2단계 동작 절차
1. **1단계: 준비 단계 (Prepare / Voting Phase)**
   - 코디네이터가 모든 참여 노드에게 트랜잭션 준비 요청(`Prepare`) 전송.
   - 참여 노드는 리두/언두 로그를 디스크(WAL)에 플러시하고, 대상 데이터에 배타적 락(X-Lock)을 건 뒤 성공 시 `Vote-Commit`, 실패 시 `Vote-Abort` 전송.
2. **2단계: 커밋 단계 (Commit / Completion Phase)**
   - **글로벌 커밋**: 모든 노드가 `Vote-Commit`을 보내면 코디네이터가 `Global Commit`을 브로드캐스트하여 영구 반영 및 락 해제.
   - **글로벌 롤백**: 단 하나의 노드라도 `Vote-Abort`를 보내거나 타임아웃 발생 시 `Global Abort`를 지시하여 전원 롤백.

### 2. 2PC의 한계점
- **블로킹 문제 (Blocking Problem)**: 코디네이터가 1단계를 마치고 2단계 지시를 내리기 직전 장애로 다운되면, 참여 노드들은 커밋도 롤백도 못 한 채 락을 잡고 무한정 대기하여 커넥션 풀 고갈 발생.
- **단일 장애점 (SPOF)**: 중앙 코디네이터의 생존 여부에 전체 시스템 생사가 직결됨.

### Ⅳ. 현대 NewSQL 및 합의 알고리즘(Raft/Paxos)의 혁신

#### 한줄 요약: 전원 만장일치(2PC)의 블로킹을 탈피하여, 과반수 합의(Quorum)로 무중단 일관성을 달성하는 분산 합의

| 구분 | 고전적 2PC (Two-Phase Commit) | Raft / Paxos 기반 NewSQL (Spanner, Cockroach) |
|:---|:---|:---|
| **합의 방식** | **만장일치 (100% 동의)** 필수 | **과반수 합의 (Quorum: $(N/2)+1$)** 기반 |
| **장애 내성** | 1개 노드만 지연/다운되어도 전체 트랜잭션 실패 | $2F+1$개 노드 중 $F$개 노드가 다운되어도 정상 가동 |
| **블로킹 여부** | 코디네이터 사망 시 영구 블로킹 발생 | 리더 사망 시 즉시 새로운 리더 선출(Leader Election) 진행 |
| **시간 동기화** | 일반 NTP 의존 $\rightarrow$ 외부 일관성(External Consistency) 한계 | Google **TrueTime**(원자시계+GPS) 또는 **HLC**(Hybrid Logical Clock) |
| **적용 사례** | Oracle XA, Java JTA 분산 트랜잭션 | Google Spanner, CockroachDB, TiDB |

### Ⅴ. 마이크로서비스(MSA) 환경의 사가(Saga) 패턴

#### 한줄 요약: 분산 락과 2PC를 배제하고, 로컬 트랜잭션 체인과 보상 트랜잭션(Compensating Tx)으로 최종 일관성 달성

```text
[오케스트레이션 기반 사가(Saga) 패턴과 보상 트랜잭션]

  [사가 오케스트레이터] ──► 1. 주문 생성 ──► [주문 서비스] (성공)
           │
           ├────────────► 2. 결제 승인 ──► [결제 서비스] (성공)
           │
           ├────────────► 3. 재고 차감 ──► [재고 서비스] (실패! 재고 부족)
           │
           ▼ [실패 감지: 역방향 보상 트랜잭션 발동]
  [사가 오케스트레이터] ──► 4. 결제 취소 ──► [결제 서비스] (보상 트랜잭션 완결)
           │
           └────────────► 5. 주문 취소 ──► [주문 서비스] (보상 트랜잭션 완결)
```

- **코레오그래피(Choreography)**: 중앙 제어자 없이 각 서비스가 이벤트를 발행·구독(Pub/Sub)하여 자율적으로 다음 트랜잭션 실행. 구조 단순하나 흐름 추적 어려움.
- **오케스트레이션(Orchestration)**: 사가 오케스트레이터가 전체 트랜잭션 순서를 중앙에서 지시하고, 단계 실패 시 이전 완료 단계들의 보상 트랜잭션(환불, 재고 원복)을 역순으로 호출하여 정합성 보장.

### Ⅵ. 실무 아키텍처 장애 유형 및 대응 전략

#### 한줄 요약: 글로벌 데드락, 2PC 롱 트랜잭션 커넥션 고갈, 시계 불일치 왜곡의 기술적 방어

- **글로벌 데드락 (Global Deadlock)**:
  - **원인**: 노드 A의 레코드를 잡고 노드 B의 레코드를 요청하는 Tx1과, 그 반대로 동작하는 Tx2가 서로 다른 물리 사이트에서 교차 락 점유.
  - **대응**: 분산 대기 그래프(Distributed Wait-For Graph) 주기적 수집 분석, 또는 타임스탬프 기반의 `Wait-Die` / `Wound-Wait` 선점 기법 적용.
- **네트워크 파티션 시 데이터 불일치 (Split-Brain)**:
  - **대응**: 쿼럼(Quorum) 기반 분할 격리 규칙 적용. 과반수 노드를 확보하지 못한 서브넷은 즉시 읽기 전용(Read-only)으로 전환하여 쓰기 차단.
- **NTP 시계 드리프트로 인한 트랜잭션 선후 관계 역전**:
  - **대응**: 물리적 시계에 논리적 카운터를 결합한 **HLC(Hybrid Logical Clock)**를 채택하여 인과 관계(Causality)를 100% 보존.

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 분산 데이터베이스의 본질은 "네트워크는 언제든 끊어질 수 있고, 물리 서버는 언제든 고장 난다"는 분산 시스템의 현실을 전제로 한다. 고전적인 분산 DB 답안이 '5대 투명성'과 '2PC 프로토콜'의 교과서적 암기에서 끝났다면, 현대의 기술사 답안은 2PC의 동기식 블로킹 한계를 지적하고, 이를 극복한 "과반수 합의 기반 NewSQL(Spanner, CockroachDB)의 Raft 아키텍처"와 "MSA 환경의 사가(Saga) 패턴 최종 일관성"으로 기술의 진화 궤적을 명확히 제시해야 고득점을 받는다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 5대 투명성의 정의 및 실현 기술 매핑 표와 2PC 2단계 시퀀스를 컴팩트하게 구성하겠다. 2교시형이라면 글로벌 핀테크 아키텍처를 사례로 들어, 금융 계좌 원장과 같은 절대적 무결성 구간에는 Raft 기반 NewSQL을 배치하고, 일반 상품 주문-물류-알림에는 사가(Saga) 오케스트레이터를 도입하여 트랜잭션 격리 비용을 최적화하는 '하이브리드 분산 트랜잭션 아키텍처'를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 마이크로서비스 및 분산 노드 전체를 동기식 2PC로 결합하면, 단일 노드 지연이 전체 시스템의 블로킹과 커넥션 풀 고갈을 초래하여 가용성이 급격히 붕괴됨.
- **대응**: 고성능 트랜잭션 코어는 과반수 합의(Raft) 기반의 NewSQL로 전환하여 자동 페일오버를 달성하고, 이기종 서비스 간 분산 트랜잭션은 Kafka 기반 사가(Saga) 패턴으로 비동기 최종 일관성을 확립함.
- **검증**: 카오스 엔지니어링(Chaos Mesh)을 통해 네트워크 단절 및 코디네이터 강제 종료 상황을 모의 실험하여 보상 트랜잭션 성공률 100%를 입증함.
- **효과**: 글로벌 트랜잭션 처리 지연시간 80% 단축 및 시스템 가용성 99.999% 무중단 보장.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <span class="step-num">1. 현행 한계</span>
    <span class="step-title">2PC 블로킹 & SPOF</span>
    <span class="step-desc">동기식 만장일치 2PC 적용 시 코디네이터 장애 및 네트워크 지연에 따른 전사 마비</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">2. 개선 방안</span>
    <span class="step-title">NewSQL & 사가 패턴 분리</span>
    <span class="step-desc">단일 클러스터는 Raft 기반 과반수 NewSQL 도입, 서비스 간 연계는 비동기 사가 전환</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">3. 검증 기준</span>
    <span class="step-title">카오스 실험 & 보상 감사</span>
    <span class="step-desc">네트워크 파티션 주입 카오스 테스트 및 보상 트랜잭션 멱등성(Idempotency) 검증</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">4. 실행 효과</span>
    <span class="step-title">글로벌 고가용성 달성</span>
    <span class="step-desc">선형적 Scale-out 확장성 확보 및 무중단 99.999% 엔터프라이즈 분산 트랜잭션 확립</span>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제117회 정보관리 2교시: 분산 데이터베이스(Distributed Database)의 개념, 5가지 투명성 및 분산 트랜잭션 2PC
  - 제111회 컴퓨터시스템응용 1교시: 2단계 커밋(2PC)의 처리 절차 및 블로킹 문제
- **검증 출처**:
  - M. Tamer Özsu & Patrick Valduriez, "Principles of Distributed Database Systems 4th Edition", Springer
  - Abraham Silberschatz et al., "Database System Concepts 7th Edition", Chapter 19 Distributed Databases
  - Martin Kleppmann, "Designing Data-Intensive Applications", Chapter 8-9 Distributed Transactions and Consensus
---

## 연결 토픽

- 상위 토픽: [03-128 데이터베이스 개요](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/128_database.md)
- 선수 토픽: [03-020 트랜잭션 ACID](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/020_transaction_acid.md), [03-113 CAP·PACELC](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/113_cap_pacelc.md)
- 후속 토픽: [03-126 데이터 복제](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/126_data_replication.md), [01-011 마이크로서비스 아키텍처(MSA)](file:///C:/workspace/study/src/content/docs/notes/itpe/01-software-engineering/011_msa.md)
