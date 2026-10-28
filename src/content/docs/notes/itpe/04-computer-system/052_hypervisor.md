---
title: "하이퍼바이저 (Hypervisor)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "052"
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- 하이퍼바이저(Hypervisor), VMM(Virtual Machine Monitor), 가상머신(VM), 게스트 OS(Guest OS)
- Type 1, Type 2, VT-x, AMD-V, EPT(Extended Page Tables), SR-IOV(Single Root I/O Virtualization)
- 서버 통합(Server Consolidation), 실시간 이전(Live Migration), KSM(Kernel Samepage Merging)
- 노이지 네이버(Noisy Neighbor), KVM(Kernel-based Virtual Machine), KubeVirt, MicroVM, DPU(Data Processing Unit)

## Ⅰ. 하이퍼바이저의 개요

- 핵심 요약 : 물리 하드웨어를 추상화하여 여러 운영체제(OS, Operating System)를 **가상머신** (VM, Virtual Machine)에 나누어 격리 실행하는 **하이퍼바이저** (Hypervisor) 계층.
- 개념 : 하나의 물리 호스트에서 CPU(Central Processing Unit)·메모리·스토리지·네트워크를 추상화하고 중재하여, 서로 다른 게스트 OS(Guest OS)를 가상머신 단위로 동시 구동하는 시스템 가상화 소프트웨어. 가상머신 모니터(VMM, Virtual Machine Monitor)라는 명칭도 함께 사용됨.
- 배경 및 필요성 : 단일 서버·단일 운영체제 구조는 낮은 자원 이용률과 서버 증설에 따른 공간·전력 비용을 수반. 이 비용을 줄이는 하드웨어 공유 계층이 필요하며, 서비스형 인프라(IaaS, Infrastructure as a Service)의 토대가 되는 기술.
- 주요 목적 : **서버 통합** (Server Consolidation)을 통한 하드웨어 활용률 향상, 가상머신 간 격리 확보, 스냅샷과 **실시간 이전** (Live Migration) 같은 운영 기능의 실현.

## Ⅱ. 하이퍼바이저의 특징 및 장점

- 핵심 요약 : 설치 위치(Type 1·Type 2)의 선택과 CPU·메모리·입출력의 하드웨어 가상화 지원이 성능·격리·효율을 함께 끌어올리는 구조.

1. **Type 1 하이퍼바이저** (베어메탈형) : 하드웨어 위에 직접 상주 → 중간 계층이 없어 오버헤드가 작고 격리가 강함 (VMware ESXi, **KVM** (Kernel-based Virtual Machine), Xen, Hyper-V).
2. **Type 2 하이퍼바이저** (호스트형) : 운영체제 위의 응용 프로그램으로 실행 → 설치가 간편하나 호스트 OS를 경유하는 성능 손실 (VirtualBox, VMware Workstation).
3. CPU 가상화 : **VT-x** (Intel Virtualization Technology)와 **AMD-V** (AMD Virtualization)가 게스트의 특권 명령을 하드웨어가 가로채 하이퍼바이저에 전달 → 소프트웨어 번역 우회 비용 감소.
4. 메모리 가상화 : **EPT** (Extended Page Tables, Intel)·NPT(Nested Page Tables, AMD)가 게스트 물리 주소→호스트 물리 주소의 2단 변환을 하드웨어가 처리 → 소프트웨어 중계 지연 제거.
5. 입출력(I/O, Input/Output) 가상화 : **SR-IOV** (Single Root I/O Virtualization)가 물리 네트워크 카드를 여러 가상 기능(VF, Virtual Function)으로 분할 → 가상머신의 하이퍼바이저 우회 접근으로 네이티브 수준 성능.

## Ⅲ. 하이퍼바이저의 구조 (흐름)

- 핵심 요약 : 하드웨어 제어 경로의 길이가 Type 1과 Type 2의 본질적 차이이며, 경로가 짧을수록 성능과 격리가 강해지는 구조.

```text
[ Type 1 베어메탈 구조 ]

가상머신 1      가상머신 2
      ↓               ↓
Type 1 하이퍼바이저
      ↓
물리 하드웨어
```

```text
[ Type 2 호스트형 구조 ]

가상머신 1      가상머신 2
      ↓               ↓
Type 2 하이퍼바이저
      ↓
호스트 운영체제
      ↓
물리 하드웨어
```

- 구성요소 : 하이퍼바이저는 가상 CPU(vCPU) 스케줄러, 메모리 사상기, 가상 장치 에뮬레이터, 관리 인터페이스로 구성되며, 가상머신마다 독립된 커널과 가상 하드웨어를 배정.
- 동작 원리 : 게스트의 특권 명령은 하드웨어 가상화 기능에 의해 가로채어(trap) 하이퍼바이저가 대행하고, 일반 명령은 하드웨어에서 직접 실행되는 구조.

## Ⅳ. 하이퍼바이저와 컨테이너의 비교

- 핵심 요약 : Type 1·Type 2·컨테이너는 실행 계층의 깊이에 따라 성능·격리·운영체제 다양성이 달라지는 상호 보완 관계.

| 비교 항목 | Type 1 (ESXi, KVM) | Type 2 (VirtualBox) | 컨테이너 (Docker 등) |
| --- | --- | --- | --- |
| 실행 계층 | 하드웨어 직접 구동 | 호스트 OS 위의 응용 | 호스트 커널 공유 |
| 성능 오버헤드 | 낮음 | 중간 | 매우 낮음 |
| 격리 강도 | 하드웨어 수준 (강함) | 호스트 OS 의존 | 커널 공유로 상대적 약함 |
| 이종 OS 구동 | 가능 | 가능 | 같은 커널 계열만 가능 |
| 기동 속도 | 느림 | 보통 | 빠름 |

- 선택 기준 : 이종 운영체제와 강한 격리가 요구되면 가상머신을, 같은 커널 계열의 경량·고밀도 배포가 요구되면 컨테이너를 택하는 판단 기준.

## Ⅴ. 하이퍼바이저의 한계와 방안

- 핵심 요약 : 게스트별 메모리 중복, vCPU 경합, 벤더 종속을 페이지 병합·자원 배분 정책·오픈소스 전환으로 대응하는 원칙.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 메모리 중복 적재 | 가상머신마다 독립 커널·시스템 프로세스 적재로 동일 페이지 낭비 | **KSM** (Kernel Samepage Merging)으로 동일 내용 페이지 병합 | 호스트 메모리 사용률, 병합 페이지 수 |
| **노이지 네이버** (Noisy Neighbor) | 특정 가상머신의 CPU 과점유로 타 가상머신 스케줄 지연·스틸 타임(Steal Time) 증가 | vCPU 고정(Pinning)과 쿼터·Shares 기반 자원 배분 정책 | 스틸 타임 비율 |
| 벤더 종속과 라이선스 비용 | 상용 하이퍼바이저의 구독 정책 변화로 총소유비용(TCO, Total Cost of Ownership) 상승 | 오픈소스 KVM 기반 전환과 단계적 전환 로드맵 수행 | 라이선스 비용 추이 |

## Ⅵ. 하이퍼바이저에 대한 기술사적 제언

- 핵심 요약 : 컨테이너와 가상머신의 통합 제어면, 경량 가상머신의 서버리스 적용, 하드웨어 오프로드로 가상화 비용을 낮추는 방향.

1. 플랫폼 운영 조직은 **KubeVirt**(쿠버네티스 위에서 가상머신을 실행하는 확장)를 도입하여 컨테이너와 가상머신을 한 제어면에서 배포·관리하는 체계로 레거시 자산의 이전 부담을 낮춘다.
2. 서버리스·다중 테넌트 서비스 조직은 **MicroVM**(경량 가상머신, 예: Firecracker)으로 함수 실행 단위를 가상머신 경계로 감싸 격리와 기동 속도를 함께 확보한다.
3. 데이터센터 인프라 조직은 **DPU** (Data Processing Unit)로 가상 스위치·스토리지 처리를 호스트 CPU에서 분리하는 오프로드 구조를 표준 참조 설계에 반영한다.

## Ⅶ. 결론

- 핵심 요약 : 하이퍼바이저는 하드웨어 추상화로 격리·서버 통합·실시간 이전을 실현하는 가상화의 기반 계층.
- 격리를 얻는 대가로 계층 비용을 수반하는 기술이므로, 컨테이너와의 역할 분담 설계를 전제로 한 도입이 요구되는 구조.
