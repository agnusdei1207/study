---
sidebar:
  order: 17
  label: "017. 고가용성 설계 - Active-Active•Active-Standby (High Availability Architecture)"
  badge:
    text: "기출 · 70%"
    variant: note
title: "무중단 시스템 이중화 및 장애 복구 : 고가용성 아키텍처 (Active-Active vs Active-Standby & 펜싱)"
date: "2026-09-07T14:00:00+09:00"
tags:
  - "notes-evaluation"
weight: 17
extra:
  question_no: "017"
  source_status: "기출"
  source_history: "135회, 137회"
  priority: 70
  priority_note: "135회·137회 반복 출제, 고가용성(HA: High Availability) 아키텍처 설계, Active-Active(무상태 계층, 100% 자원 활용, 부하 분산) vs Active-Standby(상태 저장 계층, Hot/Warm/Cold Standby, 단일 쓰기 보장), 하트비트(Heartbeat), 정족수 쿼럼(Quorum (N/2)+1), STONITH 펜싱(Fencing), 가상 IP(VIP) 페일오버 및 N-1 용량 설계"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **고가용성 아키텍처(High Availability Architecture / Active-Active & Active-Standby)**: 단일 장애점(SPOF)으로 인한 시스템 중단을 방지하고 99.99% 이상의 서비스 가용성을 보장하기 위해, 모든 인프라 계층(네트워크, 서버, 데이터베이스, 스토리지)을 이중화하고 장애 발생 시 자동 페일오버(Auto-Failover) 및 트래픽 재라우팅을 신속하게 집행하는 고신뢰성 아키텍처 설계 기법.
- **단일 장애점 중단 및 스플릿 브레인 데이터 오염 결함(SPOF Outage & Split-Brain Defect)**: 서버 1대 다운 시 전체 서비스가 마비되는 단일 장애점(SPOF) 결함이나, 이중화 환경에서 노드 간 하트비트 통신망 단절로 인해 양쪽 서버가 동시에 자신을 마스터로 선언하여 데이터베이스에 동시 쓰기를 수행함으로써 데이터가 영구적으로 파괴되는 구조적 결함.

</details>

- 정의/개념: 무중단 비즈니스 연속성을 달성하기 위해 **계층별 특성(Stateless vs Stateful) 분류 $\rightarrow$ 무상태 계층 Active-Active 부하 분산 $\rightarrow$ 상태 저장 계층 Active-Standby 동기 복제 $\rightarrow$ 하트비트 및 홀수 쿼럼($(N/2)+1$) 감시 $\rightarrow$ STONITH 노드 펜싱(Fencing) 기반 스플릿 브레인 방어 $\rightarrow$ 가상 IP(VIP) 자동 페일오버** 를 집행하는 **엔드투엔드 고가용성 엔지니어링 체계**
- 배경/필요성: 단일 서버나 인프라 노드 장애 시 전체 서비스가 즉각 중단되는 단일 장애점(SPOF) 결함이나, 이중화 환경에서 노드 간 하트비트 통신망 단절 시 양쪽 서버가 동시에 자신을 마스터로 선언하여 데이터베이스에 동시 쓰기를 수행함으로써 데이터를 영구 파괴하는 스플릿 브레인(Split-Brain) 재난이 발생하는 구조적 한계가 발생함에 따라, 무상태(Stateless) 계층에는 Active-Active 부하 분산을 적용하고 상태 저장(Stateful) 계층에는 Active-Standby 동기 복제와 홀수 쿼럼($(N/2)+1$) 및 STONITH 펜싱을 결합하는 고가용성(HA) 아키텍처를 도입하여 **단일 장애 발생 시 신속한 자동 페일오버(Auto-Failover), 스플릿 브레인 선제적 방어 및 N-1 예비 용량 확보를 통한 99.99% 이상의 무중단 비즈니스 연속성**을 달성할 필요

#### 한줄 요약
- 고가용성 설계는 Active-Active 및 Active-Standby 이중화와 펜싱 메커니즘을 통해 무중단 서비스 연속성을 보증한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **고가용성 2대 핵심 이중화 모델**:
  - **Active-Active (활성-활성)**: 모든 복제 노드가 동시 활성화되어 클라이언트 트래픽을 병렬 분산 처리하는 구조 (자원 활용률 100%).
  - **Active-Standby (활성-대기)**: 주 노드(Active)만 트래픽을 처리하고 대기 노드(Standby)는 실시간 데이터 복제만 유지하다가 장애 시 승격하는 구조 (단일 쓰기 보장).

</details>

- 무상태 A-A·상태 저장 A-S의 **계층별 이중화**
- 쿼럼과 STONITH를 결합한 **스플릿 브레인 억제**
- 노드 하나 없이 피크를 수용하는 **N-1 용량**

#### 한줄 요약
- 계층별 이중화 분리(무상태 A-A / 상태 A-S), 쿼럼 및 STONITH 펜싱, N-1 용량 확보를 제공한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **고가용성 4대 아키텍처 계층**:
  1. **Traffic & Routing Layer**: GSLB, Anycast BGP, L4/L7 로드밸런서 (VIP 바인딩).
  2. **Stateless Compute Layer**: Active-Active WAS/컨테이너 클러스터 (공유 세션 Redis).
  3. **Stateful Data Layer**: Active-Standby DBMS (Primary-Replica 반동기/동기 복제).
  4. **Cluster Management & Fencing Layer**: Pacemaker, Corosync, IPMI STONITH 펜싱.

</details>

```text
[고가용성 아키텍처]
├── [Traffic·Routing Layer]
│   └── VIP 및 로드밸런서 이중화
├── [Stateless Compute Layer]
│   └── Active-Active 부하 분산
├── [Stateful Data Layer]
│   └── Active-Standby 동기 복제
└── [Cluster Management Layer]
    └── 쿼럼 감시 및 STONITH 펜싱
```

- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| **Traffic·Routing Layer** | VIP와 로드밸런서 진입점 이중화 |
| **Stateless Compute Layer** | Active-Active 처리와 N-1 용량 확보 |
| **Stateful Data Layer** | Active-Standby 복제와 단일 쓰기 보장 |
| **Cluster Management·Fencing Layer** | 쿼럼 감시·페일오버·STONITH 집행 |

#### 한줄 요약
- 무상태 계층은 세션을 공유 저장소로 밀어내 어느 노드로 보내도 되게 만들었기에 Active-Active로 갈 수 있고, 상태를 옮길 수 없는 데이터 계층만 Active-Standby로 남아 대기 자원과 절체 시간을 치르며 그 전환의 안전은 쿼럼·펜싱 계층이 대신 보증한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **Active-Standby 자동 페일오버 5단계 수명주기 프로세스**:
  1. 평시 Primary DB(Active)와 Replica DB(Standby) 간 동기 복제 및 1초 주기 하트비트 교환
  2. Primary DB의 하드웨어 커널 패닉으로 하트비트 신호 유실 발생
  3. Corosync 쿼럼 클러스터가 3회 연속 타임아웃 감지 후 비정상 노드 확정
  4. 구 Primary 노드에 대해 IPMI STONITH 신호를 보내 전원을 강제 차단(펜싱)
  5. Replica 노드를 New Primary로 마스터 승격하고 VIP를 재할당하여 서비스 정상화

</details>

```text
1. [정상 가동 및 동기 복제 상태]
    ├─ Primary DB(Active, VIP 10.0.0.200 바인딩)가 모든 Read/Write 트랜잭션 전담
    ├─ Replica DB(Standby)로 트랜잭션 로그 실시간 동기 복제 (Sync Replication)
    └─ [전용 사설망을 통해 500ms 주기로 Corosync 하트비트 패킷 정상 교환]
            │
            ▼
2. [장애 발생 및 하트비트 유실 감지]
    ├─ 00:00:00 Primary DB 전원 공급장치 고장으로 셧다운
    ├─ 00:00:01.5 500ms 하트비트 3회 연속 실패 감지 (타임아웃)
    └─ [Corosync 쿼럼(3개 노드 중 2개 정상) 합의 ➔ Primary 장애 상태 최종 선언]
            │
            ▼
3. [STONITH 하드웨어 펜싱 집행]
    ├─ Pacemaker가 네트워크 분리(Split-Brain) 가능성을 배제하기 위해 펜싱 가동
    ├─ Primary 서버의 IPMI/BMC 원격 관리 포트로 전원 차단(Power Off) 명령 전송
    └─ [구 Primary의 스토리지 I/O 및 잔여 쓰기 시도를 물리적으로 안전하게 차단]
            │
            ▼
4. [마스터 승격 및 VIP 플로팅 인계]
    ├─ Replica DB의 WAL(Write-Ahead Log) 재실행 완료 및 최종 트랜잭션 정합성 검증
    ├─ Replica DB를 'New Primary (Read-Write Mode)'로 마스터 승격
    └─ [ARP 브로드캐스팅(Gratuitous ARP)을 통해 VIP(10.0.0.200)를 신규 마스터로 즉시 이전]
            │
            ▼
5. [서비스 정상화 및 RTO 달성]
    ├─ 애플리케이션 커넥션 풀이 신규 마스터로 자동 재연결 ➔ 트랜잭션 정상 재개
    ├─ 총 장애 복구 소요 시간: $\text{RTO} = 4.5\text{초}$, 데이터 손실량: $\text{RPO} \approx 0\text{초}$
    └─ [구 서버 수리 후 신규 Replica(Standby)로 클러스터에 안전 재편입(Failback)]
```

**동작 원리**

1. **정상 가동 및 동기 복제 상태**: 하트비트와 로그 복제
2. **장애 발생 및 하트비트 유실 감지**: 쿼럼으로 장애 확정
3. **STONITH 하드웨어 펜싱 집행**: 구 Primary 쓰기 차단
4. **마스터 승격 및 VIP 플로팅 인계**: Replica 승격
5. **서비스 정상화 및 RTO 달성**: 재연결과 Failback 준비

#### 한줄 요약
- 하트비트 유실만으로는 노드 사망인지 네트워크 단절인지 갈리지 않으므로, 승격 전에 STONITH로 구 Primary의 전원을 끊어 이중 쓰기 위험을 4.5초의 복구 시간 비용으로 바꾼다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **Active-Standby 3대 대기 방식(Hot vs Warm vs Cold) 비교**:
  - Hot Standby: 대기 서버가 상시 기동되어 데이터 동기화 완료 상태 (RTO 초 단위).
  - Warm Standby: 대기 서버 OS/미들웨어는 기동 중이나 앱/DB는 준비 상태 (RTO 수 분 단위).
  - Cold Standby: 대기 서버가 전원 OFF 상태로 장애 시 전원 투입 및 복원 (RTO 수 시간 단위).

</details>

| 비교 항목 | Active-Active (활성-활성) | Active-Standby: Hot Standby | Active-Standby: Cold Standby |
|:---|:---|:---|:---|
| **트래픽 처리** | **모든 노드가 실시간 병렬 처리**| **Active만 처리 (Standby는 복제만)**| Active만 처리 (Standby 전원 OFF)|
| **자원 활용률** | **100% (모든 자원 상시 가동)** | **50% (대기 서버 유휴 비용 발생)** | 50% (전원 차단으로 전기세 절감)|
| **복구 시간 (RTO)**| **지연 최소화 (즉시 나머지 노드가 수용)** | **초 단위 (1초 ~ 30초 내 승격)** | **수 시간 (장비 부팅 및 백업 복원)**|
| **데이터 손실 (RPO)**| **손실 최소화** | **손실 최소화 (동기 복제 시)** | 백업 주기만큼 손실 (수 시간) |
| **적합한 계층** | **웹 서버, API Gateway, NoSQL** | **RDBMS (Oracle, MySQL, PostgreSQL)**| 비핵심 배치 서버, 개발/검증 환경 |
| **구축 복잡도** | 세션 공유 및 동기화 설계 복잡 | **클러스터 쿼럼 및 펜싱 구성 필요**| 단순 수동 복구 절차 |

#### 한줄 요약
- Active-Active는 무상태 병렬 처리(RTO 0초), Hot Standby는 상태 저장 단일 쓰기(RTO 초 단위), Cold Standby는 저비용 예비용이다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **N-1 여유 용량(Headroom)**: 클러스터 내 1대 노드가 다운되어도 나머지 N-1개 노드가 CPU/메모리 임계치를 초과하지 않고 피크 트래픽을 감당할 수 있도록 평상시 확보해 두는 유휴 자원 마진이다.
- **연쇄 붕괴(Cascading Failure)**: 단일 노드의 장애로 인한 초과 트래픽이 잔여 노드로 급격히 몰리면서 남은 노드들이 차례대로 과부하 다운되는 현상이다.
- **공유 세션(Shared Session, Redis Cluster)**: 개별 WAS 인스턴스의 로컬 힙 메모리에 세션을 저장하지 않고 외부의 고성능 분산 인메모리 저장소에 중앙 집중화하여 무상태(Stateless) 아키텍처를 구현하는 기법이다.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| Active 노드 1대 장애 시 남은 1대 노드의 CPU가 100% 포화되어 **클러스터 전체가 도미노처럼 연쇄 붕괴(Cascading Failure)하는 결함 발생** | **평시 가동률을 50% 이하로 통제하고 1대 장애 시에도 피크 부하를 수용할 수 있는 N-1 용량 사이징(Headroom) 강제** | 단일 노드 셧다운 시 무중단 연속성 안정적 보장 |
| 노드 간 하트비트 전용 랜선 장애로 상호 통신이 단절되어 **두 서버가 모두 마스터로 동작하며 스플릿 브레인(Split-Brain) 데이터 영구 파괴 발생** | **3개 이상의 홀수 쿼럼(Quorum) 클러스터를 구성하고 IPMI 기반 STONITH 하드웨어 펜싱 필수 구현** | 다중 마스터 출현 및 데이터 충돌 위험 선제적 방지 |
| Active-Active WAS 구성에서 로컬 메모리에 세션을 저장하여 **로드밸런서가 다른 서버로 라우팅할 때마다 사용자의 로그인이 강제 풀리는 현상 발생** | **WAS 계층을 무상태(Stateless) 구조로 전환하고 분산 메모리 캐시(Redis Cluster)에 공유 세션 중앙 집중화** | 세션 무결성 유지 및 유연한 오토스케일링 달성 |

#### 한줄 요약
- N-1 용량으로 연쇄 붕괴를 막고, 쿼럼/STONITH로 스플릿 브레인을 방어하며, Redis로 세션을 중앙 집중화한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **멀티 가용영역(Multi-AZ, Multi Availability Zone)**: 단일 데이터센터 재해에 대비하여 동일 리전 내에서 전력, 냉각, 통신망이 완전히 독립된 2개 이상의 데이터센터에 인프라를 분산 배치하는 구조이다.
- **서비스 메시(Service Mesh)**: 마이크로서비스 간의 통신을 사이드카 프록시(Envoy)를 통해 관리하며 로드밸런싱, 장애 감지, mTLS 암호화, 서킷 브레이커를 인프라 레벨에서 자동 제공하는 계층이다.
- **STONITH(Shoot The Other Node In The Head)**: 스플릿 브레인이 의심되는 비정상 노드의 전원(IPMI/PDU)을 물리적으로 차단하여 공유 스토리지 쓰기를 원천 봉쇄하는 펜싱 기법이다.

</details>

- 단일 결함에 의한 서비스 중단 위험을 배제하고 99.99% 이상의 무중단 연속성을 수학적·구조적으로 보증하는 **무중단 시스템 이중화 및 장애 복구(High Availability Architecture / Active-Active & Active-Standby / Quorum & STONITH)의 핵심 인프라 표준**으로 확고히 자리 잡았으며, 클라우드 멀티 가용영역(Multi-AZ) 오토스케일링 및 글로벌 서비스 메시로 진화하는 가운데, 실무 고가용성 설계 및 구축 시에는 **무상태 웹/WAS의 Active-Active 및 Redis 공유 세션 중앙화, 상태 저장 DBMS의 홀수 쿼럼 기반 STONITH 하드웨어 펜싱을 통한 스플릿 브레인 방어, 단일 노드 셧다운 시에도 피크 트래픽을 안정적으로 수용하는 N-1 여유 용량(Headroom) 사이징**을 결합하여 시스템 복원력과 무중단 서비스 연속성을 체계적으로 완성해야 한다.

#### 한줄 요약
- 계층별 이중화 구조와 쿼럼 펜싱 메커니즘을 통해 무중단 고가용성 시스템을 체계적으로 완성해야 한다.
