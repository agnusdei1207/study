---
title: "가상머신 (Virtual Machine)"
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

- 가상머신(Virtual Machine, VM), 하이퍼바이저(Hypervisor), Type 1, Type 2
- 게스트 OS, VT-x, EPT, 라이브 마이그레이션(Live Migration)
- 컨테이너, VM 스프롤, KSM, Virtio, SR-IOV, 마이크로VM, SDI

## Ⅰ. 가상머신(Virtual Machine)의 개요

- 핵심 요약 : **가상머신** (Virtual Machine, VM)은 물리 하드웨어를 추상화하는 가상화 계층 위에서 독립된 운영체제와 애플리케이션을 실행하는 소프트웨어 기반 컴퓨터 환경.
- 개념 : 하나의 물리 서버 위에서 **하이퍼바이저** (Hypervisor)라 불리는 가상화 계층(VMM, Virtual Machine Monitor)이 CPU, 메모리, 스토리지, 네트워크 자원을 추상화하여, 각자 **게스트 OS** (Guest OS)를 가진 독립 실행 환경을 생성하는 방식.
- 배경 및 필요성 : 물리 서버 한 대에 OS와 애플리케이션 하나만 올리는 전통 방식은 자원 이용률이 낮고, 상면과 전력이 낭비되며, 서버 증설에 걸리는 시간이 길어 이를 해소하기 위해 등장.
- 주요 목적 : 자원 통합(Server Consolidation)에 의한 TCO(Total Cost of Ownership) 절감, OS 수준의 격리, 신속한 프로비저닝, **라이브 마이그레이션** (Live Migration)을 통한 가용성 확보.

## Ⅱ. 가상머신(Virtual Machine)의 특징 및 장점

- 핵심 요약 : 하이퍼바이저의 설치 위치와 하드웨어 가상화 지원이 성능과 격리 수준을 함께 결정하는 구조.

1. **Type 1 하이퍼바이저** (Bare-Metal) : 호스트 OS 없이 하드웨어 위에 직접 설치 → 중간 계층이 없어 오버헤드가 적고 성능과 격리 수준이 높음 (VMware ESXi, KVM, Xen 등).
2. **Type 2 하이퍼바이저** (Hosted) : 기존 OS 위에서 일반 프로세스처럼 실행 → 설치와 사용이 간편하나 호스트 OS를 경유하므로 성능 손실 발생 (VirtualBox, VMware Workstation 등).
3. 하드웨어 지원 CPU 가상화 : Intel VT-x, AMD-V가 루트/비루트 모드(VMX Root/Non-Root Mode)를 제공 → 게스트의 특권 명령으로 발생하는 VM-Exit를 하드웨어가 처리하여 트랩 오버헤드 감소.
4. 메모리 가상화 : SLAT(Second Level Address Translation) 방식의 Intel EPT(Extended Page Tables)가 게스트 가상 주소를 호스트 물리 주소로 변환하는 이중 주소 변환을 하드웨어에서 수행 → 소프트웨어 변환 부담 감소.

## Ⅲ. 가상머신(Virtual Machine)의 구조 및 동작 메커니즘

- 핵심 요약 : Type 1은 하드웨어 위에 하이퍼바이저가 직접 올라가고, Type 2는 호스트 OS 위에 하이퍼바이저가 올라가는 계층 차이.

```text
[ Type 1 : 베어메탈 하이퍼바이저 ]

게스트 VM (Guest OS + App) × N
      ↓
하이퍼바이저 (ESXi, KVM, Xen, Hyper-V)
      ↓
물리 하드웨어 (CPU VT-x, 메모리, NIC)
```

```text
[ Type 2 : 호스티드 하이퍼바이저 ]

게스트 VM (Guest OS + App) × N
      ↓
하이퍼바이저 (VirtualBox, VMware Workstation)
      ↓
호스트 운영체제 (Host OS)
      ↓
물리 하드웨어
```

## Ⅳ. 가상머신(Virtual Machine)의 비교

- 핵심 요약 : VM은 하드웨어 수준의 강한 격리를, 컨테이너는 커널을 공유하는 가벼운 기동을 택한 방식으로 서로 적용 영역이 다름.

| 비교 항목 | 가상머신 (Virtual Machine) | 컨테이너 (Container) |
| :--- | :--- | :--- |
| 가상화 수준 | 하드웨어 추상화 | 운영체제 커널 수준 격리 |
| 게스트 OS | 각 VM마다 독립 게스트 OS 필요 | 호스트 커널 공유, 별도 게스트 OS 없음 |
| 격리 수준 | 하드웨어 수준의 강한 격리 | namespaces, cgroups 기반 논리적 격리 |
| 기동 속도 | OS 부팅 과정이 필요해 상대적으로 느림 | 프로세스 기동 수준으로 빠름 |
| 자원 오버헤드 | 게스트 OS만큼 메모리와 디스크 점유 | 프로세스 수준 자원만 소모, 높은 집적도 |
| 실행 엔진 | VMware ESXi, KVM, Hyper-V | Docker, containerd, Podman |
| 적합 영역 | 레거시 모놀리식 시스템, 이종 OS 혼합, 높은 격리 요구 | 마이크로서비스(MSA, Microservice Architecture), CI/CD(Continuous Integration/Continuous Delivery) 파이프라인, 웹 스케일 서비스 |

## Ⅴ. 가상머신(Virtual Machine)의 한계와 방안

- 핵심 요약 : 자원 중복, I/O 오버헤드, VM 스프롤을 메모리 병합, 장치 직접 할당, 수명주기 관리로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| **자원 중복** (이중 OS 계층) | VM마다 커널과 시스템 데몬이 중복 적재되어 메모리와 디스크 낭비 | KSM(Kernel Samepage Merging)으로 동일 메모리 페이지 병합, 씬 프로비저닝(Thin Provisioning) 적용, 애플리케이션 계층은 컨테이너로 점진 전환 | 호스트 메모리 활용률 |
| **I/O 가상화 오버헤드** | 가상 디스크와 가상 NIC(Network Interface Card) 접근이 에뮬레이션 경로를 거쳐 처리율 저하 | 반가상화 드라이버 Virtio 도입, SR-IOV(Single Root I/O Virtualization)로 장치를 VM에 직접 할당 | VM별 I/O 지연 시간 |
| **VM 스프롤** (VM Sprawl) | 테스트 후 방치된 VM이 누적되어 컴퓨팅 자원과 라이선스 비용 잠식 | 클라우드 관리 플랫폼(CMP, Cloud Management Platform) 도입, TTL(Time to Live) 기반 만료 정책과 승인 기반 생성 워크플로 | 미사용 VM 비율 |

## Ⅵ. 가상머신(Virtual Machine)에 대한 기술사적 제언

- 핵심 요약 : 경량 마이크로VM으로 VM의 격리와 컨테이너의 기동 속도를 결합하고, 인프라 수명주기를 코드로 관리하는 방향.

1. 다중 테넌트 워크로드를 다루는 플랫폼 조직은 Firecracker나 Kata Containers 같은 마이크로VM 기술을 검토하여, 하드웨어 수준의 격리를 유지하면서 컨테이너에 가까운 빠른 기동을 확보하는 방안을 우선 평가.
2. VM, 가상 네트워크, 가상 스토리지가 반복적으로 생성되고 폐기되는 환경에서는 인프라 조직이 이를 IaC(Infrastructure as Code)로 기술하고 승인 절차를 코드 리뷰와 연결하여, 소프트웨어 정의 인프라(SDI, Software-Defined Infrastructure)의 통제력을 확보.

## Ⅶ. 결론

- 핵심 요약 : 가상머신은 하드웨어 추상화로 OS 수준의 격리와 라이브 마이그레이션을 실현하는 기술이나, 자원 중복과 I/O 오버헤드, VM 스프롤의 관리가 필수.
- 시사점 : 격리와 레거시 호환이 중요한 영역에서는 여전히 기본 단위로 쓰이며, 컨테이너와 공존하는 계층 설계가 효율의 핵심이 됨.
