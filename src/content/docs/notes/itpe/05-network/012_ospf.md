---
sidebar:
  order: 12
  label: "012. OSPF"
  badge:
    text: "기초"
    variant: note
title: "OSPF(Open Shortest Path First)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 12
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
  question_no: "012"
---

## 지식 로드맵 내 현재 위치

네트워크 → 내부 라우팅 → **OSPF**

## 30초 인출

- 본질: **OSPF** : 링크 상태를 공유한 뒤 각 라우터가 목적지까지의 최저 비용 경로를 계산하는 내부 라우팅 프로토콜
- 메커니즘: 인접 라우터 발견 → LSA 교환·LSDB 동기화 → SPF 계산 → 라우팅 테이블 반영
- 통찰: 거리 벡터의 라우팅 루프와 수렴 지연 문제를 극복하기 위해 다익스트라(Dijkstra) SPF 알고리즘으로 네트워크 전체 토폴로지 맵을 구축하고 Area 분할 구조로 대규모 엔터프라이즈의 확장성을 보장하는 링크 상태 라우팅 프로토콜임.

<details>
<summary>핵심 용어</summary>

- **OSPF(Open Shortest Path First)** : 링크 상태 데이터베이스와 최단 경로 우선 계산을 사용하는 내부 게이트웨이 프로토콜
- **LSA(Link State Advertisement)** : 라우터·네트워크의 링크 상태를 알리는 정보 단위
- **LSDB(Link State Database)** : 같은 영역의 라우터가 동기화하는 링크 상태 정보 집합
- **SPF(Shortest Path First)** : 링크 비용을 바탕으로 최단 경로 트리를 계산하는 알고리즘
- **Area(영역)** : 링크 상태 정보와 SPF 계산의 범위를 구분하는 OSPF 구성 단위
- **ABR(Area Border Router)** : 둘 이상의 OSPF 영역을 연결하는 라우터
- **ASBR(Autonomous System Boundary Router)** : 외부 경로 정보를 OSPF로 유입하는 라우터
- **DR/BDR(Designated Router/Backup Designated Router)** : 브로드캐스트·NBMA 망에서 인접 관계와 정보 교환을 조정하는 대표·예비 라우터

</details>

---

## 2~4교시 예상문제 (25점)

> 내부 라우팅 프로토콜(IGP)인 OSPF의 동작 원리, 계층적 Area 구조, LSA(Link State Advertisement) 유형 및 DR/BDR 선출 메커니즘을 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. OSPF(Open Shortest Path First)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 인터넷 표준 링크 상태(Link-State) 내부 게이트웨이 프로토콜(IGP)로서, 최단 경로 우선(SPF) 알고리즘을 사용하여 최적 경로를 계산하고 루프 프리(Loop-free) 라우팅을 제공하는 개방형 프로토콜 |
| 목적 | 홉수 제한(15)이 있는 RIP의 확장성 한계 극복, 토폴로지 변화 시 초고속 수렴(Fast Convergence) 및 링크 대역폭 기반 최적 경로 보장 |

## Ⅱ. OSPF(Open Shortest Path First)의 특징

| 특징 | 상세 내용 |
|---|---|
| 링크 상태 데이터베이스 | 모든 라우터가 네트워크 전체 토폴로지 맵(LSDB)을 동일하게 공유하여 전역 최단 경로 계산 |
| 다익스트라 SPF 알고리즘| 링크 비용(Cost = 기준대역폭/인터페이스대역폭)을 가중치로 삼아 자신을 루트로 하는 SPF 트리 도출 |
| 계층적 계층 구조(Area)| 백본 Area 0을 중심으로 영역을 분할하여 LSA 플러딩 범위를 국지화하고 라우팅 테이블 요약 지원 |
| 멀티캐스트 갱신 | 브로드캐스트 대신 전용 멀티캐스트 주소(224.0.0.5, 224.0.0.6)를 사용하여 비관계 호스트 부하 차단 |

## Ⅲ. OSPF(Open Shortest Path First)의 체계·프로세스

**OSPF 계층적 Area 분할 구조 및 라우터 역할**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ OSPF 계층적 Area 구조 ]                       │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ [ Area 0 : 백본 영역 (Backbone Area) ]                         │   │
│   │   - 모든 비백본 Area는 반드시 물리적/논리적으로 Area 0에 연결   │   │
│   │   - 백본 라우터(BR) 및 백본 코어 고속 스위치 동작              │   │
│   └──────────────┬───────────────────────────────┬─────────────────┘   │
│                  │ ABR (Area Border Router)      │ ABR                 │
│   ┌──────────────┴──────────────┐ ┌──────────────┴──────────────┐      │
│   │ [ Area 1 : 표준/스텁 영역 ] │ │ [ Area 2 : NSSA 영역 ]      │      │
│   │   - 내부 라우터 (Internal)  │ │   - ASBR (자율시스템 경계)  │      │
│   │   - LSA 1, 2, 3 플러딩      │ │   - 외부 BGP/RIP 경로 유입  │      │
│   └─────────────────────────────┘ └──────────────┬──────────────┘      │
│                                                  │ ASBR                │
│                                                  ▼                     │
│                                     [ 외부 도메인 (BGP, RIP, Static) ] │
└────────────────────────────────────────────────────────────────────────┘
```

| 라우터 역할 | 정의 및 위치 | 핵심 수행 기능 |
|---|---|---|
| **IR (Internal Router)** | 단일 Area 내부에만 모든 인터페이스가 속한 라우터 | 해당 Area 내부 LSDB 유지 및 SPF 연산 |
| **ABR (Area Border Router)** | Area 0과 하나 이상의 타 Area 경계에 걸친 라우터 | Area 간 LSA 요약(Type 3) 생성 및 전달 |
| **ASBR (AS Boundary Router)**| OSPF 도메인과 타 라우팅(BGP, 정적) 경계에 위치 | 외부 경로를 OSPF 내부로 재분배(Type 5/7 LSA) |
| **DR / BDR** | 브로드캐스트 멀티액세스 망에서 선출된 대표/부대표 | LSA 플러딩 중계로 인접 관계(Adjacency) 수 O(N^2)에서 O(N) 축소 |

## Ⅳ. OSPF(Open Shortest Path First)의 종류·비교

| 비교 항목 | RIP v2 | OSPF v2/v3 | BGP v4 |
|---|---|---|---|
| **라우팅 분류** | 거리 벡터 (Distance Vector) | 링크 상태 (Link State) | 경로 벡터 (Path Vector) |
| **적용 영역** | 소규모 소호/지사 망 (IGP) | 중대규모 엔터프라이즈 망 (IGP) | 인터넷 글로벌 백본망 (EGP) |
| **메트릭 기준** | 단순 홉 수 (Hop Count, 최대 15) | 링크 비용 (Cost = 10^8 / Bandwidth) | 다양한 AS Path 속성(AS-Path, MED, Local Pref) |
| **수렴 속도** | 느림 (30초 주기적 전체 전송) | 매우 빠름 (변화 시 LSA 즉시 플러딩)| 중간 (정책 기반 점진적 전파) |
| **알고리즘** | Bellman-Ford 알고리즘 | Dijkstra SPF 알고리즘 | Best Path Selection 규칙 |

## Ⅴ. OSPF(Open Shortest Path First)의 한계와 방안

| 한계 | 방안 |
|---|---|
| 네트워크 규모 확장 시 다익스트라 SPF 알고리즘의 CPU/메모리 부하 급증 (O(E log V)) | 네트워크를 다중 Area로 세분화하고 ABR에서 경로 축약(Route Summarization)을 강제 적용 |
| 대규모 브로드캐스트 이더넷 세그먼트에서 모든 라우터 간 완전 메시 LSA 교환 시 트래픽 폭증 | 우선순위(Priority) 및 Router-ID 기반 DR/BDR 선출을 통해 허브 앤 스포크 형태로 플러딩 최소화 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
10Gbps/100Gbps 고속 인터페이스를 사용하는 최신 데이터센터 환경에서는 OSPF 기본 참조 대역폭(Reference Bandwidth=100Mbps) 설정 시 100M 이상 모든 고속 링크의 Cost가 '1'로 동일해지는 현상이 발생하므로, 반드시 `auto-cost reference-bandwidth 100000`(100Gbps) 명령어로 기준 대역폭을 전사 통일 재설정.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ OSPF LSA (Link State Advertisement) 핵심 유형별 전파 범위 ]          │
│                                                                        │
│   Area 1 (일반 영역)        ABR (경계 라우터)        Area 0 (백본 영역)│
│   ┌─────────────────────┐    ┌─────────────┐    ┌──────────────────┐   │
│   │ Type 1: Router LSA  │───►│ LSA 1, 2 취합│───►│ Type 3: Summary  │   │
│   │ (자체 연결 링크 정보)│    │             │    │ LSA (Area 간 요약)│   │
│   │ Type 2: Network LSA │───►│             │    └──────────────────┘   │
│   │ (DR이 생성한 망 정보)│    └─────────────┘              │            │
│   └─────────────────────┘                                  │ ASBR      │
│                                                            ▼           │
│   Type 5: External LSA (외부 도메인 재분배 경로) ◄─────────────────────┘   │
│   (백본을 거쳐 전 Area로 플러딩, 스텁 영역에는 유입 차단)                 │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 특수 Area 유형 | 허용 LSA 유형 | 차단 LSA 유형 | 주 적용 목적 |
|---|---|---|---|
| **Stub Area** | Type 1, 2, 3, 기본경로 | Type 4, 5 (외부 경로 차단) | 지사 라우터 메모리 절감 |
| **Totally Stubby** | Type 1, 2, 기본경로 | Type 3, 4, 5 (타 Area 경로 차단) | 저사양 라우터 극단적 경량화 |
| **NSSA (Not-So-Stubby)**| Type 1, 2, 3, 7 (NSSA 외부) | Type 4, 5 차단 (Type 7을 5로 변환) | 지사에 소규모 외부망 연결 시 |

## 출제 이력과 검증 출처

- IETF RFC 2328: OSPF Version 2
- IETF RFC 5340: OSPF for IPv6 (OSPFv3)
- 정보관리기술사 기출(103회, 112회, 124회) 라우팅 프로토콜 출제 기준

## 연결 토픽

- 상위 토픽: [002 서브네팅](./002_subnetting.md)
- 연관 토픽: [017 OSI 7 계층](./017_osi_7_layer.md)
