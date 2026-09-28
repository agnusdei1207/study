---
sidebar:
  order: 83
  label: "083. GPGPU"
  badge:
    text: "기초"
    variant: note
title: "GPGPU (General-Purpose computing on Graphics Processing Units)"
author: "Antigravity"
date: "2026-09-24T23:30:00+09:00"
tags:
  - "notes-computer-system"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
  question_no: "083"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 병렬 컴퓨팅 → GPU 범용 연산 활용

## 30초 인출

- 본질: **GPGPU (General-Purpose computing on Graphics Processing Units)는** 그래픽 처리용 GPU를 데이터 병렬성이 높은 범용 계산에 활용하는 방식
- 메커니즘: CPU가 작업·데이터를 준비하고 GPU 커널을 실행하며, 다수 스레드가 데이터에 같은 연산을 적용
- 통찰: 그래픽 렌더링에 국한되던 GPU의 초병렬 연산 능력을 CUDA 및 OpenCL 프레임워크를 통해 범용 수치 연산, 딥러닝, 암호 해독, 물리 시뮬레이션에 확장 적용한 기술임.

<details>
<summary>핵심 용어</summary>

- **GPGPU (General-Purpose computing on Graphics Processing Units)** : 그래픽 외의 일반 계산을 GPU에서 수행하는 컴퓨팅 방식
- **SIMT (Single Instruction, Multiple Threads)** : 여러 스레드를 묶어 동일한 명령을 여러 데이터에 적용하는 GPU 실행 모델
- **커널 (Kernel)** : GPU에서 병렬 실행하도록 작성한 계산 함수
- **워프 (Warp)** : NVIDIA GPU에서 함께 스케줄되는 스레드 묶음; 크기·세부 동작은 아키텍처별 확인 필요
- **메모리 병합 접근 (Coalesced Memory Access)** : 스레드의 메모리 요청을 효율적인 데이터 전송으로 묶는 접근 패턴
</details>

---

## 2~4교시 예상문제 (25점)

> GPGPU의 실행 구조와 CPU와의 역할 분담을 설명하고, 응용시스템 적용 시 성능·데이터 이동 고려사항을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. GPGPU의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **GPGPU (General-Purpose computing on Graphics Processing Units)는** GPU의 병렬 실행 자원을 그래픽 이외의 범용 계산에 이용하는 방식 |
| 목적 | 데이터 병렬 계산에서 처리량을 높이고 CPU와 이기종으로 작업을 수행하는 것 |

## Ⅱ. 대량 데이터 병렬 처리의 특징

| 특징 | 의미 |
|---|---|
| 이기종 역할 분담 | CPU가 제어·작업 제출, GPU가 반복 계산을 병렬 처리 |
| SIMT 실행 | 여러 스레드가 같은 명령 흐름으로 서로 다른 데이터 처리 |
| 데이터 이동 비용 | 계산량 외에도 호스트·디바이스 전송과 동기화가 성능을 결정 |

## Ⅲ. 호스트·디바이스의 커널 실행 체계

```text
CPU: 입력 준비·작업 분할
  ↓ 전송·커널 제출
GPU 메모리 → 스레드 블록 → 실행 묶음별 데이터 병렬 커널
  ↓ 완료 동기화·결과 이동
CPU: 결과 결합·후속 제어
```

스레드는 개별 데이터 연산, 블록은 공유 메모리 기반 협업 및 자원 할당 단위 형성. 워프(Warp) 실행 단위의 크기와 스케줄링 메커니즘은 GPU 아키텍처 세대별로 상이.

## Ⅳ. CPU 처리와 GPU 오프로딩의 비교

| 판단축 | CPU 중심 | GPGPU 활용 |
|---|---|---|
| 적합 작업 | 복잡한 분기·의존성·시스템 제어 | 큰 데이터 집합의 반복 계산 |
| 메모리 | 호스트 자료에 직접 접근 | GPU 자료 재사용이 클수록 유리 |
| 비용 | CPU 실행시간·자원 | 전송·동기화·GPU 메모리·전력·개발 비용 |
| 병목 | 순차 처리·코어 수 | 분기 발산·비병합 메모리 접근 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 데이터 복사·동기화가 병렬 계산의 가속 이득을 줄임 | 데이터 재사용·배치·비동기 전송을 종단 프로파일링 결과에 따라 적용 |
| 분기 발산과 비병합 메모리 접근으로 처리량 저하 | 스레드 배치와 데이터 레이아웃을 커널 단위로 측정·조정 |
| 피크 연산량으로 서비스 성능을 예측하기 어려움 | 대표 데이터의 지연·처리량·메모리·전력·비용을 CPU 기준선과 비교 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
호스트 CPU-GPU 간 PCIe 데이터 전송 병목을 줄이기 위해 통합 메모리(Unified Memory)와 비동기 스트림(CUDA Stream) 파이프라이닝을 적용하여 연산과 전송을 중첩 수행.

### 2. 아키텍처 및 상세 메커니즘
```text
[ 호스트 CPU 프로세서 ]                               [ 디바이스 GPGPU 가속기 ]
        │                                                         │
        │ 1. cudaMemcpy(HostToDevice): 입력 데이터 전송 (PCIe)      │
        ├────────────────────────────────────────────────────────>│
        │                                                         │
        │ 2. 커널 함수 실행 명령 (kernel<<<Grid, Block>>>)         │
        ├────────────────────────────────────────────────────────>│
        │                                                         │ 3. 대규모 SIMT 병렬 연산 수행
        │                                                         │   (수만 개 스레드가 동시 실행)
        │                                                         │
        │ 4. cudaMemcpy(DeviceToHost): 최종 연산 결과 복원        │
        │<────────────────────────────────────────────────────────┤
        ▼                                                         ▼
```

### 3. 기술 유형 및 비교 평가
| 개발 프레임워크 | 개발 주체 | 하드웨어 호환성 | 에코시스템 및 성능 최적화 |
|---|---|---|---|
| **CUDA** | NVIDIA 독점 | NVIDIA GPU 전용 | 업계 표준, 최고 수준의 딥러닝 라이브러리(cuDNN, TensorRT) 지원 |
| **OpenCL** | Khronos 그룹 | 개방형 표준 (Intel, AMD, ARM, Apple) | 범용성 우수, 벤더별 최적화 난이도 높음 |
| **ROCm** | AMD | AMD Radeon / Instinct GPU | 오픈소스 기반, 최근 PyTorch 지원 및 생태계 급성장 |

## 출제 이력과 검증 출처

- David B. Kirk, Wen-mei W. Hwu - Programming Massively Parallel Processors: A Hands-on Approach
- NVIDIA CUDA C++ Programming Guide and Best Practices
- ACM Computing Surveys: General-Purpose Computing on Graphics Processing Units (GPGPU)

## 연결 토픽

- 상위 토픽: [020 GPU](./020_gpu.md)
- 연관 토픽: [007 NPU](./007_npu.md), [094 멀티 GPU](./094_multi_gpu.md)
