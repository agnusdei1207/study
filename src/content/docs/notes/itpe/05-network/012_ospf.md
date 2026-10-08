---
title: "OSPF(Open Shortest Path First)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. OSPF(Open Shortest Path First)의 개요

- 개념 : 대규모 **자율 시스템(AS: Autonomous System)** 내부에서 최적의 라우팅 경로를 결정하기 위해 다익스트라(Dijkstra)의 **최단 경로 우선(SPF(Shortest Path First))** 알고리즘을 사용하며, **링크 상태(Link-State)** 정보를 모든 라우터에 플러딩하여 **수렴(Convergence)** 속도를 극대화한 IETF(Internet Engineering Task Force) 표준 개방형 **내부 게이트웨이 프로토콜** (IGP).
- 배경 및 필요성 : 기존 **거리 벡터(Distance-Vector)** 프로토콜인 RIP(Routing Information Protocol)의 최대 15홉 제한, 느린 수렴 속도, 라우팅 루프 취약성 및 대역폭 미고려 단점을 극복하고 수백 대 이상의 대형 네트워크를 안정적으로 지원하기 위해 등장함.
- 핵심 목적 : 수렴 후 루프 없는 최단 경로 계산, 링크 변경 시 빠른 수렴, 계층적 영역(Area) 분할을 통한 대규모 엔터프라이즈 및 데이터센터 네트워크 확장성 보장.

## Ⅱ. OSPF(Open Shortest Path First)의 핵심 아키텍처 및 동작 메커니즘

OSPF(Open Shortest Path First)는 Hello 패킷을 통해 인접 관계(Neighbor/Adjacency)를 형성하고, LSA(Link-State Advertisement)를 플러딩하여 전체 토폴로지 데이터베이스(LSDB)를 동일하게 동기화한 뒤 SPF 알고리즘으로 라우팅 테이블을 도출함.

```text
[ OSPF 계층적 Area 구조 및 동작 메커니즘 ]

+-----------------------------------------------------------------+
|                   Area 0 (Backbone Area: 백본 영역)             |
|   +-------------------+                +-------------------+    |
|   | ABR (Area Border Router) | <============> | ABR (Area Border Router) |    |
|   +-------------------+                +-------------------+    |
+-------------│────────────────────────────────────│──────────────+
              │                                    │
              ▼                                    ▼
+-----------------------------+    +------------------------------+
| Area 1 (Standard Area)      |    | Area 2 (NSSA Area)    |
|  [Internal Router]          |    |  +--------------------+      |
|         │                   |    |  | ASBR (Autonomous System Boundary Router) |      |
|         ▼                   |    |  +---------│----------+      |
|  (Type 1/2 LSA 교환)        |    |            │ (타 라우팅 연동)|
|  * 동일 Area 내 완벽한      |    |            ▼                 |
|    동일 LSDB 보유           |    |   [ 외부 AS: BGP or RIP ]    |
+-----------------------------+    +------------------------------+

[ 라우터 간 인접 상태 전이 ]
Down -> Init -> 2-Way (DR/BDR 선출) -> ExStart -> Exchange -> Loading -> Full (완전 인접)
```

- **계층적 Area 구조** : 모든 서브 Area(Standard, Stub, NSSA 등)는 반드시 중앙의 백본 영역(Area 0)과 물리적 또는 가상(Virtual-Link)으로 직접 연결되어 라우팅 정보 집약 수행.
- **LSDB(Link-State Database) 동기화** : 모든 라우터가 자신의 링크 상태(인터페이스 IP(Internet Protocol), 대역폭 코스트, 이웃 정보)를 Type 1~7 LSA로 생성 및 플러딩하여 Area 내 모든 라우터가 동일한 지도 보유.
- **다익스트라 SPF 알고리즘** : 자신을 루트(Root)로 하는 최단 경로 트리(Shortest Path Tree)를 계산하여 목적지별 링크 코스트 합이 최소인 경로 도출. 참조 대역폭을 인터페이스 대역폭으로 나누는 방식은 장비의 기본 산정 방식이며 OSPF 표준의 유일한 공식은 아님.
- **DR(Designated Router)/BDR(Backup Designated Router) 선출** : 브로드캐스트 멀티액세스 망에서 라우터 간 인접 관계가 $N(N-1)/2$로 폭증하는 것을 방지하기 위해 대표 라우터(DR)와 백업 라우터(BDR)를 선출하여 인접 수렴.

## Ⅲ. OSPF(Open Shortest Path First)의 세부 구성 요소 및 비교 분석

| 비교 항목 | OSPF (Open Shortest Path First) | RIP (Routing Information Protocol) | BGP (Border Gateway Protocol) |
|---|---|---|---|
| 프로토콜 분류 | Link-State IGP (내부 게이트웨이) | Distance-Vector IGP | Path-Vector EGP (외부 게이트웨이) |
| 경로 계산 메트릭 | 링크 코스트 (대역폭 역수 기반) | 홉 수 (Hop Count: 최대 15홉) | AS-Path, Local Pref 등 복합 속성 |
| 알고리즘 | Dijkstra SPF 최단 경로 알고리즘 | Bellman-Ford 거리 벡터 | Best Path 선택 알고리즘 |
| 수렴 속도 | 매우 빠름 (링크 변화 시 즉시 LSA) | 느림 (30초 주기 전체 테이블 전송)| 보통 ~ 느림 (글로벌 안정성 우선) |
| 라우팅 루프 | 수렴 후 루프 방지, 수렴 중 일시적 루프 가능 | 루프 취약 (Split-Horizon 필요) | AS-Path 기반 루프 원천 방지 |
| 네트워크 규모 | 대규모 엔터프라이즈 및 데이터센터 | 소규모 단순 네트워크 (15홉 미만) | 전 세계 인터넷 백본 및 AS 간 연동 |

- OSPF는 링크 대역폭을 정밀 반영한 최단 경로 연산과 Area 분할을 통한 계층적 확장성을 바탕으로 현대 내부 기업망 및 데이터센터 언더레이(Underlay)의 절대적 표준으로 군림함.

- OSPF의 링크 코스트는 관리 가능한 메트릭이며 변경·재수렴 중의 일시적 동작도 검증 필요. [RFC 2328](https://www.rfc-editor.org/rfc/rfc2328).

## Ⅳ. OSPF(Open Shortest Path First)의 주요 한계점 및 해결 방안

- 대규모 망에서 토폴로지 변경 시 LSA 플러딩 및 SPF 재연산 부하 :
  - 한계점 : 링크 플래핑(Flapping) 발생 시마다 전체 라우터가 SPF 연산을 반복 수행하여 CPU(Central Processing Unit) 사용률 급증 및 패킷 포워딩 지연.
  - 해결 방안 : LSA 수신 및 SPF 연산 지연 타이머(SPF Throttle Timer) 지수 백오프 적용, Area 분할 및 ABR 경로 집약(Route Summarization).
- 브로드캐스트 네트워크에서 DR/BDR 선출 오버헤드 및 고정 Priority 문제 :
  - 한계점 : DR 장애 시 BDR 승격 및 신규 BDR 선출 과정에서 수렴 지연 발생.
  - 해결 방안 : 점대점(Point-to-Point) 링크 모드 강제 적용으로 DR/BDR 선출 절차 완전 생략, 양방향 포워딩 감지(BFD) 연동으로 밀리초 절체.
- Area 0 물리적 연속성 단절 시 라우팅 단절 위험 :
  - 한계점 : 백본 영역이 두 개로 분할될 경우 Area 간 통신이 전면 마비되는 구조적 제약.
  - 해결 방안 : OSPF Virtual-Link를 통한 논리적 백본 연결 임시 구성 및 이중화 백본 물리 토폴로지 구축.

## Ⅴ. OSPF(Open Shortest Path First) 적용 및 발전을 위한 기술사적 제언

- 데이터센터 Clos 스파인-리프(Spine-Leaf) 언더레이 설계 최적화 : BGP 오버레이(EVPN-VXLAN(Virtual Extensible LAN))와의 연동을 위해 모든 링크를 Point-to-Point로 설정하고 코스트를 통일하여 ECMP(Equal-Cost Multi-Path) 부하 분산 극대화.
- BFD(Bidirectional Forwarding Detection) 연동을 통한 서브세컨드 장애 복구 : OSPF Hello 타이머(기본 10초)의 느린 감지를 보완하기 위해 하드웨어 기반 BFD를 결합하여 50ms 이내 초고속 절체 달성 권장.
- OSPFv3 기반 IPv4(Internet Protocol version 4)/IPv6(Internet Protocol version 6) 통합 라우팅 단일화 : IPv6 이행 가속화에 대응하여 단일 OSPFv3 프로세스 내에서 Address Families(AF)를 활성화하여 프로토콜 운영 복잡도 경감.
