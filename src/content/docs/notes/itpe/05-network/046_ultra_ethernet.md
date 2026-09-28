---
title: "Ultra Ethernet (UEC)"
author: "Antigravity"
date: "2026-09-24T21:17:00+09:00"
tags:
  - "notes-network"
sidebar:
  label: "046. Ultra Ethernet (UEC)"
  badge:
    text: "서브"
    variant: note
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 데이터센터 패브릭 → **Ultra Ethernet (UEC)**

## 30초 인출

- 본질: **Ultra Ethernet** : 대규모 AI 분산 학습 및 HPC 워크로드 처리를 위해 기존 이더넷의 한계를 극복하고 개방형 초고속 패브릭 스택을 표준화한 UEC 컨소시엄 규격
- 메커니즘: UET 전송 계층에서 패킷 스프레잉(Packet Spraying), 비순서 수신(Out-of-Order), 신속 혼잡 통보(Fast Congestion Notification) 수행
- 통찰: RoCEv2의 무손실 네트워크 의존성(PFC 데드락)과 플로우 단위 해시 편향(ECMP 충돌)을 해소하기 위해 패킷 단위 분산 전송과 유연한 하드웨어 재정렬을 표준화한 오픈 패브릭 규격임.

<details>
<summary>핵심 용어</summary>

- **UEC (Ultra Ethernet Consortium)** : AI 및 고성능 컴퓨팅(HPC)을 위한 차세대 이더넷 표준을 개발하는 글로벌 산업 컨소시엄
- **UET (Ultra Ethernet Transport)** : 패킷 손실에 탄력적이며 비순서 수신을 기본 지원하는 초고속 전송 계층 프로토콜
- **Packet Spraying** : 대용량 플로우를 단일 경로로 보내지 않고 패브릭 내 사용 가능한 모든 다중 경로에 패킷 단위로 분산 송출하는 기술
- **RoCEv2 (RDMA over Converged Ethernet)** : UDP/IP 기반의 무손실 이더넷 환경에서 구동되는 기존 RDMA 프로토콜
- **PFC (Priority Flow Control)** : 특정 우선순위 큐에 혼잡 발생 시 일시 정지(PAUSE) 프레임을 보내 패킷 드롭을 막는 무손실 L2 흐름 제어

</details>

---

## 2~4교시 예상문제 (25점)

> 대규모 생성형 AI 클러스터를 위한 Ultra Ethernet(UEC)의 등장 배경, 핵심 아키텍처(UET 전송 계층), RoCEv2 및 InfiniBand와의 비교, 실제 도입 시 한계와 기술적 해결 방안을 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. Ultra Ethernet (UEC)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 리눅스 재단 산하 Ultra Ethernet Consortium(UEC)이 AI 모델 분산 학습 및 HPC의 초대용량 올리듀스(All-Reduce) 집단 통신을 최적화하기 위해 제정한 개방형 이더넷 표준 전송 아키텍처 |
| 목적 | 고비용 독점 인피니밴드(InfiniBand) 종속 탈피, RoCEv2의 PFC 버퍼 블로트 및 데드락 한계 극복, 수만 개 GPU 클러스터의 와이어 스피드(Wire-speed) 네트워크 확장성 확보 |

## Ⅱ. Ultra Ethernet의 특징

| 특징 | 상세 내용 |
|---|---|
| 무손실 네트워크 탈피 | 엄격한 무손실(Lossless) L2 PFC 대신 패킷 손실을 허용하고 빠른 복구 메커니즘을 내장하여 버퍼 데드락 원천 방지 |
| 패킷 단위 다중경로 스프레이| 플로우 단위 해싱(ECMP)의 대역폭 편향을 배제하고 모든 가용 링크에 패킷 단위로 분산 전송 |
| 하드웨어 비순서 수신 | 다중 경로 전송으로 인해 뒤바뀐 패킷 순서를 수신단 SmartNIC/NPU 하드웨어에서 직접 메모리 복원 |
| 초정밀 신속 혼잡 제어 | 패킷 왕복 시간(RTT) 미세 변동 및 인밴드 네트워크 텔레메트리(INT)를 기반으로 마이크로초 단위 전송률 조절 |

## Ⅲ. Ultra Ethernet의 체계·프로세스

**UET 계층 구조 및 패킷 스프레이 전송 흐름**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ Ultra Ethernet 시스템 아키텍처 ]              │
│                                                                        │
│   [ AI / HPC 애플리케이션 계층 (PyTorch, NCCL, MPI, JAX) ]             │
│                                │                                       │
│                                ▼ UEC 소프트웨어 통신 API               │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ [ UET (Ultra Ethernet Transport) 계층 ]                        │   │
│   │   - Packet Spraying 엔진 : 다중 경로 패킷 단위 분산 송출       │   │
│   │   - Out-of-Order Engine  : 비순서 수신 및 직접 메모리 배치     │   │
│   │   - Fast Congestion Control: 지연 기반 신속 전송률 감속/가속   │   │
│   └────────────────────────────┬───────────────────────────────────┘   │
│                                │                                       │
│                                ▼                                       │
│   [ 이더넷 패브릭 계층 : Spine-Leaf 스위치 망 ]                        │
│   스위치 Path 1 ──► [ 패킷 1, 4 ] ──┐                                  │
│   스위치 Path 2 ──► [ 패킷 2, 5 ] ──┼──► 수신측 UEC NIC                │
│   스위치 Path 3 ──► [ 패킷 3, 6 ] ──┘    (하드웨어 버퍼에서 즉시 재정렬)│
└────────────────────────────────────────────────────────────────────────┘
```

| 프로토콜 계층 | 주요 구성요소 | 핵심 역할 및 기능 |
|---|---|---|
| **UEC 소프트웨어 계층** | Libfabric, NCCL 플러그인 | 분산 AI 라이브러리와 통신 하드웨어 간 표준 가속 인터페이스 제공 |
| **UET 전송 계층** | UET 헤더, 혼잡 제어 엔진 | 패킷 분할, 스프레이 태깅, 선택적 재전송, RTT 기반 동적 윈도우 통제 |
| **링크 계층 (Link Layer)** | LL-L (Link-Level Replay) | 물리 선로상의 비트 오류 발생 시 홉 간 초고속 L2 재전송으로 손실 은폐 |
| **물리 계층 (PHY)** | 400G / 800G / 1.6T Ethernet | 표준 IEEE 802.3 이더넷 광 트랜시버 및 SerDes 규격 100% 호환 활용 |

## Ⅳ. AI 패브릭 기술 비교 (InfiniBand vs RoCEv2 vs Ultra Ethernet)

| 비교 항목 | InfiniBand (NDR/XDR) | RoCEv2 (RDMA over Converged) | Ultra Ethernet (UEC) |
|---|---|---|---|
| **표준화 주체** | IBTA (사실상 NVIDIA 독점) | IBTA / IEEE 확장 규격 | **Linux Foundation UEC (오픈 컨소시엄)**|
| **기본 전송 스택** | 전용 InfiniBand Subnet | UDP/IP 기반 무손실 이더넷 | **표준 이더넷 + 전용 UET 프로토콜** |
| **다중 경로 전송** | 적응형 라우팅 (하드웨어 종속)| ECMP (플로우 해시 충돌 위험) | **패킷 스프레이 (Packet Spraying) 표준화**|
| **흐름 제어 방식** | 크레딧 기반 (Credit-based) | L2 PFC (Priority Flow Control)| **혼잡 통보 기반 종단 속도 제어 (PFC 탈피)**|
| **패킷 순서 요구** | 엄격한 순서 보장 (In-order) | 엄격한 순서 보장 (In-order) | **완벽한 비순서 수신 (Out-of-Order 허용)**|
| **생태계 및 비용** | 최고가 장비, 단일 벤더 락인 | 중간 비용, 설정 복잡도 극심 | **상용 이더넷 장비 활용, 최적 TCO 달성**|

## Ⅴ. Ultra Ethernet의 한계와 방안

| 한계 | 방안 |
|---|---|
| 패킷 단위 스프레이(Packet Spraying)로 인한 대규모 비순서(Out-of-Order) 수신 시 수신측 SmartNIC 버퍼 메모리 고갈 및 재정렬 지연 병목 | SmartNIC ASIC에 고대역폭 온칩 SRAM 기반 하드웨어 패킷 재정렬 엔진을 내장하고, 미수신 홀(Hole) 발생 시 손실 블록만 선별 재요청하는 선택적 드롭 복구(Selective Drop Recovery) 구현 |
| 단일 스위치 포트에 수천 개 송신 노드가 동시에 응답 패킷을 쏟아붓는 AI All-to-All 집단 통신의 인캐스트(Incast) 버퍼 폭주 | 스위치 큐 점유율을 모니터링하여 임계치 초과 즉시 수신단이 송신단에 마이크로초 단위 속도 감속을 지시하는 신속 혼잡 통보(Fast CN) 및 프로액티브 그랜트(Proactive Grant) 메커니즘 결합 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
수만 장 규모의 초거대 AI GPU 클러스터 구축 시, 기존 RoCEv2 환경의 고질적 장애였던 PFC 데드락 및 일시 정지 폭풍(Pause Storm)을 예방하기 위해 스위치 레벨의 무손실 버퍼 설정을 과감히 해제하고, UET 패킷 스프레이를 수용할 수 있는 논블로킹(Non-blocking) 3단계 클로(Clos) 팻트리(Fat-Tree) 토폴로지 설계 수립.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ RoCEv2 ECMP 해시 충돌 vs UEC 패킷 스프레이 전송 비교 ]              │
│                                                                        │
│   [ RoCEv2 ECMP : 플로우 단위 경로 고정 ]                             │
│   Flow A (대용량) ──► [ Path 1 ] ──► (대역폭 100% 포화 및 패킷 드롭)   │
│   Flow B (대용량) ──► [ Path 1 ] ──► (해시 충돌로 동일 경로 중복 배치)│
│   가용 링크       ──► [ Path 2 ] ──► (대역폭 0% 유휴 낭비 발생!)       │
│                                                                        │
│   [ UEC Packet Spraying : 패킷 단위 고속 분산 ]                        │
│   Packet 1, 3, 5  ──► [ Path 1 ] ──► (모든 링크 균일 50% 분산 활용)    │
│   Packet 2, 4, 6  ──► [ Path 2 ] ──► (핫스팟 완벽 제거 및 95% 처리율) │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 데이터센터 패브릭 지표 | InfiniBand NDR | RoCEv2 | Ultra Ethernet 1.0 |
|---|---|---|---|
| **최대 지원 노드 수** | 수천 대 수준 (서브넷 제약) | 수만 대 | **수십만 대 (무제한 확장성)** |
| **패브릭 대역폭 활용률**| 약 85% | 약 50 ~ 60% (해시 편향) | **90% 이상 (스프레이 효과)** |
| **스위치 벤더 선택권** | NVIDIA 전용 독점 | 멀티 벤더 이더넷 지원 | **Broadcom, Cisco, Arista 등 전면 개방**|

## 출제 이력과 검증 출처

- Ultra Ethernet Consortium: Specification 1.0 Architectural Overview
- Linux Foundation: Ultra Ethernet Consortium Charter and Technical Roadmap
- 정보통신기술사 및 정보관리기술사 기출(131회, 134회) AI 데이터센터 인프라 출제 기준

## 연결 토픽

- 상위 토픽: [032 QoS](./032_qos.md)
- 연관 토픽: [047 Wi-Fi 8](./047_wifi_8.md), [050 VLAN](./050_vlan.md)
