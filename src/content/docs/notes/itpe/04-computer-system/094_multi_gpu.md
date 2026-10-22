---
title: "멀티 GPU (GPU: Graphics Processing Unit)"
author: "agnusdei1207"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 멀티 GPU(Multi-GPU)의 개요

- 핵심 요약 : **멀티 GPU**는 단일 노드에 다수 GPU를 고속 인터커넥트로 결합하여 메모리 용량·연산 성능 한계를 돌파하는 HPC/AI 인프라.
- 개념 : 단일 컴퓨팅 노드 내부에 2개 이상의 **GPU** (Graphics Processing Unit)를 장착하거나 고속 인터커넥트로 연결하여, 거대한 연산 워크로드를 병렬 분할 처리함으로써 단일 GPU의 메모리 용량 및 연산 성능 한계를 돌파하는 **고성능 컴퓨팅** (HPC, High-Performance Computing) 및 인공지능 인프라 아키텍처.
- 배경 및 필요성 : 수백억~수조 개의 파라미터를 가진 최신 생성형 AI(Artificial Intelligence) 모델은 가중치와 옵티마이저 상태만으로도 수백 GB~수 TB의 VRAM(Video Random-Access Memory)을 요구하므로, 단일 80GB/192GB GPU로는 로딩조차 불가능하여 멀티 GPU 클러스터링이 필수적임.
- 핵심 목적 : **집합 메모리 공간** (Aggregate Memory) 확장, **텐서/파이프라인 병렬** 연산을 통한 초거대 AI 학습 및 초고속 서빙, 노드 내 가속기 연산 집적도 극대화.

## Ⅱ. 멀티 GPU(Multi-GPU)의 특징 및 장점

- 핵심 요약 : **P2P 직접 접근·NVSwitch 풀 메시 패브릭**으로 노드 내 GPU 간 초고속 통신.
1. **P2P(Peer-to-Peer) 메모리 직접 접근** (GPUDirect P2P) : 호스트 CPU(Central Processing Unit) 메모리를 경유하지 않고 GPU 간 고속 버스(NVLink 또는 PCIe(Peripheral Component Interconnect Express) 스위치)를 통해 상대 GPU의 VRAM을 직접 DMA(Direct Memory Access) 읽기/쓰기.
2. **NVSwitch 완전 결합** (All-to-All Fabric) : 크로스바 스위치 구조의 NVSwitch를 탑재하여 노드 내 8개 GPU 전체가 병목 없이 **풀 메시** (Full-Mesh) 대역폭으로 통신.

## Ⅲ. 멀티 GPU(Multi-GPU)의 구조 및 동작 메커니즘

- 핵심 요약 : **CPU → PCIe 스위치 → GPU 0-7 → NVSwitch 풀 메시 패브릭**.
- 멀티 GPU 시스템은 호스트 CPU, PCIe 스위치, GPU, NVSwitch 패브릭으로 구성되며 P2P 직접 접근과 풀 메시 통신으로 동작함.

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 고성능 8-GPU 서버 노드 내부 인터커넥트 아키텍처 (HGX/NVLink 기준) ] │
│                                                                        │
│   ┌───────────────────────────┐     ┌───────────────────────────┐      │
│   │ 호스트 CPU 1 (Host CPU 1) │     │ 호스트 CPU 2 (Host CPU 2) │      │
│   └─────────────┬─────────────┘     └─────────────┬─────────────┘      │
│                 │ PCIe Gen 5                      │ PCIe Gen 5         │
│                 ▼                                 ▼                    │
│   ┌───────────────────────────┐     ┌───────────────────────────┐      │
│   │ PCIe 스위치 (Switch 1)    │     │ PCIe 스위치 (Switch 2)    │      │
│   └──────┬─────────────┬──────┘     └──────┬─────────────┬──────┘      │
│          │             │                   │             │             │
│          ▼             ▼                   ▼             ▼             │
│     [ GPU 0 ]     [ GPU 1 ]           [ GPU 2 ]     [ GPU 3 ]          │
│        ▲             ▲                   ▲             ▲               │
│        │             │                   │             │               │
│   ═════╪═════════════╪═══════════════════╪═════════════╪════════════   │
│   [ 초고속 NVSwitch 패브릭 (All-to-All 양방향 900GB/s ~ 1.8TB/s) ]     │
│   ═════╪═════════════╪═══════════════════╪═════════════╪════════════   │
│        │             │                   │             │               │
│        ▼             ▼                   ▼             ▼               │
│     [ GPU 4 ]     [ GPU 5 ]           [ GPU 6 ]     [ GPU 7 ]          │
└────────────────────────────────────────────────────────────────────────┘
```

## Ⅳ. 멀티 GPU(Multi-GPU)의 비교

- 핵심 요약 : **PCIe 버스·링 NVLink·NVSwitch** 통신 경로·대역폭·집단 통신·비용·적용 비교.

| 비교 항목 | 표준 PCIe 버스 연결 | 링 토폴로지 NVLink (하이브리드) | 스위치 기반 완전 결합 (NVSwitch) |
| :--- | :--- | :--- | :--- |
| 통신 경로 | CPU 및 온보드 PCIe 스위치 경유 | 인접 GPU 간 직접 링(Ring) 연결 | 전용 NVSwitch 패브릭을 통한 단일 홉 |
| 양방향 대역폭 | 64 ~ 128 GB/s (PCIe Gen 5) | 300 ~ 600 GB/s | 900 GB/s ~ 1.8 TB/s (NVLink 4/5) |
| 집단 통신 지연 | CPU 간섭 및 버스 경합으로 큼 | 홉(Hop) 수 증가에 따른 지연 누적 | 초저지연 하드웨어 AllReduce 지원 |
| 비용 및 구현 | 일반 상용 서버에 장착 가능 (저비용) | 중간 복잡도 | 고비용 전용 베이스보드(HGX) 필수 |
| 주요 적합 분야 | 경량 AI 추론, 독립 렌더링 팜 | 중규모 딥러닝 학습, 과학 시뮬레이션 | LLM(Large Language Model) 파운데이션 모델 분산 사전학습 |

## Ⅴ. 멀티 GPU(Multi-GPU)의 한계와 방안

- 핵심 요약 : **통신 병목·전력/발열·단일 GPU 장애**를 NCCL 튜닝·DLC·체크포인팅으로 대응.

- GPU 간 통신 병목으로 인한 선형적 확장성(Scaling Efficiency) 저하 :
  - 한계점 : GPU 개수를 2개에서 8개, 16개로 늘릴 때 집단 통신(AllReduce) 오버헤드로 인해 연산 효율이 크게 저하.
  - 해결 방안 : NCCL(NVIDIA Collective Communications Library) 튜닝, 통신과 연산을 중첩(Overlap)하는 비동기 파이프라이닝 최적화.
- 초고밀도 전력 소모(5kW~10kW per Node)와 열폭주(Thermal Throttling) :
  - 한계점 : 단일 4U/8U 섀시 내에 8개의 고발열 GPU(개당 700W~1000W) 집적 시 공랭 팬 소음 극대화 및 발열로 인한 클록 다운.
  - 해결 방안 : 직접 액체 냉각(DLC, Direct Liquid Cooling) 콜드 플레이트 전면 도입 및 48V 버스바 전력 분배 아키텍처 채택.
- 단일 GPU 고장 시 전체 분산 작업 중단(Fault Domain 리스크) :
  - 한계점 : 긴밀하게 결합된 멀티 GPU 학습 중 단 1개의 GPU만 메모리 ECC(Error-Correcting Code) 에러나 크래시가 발생해도 전체 학습 작업 중단.
  - 해결 방안 : 고속 분산 체크포인팅(Checkfreq) 기법 적용, NVLink 인터커넥트 장애 시 동적 격리 및 작업 자동 재스케줄링.

## Ⅵ. 멀티 GPU(Multi-GPU) 적용 제언

- 핵심 요약 : **GPUDirect Storage·RoCE·vGPU/MIG 거버넌스**.
- GPUDirect Storage(GDS) 및 RoCE 네트워크 통합 설계 : GDS + 400Gbps 멀티레일 NIC 1:1 매핑.
- 가상화 기반 GPU 풀링(vGPU 및 MIG) 거버넌스 수립 : MIG 분할로 개발/테스트 자원 회전율 극대화.

## Ⅶ. 결론

- 핵심 요약 : 멀티 GPU는 **노드 내 고속 인터커넥트 결합**으로 메모리 용량·연산 성능 한계를 돌파하나 통신 병목·전력/발열·단일 GPU 장애 리스크 관리가 필수.
- 멀티 GPU는 P2P 직접 접근과 NVSwitch 풀 메시 패브릭으로 메모리 용량·연산 성능 한계를 돌파하지만, 통신 병목·전력/발열·단일 GPU 장애 리스크를 NCCL 튜닝·DLC·체크포인팅으로 관리해야 함.
- 답안에는 P2P/NVSwitch 구조, 인터커넥트 토폴로지 비교, 한계·대응, GPUDirect Storage·RoCE·MIG 제언을 연결. (HGX)