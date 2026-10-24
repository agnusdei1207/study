---
title: "멀티 GPU (GPU: Graphics Processing Unit)"
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

- 멀티 GPU(Multi-GPU), GPU(Graphics Processing Unit), 고성능 컴퓨팅(HPC, High-Performance Computing)
- P2P(Peer-to-Peer), NVLink, NVSwitch, PCIe(Peripheral Component Interconnect Express), HGX
- AllReduce, NCCL(NVIDIA Collective Communications Library), 직접 액체 냉각(DLC, Direct Liquid Cooling)
- GPUDirect Storage, RoCE(RDMA over Converged Ethernet), MIG(Multi-Instance GPU), vGPU

## Ⅰ. 멀티 GPU의 개요

- 핵심 요약 : 단일 노드에 다수 GPU를 고속 인터커넥트로 묶어 메모리와 연산의 한계를 넘는 고성능 인프라 구성.
- 개념 : 한 노드에 둘 이상의 GPU(Graphics Processing Unit)를 장착하고 고속 연결로 묶어 거대한 연산을 나누어 처리하는 **멀티 GPU** (Multi-GPU) 구성. 단일 GPU의 메모리 용량과 연산 성능을 넘어서기 위해 **고성능 컴퓨팅** (HPC, High-Performance Computing)과 AI 인프라에서 쓰임.
- 배경 및 필요성 : 대규모 언어 모델(LLM, Large Language Model)은 가중치와 옵티마이저 상태만으로도 단일 GPU의 비디오 메모리(VRAM, Video Random-Access Memory) 용량을 넘어서므로, 메모리와 연산을 여러 GPU에 나눠 담는 구성이 불가피해짐.
- 주요 목적 : 여러 GPU의 메모리를 합친 **집합 메모리** (Aggregate Memory) 확보, 텐서·파이프라인 병렬 연산 지원, 노드 내 가속 연산 밀도 향상.

## Ⅱ. 멀티 GPU의 특징 및 장점

- 핵심 요약 : GPU 간 직접 접근과 완전 결합 스위치가 호스트 경유 복사를 줄여 노드 내 통신 병목을 낮춤.

1. **P2P** (Peer-to-Peer) 직접 접근 : 호스트 CPU(Central Processing Unit) 메모리를 거치지 않고 **NVLink** 또는 **PCIe** (Peripheral Component Interconnect Express) 경로로 상대 GPU의 VRAM에 직접 읽고 쓰기 → 호스트 경유 복사 비용과 지연 감소.
2. **NVSwitch** 완전 결합 : 스위치 칩으로 노드 내 GPU 전체를 연결해, 특정 GPU 쌍에만 대역폭이 몰리지 않는 전 대 전 통신 확보 → 집단 통신에서 대역폭 균형 유지.

## Ⅲ. 멀티 GPU의 구조 및 동작 메커니즘

- 핵심 요약 : 호스트 CPU와 PCIe가 GPU를 제어하는 계층과, NVSwitch 패브릭이 GPU 간 데이터를 잇는 계층의 2단 구조.
- 제어와 입출력은 CPU 및 PCIe 스위치 경로가 담당하고, 대량의 GPU 간 데이터 교환은 NVSwitch 패브릭이 담당함.

```text
[ 8-GPU 노드 인터커넥트 구조 ]

호스트 CPU (제어·입출력)
      ↓ PCIe 스위치
GPU 0 ~ GPU 7 (연산)
      ↓ NVLink 연결
NVSwitch 패브릭 (GPU 간 통신)
```

```text
[ GPU 간 P2P 전송 경로 ]

GPU 0의 VRAM
      ↓ NVLink 또는 PCIe 경로 (DMA)
GPU 5의 VRAM
      ↓
호스트 메모리 경유 없음
```

## Ⅳ. 멀티 GPU 인터커넥트의 비교

- 핵심 요약 : 일반 PCIe 연결은 저비용 범용성, 링 방식 NVLink는 중간 규모, NVSwitch 완전 결합은 대규모 학습에 적합.
- 비교 축은 통신 경로, 대역폭, 집단 통신 지연, 구현 비용, 적합 분야이며, 워크로드 규모에 따라 선택함.

| 비교 축 | PCIe 버스 연결 | 링 방식 NVLink (하이브리드) | NVSwitch 완전 결합 |
| :--- | :--- | :--- | :--- |
| 통신 경로 | CPU 및 PCIe 스위치 경유 | 인접 GPU 간 직접 링 연결 | 전용 NVSwitch 패브릭 경유 |
| 양방향 대역폭 | PCIe Gen 5 x16 기준 양방향 128GB/s | 링 구성에 따라 상이 | GPU당 양방향 900GB/s(NVLink 4), 1.8TB/s(NVLink 5) |
| 집단 통신 지연 | CPU 개입과 버스 경합으로 큼 | 홉 수가 늘면 지연 누적 | 스위치 기반 집단 통신 가속 지원 |
| 비용·구현 | 일반 상용 서버에 장착 가능 | 중간 수준의 복잡도 | 전용 베이스보드(HGX) 필요, 고비용 |
| 주요 적합 분야 | 경량 AI 추론, 독립 렌더링 | 중규모 딥러닝 학습, 과학 시뮬레이션 | 대규모 LLM 분산 사전학습 |

## Ⅴ. 멀티 GPU의 한계와 방안

- 핵심 요약 : 통신 병목, 고밀도 발열, 단일 장치 장애를 통신 튜닝·액체 냉각·분산 체크포인팅으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| 집단 통신 병목과 **확장 효율** (Scaling Efficiency) 저하 | GPU 수를 늘릴수록 **AllReduce** 동기화 오버헤드가 커져 연산 효율이 떨어짐 | **NCCL** (NVIDIA Collective Communications Library) 튜닝, 통신과 연산을 겹치는 비동기 파이프라이닝 | GPU 수 대비 처리량 증가율 |
| 고밀도 전력 소모와 열 제한 | 고발열 GPU를 한 섀시에 집적하면 공랭 한계에 부딪혀 클록이 낮아짐 | **직접 액체 냉각** (DLC, Direct Liquid Cooling) 도입, 전원 분배 구조 재설계 | 장치 온도, 스로틀링 발생률 |
| 단일 장치 장애의 전체 작업 중단 | 긴밀히 결합된 학습에서 한 GPU의 **ECC** (Error-Correcting Code) 오류나 크래시가 전체 작업을 멈춤 | **체크포인팅** (Checkpointing)의 주기적 저장, 장애 장치 격리와 작업 자동 재스케줄링 | 체크포인트 복구 소요 시간 |

## Ⅵ. 멀티 GPU 적용에 대한 기술사적 제언

- 핵심 요약 : 인터커넥트 중심의 인프라 설계와 자원 가상화, 표준 소프트웨어 스택을 함께 묶는 운영 체계 확립.
- AI 인프라를 계획할 때는 연산 장치 예산과 함께 네트워크 패브릭 예산을 같은 무게로 검토해야 학습 효율을 제대로 얻을 수 있다.
- GPU를 통째로 나누어 쓰는 대신 **MIG** (Multi-Instance GPU) 분할과 가상 GPU(vGPU, Virtual GPU)를 조합하면, 개발과 테스트 자원의 회전율을 높일 수 있다.
- **GPUDirect Storage**와 **RoCE** (RDMA over Converged Ethernet) 기반 네트워크를 함께 설계해 저장장치에서 GPU로 가는 입력 병목을 줄이는 방향이 바람직하다.
- 분산 학습 프레임워크와 서빙 도구를 표준으로 정하고 학습부터 추론까지 파이프라인을 일관되게 관리하는 거버넌스가 필요하다.

## Ⅶ. 결론

- 핵심 요약 : 멀티 GPU는 노드 내 고속 인터커넥트 결합으로 메모리와 연산의 한계를 넘는 AI·HPC 인프라 구조.
- 통신 병목, 전력과 발열, 장애 격리를 튜닝과 냉각, 체크포인트로 함께 관리해야 실효성을 얻을 수 있다.
