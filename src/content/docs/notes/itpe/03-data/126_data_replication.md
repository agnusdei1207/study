---
sidebar:
  order: 126
  label: "126. 데이터 복제 (Data Replication)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 126
title: "데이터 복제(Data Replication) 아키텍처와 계층별 복제 기술 및 DR 구축 전략"
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "126"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>분산 데이터베이스·고가용성</span><strong>데이터 복제</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Layer 1: App/CDC -->
  <rect x="25" y="20" width="470" height="60" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="45" y="42" font-size="12" font-weight="bold" fill="#1d4ed8">1. 애플리케이션 및 CDC 계층 (Kafka, Debezium, GoldenGate)</text>
  <text x="45" y="62" font-size="11" fill="var(--sl-color-text, #334155)">- 트랜잭션 로그를 이벤트로 발행하여 이기종 DBMS(Oracle to PG) 간 실시간 동기화</text>

  <!-- Layer 2: DBMS Engine -->
  <rect x="25" y="95" width="470" height="60" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="45" y="117" font-size="12" font-weight="bold" fill="#0284c7">2. DBMS 엔진 계층 (PostgreSQL Streaming, MySQL Binlog)</text>
  <text x="45" y="137" font-size="11" fill="var(--sl-color-text, #334155)">- WAL/Redo 로그 전송, 엔진 차원의 완벽한 ACID 정합성 및 RPO=0 반동기 복제 지원</text>

  <!-- Layer 3: Storage Block -->
  <rect x="25" y="170" width="470" height="60" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="45" y="192" font-size="12" font-weight="bold" fill="#059669">3. 스토리지 블록 계층 (SAN 미러링, AWS EBS 복제, DRBD)</text>
  <text x="45" y="212" font-size="11" fill="var(--sl-color-text, #334155)">- OS/DBMS에 완전히 투명한 블록 I/O 미러링, 대용량 초고속 복제 및 DR 센터 구성</text>

  <defs>
    <marker id="arrow126" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **데이터의 무중단 고가용성(HA), 재해 복구(DR), 지리적 지연 단축 및 읽기 성능 확장을 위해 동일한 데이터셋의 최신 사본을 복수의 분산 노드 또는 원격 데이터센터에 실시간으로 유지하고 동기화하는 엔터프라이즈 인프라 핵심 기술**
- 암기: `애-디-스` (3대 구현 계층: 애플리케이션/CDC 계층, DBMS 엔진 계층, 스토리지 블록 계층) / `동-비-반` (동기화 3대 방식: 동기 Synchronous, 비동기 Asynchronous, 반동기 Semi-sync) / `스-엘-씨` (충돌 해결: Split-Brain 방지 쿼럼, Last-Write-Wins, CRDT)
- 판단축:
  - **스토리지 복제**: DBMS 종류 무관, OS 투명성 극대화, 단 동종 스토리지 필요 및 읽기 전용 인스턴스 기동 불가
  - **DBMS 엔진 복제**: 동종 DBMS 최적화, 보조 노드 읽기 트래픽 분산 가능, 반동기 복제로 RPO=0 달성
  - **CDC 복제**: 이기종 DBMS 간 복제 및 실시간 데이터 파이프라인 연계에 유일한 대안
- 주의: 데이터 복제는 시스템 장애를 극복하는 HA/DR 기술이지 '데이터 백업'을 대체할 수 없음 (운영 DB에서 `DROP TABLE` 발생 시 수 밀리초 만에 복제본까지 연쇄 삭제됨)
---

## 1교시 예상문제 (10점)

> 데이터 복제(Data Replication) 아키텍처와 계층별 복제 기술 및 DR 구축 전략의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 고가용성(HA)과 재해 복구(DR)를 위해 동일한 최신 데이터를 복수의 분산 노드 또는 원격 센터에 실시간 동기화 유지하는 기술 |
| **2. 3대 구현 계층** | - **스토리지 블록**: SAN 미러링, OS/DBMS 투명성, 전사 DR 센터 전용<br/>- **DBMS 엔진**: WAL/Binlog 스트리밍, 읽기 복제본 지원, RPO=0 반동기<br/>- **애플리케이션/CDC**: Debezium/Kafka, 이기종 DB 간 변환 및 이벤트 파이프라인 |
| **3. 동기 vs 비동기** | - 동기(Sync): 원격 ACK 후 커밋, RPO=0, 트랜잭션 지연 발생<br/>- 비동기(Async): 로컬 커밋 후 전송, 성능 우수하나 RPO>0 데이터 유실 가능 |
| **4. 충돌 및 장애 방지** | 3노드 쿼럼 기반 과반수 합의로 스플릿 브레인을 방지하고, 쓰기 리전 고정 샤딩으로 충돌 원천 차단 |
---

### 핵심 관계

| 비교 항목 | 스토리지 블록 복제 | DBMS 엔진 로그 복제 | CDC 애플리케이션 복제 |
|:---|:---|:---|:---|
| **복제 단위** | 디스크 블록(Block, 4KB/8KB) | 트랜잭션 로그(WAL, Redo, Binlog) | 테이블 단위 변경 이벤트(JSON/Avro) |
| **대표 기술** | EMC SRDF, NetApp SnapMirror, DRBD | PG Streaming Replication, MySQL Group | Debezium, Oracle GoldenGate, Kafka Connect |
| **DBMS 종속성** | **완전 독립** (어떤 DBMS도 가능) | 동종 동일 버전 DBMS 필수 | **이기종 DBMS 간 복제 가능** (Oracle $\rightarrow$ PG) |
| **보조노드 조회** | **불가** (블록 잠금으로 DB 기동 불가) | **가능** (Read Replica 활성화) | **가능** (실시간 조회 및 DW 적재) |
| **네트워크 부하** | 높음 (빈 블록까지 전송될 수 있음) | 중간 (로그 파일 압축 전송) | 낮음 (변경된 레코드 컬럼만 전송) |
| **적합한 영역** | 전사 차원의 무중단 원격 DR 센터 | 고가용성 HA 클러스터 및 읽기 분산 | MSA 간 이벤트 동기화 및 실시간 DW/Lake 적재 |

---

## 2~4교시 예상문제 (25점)

> 데이터베이스 및 스토리지 레벨에서의 데이터 복제(Data Replication) 기술 유형을 비교하고, 재해복구(DR) 센터 구축 시 RPO와 RTO 관점에서의 동기/비동기 복제 방식 선정 기준 및 충돌 해결 방안을 기술하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 무중단 비즈니스를 보장하는 데이터 복제(Data Replication) 개요

#### 한줄 요약: 시스템 장애와 재해로부터 무손실 회복탄력성을 확보하기 위해 복수의 이중화 노드에 데이터 사본을 유지하는 기술

- **배경**:
  - 단일 데이터 저장소에 하드웨어 장애, 지진/화재 등 물리적 재난 발생 시 데이터 영구 유실 및 서비스 전면 중단 초래
  - 글로벌 사용자 확대로 중앙 단일 DB로의 네트워크 왕복 지연(RTT) 증가 및 읽기 트랜잭션 집중 병목 발생
- **정의**: 원천(Primary) 노드에서 발생한 데이터 생성·수정·삭제 트랜잭션을 변경 로그 형태로 캡처하여 하나 이상의 복제 대상(Replica/Standby) 노드에 전송 및 반영하는 기술
- **핵심 목표**: 고가용성(HA), 무중단 재해 복구(DR), 읽기 트래픽 분산(Scale-out), 지리적 근접 서비스 제공

### Ⅱ. 데이터 복제의 3대 구현 계층 및 기술 메커니즘

#### 한줄 요약: 스토리지 블록 미러링, DBMS 내장 로그 스트리밍, 애플리케이션 CDC 계층의 상호보완적 공존

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="155" height="140" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="92" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 스토리지 계층</text>
  <text x="92" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">블록 I/O 미러링</text>
  <text x="92" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">SAN / SRDF / DRBD</text>
  <text x="92" y="110" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">DBMS 무관 투명성</text>
  <text x="92" y="135" text-anchor="middle" font-size="10" fill="#64748b">원격 DR 센터 전용</text>

  <!-- Box 2 -->
  <rect x="182" y="20" width="155" height="140" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="260" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. DBMS 엔진 계층</text>
  <text x="260" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">트랜잭션 로그 전송</text>
  <text x="260" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">WAL / Binlog 스트림</text>
  <text x="260" y="110" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">읽기 복제본(Read) 지원</text>
  <text x="260" y="135" text-anchor="middle" font-size="10" fill="#64748b">HA 클러스터 표준</text>

  <!-- Box 3 -->
  <rect x="350" y="20" width="155" height="140" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="427" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. CDC / 앱 계층</text>
  <text x="427" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">변경 데이터 캡처</text>
  <text x="427" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Debezium / Kafka</text>
  <text x="427" y="110" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">이기종 DB 간 변환</text>
  <text x="427" y="135" text-anchor="middle" font-size="10" fill="#64748b">MSA 이벤트 스트림</text>
</svg>
</div>

| 비교 항목 | 스토리지 블록 복제 | DBMS 엔진 로그 복제 | CDC 애플리케이션 복제 |
|:---|:---|:---|:---|
| **복제 단위** | 디스크 블록(Block, 4KB/8KB) | 트랜잭션 로그(WAL, Redo, Binlog) | 테이블 단위 변경 이벤트(JSON/Avro) |
| **대표 기술** | EMC SRDF, NetApp SnapMirror, DRBD | PG Streaming Replication, MySQL Group | Debezium, Oracle GoldenGate, Kafka Connect |
| **DBMS 종속성** | **완전 독립** (어떤 DBMS도 가능) | 동종 동일 버전 DBMS 필수 | **이기종 DBMS 간 복제 가능** (Oracle $\rightarrow$ PG) |
| **보조노드 조회** | **불가** (블록 잠금으로 DB 기동 불가) | **가능** (Read Replica 활성화) | **가능** (실시간 조회 및 DW 적재) |
| **네트워크 부하** | 높음 (빈 블록까지 전송될 수 있음) | 중간 (로그 파일 압축 전송) | 낮음 (변경된 레코드 컬럼만 전송) |
| **적합한 영역** | 전사 차원의 무중단 원격 DR 센터 | 고가용성 HA 클러스터 및 읽기 분산 | MSA 간 이벤트 동기화 및 실시간 DW/Lake 적재 |

### Ⅲ. 복제 동기화 3대 방식: 동기 vs 비동기 vs 반동기

#### 한줄 요약: 데이터 정합성(RPO)과 트랜잭션 응답 지연(Latency)의 트레이드오프

| 복제 방식 | 동작 원리 | 장점 | 단점 | DR 지표 (RPO) |
|:---|:---|:---|:---|:---:|
| **동기 복제 (Sync)** | Primary가 커밋하기 전 복제본 노드의 디스크 기록 완료 ACK를 수신해야 트랜잭션 종료 | 데이터 유실 제로 보장 (완벽한 일관성) | 네트워크 지연이 트랜잭션 시간에 직접 가산 (원거리 적용 불가) | **RPO = 0** |
| **비동기 복제 (Async)** | Primary가 로컬 커밋을 완료하고 클라이언트에 즉시 응답한 뒤, 백그라운드로 로그 전송 | 원천 트랜잭션 성능 영향 없음, 장거리 DR 적합 | Primary 장애 시 미전송분 유실 발생 위험 존재 | **RPO > 0** (초~분 단위 유실) |
| **반동기 복제 (Semi-Sync)** | 복제본 노드 최소 1개가 로그를 수신(릴레이 로그 기록)했다는 ACK만 받고 즉시 커밋 완료 | 동기 복제 대비 지연 단축 및 무유실 보장 | 1개 노드 네트워크 지연 시 일시적 지연 발생 | **RPO = 0** |

### Ⅳ. 고가용성(HA) 및 재해복구(DR) 연계 전략

#### 한줄 요약: 목표 복구 시점(RPO)과 복구 시간(RTO)에 따른 이중화 구조 선정

1. **RPO / RTO 핵심 지표 매핑**:
   - **RPO (Recovery Point Objective, 목표 복구 시점)**: 장애 발생 시 허용 가능한 최대 데이터 유실 허용치. 금융권 코어 뱅킹은 $\text{RPO} = 0$ 필수 (동기/반동기 복제 강제)
   - **RTO (Recovery Time Objective, 목표 복구 시간)**: 서비스가 중단된 시점부터 정상 가동될 때까지의 허용 시간. 자동 Failover 솔루션(Pacemaker, Patroni 등) 연계 필수
2. **이중화 토폴로지 비교**:
   - **Active-Standby (Hot-Standby)**: Primary만 쓰기를 처리하고 Standby는 복제만 수신하다가 장애 시 승격 (스플릿 브레인 방지 용이, 가장 안정적)
   - **Active-Active (Multi-Master)**: 복수의 노드가 동시에 쓰기/읽기를 처리하고 상호 복제 (확장성은 극대화되나 동시 수정 충돌 해결 알고리즘 필수)

### Ⅴ. 분산 복제 충돌 해결 전략 (Conflict Resolution)

#### 한줄 요약: 양방향 동시 쓰기 환경에서의 데이터 덮어쓰기 왜곡 방지 및 무결성 보장

1. **스플릿 브레인(Split-Brain) 방지**:
   - 네트워크 단절 시 독립된 두 노드가 각자 Primary로 승격하여 데이터가 분기되는 재앙 발생
   - **대책**: 3노드 이상의 홀수 쿼럼(Quorum, 과반수 투표) 체계를 구축하여 과반수의 지지를 얻은 노드만 Primary를 유지하도록 격리(STONITH/Fencing)
2. **동시 수정 충돌 해결 메커니즘**:
   - **LWW (Last Write Wins)**: 충돌 시 물리적 또는 논리적 타임스탬프가 가장 최신인 트랜잭션만 남기고 이전 덮어쓰기 (클럭 동기화 NTP 필수)
   - **리전 샤딩(Region Sharding)**: 고객 ID 해시를 기반으로 특정 데이터의 쓰기 권한을 단일 리전에만 배타적 할당하여 원천 충돌 배제
   - **CRDT (Conflict-free Replicated Data Types)**: 수학적으로 교환 법칙과 결합 법칙이 성립하는 특수 자료구조를 사용하여 중앙 조율 없이 자동 병합

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 복제 지연(Replication Lag) 해소, 이기종 DB 데이터 타입 비호환, Split-Brain 차단

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **복제 지연(Lag) 누적으로 읽기 불일치** | 대용량 배치성 UPDATE 실행 시 Standby가 단일 스레드로 릴레이 로그를 재생하며 지연 누적 | 병렬 복제(Multi-threaded Replication) 엔진 활성화 및 대량 배치는 청크 단위로 쪼개어 실행 |
| **이기종 DB 복제 시 타임스탬프/문자셋 왜곡** | Oracle의 `DATE` 타입(초 단위)과 PostgreSQL의 `TIMESTAMP`(마이크로초) 간 정밀도 차이 | CDC 전송 계층(Debezium)에서 스키마 레지스트리를 통해 데이터 타입 및 UTC 타임존 자동 변환 매핑 강제 |
| **네트워크 단절 시 데이터 분기** | 심장박동(Heartbeat) 두절로 Standby가 임의로 Primary로 승격하여 양쪽 모두에 독립 쓰기 발생 | Raft/Paxos 기반 3노드 쿼럼 합의를 의무화하고 하드웨어 전원 차단(Fencing) 에이전트 연동 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 많은 기업들이 화려한 "Active-Active 글로벌 다중 리전 복제"를 꿈꾸지만, 물리학적으로 서울과 미국 동부 사이의 빛의 속도 한계로 인한 네트워크 RTT(약 150ms)는 결코 극복할 수 없다.
> 대륙 간 동기 복제는 불가능하며, 비동기 복제 하에서의 Active-Active는 필연적으로 동시 수정 충돌(Conflict)을 야기한다.
> 따라서 실무에서 가장 우아하고 검증된 아키텍처는 **"리전 고정형 쓰기 샤딩 + 대륙 간 비동기 CDC 복제 + 원격 DR 스토리지 블록 미러링"**의 계층화된 하이브리드 조합이다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "데이터 거버넌스 및 규제 준수(Compliance) 관점의 복제 통제"를 제언하겠다. 금융보안원 DR 규정(RPO=0, RTO 2시간 이내)을 충족하기 위한 근거리 반동기 복제와 원거리 비동기 복제의 3센터(Center) 아키텍처(2DC + 1DR)를 제시하고, 유럽 GDPR 등 국경 간 데이터 이전 규제에 대응하기 위한 지역별 암호화 복제 파이프라인의 필수성을 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 금융 및 이커머스 핵심 업무의 영속성을 위해 단순 백업을 넘어 계층화된 고성능 데이터 복제 체계 구축이 필수적임.
- **대응**:
  1. **3-데이터센터(2DC+1DR) 구축**: 주센터-제2센터 간은 반동기 복제로 RPO 0 확보, 원격 DR 센터는 비동기 복제로 지연 최소화.
  2. **이기종 CDC 파이프라인 통합**: 분석용 DW 및 검색 엔진 연계를 위해 Debezium/Kafka 기반의 비동기 이벤트 복제 분리.
  3. **쿼럼 기반 스플릿 브레인 방지**: Patroni/Consul을 연계하여 3노드 과반수 합의 실패 시 장애 노드를 즉시 Fencing.
- **검증**: 분기 1회 모의 재해복구 훈련을 통해 실측 RTO 30분 이내 및 실측 RPO 0 검증.
- **효과**: 시스템 단일 장애점(SPOF) 원천 제거 및 99.999% 엔터프라이즈 비즈니스 연속성 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">단일 DB 장애 시 데이터 유실, 원거리 복제 시 트랜잭션 지연</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">근거리 반동기(RPO 0) + 원거리 비동기 3센터 복제 구축</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">모의 DR 훈련 실측(RTO &lt; 30분, RPO = 0), 복제 지연 &lt; 1초</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">엔터프라이즈 무중단 연속성 보장 및 읽기 성능 선형 확장</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제120회 정보관리 1교시: 데이터베이스 및 분산 시스템에서의 데이터 복제(Data Replication) 방식과 재해복구(DR) 적용 방안
- **검증 출처**:
  - Martin Kleppmann, "Designing Data-Intensive Applications", O'Reilly
  - PostgreSQL Global Development Group, "High Availability, Load Balancing, and Replication"
---

## 연결 토픽

- 상위 토픽: [03-051 고가용성(HA) 아키텍처](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/051_ha_architecture.md)
- 연관 토픽: [03-114 DB 복제 유형](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/114_db_replication_types.md), [03-149 분산 데이터베이스](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/149_distributed_database.md)
