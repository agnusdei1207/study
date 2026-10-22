---
title: "상호연결망(Interconnection Network)"
author: "agnusdei1207"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 상호연결망(Interconnection Network)의 개요

- 핵심 요약 : **상호연결망**은 멀티코어·다중 프로세서·AI 클러스터 간 데이터/제어 메시지를 고속·저지연으로 전달하는 네트워크 토폴로지 인프라.
- 개념 : 멀티코어 프로세서 내부의 코어 간 통신(NoC: Network-on-Chip)부터, 다중 프로세서 시스템(SMP/NUMA(Non-Uniform Memory Access)), 슈퍼컴퓨터 및 수만 대의 AI(Artificial Intelligence) 가속기 클러스터 노드 간에 데이터와 제어 메시지를 고속·저지연으로 전달하기 위해 스위치, 라우터, 링크를 유기적으로 연결한 **네트워크 토폴로지** 및 통신 인프라.
- 배경 및 필요성 : 분산 컴퓨팅 및 딥러닝 분산 학습의 규모가 수만 개 노드로 확장됨에 따라, 시스템 전체의 성능이 개별 프로세서의 연산 속도보다 노드 간 상호연결망의 대역폭과 지연 시간(Bisection Bandwidth, Latency)에 의해 결정되는 **네트워크 바운드** (Network-Bound) 현상 심화.
- 핵심 목적 : **네트워크 직경** (Diameter) 최소화, **이등분 대역폭** (Bisection Bandwidth) 극대화, 링크 장애 시의 경로 우회 복원력(Fault-Tolerance) 확보.

## Ⅱ. 상호연결망(Interconnection Network)의 특징 및 장점

- 핵심 요약 : **정적(Direct) vs 동적(Indirect) 토폴로지·웜홀 스위칭**.
1. **정적 vs 동적 토폴로지** : 프로세서 노드가 라우팅 기능까지 겸하여 직접 링크로 연결되는 **정적 연결망**과, 노드와 전용 스위치 패브릭이 분리되어 다단계 스위칭을 거치는 **동적 연결망**으로 대별.
2. **웜홀 스위칭** (Wormhole Switching) : 패킷을 작은 **플릿** (Flit: Flow Control Unit) 단위로 쪼개어, 헤드 플릿이 라우터를 통과하며 경로를 설정하면 중간 버퍼링 없이 나머지 바디 플릿들이 뱀처럼 파이프라인으로 관통하여 버퍼 소모와 지연 시간 극소화.

## Ⅲ. 상호연결망(Interconnection Network)의 구조 및 동작 메커니즘

- 핵심 요약 : **정적(Direct) vs 동적(Indirect) 토폴로지 + 웜홀 스위칭**.
- 상호연결망은 정적 연결망(Mesh/Torus/Ring/Hypercube)과 동적 연결망(Crossbar/Clos/Fat-Tree)으로 분류되며, 웜홀 스위칭으로 지연을 극소화함.

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 상호연결망 2대 토폴로지 분류 및 패킷 라우팅 메커니즘 ]              │
│                                                                        │
│   [ 1. 정적 연결망 (Direct / Static Topology) ]                        │
│    - 노드와 노드가 점대점(Point-to-Point) 링크로 직접 연결            │
│    - 대표 구조: 2D/3D Mesh, Torus, Ring, Hypercube                     │
│                                                                        │
│   [ 2. 동적 연결망 (Indirect / Dynamic Topology) ]                      │
│    - 중간에 스위치(Switch) 스테이지를 거쳐 동적으로 경로를 형성        │
│    - 대표 구조: Crossbar Switch, Clos / Fat-Tree, Butterfly            │
│                                                                        │
│   ─── [ 웜홀 스위칭 (Wormhole Switching) 메커니즘 ] ────────────────   │
│                                                                        │
│   전체 패킷 ──> [헤드 플릿(Head Flit)] [바디 플릿(Body)] [테일 플릿(Tail)]│
│                       │ 라우팅 정보 포함                               │
│                       ▼                                                │
│      [Router 1] ───> [Router 2] ───> [Router 3] ───> [목적지 도착]     │
│      * 헤드가 길을 열면 바디/테일 플릿이 버퍼링 없이 파이프라인으로 통과 │
└────────────────────────────────────────────────────────────────────────┘
```

## Ⅳ. 상호연결망(Interconnection Network)의 비교

- 핵심 요약 : **Crossbar·Fat-Tree·Torus·Hypercube·Mesh** 직경·차수·이등분 대역폭·적용 비교.

| 토폴로지 명칭 | 네트워크 직경 (Diameter) | 노드당 차수 (Degree) | 이등분 대역폭 (Bisection Bandwidth) | 주요 적용 시스템 |
| :--- | :--- | :--- | :--- | :--- |
| **크로스바 스위치** (Crossbar) | 1 (최단 지연) | $N$ (입출력 포트 수) | 최고 (논블로킹 완전 연결) | 소규모 SMP 서버 버스, NVSwitch |
| **팻 트리** (Fat-Tree) | $2 \log_k (N/2)$ | 고정 스위치 라디스 | 논블로킹(Non-blocking) 보장 가능 | 데이터센터 AI 클러스터 (InfiniBand) |
| **2D / 3D 토러스** (Torus) | $k \cdot n / 2$ | $2n$ (고정 차수: 4 or 6) | 중간 ~ 높음 (랩어라운드 링크) | 슈퍼컴퓨터 (후가쿠 Tofu, IBM(International Business Machines) BlueGene) |
| **하이퍼큐브** (Hypercube) | $\log_2 N$ | $\log_2 N$ (차수 가변) | 높음 | 초기 병렬 슈퍼컴퓨터 |
| **2D 메시** (2D-Mesh) | $2(k - 1)$ | 2 ~ 4 (경계 노드 비대칭) | 낮음 (코너 노드 병목) | 칩 내부 통신 (Network-on-Chip: NoC) |

## Ⅴ. 상호연결망(Interconnection Network)의 한계와 방안

- 핵심 요약 : **데드락/라이브락·핫스팟/인캐스트·케이블링 비용**을 DOR·ECN/PFC·Dragonfly/CPO로 대응.

- 패킷 순환 대기로 인한 데드락(Deadlock) 및 라이브락(Livelock) :
  - 한계점 : 버퍼가 가득 찬 라우터들이 서로 상대방의 버퍼가 비기를 기다리며 순환 대기하여 패킷 전송이 영구 마비.
  - 해결 방안 : 차원 순서 라우팅(DOR: X축 우선 이동 후 Y축 이동)으로 사이클 원천 배제, 가상 채널(Virtual Channel) 분할을 통한 회피.
- 네트워크 핫스팟(Hotspot) 및 인캐스트(Incast) 혼잡 :
  - 한계점 : 다수의 송신 노드가 단일 목적지 노드로 동시에 응답을 쏟아부을 때 스위치 버퍼가 넘쳐 대규모 패킷 드롭 발생.
  - 해결 방안 : 명시적 혼잡 알림(ECN/PFC: Priority Flow Control) 기반 동적 혼잡 제어 및 적응형 라우팅(Adaptive Routing) 적용.
- 클러스터 확장 시 케이블링 비용 및 물리적 배선 복잡도 폭증 :
  - 한계점 : 팻 트리 3계층 구축 시 필요한 수만 개의 광 트랜시버와 케이블 비용이 전체 서버 비용을 초과.
  - 해결 방안 : 케이블 수를 줄이면서 직경을 좁히는 드래곤플라이(Dragonfly) 토폴로지 도입 또는 광-전기 융합 CPO(Co-Packaged Optics) 채택.

## Ⅵ. 상호연결망(Interconnection Network) 적용 제언

- 핵심 요약 : **레일 최적화 팻 트리·Ultra Ethernet**.
- 레일 최적화 팻 트리(Rail-Optimized Fat-Tree) 구축 : 동일 순번 GPU를 독립 스위치 레일로 묶어 트래픽 간섭 배제.
- 차세대 울트라 이더넷(Ultra Ethernet Consortium) 생태계 대비 : UEC 1.0 표준 선제 검증 및 단계적 도입.

## Ⅶ. 결론

- 핵심 요약 : 상호연결망은 **토폴로지·스위칭·라우팅**으로 네트워크 직경·이등분 대역폭·복원력을 최적화하나 데드락·핫스팟·케이블링 리스크 관리가 필수.
- 상호연결망은 토폴로지와 스위칭·라우팅으로 네트워크 직경·이등분 대역폭·복원력을 최적화하지만, 데드락·핫스팟·케이블링 비용 리스크를 DOR·ECN/PFC·Dragonfly/CPO로 관리해야 함.
- 답안에는 정적/동적 토폴로지, 웜홀 스위칭, 5대 토폴로지 비교, 한계·대응, 레일 최적화·Ultra Ethernet 제언을 연결. (Network-on-Chip, NoC) (Bisection Bandwidth) (Wormhole Switching) (Flit, Flow Control Unit) (DOR, Dimension-Order Routing) (ECN, Explicit Congestion Notification) (PFC, Priority Flow Control) (Dragonfly) (CPO, Co-Packaged Optics) (Ultra Ethernet Consortium, UEC)