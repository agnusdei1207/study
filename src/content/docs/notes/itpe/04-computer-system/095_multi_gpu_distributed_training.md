---
title: "멀티 GPU 분산학습 (GPU: Graphics Processing Unit)"
author: "Antigravity"
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

## Ⅰ. 멀티 GPU 분산학습의 개요

- 개념 : 단일 노드 또는 다중 노드에 분산된 수십~수만 개의 GPU(Graphics Processing Unit)를 고속 네트워크로 결합하여, 거대 **딥러닝** 모델의 파라미터와 방대한 데이터셋을 분할하고 병렬 협력 연산을 통해 학습 수렴 시간을 단축하는 **대규모 AI(Artificial Intelligence) 엔지니어링** 기술.
- 배경 및 필요성 : GPT(Generative Pre-trained Transformer), LLaMA 등 수천억 개의 파라미터를 갖는 **초거대 언어 모델** (LLM, Large Language Model)은 단일 GPU의 메모리 용량(수십~수백 GB 수준)을 수십 배 이상 초과하므로, 모델과 데이터를 분할 처리하는 **분산 학습 아키텍처** 없이는 학습 자체가 불가능함.
- 핵심 목적 : 모델 파라미터 및 배치 분할을 통한 **OOM** (Out of Memory) 극복, **집단 통신** 최적화를 통한 선형적 학습 가속(Linear Scalability) 달성.

## Ⅱ. 분산학습 4대 병렬화 아키텍처 및 텐서 연산 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 4대 분산학습 패러다임 통합 아키텍처 (3D 병렬화 + ZeRO) ]            │
│                                                                        │
│   1. 데이터 병렬화 (Data Parallelism: DDP / FSDP / ZeRO)              │
│    - 데이터셋을 마이크로 배치로 분할, 각 GPU가 동일 모델 복제본 보유    │
│    - Backward 시 그래디언트 AllReduce 동기화                          │
│                                                                        │
│   2. 텐서 병렬화 (Tensor Parallelism: Megatron-LM)                     │
│    - 단일 레이어 내부의 가중치 행렬(Matrix)을 열/행 단위로 분할        │
│    - 매 포워드/백워드 레이어마다 All-Gather / Reduce-Scatter 수행      │
│                                                                        │
│   3. 파이프라인 병렬화 (Pipeline Parallelism: GPipe, 1F1B)            │
│    - 전체 모델의 레이어(Layer)들을 여러 GPU에 순차적으로 분할 배치   │
│    - 파이프라인 버블(Bubble)을 줄이기 위해 마이크로배치 스케줄링     │
│                                                                        │
│   4. 전문가 병렬화 (Expert Parallelism: MoE)                          │
│    - MoE 모델의 라우팅 게이트에 따라 서로 다른 전문가 FFN을 GPU 분산 │
│    - All-to-All 통신을 통해 토큰을 해당 전문가 GPU로 디스패치         │
└────────────────────────────────────────────────────────────────────────┘
```

- **ZeRO** (Zero Redundancy Optimizer) : 데이터 병렬화의 메모리 중복을 제거하기 위해 3단계로 분할:
  - **ZeRO-1** : 옵티마이저 상태(Optimizer States) 분할 (메모리 4배 절감).
  - **ZeRO-2** : 옵티마이저 + 그래디언트(Gradients) 분할 (메모리 8배 절감).
  - **ZeRO-3** (FSDP) : 모델 파라미터(Parameters)까지 전 노드에 분할하여 무한대에 가까운 모델 확장 가능.
- **3D 병렬화** (3D Parallelism) : 노드 내 초고속 NVLink 구간은 **텐서 병렬화** (TP), 노드 간 저지연 네트워크 구간은 **파이프라인 병렬화** (PP), 클러스터 전체 스케일아웃은 **데이터 병렬화** (DP)로 조합 구성.

## Ⅲ. 주요 분산학습 병렬화 기법 비교 분석

| 비교 항목 | 데이터 병렬화 (DDP / FSDP) | 텐서 병렬화 (TP: Megatron) | 파이프라인 병렬화 (PP: GPipe)|
| :--- | :--- | :--- | :--- |
| **분할 대상** | **입력 데이터** (Batch) | 레이어 내부 가중치 행렬 (Weight)| 레이어 간 계층 (Layers) |
| **주요 통신 패턴** | AllReduce (DDP) / AllGather (FSDP)| All-Gather, Reduce-Scatter | Point-to-Point (P2P Send/Recv)|
| **통신 빈도 및 요구선**| 스텝당 1회 (상대적으로 통신 민감도 낮음)| 매 레이어마다 발생 (극초고속 패브릭 필수)| 파이프라인 경계에서만 발생 (낮음)|
| **적정 적용 범위** | 노드 간 스케일아웃 네트워크 | 노드 내부 NVLink/UALink 패브릭 | 랙 간 또는 데이터센터 간 연결 |
| **주요 한계점** | 단일 모델이 GPU에 적재되어야 함(DDP)| 통신 오버헤드로 8-GPU 이상 확장 제약| 파이프라인 버블(유휴 시간) 발생 |

## Ⅳ. 멀티 GPU 분산학습의 주요 한계점 및 해결 방안

- 대규모 AllReduce 통신에 따른 네트워크 병목 및 지연 :
  - 한계점 : 수천 개 GPU 클러스터로 확장 시 그래디언트 동기화 통신 시간이 실제 GPU 연산 시간보다 길어지는 통신 병목 현상.
  - 해결 방안 : FP16/BF16 혼합 정밀도 학습, 그래디언트 축적(Gradient Accumulation) 및 RDMA(Remote Direct Memory Access) 기반 RoCE(Remote Direct Memory Access over Converged Ethernet) v2/InfiniBand 패브릭 구축.
- 파이프라인 병렬화의 버블(Idle Bubble) 현상 :
  - 한계점 : 앞선 GPU의 포워드/백워드 계산이 끝날 때까지 후속 GPU가 대기해야 하는 유휴 시간(Bubble)으로 인해 GPU 가동률 하락.
  - 해결 방안 : 1F1B(One Forward, One Backward) 인터리브드 스케줄링 적용으로 유휴 시간을 은폐하고 메모리 피크 사용량 억제.
- 학습 중간 노드 장애에 따른 전체 클러스터 정지 리스크 :
  - 한계점 : 분산 학습 중 단 하나의 GPU 또는 광케이블 단선 시 전체 학습 프로세스가 멈추고 롤백 발생.
  - 해결 방안 : 비동기 인메모리 분산 체크포인팅, 장애 감지 시 해당 노드를 자동 배제하고 신규 예비 노드로 즉각 승격하는 탄력적(Elastic) 훈련 프레임워크 구축.

## Ⅴ. 국가 및 기업 AI 인프라 구축을 위한 기술사적 제언

- 인터커넥트 중심의 AI 인프라(Network-First) 사이징 : 초거대 AI 분산학습의 성패는 GPU의 스펙보다 GPU 간을 연결하는 인터커넥트(NVLink, InfiniBand/Ultra Ethernet)의 레일 최적화(Rail-Optimized) 토폴로지에 좌우되므로, 네트워크 장비와 패브릭 대역폭에 전체 인프라 예산의 30% 이상을 배정해야 함.
- 오픈소스 분산 프레임워크 표준화 및 거버넌스 확립 : 분산학습 구현 시 벤더 종속적인 단일 라이브러리에 얽매이지 않고, PyTorch FSDP, DeepSpeed, Megatron-Core 및 vLLM 서빙 연계에 이르는 전주기 AI 파이프라인 엔지니어링 표준을 사내 기술 자산으로 체계화할 것을 제언함.
