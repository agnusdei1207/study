---
sidebar:
  order: 114
  label: "114. DB 복제 유형 (Replication Types)"
  badge:
    text: "기초"
    variant: note
title: "데이터베이스 복제 유형(동기·비동기·반동기)과 고가용성 복제 아키텍처"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 114
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "114"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>분산 데이터베이스·고가용성</span><strong>DB 복제 유형</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 230" width="100%" height="auto" role="img" aria-label="데이터베이스 3대 복제 동기화 시퀀스 비교">
  <defs>
    <marker id="repArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
    <marker id="repAck" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10b981"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="230" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Col 1: 동기 복제 -->
  <g transform="translate(15, 15)">
    <rect width="155" height="198" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="155" height="26" rx="6" fill="#f8fafc"/>
    <text x="77" y="18" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">1. 동기 복제 (Sync)</text>

    <!-- Nodes Lifeline -->
    <line x1="40" y1="35" x2="40" y2="155" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="1.2"/>
    <line x1="115" y1="35" x2="115" y2="155" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="1.2"/>
    <text x="40" y="44" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1e293b)">Primary</text>
    <text x="115" y="44" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1e293b)">Replica</text>

    <!-- Messages -->
    <path d="M 40 65 L 115 75" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#repArr)"/>
    <text x="77" y="66" text-anchor="middle" font-size="7.5" fill="var(--sl-color-accent, #2563eb)">로그 전송</text>

    <text x="115" y="92" text-anchor="middle" font-size="7" fill="var(--sl-color-gray-2, #64748b)">디스크 기록</text>

    <path d="M 115 105 L 40 115" stroke="#10b981" stroke-width="1.5" marker-end="url(#repAck)"/>
    <text x="77" y="106" text-anchor="middle" font-size="7.5" font-weight="700" fill="#059669">ACK 응답</text>

    <circle cx="40" cy="130" r="3" fill="#2563eb"/>
    <text x="48" y="133" font-size="8" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">최종 커밋</text>

    <!-- Bottom Trait -->
    <text x="77" y="172" text-anchor="middle" font-size="8.5" font-weight="700" fill="#059669">RPO = 0 (무유실)</text>
    <text x="77" y="186" text-anchor="middle" font-size="8" fill="#dc2626">네트워크 RTT 지연</text>
  </g>

  <!-- Col 2: 비동기 복제 -->
  <g transform="translate(182, 15)">
    <rect width="155" height="198" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="155" height="26" rx="6" fill="#f8fafc"/>
    <text x="77" y="18" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">2. 비동기 복제 (Async)</text>

    <!-- Nodes Lifeline -->
    <line x1="40" y1="35" x2="40" y2="155" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="1.2"/>
    <line x1="115" y1="35" x2="115" y2="155" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="1.2"/>
    <text x="40" y="44" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1e293b)">Primary</text>
    <text x="115" y="44" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1e293b)">Replica</text>

    <!-- Messages -->
    <circle cx="40" cy="65" r="3" fill="#2563eb"/>
    <text x="48" y="68" font-size="8" font-weight="700" fill="#2563eb">즉시 커밋!</text>

    <path d="M 40 85 L 115 100" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" stroke-dasharray="3 2" marker-end="url(#repArr)"/>
    <text x="77" y="88" text-anchor="middle" font-size="7.5" fill="var(--sl-color-gray-2, #64748b)">백그라운드 전송</text>

    <text x="115" y="120" text-anchor="middle" font-size="7" fill="var(--sl-color-gray-2, #64748b)">릴레이 적용</text>

    <!-- Bottom Trait -->
    <text x="77" y="172" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2563eb">초저지연 최고성능</text>
    <text x="77" y="186" text-anchor="middle" font-size="8" fill="#dc2626">장애 시 RPO &gt; 0 유실</text>
  </g>

  <!-- Col 3: 반동기 복제 -->
  <g transform="translate(350, 15)">
    <rect width="155" height="198" rx="6" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
    <rect width="155" height="26" rx="6" fill="var(--sl-color-accent, #dbeafe)"/>
    <text x="77" y="18" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">3. 반동기 (Semi-Sync)</text>

    <!-- Nodes Lifeline -->
    <line x1="40" y1="35" x2="40" y2="155" stroke="var(--sl-color-accent, #93c5fd)" stroke-width="1.2"/>
    <line x1="115" y1="35" x2="115" y2="155" stroke="var(--sl-color-accent, #93c5fd)" stroke-width="1.2"/>
    <text x="40" y="44" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1e293b)">Primary</text>
    <text x="115" y="44" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1e293b)">Replica 1</text>

    <!-- Messages -->
    <path d="M 40 65 L 115 75" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#repArr)"/>
    <text x="77" y="66" text-anchor="middle" font-size="7.5" fill="var(--sl-color-accent, #1d4ed8)">로그 전송</text>

    <text x="115" y="92" text-anchor="middle" font-size="7" fill="var(--sl-color-accent, #1e40af)">메모리(Relay) 수신</text>

    <path d="M 115 105 L 40 115" stroke="#10b981" stroke-width="1.5" marker-end="url(#repAck)"/>
    <text x="77" y="106" text-anchor="middle" font-size="7.5" font-weight="700" fill="#059669">최소 1대 ACK</text>

    <circle cx="40" cy="130" r="3" fill="#1e40af"/>
    <text x="48" y="133" font-size="8" font-weight="700" fill="var(--sl-color-accent, #1e40af)">최종 커밋</text>

    <!-- Bottom Trait -->
    <text x="77" y="172" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">성능과 무유실 절충</text>
    <text x="77" y="186" text-anchor="middle" font-size="8" fill="var(--sl-color-accent, #2563eb)">엔터프라이즈 사실상 표준</text>
  </g>
</svg>
</div>

- 본질: **단일 데이터베이스의 장애로 인한 서비스 중단 및 데이터 유실을 방지하기 위해 트랜잭션 로그(WAL, Binlog)를 복수의 데이터베이스 노드로 전송·동기화하여 고가용성(HA), 읽기 트래픽 부하 분산(Scale-out), 재해 복구(DR)를 달성하는 핵심 인프라 아키텍처**
- 암기: `동-비-반` (3대 동기화 방식: 동기, 비동기, 반동기 복제) / `마-슬 / 멀-마` (토폴로지: Master-Slave, Multi-Master) / `복-지-랙` (복제 지연 Replication Lag)
- 판단축:
  - **동기 복제(Synchronous)**: 금융 결제, 계좌 원장 등 데이터 유실이 1건도 허용되지 않는 RPO=0 절대 보장 영역 (단, 네트워크 RTT 지연 감수)
  - **비동기 복제(Asynchronous)**: 초당 트랜잭션 수(TPS)가 최우선이고 미세 유실이 허용되는 대용량 로그 수집 및 SNS 피드 영역
  - **반동기 복제(Semi-Synchronous)**: 여러 복제 노드 중 최소 1개 노드 수신 확인 후 커밋하여 성능과 무유실의 균형을 맞춘 엔터프라이즈 최적해
- 주의: 비동기 복제 환경에서 읽기/쓰기 분리(Read Replica)를 적용할 경우, 쓰기 직후 복제 지연(Replication Lag)으로 인해 사용자가 방금 작성한 글을 조회하지 못하는 **읽기 일관성(Read-your-writes) 불일치**가 발생하므로 세션 라우팅 대책이 필수적임
---

## 1교시 예상문제 (10점)

> 데이터베이스 복제 유형(동기·비동기·반동기)과 고가용성 복제 아키텍처의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### [문제] DB 복제 유형 (Replication Types)

#### 1. DB 복제(Replication)의 정의
- 데이터베이스의 고가용성(HA), 부하 분산, 재해 복구를 위해 트랜잭션 로그를 네트워크를 통해 둘 이상의 노드 간에 동기화하는 복제 기술

#### 2. 복제 동기화 3대 방식 비교

| 복제 방식 | 커밋 완료 시점 | 데이터 유실 (RPO) | 성능 (Latency) |
|:---|:---|:---:|:---:|
| **동기 복제 (Sync)** | 모든 복제 노드의 디스크 기록 확인 후 | **0 (완전 무유실)** | 가장 느림 (네트워크 RTT 종속) |
| **비동기 복제 (Async)** | Primary 로컬 기록 즉시 완료 | 유실 발생 가능 ($> 0$) | **가장 빠름 (초저지연)** |
| **반동기 복제 (Semi-Sync)** | 최소 1개 복제 노드의 릴레이 로그 수신 후 | **거의 0 ($\approx 0$)** | **우수 (성능-정합성 최적 절충)** |

#### 3. 복제 지연(Replication Lag) 극복 방안
- 쓰기 직후 세션은 일정 시간 Primary에서 직접 읽도록 라우팅(Read-your-writes)하여 데이터 불일치 해소
---

### 핵심 관계

| 비교 항목 | 동기 복제 (Synchronous) | 비동기 복제 (Asynchronous) | 반동기 복제 (Semi-Synchronous) |
|:---|:---|:---|:---|
| **커밋 완료 시점** | **모든 복제 노드의 디스크 기록 및 ACK 수신 후** | **Primary 노드 로컬 기록 완료 즉시** | **최소 1개 복제 노드의 릴레이 로그 수신 ACK 후** |
| **데이터 유실 위험** | **완전 0 (RPO = 0 완벽 보장)** | **장애 시 유실 발생 가능 (RPO > 0)** | **거의 0 (RPO $\approx$ 0 달성)** |
| **트랜잭션 지연시간** | **가장 큼** (가장 느린 노드의 RTT에 종속) | **최저 지연** (네트워크 지연 영향 전무) | **낮음** (1개 노드 네트워크 RTT만 수반) |
| **네트워크 단절 시** | 전체 트랜잭션 멈춤 (Hang 상태) | Primary는 정상 처리 지속 | 타임아웃 발생 시 비동기 모드로 자동 강등 |
| **대표 적용 사례** | 금융 거래, 결제 원장, 증권 주문 | 일반 웹 서비스, SNS 피드, 빅데이터 수집 | MySQL Group Replication, 기업형 기간계 코어 |

---

## 2~4교시 예상문제 (25점)

> 엔터프라이즈 데이터베이스의 고가용성과 확장성을 보장하기 위한 복제(Replication)의 동기화 3대 방식(동기, 비동기, 반동기)의 메커니즘과 장단점을 비교하고, 읽기 분산 환경에서 발생하는 복제 지연(Replication Lag)의 해결 방안과 스플릿 브레인(Split-Brain) 방어 체계를 서술하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 무중단 서비스를 지탱하는 데이터베이스 복제(Replication) 개요

#### 한줄 요약: 트랜잭션 로그를 네트워크를 통해 보조 노드에 동기화하여 서비스 가용성과 읽기 처리량을 극대화하는 기술

- **배경**: 단일 DB 인스턴스 환경에서는 하드웨어 고장 시 전사 서비스 중단(SPOF)이 발생하며, 읽기 트래픽 폭증 시 CPU 및 I/O 고갈로 시스템 마비
- **정의**: Primary(Master) 데이터베이스에서 발생한 모든 데이터 변경 이력(WAL/Redo Log/Binary Log)을 하나 이상의 Secondary(Replica/Slave) 노드로 지속 복제하여 데이터의 복사본을 동기화하는 기술
- **3대 핵심 목적**:
  1. **고가용성(HA) 및 무중단 페일오버**: Primary 장애 시 대기 노드를 즉시 승격(Failover)하여 서비스 지속
  2. **읽기 트래픽 부하 분산(Read Scale-out)**: CUD(쓰기)는 Primary로, 대량의 SELECT(읽기)는 복제본으로 분산
  3. **지리적 재해 복구(DR)**: 원격 데이터센터로 데이터를 실시간 복제하여 지진·화재 등 물리적 재난 방어

### Ⅱ. 복제 동기화 3대 방식 상세 비교

#### 한줄 요약: 데이터 무결성을 위해 지연을 감수하는 동기 복제, 성능을 위해 유실 위험을 안는 비동기 복제, 그 절충점인 반동기 복제

| 비교 항목 | 동기 복제 (Synchronous) | 비동기 복제 (Asynchronous) | 반동기 복제 (Semi-Synchronous) |
|:---|:---|:---|:---|
| **커밋 완료 시점** | **모든 복제 노드의 디스크 기록 및 ACK 수신 후** | **Primary 노드 로컬 기록 완료 즉시** | **최소 1개 복제 노드의 릴레이 로그 수신 ACK 후** |
| **데이터 유실 위험** | **완전 0 (RPO = 0 완벽 보장)** | **장애 시 유실 발생 가능 (RPO > 0)** | **거의 0 (RPO $\approx$ 0 달성)** |
| **트랜잭션 지연시간** | **가장 큼** (가장 느린 노드의 RTT에 종속) | **최저 지연** (네트워크 지연 영향 전무) | **낮음** (1개 노드 네트워크 RTT만 수반) |
| **네트워크 단절 시** | 전체 트랜잭션 멈춤 (Hang 상태) | Primary는 정상 처리 지속 | 타임아웃 발생 시 비동기 모드로 자동 강등 |
| **대표 적용 사례** | 금융 거래, 결제 원장, 증권 주문 | 일반 웹 서비스, SNS 피드, 빅데이터 수집 | MySQL Group Replication, 기업형 기간계 코어 |

### Ⅲ. 복제 토폴로지 구조: Master-Slave vs Multi-Master

#### 한줄 요약: 쓰기 주체가 단일 노드인 비대칭 구조와 모든 노드가 쓰기를 수용하는 대칭 구조의 비교

| 비교 항목 | Master-Slave (Active-Standby) | Multi-Master (Active-Active) |
|:---|:---|:---|
| **쓰기(Write) 처리** | **오직 단일 Primary 노드만 쓰기 허용** | **모든 마스터 노드에서 자유롭게 쓰기 허용** |
| **읽기(Read) 처리** | Primary 및 복수의 Read Replica에서 분산 수행 | 모든 노드에서 로컬 읽기 수행 |
| **데이터 충돌 위험** | **충돌 없음** (단일 쓰기 지점 보장) | **노드 간 동시 수정 시 충돌(Conflict) 발생** |
| **충돌 해결 방식** | 불필요 | 타임스탬프(LWW), CRDT, 또는 분산 락(Paxos/Raft) |
| **장애 조치(Failover)** | Primary 다운 시 Slave 중 하나를 승격 필요 | 노드 1대 다운 시에도 타 마스터 노드로 즉시 우회 |
| **적용 복잡도** | 단순하며 대부분의 엔터프라이즈 표준 | 매우 복잡하며 글로벌 분산 서비스에 제한적 적용 |

### Ⅳ. 복제 지연(Replication Lag) 메커니즘과 읽기 일관성 보장 전략

#### 한줄 요약: Primary와 Replica 간의 시간차로 인한 데이터 불일치를 애플리케이션 레벨에서 라우팅하여 해결

- **복제 지연(Replication Lag)의 발생 원인**:
  - Primary는 멀티스레드로 수천 건의 쿼리를 병렬 처리하지만, 과거 Slave는 단일 스레드로 릴레이 로그를 순차 반영하면서 지연 누적
  - 대량 배치 DML(예: 100만 건 `UPDATE`) 실행 시 Slave의 반영 병목 심화
- **실무 장애 현상**: 사용자가 게시글을 작성하자마자 상세 페이지로 이동했을 때 글이 보이지 않거나 이전 데이터가 노출되는 '읽기 일관성 결여' 발생
- **엔지니어링 극복 방안**:
  1. **자신이 쓴 데이터 읽기 (Read-your-writes Consistency)**: 사용자가 쓰기를 수행한 직후 일정 시간(예: 5초간) 동안은 해당 사용자의 읽기 요청을 강제로 Primary 노드로 라우팅
  2. **멀티스레드 복제 (Multi-Threaded Replication)**: MySQL MTS(MTS)를 활성화하여 스키마 또는 논리적 트랜잭션 단위로 복제본에서도 병렬로 로그를 반영하도록 구성
  3. **GTID(Global Transaction Identifier) 기반 동기화 확인**: 읽기 요청 시 클라이언트가 방금 커밋한 트랜잭션의 GTID를 복제본이 이미 반영했는지 확인 후 쿼리 수행

### Ⅴ. 스플릿 브레인(Split-Brain) 방어 및 고가용성 오케스트레이션

#### 한줄 요약: 네트워크 단절 시 복수의 노드가 마스터를 자처하는 뇌 분리 현상을 정족수(Quorum) 투표로 차단

- **스플릿 브레인 (Split-Brain)**:
  - Primary와 Secondary 간의 통신만 단절되고 양쪽 노드는 모두 정상 동작할 때, Secondary가 Primary의 장애로 오판하여 스스로 마스터로 승격
  - 두 노드 모두 쓰기를 수용하여 데이터가 비가역적으로 오염되고 정합성이 영구 붕괴되는 치명적 재난
- **방어 메커니즘**:
  1. **정족수 기반 펜싱 (Quorum Fencing)**: 최소 3대 이상의 홀수 노드 또는 외부 감시자(Witness)를 배치하여, 과반수($N/2 + 1$)의 지지를 얻은 노드만 마스터 자격을 획득
  2. **STONITH (Shoot The Other Node In The Head)**: 장애 의심 노드의 전원(IPMI/PDU)을 물리적으로 강제 차단하여 2개의 마스터 공존 원천 배제
  3. **오케스트레이터 도입**: GitHub Orchestrator, Raft 합의 기반 패트롤 도구를 활용하여 토폴로지 자동 복구

### Ⅵ. 실무 장애 사례 및 트러블슈팅 (Troubleshooting)

#### 한줄 요약: 대량 배치로 인한 복제 지연, 복제본 쓰기 오염, 자동 장애조치 실패 방어

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **대량 DML로 인한 복제 중단** | 1,000만 건 테이블을 한 번의 트랜잭션으로 `DELETE`하여 Slave 지연시간이 수 시간 발생 | 대량 DML은 1,000건 단위 청크(Chunk)로 분할 커밋(`LIMIT 1000`) |
| **복제본 쓰기 오염 (Slave Drift)** | 개발자가 점검 중 실수로 Slave DB에 직접 DML을 실행하여 Primary와 데이터 불일치 | 복제 노드에 `read_only = ON` 및 `super_read_only = ON` 파라미터 강제 |
| **장애조치 시 트랜잭션 유실** | 비동기 복제 환경에서 Primary 급사 시 가장 최신 로그를 가진 Slave를 식별하지 못함 | Semi-Sync 복제 적용 및 MHA/Orchestrator의 최신 GTID 보유 노드 자동 선별 승격 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 많은 조직이 '무중단 DB'를 만든다고 Master-Slave 복제를 구축해 두고 정작 장애가 났을 때 아무도 Failover를 하지 못해 수 시간의 다운타임을 겪는다. 당직 엔지니어가 새벽에 전화를 받고 깨어나 DNS를 수동으로 바꾸고 Slave를 승격시키는 것은 1990년대 방식이다. 진정한 고가용성은 '무인 자동 장애조치(Automated Failover)'에 있으며, 반동기 복제(Semi-Sync)를 통해 데이터 유실을 0으로 막고, 과반수 투표 기반의 오케스트레이터(Orchestrator/Raft)가 30초 이내에 승격을 끝내야 한다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 동기, 비동기, 반동기의 3대 시퀀스 다이어그램과 RPO/지연시간 비교표를 명확히 제시하겠다. 2교시 25점형이라면 Master-Slave vs Multi-Master 토폴로지 비교와 함께 실무의 고질병인 복제 지연(Replication Lag)에 따른 읽기 일관성 깨짐 해결책(세션 기반 Primary 라우팅)과 스플릿 브레인 방어를 위한 쿼럼 펜싱(Quorum Fencing) 메커니즘을 제언에 완벽히 서술하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 비동기 복제 환경에서 마스터 장애 시 수십 초~수 분의 최신 데이터가 유실(RPO > 0)되며, 수작업 기반의 장애 복구 체계는 목표 RTO(5분 이내) 달성이 불가능함.
- **대응 (개선 방안)**: 반동기 복제(Semi-Sync)를 기본 채택하여 최소 1개 복제본의 메모리 수신 ACK를 보장하고, Raft 합의 기반 무인 자동 장애조치(Orchestrator) 및 카오스 엔지니어링 훈련 도입.
- **검증 (검증 기준)**: 마스터 강제 종료 모의훈련 시 RPO = 0 달성 검증, 자동 승격 및 DNS/VIP 스위칭 RTO 30초 이내 완료, 복제 지연 시간 1초 미만 통제.
- **효과 (실행 효과)**: 데이터 유실 사고 100% 예방, 데이터베이스 고가용성 SLA 99.999% 달성, 야간 긴급 장애 대응 인건비 80% 절감.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">비동기 복제로 장애 시 데이터 유실 위험, 수동 Failover로 RTO 수 시간 지연</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">반동기(Semi-Sync) 복제 표준화 + Raft 기반 무인 자동 장애조치 구축</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">RPO = 0 달성, 자동 페일오버 RTO 30초 이내, Replication Lag 1초 이내</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">데이터 무유실 보장, 연간 가용성 99.999% 확보, 24x365 무중단 운영 달성</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제120회 정보관리 2교시: 고가용성 확보를 위한 데이터베이스 복제(Replication)의 동기화 방식(동기, 비동기, 반동기) 비교 및 읽기/쓰기 분리 아키텍처의 복제 지연 해결 방안
- **검증 출처**:
  - MySQL 8.0 Reference Manual, "Chapter 17 Replication"
  - PostgreSQL Documentation, "Chapter 27 High Availability, Load Balancing, and Replication"
---

## 연결 토픽

- 상위 토픽: [051. 고가용성(HA) 아키텍처](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/051_ha_architecture.md)
- 연관 토픽: [113. CAP·PACELC 이론](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/113_cap_pacelc.md), [126. 데이터 복제 (Data Replication)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/126_data_replication.md)
