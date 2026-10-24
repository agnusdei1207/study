---
title: "하이퍼바이저 (Hypervisor)"
author: "agnusdei1207"
date: "2026-10-24T22:33:35+09:00"
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

- 하이퍼바이저(Hypervisor), VMM(Virtual Machine Monitor), 가상머신(VM), 게스트 OS(Guest OS)
- Type 1, Type 2, VT-x, AMD-V, EPT(Extended Page Tables), SR-IOV(Single Root I/O Virtualization)
- 서버 통합(Server Consolidation), 실시간 이전(Live Migration), KSM(Kernel Samepage Merging), 노이지 네이버(Noisy Neighbor)
- KVM(Kernel-based Virtual Machine), KubeVirt, MicroVM, DPU(Data Processing Unit)

## Ⅰ. 하이퍼바이저 (Hypervisor)의 개요

- 핵심 요약 : **하이퍼바이저**는 물리 하드웨어를 추상화하여 여러 운영체제를 가상머신에 나눠 격리 실행하는 시스템 가상화 계층.
- 개념 : 하나의 물리 호스트에서 서로 다른 운영체제(OS, Operating System)를 게스트 OS(Guest OS)로 동시에 구동하도록 CPU(Central Processing Unit), 메모리, 스토리지, 네트워크를 추상화하고 중재하는 시스템 가상화 소프트웨어 계층으로, 가상머신 모니터(VMM, Virtual Machine Monitor)라고도 함.
- 배경 및 필요성 : 단일 서버에 단일 운영체제를 올리는 방식은 평균 CPU 이용률이 낮게 머무는 자원 유휴 비용을 낳고, 서버를 늘리면 설치 공간과 전력을 포함한 총소유비용(TCO, Total Cost of Ownership)이 함께 커짐. 이 비용을 줄이려고 한 대의 물리 서버를 여러 가상머신(VM, Virtual Machine)으로 나누는 계층이 필요해졌으며, 이는 서비스형 인프라(IaaS, Infrastructure as a Service)의 토대가 됨.
- 주요 목적 : **서버 통합** (Server Consolidation)을 통한 하드웨어 활용률 향상, 가상머신 간 격리, VM 스냅샷과 무중단 **실시간 이전** (Live Migration) 실현.

## Ⅱ. 하이퍼바이저 (Hypervisor)의 특징 및 장점

- 핵심 요약 : 하이퍼바이저의 설치 위치와 하드웨어 지원 기능이 맞물려 성능, 격리, I/O 효율을 함께 끌어올리는 구조.

1. **Type 1 하이퍼바이저** (Bare-Metal) : 호스트 OS 없이 하드웨어 위에 직접 설치 → 중간 계층이 없어 오버헤드가 작고 성능과 격리가 강함 (VMware ESXi, **KVM**(Kernel-based Virtual Machine), Xen 등).
2. **Type 2 하이퍼바이저** (Hosted) : 기존 운영체제 위에서 일반 프로세스처럼 실행 → 설치와 사용이 간편하지만 호스트 OS를 거치므로 성능 손실이 생김 (VirtualBox, VMware Workstation 등).
3. **CPU 하드웨어 가상화** : **VT-x**(Intel Virtualization Technology), **AMD-V**(AMD Virtualization)가 게스트의 특권 명령을 하드웨어가 가로채 하이퍼바이저가 대신 처리 → 명령어 번역 같은 소프트웨어 우회 비용 감소.
4. **메모리 가상화** : **EPT**(Extended Page Tables, Intel) 또는 NPT(Nested Page Tables, AMD)가 게스트 물리 주소를 호스트 물리 주소로 하드웨어가 2단계 변환 → 주소 변환을 소프트웨어가 중계할 필요가 줄어듦.
5. **I/O 가상화** : **SR-IOV**(Single Root I/O Virtualization)가 물리 네트워크 인터페이스 카드(NIC, Network Interface Card)를 여러 가상 기능(VF, Virtual Function)으로 나눠 가상머신이 하이퍼바이저를 거치지 않고 장치에 직접 접근 → 네이티브에 가까운 I/O 성능.

## Ⅲ. 하이퍼바이저 (Hypervisor)의 구조 및 동작 메커니즘

- 핵심 요약 : 하이퍼바이저는 하드웨어 위에 바로 올라서는 Type 1과 호스트 OS 위에서 구동되는 Type 2로 나뉘며, 차이는 하드웨어 제어 경로의 길이에 있음.

```text
[ Type 1 (베어메탈) 구조 ]

VM1 (Linux)     VM2 (Windows)
      ↓               ↓
Type 1 하이퍼바이저
(ESXi, KVM, Xen, Hyper-V)
      ↓
물리 하드웨어
```

```text
[ Type 2 (호스티드) 구조 ]

VM1 (Linux)     VM2 (Windows)
      ↓               ↓
Type 2 하이퍼바이저
(VirtualBox, VMware Workstation)
      ↓
호스트 OS (일반 데스크톱 OS)
      ↓
물리 하드웨어
```

- Type 1은 하드웨어를 직접 제어하므로 엔터프라이즈와 클라우드 인프라의 표준이 되었고, Type 2는 개인 개발과 테스트 환경에서 손쉬운 실행 수단으로 쓰임.

## Ⅳ. 하이퍼바이저 (Hypervisor)의 비교

- 핵심 요약 : Type 1, Type 2, 컨테이너는 실행 계층의 깊이에 따라 성능과 격리, OS 다양성이 달라지며, 하이퍼바이저는 완전한 격리와 이종 OS 구동에서 강점을 가짐.

| 비교 항목 | Type 1 하이퍼바이저 (ESXi, KVM) | Type 2 하이퍼바이저 (VirtualBox) | 컨테이너 (Docker, 쿠버네티스) |
| --- | --- | --- | --- |
| 실행 계층 | 베어메탈 하드웨어 직접 구동 | 호스트 OS 위의 애플리케이션 | 호스트 OS 커널 공유 |
| 성능 오버헤드 | 낮음 | 중간 | 매우 낮음 (네이티브에 가까움) |
| 보안 격리 강도 | 하드웨어 수준 격리 (강함) | 호스트 OS에 의존 | 커널 공유로 상대적으로 약함 |
| 운영체제 다양성 | 이종 OS 동시 구동 | 이종 OS 구동 가능 | 호스트 커널과 같은 계열 OS만 구동 |
| 기동 소요 | 상대적으로 김 | 보통 | 짧음 |

- 선택 기준 : 이종 OS 격리와 보안 경계가 중요하면 하이퍼바이저를, 같은 OS 계열에서 경량 배포가 중요하면 컨테이너를 택하는 등 두 계층은 상호 보완적으로 공존함.

## Ⅴ. 하이퍼바이저 (Hypervisor)의 한계와 방안

- 핵심 요약 : 메모리 중복, vCPU 경합, 벤더 종속을 KSM 병합, vCPU 고정, 오픈소스 전환과 KubeVirt 통합으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 게스트별 메모리 중복 | 가상머신마다 독립 커널과 시스템 프로세스가 적재되어 메모리 낭비 | **KSM**(Kernel Samepage Merging)으로 동일 페이지를 병합, 컨테이너와 혼용 | 호스트 메모리 사용률, 병합 페이지 수 |
| **노이지 네이버**(Noisy Neighbor)로 인한 vCPU 경합 | 특정 VM의 CPU 과점유로 다른 VM의 스케줄 지연과 스틸 타임(Steal Time) 증가 | vCPU 고정(Pinning, Affinity), 쿼터와 Shares 기반 자원 우선순위 보장 | 스틸 타임 비율, 응답 지연 |
| 벤더 종속과 라이선스 비용 상승 | VMware 인수 이후 라이선스 정책이 바뀌어 구독 전환과 비용 증가 → 엔터프라이즈 TCO 상승 | 오픈소스 KVM 기반 전환, **KubeVirt** (쿠버네티스 위에서 가상머신을 실행하는 기술)로 컨테이너와 VM 통합 관리 | 라이선스 비용, 전환 기간 |

## Ⅵ. 하이퍼바이저 (Hypervisor)의 적용 제언

- 핵심 요약 : 레거시 VM과 컨테이너를 한 제어면에서 다루고, 경량 VM과 하드웨어 오프로드로 함수 실행과 가상화 비용을 함께 낮추는 방향.

1. 플랫폼 운영 조직은 기존 VM 자산을 버리지 않고 KubeVirt 기반으로 컨테이너와 가상머신을 같은 제어면에서 배포하여, 레거시 워크로드의 이전 부담을 단계적으로 낮춘다.
2. 서버리스와 다중 테넌트 서비스를 운영하는 조직은 **MicroVM** (경량 가상머신, 예: Firecracker)을 도입하여 함수 실행 단위를 가상머신 경계로 감싸면서도 기동 속도를 유지한다.
3. 데이터센터 인프라 조직은 **DPU** (Data Processing Unit) 같은 하드웨어 오프로드로 가상 스위치(OVS, Open vSwitch)와 스토리지 처리를 호스트 CPU에서 분리하여, 가상화에 쓰이던 CPU 자원을 워크로드 쪽으로 되돌린다.

## Ⅶ. 결론

- 핵심 요약 : 하이퍼바이저는 하드웨어 추상화로 VM 격리와 서버 통합, 실시간 이전을 실현하는 계층이며, 메모리 중복·vCPU 경합·벤더 종속 관리가 필수.
- 하이퍼바이저는 격리를 얻는 대가로 계층 비용을 치르는 기술이므로, 컨테이너와 역할을 나누어 쓰는 설계를 전제로 도입해야 한다.
