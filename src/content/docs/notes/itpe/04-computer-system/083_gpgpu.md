---
title: "GPGPU (General-Purpose computing on Graphics Processing Units)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- GPGPU(General-Purpose computing on GPU), CUDA(Compute Unified Device Architecture)
- SIMT(Single Instruction, Multiple Threads), 워프(Warp), 커널(Kernel)
- 그리드·블록·스레드 계층, 지연 은폐(Latency Hiding), 공유 메모리(Shared Memory)
- 워프 다이버전스(Warp Divergence), 메모리 결합(Memory Coalescing), 통합 메모리(Unified Memory)
- PCIe, ROCm(Radeon Open Compute), SYCL

## Ⅰ. GPGPU의 개요

- 핵심 요약 : **GPGPU** (General-Purpose computing on GPU)는 GPU의 대규모 병렬 연산 구조를 그래픽 외 범용 수치 계산에 활용하는 컴퓨팅 방식.
- 개념 : 그래픽 처리용으로 발전한 GPU(Graphics Processing Unit)의 다수 연산 코어를 과학 기술 계산, 딥러닝, 영상 분석 등 범용 연산에 활용하는 방식과 그 프로그래밍 모델.
- 배경 및 필요성 : 소수의 고성능 코어로 지연 시간을 줄이는 CPU(Central Processing Unit)만으로 대규모 행렬 연산 중심의 AI(Artificial Intelligence) 워크로드를 감당하기 어려움.
- 주요 목적 : 데이터 병렬성에 기반한 연산 처리량 극대화와 와트당 연산 효율 향상.

## Ⅱ. GPGPU의 특징 및 장점

- 핵심 요약 : SIMT 실행 모델과 지연 은폐, 공유 메모리, 계층적 프로그래밍 모델이 대량 데이터의 동시 처리를 실현하는 구조.

1. **SIMT** (Single Instruction, Multiple Threads) 실행 모델 : 32개의 스레드를 **워프** (Warp) 단위로 묶어 한 명령을 여러 데이터에 동시 적용 → 명령 발행 비용을 다수 스레드가 분담하는 처리량 증가 효과.
2. **지연 은폐** (Latency Hiding) : 메모리 접근으로 대기 중인 워프를 준비된 다른 워프로 즉시 교체 → 연산 유닛 가동률 유지 효과.
3. **공유 메모리** (Shared Memory) : 같은 블록 내 스레드가 온칩 메모리에 데이터를 공유 → 글로벌 메모리의 반복 접근 감소 효과.
4. 계층적 프로그래밍 모델 : **CUDA** (Compute Unified Device Architecture)가 **커널** (Kernel)을 그리드·블록·스레드 계층으로 구성 → 소프트웨어 계층과 하드웨어 계층의 대응에 따른 최적화 효과.

## Ⅲ. GPGPU의 구조 (흐름)

- 핵심 요약 : 커널 호출이 그리드→블록→워프→스레드 계층으로 분배되어 SM(Streaming Multiprocessor)에서 실행되는 구조.
- SM : 워프 스케줄러와 연산 코어 어레이, 온칩 메모리를 묶은 GPU 내부의 기본 실행 단위.

```text
[ CUDA 실행 계층 ]

호스트(CPU)의 커널 호출
      ↓
그리드 (전체 스레드 집합)
      ↓
블록 (SM에 할당되는 단위)
      ↓
워프 (32스레드, 명령 발행 단위)
      ↓
스레드 (최소 연산 단위)
```

```text
[ 메모리 계층 접근 경로 ]

레지스터 · 공유 메모리 (블록 내부)
      ↓ 캐시 미스 시
L2 캐시 (GPU 칩 전체 공유)
      ↓
글로벌 메모리 (HBM(High Bandwidth Memory))
```

## Ⅳ. CUDA와 개방형 프로그래밍 모델의 비교

- 핵심 요약 : CUDA의 성숙한 단일 벤더 생태계와 ROCm·SYCL의 벤더 중립성·이식성이 각각 다른 요구에 대응하는 선택지.

| 비교 축 | CUDA | ROCm | SYCL |
| :--- | :--- | :--- | :--- |
| 성격 | NVIDIA 자사 표준 생태계 | AMD 개방형 소프트웨어 스택 | Khronos 표준 단일 소스 모델 |
| 대상 하드웨어 | NVIDIA GPU 계열 | AMD GPU | 다종 GPU·CPU·가속기 |
| 생태계 성숙도 | 라이브러리와 프레임워크 최다 | 성장 단계 | 성장 단계 |
| 이식성 | NVIDIA 계열에 한정 | CUDA 코드의 이식 도구 제공 | 이기종 백엔드 대응 |

- 선택 기준 :
  1. 검증된 라이브러리와 즉시 성능이 우선이면 CUDA
  2. AMD 하드웨어 자산의 활용이 전제이면 ROCm
  3. 벤더 종속 완화와 장기 이식성이 목표이면 SYCL

## Ⅴ. GPGPU의 한계와 방안

- 핵심 요약 : 분기 분산, 전송 병목, 비연속 메모리 접근을 코드 구조와 메모리 배치 설계로 통제하는 체계.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| **워프 다이버전스** (Warp Divergence) | 워프 내 스레드의 분기 경로 분리 시 경로별 순차 실행 → 유휴 스레드 대기로 처리량 급락 | 조건문 최소화, 같은 경로의 스레드 재배치로 분기 통일 | 워프 실행 효율 |
| **PCIe** (Peripheral Component Interconnect Express) 전송 병목 | 호스트 메모리와 GPU 메모리 간 복사가 연산보다 느림 → 대기 발생 | 통합 메모리(Unified Memory)와 비동기 스트림으로 복사·연산의 중첩 | 전송 대기 시간 |
| **메모리 결합** (Memory Coalescing) 실패 | 워프 스레드의 흩어진 주소 접근으로 트랜잭션 급증 → 대역폭 낭비 | SoA(Structure of Arrays) 재설계로 연속 주소 접근 보장 | 대역폭 활용률 |

## Ⅵ. GPGPU에 대한 기술사적 제언

- 핵심 요약 : 벤더 종속의 완화와 성능 엔지니어링 역량의 조직적 내재화가 필요.

1. 플랫폼 개발 조직은 커널 호출부를 추상화한 공용 라이브러리로 가속기 의존 코드를 한 지점에 격리하는 개발 표준 수립.
2. 성능 엔지니어링 조직은 워크로드의 정밀도 요구 검증 후 텐서 코어의 혼합 정밀도(mixed precision) 연산을 적용하는 절차 표준화.
3. 품질 보증 조직은 프로파일링 지표 점검 항목을 코드 리뷰 체크리스트에 포함하는 품질 관리 체계 운영.

## Ⅶ. 결론

- 핵심 요약 : GPGPU는 SIMT 기반의 대규모 데이터 병렬 처리로 범용 연산 처리량을 끌어올리는 컴퓨팅 방식.
- 시사점 : 실행 모델과 메모리 계층에 맞춘 알고리즘 설계가 성능의 전제이며, 프로그래밍 모델 선택은 생태계 성숙도와 이식성의 균형으로 결정.
