---
title: "GPGPU (General-Purpose computing on Graphics Processing Units)"
author: "agnusdei1207"
date: "2026-10-24T22:33:37+09:00"
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

- GPGPU(General-Purpose computing on GPU), GPU(Graphics Processing Unit), CUDA
- SIMT(Single Instruction, Multiple Threads), 워프(Warp), SM(Streaming Multiprocessor)
- 지연 은폐, 공유 메모리, 텐서 코어, 데이터 병렬성
- 워프 다이버전스, 메모리 결합(Memory Coalescing), PCIe 병목

## Ⅰ. GPGPU(General-Purpose computing on GPU)의 개요

- 핵심 요약 : **GPGPU** (General-Purpose computing on GPU)는 GPU의 대규모 병렬 연산 구조를 그래픽 외 범용 수치 계산에 활용하는 컴퓨팅 방식.
- 개념 : 3차원 그래픽 처리를 위해 발전한 GPU(Graphics Processing Unit)의 병렬 연산 구조를 과학 계산, 암호 해독, 빅데이터 분석, 딥러닝 등 범용 수치 계산에 활용하는 방식과 그 프로그래밍 모델.
- 배경 및 필요성 : 적은 수의 강력한 코어로 지연 시간을 줄이는 CPU(Central Processing Unit)만으로는 대규모 행렬 연산이 필요한 AI(Artificial Intelligence) 모델을 감당하기 어려워, 많은 연산 코어를 집적한 GPU의 병렬 처리 능력이 활용됨.
- 주요 목적 : 데이터 병렬성에 기반한 높은 연산 처리량 확보와 와트당 연산 효율 향상.

## Ⅱ. GPGPU(General-Purpose computing on GPU)의 특징 및 장점

- 핵심 요약 : 워프 단위 동시 실행, 지연 은폐, 온칩 공유 메모리가 결합되어 대량의 데이터를 동시에 처리하는 구조.

1. **SIMT** (Single Instruction, Multiple Threads) 실행 모델 : 32개의 스레드를 **워프** (Warp) 단위로 묶어 같은 명령어를 여러 데이터에 동시에 적용 → 명령 발행 비용을 다수 스레드가 나눠 부담하여 처리량 증가.
2. 지연 은폐 (Latency Hiding) : 메모리 접근으로 대기가 생긴 워프를 스케줄러가 연산 준비가 끝난 다른 워프로 교체 → 연산 유닛의 유휴 시간 감소.
3. **공유 메모리** (Shared Memory) : 같은 SM(Streaming Multiprocessor) 안의 스레드 블록이 데이터를 함께 쓰는 프로그래머블 온칩 메모리 → 글로벌 메모리의 반복 접근 감소.

## Ⅲ. GPGPU(General-Purpose computing on GPU)의 구조 및 동작 메커니즘

- 핵심 요약 : SM 안의 워프 스케줄러와 연산 코어, 온칩 메모리가 기본 실행 단위를 이루고 글로벌 메모리가 이를 뒷받침하는 계층 구조.
- SM (Streaming Multiprocessor) : 워프 스케줄러, 연산 코어 어레이, 온칩 메모리를 묶은 GPU 내부의 기본 실행 단위.

```text
[ GPU 실행 계층 ]

GPU 칩
   ↓
SM (Streaming Multiprocessor) 복수 배치
   ↓
워프 스케줄러 → 명령 발행 (워프 단위)
   ↓
연산 코어 어레이 (FP32, INT32, 텐서 코어)
   ↓
공유 메모리 / L1 캐시 (SM 내부)
```

```text
[ 메모리 계층 접근 경로 ]

공유 메모리 · 레지스터 (SM 내부, 저지연)
   ↓ 캐시 미스 시
L2 캐시 (GPU 칩 공유)
   ↓
글로벌 메모리 (GDDR 또는 HBM)
```

## Ⅳ. GPGPU(General-Purpose computing on GPU)의 비교

- 핵심 요약 : CPU는 지연 시간 최소화를, GPGPU는 처리량 극대화를 목표로 설계되어 워크로드 성격에 따라 갈림.

| 비교 항목 | CPU (Central Processing Unit) | GPGPU (General-Purpose GPU) |
| :--- | :--- | :--- |
| 설계 철학 | 지연 시간 최소화 (Latency-Oriented) | 처리량 극대화 (Throughput-Oriented) |
| 코어 구성 | 소수의 복잡한 대형 코어 | 수천 개 이상의 단순한 연산 코어 |
| 제어 로직 | 분기 예측과 비순차 실행 회로에 큰 면적 할당 | 단순한 제어 유닛, 면적 대부분을 연산에 배분 |
| 캐시 메모리 | 대용량 다단계 캐시로 메모리 지연 완화 | 상대적으로 작은 캐시, 워프 전환으로 지연 은폐 |
| 병렬 처리 단위 | 태스크 병렬성, 멀티스레딩 | 데이터 병렬성, SIMT |
| 최적 워크로드 | 복잡한 제어 흐름, 순차 트랜잭션, OS 커널 | 대규모 행렬 연산, 영상 처리, 딥러닝 텐서 연산 |

## Ⅴ. GPGPU(General-Purpose computing on GPU)의 한계와 방안

- 핵심 요약 : 워프 내 분기, 호스트와 디바이스 사이 전송, 비연속 메모리 접근을 각각 코드 구조와 메모리 설계로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| **워프 다이버전스** (Warp Divergence) | 워프 내 스레드가 서로 다른 분기 경로를 타면 경로를 순차 실행하며 나머지 스레드가 대기 → 처리량 급락 | 분기 최소화, 조건문을 산술 마스킹으로 치환, 같은 경로를 타는 스레드끼리 재배치 | 워프 실행 효율 |
| **PCIe** (Peripheral Component Interconnect Express) 전송 병목 | 호스트 메모리에서 GPU 메모리로의 복사가 연산보다 느려 대기 발생 | Unified Memory(통합 가상 메모리) 활용, 비동기 스트림으로 복사와 연산을 겹치는 파이프라이닝 | 호스트-디바이스 전송 대기 시간 |
| **메모리 결합** (Memory Coalescing) 실패 | 워프 스레드가 흩어진 주소를 읽으면 한 번에 묶어 처리하지 못해 메모리 트랜잭션이 크게 늘어남 | AoS(Array of Structures)를 SoA(Structure of Arrays)로 재설계하여 연속 주소 접근 보장 | 메모리 대역폭 활용률 |

## Ⅵ. GPGPU(General-Purpose computing on GPU)에 대한 기술사적 제언

- 핵심 요약 : 단일 벤더 생태계 의존을 줄이는 개방형 개발 환경과 저정밀도 연산 최적화를 병행하는 방향.

1. 특정 벤더의 CUDA 중심 생태계에 대한 의존 위험을 줄이기 위해, 조직의 개발 표준에 ROCm, oneAPI, SYCL 같은 개방형 프로그래밍 모델을 함께 포함하고 벤더 중립적인 커널 계층을 설계.
2. 딥러닝 워크로드에서 텐서 코어가 지원하는 혼합 정밀도 연산은 같은 전력으로 더 많은 연산을 처리하게 하므로, 모델 정밀도 요구 수준을 먼저 검증한 뒤 저정밀도 연산을 적용하는 절차를 수립.

## Ⅶ. 결론

- 핵심 요약 : GPGPU는 SIMT 기반 대규모 병렬 처리로 CPU 대비 처리량을 크게 끌어올리지만, 워프 다이버전스·전송 병목·메모리 결합 실패를 함께 관리해야 하는 구조.
- 시사점 : 데이터 병렬성이 큰 워크로드에서 효과가 두드러지며, 알고리즘과 메모리 배치를 GPU 구조에 맞게 설계하는 것이 성능의 전제가 됨.
