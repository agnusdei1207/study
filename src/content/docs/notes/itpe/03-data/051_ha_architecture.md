---
sidebar:
  order: 51
  label: "051. 고가용성(HA) 아키텍처"
  badge:
    text: "A"
    variant: note
title: "고가용성(HA) 아키텍처 및 페일오버(Failover) 무중단 체계"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 51
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "051"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>분산 데이터베이스·고가용성</span><strong>고가용성(HA) 아키텍처</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-box" role="img" aria-label="고가용성 클러스터 아키텍처 및 자동 페일오버 절체 흐름도">
<svg viewBox="0 0 520 230" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-ha" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
    <filter id="shadow-ha" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="rgba(0,0,0,0.1)"/>
    </filter>
  </defs>

  <!-- 상단 VIP / L4 로드밸런서 -->
  <rect x="150" y="15" width="220" height="34" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" filter="url(#shadow-ha)"/>
  <text x="260" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">가상 IP (VIP) / L4/L7 스위치</text>
  <text x="260" y="44" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">클라이언트 단일 진입점</text>

  <!-- 정상 라우팅 & 절체 라우팅 화살표 -->
  <path d="M 210 50 L 110 75" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2" marker-end="url(#arrow-ha)"/>
  <text x="145" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-accent, #2563eb)">정상 라우팅 (VIP)</text>

  <path d="M 310 50 L 410 75" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-ha)"/>
  <text x="375" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="#ef4444">장애 시 VIP 절체</text>

  <!-- Active 노드 -->
  <rect x="25" y="78" width="170" height="65" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" filter="url(#shadow-ha)"/>
  <text x="110" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Active 노드 (Master)</text>
  <text x="110" y="114" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">Write / Read 트랜잭션</text>
  <text x="110" y="128" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">Pacemaker / Keepalived</text>

  <!-- Standby 노드 -->
  <rect x="325" y="78" width="170" height="65" rx="6" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5" filter="url(#shadow-ha)"/>
  <text x="410" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Standby 노드 (Slave)</text>
  <text x="410" y="114" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="#10b981" text-anchor="middle">실시간 로그 반영 대기</text>
  <text x="410" y="128" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">장애 감지 시 마스터 승격</text>

  <!-- 상호 하트비트 & 복제 -->
  <path d="M 195 95 L 325 95" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="260" y="90" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#f59e0b" text-anchor="middle">Heartbeat (헬스체크)</text>

  <path d="M 195 120 L 325 120" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-ha)"/>
  <text x="260" y="115" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">실시간 복제 (Semi-Sync)</text>

  <!-- 하단 방어 메커니즘 바 -->
  <rect x="25" y="155" width="470" height="28" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="#ef4444" stroke-width="1.2"/>
  <text x="260" y="173" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#ef4444" text-anchor="middle">스플릿 브레인 방어: 3노드 쿼럼(Quorum, N/2+1) 다수결 합의체 + STONITH 물리 전원 차단</text>

  <rect x="15" y="193" width="490" height="26" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="260" y="210" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">가용도 목표: 99.999% (Five-Nines, 연간 다운타임 5.26분 이내) ── RTO 수 초 / RPO=0 보장</text>
</svg>
</div>

- 본질: **단일 장애점(SPOF, Single Point of Failure)을 제거하기 위해 하드웨어·네트워크·데이터베이스 전 계층을 다중화하고, 하트비트 감시와 자동 페일오버(Failover)를 통해 연간 가용률 99.999%(Five-Nines) 수준의 무중단 서비스를 제공하는 인프라 및 데이터 아키텍처**
- 암기: `단-다-감-절` (단일장애점 제거, 다중화/복제, 상태 감시, 자동 절체) / `스-쿼-스-펜` (스플릿 브레인, 쿼럼 합의, STONITH, 펜싱)
- 판단축:
  - **Active-Active**: 모든 노드가 동시에 트랜잭션을 처리하여 자원 효율과 부하분산이 극대화되나, 분산 락 및 데이터 동기화 복잡성 증가
  - **Active-Standby (Hot Standby)**: 주 노드만 쓰기를 수행하고 대기 노드는 복제 상태를 유지하여 구조가 단순하고 안정적이나, 유휴 자원 비용 발생
- 주의: 자동 페일오버 설계 시 하트비트 네트워크 일시 단절로 양 노드가 동시에 Active로 승격되는 **스플릿 브레인(Split-Brain)** 발생 위험을 차단하기 위해 3노드 이상 쿼럼(Quorum) 또는 물리적 펜싱(STONITH)이 필수적임
---

## 1교시 예상문제 (10점)

> 고가용성(HA) 아키텍처 및 페일오버(Failover) 무중단 체계의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. 고가용성(HA)의 정의 및 가용도 평가 공식

- **정의**: 단일 장애점(SPOF)을 제거하고 자동 절체를 통해 연간 가용률 99.999%(Five-Nines)의 무중단 서비스를 제공하는 아키텍처
- **가용도 공식**: $\text{Availability} (A) = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\%$ (MTTR 단축이 핵심)

### 2. Active-Active vs Active-Standby 핵심 비교

- **핵심 구조 비교**:
  - Active-Active: 모든 노드 Write/Read 수행, 자원 활용률 100%, RTO $\approx$ 0, 분산 락 복잡도 극대
  - Active-Standby: Active만 Write 수행, Standby 실시간 대기, 자원 활용률 50%, 안정적 운영

| 구분 | Active - Active | Active - Standby (Hot) |
|---|---|---|
| **트랜잭션 처리** | 전 노드 Write/Read 동시 처리 | Active만 Write, Standby 대기 |
| **자원 활용률** | **100%** (상시 부하분산) | **약 50%** (대기 노드 유휴) |
| **절체 시간 (RTO)** | **RTO $\approx$ 0** (즉시 리디렉션) | **RTO 수 초~수십 초** (승격 소요) |
| **아키텍처 복잡도** | 극도로 높음 (분산 락 충돌) | 상대적 단순, 신뢰성 검증됨 |

### 3. 차별화 제언

- 페일오버 시 스플릿 브레인을 방지하기 위해 **홀수 쿼럼(N/2+1)과 STONITH 물리 펜싱**을 결합하고, **Chaos Mesh 기반 정기 장애 주입**으로 실측 RTO를 검증함
---

## 2~4교시 예상문제 (25점)

> 데이터베이스 및 엔터프라이즈 시스템의 서비스 연속성을 보장하기 위한 고가용성(HA) 아키텍처의 개념과 가용도 평가 지표를 제시하고, Active-Active 및 Active-Standby 구성 모델의 메커니즘을 비교한 후, 페일오버 시 발생하는 스플릿 브레인(Split-Brain) 현상의 방지 방안을 설명하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 단일 장애점(SPOF)을 극복하는 고가용성(HA) 개요

- **추진 배경**:
  - 금융, 전자상거래, 미션 크리티컬 인프라에서 수 분간의 시스템 정지는 천문학적인 금전적 손실과 대외 신뢰도 추락을 초래함
  - 특정 단일 부품이나 서버 1대의 결함이 전체 서비스 중단으로 번지는 단일 장애점(SPOF)의 원천 배제가 필수적임
- **고가용성(HA, High Availability)의 정의**:
  - 정보시스템이 장애 발생 시에도 사람의 개입 없이 정상적인 운영 상태를 유지하거나, 허용된 목표 복구 시간(RTO) 내에 자동으로 복구되어 지속적인 서비스를 제공하는 능력
- **시스템 가용도(Availability) 공식**:
  $$\text{Availability} (A) = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\%$$
  - **MTBF (Mean Time Between Failures)**: 평균 무고장 시간 (시스템의 신뢰성 지표)
  - **MTTR (Mean Time To Repair)**: 평균 수리·복구 시간 (시스템의 유지보수성 및 HA 절체 속도 지표)

| 가용도 등급 | 백분율 (%) | 연간 허용 다운타임 (Downtime) |
|---|---|---|
| **Two-Nines** | 99.0% | 약 3.65일 (87.6시간) |
| **Three-Nines** | 99.9% | 약 8.76시간 |
| **Four-Nines** | 99.99% | 약 52.6분 |
| **Five-Nines** | **99.999%** | **약 5.26분 (HA 아키텍처의 표준 목표)** |
| **Six-Nines** | 99.9999% | 약 31.5초 |

#### 한줄 요약

- 고가용성은 전 계층 다중화와 자동 절체를 통해 MTTR을 최소화하여 연간 다운타임을 5분 이내(Five-Nines)로 억제하는 아키텍처임

### Ⅱ. HA 아키텍처의 핵심 구성요소 및 시스템 토폴로지

<div class="itpe-diagram-box" role="img" aria-label="고가용성 클러스터 계층 구조도">
<svg viewBox="0 0 520 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-hatopo" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
  </defs>

  <!-- 4계층 블록 -->
  <rect x="20" y="15" width="480" height="32" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="35" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">[네트워크 계층]</text>
  <text x="145" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">VIP (Virtual IP), Anycast BGP, L4/L7 스위치, Keepalived VRRP</text>

  <path d="M 260 47 L 260 58" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-hatopo)"/>

  <rect x="20" y="58" width="480" height="32" rx="4" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="35" y="78" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)">[클러스터 제어]</text>
  <text x="145" y="78" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">Heartbeat 감시망, Pacemaker 리소스 관리자, Corosync 멤버십 엔진</text>

  <path d="M 260 90 L 260 101" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-hatopo)"/>

  <rect x="20" y="101" width="480" height="32" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="35" y="121" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">[데이터 복제 계층]</text>
  <text x="145" y="121" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">동기(Sync) / 반동기(Semi-Sync) 트랜잭션 로그 스트리밍 (WAL, Binlog)</text>

  <path d="M 260 133 L 260 144" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-hatopo)"/>

  <rect x="20" y="144" width="480" height="32" rx="4" fill="var(--sl-color-gray-6, #f8fafc)" stroke="#ef4444" stroke-width="1.2"/>
  <text x="35" y="164" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#ef4444">[스토리지 및 펜싱]</text>
  <text x="145" y="164" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">SAN/NAS 공유 스토리지 및 STONITH (IPMI / iLO 원격 물리 전원 차단 장치)</text>
</svg>
</div>

| 구성 요소 | 역할 및 핵심 기능 | 대표 기술 / 솔루션 |
|:---|:---|:---|
| **가상 IP (VIP)** | 클라이언트가 특정 물리 노드에 종속되지 않고 접속할 수 있도록 동적으로 이동하는 대표 IP 주소 | Keepalived, VRRP |
| **클러스터 매니저** | 노드 간 상호 헬스체크(Heartbeat)를 수행하고 상태 전이 및 리소스 제어를 총괄 | Pacemaker, Corosync |
| **하트비트 (Heartbeat)** | 노드 간의 생존 여부와 네트워크 무결성을 확인하기 위해 주기적으로 주고받는 제어 패킷 | 전용 인터커넥트 LAN, 링 토폴로지 |
| **복제 엔진 (Replication)** | Active의 트랜잭션 로그(WAL, Binlog)를 Standby로 실시간 전송하여 데이터 일치 유지 | MySQL Group Replication, PostgreSQL Streaming Replication |
| **펜싱 (Fencing)** | 장애가 의심되는 구 노드가 공유 스토리지나 네트워크에 쓰기 작업을 수행하지 못하도록 물리적으로 강제 차단 | STONITH (IPMI, iLO), SAN Switch 바인딩 해제 |

#### 한줄 요약

- HA 시스템은 가상 IP, 하트비트 클러스터 매니저, 데이터 복제 엔진, STONITH 펜싱의 4대 계층이 유기적으로 결합되어 구동됨

### Ⅲ. 페일오버(Failover) 동작 절차 및 스플릿 브레인 방지 메커니즘

### 1. 자동 페일오버 5단계 프로세스

1. **[1단계: 장애 발생]**: 주 노드(Active) 하드웨어 결함 또는 커널 패닉 발생
2. **[2단계: 장애 감지]**: Standby 노드가 Heartbeat 신호 타임아웃 감지 (예: 3초 무응답)
3. **[3단계: 노드 펜싱]**: 쿼럼 합의 후 STONITH 명령으로 Active 노드 IPMI 전원 강제 OFF (격리)
4. **[4단계: 노드 승격]**: Standby 노드가 Master 역할로 전환 (Read-Write 모드 활성화)
5. **[5단계: VIP 인계]**: ARP 브로드캐스트(GARP)를 통해 VIP를 신규 Master로 재할당 후 서비스 재개

### 2. 스플릿 브레인(Split-Brain) 현상 및 3대 방지 대책

- **스플릿 브레인의 본질**:
  - 노드 간 하트비트 전용 네트워크가 단절되었으나 각 노드 자체는 정상 동작 중일 때 발생
  - 양쪽 노드가 서로 "상대방이 다운되었다"고 오판하여 **둘 다 Active로 승격**
  - 클라이언트 요청이 양쪽으로 분산 쓰기되어 **데이터베이스 정합성이 영구적으로 파괴(데이터 분기)**되는 치명적 재난 초래
- **스플릿 브레인 3대 방지 대책**:
  1. **쿼럼(Quorum) 다수결 합의체**: 클러스터 노드 수를 홀수(최소 3노드 이상)로 구성하여 과반수($N/2 + 1$) 이상을 확보한 파티션만 Active 권한 획득 (2노드 시 Witness/Arbiter 노드 배치 필수)
  2. **STONITH (Shoot The Other Node In The Head)**: 쿼럼을 확보한 노드가 베이스보드 관리 컨트롤러(IPMI, iLO)를 통해 상대방 노드의 물리 전원을 즉각 차단
  3. **하트비트 통신망 다중화**: 단일 LAN에 의존하지 않고, 듀얼 NIC 본딩 및 디스크 공유 하트비트(Disk Heartbeat)를 동시 운용

#### 한줄 요약

- 하트비트 두절 시 양쪽이 마스터로 승격되는 스플릿 브레인은 3노드 홀수 쿼럼 다수결과 STONITH 물리 전원 차단으로 원천 봉쇄함

### Ⅳ. HA 구성 패턴 비교: Active-Active vs Active-Standby

| 비교 항목 | Active - Active (멀티 마스터) | Active - Standby (Hot Standby) |
|:---|:---|:---|
| **트랜잭션 처리** | 모든 노드가 쓰기(Write)/읽기(Read) 동시 수행 | Active 노드만 Write 수행, Standby는 대기(또는 Read-Only) |
| **자원 활용률** | **100%** (모든 하드웨어 자원을 상시 활용) | **50% 수준** (대기 노드의 컴퓨팅 자원이 유휴 상태) |
| **장애 시 절체 시간** | **RTO $\approx$ 0** (트래픽을 정상 노드로 즉시 리디렉션) | **RTO 수 초~수 분** (헬스체크 판정 + 승격 + VIP 이동 소요) |
| **데이터 동기화** | 멀티 마스터 양방향 복제 및 분산 락(Distributed Lock) 필수 | 마스터 $\rightarrow$ 슬레이브 단방향 트랜잭션 로그 스트리밍 |
| **아키텍처 복잡도** | **극도로 높음** (동시 쓰기 충돌 해결, 네트워크 분할 대응) | **상대적으로 낮음** (검증된 상용/오픈소스 솔루션 풍부) |
| **대표 사례** | Oracle RAC, MySQL Group Replication, Cassandra | PostgreSQL Patroni, MySQL MHA/Orchestrator, Redis Sentinel |

- **Active-Standby 3가지 대기 모드**:
  - Hot Standby: 대기 노드가 항상 부팅되어 있고 실시간 로그를 반영하여 즉각 승격 가능 ($RTO \le 10$초)
  - Warm Standby: 시스템은 켜져 있으나 복제 데이터가 주기적(배치)으로 갱신되어 최신화 절차 필요 ($RTO \le$ 수 분)
  - Cold Standby: 전원이 꺼져 있거나 백업만 보관되어 서버 기동 및 복원이 수반됨 ($RTO \ge$ 수 시간)

#### 한줄 요약

- Active-Active는 자원 100% 활용 대신 분산 락 복잡성을 감수하고, Active-Standby는 유휴 자원을 대가로 단순성과 높은 안정성을 확보함

### Ⅴ. 고가용성(HA) vs 재해복구(DR) 비교 및 RTO/RPO 지표 분석

| 구분 | 고가용성 (HA, High Availability) | 재해복구 (DR, Disaster Recovery) |
|:---|:---|:---|
| **대상 장애 수준** | 부품 고장, 단일 서버 장애, 프로세스 다운, 로컬 스위치 불량 | IDC 정전, 화재, 지진, 사이버 테러 등 센터 전체 마비 |
| **물리적 거리** | 동일 랙(Rack), 동일 센터, 또는 인접 가용영역(AZ, 수십 ms 이내) | 원격지 데이터센터 (물리적 거리 30km~수백 km 이상 격리) |
| **복제 메커니즘** | **동기(Sync) / 반동기(Semi-Sync)** 네트워크 복제 | 지연 시간(Latency) 극복을 위한 **비동기(Async)** 스토리지 복제 |
| **복구 목표 시간 (RTO)** | **수 초 ~ 수 분** 이내 (시스템 기반 자동 페일오버) | **수 분 ~ 수 시간** (경영진 재해 선언 및 비상 운영 매뉴얼 수행) |
| **복구 목표 시점 (RPO)** | **$RPO = 0$** (트랜잭션 유실 절대 불가 원칙) | $RPO \approx 0$ 또는 허용된 복제 지연 분량 유실 가능 |

#### 한줄 요약

- HA는 동일 센터 내 장비 장애에 대응하는 단거리 자동 절체($RPO=0$)이고, DR은 광역 재난에 대비한 원격지 복구 체계임

### Ⅵ. 실무 데이터베이스 HA 구축 시 장애 패턴 및 튜닝 전략

| 문제 상황 | 근본 원인 | 실무 엔지니어링 대책 | 개선 효과 |
|---|---|---|---|
| **페일오버 시 트랜잭션 유실 (Split Data)** | 비동기 복제 환경에서 미전송 트랜잭션 로그가 존재하는 상태로 승격 | **반동기 복제(Semi-Sync)** 적용 (최소 1개 슬레이브 ACK 확인 후 커밋) | RPO=0 무손실 달성 |
| **잦은 절체로 인한 플래핑 (Flapping)** | 일시적 네트워크 스파이크(1~2초) 시 조급한 페일오버 트리거 | 하트비트 타임아웃 윈도우 적정화(3~5회 연속 실패 시 판정) 및 **수동 페일백 정책** | 불필요한 커넥션 단절 차단 |
| **스플릿 브레인에 의한 데이터 오염** | 하트비트 단절 시 양 노드가 상호 Active로 승격 | 3노드 **Raft 쿼럼 합의체** + IPMI 기반 **STONITH 펜싱** 필수화 | 데이터 분기 원천 배제 |
| **DNS 캐시 고정으로 인한 절체 지연** | VIP 대신 DNS 기반 절체 시 클라이언트/OS DNS TTL 캐싱으로 구 마스터 접근 | **GARP(Gratuitous ARP) 기반 VIP 인계** 및 클러스터 커넥션 풀 강제 리셋 | 페일오버 RTO 10초 이내 보장 |

#### 한줄 요약

- Semi-Sync 복제를 통한 RPO=0 확보, 하트비트 윈도우 튜닝으로 플래핑 방지, GARP 기반 VIP 즉시 인계가 실무 HA의 핵심임

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> "검증되지 않은 고가용성은 그저 심리적 위안에 불과하다." 수많은 기업이 수억 원을 들여 HA 클러스터를 구축해 놓고도 실제 장애가 터졌을 때 페일오버 스크립트 오작동, 방화벽 미개방, 스플릿 브레인 발생으로 수 시간 이상 서비스를 마비시킨다. 진짜 HA 엔지니어링은 다중화 장비를 갖추는 데서 끝나는 것이 아니라, 평상시 프로덕션 비수기 구간에 의도적으로 마스터 노드 전원을 내리는 **카오스 엔지니어링(Chaos Engineering)**을 통해 자동 절체의 실효성과 RTO/RPO 실측치를 주기적으로 증명하는 데 있다.

> **[나라면 이렇게 쓴다]**
> 25점 답안 4단락 차별화로 "전 계층 엔드투엔드(End-to-End) HA 매핑 및 카오스 엔지니어링 실증 체계"를 제시하겠다. DB 계층의 HA만으로는 전체 가용성을 보장할 수 없으므로, DNS(Anycast) $\rightarrow$ GSLB/L4 $\rightarrow$ Web/WAS $\rightarrow$ DB $\rightarrow$ 공유 스토리지 전 계층에 걸쳐 단일 장애점(SPOF)이 완전히 제거되었는지 매핑하고, Chaos Mesh 도구를 파이프라인에 통합하여 주 1회 가상 장애 주입을 수행하는 무결성 검증 체계를 제언한다.

### 실전 답안용 기술사적 제언

- **[HA 절체 검증 부재에 따른 실무 장애 장기화 한계]**: 다중화 구성에도 불구하고 실제 장애 시 스크립트 오류, 플래핑, 스플릿 브레인으로 인한 RTO 지연 발생
- **[실무 최적화 방안]**: Semi-Sync 복제 기반 $RPO=0$ 확립, 3노드 쿼럼 및 STONITH 펜싱 표준화, 수동 페일백 정책으로 안정성 확보
- **[카오스 엔지니어링 기반 상시 실증 체계]**: Chaos Mesh/LitmusChaos를 활용한 정기 무작위 장애 주입으로 실측 RTO(&le; 10초) 검증 및 전 계층 SPOF 제로화

<div class="itpe-flow-map" role="group" aria-label="고가용성 체계 고도화 4단계 흐름">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">1</div>
    <div class="itpe-flow-step__title">현행 한계</div>
    <div class="itpe-flow-step__desc">비동기 복제 트랜잭션 유실 및 하트비트 두절 시 스플릿 브레인 위험</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">2</div>
    <div class="itpe-flow-step__title">개선 방안</div>
    <div class="itpe-flow-step__desc">Semi-Sync 복제 + 3노드 Raft 쿼럼 및 STONITH 하드웨어 펜싱 도입</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">3</div>
    <div class="itpe-flow-step__title">검증 기준</div>
    <div class="itpe-flow-step__desc">자동 절체 RTO &le; 10초, 데이터 유실 RPO=0, 플래핑 발생률 0%</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">4</div>
    <div class="itpe-flow-step__title">실행 효과</div>
    <div class="itpe-flow-step__desc">연간 가용률 99.999%(Five-Nines) 달성 및 무중단 비즈니스 연속성 보장</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- 정보관리기술사 제138회 3교시 4번: 가용성 보장 및 HA 아키텍처
- 컴퓨터시스템응용기술사 제128회 1교시: HA 구성 방식과 SPOF 제거 전략
- Red Hat Enterprise Linux High Availability Add-On Architecture Guide
- Pacemaker & Corosync High Availability Cluster Project Documentation

## 연결 토픽

- [분산 데이터베이스 투명성](./025_distributed_db_transparency/) · [샤딩](./045_sharding/) · [CAP·PACELC 이론](./113_cap_pacelc/) · [오픈소스 DBMS 전환](./063_opensource_dbms_migration/)
