---
title: "GPGPU (General-Purpose computing on Graphics Processing Units)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. GPGPU(General-Purpose computing on GPU)의 개요

- 개념 : 본래 3차원 그래픽 렌더링 파이프라인 처리를 위해 개발된 그래픽스 처리 장치(GPU, Graphics Processing Unit)의 대규모 병렬 연산 하드웨어 구조를 그래픽 이외의 과학 계산, 암호 해독, 빅데이터 분석, 딥러닝 AI(Artificial Intelligence) 등 **범용 수치 계산** (General-Purpose Computing)에 활용하는 컴퓨팅 아키텍처 및 프로그래밍 패러다임.
- 배경 및 필요성 : 직렬 제어 흐름과 레이턴시 최소화에 최적화된 소수의 강력한 코어를 가진 CPU(Central Processing Unit)로는 수억~수천억 회의 반복 행렬 연산이 필요한 현대 AI 모델 연산을 감당할 수 없어, 대규모 연산 코어를 집적한 GPU의 병렬 처리 능력이 주목받음.
- 핵심 목적 : 대규모 **데이터 병렬성** (Data Parallelism)을 활용한 수십 TFLOPS~PFLOPS 급 **연산 처리량(Throughput)** 달성, CPU 대비 와트당 연산 가성비 극대화.

## Ⅱ. GPGPU의 핵심 아키텍처 및 SIMT 실행 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ GPGPU 하드웨어 구조 (Streaming Multiprocessor: SM) 및 SIMT 모델 ]   │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 스트리밍 멀티프로세서 (Streaming Multiprocessor: SM)           │   │
│   │  ┌──────────────────────────────────────────────────────────┐  │   │
│   │  │ 워프 스케줄러 (Warp Scheduler) & 디스패치 유닛           │  │   │
│   │  │ (32개 스레드로 구성된 워프(Warp) 단위로 명령어를 락스텝 발행)│  │   │
│   │  └──────────────────────────┬───────────────────────────────┘  │   │
│   │                             ▼                                  │   │
│   │  ┌──────────────────────────────────────────────────────────┐  │   │
│   │  │ 대규모 연산 코어 어레이 (FP32, FP64, INT32, Tensor Cores)│  │   │
│   │  │  [Core 0] [Core 1] [Core 2] ... [Core 31] (Warp 32 Threads)│  │   │
│   │  └──────────────────────────────────────────────────────────┘  │   │
│   │  ┌──────────────────────────────────────────────────────────┐  │   │
│   │  │ 고속 공유 메모리 / L1 데이터 캐시 (Shared Memory: 128KB+)│  │   │
│   │  │ (스레드 블록 내부의 초고속 데이터 공유 및 메모리 결합)   │  │   │
│   │  └──────────────────────────────────────────────────────────┘  │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │ Global Memory Access               │
│                                   ▼                                    │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 대용량 공유 L2 캐시 및 초고대역폭 글로벌 메모리 (GDDR6 / HBM3E)│   │
│   └────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

- **SIMT(Single Instruction, Multiple Threads) 실행 모델** : 32개의 스레드가 '워프(Warp)'라는 단일 실행 단위로 묶여 동일한 명령어를 서로 다른 데이터(SIMD(Single Instruction, Multiple Data) 확장)에 대해 락스텝(Lock-step)으로 동시 실행.
- **대규모 스레드 기반 지연 은폐(Latency Hiding)** : 메모리 I/O 지연 발생 시 CPU처럼 캐시나 대기에 의존하지 않고, 워프 스케줄러가 즉각 연산 준비가 완료된 다른 워프로 제어권을 넘겨 연산 파이프라인 유휴 상태를 은폐.

## Ⅲ. CPU와 GPGPU의 아키텍처 및 설계 철학 비교 분석

| 비교 항목 | CPU (Central Processing Unit) | GPGPU (General-Purpose GPU) |
| :--- | :--- | :--- |
| **설계 철학** | 지연 시간 최소화 (Latency-Oriented)| 처리량 극대화 (Throughput-Oriented) |
| **코어 구성** | 4 ~ 128개의 복잡하고 강력한 대형 코어 | 수천 ~ 수만 개의 단순한 소형 산술 코어 |
| **제어 로직 (Control)**| 분기 예측기, 비순차 실행(OoO) 회로에 다이 면적 대거 할당| 단순 제어 유닛, 다이 면적의 대부분을 ALU(Arithmetic Logic Unit)에 집중 |
| **캐시 메모리** | 대용량 L1, L2, L3 캐시로 메모리 지연 극소화| 상대적으로 작은 캐시, 스레드 전환으로 지연 은폐 |
| **병렬 처리 단위** | 태스크 병렬성 (Task Parallelism), 멀티스레딩| 데이터 병렬성 (Data Parallelism), SIMT |
| **최적 워크로드** | 복잡한 제어 흐름, 순차적 트랜잭션, OS(Operating System) 커널 | 대규모 행렬 곱셈, 영상 처리, 딥러닝 텐서 연산 |

## Ⅳ. GPGPU 컴퓨팅의 주요 한계점 및 해결 방안

- **분기 다이버전스** (Warp Divergence)로 인한 성능 급락 :
  - 한계점 : 워프 내 32개 스레드 간 `if-else` 분기 조건이 갈라질 경우, 각 분기 경로를 순차 실행하면서 비활성 스레드가 대기하여 성능이 최대 1/N로 저하.
  - 해결 방안 : 분기문 최소화, 조건 연산자를 산술 연산 마스킹으로 치환, 동일 분기 경로를 가진 스레드끼리 워프 재그룹화.
- **호스트-디바이스(PCIe, Peripheral Component Interconnect Express)** 간 데이터 전송 대역폭 병목 :
  - 한계점 : 호스트 CPU 메모리에서 GPU 글로벌 메모리로 데이터를 복사하는 PCIe 버스 속도가 GPU 내부 연산 속도보다 현저히 느려 I/O 대기 발생.
  - 해결 방안 : Unified Memory(통합 가상 메모리) 도입, 호스트 메모리와 GPU 간 비동기 스트림(Stream) 복사 및 연산 오버랩(Overlap) 파이프라이닝.
- 비연속 메모리 접근에 따른 **메모리 결합(Memory Coalescing)** 실패 :
  - 한계점 : 워프 내 스레드들이 연속된 메모리 주소를 읽지 않고 산발적인 오프셋을 접근할 경우 메모리 트랜잭션 수가 32배 폭증.
  - 해결 방안 : 데이터 구조를 AoS(Array of Structures)에서 SoA(Structure of Arrays)로 재설계하여 메모리 정렬 및 연속 주소 접근 보장.

## Ⅴ. 미래 컴퓨팅 환경에서의 기술사적 제언

- 소프트웨어 **에코시스템(CUDA(Compute Unified Device Architecture) 독점)** 탈피를 위한 개방형 표준 육성 : 현재 GPGPU 생태계는 NVIDIA CUDA에 과도하게 종속되어 있으므로, AMD(Advanced Micro Devices) ROCm, 인텔 oneAPI 및 Khronos SYCL, OpenAI Triton과 같은 이기종 공통 프레임워크를 기반으로 벤더 중립적 고성능 커널 개발 체계를 확립해야 함.
- **텐서 코어(Tensor Core)** 및 저정밀도(FP4/INT4) 연산 최적화 : 범용 FP32 연산에 머무르지 않고 하드웨어 가속 텐서 코어의 다차원 행렬 곱셈 누적(MMA, Matrix Multiply-Accumulate) 명령어를 직접 활용하며, 정확도 손실을 최소화하는 FP8/FP4 혼합 정밀도(Mixed Precision) 엔지니어링을 적극 도입할 것을 제언함.
