---
title: "AI 학습·추론 고성능 컴퓨팅 인프라 (AI: Artificial Intelligence)"
author: "agnusdei1207"
date: "2026-10-24T22:33:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- AI/HPC 인프라, GPU 클러스터, NVLink·NVSwitch, InfiniBand, RoCE v2, RDMA, SHARP, GPUDirect Storage
- 병렬 파일시스템, All-Reduce, 스트래글러, 체크포인트 스톨, 직접 칩 액체냉각(D2C), MFU, PUE

## Ⅰ. AI 가속·HPC 인프라의 개요

- 핵심 요약 : 인공지능(AI, Artificial Intelligence)과 고성능 컴퓨팅(HPC, High-Performance Computing) 워크로드를 위해 가속기 클러스터, 초고속 네트워크, 병렬 스토리지, 액체냉각을 한 체계로 설계한 전용 인프라.
- 개념 : 대규모 파라미터를 가진 거대언어모델(LLM, Large Language Model)을 학습하고 대규모 과학 연산을 수행하기 위해, 그래픽 처리 장치(GPU, Graphics Processing Unit)나 신경망 처리 장치(NPU, Neural Processing Unit) 클러스터, 무손실 상호연결망, 병렬 분산 파일시스템, 고밀도 액체냉각을 결합한 **AI/HPC 인프라**.
- 배경 및 필요성 : 일반 기업용 데이터센터(IDC, Internet Data Center)는 노드 간 네트워크 대역폭, 스토리지 I/O, 랙당 전력 밀도와 공랭 능력이 부족해 대규모 분산 학습을 감당하기 어렵다. 이 한계가 인프라를 전용 HPC 아키텍처로 분화시킨 계기다.
- 주요 목적 : 이론상 연산 성능 대비 실제로 쓰이는 비율인 **모델 FLOPs 활용률** (MFU, Model FLOPs Utilization)을 높이고, 노드 간 통신 지연을 줄이며, 대용량 데이터를 GPU로 끊김 없이 공급하는 것.

## Ⅱ. AI 가속·HPC 인프라의 특징 및 장점

- 핵심 요약 : 연산·연결·저장·전력을 하나의 체계로 묶어 통신 병목과 I/O 대기를 줄이고, 그 결과 학습 효율을 높이는 구조.

1. **NVLink·NVSwitch** 스케일업 패브릭 : 한 노드 안의 GPU를 고대역 점대점 링크로 묶어 하나의 큰 메모리 공간처럼 사용 → 노드 내부 GPU 간 데이터 교환 지연 감소.
2. **InfiniBand**와 **RoCE v2** (RDMA over Converged Ethernet v2) 무손실 네트워크 : **원격 직접 메모리 접근** (RDMA, Remote Direct Memory Access)으로 CPU 개입 없이 원격 GPU 메모리를 직접 읽고 쓰며, 패킷 손실 없이 전달 → 노드 간 통신 오버헤드 감소.
3. **SHARP** (Scalable Hierarchical Aggregation and Reduction Protocol) 인네트워크 컴퓨팅 : All-Reduce 같은 집합 통신 연산을 스위치 하드웨어에서 처리 → 호스트로 오가는 트래픽 절감.
4. **GPUDirect Storage** : 스토리지와 GPU 메모리 사이에 직접 데이터 경로를 열어 CPU와 OS 페이지 캐시를 거치지 않음 → 호스트 측 I/O 병목 제거.
5. **직접 칩 액체냉각** (D2C, Direct-to-Chip) : 발열이 큰 칩에 냉각수를 직접 전달 → 랙 전력 밀도를 높이고 장비 간 광케이블 길이를 줄여 지연 완화.

## Ⅲ. AI 가속·HPC 인프라의 구조 및 동작 메커니즘

- 핵심 요약 : 컴퓨팅에서 전력·냉각까지 5계층이 아래에서 위로 받쳐 주는 구조이며, 학습 한 스텝은 GPU 연산 후 동기화와 저장 단계로 이어짐.

```text
[ AI/HPC 인프라 5계층 ]

1. 컴퓨팅 계층 (GPU 서버)
      ↓
2. 스케일업 계층 (NVLink, 노드 내부)
      ↓
3. 스케일아웃 네트워크 (InfiniBand, RoCE v2)
      ↓
4. 병렬 스토리지 (GPUDirect Storage)
      ↓
5. 전력·냉각 계층 (D2C 액체냉각)
```

```text
[ 분산 학습 1 스텝의 흐름 ]

GPU 연산 (순전파·역전파)
      ↓
그래디언트 동기화 (All-Reduce)
      ↓
SHARP가 스위치에서 집계
      ↓
다음 스텝 진행
      ↓
주기적 체크포인트 → 병렬 스토리지 저장
```

- 스케일업은 한 노드 안에서 GPU를 묶는 계층이고, 스케일아웃은 노드들을 네트워크로 잇는 계층이다. 두 계층의 대역폭 차이가 학습 속도를 좌우하므로 설계 단계에서 함께 고려된다.

## Ⅳ. AI 가속·HPC 인프라의 비교

- 핵심 요약 : 범용 IDC는 가상화 중심의 저밀도 공랭 구조이고, AI/HPC 인프라는 가속기 중심의 고밀도 무손실 구조라 설계 기준이 다르다.

| 비교 축 | 엔터프라이즈 범용 IDC | AI/HPC 특화 인프라 |
| --- | --- | --- |
| 컴퓨팅 중심 | 가상머신 중심의 CPU(Central Processing Unit) 서버 | GPU·NPU 가속기 클러스터 |
| 랙당 전력 밀도 | 표준 공랭식이 감당하는 수준 | 액체냉각을 전제로 한 고밀도 |
| 노드 간 네트워크 | TCP/IP(Transmission Control Protocol/Internet Protocol) 이더넷 | 무손실 InfiniBand·RoCE v2 기반 RDMA |
| 스토리지 I/O | NFS(Network File System)·SAN(Storage Area Network) | 병렬 파일시스템과 GPUDirect Storage |
| 네트워크 토폴로지 | 오버서브스크립션(Oversubscription)을 허용하는 계층형 구조 | 비차단(Non-blocking) 레일 최적화 구조 |

- 선택 기준 : 워크로드가 노드 간 동기 통신과 대용량 I/O에 얼마나 의존하는지에 따라 전용 인프라 전환 여부를 정한다. 단순 서버 증설로는 전력, 냉각, 토폴로지, 스토리지를 따로 맞출 수 없다는 점이 핵심이다.

## Ⅴ. AI 가속·HPC 인프라의 한계와 방안

- 핵심 요약 : 동기화 정체, 체크포인트 중단, 전력·냉각 한계를 레일 최적화, 비동기 체크포인트, 액체냉각으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| **스트래글러** (Straggler) 정체 | 한 GPU나 링크의 미세 지연이 All-Reduce 동기화 지점에서 전체 클러스터를 멈춤 | 레일 최적화 케이블링, 텔레메트리 기반 이상 GPU 즉시 격리, 서브토폴로지 동적 재구성 | 스텝당 대기 시간, 격리 건수 |
| **체크포인트 스톨** (Checkpoint Stalling) | 대용량 모델 가중치를 저장하는 동안 연산이 멈춰 GPU 가동률 하락 | 메모리 → 로컬 NVMe(NVMe, Non-Volatile Memory Express) → 병렬 스토리지로 이어지는 다계층 비동기 체크포인팅, 차분 체크포인트 | 저장 소요 시간, MFU |
| 전력 밀도·냉각 한계 | 공랭식으로는 고밀도 GPU 랙의 열을 감당하기 어려워 랙을 듬성듬성 배치하고, 케이블 길이와 지연이 늘어남 | D2C 액체냉각 도입, 랙 밀도 상향과 냉각 설계 일체화 | 랙당 발열 여유, PUE |

## Ⅵ. AI 가속·HPC 인프라 적용 제언

- 핵심 요약 : 활용률 지표를 중심으로 하드웨어와 학습 소프트웨어를 함께 설계하고, 네트워크 규격과 전력 조달을 함께 관리하는 것이 실효성을 높인다.

1. 모델 FLOPs 활용률을 클러스터 성과 지표로 삼고, 하드웨어와 학습 소프트웨어를 함께 조정하는 코디자인 체계를 두어야 한다.
2. 차세대 이더넷 기반 RDMA 규격의 개방형 표준을 추적하고, **울트라 이더넷 컨소시엄** (UEC, Ultra Ethernet Consortium)이 정의하는 규격을 소규모 검증 과제로 먼저 시험하는 것이 바람직하다.
3. 데이터센터 사업자는 **전력구매계약** (PPA, Power Purchase Agreement)으로 재생에너지를 직접 조달하고 액체냉각 폐열 회수를 검토해, **전력 사용 효율** (PUE, Power Usage Effectiveness)을 관리 가능한 수준으로 낮춰야 한다.

## Ⅶ. 결론

- 핵심 요약 : AI/HPC 인프라는 연산, 네트워크, 스토리지, 냉각을 통합해 초대형 학습을 가능하게 하지만 동기화와 전력 리스크가 따르는 구조.
- 시사점 : 인프라 성능은 개별 장비 사양보다 계층 간 통합 설계에서 결정되므로, 활용률 지표를 기준으로 투자 우선순위를 정하는 것이 합리적이다.
