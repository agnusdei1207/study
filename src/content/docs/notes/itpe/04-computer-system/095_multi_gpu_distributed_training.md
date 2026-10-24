---
title: "멀티 GPU 분산학습 (GPU: Graphics Processing Unit)"
author: "agnusdei1207"
date: "2026-10-24T22:33:46+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 분산 학습(Distributed Training), 데이터 병렬화(Data Parallelism), 텐서 병렬화(Tensor Parallelism), 파이프라인 병렬화(Pipeline Parallelism), 전문가 병렬화(Expert Parallelism)
- 3D 병렬화(3D Parallelism), ZeRO(Zero Redundancy Optimizer), DDP(Distributed Data Parallel), FSDP(Fully Sharded Data Parallel), MoE(Mixture of Experts)
- AllReduce, 1F1B, 파이프라인 버블(Pipeline Bubble), 혼합 정밀도(Mixed Precision), 그래디언트 누적(Gradient Accumulation), 탄력적 학습(Elastic Training)

## Ⅰ. 멀티 GPU 분산학습의 개요

- 핵심 요약 : 다수 GPU에 모델과 데이터를 나누어 병렬로 협력 연산하며 학습 시간을 줄이는 대규모 AI 엔지니어링 기술.
- 개념 : 한 노드 또는 여러 노드의 GPU(Graphics Processing Unit)를 고속 네트워크로 묶어 모델 파라미터와 데이터셋을 나누고, 병렬 협력 연산으로 학습 수렴 시간을 줄이는 **분산 학습** (Distributed Training) 기술.
- 배경 및 필요성 : 수천억 개의 파라미터를 가진 대규모 언어 모델(LLM, Large Language Model)은 단일 GPU의 메모리 용량을 크게 넘어서므로, 모델과 데이터를 나누지 않으면 학습 자체가 불가능함.
- 주요 목적 : 파라미터와 배치를 분할해 메모리 부족(OOM, Out of Memory) 극복, 집단 통신을 최적화해 선형에 가까운 학습 가속 달성.

## Ⅱ. 멀티 GPU 분산학습의 특징 및 장점

- 핵심 요약 : 네 가지 병렬화 축과 메모리 중복을 없애는 ZeRO를 조합해 모델 규모와 학습 속도의 한계를 넓힘.

1. **ZeRO** (Zero Redundancy Optimizer) : **데이터 병렬화** (Data Parallelism)에서 GPU마다 중복 보관되는 상태를 나누어 저장하는 기법으로, 단계가 높을수록 나누는 대상이 늘어 GPU당 메모리 사용이 줄어듦.
   - ZeRO-1 : 옵티마이저 상태(Optimizer States)를 분할.
   - ZeRO-2 : 옵티마이저 상태와 그래디언트(Gradients)를 분할.
   - ZeRO-3 : 모델 파라미터(Parameters)까지 분할해 모델 규모 확장 여지를 넓힘.
2. **3D 병렬화** (3D Parallelism) : 노드 내 고속 NVLink 구간에는 **텐서 병렬화** (Tensor Parallelism), 노드 간 구간에는 **파이프라인 병렬화** (Pipeline Parallelism), 클러스터 전체 확장에는 데이터 병렬화를 조합 → 각 통신 특성에 맞춰 병렬 축을 배치.

## Ⅲ. 멀티 GPU 분산학습의 구조 및 동작 메커니즘

- 핵심 요약 : 데이터, 텐서, 파이프라인, 전문가 병렬화가 나누는 대상과 통신 패턴이 달라 네 가지 패러다임으로 동작.
- **DDP** (Distributed Data Parallel)와 **FSDP** (Fully Sharded Data Parallel)는 데이터 병렬화의 대표 구현이며, 데이터 병렬화는 역전파 후 그래디언트를 **AllReduce**로 동기화함.
- 파이프라인 병렬화는 레이어 묶음을 GPU 순서대로 배치하고, **전문가 병렬화** (Expert Parallelism)는 **MoE** (Mixture of Experts) 모델의 라우팅 결과에 따라 전문가 네트워크를 서로 다른 GPU에 배치함.

```text
[ 3D 병렬화 배치 (노드 구조 기준) ]

클러스터 전체: 데이터 병렬화
      ↓
노드 간 구간: 파이프라인 병렬화
      ↓
노드 내 NVLink 구간: 텐서 병렬화
```

```text
[ 병렬화 축별 통신 빈도 ]

데이터 병렬화: 스텝당 1회 동기화
      ↓
텐서 병렬화: 레이어마다 수집·분산
      ↓
파이프라인 병렬화: 경계에서만 송수신
```

## Ⅳ. 멀티 GPU 분산학습 병렬화 방식의 비교

- 핵심 요약 : 데이터 병렬화는 스텝당 통신, 텐서 병렬화는 레이어마다의 초고속 통신, 파이프라인 병렬화는 경계 통신을 요구함.
- 비교 축은 분할 대상, 주요 통신, 통신 빈도, 적정 범위, 주요 한계이며, 인터커넥트 수준에 따라 조합을 정함.

| 비교 축 | 데이터 병렬화 (DDP, FSDP) | 텐서 병렬화 (Megatron-LM) | 파이프라인 병렬화 (GPipe) |
| :--- | :--- | :--- | :--- |
| 분할 대상 | 입력 데이터 배치 | 레이어 내부 가중치 행렬 | 레이어 간 계층 |
| 주요 통신 | AllReduce(DDP), All-Gather(FSDP) | All-Gather, Reduce-Scatter | 인접 단계 간 Point-to-Point 송수신 |
| 통신 빈도 | 스텝당 1회 | 레이어마다 발생 | 단계 경계에서만 발생 |
| 적정 범위 | 노드 간 확장 네트워크 | 노드 내 고속 NVLink 패브릭 | 랙 간 또는 데이터센터 간 연결 |
| 주요 한계 | 모델 한 복제본이 GPU 메모리에 들어가야 함 | 통신 오버헤드로 확장 제약 | 파이프라인 버블로 인한 유휴 시간 |

## Ⅴ. 멀티 GPU 분산학습의 한계와 방안

- 핵심 요약 : 통신 병목, 파이프라인 유휴 시간, 노드 장애를 저정밀 학습, 스케줄링, 체크포인트로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| 대규모 AllReduce 통신 병목 | GPU 수가 수천 단위로 늘면 그래디언트 동기화 시간이 연산 시간보다 길어짐 | **혼합 정밀도** (Mixed Precision) 학습, **그래디언트 누적** (Gradient Accumulation), RDMA 기반 RoCE v2 또는 InfiniBand 패브릭 | 통신 대비 연산 시간 비율 |
| **파이프라인 버블** (Pipeline Bubble) | 앞 단계의 순전파와 역전파가 끝날 때까지 뒤 GPU가 유휴 상태로 대기 | **1F1B** (One Forward One Backward) 인터리브 스케줄링으로 유휴 시간을 줄이고 메모리 피크 억제 | GPU 가동률 |
| 노드·링크 장애로 인한 전체 정지 | 한 GPU나 광케이블 단선으로 학습 전체가 멈추고 롤백 발생 | 비동기 체크포인팅, 장애 노드 자동 배제 후 예비 노드로 승격하는 **탄력적 학습** (Elastic Training) | 롤백으로 잃은 학습 시간 |

## Ⅵ. 멀티 GPU 분산학습 적용에 대한 기술사적 제언

- 핵심 요약 : 인터커넥트 중심의 인프라 설계와 표준 소프트웨어 스택, 장애 대응 거버넌스를 함께 세우는 운영 체계.
- 학습 인프라를 계획할 때는 연산 장치보다 인터커넥트 대역폭을 먼저 확보하고, 그 대역폭에 맞춰 병렬화 축을 배치하는 네트워크 우선 설계가 바람직하다.
- PyTorch FSDP, DeepSpeed, Megatron-Core와 서빙 도구를 조직 표준으로 정해 학습부터 배포까지 절차를 일관되게 관리하는 것이 필요하다.
- 체크포인트 주기와 예비 노드 확보량을 학습 작업의 서비스 수준 협약(SLA, Service Level Agreement) 기준과 연결해 정하면, 장애 손실을 비용 관점에서 통제할 수 있다.

## Ⅶ. 결론

- 핵심 요약 : 분산 학습은 4대 병렬화와 ZeRO로 메모리 한계를 넘고 선형에 가까운 가속을 노리는 대규모 AI 엔지니어링 기술.
- 통신 병목, 파이프라인 버블, 노드 장애를 통신 설계와 스케줄링, 체크포인트로 함께 관리해야 실효성이 확보된다.
