---
sidebar:
  order: 0
title: "컴퓨터 시스템"
description: "컴퓨터구조·운영체제에서 가상화·클라우드·AI 인프라까지 이어지는 과목 학습 로드맵"
weight: 4
---

## 8과목 전체 지도와 현재 위치

```text
[01 IT 전략] ── [02 SW 공학] ── [03 데이터] ── [04 시스템 ◀ 현재 과목]
      │                 │               │                    │
      └──────────── 가치·요구·정보·처리 기반 ───────────────┘
                                                                │
                                                                ▼
[08 법·정책] ── [06 보안] ───── [05 네트워크] ── [07 AI·디지털]
 규범·책임         신뢰 경계             연결·전송          지능·서비스 확장
```

- 04 시스템은 **데이터를 실행하는 계산 자원과 운영 기반**을 설명하며, 네트워크·보안·AI 서비스가 올라가는 공통 하부 구조
- 앞 과목 연결: SW의 실행 단위와 데이터의 저장 요구를 CPU·메모리·스토리지·OS가 구현
- 뒤 과목 연결: 네트워크 연결, 보안 통제, AI 가속·클라우드 서비스의 성능·가용성 기반 제공

## 04 컴퓨터 시스템 확대 지도

```text
                         [컴퓨터 시스템]
                                │
            ┌───────────────────┼───────────────────┐
            ▼                   ▼                   ▼
      [컴퓨터구조]          [운영체제]          [인프라·클라우드]
 CPU·GPU·NPU·TPU       프로세스·스레드       가상화·컨테이너
 메모리 계층·캐시       동기화·교착상태        K8s·서버리스
 병렬처리·Flynn         스케줄링·가상메모리    HA·DR·스토리지
            │                   │                   │
            └──────────────┬────┴──────────────┬────┘
                           ▼                   ▼
                    [성능·신뢰성]        [AI·차세대 인프라]
                  병목·튜닝·가용성      HBM·CXL·칩렛·액체냉각
                           │                   │
                           └──────────┬────────┘
                                      ▼
                         [서비스 수준·비용·에너지 최적화]
```

- 관통 질문: **명령과 데이터를 어디서 처리하고, 자원을 누가 배분하며, 장애와 병목을 어떻게 통제하는가?**

## 30초 인출

```text
구조: CPU ↔ Cache ↔ Memory ↔ Storage
             │
OS: Process → Scheduling → Synchronization → Virtual Memory
             │
추상화: VM → Container → Kubernetes → Serverless
             │
운영: HA·FTS → DR → Observability·Auto Scaling
             │
확장: GPU·NPU·TPU ↔ HBM·CXL·Chiplet ↔ Cooling·Power
```

## 학습 단계와 누적 회독

| 학습 단계 | 의미 | 누적 회독 |
|---|---|---|
| **A·기초** | 기초·필수 개념 | A |
| **B·확장** | A의 적용·구현·비교 확장 | A+B |
| **C·심화** | B에서 파생되는 심화·융합 개념 | A+B+C |

> 전체 키워드를 보존하고 회독 범위를 누적 확장한다.

## 영역별 토픽 링크

### 1. 운영체제 자원관리

- [은행가 알고리즘](./002_bankers_algorithm/)
- [프로세스 동기화 기법](./122_process_synchronization/)
- [CPU 스케줄링](./019_cpu_scheduling/), [가상 메모리](./023_virtual_memory/), [디스크 스케줄링](./024_disk_scheduling/)
- [교착상태](./038_deadlock/), [스레싱](./039_thrashing/), [IPC](./034_ipc/)

### 2. 컴퓨터구조·가속기

- [CPU](./076_cpu/), [GPU](./020_gpu/), [TPU](./022_tpu/), [NPU](./007_npu/)
- [캐시 메모리·일관성](./051_cache_memory/), [메모리 계층·인터리빙](./096_memory_hierarchy_interleaving/)
- [HBM](./079_hbm/), [CXL](./063_cxl/), [칩렛·UCIe](./030_chiplet_ucie_3_0/)

### 3. 가상화·클라우드

- [가상화](./008_virtualization/), [하이퍼바이저](./061_hypervisor/), [가상머신](./085_virtual_machine/)
- [컨테이너](./032_container/), [쿠버네티스](./012_kubernetes/), [서버리스](./003_serverless_computing/)
- [클라우드 컴퓨팅](./013_cloud_computing/), [멀티 클라우드](./009_multi_cloud/), [서비스 모델](./109_cloud_computing_service_models/)

### 4. 스토리지·가용성·재해복구

- [스토리지 유형 비교](./123_storage_type_comparison/)
- [HA·FTS](./042_ha_availability_assurance/), [RAID](./056_raid/)
- [멀티 리전 Active-Active DR](./068_multi_region_active_active_disaster_recovery/)

### 5. 최신 AI 인프라

- [AI HPC 인프라](./041_ai_hpc_infrastructure/), [랙 스케일 AI 시스템](./070_rack_scale_ai_system/)
- [액체냉각](./028_liquid_cooling/), [에너지 효율 컴퓨팅](./073_energy_efficient_computing/)
- [하드웨어 규모산정](./117_hardware_sizing/), [성능 튜닝](./120_performance_tuning/)

## 일반 학습 원칙

- 컴퓨터구조·OS의 기초 개념을 최신 인프라의 동작 원리와 연결한다.
- 최신 규격·제품 수치·정책은 작성일 기준 1차 출처로 재검증하고, 검증하지 않은 성능 배수는 쓰지 않는다.
