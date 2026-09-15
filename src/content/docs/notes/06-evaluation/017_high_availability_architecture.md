---
sidebar:
  order: 17
  label: "017. 고가용성 설계 - Active-Active•Active-Standby (High Availability Architecture)"
  badge:
    text: "기출 · 70%"
    variant: note
title: "무중단 시스템 이중화 및 장애 복구 : 고가용성 아키텍처 (Active-Active vs Active-Standby & 펜싱)"
date: "2026-09-15T09:29:00+09:00"
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
| Traffic·Routing Layer | VIP와 로드밸런서 진입점 이중화 |
| Stateless Compute Layer | Active-Active 처리와 N-1 용량 확보 |
| Stateful Data Layer | Active-Standby 복제와 단일 쓰기 보장 |
| Cluster Management·Fencing Layer | 쿼럼 감시·페일오버·STONITH 집행 |

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
[정상 가동] (Primary DB 활성 및 Replica DB 실시간 동기 복제)
 └── [장애 감지] (① 하트비트 3회 실패 및 Corosync 쿼럼 합의)
      └── [노드 펜싱] (② 구 Primary에 IPMI STONITH 전원 차단 집행)
           └── [마스터 승격] (③ WAL 로그 정합성 검증 및 Replica 승격)
                └── [VIP 이전] (④ Gratuitous ARP 기반 VIP 신규 마스터 할당)
                     └── [서비스 정상화] (⑤ 커넥션 풀 재연결 및 Failback 준비)
```

- 분기 결과: 쿼럼 확보 시 4.5초 내 자동 페일오버 완결, 쿼럼 미달 시 스플릿 브레인 방지를 위해 클러스터 쓰기 중단.

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
| 트래픽 처리 | **모든 노드가 실시간 병렬 처리** | **Active만 처리 (Standby는 복제만)** | Active만 처리 (Standby 전원 OFF) |
| 자원 활용률 | **100% (모든 자원 상시 가동)** | **50% (대기 서버 유휴 비용 발생)** | 50% (전원 차단으로 전기세 절감) |
| 복구 시간 (RTO) | **지연 최소화 (즉시 나머지 노드가 수용)** | **초 단위 (1초 ~ 30초 내 승격)** | **수 시간 (장비 부팅 및 백업 복원)** |
| 데이터 손실 (RPO) | **손실 최소화** | **손실 최소화 (동기 복제 시)** | 백업 주기만큼 손실 (수 시간) |
| 적합한 계층 | **웹 서버, API Gateway, NoSQL** | **RDBMS (Oracle, MySQL, PostgreSQL)** | 비핵심 배치 서버, 개발/검증 환경 |
| 구축 복잡도 | 세션 공유 및 동기화 설계 복잡 | **클러스터 쿼럼 및 펜싱 구성 필요** | 단순 수동 복구 절차 |

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
| 노드 1대 다운 시 초과 트래픽으로 **클러스터 연쇄 붕괴 발생** | 평시 가동률 50% 통제 및 **N-1 여유 용량(Headroom)** 확보 | **잔여 노드 과부하** 방지 |
| 하트비트 단절로 동시 쓰기 발생하여 **스플릿 브레인 데이터 파괴** | **홀수 쿼럼((N/2)+1) 구성 및 IPMI STONITH** 펜싱 강제 | **이중 마스터 출현** 차단 |
| WAS 로컬 메모리 세션 저장으로 **라우팅 변경 시 로그인 풀림** | 무상태(Stateless) 전환 및 **Redis 클러스터 세션 공유** | **세션 연속성 및 무중단 스케일링** |

#### 한줄 요약
- N-1 용량으로 연쇄 붕괴를 막고, 쿼럼/STONITH로 스플릿 브레인을 방어하며, Redis로 세션을 중앙 집중화한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **멀티 가용영역(Multi-AZ, Multi Availability Zone)**: 단일 데이터센터 재해에 대비하여 동일 리전 내에서 전력, 냉각, 통신망이 완전히 독립된 2개 이상의 데이터센터에 인프라를 분산 배치하는 구조이다.
- **서비스 메시(Service Mesh)**: 마이크로서비스 간의 통신을 사이드카 프록시(Envoy)를 통해 관리하며 로드밸런싱, 장애 감지, mTLS 암호화, 서킷 브레이커를 인프라 레벨에서 자동 제공하는 계층이다.
- **STONITH(Shoot The Other Node In The Head)**: 스플릿 브레인이 의심되는 비정상 노드의 전원(IPMI/PDU)을 물리적으로 차단하여 공유 스토리지 쓰기를 원천 봉쇄하는 펜싱 기법이다.

</details>

- **기술 위상/발전**: 단일 장애점(SPOF)을 제거하고 비즈니스 연속성을 담보하는 **고가용성 인프라 엔지니어링 표준**으로 정착, 멀티 AZ 오토스케일링 및 글로벌 서비스 메시와 연계 발전
- **실무 적용/통제**: 인프라 구축 시 **무상태 계층 Active-Active 및 Redis 공유 세션 적용**, 상태 저장 DB의 **홀수 쿼럼 기반 STONITH 펜싱으로 스플릿 브레인 방어**, 단일 노드 고장 대비 **N-1 여유 용량(Headroom) 확보** 필수

#### 한줄 요약
- 계층별 이중화 구조와 쿼럼 펜싱 메커니즘을 통해 무중단 고가용성 시스템을 체계적으로 완성해야 한다.
