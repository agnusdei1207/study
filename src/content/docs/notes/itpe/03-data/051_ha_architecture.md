---
title: "고가용성 아키텍처(HA, High Availability)"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 무중단 비즈니스를 위한 고가용성 아키텍처(HA) 개요

### 가. 고가용성(High Availability, HA)의 정의
- **고가용성** : 시스템, 네트워크, 애플리케이션 또는 데이터베이스가 특정 하드웨어 결함이나 소프트웨어 장애가 발생하더라도 정상적인 서비스 제공 상태를 지속적으로 유지할 수 있도록 **이중화** 및 **장애 복구** 체계를 갖춘 아키텍처.
- 통상 연간 다운타임 허용치를 기준으로 'Five Nines'(99.999%, 연간 장애 시간 5.26분 이내) 달성을 목표로 함.

### 나. 가용성 평가 핵심 지표

```text
[ HA 핵심 평가 공식 ]
                MTBF (평균 무고장 시간)
  가용도 (A) = -----------------------------
               MTBF + MTTR (평균 수리 복구 시간)
  * MTBF (Mean Time Between Failures) : 시스템이 정상 작동한 평균 시간 (극대화 필요)
  * MTTR (Mean Time To Repair)         : 장애 발생 후 정상 복구까지 소요된 시간 (극소화 필요)
```

---

## Ⅱ. 고가용성 클러스터 구성 유형 및 메커니즘

### 가. HA 클러스터 3대 구성 토폴로지

```text
[ HA 클러스터링 모델 ]
(A) Active-Standby (Cold / Warm / Hot)
    [Active Node] ===(Heartbeat / Data Sync)===> [Standby Node]
    (정상 시 모든 트래픽 처리)                     (장애 시 페일오버 대기)

(B) Active-Active (부하 분산)
    [Active Node 1] <--- [L4/L7 Load Balancer] ---> [Active Node 2]
    (양 노드가 동시 서비스 처리, 상호 백업)
```

| 구성 모델 | 동작 메커니즘 | 장점 | 트레이드오프 및 한계 |
| :--- | :--- | :--- | :--- |
| **Active - Hot Standby** | Standby 노드가 가동 상태로 데이터를 실시간 동기화하며 대기 | 페일오버 시간(RTO, Recovery Time Objective) 수초 이내로 극히 짧음 | Standby 노드의 컴퓨팅 자원이 유휴 상태로 방치되어 비용 비효율 |
| **Active - Active** | 복수의 노드가 트래픽을 분산 처리하며 서로의 예비 노드 역할 수행 | 자원 활용률 100%, 전체 처리량(Throughput) 증대 | 노드 간 동기화 오버헤드, 한 노드 장애 시 남은 노드의 부하 2배 급증 |
| **Active - Warm Standby** | Standby 노드가 켜져 있으나 애플리케이션은 비활성 상태 | Hot 대비 인프라 비용 절감 | 앱 기동 및 캐시 로딩에 수분가량의 RTO 소요 |

### 나. 장애 감지 및 페일오버 핵심 기술
- **하트비트(Heartbeat)** : 노드 간 전용 네트워크 링크를 통해 상태 신호를 주기적 교환.
- **스플릿 브레인(Split-Brain) 방어** : 네트워크 단절 시 양 노드가 모두 자신을 Active로 인식하여 데이터를 덮어쓰는 재앙을 막기 위해 **쿼럼** (Quorum) 기반 과반수 투표 또는 **펜싱** (STONITH: Shoot The Other Node In The Head) 메커니즘 적용.

---

## Ⅲ. 복구 목표 지표(RPO/RTO)와 재해복구(DR) 연계

### 가. RPO vs RTO 정의

```text
[ 재해 복구 타임라인 ]
-------[정상 운영]-------> [재해 발생] ------[복구 작업]------> [서비스 정상화]
                                |<-------- RTO -------->| (복구 소요 시간)
            |<------ RPO ------>|
            (데이터 유실 허용 시점)
```

- **RPO (Recovery Point Objective)** : 장애 발생 시 감내할 수 있는 최대 데이터 손실 시점(데이터 유실량).
- **RTO (Recovery Time Objective)** : 서비스가 중단된 시점부터 정상 복구될 때까지 허용되는 최대 중단 시간.

---

## Ⅳ. 고가용성 아키텍처(HA) 구축 및 운영의 주요 한계점 및 해결 방안

- 스플릿 브레인(Split-Brain) 현상으로 인한 데이터 정합성 파괴 :
  - 한계점 : 클러스터 노드 간 하트비트 네트워크가 단절될 경우 양측 모두 자신이 활성(Active) 마스터로 승격하여 서로 다른 쓰기를 수행, 데이터 분기 및 손실 발생.
  - 해결 방안 : 쿼럼(Quorum, 과반수 합의) 메커니즘 필수 적용(홀수 노드 구성), 펜싱(STONITH / Shoot The Other Node In The Head) 하드웨어 차단 장치 연동.
- 페일오버(Failover) 시점의 RPO/RTO 지연 및 세션 유실 :
  - 한계점 : 비동기 복제 환경에서 장애 발생 시 복제되지 못한 트랜잭션 유실(RPO > 0) 및 헬스체크 임계치 판정 및 승격 시간 동안 서비스 중단(RTO 지연).
  - 해결 방안 : 동기식 복제(Sync Replication) 또는 Raft 기반 합의 엔진 적용, 자동 DNS(Domain Name System)/가상 IP(VIP(Virtual IP)) 스위칭 및 클라이언트 자동 재연결(Reconnection) 풀 구성.
- 액티브-스탠바이(Active-Standby) 자원 유휴화 및 클라우드 비용 낭비 :
  - 한계점 : 정상 운영 시 스탠바이 서버가 아무런 트래픽도 처리하지 않고 대기하여 인프라 비용 효율성이 낮은 수준으로 급락.
  - 해결 방안 : 액티브-액티브(Active-Active) 멀티 리전 아키텍처로 전환, 읽기 전용 쿼리를 분산하는 세컨더리 복제본(Read Replica) 트래픽 분산 활용.

---

## Ⅴ. 클라우드 네이티브 HA 구축을 위한 실무 제언

- 다중 가용영역(Multi-AZ, Availability Zone) 액티브-액티브 배포 : 단일 데이터센터 장애에 대비하여 AWS(Amazon Web Services), Azure 등 클라우드의 3개 이상 가용영역(AZ)에 상태 비저장(Stateless) 웹/앱 컨테이너를 분산 배치하고, DB(Database)는 Multi-AZ 자동 동기식 복제를 적용해야 함.
- 카오스 엔지니어링(Chaos Engineering) 상시화 : 실제 장애 발생 시 HA(High Availability) 메커니즘이 정상 작동하는지 검증하기 위해 Chaos Mesh나 Chaos Monkey를 도입하여 운영 환경에서 무작위로 인스턴스를 강제 종료하는 카오스 테스트를 정례화할 것을 제언함.
